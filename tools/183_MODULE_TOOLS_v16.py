#!/usr/bin/env python3
"""Validate or rebuild questionnaire HTML BANK data from per-section LV/EN/RU snapshots.

No third-party dependencies. Does not modify published files. Requires original standalone
HTML templates as inputs. All labels/report/UI JavaScript remain in those templates.
"""
import argparse, copy, hashlib, json
from pathlib import Path

LANG_FILES = {'lv':'162_Sagatavosanas_vizitei_LV_v16.html',
              'en':'172_Questionnaire_EN_v16_DRAFT_NOT_RELEASED.html',
              'ru':'172_Questionnaire_RU_v16_DRAFT_NOT_RELEASED.html'}
LOC = ('title','time','help','choices')


def parse_bank(html):
    token='const BANK = '
    if html.count(token)!=1: raise ValueError('Expected exactly one BANK definition')
    start=html.index(token)+len(token)
    value, consumed=json.JSONDecoder().raw_decode(html[start:])
    if not isinstance(value,list): raise ValueError('Question BANK is not an array')
    return value,start,start+consumed


def load_modules(folder):
    modules=sorted(folder.glob('182_MODULE_??_LV_EN_RU_v16.json'))
    if len(modules)!=48: raise ValueError(f'Expected 48 module files, found {len(modules)}')
    observed=set(); result=[]
    for section,path in enumerate(modules,1):
        b=json.loads(path.read_text(encoding='utf-8'))
        if b['section']!=section or b['count']!=len(b['entries']):
            raise ValueError(f'Section/count mismatch: {path.name}')
        for item in b['entries']:
            q=item['lv']; question_id=q['id']; order=item['order']
            if q['section']!=section or question_id in observed or not isinstance(order,int):
                raise ValueError(f'Invalid ID/section/order in {path.name}: {question_id}')
            observed.add(question_id)
            for lang in ('en','ru'):
                if set(item[lang])!=set(k for k in LOC if k in q):
                    raise ValueError(f'Incomplete localized fields {question_id}: {lang}')
                if set(item[lang]['choices'])!=set(q['choices']):
                    raise ValueError(f'Choice code mismatch {question_id}: {lang}')
            result.append(item)
    if len(result)!=712 or sorted(x['order'] for x in result)!=list(range(712)):
        raise ValueError('Question count/order corrupted')
    return sorted(result,key=lambda x:x['order'])


def data_for(lang,entries):
    b=[]
    for item in entries:
        q=copy.deepcopy(item['lv'])
        if lang!='lv':
            for key,val in item[lang].items():q[key]=copy.deepcopy(val)
        b.append(q)
    return b


def run():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--modules',type=Path,required=True,help='Folder containing 48 module JSON files')
    p.add_argument('--templates',type=Path,required=True,help='Directory containing original LV/EN/RU HTML files')
    p.add_argument('--output',type=Path,help='When provided, emit rebuilt HTML to a separate folder, never overwrite templates')
    a=p.parse_args()
    entries=load_modules(a.modules)
    results={}
    for lang,filename in LANG_FILES.items():
        template=(a.templates/filename)
        html=template.read_text(encoding='utf-8')
        old,start,end=parse_bank(html)
        new=data_for(lang,entries)
        if len(old)!=len(new) or [r['id'] for r in old]!=[r['id'] for r in new]:
            raise ValueError(f'Question ID/order incompatibility: {lang}')
        match=(new==old)
        if a.output is None and not match:raise ValueError(f'Modules differ from current HTML bank for {lang}; use --output to create drafts')
        if a.output is not None:
            if a.output.resolve()==a.templates.resolve(): raise ValueError('Output cannot equal templates directory')
            a.output.mkdir(parents=True,exist_ok=True)
            new_json=json.dumps(new,ensure_ascii=False,separators=(',',':'))
            rebuilt=html[:start]+new_json+html[end:]
            dest=a.output/(template.stem+'_REBUILT_REVIEW_REQUIRED.html')
            dest.write_text(rebuilt,encoding='utf-8')
        results[lang]={'question_count':len(new),'identical_question_data_to_template':match,'template_sha256':hashlib.sha256(template.read_bytes()).hexdigest()}
    print(json.dumps({'all_verified':all(x['identical_question_data_to_template'] for x in results.values()),'languages':results},indent=2))

if __name__=='__main__':run()
