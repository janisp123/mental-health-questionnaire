"use strict";
const assert = require("node:assert/strict");

require("../../src/app/screens/start.js");
require("../../src/app/screens/section-selector.js");
const screens = globalThis.QuestionnaireScreens;
const labels = {
  intro: "Synthetic introduction", reviewNote: "Synthetic review note",
  selector: "Choose sections", selectIntro: "Select any sections",
  sectionProgress: "{total} questions · completed: {completed}",
  chooseAllAndContinue: "Select all and continue", continueSelected: "Continue with selected sections",
  cancel: "Back", start: "Start", jump: "Go to section",
};
const label = key => labels[key] || key;
const btn = (action, key, cls = "", extra = "") =>
  `<button data-act="${action}" class="${cls}" ${extra}>${label(key)}</button>`;

const start = screens.start({label, btn});
assert.match(start, /Synthetic introduction/);
assert.match(start, /data-act="start"/);
assert.doesNotMatch(start, /data-act="all"|data-act="choose"|data-act="guide"/);
assert.equal((start.match(/<button/g)||[]).length, 1);

const groups = new Map([[
  "S01", {id:"S01", required:false},
]]);
const data = {groups:[
  {id:"S01", required:false, questionCount:35, titles:{lv:"Ikdiena"}},
]};
const state = {screen:"selector", lang:"lv", sectionDraft:["S01"], selected:["S01"], answers:{}};
const selector = screens.sectionSelector({
  state, data, groups, label, btn, escape:value=>String(value),
  countGroup:()=>({done:2,total:1}), active:()=>[],
});
assert.match(selector, /data-act="all"/);
assert.match(selector, /data-act="confirm"/);
assert.match(selector, /data-module="S01"[^>]*checked/);
assert.match(selector, /35 questions · completed: 2/);
assert.doesNotMatch(selector, /0\/1|notSelected|clearSections/);
assert.match(selector, /data-act="jump"/);

console.log("PASS: start contains one button; section picker offers select-all/continue, selected-section continue and useful totals.");
