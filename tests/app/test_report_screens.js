"use strict";
const assert = require("node:assert/strict");
require("../../src/app/screens/results.js");
require("../../src/app/screens/report-page.js");
const screens = globalThis.QuestionnaireScreens;
const labels = {
  countDone:"Answered", reportCountSelected:"Covered",reportCountDone:"Answered",reportCountSkip:"Skipped",coverageNote:"Selected questions plus earlier saved responses",results:"Finished", doctorDisclaimer:"Review with a professional",
  noneFlagged:"No feedback yet", specialist:"Generate report", feedbackProjectReport:"Prepare feedback report",
  back:"Back", editSections:"Edit sections", new:"Start over", print:"Print / save PDF", backToAnswers:"Back to answers",
};
const label = key => labels[key] || key;
const btn = (action,key,cls="") =>
  '<button data-act="'+action+'" class="'+cls+'">'+label(key)+'</button>';
const escape = value => String(value ?? "").replace(/&/g,"&amp;").replace(/</g,"&lt;");

const results = screens.results({
  label,btn,counts:{selected:6,answered:2,skipped:1,unanswered:3,completed:3},
  selected:"",
  reportLanguageOptions:'<option value="lv">Latviešu</option>',
});
assert.match(results,/Covered <b>6<\/b>/);
assert.match(results,/Answered <b>2<\/b>/);
assert.match(results,/Skipped <b>1<\/b>/);
assert.match(results,/Selected questions plus earlier saved responses/);
assert.doesNotMatch(results,/Open|unanswered|Synthetic section|review@example\.test/);
assert.doesNotMatch(results,/data-act="feedbackReport"/);
assert.doesNotMatch(results,/copyFeedback|<textarea/);
assert.match(results,/data-act="doctor"[^>]*>Generate report<\/button>/);
assert.match(results,/<select id="report-language"><option value="lv">Latviešu<\/option><\/select>/);

const report = screens.reportPage({
  heading:"Doctor report",locale:"lv",markup:"<p>Synthetic report</p>",btn,escape,label,
});
assert.match(report,/Synthetic report/);
assert.match(report,/class="report-preview" lang="lv"/);
assert.match(report,/data-act="print"/);
assert.match(report,/data-act="new"/);
assert.match(report,/data-act="shareQuestionnaire"/);
assert.match(report,/data-act="back"/);
assert.match(report,/data-act="sections"/);
assert.match(report,/data-act="resultScreen"/);
assert.doesNotMatch(report,/data-act="feedbackReport"/);
assert.doesNotMatch(report,/data-act="copyDoctor"|data-act="downloadReport"|<textarea/);

const flaggedReport = screens.reportPage({
  heading:"Doctor report",locale:"lv",markup:"<p>Synthetic report</p>",btn,escape,label,hasFeedback:true,
});
assert.match(flaggedReport,/data-act="feedbackReport"/);

const feedback = screens.reportPage({
  locale:"en",markup:"<p>Synthetic project feedback</p>",btn,escape,label,
  feedbackEmail:"review@example.test",
});
assert.match(feedback,/class="report-preview feedback-report" lang="en"/);
assert.match(feedback,/data-act="sendFeedback"/);
assert.match(feedback,/data-act="copyFeedback"/);
assert.match(feedback,/id="feedback-copy"/);
assert.match(feedback,/data-act="print"/);
assert.match(feedback,/data-act="doctor"/);

console.log("PASS: one Generate report action; only flagged clinician reports offer project feedback.");

const empty=screens.reportPage({heading:"Doctor report",locale:"en",markup:"No answers",btn,escape,label,hasAnswers:false});
assert.doesNotMatch(empty,/data-act="print"/);
assert.match(empty,/data-act="back"/);
assert.match(empty,/data-act="new"/);
