/* Clinician print controls and a readable project feedback report. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.reportPage = function ({heading,locale,markup,escape,btn,label,feedbackEmail,hasFeedback}) {
 const preview='<div class="report-preview'+(feedbackEmail?' feedback-report':'')+'" lang="'+escape(locale)+'">'+markup+'</div>';
 const print=btn("print","print","primary-inline");
 if(feedbackEmail){
  const email=escape(feedbackEmail);
  return '<section class="card report report-page">'+
   '<p class="report-actions">'+label("feedbackProjectSend")+' <a href="mailto:'+email+'">'+email+'</a></p>'+
   '<div class="actions report-actions">'+print+btn("doctor","doctorHeading")+btn("resultScreen","results")+'</div>'+
   preview+'</section>';
 }
 return '<section class="card report report-page"><h2>'+escape(heading)+'</h2>'+
 '<div class="actions report-actions">'+print+(hasFeedback?btn("feedbackReport","feedbackProjectReport"):"")+'</div>'+
 '<div class="actions report-actions">'+btn("resultScreen","results")+btn("back","backToAnswers")+btn("sections","editSections")+'</div>'+
 preview+'</section>';
};
})(globalThis);
