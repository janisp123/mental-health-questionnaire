/* Completion and project-feedback page markup. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.results = function ({label,escape,btn,counts,selected,feedbackText,reportLanguageOptions}) {
 const stats='<div class="stats"><span>'+label("countDone")+' <b>'+(counts.completed??counts.answered)+'</b></span></div>';
 return '<section class="card"><h2>'+label("results")+'</h2>'+stats+selected+'<p>'+label("doctorDisclaimer")+'</p><p>'+label("noneFlagged")+'</p>'+
 '<textarea id="projectFeedbackSource" class="copy-source" readonly aria-hidden="true" tabindex="-1">'+escape(feedbackText)+'</textarea>'+
 '<label class="lang">'+label("reportLanguage")+' <select id="report-language">'+reportLanguageOptions+'</select></label>'+
 '<div class="actions">'+btn("doctor","specialist","primary-inline")+btn("copyFeedback","feedbackProjectCopy")+'</div>'+
 '<div class="actions">'+btn("back","back")+btn("sections","editSections")+btn("new","new")+'</div></section>';
};
})(globalThis);
