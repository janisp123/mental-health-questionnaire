"""Full questionnaire navigation and report orders remain separate and complete."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "questionnaire_build", ROOT / "tools" / "build_questionnaire.py"
)
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

bundle = build.build_bundle()
layout = json.loads((ROOT / "src/questionnaire/layout.json").read_text())
presentation = bundle["presentation"]
expected = {f"S{number:02d}" for number in range(1, 16)}
navigation = [group["id"] for group in bundle["groups"]]
assert len(navigation) == 15 and set(navigation) == expected
assert navigation == [group["id"] for group in layout["section_groups"]]
assert all(not group["required"] for group in bundle["groups"])
assert all(36 <= group["questionCount"] <= 70 for group in bundle["groups"])
assert navigation[0] == "S11" and navigation[-1] == "S05"
assert len(presentation["topicOrder"]) == 15
assert set(presentation["topicOrder"]) == expected
assert presentation["topicOrder"][0] == "S11" and presentation["topicOrder"][-1] == "S05"

questions = [question for group in bundle["groups"] for question in group["questions"]]
positions = {question["id"]: index for index, question in enumerate(questions)}
by_id = {question["id"]: question for question in questions}
assert len(positions) == 712
assert all(
    not question.get("context") or positions[question["context"]["id"]] < positions[question["id"]]
    for question in questions
)
assert by_id["M32_02"]["originModule"] == 33 and by_id["M32_02"]["sourceModule"] == "33"
assert by_id["M32_02"]["module"] == "S11"
assert {q["sourceModule"] for q in questions} == {f"{n:02d}" for n in range(1,49)}

report_position = {key: index for index, key in enumerate(presentation["topicOrder"])}
assert presentation["topicOrder"][-4:] == ["S02", "S03", "S04", "S05"]
print("PASS: all 712 IDs occur once; 15 user sections each contain 36–70 questions; report order is independently complete.")
