"""Real offline browser helpers; no live/patient responses."""
import json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
import build_pilot as build

def launch(pw):
    return pw.chromium.launch(executable_path=os.getenv('PILOT_BROWSER'),args=['--no-sandbox'])

def act(page,key):
    button=page.locator(f'[data-act="{key}"]:visible').first
    if not button.count():
        page.locator('footer details').first.locator('summary').click()
        button=page.locator(f'[data-act="{key}"]:visible').first
    button.click()

def qid(page):
    return page.locator('.question').get_attribute('data-question')

def choose(page,code):
    page.wait_for_timeout(520)
    page.locator(f'input[name="answer"][value="{code}"]').locator('..').click()

def backup(page):
    with page.expect_download() as event: act(page,'backup')
    return json.loads(event.value.path().read_text())

def restore(page,payload):
    page.locator('#restore').set_input_files({'name':'synthetic.json','mimeType':'application/json','buffer':json.dumps(payload).encode()})
    page.wait_for_timeout(80)

def seed(selected,answers=None,current=None,**extra):
    return dict(schema='mental-pilot-recovery-v1',version='0.1.0-prototype',layoutVersion='optional-topics-v1',lang='en',selected=selected,sectionConfirmed=True,answers=answers or {},currentId=current,savedCount=len(answers or {}),**extra)

def response(codes): return {'kind':'choice','codes':codes,'status':'answered','savedAt':'2026-11-06T12:00:00Z'}

def open_page(browser,path,width=390):
    page=browser.new_page(accept_downloads=True,offline=True,viewport={'width':width,'height':844})
    errors=[];network=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.on('request',lambda r:network.append(r.url) if r.url.startswith(('http:','https:')) else None)
    page.on('dialog',lambda d:d.accept())
    page.goto(path.as_uri());page.select_option('#language','en')
    return page,errors,network
