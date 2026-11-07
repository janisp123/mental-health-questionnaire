"use strict";
const assert = require("node:assert/strict");
require("../../src/app/screens/feedback.js");
require("../../src/app/screens/medicine.js");
require("../../src/app/screens/question.js");
const screens = globalThis.QuestionnaireScreens;
const labels = {
  feedbackQuestion:"Question wording", feedbackLanguage:"Language", feedbackAnswerPrefix:"Answer",
  feedbackOther:"Other", feedbackTitle:"Report a problem", feedbackComment:"Comment",
  optionalText:"Optional", feedbackPrivacy:"No medical answers are included",
  feedbackContinue:"Save and continue", removeFeedback:"Remove feedback", feedbackFlag:"Flag question",
  feedbackFlagged:"Feedback added", enterText:"Your answer", saveWarning:"Save your answer",
  autoHint:"Choose one answer", multiHint:"Vari izvēlēties vairākas atbildes.",
  multiMaxHint:"Vari izvēlēties ne vairāk kā {count} atbildes.",
  next:"Save and continue", skipSection:"Skip section", skipRest:"Finish",
};
const label = key => labels[key] || key;
const btn = (action,key,cls="",extra="") =>
  '<button type="button" data-act="'+action+'" class="'+cls+'" '+extra+'>'+label(key)+'</button>';
const escape = value => String(value ?? "").replace(/&/g,"&amp;").replace(/</g,"&lt;");

const feedback = screens.feedback({
  q:{id:"SYN_01",choiceCodes:["A","B"]},
  t:{choices:{A:"Often",B:"Never"}},
  ui:{feedbackAnswerPrefix:"Answer"},
  state:{feedbackOpen:true,feedback:{SYN_01:{reasons:["answer:B"],comment:"Synthetic note"}}},
  label,escape,btn,
});
assert.match(feedback,/data-feedback-reason="answer:B" checked/);
assert.match(feedback,/Synthetic note/);
assert.match(feedback,/data-act="removeFeedback"/);
assert.equal(screens.feedback({q:{id:"SYN_01"},state:{feedbackOpen:false},label,escape,btn}),"");

const medicine = screens.medicine({
  medicine:{help:"Help",entry:"Medicine",fields:{name:"Name",dose:"Dose",status:"Status",benefit:"Effect"},status:{current:"Current",past:"Past",unknown:"Unknown"},benefits:{better:"Better"},remove:"Remove",add:"Add",discussion:"Discuss",select:"Select"},
  draft:{records:[{name:"Example",dose:"10 mg",status:"current",benefit:"better"}],discussion:"Synthetic discussion"},
  medicineFields:["name","dose","status","benefit"],escape,
});
assert.match(medicine,/data-med-field="name" value="Example"/);
assert.match(medicine,/data-med-field="status"/);
assert.match(medicine,/Synthetic discussion/);

const q = {
  id:"SYN_01",type:"choice",multi:false,choiceCodes:["A","B"],
  translations:{lv:{title:"Synthetic question",time:"Past week",help:"Synthetic help",choices:{A:"Often",B:"Never"}}},
};
const question = screens.question({
  q,state:{lang:"lv",draft:{codes:["A"]},feedback:{},feedbackOpen:false},
  ui:{},queue:[q],group:"Synthetic section",label,btn,escape,
  renderFeedback:()=>"<fieldset>Feedback control</fieldset>",renderMedicine:()=>"",
});
assert.match(question,/Synthetic question/);
assert.match(question,/value="A" checked/);
assert.match(question,/Feedback control/);
assert.match(question,/data-act="skipSection"/);

const multi = {...q,multi:true,maxChoices:3};
const multiQuestion = screens.question({
  q:multi,state:{lang:"lv",draft:{codes:[]},feedback:{},feedbackOpen:false},ui:{},queue:[multi],
  group:"Synthetic section",label,btn,escape,renderFeedback:()=>"",renderMedicine:()=>"",
});
assert.match(multiQuestion,/ne vairāk kā 3 atbildes/);
assert.match(multiQuestion,/selection-hint/);

const unlimited = {...multi}; delete unlimited.maxChoices;
const unlimitedQuestion = screens.question({
  q:unlimited,state:{lang:"lv",draft:{codes:[]},feedback:{},feedbackOpen:false},ui:{},queue:[unlimited],
  group:"Synthetic section",label,btn,escape,renderFeedback:()=>"",renderMedicine:()=>"",
});
assert.match(unlimitedQuestion,/Vari izvēlēties vairākas atbildes\./);
assert.doesNotMatch(unlimitedQuestion,/ne vairāk kā/);

console.log("PASS: question, medicine, and feedback screens render from synthetic records.");
