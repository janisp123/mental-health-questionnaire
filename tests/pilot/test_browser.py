"""Offline UX/recovery/report regression. Desktop Chromium, NOT native Android."""
import json,tempfile
from playwright.sync_api import sync_playwright
from browser_helpers import *

with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
    folder=Path(tmp);html=folder/'pilot.html';html.write_text(build.make_html())
    browser=launch(pw);page,errors,network=open_page(browser,html)
    dialogs=[];page.on('dialog',lambda d:dialogs.append(d.message))
    act(page,'start');assert qid(page)=='M23_11'
    assert page.locator('[data-act=save]:visible').count()==1 # multiple choice
    page.locator('input[value=A]').check();page.locator('input[value=B]').check()
    assert qid(page)=='M23_11';assert backup(page)['answers']=={}
    act(page,'save');assert qid(page)=='M02_01'
    assert not page.locator('[data-act=save]:visible').count()
    # A physical double click must save just one question even after synchronous rendering.
    page.locator('input[value=B]').locator('..').dblclick(delay=40)
    assert qid(page)=='M02_02'
    payload=backup(page);assert payload['answers']['M02_01']['codes']==['B'];assert 'M02_02' not in payload['answers']
    act(page,'previous');assert qid(page)=='M02_01'
    choose(page,'D');assert qid(page)=='M02_02'
    assert backup(page)['answers']['M02_01']['codes']==['D']
    # Fixed centered Skip: same viewport coordinates, no confirmation, variable question lengths.
    for width in [320,390,540]:
        page.set_viewport_size({'width':width,'height':844})
        box=page.locator('.question-nav [data-act=skip]').bounding_box()
        assert abs(box['x']+box['width']/2-width/2)<2
        assert page.locator('main').bounding_box()['height']<=page.locator('.question-nav').bounding_box()['y']
        x,y=box['x']+box['width']/2,box['y']+box['height']/2
        for _ in range(2):
            before=qid(page);page.mouse.click(x,y);assert qid(page)!=before
            after=page.locator('.question-nav [data-act=skip]').bounding_box()
            assert abs(after['y']-box['y'])<1
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    assert not dialogs,dialogs
    act(page,'previous');skipped=qid(page);choose(page,'A')
    assert backup(page)['answers'][skipped]['kind']=='choice'
    # Ten saved/skipped responses produce a cumulative recovery download.
    page.goto(html.as_uri());restore(page,seed(['02'],current='M02_01'))
    for i in range(9):act(page,'skip')
    with page.expect_download() as download:act(page,'skip')
    ten=json.loads(download.value.path().read_text());assert ten['savedCount']==10 and len(ten['answers'])==10
    assert all(a['kind']=='skip' for a in ten['answers'].values())
    page.goto(html.as_uri());restore(page,ten);assert qid(page)=='M02_11'
    assert backup(page)['answers']==ten['answers']
    # Every safety question can be skipped and then answered; support remains after advancing.
    page.goto(html.as_uri());restore(page,seed(['06'],current='M06_01'))
    act(page,'skip');assert qid(page)=='M06_02'
    act(page,'previous');choose(page,'B');assert qid(page)=='M06_02'
    assert page.locator('#support-message').is_visible()
    assert page.locator('#support-message a[href^="tel:+371116123"]').is_visible()
    assert not page.locator('#support-message a[href="tel:112"]').count()
    assert page.evaluate('document.activeElement.id')=='support-message'
    act(page,'dismissSupport');choose(page,'B');assert page.locator('#support-message').is_visible() # escalation
    assert page.locator('#support-message a[href="tel:112"]').is_visible()
    act(page,'dismissSupport');choose(page,'B');assert not page.locator('#support-message').count() # no identical interruption
    act(page,'support');assert page.locator('#support-message').is_visible()
    page.screenshot(path='/tmp/pilot-support.png',full_page=True)
    # Text remains manually saved and both fields optional.
    page.goto(html.as_uri());restore(page,seed(['33'],current='M33_01'))
    page.locator('#shortText').fill('SYNTHETIC EXAMPLE');assert backup(page)['answers']=={}
    act(page,'save');assert qid(page)=='M33_02'
    act(page,'save');assert qid(page)=='M32_02';assert backup(page)['answers']['M33_02']['kind']=='skip'
    act(page,'previous');page.locator('#shortText').fill('EXAMPLE');act(page,'save')
    # Old recovery with implicit mandatory opening migrates without dropping data.
    legacy=seed(['02','21'],{'M33_01':{'kind':'text','value':'SYNTHETIC','status':'answered'},'M06_02':response(['B'])},'M02_01')
    del legacy['layoutVersion'];page.goto(html.as_uri());restore(page,legacy)
    migrated=backup(page);assert migrated['answers']['M06_02']['codes']==['B']
    assert set(migrated['selected'])=={'02','21','06','18','23','31','33'}
    invalid={**migrated,'answers':{'M02_01':response(['Z'])}};restore(page,invalid)
    assert page.get_by_text('Cannot load this file. Check its format and version.').is_visible()
    assert backup(page)['answers']==migrated['answers']
    # Real output includes selected answers, explicit uncertainty/refusal, no skipped rows or IDs.
    records={'M33_01':{'kind':'text','value':'SYNTHETIC EXAMPLE','status':'answered'},'M06_02':response(['B']),'M06_01':response(['A']),'M02_03':response(['B']),'M02_02':response(['D']),'M02_11':response(['C']),'M02_12':response(['J']),'M02_01':{'kind':'skip','status':'skipped'}}
    page.goto(html.as_uri());restore(page,seed(['02','06','33'],records,'M02_01'))
    act(page,'results');act(page,'doctor')
    doc=page.locator('#reportText').input_value()
    assert 'SYNTHETIC EXAMPLE' in doc and 'M06_02' not in doc
    assert doc.index('SYNTHETIC EXAMPLE')<doc.index('Do you currently intend to die by suicide?')
    assert 'Saved answers: 7' in doc and 'Skipped questions: 1' in doc
    assert 'Over the past 2 weeks.' in doc
    page.evaluate('window.__copied=null;Object.defineProperty(navigator,"clipboard",{value:{writeText:async t=>{window.__copied=t}},configurable:true})')
    act(page,'copyDoctor');assert page.evaluate('window.__copied')==doc
    with page.expect_download() as event:act(page,'downloadReport')
    report_html=event.value.path().read_text();assert '<pre>' in report_html and 'SYNTHETIC EXAMPLE' in report_html
    page.emulate_media(media='print');assert page.locator('.print-report').is_visible()
    assert not page.locator('footer').is_visible();page.pdf(path='/tmp/pilot-report.pdf',format='A4');page.emulate_media(media='screen')
    act(page,'ai');text=page.locator('#reportText').input_value()
    assert 'M02_' not in text and 'DECODING KEY' not in text and '"codes"' not in text
    assert 'Little interest or pleasure' not in text and "I don't know / I'm not sure" in text and 'Prefer not to answer.' in text
    act(page,'copyAI');assert page.evaluate('window.__copied')==text
    for lang in ['lv','ru','en']:
        page.select_option('#language',lang)
        assert page.locator('#reportText').input_value().endswith(build.build_bundle()['ui'][lang]['aiInstruction'])
    # Tools and docs are after main content, collapsed by default.
    assert not page.locator('footer details[open]').count()
    assert page.locator('footer details').count()==6
    # Keyboard and restore review sequence remain usable without a forced opening.
    page.goto(html.as_uri());restore(page,seed(['02'],current='M02_01'))
    page.locator('input[value=A]').focus();page.keyboard.press('Space');assert qid(page)=='M02_02'
    old_review=seed(['02'],{},'M06_01',reviewQueue=['M06_01','M06_02'],reviewReturn={'screen':'question','id':'M02_01'})
    del old_review['layoutVersion'];page.goto(html.as_uri());restore(page,old_review)
    act(page,'skip');assert qid(page)=='M06_02';act(page,'skip');assert qid(page)=='M02_01'
    # Single and multi changes must not replace the persistent supportive message.
    act(page,'support');act(page,'sections');page.locator('[data-jump="23"]').click()
    page.locator('input[value=A]').check();assert page.locator('#support-message a[href^="tel:+371116123"]').count()==1
    assert not errors,errors;assert not network,network
    browser.close()
print('PASS: offline single/multi/text, double tap, fixed repeated Skip, back/edit, support, recovery/legacy/invalid, reports/copy/print, three languages; native Android UNVERIFIED.')
