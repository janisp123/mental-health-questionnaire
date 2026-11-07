"use strict";
const fs=require("fs"),vm=require("vm"),path=require("path");
const project=path.resolve(__dirname,"../.."),root={};root.globalThis=root;
vm.runInNewContext(fs.readFileSync(path.join(project,"src/app/core/events.js"),"utf8"),root);
const listeners={},calls=[];
root.QuestionnaireEvents.bind({addEventListener:(name,fn)=>listeners[name]=fn},{
 singleAnswer:value=>calls.push(["single",value]),action:value=>calls.push(["action",value]),
 medicineAction:(action,index)=>calls.push(["medicine",action,index]),jump:id=>calls.push(["jump",id]),
 language:value=>calls.push(["language",value]),medicineChange:()=>calls.push(["medicineChange"]),
 moduleChange:()=>calls.push(["moduleChange"]),restore:file=>calls.push(["restore",file]),
 answerChange:event=>calls.push(["answerChange",event.target.value]),shortTextInput:value=>calls.push(["shortText",value]),
 medicineDiscussionInput:value=>calls.push(["discussion",value]),
});
function emit(type,target,detail=1){let prevented=false;listeners[type]({target,detail,preventDefault:()=>prevented=true});return prevented;}
function target({id="",name="",value="",dataset={},attrs=[],files=[]}={}){
 return {id,name,value,dataset,files,hasAttribute:key=>attrs.includes(key),closest:()=>null};
}
const radio=target({value:"B"}),choice={querySelector:()=>radio};
const single=target();single.closest=selector=>selector===".choice"?choice:null;
assert(!emit("click",single),"allows the browser to show the native radio selection");
assert(calls[0].join("|")==="single|B","delegates one-tap answers");
const add=target({dataset:{act:"addMedicine",medRemove:"2"}});add.closest=selector=>selector==="[data-act]"?add:null;
emit("click",add);assert(calls[1].join("|")==="medicine|addMedicine|2","delegates medicine actions");
const jump=target({dataset:{act:"jump",jump:"04"}});jump.closest=selector=>selector==="[data-act]"?jump:null;
emit("click",jump);assert(calls[2].join("|")==="jump|04","delegates section jumps");
const button=target({dataset:{act:"results"}});button.closest=selector=>selector==="[data-act]"?button:null;
emit("click",button);assert(calls[3].join("|")==="action|results","delegates page actions");
emit("change",target({id:"language",value:"ru"}));
emit("change",target({attrs:["data-med-field"]}));
emit("change",target({attrs:["data-module"]}));
emit("change",target({id:"restore",files:["synthetic.json"]}));
emit("change",target({name:"answer",value:"A"}));
emit("input",target({id:"shortText",value:"synthetic"}));
emit("input",target({attrs:["data-med-field"]}));
emit("input",target({id:"medicineDiscussion",value:"synthetic"}));
assert(calls.slice(4).map(x=>x[0]).join(",")==="language,medicineChange,moduleChange,restore,answerChange,shortText,medicineChange,discussion","routes change and input events");
console.log("PASS: synthetic click/change/input events dispatch to isolated coordinator callbacks.");

function assert(value,message){if(!value)throw new Error(message);}
