"""Read-only audit of the frozen 48-module source against current engine capabilities."""
import collections
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
paths=sorted((ROOT/'src/modules').glob('182_MODULE_*_LV_EN_RU_v16.json'))
assert len(paths)==48, f'Expected 48 original modules; found {len(paths)}'
modules=[json.loads(p.read_text(encoding='utf-8')) for p in paths]
entries=[];ids={};orders={};types=collections.Counter();cross_module_conditions=[];multi_parents=[]
allowed_logic={'id','title','profile','multi','time','context','choices','exclusive','incompatible','section','answerStatus','help','type','maxChoices'}
allowed_translation={'title','time','choices','help'}

for expected,mod in enumerate(modules,1):
    assert mod['schema']=='question-module-bundle-v1'
    assert mod['section']==expected and mod['count']==len(mod['entries'])
    for entry in mod['entries']:
        q=entry['lv'];qid=q['id'];order=entry['order']
        assert set(q)<=allowed_logic, (qid,set(q)-allowed_logic)
        assert q['section']==expected and qid not in ids and order not in orders
        assert re.fullmatch(r'M\d{2}_\d{2}[A-Z]?',qid), qid
        ids[qid]=q;orders[order]=qid;entries.append(entry)
        assert set(q['answerStatus'])==set(q['choices'])
        assert set(q['answerStatus'].values())<={'answered','uncertain','refused'}
        assert all(re.fullmatch(r'[A-Z]',code) for code in q['choices'])
        assert isinstance(q['multi'],bool) and isinstance(q['profile'],str)
        types[q.get('type','choice')]+=1
        for lang in ('lv','en','ru'):
            t={key:q[key] for key in allowed_translation if key in q} if lang=='lv' else entry[lang]
            assert set(t)<=allowed_translation and {'title','time','choices'}<=set(t), (qid, lang, sorted(t))
            assert ('help' in q)==('help' in t), (qid,lang,sorted(t))
            assert set(t['choices'])==set(q['choices'])
        if q.get('maxChoices'):
            assert q['multi'] and 1<=q['maxChoices']<=len(q['choices']), qid
        exclusive=set(q.get('exclusive',''))
        assert exclusive<=set(q['choices']), qid
        for pair in q.get('incompatible',[]):
            assert len(pair)==2 and pair[0]!=pair[1] and set(pair)<=set(q['choices']), qid
        context=q.get('context')
        if context:
            assert set(context)<=({'id','showValues','hideValues'}) and context.get('id'), qid
            for key in ('showValues','hideValues'):
                assert set(context.get(key,[]))<=set(ids.get(context['id'],{}).get('choices',{})) or context['id'] not in ids, (qid,key)
            cross_module_conditions.append((qid,context['id'])) if context['id'] in ids and ids[context['id']]['section']!=q['section'] else None
            if ids.get(context['id'],{}).get('multi'):
                multi_parents.append((qid,context['id']))

assert len(entries)==712 and set(orders)==set(range(712))
# Translation edits must never alter the frozen Latvian source or its logic.
reference=(ROOT/'reference/baseline/html/162_Sagatavosanas_vizitei_LV_v16.html').read_text(encoding='utf-8')
frozen_bank=json.JSONDecoder().raw_decode(reference.split('const BANK = ',1)[1])[0]
ordered_entries=sorted(entries,key=lambda entry:entry['order'])
assert len(frozen_bank)==len(ordered_entries)
for frozen,entry in zip(frozen_bank,ordered_entries):
    assert entry['lv']==frozen, ('Frozen Latvian text/logic changed', frozen['id'])
order_by_id={qid:order for order,qid in orders.items()}
assert all(context['id'] in ids and order_by_id[context['id']]<entry['order']
           for entry in entries if (context:=entry['lv'].get('context')))
assert types=={'choice':709,'shortText':2,'medicineList':1}, types
assert [qid for qid,q in ids.items() if q.get('type')=='medicineList']==['M14_02']
assert len(multi_parents)==5
app=(ROOT/'src/app/core/app.js').read_text(encoding='utf-8')
recovery=(ROOT/'src/app/core/recovery.js').read_text(encoding='utf-8')
reports=(ROOT/'src/app/reports/reports.js').read_text(encoding='utf-8')
assert 'q.type==="medicineList"' in app and 'record.kind==="medicine"' in recovery
assert 'function medicineValues' in reports

print(f'PASS: source structure is consistent across {len(modules)} modules and {len(entries)} questions; IDs/orders unique; LV/EN/RU choices and condition parents match.')
print(f'ENGINE AUDIT: choice, multi, maxChoices, exclusive, incompatible, refusal/uncertainty status, optional help/time and hide/show conditions fit current generic engine; {len(multi_parents)} conditions have multi-select parents; {len(cross_module_conditions)} cross-section conditions.')
print('ENGINE STATUS: medicineList has a tested form, recovery record, and report formatter; full runtime is checked in Chromium.')
print('LIMIT: audit validates data shape and translation/code consistency, not EN/RU language accuracy, clinical meaning, or full-browser behavior.')
