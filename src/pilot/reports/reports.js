/* Compact clinician report. Bold behavior comes only from explicit answer-code mappings. */
(function () {
"use strict";
function esc(value) { return String(value == null ? "" : value).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#39;"); }
function readable(q,rec,locale) {
 if(!rec)return "";
 if(rec.kind==="text")return rec.value||"—";
 if(rec.kind==="skip")return "";
 return (rec.codes||[]).map(c=>(q.translations[locale].choices||{})[c]||c).join("; ");
}
function counters(questions,answers) {
 const counts={answered:0,skipped:0,unanswered:0};
 questions.forEach(q=>{const a=answers[q.id];if(!a)counts.unanswered++;else if(a.kind==="skip")counts.skipped++;else counts.answered++;});
 return counts;
}
function entries(questions,answers,locale,presentation) {
 const order=presentation.topicOrder||[];
 return questions.filter(q=>answers[q.id]&&answers[q.id].kind!=="skip").map((q,index)=>{
  const rec=answers[q.id],t=q.translations[locale],rule=presentation.questions?.[q.id]||{};
  const title=rule.labels?.[locale]||t.title;
  const choices=rec.kind==="text"?[{text:rec.value||"—",bold:false}]: (rec.codes||[]).map(code=>({text:t.choices[code]||code,bold:(presentation.boldAnswers?.[q.id]||[]).includes(code)}));
  const prefix=title+(t.time?" ("+t.time+")":"")+": ";
  const value=choices.map(c=>c.text).join("; ");
  const response=choices.map(c=>c.bold?"<strong>"+esc(c.text)+"</strong>":esc(c.text)).join("; ");
  return {id:q.id,index,topic:Math.max(0,order.indexOf(q.module)),plain:prefix+value,html:"<p>"+esc(prefix)+response+"</p>"};
 }).sort((a,b)=>a.topic-b.topic||a.index-b.index);
}
function doctorText(questions,answers,selected,locale,ui,groups,presentation) {
 const counts=counters(questions,answers);
 return [ui.doctorHeading,ui.doctorDisclaimer,
  ui.countDone+": "+counts.answered+" · "+ui.countSkip+": "+counts.skipped+" · "+ui.countOpen+": "+counts.unanswered,
  ui.omissionNote,"",...entries(questions,answers,locale,presentation).map(e=>e.plain)].join("\n");
}
function doctorMarkup(questions,answers,selected,locale,ui,groups,presentation) {
 const counts=counters(questions,answers);
 return "<h1>"+esc(ui.doctorHeading)+"</h1><p>"+esc(ui.doctorDisclaimer)+"</p><p>"+
 esc(ui.countDone+": "+counts.answered+" · "+ui.countSkip+": "+counts.skipped+" · "+ui.countOpen+": "+counts.unanswered)+"</p><p>"+
 esc(ui.omissionNote)+"</p><hr>"+entries(questions,answers,locale,presentation).map(e=>e.html).join("");
}
function doctorHtml(questions,answers,selected,locale,ui,groups,presentation) {
 return '<!doctype html><html lang="'+esc(locale)+'"><head><meta charset="utf-8"><title>'+esc(ui.doctorHeading)+
 '</title><style>@page{size:A4;margin:12mm}body{font:10pt/1.3 Arial,sans-serif;color:#000;background:#fff;margin:0 auto;max-width:186mm}p{margin:0 0 5pt}hr{border:0;border-top:1px solid #777;margin:7pt 0}strong{font-weight:700}</style></head><body>'+doctorMarkup(questions,answers,selected,locale,ui,groups,presentation)+'</body></html>';
}
window.PilotReports={entries,readable,counters,doctorText,doctorMarkup,doctorHtml,esc};
})();
