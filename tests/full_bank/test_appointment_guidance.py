"""Appointment hints must be complete, narrow, and never become clinician answers."""
import copy,json,subprocess,sys
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tools'))
import build_questionnaire as build
bundle=build.build_bundle();by_id={q['id']:q for g in bundle['groups'] for q in g['questions']}
for qid in ('M14_02','M02_09'):
 for locale in bundle['ui']:
  assert by_id[qid]['translations'][locale].get('help','').strip(),f'Missing appointment guidance: {qid}/{locale}'
safety=next(g for g in bundle['groups'] if g['id']=='S04')
for locale in bundle['ui']:
 assert safety['titles'][locale] in by_id['M02_09']['translations'][locale]['help'],locale
# Real source records retain their existing title/time/choices; only help is added.
source={q['id']:q for g in build.build_source_groups() for q in g['questions']}
for qid in ('M14_02','M02_09'):
 for locale in build.SOURCE_LANGS:
  actual=dict(by_id[qid]['translations'][locale]);actual.pop('help')
  assert actual==source[qid]['translations'][locale],(qid,locale)
# Reject a malformed or incomplete help catalog before a distribution can be built.
catalog=build.read_json(build.QUESTIONNAIRE/'appointment-guidance.json')
read=build.read_json
bad_cases=[]
for mutate in (
 lambda x:x.update(schema='wrong'),
 lambda x:x['questions']['M02_09'].pop('uk'),
 lambda x:x['questions']['M02_09'].update(en=' '),
 lambda x:x['questions']['M02_09'].update(xx='unconfigured locale'),
 lambda x:x['questions'].update(M02_01=x['questions']['M02_09']),
 lambda x:x['questions'].update(M02_09=[]),
):
 bad=copy.deepcopy(catalog);mutate(bad);bad_cases.append(bad)
for bad in bad_cases:
 def altered(path):
  return bad if path.name=='appointment-guidance.json' else read(path)
 with patch.object(build,'read_json',side_effect=altered):
  try:build.apply_appointment_guidance(copy.deepcopy(bundle))
  except ValueError:pass
  else:raise AssertionError('Malformed guidance accepted')
# Exercise actual report renderer: helper wording never enters provided answers.
js='''const fs=require('fs'),vm=require('vm'),d=JSON.parse(fs.readFileSync(0,'utf8')),c={window:{}};vm.runInNewContext(fs.readFileSync('src/app/reports/reports.js','utf8'),c);const qs=d.groups.flatMap(g=>g.questions);for(const l of Object.keys(d.ui)){const q=qs.find(q=>q.id==='M02_09');for(const code of q.choiceCodes){const answer={[q.id]:{kind:'choice',codes:[code]}};const text=c.window.QuestionnaireReports.doctorText([q],answer,l,d.ui[l],d.presentation);if(!text.includes(q.translations[l].choices[code])||text.includes(q.translations[l].help))throw Error('Help altered report response');}}'''
subprocess.run(['node','-e',js],input=json.dumps(bundle),text=True,cwd=ROOT,check=True)
print('PASS: complete appointment guidance, rejected malformed catalogs, frozen wording and unchanged report responses.')
