"""Offline medicine-list lifecycle using synthetic data only."""
import json,re,tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_helpers import *

ROOT=Path(__file__).resolve().parents[2]
def medicine_html():
    data=build.build_bundle()
    source=json.loads((ROOT/'src/modules/182_MODULE_14_LV_EN_RU_v16.json').read_text())
    entry=next(item for item in source['entries'] if item['lv']['id']=='M14_02')
    q={'id':'M14_02','module':'02','originModule':14,'order':1000,'type':'medicineList','multi':False,
       'choiceCodes':[],'translations':{lang:{'title':entry[lang]['title'],'time':entry[lang]['time'],'choices':{}}
                                         for lang in ('lv','en','ru')}}
    next(group for group in data['groups'] if group['id']=='02')['questions'].insert(0,q)
    html=build.make_html()
    blob=re.search(r'(<script id="pilot-data" type="application/json">)(.*?)(</script>)',html,re.S)
    assert blob
    encoded=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('>','\\u003e')
    return html[:blob.start(2)]+encoded+html[blob.end(2):]

with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
    path=Path(tmp)/'medicine.html';path.write_text(medicine_html())
    browser=launch(pw);page,errors,network=open_page(browser,path)
    empty={q['id']:{'kind':'skip','status':'skipped','savedAt':''}
           for g in build.build_bundle()['groups'] if g['required'] for q in g['questions']}
    restore(page,seed(['02'],empty,'M14_02'))
    assert qid(page)=='M14_02'
    assert page.locator('[data-med-field="name"]').count()==1
    page.locator('[data-med-field="name"]').fill('Synthetic medicine')
    page.locator('[data-med-field="strength"]').fill('20 mg')
    page.locator('[data-med-field="benefit"]').select_option('B')
    act(page,'addMedicine')
    assert page.locator('[data-med-index="1"][data-med-field="name"]').count()==1
    page.locator('[data-med-index="1"][data-med-field="name"]').fill('Second synthetic medicine')
    page.locator('[data-med-remove="0"]').click()
    assert page.locator('[data-med-field="name"]').input_value()=='Second synthetic medicine'
    page.locator('#medicineDiscussion').fill('Synthetic question')
    act(page,'save')
    assert qid(page)=='M02_01'
    saved=backup(page)
    rec=saved['answers']['M14_02'];assert rec['kind']=='medicine'
    assert len(rec['records'])==1 and rec['records'][0]['name']=='Second synthetic medicine'
    assert rec['discussion']=='Synthetic question'

    # Return, restore, and save again without losing medication details.
    page.goto(path.as_uri());restore(page,saved)
    assert qid(page)=='M02_01'
    page.goto(path.as_uri());restore(page,{**saved,'currentId':'M14_02'})
    assert page.locator('[data-med-field="name"]').input_value()=='Second synthetic medicine'
    assert page.locator('#medicineDiscussion').input_value()=='Synthetic question'
    act(page,'skip')
    skipped=backup(page);assert skipped['answers']['M14_02']['kind']=='skip'

    # Invalid medicine recovery is rejected without replacing current session.
    invalid={**saved,'currentId':'M14_02','answers':{**saved['answers'],'M14_02':{
        'kind':'medicine','status':'answered','discussion':'','records':[{'name':'bad','status':'invalid'}]}}}
    page.goto(path.as_uri());restore(page,invalid)
    assert page.get_by_text(build.build_bundle()['ui']['lv']['restoreError']).is_visible()
    assert not errors,errors;assert not network,network
    browser.close()
print('PASS: medicine form add/edit/remove/save/skip and recovery; native Android UNVERIFIED.')
