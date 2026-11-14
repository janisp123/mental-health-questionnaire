"""Peak clarification is shown in every active locale without changing the question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tools'))
import build_questionnaire as build
bundle=build.build_bundle();q=next(q for g in bundle['groups'] for q in g['questions'] if q['id']=='M04_01')
old=next(q for g in build.build_source_groups() for q in g['questions'] if q['id']=='M04_01')
for lang in bundle['ui']:
 assert q['translations'][lang].get('help'),lang
 if lang in build.SOURCE_LANGS:
  assert {k:v for k,v in q['translations'][lang].items() if k!='help'}=={k:v for k,v in old['translations'][lang].items() if k!='help'}
for key in ('id','order','multi','context','choiceCodes','exclusive','incompatible','answerStatus'):
 assert q[key]==old[key],key
print('PASS: four-language panic-peak explanation; original question, choices and branching retained.')
