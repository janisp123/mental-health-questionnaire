/* Deliberate email handoff; only the existing separate feedback report is read. */
(function (root) {
"use strict";
function compose(questions,feedback,locale,catalogs,email,version){
 const text=root.QuestionnaireReports.projectFeedbackText(questions,feedback,locale,catalogs,email,version);
 const hasFeedback=root.QuestionnaireReports.feedbackEntries(questions,feedback,catalogs).length>0;
 const validEmail=/^[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/.test(email||"");
 // A restored comment or a length-limited emoji may contain an unpaired surrogate.
 // Replace only invalid Unicode in the URI; keep the complete report for copying.
 const body=Array.from(text.replace(/\r?\n/g,'\r\n'),character=>character.length===1&&character.charCodeAt(0)>=0xD800&&character.charCodeAt(0)<=0xDFFF?'\uFFFD':character).join('');
 const candidate=validEmail&&hasFeedback?'mailto:'+email+'?subject='+encodeURIComponent('MH_TEST — Feedback')+'&body='+encodeURIComponent(body):null;
 // Conservative interoperability budget, not a universal browser/client limit.
 return {text,hasFeedback,url:candidate&&candidate.length<=1800?candidate:null};
}
root.QuestionnaireFeedbackDelivery={compose};
})(globalThis);
