/* Shared reporting layer for the offline two-section prototype. No remote calls. */
(function () {
"use strict";
function esc(value) { return String(value == null ? "" : value).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#39;"); }
function status(a,ui) {
  if (!a) return ui.unanswered;
  if (a.kind === "skip") return ui.skipped;
  if (a.status === "refused") return ui.refused;
  if (a.status === "uncertain") return ui.uncertain;
  return ui.done;
}
function readable(q,rec,locale,ui) {
  if (!rec) return ui.unanswered;
  if (rec.kind === "skip") return ui.skipped;
  if (rec.kind === "text") return rec.value || "—";
  return (rec.codes || []).map(c => (q.translations[locale].choices || {})[c] || c).join("; ");
}
function counters(questions,answers) {
  const r = {answered:0,skipped:0,unanswered:0,uncertain:0,refused:0};
  questions.forEach(q => {
    const a=answers[q.id]; if (!a) r.unanswered++;
    else if (a.kind==="skip") r.skipped++;
    else {r.answered++; if(a.status==="refused")r.refused++; else if(a.status==="uncertain")r.uncertain++;}
  }); return r;
}
function flags(questions,answers) {
  return questions.filter(q=>answers[q.id]?.codes?.some(code=>q.discussCodes?.includes(code)));

}
// Null is deliberately unrated, never zero. Priorities order individual entries only.
function priority(q,rec,presentation) {
 if(!rec || rec.kind==="skip" || ["uncertain","refused"].includes(rec.status))return null;
 const rule=presentation?.questions?.[q.id];
 if(rec.kind==="text")return rule?.textWeight ?? null;
 const values=(rec.codes||[]).map(c=>rule?.weights?.[c]);
 if(!values.length || values.some(v=>v==null))return null;
 return Math.max(...values);
}
function entries(questions,answers,locale,presentation,sorted) {
 const list=questions.filter(q=>answers[q.id]&&answers[q.id].kind!=="skip").map((q,index)=>{
  const t=q.translations[locale],rec=answers[q.id],rule=presentation?.questions?.[q.id];
  const name=rule?.labels?.[locale]||t.title;
  const value=rec.kind==="text"?rec.value:(rec.codes||[]).map(c=>t.choices[c]).join("; ");
  const rank=presentation?.topicOrder?.indexOf(q.module)??-1;
  return {id:q.id,index,topic:rank<0?999:rank,weight:priority(q,rec,presentation),text:name+(t.time?" ("+t.time+")":"")+": "+value};
 });
 // Unrated disclosures sit after ordinary information, before weighted difficulties.
 // This placement is a layout convention, not an inferred response or severity.
 if(sorted)list.sort((a,b)=>(a.weight===null?0.5:a.weight)-(b.weight===null?0.5:b.weight)||a.topic-b.topic||a.index-b.index);
 return list;
}
function doctorText(questions,answers,selected,locale,ui,groups,presentation) {
 const v=counters(questions,answers);
 return [ui.doctorHeading,ui.doctorDisclaimer,
  ui.countDone+": "+v.answered+" · "+ui.countSkip+": "+v.skipped+" · "+ui.countOpen+": "+v.unanswered,
  ui.omissionNote,ui.coverageNote,"",...entries(questions,answers,locale,presentation,true).map(e=>e.text)].join("\n");
}
function doctorHtml(questions,answers,selected,locale,ui,groups,presentation) {
 const text=doctorText(questions,answers,selected,locale,ui,groups,presentation);
 return '<!doctype html><html lang="'+esc(locale)+'"><head><meta charset="utf-8"><title>'+esc(ui.doctorHeading)+'</title><style>@page{size:A4;margin:12mm}body{font:10pt/1.3 Arial,sans-serif;color:#000;background:#fff;margin:0 auto;max-width:186mm}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit}</style></head><body><pre>'+esc(text)+'</pre></body></html>';
}
function aiText(questions,answers,selected,locale,ui,groups,presentation) {
 return [ui.omissionNote,...entries(questions,answers,locale,presentation,false).map(e=>e.text),"",ui.aiInstruction].join("\n");
}
// Keep the API name for callers migrating from the old coded export.
function codedText(questions,answers,selected,locale,ui,availability,presentation) {
 return aiText(questions.filter(q=>!availability||!availability(q)),answers,selected,locale,ui,null,presentation);
}
function allTxt(questions,answers,selected,locale,ui) {
 const lines=[ui.allAnswers,ui.doctorDisclaimer,"",ui.countDone+": "+counters(questions,answers).answered];
 for(const q of questions) {
    const a=answers[q.id];
    const code=a?.kind==="choice"?a.codes.join("+"):a?.kind==="text"?"TEXT":a?.kind==="skip"?"~X":"~U";
    lines.push("\n"+q.id+" ["+q.module+"] "+q.translations[locale].title+"\n"+code+" | "+status(a,ui)+" | "+readable(q,a,locale,ui));
 }
 return lines.join("\n");
}
function decodingKey(questions,locale) {
 const lines=["# Questionnaire question and answer key","","> Prototype: not validated; language translations may be unreviewed.",""];
 for(const q of questions){
   const t=q.translations[locale];
   lines.push("## "+q.id+" — "+t.title);
   if(t.time)lines.push("*"+t.time+"*");
   if(t.help)lines.push(t.help);
   for(const [key,value] of Object.entries(t.choices||{}))lines.push("- "+key+": "+value);
   lines.push("");
 }
 return lines.join("\n");
}
window.PilotReports={priority,entries,aiText,status,readable,counters,flags,doctorText,doctorHtml,codedText,allTxt,decodingKey,esc};
})();
