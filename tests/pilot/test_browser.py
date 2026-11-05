#!/usr/bin/env python3
"""Headless Chromium smoke journeys for the two-section offline prototype.

Requires: pip install playwright; python -m playwright install chromium
Runs against a file:// URL. No remote site, tracker or analytics are needed.
"""
from pathlib import Path
import tempfile
import sys

from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT / "tools"))
from build_pilot import make_html

with tempfile.TemporaryDirectory() as temp:
    path=Path(temp)/"prototype.html"
    path.write_text(make_html(),encoding="utf-8")
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,args=["--no-sandbox"])
        page=browser.new_page(accept_downloads=True)
        errors=[]
        page.on("pageerror",lambda err: errors.append(str(err)))
        requests=[]
        page.on("request",lambda request:requests.append(request.url) if request.url.startswith(("https://", "http://")) else None)
        page.goto(path.as_uri())
        assert "Sagatavošanās" in page.locator("h1").inner_text()
        assert page.locator('[data-act="start"]').count()==1
        page.select_option("#language","en")
        assert page.get_by_text("PROTOTYPE · NOT PUBLISHED").count()==1
        page.click('[data-act="choose"]')
        assert page.locator("#optional02").count()==1
        page.locator("#optional02").check()
        page.click('[data-act="confirm"]')
        assert "M33_01" in page.locator(".question").inner_text()
        page.locator("#shortText").fill("FAKE_TEST_NAME")
        # Editing an answer without Save & Next must not commit it.
        page.click('[data-act="results"]')
        assert page.get_by_text("Some opening safety questions still need an answer.").is_visible()
        page.click('[data-act="ai"]')
        assert "free_text_redacted" not in page.locator("#reportText").input_value()
        page.click('[data-act="resultScreen"]')
        page.click('[data-act="back"]')
        assert "M33_01" in page.locator(".question").inner_text()
        page.locator("#shortText").fill("FAKE_TEST_NAME")
        page.click('[data-act="save"]')
        assert "M33_02" in page.locator(".question").inner_text()
        page.select_option("#language","ru")
        assert "M33_02" in page.locator(".question").inner_text()
        page.select_option("#language","en")
        with page.expect_download() as saved:
            page.click('[data-act="backup"]')
        backup=saved.value
        backup_path=Path(temp)/"recovery.json"
        backup.save_as(backup_path)
        assert backup_path.exists()
        page.click('[data-act="results"]')
        page.click('[data-act="ai"]')
        coded=page.locator("#reportText").input_value()
        assert '"status": "free_text_redacted"' in coded
        assert "FAKE_TEST_NAME" not in coded
        page.click('[data-act="resultScreen"]')
        page.once("dialog",lambda d:d.accept())
        page.click('[data-act="new"]')
        page.locator("#restore").set_input_files(str(backup_path))
        page.wait_for_timeout(250)
        assert "M33_02" in page.locator(".question").inner_text()
        # Finish remaining opening and visit optional section with synthetic answers.
        for i in range(45):
            if page.locator(".question").count():
                here=page.locator(".question").inner_text()
                if "M02_01" in here: break
                if "M06_01" in here:
                    assert page.locator('[data-act="skip"]').count()==0
                    page.locator('input[value="B"]').check()
                    assert "112" in page.locator("#safetyHint").inner_text()
                if page.locator("#shortText").count():
                    page.locator("#shortText").fill("")
                else:
                    page.locator('input[name="answer"]').first.check()
                page.click('[data-act="save"]')
            elif page.locator("#optional02").count():
                page.locator("#optional02").check()
                page.click('[data-act="confirm"]')
            else: raise AssertionError("Unexpected screen during opening")
        assert "M02_01" in page.locator(".question").inner_text()
        assert page.locator('[data-act="skipSection"]').count()==1
        page.once("dialog",lambda d:d.accept())
        page.click('[data-act="skipSection"]')
        assert page.locator('[data-act="doctor"]').count()==1
        page.click('[data-act="doctor"]')
        assert page.locator("#reportText").count()==1
        assert page.locator('[data-act="downloadReport"]').count()==1
        page.emulate_media(media="print")
        assert page.locator(".print-report").is_visible()
        assert page.locator(".print-report").inner_text() == page.locator("#reportText").input_value()
        assert page.pdf(prefer_css_page_size=True).startswith(b"%PDF")
        page.emulate_media(media="screen")
        with page.expect_download() as exported:
            page.click('[data-act="downloadReport"]')
        assert "<!doctype html>" in exported.value.path().read_text()
        with page.expect_download() as result:
            page.click('[data-act="reference"]')
        assert result.value.suggested_filename.endswith(".md")
        with page.expect_download() as result:
            page.click('[data-act="downloadTxt"]')
        assert result.value.suggested_filename.endswith(".txt")
        # Revisiting safety must traverse every item, including ones already answered.
        page.click('[data-act="reviewSafety"]')
        seen=[]
        for _ in range(11):
            assert page.locator('[data-act="skip"]').count()==0
            seen.append(page.locator(".question .muted").first.inner_text().split(" · ")[-1])
            page.locator('input[name="answer"]').first.check()
            page.click('[data-act="save"]')
        assert len(set(seen)) == 11 and seen[0] == "M06_01" and seen[-1]=="M06_13"
        assert page.locator("#reportText").is_visible()
        assert not errors,"Javascript errors: "+repr(errors)
        assert not requests,"Runtime network requests: "+repr(requests)
        browser.close()
print("PASS browser: offline, language switching, manual saving, backups, redacted AI, optional section and exports")
print("This is a smoke test, not clinical, translation or full release certification.")

