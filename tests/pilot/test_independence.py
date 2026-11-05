"""Run against disposable module files and synthetic answers only."""
import json
import shutil
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import build_pilot as build


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")


def snapshot(root):
    return {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def build_page(folder, name):
    path = folder / name
    path.write_text(build.make_html(), encoding="utf-8")
    return path.as_uri()


with tempfile.TemporaryDirectory() as tmp, sync_playwright() as pw:
    temp = Path(tmp)
    source = temp / "pilot"
    shutil.copytree(build.SOURCE, source)
    build.SOURCE = source
    before = snapshot(source)
    modules = source / "modules"
    registry = build.read_json(modules / "registry.json")
    # A single synthetic question keeps this test independent of future clinical edits.
    question = {"id": "TEST21", "order": 10000, "choiceCodes": ["A","B"], "multi": False}
    module = modules / "21"
    module.mkdir()
    follow = {**question, "id":"TEST21_F", "order":10001, "context":{"id":"TEST21","showValues":["A"]}}
    write(module / "logic.json", {"group":"21","questions":[question,follow]})
    registry["groups"].append({"id":"21","required":False,"question_count":2})
    write(modules / "registry.json", registry)
    for lang in build.LANGS:
        write(module / (lang + ".json"), {"module":"21","lang":lang,"title":"Test 21 "+lang,
              "questions":{"TEST21":{"title":"Original "+lang,"choices":{"A":"A","B":"B"}},
                           "TEST21_F":{"title":"Conditional "+lang,"choices":{"A":"A","B":"B"}}}})
    assert all((source/p).read_bytes()==v for p,v in before.items() if p!=Path("modules/registry.json"))
    old = build_page(temp, "before.html")
    baseline = snapshot(source)
    locale = module / "en.json"
    english = build.read_json(locale)
    english["questions"]["TEST21"]["title"] = "Edited English question"
    write(locale, english)
    new = build_page(temp, "after.html")
    assert {p for p,v in baseline.items() if (source/p).read_bytes()!=v} == {locale.relative_to(source)}

    browser = pw.chromium.launch()
    page = browser.new_page(accept_downloads=True, offline=True)
    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    def click(action):
        page.locator(f'[data-act="{action}"]').click()

    page.goto(old)
    page.select_option("#language","en")
    click("guide")
    assert not page.locator("#optional02").is_checked()
    assert page.get_by_text("Low mood, loss of interest or changes in mood").is_visible()
    click("all")
    assert page.locator("#optional21").is_checked()
    click("confirm")
    # Complete the opening using the normal controls. Verify the tenth-save file.
    saved = 0
    while "M02_01" not in page.locator(".question").inner_text():
        assert saved < 25
        if page.locator("#shortText").count():
            page.locator("#shortText").fill("SYNTHETIC")
        else:
            page.locator('input[name="answer"]').first.check()
        saved += 1
        if saved == 10:
            with page.expect_download() as recovery:
                click("save")
            payload = json.loads(recovery.value.path().read_text())
            assert payload["savedCount"] == len(payload["answers"]) == 10
        else:
            click("save")
    page.once("dialog",lambda d:d.accept())
    click("skipSection")
    assert page.locator(".question h2").inner_text() == "Original en"
    page.locator('input[value="A"]').check()
    click("save")
    assert page.locator(".question h2").inner_text()=="Conditional en"
    click("previous")
    page.locator('input[value="B"]').check()
    click("save")
    with page.expect_download() as recovery:
        click("backup")
    backup = temp / "synthetic.json"
    recovery.value.save_as(backup)
    previous = json.loads(backup.read_text())
    page.goto(new)
    page.locator("#restore").set_input_files(backup)
    page.wait_for_selector('.question')
    assert page.locator(".question h2").inner_text() == "Edited English question"
    assert page.locator('input[value="B"]').is_checked()
    for lang in ("lv","ru","en"):
        page.select_option("#language",lang)
        expected = "Edited English question" if lang=="en" else "Original "+lang
        assert page.locator(".question h2").inner_text() == expected
    with page.expect_download() as recovery:
        click("backup")
    restored = json.loads(recovery.value.path().read_text())
    assert restored["answers"] == previous["answers"]
    assert restored["selected"] == previous["selected"] == ["02","21"]
    click("sections")
    page.locator('[data-jump="21"]').click()
    assert page.locator(".question h2").inner_text() == "Edited English question"
    click("results")
    click("doctor")
    assert "Test 21 en: 1/1" in page.locator("#reportText").input_value()
    click("ai")
    report=page.locator("#reportText").input_value()
    answers=json.loads(report[report.index("{"):report.index("DECODING KEY")])["answers"]
    assert next(a for a in answers if a["id"]=="TEST21_F")["status"]=="hidden"
    click("sections")
    page.locator("#optional21").uncheck()
    click("confirm")
    click("results")
    click("ai")
    coded=page.locator("#reportText").input_value()
    records=json.loads(coded[coded.index("{"):coded.index("DECODING KEY")].strip())["answers"]
    record=next(row for row in records if row["id"]=="TEST21")
    assert record["status"]=="omitted" and record["codes"]==[]
    assert not errors, errors
    browser.close()
print("PASS: registry-only addition, isolated English edit, skip continuation and recovery across builds")
