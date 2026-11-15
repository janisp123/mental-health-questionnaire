"""Question explanations are visible in every locale and preserve existing questions."""
import tempfile,sys
from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_helpers import launch,open_page,restore
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'tools'))
import build_questionnaire as build
bundle=build.build_bundle();questions=[q for g in bundle['groups'] for q in g['questions'] if q['id'] in {'M04_01','M14_02','M02_09'}]
with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
 path=Path(tmp)/'panic.html';path.write_text(build.make_html(bundle),encoding='utf-8');browser=launch(pw)
 for question in questions:
  for locale in bundle['ui']:
   page,errors,network=open_page(browser,path)
   restore(page,{'schema':'mental-pilot-recovery-v1','version':bundle['version'],'layoutVersion':bundle['layout_version'],'lang':locale,'selected':[question['module']],'sectionConfirmed':True,'currentId':question['id'],'answers':{},'feedback':{}})
   help=page.get_by_text(question['translations'][locale]['help'],exact=True);assert help.is_visible()
   assert help.inner_text()==question['translations'][locale]['help']
   assert page.locator('#question-heading').inner_text()==question['translations'][locale]['title']
   for width in (320,390):
    page.set_viewport_size({'width':width,'height':844});assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
   assert not errors,errors
   assert not network,network
   page.close()
 browser.close()
print('PASS: panic, medicine and safety guidance visible in every locale; titles and 320/390px layouts preserved.')
