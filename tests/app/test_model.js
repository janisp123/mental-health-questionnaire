"use strict";
const fs=require("fs"),vm=require("vm"),path=require("path");
const root={};root.globalThis=root;
const project=path.resolve(__dirname,"../..");
vm.runInNewContext(fs.readFileSync(path.join(project,"src/app/core/model.js"),"utf8"),root);
const q=(id,module,context=null)=>({id,module,context});
const data={groups:[
 {id:"01",required:true,questions:[q("P","01"),q("C","01",{id:"P",showValues:["B"]}),q("H","01",{id:"P",hideValues:["X"]})]},
 {id:"02",required:false,questions:[q("O","02")]},
]};
const model=root.QuestionnaireModel.create(data);
const state={answers:{},selected:[]};
assert(model.all.map(x=>x.id).join(",")==="P,C,H,O","preserves source order");
assert(model.active(state).map(x=>x.id).join(",")==="P,H","hides unmatched conditional and unselected optional group");
state.answers.P={kind:"choice",codes:["A"]};
assert(model.active(state).map(x=>x.id).join(",")==="P,H","showValues hides child when the answer does not match");
state.answers.P={kind:"choice",codes:["B"]};
assert(model.active(state).map(x=>x.id).join(",")==="P,C,H","showValues reveals matching child");
state.answers.P={kind:"choice",codes:["X"]};
assert(model.active(state).map(x=>x.id).join(",")==="P","hideValues hides matching child");
state.answers.P={kind:"choice",codes:["B"]};
state.selected=["02"];
assert(model.active(state).map(x=>x.id).join(",")==="P,C,H,O","selected optional section joins active queue");
assert(model.countGroup(state,"01").total===3,"counts only visible questions");
assert(model.countGroup(state,"01").done===1,"counts saved visible questions");
assert(model.reportQuestions(state).length===4,"reports visible questions across section selection");
let duplicateRejected=false;
try{root.QuestionnaireModel.create({groups:[{id:"01",required:true,questions:[q("D","01"),q("D","01")]}]});}catch(e){duplicateRejected=true;}
assert(duplicateRejected,"rejects duplicate question IDs");
console.log("PASS: synthetic question visibility, queue, section selection, progress, and ID uniqueness.");

function assert(value,message){if(!value)throw new Error(message);}
