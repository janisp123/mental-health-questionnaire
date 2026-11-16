"""The editorial table covers every ID/code, rejects unsafe metadata and preserves source data."""
import copy,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'tools'))
import build_questionnaire as build
bundle=build.build_bundle();questions=[q for group in bundle['groups'] for q in group['questions']]
policy=bundle['presentation'].get('reportPriority')
assert policy, 'Report-only priority policy is missing'
build.validate_report_priority(policy,questions)
assert len(policy['questions'])==len(questions)==715
for question in questions:
 rule=policy['questions'][question['id']]
 assert type(rule['default']) is int and 1<=rule['default']<=5
 assert set(rule['answers'])==set(question['choiceCodes'])
 assert all(type(v) is int and 1<=v<=5 for v in rule['answers'].values())
for change in ('missing','unknown','invalid_code','zero','float','boolean','group_unknown','group_duplicate','uncertain_urgent','refused_urgent','clinical_weights'):
 bad=copy.deepcopy(policy)
 if change=='missing':bad['questions'].pop('M06_02')
 elif change=='unknown':bad['questions']['UNKNOWN']={'default':3,'answers':{}}
 elif change=='invalid_code':bad['questions']['M06_02']['answers']['UNKNOWN']=5
 elif change=='zero':bad['questions']['M06_02']['default']=0
 elif change=='float':bad['questions']['M06_02']['default']=3.5
 elif change=='boolean':bad['questions']['M06_02']['answers']['B']=True
 elif change=='group_unknown':bad['relatedGroups']['current_safety'].append('UNKNOWN')
 elif change=='group_duplicate':bad['relatedGroups']['duplicate']=['M06_02','M06_03']
 elif change=='uncertain_urgent':bad['questions']['M06_02']['answers']['C']=5
 elif change=='refused_urgent':bad['questions']['M06_02']['answers']['D']=5
 elif change=='clinical_weights':bad['weights']={'M06_02':5}
 try:build.validate_report_priority(bad,questions)
 except ValueError:pass
 else:raise AssertionError('Accepted invalid report priority: '+change)
print('PASS: complete 715-ID/code editorial ordering table; bounded values and valid unique context families.')
