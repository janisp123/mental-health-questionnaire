"use strict";
const assert = require("node:assert/strict");

require("../../src/app/screens/start.js");
require("../../src/app/screens/section-selector.js");
const screens = globalThis.QuestionnaireScreens;
const labels = {
  intro: "Synthetic introduction",
  reviewNote: "Synthetic review note",
  noAuto: "Synthetic privacy note",
  selector: "Choose sections",
  selectIntro: "Select any sections",
  guideIntro: "Suggested sections",
  selected: "Selected",
  notSelected: "Not selected",
  chooseAll: "All",
  clearSections: "Clear",
  confirmSections: "Continue",
  cancel: "Back",
  chooseOwn: "Choose",
  chooseGuide: "Guide",
  start: "Start",
  jump: "Go to section",
};
const label = key => labels[key] || key;
const btn = (action, key, cls = "", extra = "") =>
  `<button data-act="${action}" class="${cls}" ${extra}>${label(key)}</button>`;

const start = screens.start({label, btn});
assert.match(start, /Synthetic introduction/);
assert.match(start, /data-act="start"/);
assert.match(start, /Synthetic privacy note/);

const groups = new Map([
  ["01", {id:"01", required:true}],
  ["02", {id:"02", required:false}],
]);
const data = {groups:[
  {id:"01", required:true, titles:{lv:"Ikdiena"}, concerns:{lv:"Ikdiena"}},
  {id:"02", required:false, titles:{lv:"Labsajūta"}, concerns:{lv:"Grūtību pazīmes"}},
]};
const state = {screen:"selector", lang:"lv", sectionDraft:["02"], selected:["02"], answers:{}};
const selector = screens.sectionSelector({
  state, data, groups, label, btn, escape:value=>String(value),
  countGroup:()=>({done:0,total:1}), active:()=>[],
});
assert.match(selector, /Ikdiena/);
assert.match(selector, /Labsajūta/);
assert.match(selector, /data-module="02"[^>]*checked/);
assert.match(selector, /data-act="jump"/);
assert.match(selector, /data-act="confirm"/);

state.screen = "guide";
const guide = screens.sectionSelector({
  state, data, groups, label, btn, escape:value=>String(value),
  countGroup:()=>({done:0,total:1}), active:()=>[],
});
assert.match(guide, /Grūtību pazīmes/);
assert.doesNotMatch(guide, /data-act="jump"/);

console.log("PASS: start and section-picker screens render independently with synthetic content.");
