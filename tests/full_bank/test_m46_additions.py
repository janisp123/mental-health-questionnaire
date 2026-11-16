"""Additive M46 questions retain frozen records and allow mild/rare experiences."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'tools'))
import build_questionnaire as build
bundle=build.build_bundle()
questions=[q for g in bundle['groups'] for q in g['questions']]
by_id={q['id']:q for q in questions}
assert {'M46_07','M46_08','M46_09'}<=set(by_id),'Missing focused M46 coverage'
assert len(questions)==715 and len({q['order'] for q in questions})==715
for qid in ('M46_07','M46_08','M46_09'):
 q=by_id[qid]
 assert q['context'] is None and not q['multi'] and q['type']=='choice'
 assert q['sourceModule']=='46' and q['module']==by_id['M46_01']['module']
 assert set(q['translations'])==set(bundle['ui'])
 for locale,t in q['translations'].items():
  assert t['title'] and t['time'] and set(t['choices'])==set(q['choiceCodes'])
 assert q['answerStatus'][q['choiceCodes'][-1]]=='refused'
 assert q['answerStatus'][q['choiceCodes'][-2]]=='uncertain'
assert 'rare' in by_id['M46_09']['translations']['en']['choices']['B'].lower()
assert questions.index(by_id['M46_03'])<questions.index(by_id['M46_07'])<questions.index(by_id['M46_04'])
# Every original frozen ID, order and context retains its contract.
for group in build.build_source_groups():
 for source in group['questions']:
  q=by_id[source['id']]
  for field in ('order','choiceCodes','context','answerStatus','multi','type'):
   assert q[field]==source[field],(q['id'],field)
# New report positions are neutral editorial metadata, never clinical scores.
for qid in ('M46_07','M46_08','M46_09'):
 assert set(bundle['presentation']['reportPriority']['questions'][qid]['answers'].values())=={3}
print('PASS: three independent localized M46 questions; rare experiences answerable; all 712 frozen contracts preserved.')
