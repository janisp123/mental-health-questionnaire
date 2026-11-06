import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tools'))
from build_pilot import build_bundle
b=build_bundle();qs=[q for g in b['groups'] for q in g['questions']]
assert sorted(q['id'] for q in qs)==json.loads((ROOT/'tests/pilot/original_ids.json').read_text())
assert all(not g['required'] for g in b['groups'])
assert b['groups'][0]['id']=='23'
assert b['groups'][-1]['id']=='33'
assert all(q['originModule']==int(g['id']) for g in b['groups'] for q in g['questions'])
assert b['layout_version']=='optional-topics-v1'
assert set(b['legacy_opening_groups'])=={'06','18','23','31','33'}
layout=json.loads((ROOT/'src/questionnaire/layout.json').read_text())
presentation=json.loads((ROOT/'src/questionnaire/presentation.json').read_text())
expected={f'{i:02d}' for i in range(1,49)}
assert layout['order']==['23','02','21','06','18','31','33']
assert len(layout['full_order'])==48 and set(layout['full_order'])==expected
assert len(presentation['topicOrder'])==48 and set(presentation['topicOrder'])==expected
assert layout['full_order'][0]=='23' and layout['full_order'][-1]=='33'
assert presentation['topicOrder'][0]=='33' and presentation['topicOrder'][-1]=='48'
report_position={key:i for i,key in enumerate(presentation['topicOrder'])}
assert all(report_position[key]>report_position['16'] for key in ('06','10','18','19','21'))
print('PASS: all original IDs preserved exactly once; optional thematic layout; personal details last; legacy opening mapping.')
