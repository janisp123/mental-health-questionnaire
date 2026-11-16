"""Immediate feedback preserves unsaved medical drafts and separates the queue."""
import sys,tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'full_bank'))
from browser_helpers import act,backup,launch,open_page,qid,restore
from runtime_fixture import write_fixture,LOCALES

with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
 path=Path(tmp)/'feedback.html';write_fixture(path)
 browser=launch(pw);page,errors,network=open_page(browser,path)
 act(page,'start');page.locator('[data-module="S01"]').check();act(page,'confirm')
 base=backup(page)
 base['feedback']={'SYN_02':{'reasons':['other'],'comment':'QUEUED_ONLY','language':'en','version':'test','updatedAt':'2026-11-16T00:00:00Z'}}
 restore(page,base)
 page.evaluate("window.confirm=()=>false; Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:()=>Promise.reject(new Error('unavailable'))}})")
 for locale in LOCALES:
  page.select_option('#language',locale)
  act(page,'feedback')
  while page.locator('[data-feedback-reason]:checked').count():page.locator('[data-feedback-reason]:checked').first.uncheck()
  act(page,'emailQuestionFeedback')
  assert qid(page)=='SYN_01' and page.locator('.notice').inner_text()
  page.locator('[data-feedback-reason="question"]').check()
  page.locator('[data-feedback-reason="answer:B"]').check()
  page.locator('#feedback-comment').fill('Only this flag ā ё ї')
  act(page,'emailQuestionFeedback')
  assert qid(page)=='SYN_01' and page.locator('#feedback-comment').input_value()=='Only this flag ā ё ї'
  text=page.locator('#question-feedback-copy').input_value()
  assert 'Only this flag ā ё ї' in text and 'SYN_01' in text and 'Option B' in text
  assert 'QUEUED_ONLY' not in text and 'SYN_02' not in text
  act(page,'copyQuestionFeedback');page.wait_for_timeout(50)
  assert page.locator('#question-feedback-copy').evaluate('(el)=>document.activeElement===el && el.selectionEnd===el.value.length')
  assert page.locator('#question-feedback-status').inner_text()
  page.locator('#feedback-comment').fill('ї'*500)
  assert page.locator('#question-feedback-copy').count()==0,'Editing feedback must invalidate stale manual copy'
  act(page,'emailQuestionFeedback')
  assert 'ї'*500 in page.locator('#question-feedback-copy').input_value()
  assert qid(page)=='SYN_01'
  saved=backup(page);assert saved['answers']==base['answers'] and saved['feedback']==base['feedback']
  act(page,'feedback')
 # A pending single choice is paused when flagging: retain visible choice, no save/advance.
 page.select_option('#language','en')
 page.locator('input[name="answer"][value="A"]').locator('..').click()
 act(page,'feedback');page.wait_for_timeout(800)
 assert qid(page)=='SYN_01' and page.locator('input[name="answer"][value="A"]').is_checked()
 assert backup(page)['answers']==base['answers']
 # Successful handoff uses a real mailto href but cannot silently send or add to queue.
 page.locator('#feedback-comment').fill('Final feedback')
 page.evaluate("() => {window.confirm=()=>true;window.handoffs=[];window.QuestionnaireFeedbackDelivery.open=url=>window.handoffs.push(url);}")
 act(page,'emailQuestionFeedback')
 assert page.evaluate('window.handoffs.length')==1
 assert page.evaluate('window.handoffs[0]').startswith('mailto:test@example.invalid?')
 assert qid(page)=='SYN_01' and backup(page)['feedback']==base['feedback']
 # Missing handler/exception remains recoverable and preserves unsaved draft.
 page.evaluate("() => {window.QuestionnaireFeedbackDelivery.open=()=>{throw new Error('No email app')};}")
 act(page,'emailQuestionFeedback')
 assert page.locator('#question-feedback-copy').is_visible()
 assert page.locator('#feedback-comment').input_value()=='Final feedback'
 act(page,'feedbackContinue')
 saved=backup(page)
 assert saved['feedback']['SYN_01']['comment']=='Final feedback' and saved['feedback']['SYN_02']==base['feedback']['SYN_02']
 assert not errors,errors
 assert not network,network
 browser.close()
print('PASS: immediate feedback in all locales; reason validation, privacy, cancellation, Unicode/copy fallback, timers, navigation and queue isolation.')
