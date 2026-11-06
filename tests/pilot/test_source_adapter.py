"""Read-only adapter must preserve original question records exactly."""
import importlib.util,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('pilot_build',ROOT/'tools'/'build_pilot.py')
build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)
source_files=[ROOT/'src/modules'/f'182_MODULE_{n:02d}_LV_EN_RU_v16.json' for n in range(1,17)]
seen_ids=set();seen_orders=set();adapted={};count=0
for path in source_files:
    module=json.loads(path.read_text(encoding='utf-8'))
    for original in module['entries']:
        q=build.adapt_source_entry(original)
        lv=original['lv'];qid=lv['id']
        assert q['id']==qid and q['order']==original['order']
        assert q['originModule']==lv['section'] and q['section']==lv['section'] and q['profile']==lv['profile']
        assert q['multi']==lv['multi'] and q['context']==lv['context']
        assert q['choiceCodes']==list(lv['choices'])
        assert q['exclusive']==lv['exclusive'] and q['incompatible']==lv['incompatible']
        assert q['answerStatus']==lv['answerStatus']
        assert q['type']==lv.get('type','choice')
        if 'maxChoices' in lv:assert q['maxChoices']==lv['maxChoices']
        for lang in ('lv','en','ru'):
            expected=lv if lang=='lv' else original[lang]
            translated=q['translations'][lang]
            assert translated['title']==expected['title'] and translated['time']==expected['time']
            assert translated['choices']==expected['choices']
            assert translated.get('help')==expected.get('help')
        assert qid not in seen_ids and q['order'] not in seen_orders
        seen_ids.add(qid);seen_orders.add(q['order']);adapted[qid]=q;count+=1
assert count==293
assert all(q['context'] is None or q['context']['id'] in adapted for q in adapted.values())
assert all(q['context'] is None or adapted[q['context']['id']]['order']<q['order'] for q in adapted.values())
assert sum(len(g['questions']) for g in build.build_bundle()['groups'])==60
print(f'PASS: read-only adapter preserves all {count} questions in modules 01–16; pilot remains 60 questions.')
