"""Offline browser regression for the complete 48-module questionnaire."""
import json
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright
from browser_helpers import act, backup, choose, launch, open_page, qid, restore
import build_questionnaire as build


with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
    html_path = Path(tmp) / "questionnaire.html"
    html_path.write_text(build.make_html(), encoding="utf-8")
    browser = launch(pw)
    page, errors, network = open_page(browser, html_path)

    data = page.locator("#questionnaire-data").evaluate("el => JSON.parse(el.textContent)")
    assert len(data["groups"]) == 48
    questions = [q for group in data["groups"] for q in group["questions"]]
    assert len(questions) == 712
    assert len({q["id"] for q in questions}) == 712

    # All sections are optional, and the section picker exposes the full bank.
    page.locator('[data-act="all"]').click()
    assert page.locator("input[data-module]").count() == 48
    assert page.locator("input[data-module]:checked").count() == 48
    page.locator('[data-act="confirm"]').click()

    # Multi-select is manually saved; single-select saves once even on a double tap.
    assert qid(page) == "M23_11"
    page.locator('input[name="answer"][value="A"]').check()
    choose(page, "B")
    assert backup(page)["answers"] == {}
    act(page, "save")
    assert qid(page) == "M23_01"
    page.locator('input[name="answer"][value="B"]').locator("..").dblclick(delay=40)
    assert qid(page) == "M23_02"
    assert backup(page)["answers"]["M23_01"]["codes"] == ["B"]

    # Feedback is separate from a saved medical answer and survives recovery.
    act(page, "previous")
    act(page, "feedback")
    page.locator('[data-feedback-reason="question"]').check()
    page.locator("#feedback-comment").fill("Synthetic question note")
    act(page, "feedbackContinue")
    saved = backup(page)
    assert saved["answers"]["M23_01"]["codes"] == ["B"]
    assert saved["feedback"]["M23_01"]["reasons"] == ["question"]
    assert saved["feedback"]["M23_01"]["comment"] == "Synthetic question note"
    restore(page, saved)
    round_trip = backup(page)
    assert round_trip["answers"] == saved["answers"]
    assert round_trip["feedback"] == saved["feedback"]

    # A real conditional follow-up appears for an applicable parent answer.
    act(page, "sections")
    page.locator('[data-jump="01"]').click()
    assert qid(page) == "M01_01"
    for question_number in range(1, 8):
        choose(page, "A")
        assert qid(page) == f"M01_{question_number + 1:02d}"
    choose(page, "B")
    assert qid(page) == "M01_09"
    choose(page, "A")
    assert qid(page) == "M01_10"

    # The full-bank safety rules still produce the gentle support message.
    act(page, "sections")
    page.locator('[data-jump="06"]').click()
    assert qid(page) == "M06_01"
    choose(page, "B")
    assert page.locator("#support-message").is_visible()
    assert page.locator('#support-message a[href^="tel:+371116123"]').is_visible()
    act(page, "dismissSupport")

    # Reach the real medication-list item via ordinary section navigation.
    act(page, "sections")
    page.locator('[data-jump="14"]').click()
    assert qid(page) == "M14_01"
    choose(page, "B")
    assert qid(page) == "M14_02", f"Expected medication form next, got {qid(page)}"
    page.locator('[data-med-index="0"][data-med-field="name"]').fill("SYNTHETIC MEDICINE")
    act(page, "save")
    assert backup(page)["answers"]["M14_02"]["kind"] == "medicine"

    # Text questions are manually saved and remain in the clinician report.
    act(page, "sections")
    page.locator('[data-jump="33"]').click()
    assert qid(page) == "M33_01"
    page.locator("#shortText").fill("SYNTHETIC NAME")
    act(page, "save")
    assert qid(page) == "M33_02"
    skip_box = page.locator('.question-nav [data-act="skip"]').bounding_box()
    assert abs(skip_box["x"] + skip_box["width"] / 2 - 195) < 2
    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
    act(page, "skip")
    assert qid(page) != "M33_02"
    assert backup(page)["answers"]["M33_02"]["kind"] == "skip"
    act(page, "previous")
    assert qid(page) == "M33_02"
    act(page, "results")
    page.evaluate('window.__copied=null;Object.defineProperty(navigator,"clipboard",{value:{writeText:async t=>{window.__copied=t}},configurable:true})')
    act(page, "copyFeedback")
    page.wait_for_function("window.__copied!==null")
    project_feedback = page.evaluate("window.__copied")
    assert "Synthetic question note" in project_feedback
    assert "SYNTHETIC NAME" not in project_feedback
    assert "SYNTHETIC MEDICINE" not in project_feedback
    act(page, "doctor")
    report = page.locator("#reportText").input_value()
    assert "SYNTHETIC NAME" in report
    assert "SYNTHETIC MEDICINE" in report
    assert report.index("Question feedback") < report.index("SYNTHETIC NAME")
    page.evaluate('window.__copied=null;Object.defineProperty(navigator,"clipboard",{value:{writeText:async t=>{window.__copied=t}},configurable:true})')
    act(page, "copyDoctor")
    page.wait_for_function("window.__copied!==null")
    assert page.evaluate("window.__copied") == report
    page.emulate_media(media="print")
    assert page.locator(".report-preview").is_visible()
    assert not page.locator("footer").is_visible()
    pdf_path = Path(tmp) / "doctor-report.pdf"
    page.pdf(path=str(pdf_path), format="A4")
    assert pdf_path.stat().st_size > 1000
    page.emulate_media(media="screen")
    for language in ("lv", "ru", "en"):
        page.select_option("#language", language)
        assert page.locator(".report-preview h1").inner_text() == data["ui"][language]["doctorHeading"]
    assert not page.locator('[data-act="ai"]').count()
    assert not errors, errors
    assert not network, network

    # A fresh full-bank run downloads cumulative recovery after ten skips.
    recovery_page, recovery_errors, recovery_network = open_page(browser, html_path)
    recovery_page.locator('[data-act="start"]').click()
    first = questions[0]
    for language in ("lv", "ru", "en"):
        recovery_page.select_option("#language", language)
        assert recovery_page.locator(".question h2").inner_text() == first["translations"][language]["title"]
    for _ in range(9):
        act(recovery_page, "skip")
    with recovery_page.expect_download() as event:
        act(recovery_page, "skip")
    ten_skips = json.loads(event.value.path().read_text())
    assert ten_skips["savedCount"] == 10 and len(ten_skips["answers"]) == 10
    assert all(answer["kind"] == "skip" for answer in ten_skips["answers"].values())
    restore(recovery_page, ten_skips)
    assert backup(recovery_page)["answers"] == ten_skips["answers"]
    assert not recovery_errors, recovery_errors
    assert not recovery_network, recovery_network
    recovery_page.close()
    browser.close()

print("PASS: full offline runtime includes selection, answer types, conditions, support, feedback/recovery, skip/back, copy/print, three locales, and ten-answer recovery. Android device UNVERIFIED.")
