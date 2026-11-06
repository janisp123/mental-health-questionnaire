/* Doctor report page controls around the separately generated report. */
(function (root) {
"use strict";
const screens = root.QuestionnaireScreens = root.QuestionnaireScreens || {};
screens.reportPage = function ({heading,markup,plain,escape,btn,label}) {
 return '<section class="card report"><h2>'+escape(heading)+'</h2><div class="report-preview">'+markup+'</div><textarea id="reportText" class="copy-source" readonly aria-hidden="true" tabindex="-1">'+escape(plain)+'</textarea>'+
 '<div class="actions">'+btn("copyDoctor","copyDoctor","primary-inline")+btn("print","print")+btn("downloadReport","downloadReport")+'</div>'+
 '<div class="actions">'+btn("resultScreen","backToAnswers")+btn("sections","editSections")+'</div></section>';
};
})(globalThis);
