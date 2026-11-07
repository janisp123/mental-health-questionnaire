"use strict";
const assert = require("node:assert/strict");
require("../../src/app/screens/results.js");
require("../../src/app/screens/report-page.js");
const screens = globalThis.QuestionnaireScreens;
const labels = {
  countDone:"Completed", countSkip:"Skipped", countOpen:"Open", results:"Finished",
  doctorDisclaimer:"Review with a professional", noneFlagged:"No feedback yet",
  feedbackContactLabel:"Contact", specialist:"Doctor report", feedbackProjectCopy:"Copy project feedback",
  back:"Back", editSections:"Edit sections", new:"Start over", copyDoctor:"Copy",
  print:"Print", downloadReport:"Download", backToAnswers:"Answers",
};
const label = key => labels[key] || key;
const btn = (action,key,cls="",extra="") =>
  '<button data-act="'+action+'" class="'+cls+'" '+extra+'>'+label(key)+'</button>';
const escape = value => String(value ?? "").replace(/&/g,"&amp;").replace(/</g,"&lt;");

const results = screens.results({
  label,btn,escape,counts:{answered:2,skipped:1,unanswered:3,completed:3},
  selected:"",
  feedbackText:"Synthetic project feedback only",feedbackEmail:"review@example.test",
});
assert.match(results,/Completed <b>3<\/b>/);
assert.doesNotMatch(results,/Open|unanswered|Synthetic section/);
assert.match(results,/review@example.test/);
assert.match(results,/Synthetic project feedback only/);
assert.match(results,/data-act="copyFeedback"/);
assert.match(results,/data-act="doctor"/);

const report = screens.reportPage({
  heading:"Doctor report",markup:"<p>Synthetic report</p>",plain:"Plain report",
  label,btn,escape,
});
assert.match(report,/Synthetic report/);
assert.match(report,/Plain report/);
assert.match(report,/data-act="print"/);
assert.match(report,/data-act="sections"/);

console.log("PASS: completion and doctor-report pages render independently.");
