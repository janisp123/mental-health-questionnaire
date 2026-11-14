"""Offline feedback sharing: real UI, synthetic health data, no actual email sending."""
import sys
import tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'full_bank'))
from browser_helpers import act, backup, launch, open_page, restore
from runtime_fixture import write_fixture, LOCALES

with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
    path = Path(tmp) / 'feedback.html'
    write_fixture(path)
    browser = launch(pw)
    page, errors, network = open_page(browser, path)
    act(page, 'start')
    page.locator('[data-module="S01"]').check()
    act(page, 'confirm')
    saved = backup(page)
    saved['answers'] = {'SYN_01': {'kind':'choice','codes':['A'],'status':'answered'},
                        'SYN_02': {'kind':'choice','codes':['B'],'status':'answered'}}
    saved['feedback'] = {'SYN_01': {'reasons':['question'],'comment':'ā ё ї & + #?','language':'en','version':'synthetic-test','updatedAt':'2026-11-14T12:00:00Z'}}
    restore(page, saved)
    # Reject clipboard access to exercise the dependable manual fallback.
    page.evaluate("Object.defineProperty(navigator, 'clipboard', {configurable:true,value:{writeText:()=>Promise.reject(new Error('blocked'))}})")
    page.evaluate("window.testConfirmations=[]; window.confirm=(message)=>{window.testConfirmations.push(message); return false;}")
    for locale in LOCALES:
        page.select_option('#language', locale)
        act(page, 'results')
        act(page, 'feedbackReport')
        text = page.locator('#feedback-copy').input_value()
        assert 'ā ё ї & + #?' in text and 'SYN_01' in text
        assert 'SYN_02' not in text and 'Option A' not in text
        assert page.locator('[data-act="sendFeedback"]').is_enabled()
        page.locator('[data-act="copyFeedback"]').focus()
        page.keyboard.press('Enter')
        page.wait_for_timeout(50)
        assert page.locator('#feedback-copy').evaluate('(el)=>document.activeElement===el && el.selectionEnd===el.value.length')
        assert page.locator('[role="status"]').last.inner_text()
        # Dismiss the warning: no handoff occurs, report stays open.
        act(page, 'sendFeedback')
        assert page.evaluate('window.testConfirmations.length') and page.locator('#feedback-copy').is_visible()
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        act(page, 'resultScreen')
    # Multiple flags + long Unicode exceed the encoded mailto budget, without truncation.
    saved['feedback']['SYN_01']['comment']='ї'*500
    saved['feedback']['SYN_02']={**saved['feedback']['SYN_01'], 'comment':'Second flag'}
    page.evaluate('window.confirm=()=>true')
    restore(page, saved)
    act(page, 'results');act(page, 'feedbackReport')
    assert page.locator('[data-act="sendFeedback"]').is_disabled()
    text=page.locator('#feedback-copy').input_value()
    assert 'ї'*500 in text and 'Second flag' in text
    assert page.locator('[data-act="copyFeedback"]').is_enabled()
    assert not errors, errors
    assert not network, network
    browser.close()
print('PASS: four-language offline feedback, cancellation, clipboard rejection, long text and multiple flags; no HTTP requests.')
