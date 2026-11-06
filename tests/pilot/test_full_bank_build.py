"""Verify the explicit full-bank bundle and self-contained HTML build."""
import importlib.util
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("pilot_build", ROOT / "tools" / "build_pilot.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

pilot = build.build_bundle()
assert sum(len(group["questions"]) for group in pilot["groups"]) == 60

full = build.build_bundle(full_bank=True)
assert full["schema"] == "offline-questionnaire-full-bank-v1"
assert full["build_mode"] == "full_bank"
assert [group["id"] for group in full["groups"]] == build.read_json(
    ROOT / "src" / "pilot" / "modules" / "layout.json"
)["full_order"]
assert all(group["required"] is False for group in full["groups"])
questions = [question for group in full["groups"] for question in group["questions"]]
assert len(questions) == 712
assert len({question["id"] for question in questions}) == 712
assert len({question["order"] for question in questions}) == 712
assert all(set(question["translations"]) == {"lv", "en", "ru"} for question in questions)
by_id = {question["id"]: question for question in questions}
source_by_id = {
    question["id"]: question
    for group in build.build_source_groups()
    for question in group["questions"]
}
assert by_id == source_by_id
positions = {question["id"]: index for index, question in enumerate(questions)}
for question in questions:
    for language in ("lv", "en", "ru"):
        translation = question["translations"][language]
        assert translation["title"]
        assert set(translation["choices"]) == set(question["choiceCodes"])
    condition = question.get("context")
    assert not condition or (
        condition["id"] in by_id
        and by_id[condition["id"]]["order"] < question["order"]
        and positions[condition["id"]] < positions[question["id"]]
    )

presentation = full["presentation"]
assert set(presentation["topicOrder"]) == {group["id"] for group in full["groups"]}
for question_id, rule in presentation["questions"].items():
    assert question_id in by_id
    assert all(code in by_id[question_id]["choiceCodes"]
               for code in rule.get("support", {}))
for question_id, codes in presentation["boldAnswers"].items():
    assert question_id in by_id
    assert all(code in by_id[question_id]["choiceCodes"] for code in codes)

html = build.make_html(full_bank=True)
assert html.count('id="pilot-data"') == 1
assert "<script src=" not in html and "<link rel=" not in html
assert "connect-src &#39;none&#39;" in html
assert "fetch(" not in html and "XMLHttpRequest" not in html
embedded = re.search(
    r'<script id="pilot-data" type="application/json">(.*?)</script>', html, re.S
)
assert embedded
assert json.loads(embedded.group(1)) == full

with tempfile.TemporaryDirectory() as temp_dir:
    output_path = Path(temp_dir) / "full-bank.html"
    subprocess.run(
        ["python3", str(ROOT / "tools" / "build_pilot.py"), "--full-bank",
         "--output", str(output_path)],
        check=True, capture_output=True, text=True,
    )
    cli_html = output_path.read_text(encoding="utf-8")
    cli_data = re.search(
        r'<script id="pilot-data" type="application/json">(.*?)</script>', cli_html, re.S
    )
    assert cli_data and json.loads(cli_data.group(1)) == full

print("PASS: explicit full-bank build embeds 712 questions/48 optional groups; default pilot remains 60.")
