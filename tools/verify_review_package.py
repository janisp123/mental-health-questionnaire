#!/usr/bin/env python3
"""Verify package bytes and the embedded current questionnaire data."""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path
import build_questionnaire as build


def verify(folder, with_zip=False):
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["schema"] == "questionnaire-review-package-v1"
    assert manifest["source_dirty"] is False, "Package was built from uncommitted source"
    assert len(manifest["files"]) == 2
    for record in manifest["files"]:
        assert Path(record["name"]).name == record["name"], "Invalid package filename"
        content = (folder / record["name"]).read_bytes()
        assert len(content) == record["bytes"] and hashlib.sha256(content).hexdigest() == record["sha256"], record["name"]
        if record["name"].endswith(".html"):
            embedded = re.search(r'<script id="questionnaire-data" type="application/json">(.*?)</script>', content.decode("utf-8"), re.S)
            assert embedded and json.loads(embedded.group(1)) == build.build_bundle(), "Package differs from current source"
        else:
            assert record["name"].endswith(".pdf") and content.startswith(b"%PDF-"), "Expected HTML/PDF pair"
    if with_zip:
        record = manifest["zip"]
        assert Path(record["name"]).name == record["name"]
        content = (folder / record["name"]).read_bytes()
        assert hashlib.sha256(content).hexdigest() == record["sha256"]
        with zipfile.ZipFile(folder / record["name"]) as archive:
            assert set(archive.namelist()) == {item["name"] for item in manifest["files"]}
            assert archive.testzip() is None
            for item in manifest["files"]:
                assert archive.read(item["name"]) == (folder / item["name"]).read_bytes()
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", nargs="?", type=Path, default=build.ROOT / "MH_Public_version")
    parser.add_argument("--with-zip", action="store_true")
    args = parser.parse_args()
    manifest = verify(args.folder, args.with_zip)
    print("PASS: current HTML/PDF bytes, embedded questionnaire and package checksums:", manifest["version"])
