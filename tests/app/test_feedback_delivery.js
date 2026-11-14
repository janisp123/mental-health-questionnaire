"use strict";
const assert = require("node:assert/strict");
global.window = globalThis;
require("../../src/app/reports/reports.js");
require("../../src/app/reports/feedback-delivery.js");
const delivery = globalThis.QuestionnaireFeedbackDelivery;
const catalogs = {en:{feedbackProjectHeading:"Feedback",feedbackVersionLabel:"Version",feedbackContactLabel:"Contact",feedbackQuestion:"Unclear",feedbackReasonLabel:"Reason",feedbackComment:"Comment",feedbackNone:"None"}};
const questions = [{id:"Q1",translations:{en:{title:"Question?",choices:{}}}}];
const feedback = {Q1:{language:"en",version:"test",reasons:["question"],comment:"LV ā & RU ё UK ї + #?\nLine",answers:"PRIVATE_ANSWER",name:"PRIVATE_NAME"}};
const result = delivery.compose(questions,feedback,"en",catalogs,"review@example.test","test");
assert.ok(result.url.startsWith("mailto:review@example.test?"));
const params = new URLSearchParams(result.url.split("?")[1]);
assert.equal(params.get("subject"),"MH_TEST — Feedback");
assert.ok(params.get("body").includes(feedback.Q1.comment.replace(/\n/g,"\r\n")));
assert.ok(params.get("body").includes("Q1"));
assert.ok(!/PRIVATE_ANSWER|PRIVATE_NAME/.test(result.text));
assert.equal(delivery.compose(questions,{},"en",catalogs,"review@example.test","test").url,null);
const long = delivery.compose(questions,{Q1:{...feedback.Q1,comment:"ї".repeat(4000)}},"en",catalogs,"review@example.test","test");
assert.equal(long.url,null);
assert.ok(long.text.includes("ї".repeat(4000)));
for(const email of ["bad\r\nBcc:other@example.test","x@example.test?bcc=bad",""]){
 assert.equal(delivery.compose(questions,feedback,"en",catalogs,email,"test").url,null);
}
const broken = delivery.compose(questions,{Q1:{...feedback.Q1,comment:"emoji cut \ud83d"}},"en",catalogs,"review@example.test","test");
assert.ok(broken.url);
assert.ok(new URLSearchParams(broken.url.split("?")[1]).get("body").includes("emoji cut \ufffd"));
console.log("PASS: feedback delivery encodes Unicode, excludes non-feedback fields and preserves oversized text.");
