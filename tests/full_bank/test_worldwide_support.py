"""Country-neutral displayed guidance must preserve all clinical answer contracts."""
import copy,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tools'))
import build_questionnaire as build
bundle=build.build_bundle();countries=re.compile(r'\b112\b|\b116\s?123\b')
for lang,ui in bundle['ui'].items():
 for key in ('supportBody','help','emergencyBody','supportLink'):
  assert not countries.search(ui[key]),(lang,key)
 assert ui['supportBody'] and ui['emergencyBody']
source={q['id']:q for g in build.build_source_groups() for q in g['questions']}
changed=[]
for group in bundle['groups']:
 for q in group['questions']:
  for lang,t in q['translations'].items():
   assert not countries.search(json.dumps(t,ensure_ascii=False)),(q['id'],lang)
   if lang in build.SOURCE_LANGS and q['id'] in source:
    old=source[q['id']]['translations'][lang]
    if old['time']!=t['time']:changed.append((q['id'],lang))
    ignored={'time','help'} if q['id'] in {'M04_01','M14_02','M02_09'} else {'time'}
    assert {k:v for k,v in t.items() if k not in ignored}=={k:v for k,v in old.items() if k not in ignored}
  if q['id'] not in source:continue
  for key in ('id','order','profile','multi','context','choiceCodes','exclusive','incompatible','answerStatus','type'):
   assert q[key]==source[q['id']][key],(q['id'],key)
assert {qid for qid,lang in changed}=={'M15_19','M18_13','M30_17'}
assert len(changed)==9
print('PASS: country-neutral guidance; only three displayed safety notices differ; IDs, choices and conditions preserved.')
