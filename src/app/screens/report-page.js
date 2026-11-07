/* Concise report actions; the readable report is print-only. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.reportPage = function ({heading,markup,escape,btn,label}) {
 return '<section class="card report report-page"><h2>'+escape(heading)+'</h2><div class="report-preview">'+markup+'</div>'+
 '<div class="actions report-actions">'+btn("print","print","primary-inline")+'</div>'+
 '<div class="actions report-actions">'+btn("back","backToAnswers")+btn("sections","editSections")+'</div></section>';
};
})(globalThis);
