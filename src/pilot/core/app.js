/* Offline questionnaire pilot: one engine, independent logic + per-language text. */
(function () {
"use strict";
const embedded=document.getElementById("pilot-data");
const data=JSON.parse(embedded.textContent);
const groups=new Map(data.groups.map(g=>[g.id,g]));
const optionalIds=data.groups.filter(g=>!g.required).map(g=>g.id);
const byId={};
const all=[];
for(const group of data.groups){
 for(const q of group.questions){if(byId[q.id])throw Error("Duplicate question: "+q.id);byId[q.id]=q;all.push(q);}
}
all.sort((a,b)=>a.order-b.order);
const app=document.getElementById("app");
const report=window.PilotReports;
let state={lang:"lv",screen:"start",currentId:null,answers:{},selected:[],sectionDraft:[],sectionConfirmed:false,savedCount:0,notice:"",reportView:"doctor",draft:null};
function ui(){return data.ui[state.lang];}
function esc(s){return report.esc(s);}
function label(key){return esc(ui()[key]||key);}
function btn(act,key,cls,extra){return '<button type="button" data-act="'+act+'" class="'+(cls||"")+'" '+(extra||"")+'>'+label(key)+'</button>';}
function isSafety(q){return q.module==="opening" && q.order>=5 && q.order<=15;}
function canSkip(q){return !isSafety(q);}
function copyObject(x){return JSON.parse(JSON.stringify(x));}
function normalizeCode(a){return a?.kind==="choice"?(a.codes||[]):[];}
function questionVisible(q){
 const c=q.context;if(!c || !c.id)return true;
 const a=state.answers[c.id];
 if(!a || a.kind!=="choice")return !Array.isArray(c.showValues);
 const chosen=new Set(a.codes||[]);
 if(Array.isArray(c.showValues)&&!c.showValues.some(v=>chosen.has(v)))return false;
 if(Array.isArray(c.hideValues)&&c.hideValues.some(v=>chosen.has(v)))return false;
 return true;
}
function active(){return all.filter(q=>(groups.get(q.module).required||state.selected.includes(q.module))&&questionVisible(q));}
function current(){return byId[state.currentId]||null;}
function countGroup(group){
 const q=all.filter(x=>x.module===group && questionVisible(x));
 return {total:q.length,done:q.filter(x=>state.answers[x.id]).length,skipped:q.filter(x=>state.answers[x.id]?.kind==="skip").length};
}
function sectionBar(){
 return '<div class="section-progress">'+data.groups.map(g=>{
  const count=countGroup(g.id);
  return '<span>'+esc(g.titles[state.lang])+' <strong>'+count.done+'/'+count.total+'</strong></span>';
 }).join("")+'</div>';
}
function header(){
 const opts=["lv","en","ru"].map(id=>'<option value="'+id+'"'+(id===state.lang?" selected":"")+">"+({lv:"Latviešu",en:"English",ru:"Русский"}[id])+"</option>").join("");
 return '<header><div class="header-row"><h1>'+label("project")+'</h1><label class="lang">'+label("language")+' <select id="language">'+opts+'</select></label></div><p class="muted">'+label("pilot")+'</p><p class="prototype">'+label("notReleased")+'</p>'+sectionBar()+'</header>';
}
function toolbar(){
 return '<nav class="toolbar" aria-label="Tools">'+btn("backup","saveBackup")+ '<label class="file-label">'+label("restoreBackup")+'<input id="restore" type="file" accept=".json,application/json" aria-label="'+label("restoreBackup")+'"></label>'+btn("results","results")+btn("sections","editSections")+'</nav>';
}
function footer(){
 return '<footer><details><summary>'+label("legal")+'</summary><p>'+label("intro")+'</p><p>'+label("privacy")+'</p><p>'+label("help")+'</p></details><details><summary>'+label("helpers")+'</summary><p>'+label("credits")+'</p></details><p class="muted">'+label("footer")+'</p></footer>';
}
function renderStart(){
 return '<section class="card"><p>'+label("intro")+'</p><p class="warning">'+label("reviewNote")+'</p><p>'+label("noAuto")+'</p>'+btn("start","start","primary")+ '<div class="actions">'+btn("all","chooseAll")+btn("choose","chooseOwn")+btn("guide","chooseGuide")+'</div></section>';
}
function renderSelector(){
 const rows=data.groups.map(g=>{
  const count=countGroup(g.id), title=esc(g.titles[state.lang]), progress=count.done+'/'+count.total;
  if(g.required)return '<p><strong>'+title+'</strong> — '+progress+'</p>';
  const checked=state.sectionDraft.includes(g.id);
  return '<label class="choice module-choice"><input type="checkbox" data-module="'+esc(g.id)+'" id="optional'+esc(g.id)+'"'+(checked?' checked':'')+'> <span><strong>'+title+'</strong><small>'+progress+' · '+label(checked?'selected':'notSelected')+'</small></span></label>';
 });
 return '<section class="card"><h2>'+label("selector")+'</h2><p>'+label("selectIntro")+'</p>'+rows.join("")+
 '<div class="actions">'+btn("all","chooseAll")+btn("clear","clearSections")+'</div>'+btn("confirm","confirmSections","primary")+btn("cancel","cancel")+'</section>';
}
function storedDraft(q){
 const r=state.answers[q.id];
 if(r?.kind==="choice")return {codes:[...r.codes]};
 if(r?.kind==="text")return {value:r.value||""};
 return {codes:[],value:""};
}
function renderQuestion(){
 const q=current(),u=ui();
 if(!q){state.screen="results";return renderResults();}
 const t=q.translations[state.lang];
 if(!state.draft || state.draft.forId!==q.id)state.draft={forId:q.id,...storedDraft(q)};
 const queue=active(),idx=queue.findIndex(x=>x.id===q.id);
 const group=groups.get(q.module).titles[state.lang];
 const time=t.time?'<p class="muted">'+esc(t.time)+'</p>':"";
 const help=t.help?'<p class="help">'+esc(t.help)+'</p>':"";
 let options="";
 if(q.type==="shortText") {
  options='<label class="field-label">'+label("enterText")+' <input id="shortText" autocomplete="off" type="text" maxlength="200" value="'+esc(state.draft.value||"")+'"></label><p class="muted">'+label("optionalText")+'</p>';
 } else {
  options='<fieldset><legend class="sr-only">'+esc(t.title)+'</legend>'+
  q.choiceCodes.map(key=>{
    const checked=(state.draft.codes||[]).includes(key);
    const kind=q.multi?"checkbox":"radio";
    return '<label class="choice"><input type="'+kind+'" name="answer" value="'+esc(key)+'"'+(checked?" checked":"")+'> <span><b>'+esc(key)+'</b> '+esc(t.choices[key]||key)+'</span></label>';
  }).join("")+'</fieldset>';
 }
 return '<section class="card question"><div class="muted">'+esc(group)+' · '+(idx+1)+'/'+queue.length+' · '+esc(q.id)+'</div><h2>'+esc(t.title)+'</h2>'+time+help+options+
 '<p class="muted">'+label("saveWarning")+'</p>'+btn("save","next","primary")+
 '<div class="actions">'+(canSkip(q)?btn("skip","skipQuestion"):"")+btn("previous","prev")+(!groups.get(q.module).required?btn("skipSection","skipSection"):"")+btn("sections","editSections")+btn("end","skipRest")+'</div></section>';
}
function renderResults(){
 const qs=active(),u=ui(),v=report.counters(qs,state.answers);
 const stats='<div class="stats"><span>'+label("countDone")+' <b>'+v.answered+'</b></span><span>'+label("countSkip")+' <b>'+v.skipped+'</b></span><span>'+label("countOpen")+' <b>'+v.unanswered+'</b></span></div>';
 const selected=data.groups.map(g=>'<p>'+esc(g.titles[state.lang])+' · '+(g.required||state.selected.includes(g.id)?label("selected"):label("notSelected"))+'</p>').join("");
 const flag=report.flags(qs,state.answers).length;
 return '<section class="card"><h2>'+label("results")+'</h2>'+stats+selected+'<p>'+label("doctorDisclaimer")+'</p>'+
 (flag?'<p class="warning">'+label("attention")+': '+flag+'. '+label("warningSensitive")+'</p>':'<p>'+label("noneFlagged")+'</p>')+
 '<div class="actions">'+btn("doctor","specialist","primary-inline")+btn("ai","ai")+btn("downloadTxt","txt")+btn("reference","reference")+'</div>'+
 '<div class="actions">'+btn("back","back")+btn("reviewSafety","reviewSafety")+btn("new","new")+'</div></section>';
}
function renderReport(){
 const q=active(),u=ui(),doctor=state.reportView!=="ai";
 const heading=doctor?u.doctorHeading:u.coded;
 const result=doctor?report.doctorText(q,state.answers,state.selected,state.lang,u,data.groups):report.codedText(q,state.answers,state.selected,state.lang,u);
 return '<section class="card report"><h2>'+esc(heading)+'</h2><p>'+label("doctorDisclaimer")+'</p><textarea id="reportText" readonly rows="17">'+esc(result)+'</textarea>'+
 '<div class="actions">'+btn(doctor?"copyDoctor":"copyAI",doctor?"copyDoctor":"copyAI","primary-inline")+
 btn("doctor","specialist")+btn("ai","ai")+btn("print","print")+btn("downloadReport","downloadReport")+btn("downloadTxt","txt")+btn("reference","reference")+'</div>'+
 '<div class="actions">'+btn("resultScreen","backToAnswers")+btn("reviewSafety","reviewSafety")+'</div></section>';
}
function render(){
 document.documentElement.lang=state.lang;
 document.title=ui().project;
 const body=state.screen==="start"?renderStart():state.screen==="selector"?renderSelector():state.screen==="question"?renderQuestion():state.screen==="report"?renderReport():renderResults();
 app.innerHTML='<main>'+header()+toolbar()+(state.notice?'<p role="status" class="notice">'+esc(state.notice)+'</p>':"")+body+footer()+'</main>';
}
function setQuestion(id){state.currentId=id;state.draft=null;state.screen="question";state.notice="";render();}
function advance(){
 const list=active();
 const now=list.findIndex(q=>q.id===state.currentId);
 const next=list.slice(now+1).find(q=>!state.answers[q.id]);
 if(next){setQuestion(next.id);return;}
 const initialRemaining=list.some(q=>groups.get(q.module).required&&!state.answers[q.id]);
 if(!initialRemaining && !state.sectionConfirmed){state.sectionDraft=[...state.selected];state.screen="selector";state.notice="";render();return;}
 const later=list.find(q=>!state.answers[q.id]);
 if(later){setQuestion(later.id);return;}
 state.screen="results";state.draft=null;state.notice="";render();
}
function start(){const q=active().find(x=>!state.answers[x.id]);if(q)setQuestion(q.id);else {state.screen=state.sectionConfirmed?"results":"selector";render();}}
function save(){
 const q=current();if(!q)return;
 let rec={savedAt:new Date().toISOString()};
 if(q.type==="shortText"){
   rec.kind="text";rec.value=document.getElementById("shortText")?.value.trim().slice(0,200)||"";rec.status="answered";
 } else {
   const codes=(state.draft?.codes||[]).filter(key=>q.choiceCodes.includes(key));
   if(!codes.length){state.notice=ui().chooseAnswer;render();return;}
   if(q.maxChoices&&codes.length>q.maxChoices){state.notice=ui().maxChoices+" "+q.maxChoices;render();return;}
   rec.kind="choice";rec.codes=codes;rec.status=codes.length===1?(q.answerStatus?.[codes[0]]||"answered"):"answered";
 }
 state.answers[q.id]=rec;state.savedCount++;
 advance();
 if(state.savedCount%10===0){
   downloadBackup();
   state.notice=ui().saved10;render();
 }
}
function skip(){
 const q=current();if(!q||!canSkip(q))return;
 state.answers[q.id]={kind:"skip",savedAt:new Date().toISOString(),status:"skipped"};
 state.savedCount++;
 advance();
 if(state.savedCount%10===0){downloadBackup();state.notice=ui().saved10;render();}
}
function previous(){const list=active(),idx=list.findIndex(q=>q.id===state.currentId);if(idx>0)setQuestion(list[idx-1].id);else {state.screen="start";render();}}
function skipSection(){
 const q=current();if(!q||groups.get(q.module).required)return;
 if(!window.confirm(ui().skipConfirm))return;
 for(const item of all.filter(x=>x.module===q.module&&questionVisible(x))){
  if(!state.answers[item.id])state.answers[item.id]={kind:"skip",savedAt:new Date().toISOString(),status:"skipped"};
 }
 advance();
}
function skipRest(){if(window.confirm(ui().restConfirm)){state.screen="results";state.draft=null;render();}}
function showSections(m){state.screen="selector";state.sectionDraft=m?[...m]:[...state.selected];state.draft=null;render();}
function confirmSections(){
 state.selected=optionalIds.filter(id=>state.sectionDraft.includes(id));state.sectionConfirmed=true;
 state.screen="question";
 const first=active().find(q=>!state.answers[q.id]);
 if(first)setQuestion(first.id);else {state.screen="results";render();}
}
function setDraft(ev){
 const q=current();if(!q||q.type==="shortText")return;
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
  const message=app.querySelector('[role="status"]');if(message)message.textContent=state.notice;
 }
}
function downloadFile(name,contents,mime){
 const blob=new Blob([contents],{type:mime||"text/plain;charset=utf-8"});
 const href=URL.createObjectURL(blob),link=document.createElement("a");link.href=href;link.download=name;document.body.appendChild(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(href),1500);
}
function downloadBackup(){
 const payload={schema:"mental-pilot-recovery-v1",version:data.version,lang:state.lang,selected:[...state.selected],sectionConfirmed:state.sectionConfirmed,currentId:state.currentId,answers:state.answers,savedCount:state.savedCount,exportedAt:new Date().toISOString()};
 downloadFile("anketa-pilot-recovery.json",JSON.stringify(payload,null,2),"application/json");
}
function restore(file){
 if(!file)return;
 const reader=new FileReader();
 reader.onload=function(){
  try{
   const x=JSON.parse(String(reader.result));
   if(x.schema!=="mental-pilot-recovery-v1"||!x.answers||typeof x.answers!=="object"||Array.isArray(x.answers))throw Error("Invalid schema");
   const a={};
   for(const [id,rec] of Object.entries(x.answers)){
    const q=byId[id];if(!q||!rec||typeof rec!=="object")throw Error("Invalid record");
    if(rec.kind==="choice"){
      if(!Array.isArray(rec.codes)||!rec.codes.every(code=>q.choiceCodes.includes(code)))throw Error("Unknown choice");
      if(!q.multi&&rec.codes.length!==1)throw Error("Invalid single answer");
      a[id]={kind:"choice",codes:[...rec.codes],status:rec.status||"answered",savedAt:rec.savedAt||""};
    }else if(rec.kind==="text"){
      if(q.type!=="shortText"||typeof rec.value!=="string")throw Error("Invalid text");
      a[id]={kind:"text",value:rec.value.slice(0,200),status:"answered",savedAt:rec.savedAt||""};
    }else if(rec.kind==="skip")a[id]={kind:"skip",status:"skipped",savedAt:rec.savedAt||""};
    else throw Error("Unknown record");
   }
   state.answers=a;state.selected=Array.isArray(x.selected)?optionalIds.filter(id=>x.selected.includes(id)):[];state.sectionConfirmed=!!x.sectionConfirmed;
   state.savedCount=Number.isInteger(x.savedCount)&&x.savedCount>=0?x.savedCount:Object.keys(a).length;
   if(["lv","en","ru"].includes(x.lang))state.lang=x.lang;
   state.currentId=typeof x.currentId==="string"&&byId[x.currentId]?x.currentId:null;
   if(!active().some(q=>q.id===state.currentId))state.currentId=active().find(q=>!state.answers[q.id])?.id||null;
   state.screen=state.currentId?"question":"start";state.draft=null;state.notice=ui().restoreOK;render();
  }catch(err){state.notice=ui().restoreError;render();}
 };
 reader.onerror=function(){state.notice=ui().restoreError;render();};
 reader.readAsText(file,"utf-8");
}
async function copyText(text){
 const area=document.getElementById("reportText");
 if(area){area.value=text;area.focus();area.select();}
 try{
  if(navigator.clipboard&&navigator.clipboard.writeText){await navigator.clipboard.writeText(text);state.notice=ui().copied;}
  else if(area&&document.execCommand("copy"))state.notice=ui().copied;
  else state.notice=ui().copyFailure;
 }catch(e){state.notice=ui().copyFailure;}
 const target=document.querySelector('[role="status"]');
 if(target)target.textContent=state.notice;else{const p=document.createElement("p");p.role="status";p.className="notice";p.textContent=state.notice;app.querySelector("header").after(p);}
}
function action(key){
 const q=active(),u=ui();
 if(key==="start"){start();return;}
 if(key==="all"){if(state.screen==="selector"){state.sectionDraft=[...optionalIds];render();}else showSections([...optionalIds]);return;}
 if(key==="choose"){showSections([]);return;}
 if(key==="guide"){showSections([...optionalIds]);return;}
 if(key==="clear"){state.sectionDraft=[];render();return;}
 if(key==="confirm"){confirmSections();return;}
 if(key==="cancel"){state.screen=state.currentId?"question":"start";render();return;}
 if(key==="save"){save();return;}
 if(key==="skip"){skip();return;}
 if(key==="previous"){previous();return;}
 if(key==="skipSection"){skipSection();return;}
 if(key==="end"){skipRest();return;}
 if(key==="sections"){showSections();return;}
 if(key==="results"){state.screen="results";render();return;}
 if(key==="doctor"||key==="ai"){state.reportView=key==="doctor"?"doctor":"ai";state.screen="report";render();return;}
 if(key==="resultScreen"){state.screen="results";render();return;}
 if(key==="back"){state.screen=state.currentId?"question":"start";render();return;}
 if(key==="reviewSafety"){setQuestion("M06_01");return;}
 if(key==="new"){
   if(window.confirm(u.newConfirm)){
     const lang=state.lang;state={lang,screen:"start",currentId:null,answers:{},selected:[],sectionDraft:[],sectionConfirmed:false,savedCount:0,notice:"",reportView:"doctor",draft:null};render();
   }return;
 }
 if(key==="backup"){downloadBackup();state.notice=u.backupSaved;render();return;}
 if(key==="downloadTxt"){downloadFile("anketa-pilot-"+state.lang+".txt",report.allTxt(q,state.answers,state.selected,state.lang,u));return;}
 if(key==="reference"){downloadFile("anketa-pilot-reference-"+state.lang+".md",report.decodingKey(q,state.lang),"text/markdown;charset=utf-8");return;}
 if(key==="downloadReport"){downloadFile("anketa-pilot-report-"+state.lang+".html",report.doctorHtml(q,state.answers,state.selected,state.lang,u,data.groups),"text/html;charset=utf-8");return;}
 if(key==="print"){
   if(state.screen!=="report"){state.reportView="doctor";state.screen="report";render();}
   window.print();return;
 }
 if(key==="copyDoctor"||key==="copyAI"){
   const text=key==="copyDoctor"?report.doctorText(q,state.answers,state.selected,state.lang,u,data.groups):report.codedText(q,state.answers,state.selected,state.lang,u);
   copyText(text);return;
 }
}
app.addEventListener("click",e=>{const el=e.target.closest("[data-act]");if(el){e.preventDefault();action(el.getAttribute("data-act"));}});
app.addEventListener("change",e=>{
 if(e.target.id==="language"){state.lang=e.target.value;state.notice="";render();return;}
 if(e.target.hasAttribute("data-module")){
  state.sectionDraft=Array.from(app.querySelectorAll("[data-module]:checked"),el=>el.dataset.module);
  render();return;
 }
 if(e.target.id==="restore"){restore(e.target.files[0]);return;}
 if(e.target.name==="answer")setDraft(e);
});
app.addEventListener("input",e=>{
 if(e.target.id==="shortText"&&current()){state.draft={forId:current().id,value:e.target.value};}
});
render();
})();
