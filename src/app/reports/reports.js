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
 const counts={selected:questions.length,answered:0,skipped:0,unanswered:0};
 questions.forEach(q=>{const a=answers[q.id];if(!a)counts.unanswered++;else if(a.kind==="skip")counts.skipped++;else counts.answered++;});
 return counts;
}
function medicineValues(rec,medicine) {
 const fields=medicine.fields,items=[];
 (rec.records||[]).forEach((record,index)=>{
  const parts=[];
  Object.keys(fields).forEach(key=>{
   const value=key==="status"?(medicine.status[record.status]||""):
    key==="benefit"?(medicine.benefits[record.benefit]||""):(record[key]||"");
   if(value)parts.push(fields[key]+": "+value);
  });
  if(parts.length)items.push(medicine.entry+" "+(index+1)+": "+parts.join("; "));
 });
 if(rec.discussion)items.push(medicine.notes+": "+rec.discussion);
 return items.join("\n");
}
function entries(questions,answers,locale,presentation,medicine) {
 const order=presentation.topicOrder||[];
 return questions.filter(q=>answers[q.id]&&answers[q.id].kind!=="skip").map((q,index)=>{
  const rec=answers[q.id],t=q.translations[locale],rule=presentation.questions?.[q.id]||{};
  const title=rule.labels?.[locale]||t.title;
  const medicineText=rec.kind==="medicine"?medicineValues(rec,medicine||{}):"";
  const choices=rec.kind==="text"?[{text:rec.value||"—",bold:false}]:rec.kind==="medicine"?[{text:medicineText,bold:false}]:(rec.codes||[]).map(code=>({text:t.choices[code]||code,bold:(presentation.boldAnswers?.[q.id]||[]).includes(code)}));
  const prefix=title+(t.time?" ("+t.time+")":"")+": ";
  const value=choices.map(c=>c.text).join("; ");
  const response=choices.map(c=>c.bold?"<strong>"+esc(c.text)+"</strong>":esc(c.text)).join("; ");
  return {id:q.id,index,topic:Math.max(0,order.indexOf(q.module)),plain:prefix+value,html:"<p>"+esc(prefix)+response+"</p>"};
 }).sort((a,b)=>a.topic-b.topic||a.index-b.index);
}
function feedbackEntries(questions,feedback,catalogs) {
 const byId=new Map(questions.map(q=>[q.id,q]));
 return Object.entries(feedback||{}).map(([id,rec])=>{
  const q=byId.get(id);if(!q)return null;
  const lang=rec.language,ui=catalogs[lang],t=q.translations[lang];
  const reasons=(rec.reasons||[]).map(reason=>{
   if(reason.startsWith("answer:")){
    const code=reason.slice(7);return ui.feedbackAnswerPrefix+" "+code+": "+(t.choices[code]||code);
   }
   return ({question:ui.feedbackQuestion,language:ui.feedbackLanguage,other:ui.feedbackOther})[reason]||reason;
  });
  const questionText=t.title+(t.time?" ("+t.time+")":"");
  const lines=[id+" · "+lang.toUpperCase()+" · "+rec.version,questionText,
   ui.feedbackReasonLabel+": "+reasons.join("; ")];
  if(rec.comment)lines.push(ui.feedbackComment+": "+rec.comment);
  const safe=lines.map(esc);
  return {id,language:lang,version:rec.version,title:questionText,reasons,comment:rec.comment||"",
   plain:lines.join("\n"),html:"<p><strong>"+safe[0]+"</strong><br>"+safe.slice(1).join("<br>")+"</p>"};
 }).filter(Boolean).sort((a,b)=>questions.indexOf(byId.get(a.id))-questions.indexOf(byId.get(b.id)));
}
function projectFeedbackText(questions,feedback,locale,catalogs,contactEmail,version) {
 const ui=catalogs[locale],items=feedbackEntries(questions,feedback,catalogs);
 return [ui.feedbackProjectHeading,ui.feedbackVersionLabel+": "+version,
  ui.feedbackContactLabel+": "+contactEmail,
  ...(items.length?["",...items.map(item=>item.plain)]:["",ui.feedbackNone])].join("\n");
}
function identityText(ui,identity={}) {
 const name=[identity.name,identity.surname].map(value=>String(value||"").trim()).filter(Boolean).join(" ");
 return ui.reportName+": "+(name||"____________________________")+"\n"+ui.reportDate+": ____________________";
}
function countText(counts,ui) {
 return [ui.reportCountSelected+": "+counts.selected,ui.reportCountDone+": "+counts.answered,ui.reportCountSkip+": "+counts.skipped].join(" · ");
}
function doctorText(questions,answers,locale,ui,presentation,identity={}) {
 const counts=counters(questions,answers);
 const responses=entries(questions,answers,locale,presentation,ui.medicine).map(e=>e.plain);
 return [identityText(ui,identity),"",ui.doctorHeading,ui.doctorDisclaimer,countText(counts,ui),"",...responses].join("\n");
}
function doctorMarkup(questions,answers,locale,ui,presentation,identity={}) {
 const counts=counters(questions,answers);
 const name=[identity.name,identity.surname].map(value=>String(value||"").trim()).filter(Boolean).join(" ");
 const nameValue=name?esc(name):'<span class="write-in"></span>';
 const dateHtml='<p><strong>'+esc(ui.reportDate)+':</strong> <span class="write-in write-in-date"></span></p>';
 const summary="<p class=\"report-counts\">"+esc(countText(counts,ui))+"</p>";
 const responses=entries(questions,answers,locale,presentation,ui.medicine).map(e=>e.html.replace(/\n/g,"<br>")).join("");
 return '<div class="report-identity"><p><strong>'+esc(ui.reportName)+':</strong> '+nameValue+'</p>'+dateHtml+'</div><h1>'+esc(ui.doctorHeading)+'</h1><p>'+esc(ui.doctorDisclaimer)+'</p>'+summary+'<hr>'+responses;
}
function doctorHtml(questions,answers,locale,ui,presentation,identity={}) {
 return '<!doctype html><html lang="'+esc(locale)+'"><head><meta charset="utf-8"><title>'+esc(ui.doctorHeading)+
 '</title><style>@page{size:A4;margin:12mm}body{font:10pt/1.3 Arial,sans-serif;color:#000;background:#fff;margin:0 auto;max-width:186mm}p{margin:0 0 5pt}hr{border:0;border-top:1px solid #777;margin:7pt 0}strong{font-weight:700}.write-in{display:inline-block;width:75mm;height:12pt;border-bottom:1px solid #555;vertical-align:baseline}.write-in-date{width:35mm}.report-identity{margin-bottom:10pt}.report-counts{font-weight:700}</style></head><body>'+doctorMarkup(questions,answers,locale,ui,presentation,identity)+'</body></html>';
}
window.QuestionnaireReports={entries,medicineValues,feedbackEntries,projectFeedbackText,readable,counters,doctorText,doctorMarkup,doctorHtml,esc};
})();
