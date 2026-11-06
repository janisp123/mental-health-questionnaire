"""Real section 21 source-to-UI-to-report roundtrip, independently read frozen labels."""
import tempfile
from playwright.sync_api import sync_playwright
from browser_helpers import *
bank=json.loads((ROOT/'src/modules/182_MODULE_21_LV_EN_RU_v16.json').read_text())
with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
    html=Path(tmp)/'pilot.html';html.write_text(build.make_html())
    browser=launch(pw);page,errors,network=open_page(browser,html)
    act(page,'choose');page.locator('#optional21').check();act(page,'confirm')
    expected={}
    for entry in bank['entries']:
        id=entry['lv']['id'];assert qid(page)==id
        assert page.locator('.question h2').inner_text()==entry['en']['title']
        for code,label in entry['en']['choices'].items():
            assert page.locator(f'input[value="{code}"]').locator('..').inner_text()==label
        if id=='M21_06':
            page.locator('input[value=A]').check();page.locator('input[value=E]').check();act(page,'save')
            assert 'A + E' in page.locator('.notice').inner_text()
            page.locator('input[value=E]').uncheck();page.locator('input[value=B]').check()
            expected[id]=['A','B'];act(page,'save')
        elif entry['lv'].get('multi'):
            code=next(iter(entry['lv']['choices']));page.locator(f'input[value={code}]').check();expected[id]=[code];act(page,'save')
        else:
            code='B' if id=='M21_15' else next(iter(entry['lv']['choices']));expected[id]=[code];choose(page,code)
        if id=='M21_15':assert page.locator('#support-message a[href="tel:112"]').is_visible()
    saved=backup(page);assert saved['selected']==['21']
    assert {k:saved['answers'][k]['codes'] for k in expected}==expected
    page.goto(html.as_uri());restore(page,saved)
    damaged=json.loads(json.dumps(saved));damaged['answers']['M21_06']['codes']=['A','E'];restore(page,damaged)
    assert page.get_by_text('Cannot load this file. Check its format and version.').is_visible()
    assert backup(page)['answers']==saved['answers']
    act(page,'results');act(page,'doctor');doctor=page.locator('#reportText').input_value()
    assert 'Saved answers: 19' in doctor
    assert doctor.rstrip().endswith('Currently.): Yes') # current dangerous urging is last
    act(page,'ai');report=page.locator('#reportText').input_value()
    assert 'M21_' not in report and 'DECODING KEY' not in report
    # Each output line uses the independent source's exact selected response(s) and time.
    lines=report.splitlines()[1:-2];assert len(lines)==19
    for entry,line in zip(bank['entries'],lines):
        id=entry['lv']['id'];t=entry['en'];assert t['time'] in line
        assert line.endswith(': '+'; '.join(t['choices'][c] for c in expected[id]))
    assert not errors,errors;assert not network,network;browser.close()
print('PASS: 19 frozen-source questions/choices, incompatibility handling, support, restoration, compact doctor and AI response fidelity.')
