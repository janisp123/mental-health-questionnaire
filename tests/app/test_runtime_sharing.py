"""Public-only sharing, empty reports and confirmed reset; synthetic data only."""
import sys,tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'full_bank'))
from browser_helpers import act,backup,launch,open_page,restore
from runtime_fixture import write_fixture,LOCALES

URL='https://janisp123.github.io/mental-health-questionnaire/'
with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
 path=Path(tmp)/'sharing.html';write_fixture(path);browser=launch(pw)
 for locale in LOCALES:
  page,errors,network=open_page(browser,path)
  page.select_option('#language',locale)
  data=page.locator('#questionnaire-data').evaluate('e=>JSON.parse(e.textContent)');ui=data['ui'][locale]
  contributions=page.locator('#project-contributions')
  assert contributions.is_visible(),'Contributions must stay visible even without names'
  contributions.locator('summary').click()
  assert ui['projectContributors'] in contributions.inner_text()
  assert ui['contributionsInvitation'] in contributions.inner_text()
  assert 'test@example.invalid' not in contributions.inner_text()
  payload={'schema':'mental-pilot-recovery-v1','version':'synthetic-test','layoutVersion':data['layout_version'],'lang':locale,'selected':['S01'],'sectionConfirmed':True,'currentId':'SYN_01','answers':{'SYN_01':{'kind':'choice','codes':['B'],'status':'answered'}},'feedback':{'SYN_01':{'reasons':['question'],'comment':'PRIVATE_FEEDBACK_SENTINEL','language':'en','version':'synthetic-test','updatedAt':'2026-11-15T06:00:00Z'}}}
  restore(page,payload);act(page,'results');act(page,'doctor')
  assert page.locator('[data-act="print"]').is_visible()
  assert 'Single choice' in page.locator('.report-preview').inner_text()
  # Cancel reset: existing answers and report survive.
  page.evaluate('window.confirm=()=>false');act(page,'new')
  assert 'Single choice' in page.locator('.report-preview').inner_text()
  page.evaluate("window.shared=[];window.copied=[];Object.defineProperty(navigator,'share',{configurable:true,writable:true,value:async value=>{window.shared.push(value)}});Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async value=>{window.copied.push(value)}}})")
  act(page,'shareQuestionnaire')
  field=page.locator('#questionnaire-share-copy');text=field.input_value()
  assert text==ui['shareMessage']+'\n'+URL
  for private in ('PRIVATE_FEEDBACK_SENTINEL','SYN_01','Option B','synthetic-test'):assert private not in text
  assert page.evaluate('window.shared.length+window.copied.length')==0,'Opening must not transmit or copy'
  act(page,'nativeShare');page.wait_for_timeout(30)
  assert page.evaluate('window.shared')==[{'title':ui['shareTitle'],'text':ui['shareMessage'],'url':URL}]
  act(page,'copyQuestionnaire');page.wait_for_timeout(30)
  assert page.evaluate('window.copied')==[text]
  assert page.locator('#questionnaire-share-status').inner_text()==ui['shareCopied']
  page.evaluate("()=>{navigator.share=()=>Promise.reject(new DOMException('cancel','AbortError'));}")
  act(page,'nativeShare');page.wait_for_timeout(30)
  assert page.locator('#questionnaire-share-status').inner_text()==ui['shareCancelled']
  page.evaluate("()=>{navigator.share=()=>Promise.reject(new Error('blocked'));navigator.clipboard.writeText=()=>Promise.reject(new Error('blocked'));}")
  act(page,'nativeShare');page.wait_for_timeout(30)
  assert page.locator('#questionnaire-share-status').inner_text()==ui['shareCopyHelp']
  act(page,'copyQuestionnaire');page.wait_for_timeout(30)
  assert field.evaluate('(e)=>document.activeElement===e && e.selectionEnd===e.value.length')
  assert page.locator('#questionnaire-share-status').inner_text()==ui['shareCopyHelp']
  page.evaluate("Object.defineProperty(navigator,'share',{configurable:true,value:undefined});Object.defineProperty(navigator,'clipboard',{configurable:true,value:undefined})")
  act(page,'shareQuestionnaire');act(page,'shareQuestionnaire')
  assert page.locator('[data-act="nativeShare"]').count()==0
  act(page,'copyQuestionnaire')
  assert field.evaluate('(e)=>e.selectionEnd===e.value.length')
  assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
  page.emulate_media(media='print')
  assert not page.locator('#questionnaire-sharing').is_visible()
  assert not page.locator('[data-act="new"]').is_visible()
  page.emulate_media(media='screen')
  page.evaluate('window.confirm=()=>true');act(page,'new')
  assert page.locator('[data-act="start"]').is_visible()
  assert page.locator('#language').input_value()==locale
  saved=backup(page)
  assert saved['answers']=={} and saved['feedback']=={} and saved['selected']==[]
  act(page,'results');act(page,'doctor')
  assert page.locator('[data-act="print"]').count()==0
  assert ui['reportEmpty'] in page.locator('.report-preview').inner_text()
  assert page.locator('[data-act="back"]').is_visible()
  assert not errors,errors
  assert not network,network
  page.close()
 browser.close()
print('PASS: localized public-only sharing/copy fallbacks, no automatic transmission, print isolation, empty reports, consented reset and visible contributions.')
