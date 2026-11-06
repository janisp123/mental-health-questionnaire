"""Registry independence, isolated locale edit and conditional-answer recovery/export."""
import shutil,tempfile
from playwright.sync_api import sync_playwright
from browser_helpers import *

def write(path,value):path.write_text(json.dumps(value,ensure_ascii=False))
def snapshot(path):return {p.relative_to(path):p.read_bytes() for p in path.rglob('*') if p.is_file()}

with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
    temp=Path(tmp);source=temp/'pilot';shutil.copytree(build.SOURCE,source);build.SOURCE=source
    before=snapshot(source);modules=source/'modules';registry=build.read_json(modules/'registry.json')
    module=modules/'fixture';module.mkdir()
    q={'id':'TEST21','order':10000,'choiceCodes':['A','B'],'multi':False}
    follow={**q,'id':'TEST21_F','order':10001,'context':{'id':'TEST21','showValues':['A']}}
    write(module/'logic.json',{'group':'fixture','questions':[q,follow]})
    registry['groups'].append({'id':'fixture','required':False,'question_count':2});write(modules/'registry.json',registry)
    for lang in build.LANGS:
        write(module/(lang+'.json'),{'module':'fixture','lang':lang,'title':'Test fixture '+lang,'questions':{'TEST21':{'title':'Original '+lang,'choices':{'A':'First','B':'Second'}},'TEST21_F':{'title':'Conditional '+lang,'choices':{'A':'Follow first','B':'Follow second'}}}})
    assert all((source/p).read_bytes()==v for p,v in before.items() if p!=Path('modules/registry.json'))
    old=temp/'before.html';old.write_text(build.make_html());baseline=snapshot(source)
    en=build.read_json(module/'en.json');en['questions']['TEST21']['title']='Edited English question';write(module/'en.json',en)
    assert {p for p,v in baseline.items() if (source/p).read_bytes()!=v}=={Path('modules/fixture/en.json')}
    new=temp/'after.html';new.write_text(build.make_html())
    browser=launch(pw);page,errors,network=open_page(browser,old)
    act(page,'choose');page.locator('#optionalfixture').check();act(page,'confirm')
    assert qid(page)=='TEST21';choose(page,'A');assert qid(page)=='TEST21_F'
    choose(page,'B');act(page,'back');assert qid(page)=='TEST21_F'
    act(page,'previous');choose(page,'B');assert not page.locator('.question').count()
    prior=backup(page);assert prior['answers']['TEST21_F']['codes']==['B']
    act(page,'ai');assert 'Conditional' not in page.locator('#reportText').input_value()
    page.goto(new.as_uri());restore(page,prior)
    assert page.locator('.question h2').inner_text()=='Edited English question'
    assert page.locator('input[value=B]').is_checked()
    for lang in ['lv','ru','en']:
        page.select_option('#language',lang)
        assert page.locator('.question h2').inner_text()==('Edited English question' if lang=='en' else 'Original '+lang)
    assert backup(page)['answers']==prior['answers']
    restore(page,{**prior,'selected':['99']});assert page.get_by_text('Cannot load this file. Check its format and version.').is_visible()
    assert backup(page)['answers']==prior['answers']
    # A previously hidden answer reappears unchanged when its condition becomes true.
    choose(page,'A');assert qid(page)=='TEST21_F';assert page.locator('input[value=B]').is_checked()
    act(page,'results');act(page,'ai');assert 'Conditional en: Follow second' in page.locator('#reportText').input_value()
    # Deselecting a topic does not silently erase recorded, applicable responses from reports.
    act(page,'sections');page.locator('#optionalfixture').uncheck();act(page,'confirm');act(page,'ai')
    assert 'Edited English question: First' in page.locator('#reportText').input_value()
    assert not errors,errors;assert not network,network;browser.close()
print('PASS: independent module/locale, conditional navigation, hidden-answer recovery, invalid restore rejection, standalone export.')
