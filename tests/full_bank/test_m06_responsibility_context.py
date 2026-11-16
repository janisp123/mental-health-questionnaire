"""Independent M06 hypothetical context, safe editorial meaning and isolated rollback."""
import copy,sys
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'tools'))
import build_questionnaire as build
bundle=build.build_bundle();questions=[q for g in bundle['groups'] for q in g['questions']];by_id={q['id']:q for q in questions}
assert 'M06_25' in by_id,'Missing responsibilities context in existing M06'
q=by_id['M06_25'];assert q['sourceModule']=='06' and q['module']==by_id['M06_24']['module']
assert q['context'] is None and q['type']=='choice' and q['multi'] is False
assert q['choiceCodes']==list('ABCDEF') and set(q['translations'])==set(bundle['ui'])
assert len(questions)==718 and len({x['order'] for x in questions})==718
assert questions.index(q)==questions.index(by_id['M06_24'])+1
for locale,t in q['translations'].items():
 assert t['title'] and t['time'] and t['help'] and list(t['choices'])==q['choiceCodes']
assert q['answerStatus']==dict(A='answered',B='answered',C='answered',D='answered',E='uncertain',F='refused')
priority=bundle['presentation']['reportPriority'];assert priority['questions']['M06_25']=={'default':3,'answers':dict(A=4,B=3,C=3,D=3,E=3,F=3)}
assert 'M06_25' in priority['relatedGroups']['current_safety']
assert 'M06_25' not in bundle['presentation']['questions'],'Do not infer emergency from hypothetical response'
# Removing only this build hook reconstructs the exact earlier application bundle.
with patch.object(build,'apply_m06_responsibility_context',lambda bundle,priority:None):old=build.build_bundle()
expected=copy.deepcopy(bundle)
for g in expected['groups']:
 g['questions']=[x for x in g['questions'] if x['id']!='M06_25'];g['questionCount']=len(g['questions'])
del expected['presentation']['reportPriority']['questions']['M06_25']
expected['presentation']['reportPriority']['relatedGroups']['current_safety'].remove('M06_25')
assert expected==old,'Unrelated question/priority/state data changed'
read=build.read_json
for mode in ('duplicate_order','missing_locale','bad_code','reassuring_priority','uncertain_priority','wrong_module'):
 def mutate(path):
  data=read(path)
  if path.name=='m06-responsibility-context.json':
   if mode=='duplicate_order':data['question']['order']=714
   elif mode=='missing_locale':data['question']['translations'].pop('uk')
   elif mode=='bad_code':data['question']['choiceCodes'].append('Z')
   elif mode=='reassuring_priority':data['reportPriority']['answers']['B']=1
   elif mode=='uncertain_priority':data['reportPriority']['answers']['E']=5
   elif mode=='wrong_module':data['question']['sourceModule']='07'
  return data
 with patch.object(build,'read_json',side_effect=mutate):
  try:build.build_bundle()
  except ValueError:pass
  else:raise AssertionError('Accepted invalid M06 context: '+mode)
print('PASS: localized M06_25, conservative editorial priorities, malformed-source rejection and isolated additive rollback.')
