"""Offline project-feedback regression; synthetic content only."""
import json,tempfile
from playwright.sync_api import sync_playwright
from browser_helpers import *

with tempfile.TemporaryDirectory() as tmp,sync_playwright() as pw:
    path=Path(tmp)/'pilot.html';path.write_text(build.make_html())
    browser=launch(pw);page,errors,network=open_page(browser,path)
    act(page,'start');qid0=qid(page);assert qid0=='M23_11'
    assert page.locator('[data-act="feedback"]').count()==1
    required={'feedbackFlag','feedbackFlagged','feedbackTitle','feedbackQuestion','feedbackLanguage',
              'feedbackAnswerPrefix','feedbackOther','feedbackComment','feedbackContinue',
              'removeFeedback','feedbackChooseReason','feedbackPrivacy','feedbackProjectCopy',
              'feedbackProjectHeading','feedbackSectionHeading','feedbackReasonLabel',
              'feedbackVersionLabel','feedbackContactLabel','feedbackNone'}
    bundle=build.build_bundle()
    assert all(required<=set(bundle['ui'][lang]) for lang in ('lv','en','ru'))
    code=next(iter(next(q for g in bundle['groups'] for q in g['questions'] if q['id']==qid0)['choiceCodes']))
    for lang in ('lv','ru','en'):
        page.select_option('#language',lang);act(page,'feedback')
        assert bundle['ui'][lang]['feedbackQuestion'] in page.locator('#question-feedback').inner_text()
        answer_label=bundle['ui'][lang]['feedbackAnswerPrefix']+' '+code
        assert answer_label in page.locator('[data-feedback-reason="answer:'+code+'"]').locator('..').inner_text()
        act(page,'feedback')
    act(page,'feedback')
    assert page.locator('#question-feedback').is_visible()
    assert bundle['ui']['en']['feedbackPrivacy'] in page.locator('#question-feedback').inner_text()
    assert page.locator('[data-feedback-reason="answer:A"]').is_visible()
    page.locator('[data-feedback-reason="question"]').check()
    page.locator('[data-feedback-reason="answer:A"]').check()
    page.locator('[data-feedback-reason="other"]').check()
    page.locator('#feedback-comment').fill('Synthetic note')
    act(page,'feedbackContinue')
    saved=backup(page)
    assert saved['answers'][qid0]['kind']=='skip'
    assert saved['feedback'][qid0]['reasons']==['question','answer:A','other']
    assert saved['feedback'][qid0]['comment']=='Synthetic note'
    assert saved['feedback'][qid0]['language']=='en'
    assert qid(page)=='M02_01'

    # Editing/removing feedback leaves the original skipped record unchanged.
    act(page,'previous');assert qid(page)==qid0
    old_answer=backup(page)['answers'][qid0]
    act(page,'feedback');assert page.locator('[data-feedback-reason="question"]').is_checked()
    act(page,'removeFeedback')
    removed=backup(page)
    assert qid0 not in removed['feedback'] and removed['answers'][qid0]==old_answer

    # Save & Continue never changes an existing medical answer.
    answered={'M02_01':response(['B'])}
    page.goto(path.as_uri());restore(page,seed(['02'],answered,'M02_01'))
    act(page,'feedback');page.locator('[data-feedback-reason="language"]').check()
    act(page,'feedbackContinue')
    saved=backup(page)
    assert saved['answers']['M02_01']==answered['M02_01']
    assert saved['feedback']['M02_01']['reasons']==['language']
    assert qid(page)=='M02_02'

    # Older pilot-v1 recovery without feedback restores; invalid feedback is rejected atomically.
    old=seed(['02'],{},'M02_01');page.goto(path.as_uri());restore(page,old)
    with page.expect_download() as event:act(page,'backup')
    current=json.loads(event.value.path().read_text())
    assert current['feedback']=={}
    invalid={**current,'feedback':{'UNKNOWN':{'reasons':['question'],'comment':''}}}
    restore(page,invalid)
    assert page.get_by_text(build.build_bundle()['ui']['en']['restoreError']).is_visible()
    assert qid(page)=='M02_01'

    # Project feedback works with no medical answers and cannot include answer fields.
    marked={'M02_01':{'reasons':['question','answer:B'],'comment':'Synthetic feedback note',
                      'language':'en','version':'v0.2','updatedAt':'2026-11-06T12:00:00Z'}}
    page.goto(path.as_uri());restore(page,seed(['02'],{},'M02_01',feedback=marked))
    act(page,'results')
    page.evaluate('window.__copied=null;Object.defineProperty(navigator,"clipboard",{value:{writeText:async t=>{window.__copied=t}},configurable:true})')
    act(page,'copyFeedback');project=page.evaluate('window.__copied')
    assert 'M02_01' in project and 'Synthetic feedback note' in project
    assert 'janis.paegle.email@gmail.com' in project and 'PRIVATE_PATIENT_SENTINEL' not in project
    assert 'Incorrect answer B' in project
    assert 'EN · v0.2' in project and 'Questionnaire version: 0.2.0-prototype' in project

    # The clinician report lists question feedback before answers, then keeps ordinary information first.
    answers={'M33_01':{'kind':'text','value':'PRIVATE_PATIENT_SENTINEL','status':'answered'},'M06_02':response(['B'])}
    page.goto(path.as_uri());restore(page,seed(['02','33','06'],answers,'M02_01',feedback=marked))
    page.evaluate('window.__copied=null;Object.defineProperty(navigator,"clipboard",{value:{writeText:async t=>{window.__copied=t}},configurable:true})')
    act(page,'results');act(page,'copyFeedback');project=page.evaluate('window.__copied')
    assert 'PRIVATE_PATIENT_SENTINEL' not in project
    act(page,'doctor');doctor=page.locator('#reportText').input_value()
    assert doctor.index(build.build_bundle()['ui']['en']['feedbackSectionHeading'])<doctor.index('PRIVATE_PATIENT_SENTINEL')
    bundle=build.build_bundle()
    safety=next(q for g in bundle['groups'] for q in g['questions'] if q['id']=='M06_02')
    assert doctor.index('PRIVATE_PATIENT_SENTINEL')<doctor.index(safety['translations']['en']['choices']['B'])
    assert not errors,errors;assert not network,network
    browser.close()
print('PASS: feedback edit/remove, Save & Continue skip/preserve, recovery compatibility and invalid-feedback rejection; native Android UNVERIFIED.')
