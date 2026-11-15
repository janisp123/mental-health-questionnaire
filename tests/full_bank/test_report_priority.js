/* Review ordering must preserve every included response and never mutate saved data. */
const fs=require('fs'),vm=require('vm'),assert=require('node:assert/strict'),cp=require('child_process');
const data=JSON.parse(cp.execFileSync('python',['-c','import sys,json;sys.path.insert(0,"tools");from build_questionnaire import build_bundle;print(json.dumps(build_bundle()))'],{maxBuffer:10e6}));
const context={window:{}};
if(fs.existsSync('src/app/reports/review-priority.js'))vm.runInNewContext(fs.readFileSync('src/app/reports/review-priority.js','utf8'),context);
vm.runInNewContext(fs.readFileSync('src/app/reports/reports.js','utf8'),context);
const r=context.window.QuestionnaireReports,qs=data.groups.flatMap(g=>g.questions),policy=data.presentation.reportPriority;
const q=id=>qs.find(item=>item.id===id);
const answers={M33_01:{kind:'text',value:'SYNTHETIC MAIN CONCERN'},M14_09:{kind:'choice',codes:['B'],status:'answered'},M15_19:{kind:'choice',codes:['B'],status:'answered'},M06_02:{kind:'choice',codes:['B'],status:'answered'},M06_03:{kind:'choice',codes:['A'],status:'answered'},M06_07:{kind:'choice',codes:['A'],status:'answered'},M05_14:{kind:'choice',codes:['E'],status:'answered'},M02_01:{kind:'choice',codes:['A'],status:'answered'},M23_07:{kind:'choice',codes:['A'],status:'answered'},M43_01:{kind:'choice',codes:['E'],status:'answered'},M14_01:{kind:'choice',codes:['A'],status:'answered'},M31_09:{kind:'choice',codes:['C'],status:'uncertain'},M31_10:{kind:'choice',codes:['D'],status:'refused'},M23_11:{kind:'skip',status:'skipped'}};
const snapshot=JSON.stringify({qs,answers,presentation:data.presentation});
const legacy={...data.presentation};delete legacy.reportPriority;
let expectedIds;
for(const locale of Object.keys(data.ui)){
 const before=r.entries(qs,answers,locale,legacy,data.ui[locale].medicine);
 const after=r.entries(qs,answers,locale,data.presentation,data.ui[locale].medicine);
 const canonical=entries=>JSON.stringify([...entries].sort((a,b)=>a.id.localeCompare(b.id)));
 assert.equal(canonical(before),canonical(after),'Sorting must preserve the complete id/plain/html/index/topic payload');
 assert.notDeepEqual(after.map(e=>e.id),before.map(e=>e.id),'Priority ordering must replace the old topic-only order');
 const ids=Array.from(after,e=>e.id);if(expectedIds)assert.deepEqual(ids,expectedIds);else expectedIds=ids;
 const position=id=>ids.indexOf(id);
 assert(position('M15_19')<position('M14_09'),'Current severe withdrawal cue precedes supporting history');
 assert(position('M06_02')<position('M33_01'),'Current intent precedes routine concern text');
 assert.equal(Math.abs(position('M06_02')-position('M06_03')),1,'Linked current safety answers remain adjacent');
 assert(position('M31_09')>position('M06_02'),'Uncertainty remains distinct from affirmative urgent cue');
 assert(position('M31_10')>position('M06_02'),'Refusal is retained without becoming affirmative urgency');
 assert(position('M43_01')>position('M05_14'),'Positive wellbeing is not mistaken for high symptom frequency');
 const text=r.doctorText(qs,answers,locale,data.ui[locale],data.presentation),html=r.doctorHtml(qs,answers,locale,data.ui[locale],data.presentation);
 assert(text.includes(data.ui[locale].reportOrderNote));
 for(let i=1;i<after.length;i++){
  assert(text.indexOf(after[i-1].plain)<text.indexOf(after[i].plain));
  assert(html.indexOf(after[i-1].html.replace(/\n/g,'<br>'))<html.indexOf(after[i].html.replace(/\n/g,'<br>')));
 }
 assert.deepEqual(Array.from(r.entries(qs,answers,locale,data.presentation,data.ui[locale].medicine),e=>e.id),ids,'Order is deterministic');
}
assert.equal(JSON.stringify({qs,answers,presentation:data.presentation}),snapshot,'Report generation must not mutate source questions, priorities or saved answers');
assert(policy,'Complete ID/code policy is embedded');
const priority=context.window.QuestionnaireReviewPriority;
for(const [id,codes,value] of [['M06_02',['B'],5],['M06_02',['A'],1],['M06_02',['C'],3],['M06_02',['D'],3],['M06_03',['A'],5],['M06_03',['B'],1],['M15_19',['B'],5],['M15_18',['B'],4],['M06_09',['A'],5],['M06_09',['E'],3],['M43_01',['A'],3],['M43_01',['E'],1]]){
 assert.equal(priority.responsePriority(q(id),{kind:'choice',codes},policy),value,id+': '+codes);
}
console.log('PASS: report-only priority, response conservation, safety/context order, stable ties, all locales and nonmutation.');
const simpleQuestions=['one','five','three','two','four'].map(id=>({id}));
const simpleEntries=simpleQuestions.map(q=>({id:q.id}));
const simpleAnswers=Object.fromEntries(simpleQuestions.map(q=>[q.id,{kind:'choice',codes:['A']}]));
const simplePolicy={questions:Object.fromEntries(simpleQuestions.map((q,i)=>[q.id,{default:[1,5,3,2,4][i],answers:{A:[1,5,3,2,4][i]}}])),relatedGroups:{}};
assert.deepEqual(Array.from(priority.sortEntries(simpleEntries,simpleQuestions,simpleAnswers,simplePolicy),e=>e.id),['five','four','three','two','one']);
assert.deepEqual(Array.from(priority.sortEntries(simpleEntries,simpleQuestions,simpleAnswers,null),e=>e.id),['one','five','three','two','four']);
const siblings=[{id:'one',context:{id:'absent_parent'}},{id:'five',context:{id:'absent_parent'}},{id:'four'}];
assert.deepEqual(Array.from(priority.sortEntries(siblings.map(q=>({id:q.id})),siblings,simpleAnswers,simplePolicy),e=>e.id),['one','five','four'],'Included sibling context stays together even when its parent is not in the report');

// Every coded response in every active locale keeps exactly the same report payload.
for(const locale of Object.keys(data.ui)){
 for(let slot=0;slot<Math.max(...qs.map(q=>q.choiceCodes.length));slot++){
  const batch=Object.fromEntries(qs.filter(q=>q.choiceCodes[slot]).map(q=>[q.id,{kind:'choice',codes:[q.choiceCodes[slot]]}]));
  const snapshot=JSON.stringify(batch);
  const original=r.entries(qs,batch,locale,legacy,data.ui[locale].medicine);
  const reordered=r.entries(qs,batch,locale,data.presentation,data.ui[locale].medicine);
  const canonical=rows=>JSON.stringify([...rows].sort((a,b)=>a.id.localeCompare(b.id)));
  assert.equal(canonical(reordered),canonical(original),locale+' code-slot '+slot+' lost or changed a response');
  assert.equal(JSON.stringify(batch),snapshot);
 }
}
console.log('PASS: every coded choice is preserved verbatim in every active language.');
// Directional regressions from independent policy review: protective and graded choices.
for(const [id,codes,expected] of [
 ['M19_10',['A'],3],['M19_10',['B'],1],['M19_15',['A'],1],['M19_15',['B'],3],
 ['M27_16',['A'],1],['M27_16',['B'],5],
 ['M11_15',['A'],3],['M11_15',['B'],1],['M12_09',['A'],3],['M12_09',['B'],1],['M22_09',['A'],3],['M22_09',['B'],1],
 ['M23_24',['A'],1],['M23_24',['B'],3],['M23_24',['C'],4],['M23_24',['D'],4],
 ['M13_19',['E'],4],['M02_15',['E'],4],['M22_13',['E'],4],
 ['M01_05',['A'],2],['M01_05',['B'],2],['M14_04',['A'],2],['M14_04',['C'],2],['M14_04',['D'],1]
])assert.equal(priority.responsePriority(q(id),{kind:'choice',codes},policy),expected,id+': '+codes);
for(const id of ['M23_24','M13_19','M02_15','M22_13']){
 const codes=id==='M23_24'?['A','B','C','D']:['A','B','C','D','E'];
 const values=codes.map(code=>priority.responsePriority(q(id),{kind:'choice',codes:[code]},policy));
 assert(values.every((v,i)=>i===0||v>=values[i-1]),id+' must not move later for greater stated impact/dependence');
}
console.log('PASS: reviewed protective, functional-impact, dependence and supporting-context directions.');
