"""Full source data forms complete optional groups without question copies."""
import importlib.util,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('questionnaire_build',ROOT/'tools'/'build_questionnaire.py')
build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)
groups=build.build_source_groups()
assert [group['id'] for group in groups]==[f'{i:02d}' for i in range(1,49)]
assert all(not group['required'] for group in groups)
questions=[q for group in groups for q in group['questions']]
assert len(questions)==712 and len({q['id'] for q in questions})==712
assert len({q['order'] for q in questions})==712
titles=build.load_module_titles()
assert all(group['titles']=={lang:titles[lang][group['id']] for lang in ('lv','en','ru')} for group in groups)
by_id={q['id']:q for q in questions}
assert all(not q['context'] or by_id[q['context']['id']]['order']<q['order'] for q in questions)

# Preserve the source's documented unusual placement; do not infer module from ID prefix.
odd=by_id['M32_02']
assert odd['originModule']==33 and odd['module']=='33'
assert odd in next(group for group in groups if group['id']=='33')['questions']
bundle=build.build_bundle()
assert len(bundle['groups'])==15 and all(36<=g['questionCount']<=70 for g in bundle['groups'])
assert sum(len(g['questions']) for g in bundle['groups'])==712
assert next(q for g in bundle['groups'] for q in g['questions'] if q['id']=='M32_02')['module']=='S11'
print('PASS: 48 immutable source modules map to 15 optional groups/712 questions; exact source titles and earlier conditions remain available.')
