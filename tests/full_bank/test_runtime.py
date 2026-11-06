"""Offline browser smoke test for the complete 48-module questionnaire."""
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright
from browser_helpers import act, backup, launch, open_page, qid
import build_pilot as build


with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
    html_path = Path(tmp) / "questionnaire.html"
    html_path.write_text(build.make_html(full_bank=True), encoding="utf-8")
    browser = launch(pw)
    page, errors, network = open_page(browser, html_path)

    data = page.locator("#pilot-data").evaluate("el => JSON.parse(el.textContent)")
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
    page.locator('input[name="answer"][value="B"]').check()
    assert backup(page)["answers"] == {}
    act(page, "save")
    assert qid(page) == "M23_01"
    page.locator('input[name="answer"][value="B"]').locator("..").dblclick(delay=40)
    assert qid(page) == "M23_02"
    assert backup(page)["answers"]["M23_01"]["codes"] == ["B"]

    # Reach the real medicine-list item via ordinary section navigation.
    act(page, "sections")
    page.locator('[data-jump="14"]').click()
    assert qid(page) == "M14_01"
    page.locator('input[name="answer"][value="B"]').check()
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
    act(page, "results")
    act(page, "doctor")
    report = page.locator("#reportText").input_value()
    assert "SYNTHETIC NAME" in report
    assert "SYNTHETIC MEDICINE" in report
    assert not page.locator('[data-act="ai"]').count()
    assert not errors, errors
    assert not network, network
    browser.close()

print("PASS: 48 sections/712 questions run offline; selection, multi/single, medicine, text and doctor report; Android device UNVERIFIED.")
