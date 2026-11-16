"""Independent action-history coverage, strict routing and isolated rollback."""
import copy,sys
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'tools'))
import build_questionnaire as build
b=build.build_bundle();qs=[q for g in b['groups'] for q in g['questions']];by={q['id']:q for q in qs}
assert {'M06_26','M06_27'}<=set(by),'Missing independent action history and timing'
a,t=by['M06_26'],by['M06_27'];assert len(qs)==718 and len({q['order'] for q in qs})==718
assert qs.index(a)==qs.index(by['M06_09'])+1 and qs.index(t)==qs.index(a)+1
assert a['context'] is None and t['context']=={'id':'M06_26','showValues':list('ABCD')}
for q,codes in ((a,'ABCDEFG'),(t,'ABCDEFGH')):
 assert q['sourceModule']=='06' and q['module']==by['M06_09']['module'] and q['type']=='choice' and not q['multi']
 assert q['choiceCodes']==list(codes) and set(q['translations'])==set(b['ui'])
 for lang,wording in q['translations'].items():assert wording['title'] and wording['time'] and list(wording['choices'])==list(codes)
assert a['answerStatus']==dict(A='answered',B='answered',C='answered',D='answered',E='answered',F='uncertain',G='refused')
for lang in b['ui']:assert t['translations'][lang]['choices']==by['M06_09']['translations'][lang]['choices']
p=b['presentation']['reportPriority'];assert p['questions']['M06_26']=={'default':3,'answers':dict(A=3,B=3,C=3,D=3,E=1,F=3,G=3)}
assert p['questions']['M06_27']=={'default':3,'answers':dict(A=4,B=4,C=3,D=3,E=3,F=1,G=3,H=3)}
assert not any(x in p['relatedGroups']['suicide_history'] for x in ('M06_26','M06_27'))
assert not any(x in b['presentation']['questions'] for x in ('M06_26','M06_27'))
with patch.object(build,'apply_m06_action_history',lambda bundle,priority:None):old=build.build_bundle()
expected=copy.deepcopy(b)
for g in expected['groups']:
 g['questions']=[q for q in g['questions'] if q['id'] not in ('M06_26','M06_27')];g['questionCount']=len(g['questions'])
for qid in ('M06_26','M06_27'):del expected['presentation']['reportPriority']['questions'][qid]
assert expected==old,'Unrelated source/report data changed'
read=build.read_json
for kind in ('duplicate','locale','condition','priority','timing_wording'):
 def mutate(path):
  data=read(path)
  if path.name=='m06-action-history.json':
   if kind=='duplicate':data['questions'][1]['order']=716
   elif kind=='locale':data['questions'][0]['translations'].pop('uk')
   elif kind=='condition':data['questions'][1]['context']['showValues'].append('E')
   elif kind=='priority':data['reportPriorities']['M06_26']['answers']['A']=5
   elif kind=='timing_wording':data['questions'][1]['translations']['en']['choices']['A']='Changed meaning'
  return data
 with patch.object(build,'read_json',side_effect=mutate):
  try:build.build_bundle()
  except ValueError:pass
  else:raise AssertionError('Accepted malformed history data: '+kind)
print('PASS: independent history/timing, locales, exact recency meanings, conservative priority, invalid data rejection and isolated rollback.')
