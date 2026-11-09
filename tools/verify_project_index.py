#!/usr/bin/env python3
"""Verify imported original file hashes and question-module structure. Not a release test."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "project-manifest.json").read_text(encoding="utf-8"))
files = manifest["files"]
assert len(files) == len({f["path"] for f in files}) == 79
for f in files:
    data = (root / f["path"]).read_bytes()
    sha = hashlib.sha1(("blob " + str(len(data)) + chr(0)).encode() + data).hexdigest()
    assert len(data) == f["bytes"] and sha == f["git_blob_sha1"], f["path"]
index = json.loads((root / "tests/fixtures/181_MODULE_INDEX_v16.json").read_text(encoding="utf-8"))
assert index["section_count"] == 48 and index["question_count"] == 712
ids, orders = set(), set()
for part in index["module_files"]:
    section = part["section"]
    name = part["name"]
    data = (root / "src/modules" / name).read_bytes()
    assert hashlib.sha256(data).hexdigest() == part["sha256"], name
    module = json.loads(data)
    assert module["section"] == section and len(module["entries"]) == module["count"]
    for q in module["entries"]:
        lv = q["lv"]
        assert lv["id"] not in ids and q["order"] not in orders
        assert lv["section"] == section
        for lang in ("en", "ru"):
            assert set(q[lang]["choices"]) == set(lv["choices"])
        ids.add(lv["id"])
        orders.add(q["order"])
assert len(ids) == 712 and orders == set(range(712))
print("PASS: 79 original files, 48 module hashes, 712 question IDs and orders")
print("This is not clinical, browser, or translation validation.")
