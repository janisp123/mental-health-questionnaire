/* Medicine-list report stays compact, localized, and safely escaped. */
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const cp=require('child_process');
const data=JSON.parse(cp.execFileSync('python',['-c','import sys,json;sys.path.insert(0,"tools");from build_questionnaire import build_bundle;print(json.dumps(build_bundle()))'],{maxBuffer:8e6}));
const q={id:'M14_02',module:'14',order:1,type:'medicineList',choiceCodes:[],translations:{}};
for(const lang of ['lv','en','ru'])q.translations[lang]={title:'Medicine information',time:'Current and past'};
const answers={'M14_02':{kind:'medicine',status:'answered',discussion:'Ask about timing',records:[{
 name:'Example medicine',status:'past',strength:'20 mg',dose:'one tablet',schedule:'once daily',duration:'3 months',doseDuration:'2 months',
 reason:'Sleep',benefit:'B',effects:'<script>synthetic</script>',changes:'Worse after stopping',stoppedWhen:'May',stopReason:'No longer needed'
}]}};
const context={window:{}};vm.runInNewContext(fs.readFileSync('src/app/reports/reports.js','utf8'),context);
const r=context.window.QuestionnaireReports;
for(const lang of ['lv','en','ru']){
 const entries=r.entries([q],answers,lang,data.presentation,data.ui[lang].medicine);
 assert.equal(entries.length,1);
 assert(entries[0].plain.includes(data.ui[lang].medicine.fields.name));
 assert(entries[0].plain.includes(data.ui[lang].medicine.status.past));
 assert(entries[0].plain.includes(data.ui[lang].medicine.benefits.B));
 assert(entries[0].plain.includes('Ask about timing'));
 assert(entries[0].html.includes('&lt;script&gt;synthetic&lt;/script&gt;'));
 assert(!entries[0].html.includes('<script>'));
 const skip=r.entries([q],{'M14_02':{kind:'skip'}},lang,data.presentation,data.ui[lang].medicine);
 assert.equal(skip.length,0);
}
console.log('PASS: medicine-list report labels, values, time context and escaping in LV/EN/RU.');
