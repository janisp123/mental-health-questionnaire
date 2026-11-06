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
expected = {f"{number:02d}" for number in range(1, 49)}
navigation = [group["id"] for group in bundle["groups"]]
assert len(navigation) == 48 and set(navigation) == expected
assert navigation == layout["full_order"]
assert all(not group["required"] for group in bundle["groups"])
assert navigation[0] == "23" and navigation[-1] == "33"
assert len(presentation["topicOrder"]) == 48
assert set(presentation["topicOrder"]) == expected
assert presentation["topicOrder"][0] == "33" and presentation["topicOrder"][-1] == "48"

questions = [question for group in bundle["groups"] for question in group["questions"]]
positions = {question["id"]: index for index, question in enumerate(questions)}
by_id = {question["id"]: question for question in questions}
assert len(positions) == 712
assert all(
    not question.get("context") or positions[question["context"]["id"]] < positions[question["id"]]
    for question in questions
)
assert by_id["M32_02"]["originModule"] == 33 and by_id["M32_02"]["module"] == "33"

report_position = {key: index for index, key in enumerate(presentation["topicOrder"])}
assert all(report_position[key] > report_position["16"] for key in ("06", "10", "18", "19", "21"))
print("PASS: all 712 IDs occur once; all optional sections navigate in full order; report order is independently complete.")
