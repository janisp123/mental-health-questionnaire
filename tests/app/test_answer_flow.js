"use strict";
const fs=require("fs"),vm=require("vm"),path=require("path");
const project=path.resolve(__dirname,"../.."),root={};root.globalThis=root;
vm.runInNewContext(fs.readFileSync(path.join(project,"src/app/core/answer-flow.js"),"utf8"),root);
const questions=[{id:"A"},{id:"B"},{id:"C"}];
const state={currentId:"A"};
assert(root.QuestionnaireFlow.next(state,questions).id==="B","advances in active order");
state.currentId="C";
assert(root.QuestionnaireFlow.next(state,questions).screen==="results","finishes after final active item");
assert(root.QuestionnaireFlow.previous(state,questions).id==="B","moves to the previous active item");
state.currentId="A";
assert(root.QuestionnaireFlow.previous(state,questions).screen==="start","returns to start before first item");

state.currentId="A";state.reviewQueue=["A","C"];state.reviewReturn={screen:"question",id:"B"};
assert(root.QuestionnaireFlow.afterSave(state,questions).id==="C"&&state.reviewQueue.length===1,"continues ordered safety review");
state.currentId="C";
assert(root.QuestionnaireFlow.afterSave(state,questions).id==="B"&&state.reviewQueue===null,"returns to the original question after review");
state.currentId="A";state.reviewQueue=["A"];state.reviewReturn={screen:"results",id:"C"};
const result=root.QuestionnaireFlow.afterSave(state,questions);
assert(result.screen==="results"&&result.currentId==="C"&&result.clearDraft,"returns to non-question screen after review");
console.log("PASS: synthetic answer advancement, back navigation, and safety review transitions.");

function assert(value,message){if(!value)throw new Error(message);}
