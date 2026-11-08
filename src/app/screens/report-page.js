/* Clinician print controls and a readable project feedback report. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.reportPage = function ({heading,locale,markup,escape,btn,label,feedbackEmail}) {
 const preview='<div class="report-preview'+(feedbackEmail?' feedback-report':'')+'" lang="'+escape(locale)+'">'+markup+'</div>';
 const print='<div class="actions report-actions">'+btn("print","print","primary-inline")+'</div>';
 if(feedbackEmail){
  const email=escape(feedbackEmail);
  return '<section class="card report report-page">'+preview+
   '<p class="report-actions">'+label("feedbackProjectSend")+' <a href="mailto:'+email+'">'+email+'</a></p>'+
   print+'<div class="actions report-actions">'+btn("resultScreen","results")+'</div></section>';
 }
 return '<section class="card report report-page"><h2>'+escape(heading)+'</h2>'+preview+print+
 '<div class="actions report-actions">'+btn("back","backToAnswers")+btn("sections","editSections")+'</div></section>';
};
})(globalThis);
