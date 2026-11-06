/* Validate and normalize recovery files without DOM or application state. */
(function (root) {
"use strict";
root.QuestionnaireRecovery = {
 validate(payload,options){
  const {byId,optionalIds,legacyOpeningGroups,layoutVersion,medicineFields,choiceStatus,incompatiblePair,isSafety}=options;
  const x=payload;
  if(!x||x.schema!=="mental-pilot-recovery-v1"||!x.answers||typeof x.answers!=="object"||Array.isArray(x.answers))throw Error("Invalid schema");
  if(x.layoutVersion&&x.layoutVersion!==layoutVersion)throw Error("Unsupported layout");
  const answers={};
  for(const [id,record] of Object.entries(x.answers)){
   const q=byId[id];if(!q||!record||typeof record!=="object"||Array.isArray(record))throw Error("Invalid record");
   if(record.kind==="choice"){
    if(q.type==="shortText"||q.type==="medicineList"||!Array.isArray(record.codes)||!record.codes.length||new Set(record.codes).size!==record.codes.length||!record.codes.every(code=>q.choiceCodes.includes(code)))throw Error("Unknown choice");
    if((!q.multi&&record.codes.length!==1)||(q.maxChoices&&record.codes.length>q.maxChoices)||(record.codes.length>1&&record.codes.some(code=>q.exclusive?.includes(code))))throw Error("Invalid single answer");
    if(incompatiblePair(q,record.codes))throw Error("Incompatible answers");
    answers[id]={kind:"choice",codes:[...record.codes],status:choiceStatus(q,record.codes),savedAt:record.savedAt||""};
   }else if(record.kind==="text"){
    if(q.type!=="shortText"||typeof record.value!=="string")throw Error("Invalid text");
    answers[id]={kind:"text",value:record.value.slice(0,200),status:"answered",savedAt:record.savedAt||""};
   }else if(record.kind==="medicine"){
    if(q.type!=="medicineList"||!Array.isArray(record.records)||record.records.length>50||typeof record.discussion!=="string"||record.discussion.length>3000)throw Error("Invalid medicine list");
    const statuses=new Set(["current","past","unknown"]),benefits=new Set(["","A","B","C","D","E","F","G"]);
    const records=record.records.map(item=>{
     if(!item||typeof item!=="object"||Array.isArray(item)||Object.keys(item).sort().join(",")!==medicineFields.slice().sort().join(",")||
        !medicineFields.every(key=>typeof item[key]==="string"&&item[key].length<=1000)||
        !statuses.has(item.status)||!benefits.has(item.benefit)||!medicineFields.some(key=>key!=="status"&&item[key].trim()))throw Error("Invalid medicine record");
     return Object.fromEntries(medicineFields.map(key=>[key,item[key]]));
    });
    if(!records.length&&!record.discussion.trim())throw Error("Empty medicine list");
    answers[id]={kind:"medicine",status:"answered",records,discussion:record.discussion,savedAt:record.savedAt||""};
   }else if(record.kind==="skip")answers[id]={kind:"skip",status:"skipped",savedAt:record.savedAt||""};
   else throw Error("Unknown record");
  }
  const feedback=x.feedback==null?{}:x.feedback;
  if(!feedback||typeof feedback!=="object"||Array.isArray(feedback))throw Error("Invalid feedback");
  const restoredFeedback={};
  for(const [id,record] of Object.entries(feedback)){
   const q=byId[id];
   if(!q||!record||typeof record!=="object"||Array.isArray(record)||!Array.isArray(record.reasons)||!record.reasons.length||new Set(record.reasons).size!==record.reasons.length)throw Error("Invalid feedback record");
   const valid=new Set(["question","language","other",...q.choiceCodes.map(code=>"answer:"+code)]);
   if(!record.reasons.every(reason=>typeof reason==="string"&&valid.has(reason))||typeof record.comment!=="string"||record.comment.length>500||
      !["lv","en","ru"].includes(record.language)||typeof record.version!=="string"||record.version.length>40||typeof record.updatedAt!=="string")throw Error("Invalid feedback details");
   restoredFeedback[id]={reasons:[...record.reasons],comment:record.comment,language:record.language,version:record.version,updatedAt:record.updatedAt};
  }
  if(x.selected!=null&&(!Array.isArray(x.selected)||x.selected.some(id=>!optionalIds.includes(id))))throw Error("Recovery file requires an unavailable section");
  const queue=x.reviewQueue;
  if(queue!=null&&(!Array.isArray(queue)||new Set(queue).size!==queue.length||queue.some(id=>!byId[id]||!isSafety(byId[id]))))throw Error("Invalid review sequence");
  const selectedIds=Array.isArray(x.selected)?x.selected:[];
  const selected=optionalIds.filter(id=>selectedIds.includes(id)||(!x.layoutVersion&&legacyOpeningGroups.includes(id)));
  const reviewQueue=queue?.length?[...queue]:null;
  const currentId=reviewQueue?reviewQueue[0]:(typeof x.currentId==="string"&&byId[x.currentId]?x.currentId:null);
  return {
   answers,feedback:restoredFeedback,selected,sectionConfirmed:!!x.sectionConfirmed,
   reviewQueue,
   reviewReturn:reviewQueue&&["question","report","results"].includes(x.reviewReturn?.screen)?{screen:x.reviewReturn.screen,id:x.reviewReturn.id}:null,
   savedCount:Number.isInteger(x.savedCount)&&x.savedCount>=0?x.savedCount:Object.keys(answers).length,
   lang:["lv","en","ru"].includes(x.lang)?x.lang:null,currentId
  };
 }
};
})(globalThis);
