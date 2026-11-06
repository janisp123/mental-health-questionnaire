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
print('PASS: all original IDs preserved exactly once; optional thematic layout; personal details last; legacy opening mapping.')
