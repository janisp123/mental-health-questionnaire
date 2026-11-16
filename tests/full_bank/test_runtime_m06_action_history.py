"""All intent distinctions, same-occasion timing, reports, and old progress."""
import io,tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
from browser_helpers import act,backup,choose,launch,open_page,qid,restore
import build_questionnaire as build

with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
 data=build.build_bundle();by={q['id']:q for g in data['groups'] for q in g['questions']}
 path=Path(tmp)/'q.html';path.write_text(build.make_html(data),encoding='utf-8');browser=launch(pw);page,errors,network=open_page(browser,path)
 act(page,'start');page.locator(f'[data-module="{data["source_module_to_section"]["06"]}"]').check();act(page,'confirm');old=backup(page)
 old.update(version='0.2.16-review+full-bank',currentId='M06_08',answers={q:{'kind':'choice','codes':['A'],'status':'answered','savedAt':'2026-11-16T00:00:00Z'} for q in ('M06_01','M06_06','M06_08')})
 for locale in data['ui']:
  restore(page,{**old,'lang':locale});choose(page,'A')
  assert page.locator('[data-question="M06_26"]').count(),'No to an attempt must not hide independent history'
  for width in (320,390):
   page.set_viewport_size({'width':width,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  for code in 'ABCDEFG':
   restore(page,{**old,'lang':locale,'currentId':'M06_26'});choose(page,code)
   assert qid(page)==('M06_27' if code in 'ABCD' else 'M06_12')
   if code in 'ABCD':choose(page,'B')
   assert page.locator('#support-message').count()==0
   saved=backup(page);assert saved['answers']['M06_26']['codes']==[code] and saved['answers']['M06_08']['codes']==['A']
   restore(page,saved);assert backup(page)['answers']==saved['answers']
   act(page,'results');act(page,'doctor');text=page.locator('.report-preview').inner_text();a=by['M06_26']['translations'][locale]
   assert a['title'] in text and a['choices'][code] in text and a['time'] in text
   assert a['scope'] in text,'Essential scope must survive clinician reports'
   if code in 'ABCD':assert by['M06_27']['translations'][locale]['title'] in text
   else:assert by['M06_27']['translations'][locale]['title'] not in text
   pdf=' '.join(' '.join(p.extract_text() for p in PdfReader(io.BytesIO(page.pdf())).pages).split())
   assert ' '.join(a['title'].split()) in pdf and ' '.join(a['choices'][code].split()) in pdf
   assert ' '.join(a['scope'].split()) in pdf
   act(page,'resultScreen');act(page,'back')
  # Every timing label survives recovery and report rendering in every locale.
  for timing in 'ABCDEFGH':
   payload={**old,'lang':locale,'currentId':'M06_27','answers':{**old['answers'],'M06_26':{'kind':'choice','codes':['C'],'status':'answered'}}}
   restore(page,payload);choose(page,timing);saved=backup(page)
   assert saved['answers']['M06_27']['codes']==[timing]
   restore(page,saved);assert backup(page)['answers']==saved['answers']
   act(page,'results');act(page,'doctor');assert by['M06_27']['translations'][locale]['choices'][timing] in page.locator('.report-preview').inner_text()
   act(page,'resultScreen');act(page,'back')
  # A changed parent does not leak a now-hidden old timing answer into reports.
  stale={**old,'lang':locale,'currentId':'M06_26','answers':{**old['answers'],'M06_26':{'kind':'choice','codes':['A'],'status':'answered'},'M06_27':{'kind':'choice','codes':['A'],'status':'answered'}}}
  restore(page,stale);choose(page,'E');saved=backup(page);assert saved['answers']['M06_27']['codes']==['A']
  act(page,'results');act(page,'doctor');assert by['M06_27']['translations'][locale]['title'] not in page.locator('.report-preview').inner_text()
  act(page,'resultScreen');act(page,'back')
  restore(page,{**old,'lang':locale,'currentId':'M06_26'});act(page,'skip');assert qid(page)=='M06_12';act(page,'previous');assert qid(page)=='M06_26'
 restore(page,{**old,'lang':'en','currentId':'M06_02'});choose(page,'B');assert page.locator('#support-message').is_visible()
 assert not errors,errors
 assert not network,network
 browser.close()
print('PASS: all action/intent and timing responses/locales, No gates, stale-child reports, old/current progress, PDFs, skip/back, existing urgent prompts and no requests.')
