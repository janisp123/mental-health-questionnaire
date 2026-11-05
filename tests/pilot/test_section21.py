"""Offline UI round trip using real section 21 and independently loaded v16 labels."""
import json
import os
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from build_pilot import make_html

bank = json.loads((ROOT/"src/modules/182_MODULE_21_LV_EN_RU_v16.json").read_text())
with TemporaryDirectory() as tmp, sync_playwright() as pw:
    directory = Path(tmp)
    html = directory/"pilot.html"
    html.write_text(make_html(), encoding="utf-8")
    browser = pw.chromium.launch(executable_path=os.getenv("PILOT_BROWSER"))
    page = browser.new_page(offline=True, accept_downloads=True)
    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))

    def click(action):
        page.locator(f'[data-act="{action}"]').click()

    def check(code):
        page.locator(f'input[name="answer"][value="{code}"]').check()

    page.goto(html.as_uri())
    page.select_option("#language","en")
    click("choose")
    page.locator("#optional21").check()
    click("confirm")
    for _ in range(20):
        if page.locator("#shortText").count():
            page.locator("#shortText").fill("")
        else:
            page.locator('input[name="answer"]').first.check()
        click("save")

    expected = {}
    for entry in bank["entries"]:
        qid = entry["lv"]["id"]
        assert qid in page.locator(".question").inner_text()
        assert page.locator(".question h2").inner_text() == entry["en"]["title"]
        if qid == "M21_06":
            check("A")
            check("E")
            click("save")
            assert "A + E" in page.locator('[role="status"]').inner_text()
            page.locator('input[value="E"]').uncheck()
            check("B")
            expected[qid] = ["A","B"]
        else:
            code = "B" if qid=="M21_15" else next(iter(entry["lv"]["choices"]))
            check(code)
            expected[qid] = [code]
            if qid=="M21_15":
                assert "112" in page.locator("#safetyHint").inner_text()
        click("save")

    with page.expect_download() as download:
        click("backup")
    backup=directory/"saved.json"
    download.value.save_as(backup)
    saved=json.loads(backup.read_text())
    assert saved["selected"]==["21"]
    assert {k:saved["answers"][k]["codes"] for k in expected}==expected
    page.goto(html.as_uri())
    page.locator("#restore").set_input_files(backup)
    page.wait_for_selector(".question")
    damaged=directory/"invalid.json"
    saved["answers"]["M21_06"]["codes"]=["A","E"]
    damaged.write_text(json.dumps(saved))
    page.locator("#restore").set_input_files(damaged)
    page.get_by_text("Cannot load this file. Check its format and version.").wait_for()
    click("results")
    click("doctor")
    doctor=page.locator("#reportText").input_value()
    assert "21 · Unusual experiences: 19/19" in doctor
    urgent=next(e["en"] for e in bank["entries"] if e["lv"]["id"]=="M21_15")
    assert urgent["title"]+": "+urgent["choices"]["B"] in doctor
    click("ai")
    report=page.locator("#reportText").input_value()
    records=json.loads(report[report.index("{"):report.index("DECODING KEY")])["answers"]
    assert {r["id"]:r["codes"] for r in records if r["module"]=="21"}==expected
    for entry in bank["entries"]:
        qid=entry["lv"]["id"]
        line=next(line for line in report.splitlines() if line.startswith(qid+": "))
        assert entry["en"]["title"] in line
        for code in expected[qid]:
            assert code+"="+entry["en"]["choices"][code] in line
    assert not errors, errors
    browser.close()
print("PASS: 19 real section 21 answers, conflicting choice rejection, backup, restore, doctor report and AI decoding")
