/* Report rules are explicit and must never produce a score or coded export. */
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const cp=require('child_process');
const data=JSON.parse(cp.execFileSync('python',['-c','import sys,json;sys.path.insert(0,"tools");from build_pilot import build_bundle;print(json.dumps(build_bundle()))'],{maxBuffer:8e6}));
const context={window:{}};vm.runInNewContext(fs.readFileSync('src/pilot/reports/reports.js','utf8'),context);
const r=context.window.PilotReports,qs=data.groups.flatMap(g=>g.questions),q=id=>qs.find(q=>q.id===id);
const answers={M33_01:{kind:'text',value:'Synthetic'},M06_02:{kind:'choice',codes:['B'],status:'answered'},M06_01:{kind:'choice',codes:['A'],status:'answered'},M02_09:{kind:'choice',codes:['A'],status:'answered'},M23_11:{kind:'choice',codes:['A'],status:'answered'}};
assert.deepEqual(Object.keys(data.presentation).sort(),['boldAnswers','feedbackContactEmail','purpose','questions','schema','topicOrder']);
assert(!/"[^"]*weight[^"]*"\s*:/i.test(JSON.stringify(data)));
for(const lang of ['lv','en','ru']){
 const entries=r.entries(qs,answers,lang,data.presentation);
 assert.deepEqual(entries.map(e=>e.id),['M33_01','M23_11','M02_09','M06_01','M06_02']);
 const plain=r.doctorText(qs,answers,[],lang,data.ui[lang],data.groups,data.presentation);
 const html=r.doctorHtml(qs,answers,[],lang,data.ui[lang],data.groups,data.presentation);
 assert(plain.includes(q('M06_02').translations[lang].choices.B));
 assert(!/M06_02|\[B\]|\bweight\b|risk score/i.test(plain));
 assert(html.includes('<strong>'+q('M06_02').translations[lang].choices.B+'</strong>'));
 assert(!html.includes('<strong>'+q('M06_01').translations[lang].choices.A+'</strong>'));
 assert(!html.includes('<strong>'+q('M02_09').translations[lang].choices.A+'</strong>'));
}
for(const [id,codes] of Object.entries(data.presentation.boldAnswers)){
 const question=q(id);assert(question,id);
 assert(codes.length>0&&new Set(codes).size===codes.length,id);
 assert(codes.every(c=>question.choiceCodes.includes(c)),id);
}
const feedback={M02_01:{reasons:['question','answer:B'],comment:'Synthetic wording note',language:'en',version:'v0.2',updatedAt:'2026-11-06T12:00:00Z'}};
const feedbackEntries=r.feedbackEntries(qs,feedback,data.ui);
assert.equal(feedbackEntries.length,1);
assert.equal(feedbackEntries[0].id,'M02_01');
assert(feedbackEntries[0].plain.includes(q('M02_01').translations.en.title));
assert(feedbackEntries[0].plain.includes(q('M02_01').translations.en.choices.B));
const projectText=r.projectFeedbackText(qs,feedback,'en',data.ui,'janis.paegle.email@gmail.com','v0.2');
assert(projectText.includes('janis.paegle.email@gmail.com'));
assert(projectText.includes('M02_01')&&projectText.includes('Synthetic wording note'));
assert(!projectText.includes('PRIVATE_MEDICAL_SENTINEL'));
const emptyFeedback=r.projectFeedbackText(qs,{},'en',data.ui,'janis.paegle.email@gmail.com','v0.2');
assert(emptyFeedback.includes(data.ui.en.feedbackNone));
assert(emptyFeedback.includes('janis.paegle.email@gmail.com'));
const doctorWithFeedback=r.doctorText(qs,answers,[], 'en',data.ui.en, data.groups,data.presentation,feedback,qs);
assert(doctorWithFeedback.indexOf(data.ui.en.feedbackSectionHeading)<doctorWithFeedback.indexOf('Synthetic'));
assert(doctorWithFeedback.indexOf(data.ui.en.feedbackSectionHeading)<doctorWithFeedback.indexOf(r.entries(qs,answers,'en',data.presentation)[0].plain));
const html=cp.execFileSync('python',['-c','import sys;sys.path.insert(0,"tools");from build_pilot import make_html;print(make_html())'],{encoding:'utf8',maxBuffer:8e6});
for(const word of ['Prepare answers for AI','Copy coded answers for AI','DECODING KEY','aiInstruction','copyAI'])assert(!html.includes(word),word);
console.log('PASS: one doctor report, explicit answer-code bold rules, normal-to-sensitive order, three locales, no AI export or weights.');
