"""The app manifest assembles small source files without loading the question bank."""
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "questionnaire_build", ROOT / "tools" / "build_questionnaire.py"
)
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

manifest = json.loads((ROOT / "src" / "app" / "build.json").read_text(encoding="utf-8"))
styles, scripts = build.load_app_sources()
assert styles == "".join(
    (ROOT / "src" / "app" / path).read_text(encoding="utf-8")
    for path in manifest["styles"]
)
assert scripts == "".join(
    (ROOT / "src" / "app" / path).read_text(encoding="utf-8")
    for path in manifest["scripts"]
)

fixture = {"ui": {"lv": {"project": "Synthetic test"}}}
document = build.make_html(fixture)
assert "<style>" + styles + "</style>" in document
embedded_script = re.search(r"<script>(.*?)</script>", document, re.S)
assert embedded_script and embedded_script.group(1) == scripts
assert '<script src=' not in document and '<link rel=' not in document
assert "connect-src &#39;none&#39;" in document

print("PASS: explicit app sources assemble offline with a synthetic bundle only.")
