"use strict";
const fs=require("fs"),vm=require("vm"),path=require("path");
const project=path.resolve(__dirname,"../.."),root={};root.globalThis=root;
vm.runInNewContext(fs.readFileSync(path.join(project,"src/app/core/recovery.js"),"utf8"),root);
const fields=["name","dose","frequency","purpose","duration","status","benefit"];
const byId={
 CHOICE:{type:"choice",choiceCodes:["A","B"],multi:false,incompatible:[],safetyRequired:false},
 TEXT:{type:"shortText",choiceCodes:[],safetyRequired:false},
 MED:{type:"medicineList",choiceCodes:[],safetyRequired:false},
 SAFE:{type:"choice",choiceCodes:["Y","N"],multi:false,safetyRequired:true},
};
const opts={byId,optionalIds:["02"],legacyOpeningGroups:["02"],layoutVersion:"layout-v1",medicineFields:fields,
 choiceStatus:(q,codes)=>codes.includes("A")?"uncertain":"answered",
 incompatiblePair:(q,codes)=>q.incompatible?.find(([a,b])=>codes.includes(a)&&codes.includes(b)),
 isSafety:q=>!!q.safetyRequired};
const payload={schema:"mental-pilot-recovery-v1",layoutVersion:"layout-v1",version:"synthetic",lang:"en",selected:["02"],sectionConfirmed:true,
 currentId:"CHOICE",savedCount:4,reviewQueue:["SAFE"],reviewReturn:{screen:"results",id:"CHOICE"},
 answers:{CHOICE:{kind:"choice",codes:["B"]},TEXT:{kind:"text",value:"synthetic"},MED:{kind:"medicine",records:[{name:"example",dose:"",frequency:"",purpose:"",duration:"",status:"current",benefit:""}],discussion:""},SAFE:{kind:"skip"}},
 feedback:{CHOICE:{reasons:["question","answer:A"],comment:"synthetic note",language:"en",version:"synthetic",updatedAt:"now"}}};
const clean=root.QuestionnaireRecovery.validate(payload,opts);
assert(clean.answers.CHOICE.status==="answered"&&clean.answers.CHOICE.codes[0]==="B","normalizes coded answers");
assert(clean.answers.TEXT.value==="synthetic"&&clean.answers.MED.records[0].name==="example","normalizes text and medicine records");
assert(clean.answers.SAFE.kind==="skip"&&clean.feedback.CHOICE.reasons.length===2,"preserves skip and feedback records");
assert(clean.selected[0]==="02"&&clean.reviewQueue[0]==="SAFE"&&clean.reviewReturn.screen==="results","restores selection and safety review state");
assert(clean.currentId==="SAFE"&&clean.savedCount===4&&clean.lang==="en","restores navigation metadata");

const legacy=root.QuestionnaireRecovery.validate({schema:"mental-pilot-recovery-v1",answers:{}},opts);
assert(legacy.selected[0]==="02","migrates legacy implicit section selection");
const groupedOptions={...opts,optionalIds:["S01"],layoutVersion:"grouped-v1",previousLayoutVersions:["old-layout"],selectedModuleMap:{"01":"S01"},legacyOpeningGroups:[]};
const grouped=root.QuestionnaireRecovery.validate({schema:"mental-pilot-recovery-v1",layoutVersion:"old-layout",answers:{},selected:["01"]},groupedOptions);
assert(grouped.selected[0]==="S01","maps a prior source-module selection into its new grouped section");
rejectWith({...{schema:"mental-pilot-recovery-v1",layoutVersion:"old-layout",answers:{},selected:["99"]}},groupedOptions,"unknown legacy section");
reject({...payload,layoutVersion:"other"},"unsupported layout");
reject({...payload,answers:{CHOICE:{kind:"choice",codes:["UNKNOWN"]}}},"unknown answer code");
reject({...payload,feedback:{CHOICE:{reasons:["answer:unknown"],comment:"",language:"en",version:"v",updatedAt:""}}},"unknown feedback answer code");
reject({...payload,reviewQueue:["CHOICE"]},"non-safety review item");
console.log("PASS: synthetic recovery normalization, legacy compatibility, and invalid-data rejection.");

function assert(value,message){if(!value)throw new Error(message);}
function reject(value,message){let rejected=false;try{root.QuestionnaireRecovery.validate(value,opts);}catch(e){rejected=true;}assert(rejected,"rejects "+message);}
function rejectWith(value,options,message){let rejected=false;try{root.QuestionnaireRecovery.validate(value,options);}catch(e){rejected=true;}assert(rejected,"rejects "+message);}
