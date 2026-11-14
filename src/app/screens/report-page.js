/* Clinician print controls and a readable project feedback report. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.reportPage = function ({heading,locale,markup,escape,btn,label,feedbackEmail,hasFeedback,feedbackText="",canSend=false}) {
 const preview='<div class="report-preview'+(feedbackEmail?' feedback-report':'')+'" lang="'+escape(locale)+'">'+markup+'</div>';
 const print=btn("print","print","primary-inline");
 if(feedbackEmail){
  const email=escape(feedbackEmail);
  return '<section class="card report report-page">'+
   '<p class="report-actions">'+label("feedbackDeliveryPrivacy")+'</p><p class="report-actions">'+label("feedbackContactLabel")+': '+email+'</p>'+
   '<div class="actions report-actions">'+btn("sendFeedback","sendFeedback","primary-inline",canSend?'':'disabled')+btn("copyFeedback","copyFeedback")+'</div>'+
   '<p class="report-actions">'+label(canSend?"feedbackCopyHelp":"feedbackLongHelp")+'</p>'+
   '<label class="report-actions" for="feedback-copy">'+label("feedbackCopyHelp")+'</label><textarea class="report-actions" id="feedback-copy" readonly rows="8">'+escape(feedbackText)+'</textarea>'+
   '<div class="actions report-actions">'+print+btn("doctor","doctorHeading")+btn("resultScreen","results")+'</div>'+
   preview+'</section>';
 }
 return '<section class="card report report-page"><h2>'+escape(heading)+'</h2>'+
 '<div class="actions report-actions">'+print+(hasFeedback?btn("feedbackReport","feedbackProjectReport"):"")+'</div>'+
 '<div class="actions report-actions">'+btn("resultScreen","results")+btn("back","backToAnswers")+btn("sections","editSections")+'</div>'+
 preview+'</section>';
};
})(globalThis);
