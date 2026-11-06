/* Pure report acceptance checks: synthetic responses only. */
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const cp=require('child_process');
const data=JSON.parse(cp.execFileSync('python',['-c','import sys,json;sys.path.insert(0,"tools");from build_pilot import build_bundle;print(json.dumps(build_bundle()))'],{maxBuffer:8e6}));
const context={window:{}};vm.runInNewContext(fs.readFileSync('src/pilot/reports/reports.js','utf8'),context);
const r=context.window.PilotReports,qs=data.groups.flatMap(g=>g.questions),q=id=>qs.find(q=>q.id===id);
const answer=(id,codes)=>({kind:'choice',codes,status:codes.some(c=>q(id).answerStatus[c]==='refused')?'refused':codes.some(c=>q(id).answerStatus[c]==='uncertain')?'uncertain':'answered'});
const answers={M33_01:{kind:'text',value:'<Synthetic & example>',status:'answered'},M06_02:answer('M06_02',['B']),M02_03:answer('M02_03',['B']),M02_02:answer('M02_02',['D']),M06_01:answer('M06_01',['A']),M02_11:answer('M02_11',['C']),M02_12:answer('M02_12',['J']),M02_01:{kind:'skip',status:'skipped'},M21_06:answer('M21_06',['A','B'])};
assert.equal(r.priority(q('M06_02'),answers.M06_02,data.presentation),3);
assert.equal(r.priority(q('M06_01'),answers.M06_01,data.presentation),0);
assert.equal(r.priority(q('M02_11'),answers.M02_11,data.presentation),null);
assert.equal(r.priority(q('M02_01'),answers.M02_01,data.presentation),null);
assert.equal(r.priority(q('M02_04'),undefined,data.presentation),null);
assert.equal(r.priority(q('M06_03'),answer('M06_03',['A']),data.presentation),3);
assert.equal(r.priority(q('M06_03'),answer('M06_03',['B']),data.presentation),0);
for(const lang of ['lv','en','ru']){
 const args=[qs,answers,[],lang,data.ui[lang],data.groups,data.presentation];
 const ai=r.aiText(...args),doc=r.doctorText(...args),html=r.doctorHtml(...args);
 for(const text of [ai,doc]){
  assert(!/M\d\d_|"codes"|DECODING KEY/.test(text));
  assert(!text.includes(q('M02_01').translations[lang].title));
  for(const [id,a] of Object.entries(answers))if(a.kind==='choice'){
   const t=q(id).translations[lang];
   for(const c of a.codes) assert(text.includes(t.choices[c]),id+'/'+lang+'/'+c);
   assert(text.includes(t.time),id+' time');
  }
 }
 const entries=r.entries(qs,answers,lang,data.presentation,true);
 const pos=id=>entries.findIndex(e=>e.id===id);
 assert(pos('M06_01')<pos('M02_03'));
 assert(pos('M02_03')<pos('M02_02'));
 assert(pos('M02_02')<pos('M06_02'));
 assert(pos('M33_01')<pos('M06_01'));
 assert(pos('M33_01')<pos('M06_02'));
 assert(!html.includes('<Synthetic'));assert(html.includes('&lt;Synthetic &amp; example&gt;'));
 assert(!/risk score|risk percentage|High attention|weight:/.test(doc));
 assert(ai.endsWith(data.ui[lang].aiInstruction));
}
// Every active source answer has an explicit, reviewable priority (null for unknown/refused).
for(const question of qs){
 const rule=data.presentation.questions[question.id];assert(rule,question.id);
 assert.deepEqual(Object.keys(rule.weights).sort(),question.choiceCodes.slice().sort());
 for(const c of question.choiceCodes){
  const v=rule.weights[c];assert(v===null||[0,1,2,3].includes(v));
  if(['uncertain','refused'].includes(question.answerStatus[c]))assert.equal(v,null);
 }
}
console.log('PASS: self-contained reports, actual answer text/time, ascending priorities, unrated states, escaping, all three languages.');
