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
              'removeFeedback','feedbackChooseReason'}
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
    assert not errors,errors;assert not network,network
    browser.close()
print('PASS: feedback edit/remove, Save & Continue skip/preserve, recovery compatibility and invalid-feedback rejection; native Android UNVERIFIED.')
