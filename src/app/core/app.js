/* Offline questionnaire: shared interface and runtime, separate question content. */
(function () {
"use strict";
const embedded=document.getElementById("questionnaire-data");
const data=JSON.parse(embedded.textContent);
const model=window.QuestionnaireModel.create(data);
const flow=window.QuestionnaireFlow;
const {groups,optionalIds,byId,all}=model;
// Registry display order is independent of frozen source order.
let pendingSingleAnswer=null;
const app=document.getElementById("app");
const report=window.QuestionnaireReports;
let state={lang:"lv",screen:"start",currentId:null,answers:{},feedback:{},feedbackOpen:false,selected:[],sectionDraft:[],sectionConfirmed:false,pendingSectionEnd:null,notice:"",draft:null};
function ui(){return data.ui[state.lang];}
function esc(s){return report.esc(s);}
function label(key){return esc(ui()[key]||key);}
function btn(act,key,cls,extra){return '<button type="button" data-act="'+act+'" class="'+(cls||"")+'" '+(extra||"")+'>'+label(key)+'</button>';}
function canSkip(q){return !!q;}
function questionVisible(q){return model.questionVisible(state,q);}
function reportQuestions(){return model.reportQuestions(state);}
function active(){return model.active(state);}
function current(){return model.current(state);}
function isSafety(q){return model.isSafety(q);}
function countGroup(group){return model.countGroup(state,group);}
function header(){
 const opts=["lv","en","ru"].map(id=>'<option value="'+id+'"'+(id===state.lang?" selected":"")+">"+({lv:"Latviešu",en:"English",ru:"Русский"}[id])+"</option>").join("");
 return '<header>'+(state.screen==="start"?'<h1>'+label("project")+'</h1>':"")+'<label class="lang">'+label("language")+' <select id="language">'+opts+'</select></label></header>';
}
function supportLinks(includeEmergency){
 const line='<a href="tel:116123">'+label("supportLink")+'</a>';
 return line+(includeEmergency?'<p>'+label("emergencyBody")+' <a href="tel:112">112</a></p>':"");
}
function supportCard(){
 if(!state.support)return "";
 return '<aside id="support-message" class="support-card" role="status" aria-live="polite" tabindex="-1"><h2>'+label("supportTitle")+'</h2>'+supportLinks(state.support==="emergency")+'<p>'+label("supportBody")+'</p>'+btn("dismissSupport","dismissSupport")+'</aside>';
}
function offerSupport(q,codes){
 const rules=data.presentation.questions[q.id]?.support||{};
 const levels=codes.map(c=>rules[c]).filter(Boolean);
 const level=levels.includes("emergency")?"emergency":levels.length?"support":null;
 if(!level)return;
 state.supportSeen=state.supportSeen||[];
 if(!state.supportSeen.includes(level)){
  state.support=level;state.supportSeen.push(level);
  if(level==="emergency"&&!state.supportSeen.includes("support"))state.supportSeen.push("support");
  state.focusSupport=true;
 }
}
function navigation(){
 return state.screen==="question"?'<nav class="question-nav" aria-label="'+label("progress")+'">'+btn("previous","prev")+btn("skip","skipQuestion")+btn("support","supportMenu")+'</nav>':"";
}
function toolbar(){
 return '<nav class="toolbar" aria-label="Tools">'+btn("backup","saveBackup")+'<small class="backup-note">'+label("backupWarning")+'</small><label class="file-label">'+label("restoreBackup")+'<input id="restore" type="file" accept=".json,application/json" aria-label="'+label("restoreBackup")+'"></label>'+btn("results","results")+btn("sections","editSections")+'</nav>';
}
function footer(){
 return '<footer><details><summary>'+label("tools")+'</summary>'+toolbar()+'</details><details id="support-details"><summary>'+label("supportMenu")+'</summary><p>'+label("supportBody")+'</p>'+supportLinks()+'</details><details><summary>'+label("guideTitle")+'</summary><p>'+label("guideBody")+'</p></details><details><summary>'+label("notesTitle")+'</summary><p>'+label("notesBody")+'</p></details><details><summary>'+label("legal")+'</summary>'+ui().legalBody.split("\n\n").map(text=>'<p>'+esc(text)+'</p>').join("")+'</details><details><summary>'+label("helpers")+'</summary><p>'+label("credits")+'</p></details><p class="muted">'+label("statusNote")+' · '+label("footer")+'</p></footer>';
}
function renderStart(){
 return window.QuestionnaireScreens.start({label,btn});
}
function renderSelector(){
 return window.QuestionnaireScreens.sectionSelector({state,data,countGroup,active,groups,escape:esc,label,btn});
}
function storedDraft(q){
 const r=state.answers[q.id];
 if(r?.kind==="choice")return {codes:[...r.codes]};
 if(r?.kind==="text")return {value:r.value||""};
 if(r?.kind==="medicine")return {records:r.records.map(x=>({...x})),discussion:r.discussion||""};
 if(q.type==="medicineList")return {records:[blankMedicine()],discussion:""};
 return {codes:[],value:""};
}
const medicineFields=Object.keys(data.ui.lv.medicine.fields);
function blankMedicine(){return Object.fromEntries(medicineFields.map(k=>[k,k==="status"?"current":""]));}
function renderMedicine(){
 return window.QuestionnaireScreens.medicine({medicine:ui().medicine,draft:state.draft,medicineFields,escape:esc});
}
function readMedicineControls(){
 const q=current();if(q?.type!=="medicineList"||!state.draft)return;
 app.querySelectorAll('[data-med-index][data-med-field]').forEach(el=>{
  const i=Number(el.dataset.medIndex),key=el.dataset.medField;
  if(state.draft.records[i]&&medicineFields.includes(key))state.draft.records[i][key]=el.value;
 });
 state.draft.discussion=document.getElementById("medicineDiscussion")?.value||state.draft.discussion||"";
}
function changeMedicineList(actionName,index){
 readMedicineControls();const d=state.draft,m=ui().medicine;
 if(actionName==="addMedicine"){
  if(d.records.length>=50){state.notice=m.limit;render();return;}
  d.records.push(blankMedicine());
 }else{
  d.records.splice(index,1);if(!d.records.length)d.records.push(blankMedicine());
 }
 render();
}
function cleanMedicineDraft(){
 readMedicineControls();const m=ui().medicine;
 const records=state.draft.records.map(r=>Object.fromEntries(medicineFields.map(k=>[k,(r[k]||"").trim().slice(0,1000)])))
  .filter(r=>medicineFields.some(k=>k!=="status"&&r[k]));
 const discussion=(state.draft.discussion||"").trim().slice(0,3000);
 return {records,discussion,valid:records.length>0||!!discussion};
}
function renderFeedback(q,t){
 return window.QuestionnaireScreens.feedback({q,t,state,ui:ui(),label,escape:esc,btn});
}
function renderQuestion(){
 const q=current(),u=ui();
 if(!q){state.screen="results";return renderResults();}
 if(!state.draft || state.draft.forId!==q.id)state.draft={forId:q.id,...storedDraft(q)};
 const queue=active();
 const group=groups.get(q.module).titles[state.lang];
 return window.QuestionnaireScreens.question({
  q,state,ui:u,queue,group,escape:esc,label,btn,
  renderFeedback:()=>renderFeedback(q,q.translations[state.lang]),renderMedicine,
 });
}
function renderResults(){
 const qs=reportQuestions(),v=report.counters(qs,state.answers);
 v.completed=v.answered+v.skipped;
 const selected="";
 const feedbackText=report.projectFeedbackText(all,state.feedback,state.lang,data.ui,data.presentation.feedbackContactEmail,data.version);
 return window.QuestionnaireScreens.results({
  label,escape:esc,btn,counts:v,selected,feedbackText,feedbackEmail:data.presentation.feedbackContactEmail,
 });
}
function renderReport(){
 const q=reportQuestions(),u=ui();
 const plain=report.doctorText(q,state.answers,state.selected,state.lang,u,data.groups,data.presentation,state.feedback,all,data.ui);
 const markup=report.doctorMarkup(q,state.answers,state.selected,state.lang,u,data.groups,data.presentation,state.feedback,all,data.ui);
 return window.QuestionnaireScreens.reportPage({heading:u.doctorHeading,markup,plain,escape:esc,label,btn});
}
function renderSectionComplete(){
 return '<section class="card"><h2>'+label("sectionCompleteTitle")+'</h2><p>'+label("sectionCompleteBody")+'</p>'+btn("saveAndContinue","saveAndContinue","primary")+btn("continueWithoutSaving","continueWithoutSaving")+'</section>';
}
function render(){
 const keepSupportFocus=document.activeElement?.id==="support-message";
 document.documentElement.lang=state.lang;
 document.title=ui().project;
 const body=state.screen==="start"?renderStart():state.screen==="selector"?renderSelector():state.screen==="question"?renderQuestion():state.screen==="sectionComplete"?renderSectionComplete():state.screen==="report"?renderReport():renderResults();
 app.innerHTML='<main>'+header()+supportCard()+(state.notice?'<p role="status" class="notice">'+esc(state.notice)+'</p>':"")+body+(state.screen==="sectionComplete"?"":footer())+navigation()+'</main>';
 if(state.focusSupport||keepSupportFocus){document.getElementById('support-message')?.focus({preventScroll:true});state.focusSupport=false;}
}
function clearPendingSingleAnswer(){if(pendingSingleAnswer)clearTimeout(pendingSingleAnswer.timer);pendingSingleAnswer=null;}
function setQuestion(id){clearPendingSingleAnswer();state.currentId=id;state.pendingSectionEnd=null;state.draft=null;state.feedbackOpen=false;state.screen="question";state.notice="";render();window.scrollTo(0,0);}
function advance(){
 const destination=flow.next(state,active());
 if(destination.id){setQuestion(destination.id);return;}
 state.screen=destination.screen;state.currentId=destination.currentId;state.draft=null;state.notice="";render();window.scrollTo(0,0);
}
function start(){
 showSections(state.sectionConfirmed?[...state.selected]:[]);
}
function choiceStatus(q,codes){
 const statuses=codes.map(c=>q.answerStatus?.[c]);
 return statuses.includes("refused")?"refused":statuses.includes("uncertain")?"uncertain":"answered";
}
function advanceAfterSave(){
 const wasReviewing=!!state.reviewQueue,finished=current();
 const destination=flow.afterSave(state,active());
 const next=destination.id&&byId[destination.id];
 if(!wasReviewing&&finished&&(destination.screen==="results"||(next&&next.module!==finished.module))){
  state.pendingSectionEnd=destination;state.screen="sectionComplete";state.draft=null;state.notice="";render();window.scrollTo(0,0);return;
 }
 if(destination.id){setQuestion(destination.id);return;}
 state.currentId=destination.currentId;state.screen=destination.screen;state.draft=null;
 if(destination.clearNotice)state.notice="";
 render();if(destination.scroll)window.scrollTo(0,0);
}
function incompatiblePair(q,codes){
 return (q.incompatible||[]).find(([a,b])=>codes.includes(a)&&codes.includes(b));
}
function save(){
 const q=current();if(!q)return;
 let rec={savedAt:new Date().toISOString()};
 if(q.type==="medicineList"){
   const cleaned=cleanMedicineDraft();
   if(!cleaned.valid){state.notice=ui().medicine.empty;render();return;}
   rec.kind="medicine";rec.status="answered";rec.records=cleaned.records;rec.discussion=cleaned.discussion;
 } else if(q.type==="shortText"){
   rec.kind="text";rec.value=document.getElementById("shortText")?.value.trim().slice(0,200)||"";rec.status="answered";
   if(!rec.value){skip();return;}
 } else {
   const codes=(state.draft?.codes||[]).filter(key=>q.choiceCodes.includes(key));
   if(!codes.length){state.notice=ui().chooseAnswer;render();return;}
   if(q.maxChoices&&codes.length>q.maxChoices){state.notice=ui().maxChoices+" "+q.maxChoices;render();return;}
   const pair=incompatiblePair(q,codes);
   if(pair){state.notice=ui().incompatibleAnswers+" "+pair.join(" + ");render();return;}
   rec.kind="choice";rec.codes=codes;rec.status=choiceStatus(q,codes);
 }
 state.answers[q.id]=rec;
 if(rec.kind==="choice")offerSupport(q,rec.codes);
 advanceAfterSave();
}
function skip(){
 clearPendingSingleAnswer();
 const q=current();if(!q||!canSkip(q))return;
 state.answers[q.id]={kind:"skip",savedAt:new Date().toISOString(),status:"skipped"};
 advanceAfterSave();
}
function previous(){const destination=flow.previous(state,active());if(destination.id)setQuestion(destination.id);else {state.screen=destination.screen;render();}}
function skipSection(){
 const q=current();if(!q||groups.get(q.module).required)return;
 if(!window.confirm(ui().skipConfirm))return;
 for(const item of all.filter(x=>x.module===q.module&&questionVisible(x))){
  if(!state.answers[item.id])state.answers[item.id]={kind:"skip",savedAt:new Date().toISOString(),status:"skipped"};
 }
 const next=active().find(x=>x.module!==q.module&&all.indexOf(x)>all.indexOf(q));
 if(next)setQuestion(next.id);else{state.screen="results";render();}
}
function skipRest(){if(window.confirm(ui().restConfirm)){state.screen="results";state.draft=null;render();}}
function showSections(m){state.screen="selector";state.sectionDraft=m?[...m]:[...state.selected];state.draft=null;render();}
function confirmSections(){
 if(!state.sectionDraft.length){state.notice=ui().noSectionsSelected;render();return;}
 state.selected=optionalIds.filter(id=>state.sectionDraft.includes(id));state.sectionConfirmed=true;
 state.screen="question";
 const first=active().find(q=>!state.answers[q.id]);
 if(first)setQuestion(first.id);else {state.screen="results";render();}
}
function setDraft(ev){
 const q=current();if(!q||q.type==="shortText"||q.type==="medicineList")return;
 const inp=ev.target;if(inp.name!=="answer")return;
 let codes=(state.draft?.codes||[]).slice();
 if(!q.multi){codes=[inp.value];}else{
  if(inp.checked){
    if((q.exclusive||"").includes(inp.value))codes=[inp.value];
    else{codes=codes.filter(c=>!(q.exclusive||"").includes(c));if(!codes.includes(inp.value))codes.push(inp.value);}
  }else codes=codes.filter(c=>c!==inp.value);
  if(q.maxChoices&&codes.length>q.maxChoices){state.notice=ui().maxChoices+" "+q.maxChoices;codes=codes.filter(c=>c!==inp.value);}
 }
 state.draft={forId:q.id,codes};
 if(q.multi){
  app.querySelectorAll('input[name="answer"]').forEach(el=>el.checked=codes.includes(el.value));
  const message=app.querySelector('.notice');if(message)message.textContent=state.notice;
 }
}
function downloadFile(name,contents,mime){
 const blob=new Blob([contents],{type:mime||"text/plain;charset=utf-8"});
 const href=URL.createObjectURL(blob),link=document.createElement("a");link.href=href;link.download=name;document.body.appendChild(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(href),1500);
}
function downloadBackup(){
 const payload={schema:"mental-pilot-recovery-v1",version:data.version,layoutVersion:data.layout_version,lang:state.lang,selected:[...state.selected],sectionConfirmed:state.sectionConfirmed,currentId:state.currentId,answers:state.answers,feedback:state.feedback,reviewQueue:state.reviewQueue||null,reviewReturn:state.reviewReturn||null,exportedAt:new Date().toISOString()};
 downloadFile("questionnaire-recovery.json",JSON.stringify(payload,null,2),"application/json");
}
function continueAfterSection(shouldSave){
 const destination=state.pendingSectionEnd;if(!destination)return;
 if(shouldSave){if(destination.id)state.currentId=destination.id;downloadBackup();}
 state.pendingSectionEnd=null;
 state.notice=shouldSave?ui().backupSaved:"";
 if(destination.id){state.currentId=destination.id;state.draft=null;state.feedbackOpen=false;state.screen="question";render();window.scrollTo(0,0);return;}
 state.currentId=destination.currentId??state.currentId;state.screen=destination.screen||"results";state.draft=null;render();window.scrollTo(0,0);
}
function restore(file){
 if(!file)return;
 const reader=new FileReader();
 reader.onload=function(){
  try{
   const x=JSON.parse(String(reader.result));
   const restored=window.QuestionnaireRecovery.validate(x,{byId,optionalIds,legacyOpeningGroups:data.legacy_opening_groups,
    layoutVersion:data.layout_version,previousLayoutVersions:data.previous_layout_versions,
    selectedModuleMap:data.source_module_to_section,medicineFields,choiceStatus,incompatiblePair,isSafety});
   if((Object.keys(state.answers).length||Object.keys(state.feedback).length)&&!window.confirm(ui().replaceSession))return;
   state.reviewQueue=restored.reviewQueue;
   state.reviewReturn=restored.reviewReturn;
   state.answers=restored.answers;
   state.feedback=restored.feedback;state.feedbackOpen=false;
   state.selected=restored.selected;
   state.sectionConfirmed=restored.sectionConfirmed;
   state.support=null;state.supportSeen=[];
   if(restored.lang)state.lang=restored.lang;
   state.currentId=restored.currentId;
   if(state.reviewQueue)state.currentId=state.reviewQueue[0];
   const pending=active().find(q=>groups.get(q.module).required&&!state.answers[q.id]);
   if(pending&&state.currentId&&!groups.get(byId[state.currentId].module).required)
     state.currentId=pending.id;
   if(!active().some(q=>q.id===state.currentId))state.currentId=active().find(q=>!state.answers[q.id])?.id||null;
   state.screen=state.currentId?"question":"start";state.draft=null;state.notice=ui().restoreOK;render();
  }catch(err){state.notice=ui().restoreError;render();}
 };
 reader.onerror=function(){state.notice=ui().restoreError;render();};
 reader.readAsText(file,"utf-8");
}
async function copyText(text,sourceId="reportText"){
 const area=document.getElementById(sourceId);
 if(area){area.value=text;area.focus();area.select();}
 try{
  if(navigator.clipboard&&navigator.clipboard.writeText){await navigator.clipboard.writeText(text);state.notice=ui().copied;}
  else if(area&&document.execCommand("copy"))state.notice=ui().copied;
  else state.notice=ui().copyFailure;
 }catch(e){state.notice=ui().copyFailure;}
 const target=document.querySelector('.notice');
 if(target)target.textContent=state.notice;else{const p=document.createElement("p");p.role="status";p.className="notice";p.textContent=state.notice;app.querySelector("header").after(p);}
}
function action(key){
 if(["skip","previous","skipSection","end","sections","results","doctor","resultScreen","back","reviewSafety","new","feedbackContinue"].includes(key))clearPendingSingleAnswer();
 const q=reportQuestions(),u=ui();
 if(key==="support"){state.support="support";state.focusSupport=true;render();window.scrollTo(0,0);return;}
 if(key==="dismissSupport"){state.support=null;render();return;}
 if(key==="start"){start();return;}
 if(key==="all"){state.sectionDraft=[...optionalIds];confirmSections();return;}
 if(key==="confirm"){confirmSections();return;}
 if(key==="cancel"){state.screen=state.currentId?"question":"start";render();return;}
 if(key==="save"){save();return;}
 if(key==="saveAndContinue"){continueAfterSection(true);return;}
 if(key==="continueWithoutSaving"){continueAfterSection(false);return;}
 if(key==="feedback"){state.feedbackOpen=!state.feedbackOpen;state.notice="";render();return;}
 if(key==="feedbackContinue"){
  const currentQuestion=current();if(!currentQuestion)return;
  const reasons=Array.from(app.querySelectorAll('[data-feedback-reason]:checked'),el=>el.dataset.feedbackReason);
  if(!reasons.length){state.notice=ui().feedbackChooseReason;render();return;}
  const comment=(document.getElementById("feedback-comment")?.value||"").trim().slice(0,500);
  state.feedback[currentQuestion.id]={reasons,comment,language:state.lang,version:data.version,updatedAt:new Date().toISOString()};
  state.feedbackOpen=false;state.notice="";
  if(!state.answers[currentQuestion.id])state.answers[currentQuestion.id]={kind:"skip",savedAt:new Date().toISOString(),status:"skipped"};
  advanceAfterSave();
  return;
 }
 if(key==="removeFeedback"){
  if(current())delete state.feedback[state.currentId];state.feedbackOpen=false;state.notice="";render();return;
 }
 if(key==="skip"){skip();return;}
 if(key==="previous"){previous();return;}
 if(key==="skipSection"){skipSection();return;}
 if(key==="end"){skipRest();return;}
 if(key==="sections"){showSections();return;}
 if(key==="results"){state.screen="results";render();return;}
 if(key==="doctor"){state.screen="report";render();return;}
 if(key==="resultScreen"){state.screen="results";render();return;}
 if(key==="back"){state.screen=state.currentId?"question":"start";render();return;}
 if(key==="reviewSafety"){const safety=active().filter(isSafety);if(safety.length){
   state.reviewQueue=safety.map(q=>q.id);
   state.reviewReturn={screen:state.screen,id:state.currentId};
   setQuestion(state.reviewQueue[0]);
  }return;}
 if(key==="new"){
   if(window.confirm(u.newConfirm)){
     const lang=state.lang;state={lang,screen:"start",currentId:null,answers:{},feedback:{},feedbackOpen:false,selected:[],sectionDraft:[],sectionConfirmed:false,notice:"",draft:null};render();
   }return;
 }
 if(key==="backup"){downloadBackup();state.notice=u.backupSaved;render();return;}
 if(key==="downloadReport"){downloadFile("questionnaire-report-"+state.lang+".html",report.doctorHtml(q,state.answers,state.selected,state.lang,u,data.groups,data.presentation,state.feedback,all,data.ui),"text/html;charset=utf-8");return;}
 if(key==="print"){
   if(state.screen!=="report"){state.reportView="doctor";state.screen="report";render();}
   window.print();return;
 }
 if(key==="copyDoctor"){
   copyText(report.doctorText(q,state.answers,state.selected,state.lang,u,data.groups,data.presentation,state.feedback,all,data.ui));return;
 }
 if(key==="copyFeedback"){
   copyText(report.projectFeedbackText(all,state.feedback,state.lang,data.ui,data.presentation.feedbackContactEmail,data.version),"projectFeedbackSource");return;
 }
}
function singleAnswer(code){
 const q=current();if(!q||q.multi||q.type==="shortText")return;
 if(pendingSingleAnswer?.id===q.id&&pendingSingleAnswer.code===code)return;
 clearPendingSingleAnswer();
 state.draft={forId:q.id,codes:[code]};
 const pending={id:q.id,code,timer:null};
 pending.timer=setTimeout(()=>{
  if(pendingSingleAnswer!==pending||current()?.id!==pending.id)return;
  pendingSingleAnswer=null;
  save();
 },1000);
 pendingSingleAnswer=pending;
}
window.QuestionnaireEvents.bind(app,{
 singleAnswer,action,
 medicineAction:changeMedicineList,
 jump:moduleId=>{
  const choices=active().filter(q=>q.module===moduleId),next=choices.find(q=>!state.answers[q.id])||choices[0];
  if(next)setQuestion(next.id);
 },
 language:value=>{state.lang=value;state.notice="";render();},
 medicineChange:readMedicineControls,
 moduleChange:()=>{state.sectionDraft=Array.from(app.querySelectorAll("[data-module]:checked"),el=>el.dataset.module);render();},
 restore,
 answerChange:event=>{if(current()?.multi)setDraft(event);else singleAnswer(event.target.value);},
 shortTextInput:value=>{if(current())state.draft={forId:current().id,value};},
 medicineDiscussionInput:value=>{if(state.draft)state.draft.discussion=value;}
});
render();
})();
