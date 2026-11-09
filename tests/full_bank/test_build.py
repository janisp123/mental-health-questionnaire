"""Verify the default one-file build contains the complete questionnaire."""
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "questionnaire_build", ROOT / "tools" / "build_questionnaire.py"
)
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

bundle = build.build_bundle()
assert bundle["schema"] == "offline-questionnaire-full-bank-v1"
assert [group["id"] for group in bundle["groups"]] == [group["id"] for group in build.read_json(
    ROOT / "src" / "questionnaire" / "layout.json"
)["section_groups"]]
assert all(group["required"] is False for group in bundle["groups"])
assert len(bundle["groups"]) == 15
assert all(group["questionCount"] == len(group["questions"]) and 36 <= group["questionCount"] <= 70 for group in bundle["groups"])
questions = [question for group in bundle["groups"] for question in group["questions"]]
assert len(bundle["groups"]) == 15
assert len(questions) == 712
assert len({question["id"] for question in questions}) == 712
assert len({question["order"] for question in questions}) == 712
assert all(set(question["translations"]) == {"lv", "en", "ru", "uk"} for question in questions)
by_id = {question["id"]: question for question in questions}
source_by_id = {
    question["id"]: question
    for group in build.build_source_groups()
    for question in group["questions"]
}
assert set(by_id) == set(source_by_id)
assert source_by_id["M23_11"]["maxChoices"] == 3
assert "maxChoices" not in by_id["M23_11"]
for question_id, source_question in source_by_id.items():
    grouped_question = dict(by_id[question_id])
    assert grouped_question["sourceModule"] == source_question["module"]
    grouped_question["module"] = grouped_question["sourceModule"]
    expected = dict(source_question)
    if question_id == "M23_11":
        del expected["maxChoices"]
    # Frozen sources own three locales; the active product adds Ukrainian wording.
    grouped_question["translations"] = dict(grouped_question["translations"])
    ukrainian = grouped_question["translations"].pop("uk")
    assert ukrainian["title"]
    assert grouped_question == expected
positions = {question["id"]: index for index, question in enumerate(questions)}
for question in questions:
    for language in ("lv", "en", "ru", "uk"):
        translation = question["translations"][language]
        assert translation["title"]
        assert set(translation["choices"]) == set(question["choiceCodes"])
    condition = question.get("context")
    assert not condition or (
        condition["id"] in by_id
        and by_id[condition["id"]]["order"] < question["order"]
        and positions[condition["id"]] < positions[question["id"]]
    )

presentation = bundle["presentation"]
assert set(presentation["topicOrder"]) == {group["id"] for group in bundle["groups"]}
for question_id, rule in presentation["questions"].items():
    assert question_id in by_id
    assert all(code in by_id[question_id]["choiceCodes"] for code in rule.get("support", {}))
for question_id, codes in presentation["boldAnswers"].items():
    assert question_id in by_id
    assert all(code in by_id[question_id]["choiceCodes"] for code in codes)

html = build.make_html()
assert html.count('id="questionnaire-data"') == 1
assert "<script src=" not in html and "<link rel=" not in html
assert "connect-src &#39;none&#39;" in html
assert "fetch(" not in html and "XMLHttpRequest" not in html
embedded = re.search(
    r'<script id="questionnaire-data" type="application/json">(.*?)</script>', html, re.S
)
assert embedded and json.loads(embedded.group(1)) == bundle

with tempfile.TemporaryDirectory() as temp_dir:
    output_path = Path(temp_dir) / "questionnaire.html"
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "build_questionnaire.py"), "--output", str(output_path)],
        check=True,
        capture_output=True,
        text=True,
    )
    cli_html = output_path.read_text(encoding="utf-8")
    cli_data = re.search(
        r'<script id="questionnaire-data" type="application/json">(.*?)</script>',
        cli_html,
        re.S,
    )
    assert cli_data and json.loads(cli_data.group(1)) == bundle

print("PASS: default CLI creates one offline HTML with all 712 questions in 15 optional sections; original 48-module source mapping is retained.")
