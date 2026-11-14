/* Completion and project-feedback page markup. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.results = function ({label,btn,counts,selected,reportLanguageOptions,hasFeedback=false}) {
 const stats='<div class="stats">'+[["reportCountSelected",counts.selected],["reportCountDone",counts.answered],["reportCountSkip",counts.skipped]]
  .map(([key,value])=>'<span>'+label(key)+' <b>'+value+'</b></span>').join("")+'</div>';
 return '<section class="card"><h2>'+label("results")+'</h2>'+stats+selected+'<p class="muted">'+label("coverageNote")+'</p><p>'+label("doctorDisclaimer")+'</p><p>'+label("noneFlagged")+'</p>'+
 '<label class="lang">'+label("reportLanguage")+' <select id="report-language">'+reportLanguageOptions+'</select></label>'+
 '<div class="actions">'+btn("doctor","specialist","primary-inline")+(hasFeedback?btn("feedbackReport","feedbackProjectReport"):"")+'</div>'+
 '<div class="actions">'+btn("back","back")+btn("sections","editSections")+btn("new","new")+'</div></section>';
};
})(globalThis);
