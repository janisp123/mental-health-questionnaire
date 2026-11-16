"""M06 hypothetical context: all responses/locales, current safety and old progress."""
import io,json,tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
from browser_helpers import act,backup,choose,launch,open_page,qid,restore
import build_questionnaire as build

with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
 data=build.build_bundle();by_id={q['id']:q for g in data['groups'] for q in g['questions']}
 path=Path(tmp)/'questionnaire.html';path.write_text(build.make_html(data),encoding='utf-8')
 browser=launch(pw);page,errors,network=open_page(browser,path)
 act(page,'start');page.locator(f'[data-module="{data["source_module_to_section"]["06"]}"]').check();act(page,'confirm')
 old=backup(page);old['version']='0.2.15-review+full-bank';old['currentId']='M06_24'
 old['answers']={'M06_01':{'kind':'choice','codes':['A'],'status':'answered','savedAt':'2026-11-15T00:00:00Z'}}
 for locale in data['ui']:
  restore(page,{**old,'lang':locale});assert qid(page)=='M06_24'
  act(page,'skip');assert page.locator('[data-question="M06_25"]').count(),'No to current thoughts must not hide this independent item'
  for width in (320,390):
   page.set_viewport_size({'width':width,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  for code in 'ABCDEF':
   payload={**old,'lang':locale,'currentId':'M06_25'};restore(page,payload)
   assert qid(page)=='M06_25'
   assert page.locator('#question-heading').inner_text()==by_id['M06_25']['translations'][locale]['title']
   choose(page,code)
   assert page.locator('#support-message').count()==0,'Hypothetical answer must not infer current emergency'
   saved=backup(page);record=saved['answers']['M06_25'];assert record['codes']==[code]
   assert saved['answers']['M06_01']['codes']==['A']
   restore(page,saved);assert backup(page)['answers']==saved['answers']
   act(page,'results');act(page,'doctor');preview=page.locator('.report-preview').inner_text();t=by_id['M06_25']['translations'][locale]
   assert t['title'] in preview and t['choices'][code] in preview
   pdf=' '.join(' '.join(p.extract_text() for p in PdfReader(io.BytesIO(page.pdf())).pages).split())
   assert ' '.join(t['title'].split()) in pdf and ' '.join(t['choices'][code].split()) in pdf
   act(page,'resultScreen');act(page,'back')
  restore(page,{**old,'lang':locale,'currentId':'M06_25'});act(page,'skip');assert backup(page)['answers']['M06_25']['kind']=='skip'
  act(page,'back');assert qid(page)=='M06_25'
  act(page,'previous');assert qid(page)=='M06_24'
  act(page,'skip');assert qid(page)=='M06_25'
 # Explicit current intent retains the existing emergency prompt.
 restore(page,{**old,'lang':'en','currentId':'M06_02'});choose(page,'B')
 assert page.locator('#support-message').is_visible()
 assert not errors,errors
 assert not network,network
 browser.close()
print('PASS: M06_25 every response/locale in progress, preview and PDF; old imports, skip/back, phone widths, current safety unchanged and no requests.')
