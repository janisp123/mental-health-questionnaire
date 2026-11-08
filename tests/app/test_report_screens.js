"use strict";
const assert = require("node:assert/strict");
require("../../src/app/screens/results.js");
require("../../src/app/screens/report-page.js");
const screens = globalThis.QuestionnaireScreens;
const labels = {
  countDone:"Completed", results:"Finished", doctorDisclaimer:"Review with a professional",
  noneFlagged:"No feedback yet", specialist:"Doctor report", feedbackProjectReport:"Prepare feedback report",
  back:"Back", editSections:"Edit sections", new:"Start over", print:"Print / save PDF", backToAnswers:"Back to answers",
};
const label = key => labels[key] || key;
const btn = (action,key,cls="") =>
  '<button data-act="'+action+'" class="'+cls+'">'+label(key)+'</button>';
const escape = value => String(value ?? "").replace(/&/g,"&amp;").replace(/</g,"&lt;");

const results = screens.results({
  label,btn,counts:{answered:2,skipped:1,unanswered:3,completed:3},
  selected:"",
  reportLanguageOptions:'<option value="lv">Latviešu</option>',
});
assert.match(results,/Completed <b>3<\/b>/);
assert.doesNotMatch(results,/Open|unanswered|Synthetic section|review@example\.test/);
assert.match(results,/data-act="feedbackReport"/);
assert.doesNotMatch(results,/copyFeedback|<textarea/);
assert.match(results,/data-act="doctor"/);
assert.match(results,/<select id="report-language"><option value="lv">Latviešu<\/option><\/select>/);

const report = screens.reportPage({
  heading:"Doctor report",locale:"lv",markup:"<p>Synthetic report</p>",btn,escape,
});
assert.match(report,/Synthetic report/);
assert.match(report,/class="report-preview" lang="lv"/);
assert.match(report,/data-act="print"/);
assert.match(report,/data-act="back"/);
assert.match(report,/data-act="sections"/);
assert.doesNotMatch(report,/data-act="copyDoctor"|data-act="downloadReport"|<textarea/);

console.log("PASS: completion page omits contact details; report page exposes only print, answers, and sections.");
