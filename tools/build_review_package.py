#!/usr/bin/env python3
"""Build a versioned offline HTML/PDF package without overwriting an existing one."""
import argparse
import hashlib
import io
import json
import re
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

import reportlab
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer

import build_questionnaire as build

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATHS = ["src", "translations", "tools", "assets/fonts", "docs/review/GUIDE_LV_EN_RU_UK.md"]


def git(*arguments):
    return subprocess.check_output(["git", *arguments], cwd=ROOT, text=True).strip()


def guide_pdf(source):
    if reportlab.Version != "4.4.9":
        raise ValueError("Install the pinned tools/review-requirements.txt before building the PDF")
    font_dir = ROOT / "assets/fonts"
    manifest = build.read_json(font_dir / "manifest.json")
    for name, record in manifest.items():
        path = font_dir / name
        if hashlib.sha256(path.read_bytes()).hexdigest() != record["sha256"]:
            raise ValueError("Review font checksum differs: " + name)
        pdfmetrics.registerFont(TTFont(record["font_name"], str(path)))
    body = ParagraphStyle("GuideBody", fontName="GuideSans", fontSize=11, leading=16, spaceAfter=9)
    heading = ParagraphStyle("GuideLanguage", parent=body, fontName="GuideSansBold", fontSize=15, leading=20, spaceAfter=11)
    story = []
    for section in source.split("# "):
        if not section.strip():
            continue
        title, *paragraphs = section.strip().split("\n\n")
        blocks = [Paragraph(escape(title), heading)]
        blocks += [Paragraph(escape(text.strip()).replace("\n", " "), body) for text in paragraphs if text.strip()]
        story += [KeepTogether(blocks), Spacer(1, 18)]
    stream = io.BytesIO()
    document = SimpleDocTemplate(stream, pagesize=A4, leftMargin=48, rightMargin=48,
                                 topMargin=42, bottomMargin=42, invariant=1,
                                 title="Four-language questionnaire guide", author="Mental health questionnaire project")
    document.build(story)
    if document.page != 1:
        raise ValueError("The short reviewer guide must fit on one A4 page")
    return stream.getvalue()


def build_package(destination):
    if destination.exists():
        raise ValueError("Output directory already exists; choose a new versioned destination")
    config = build.read_json(build.QUESTIONNAIRE / "build.json")
    bundle = build.build_bundle()
    version = re.match(r"\d+\.\d+\.\d+", bundle["version"]).group()
    epoch = config["buildEpoch"]
    timestamp = datetime.fromtimestamp(epoch, timezone.utc)
    if timestamp.year < 1980:
        raise ValueError("buildEpoch must be a ZIP-compatible timestamp")
    # ReportLab invariant mode fixes PDF internal timestamps/IDs; ZIP uses the pinned epoch.
    files = {
        f"187_Questionnaire_FULL_712Q_LV_EN_RU_UK_v{version}_REVIEW_BUILD.html": build.make_html(bundle).encode("utf-8"),
        f"188_README_LV_EN_RU_UK_v{version}_REVIEW_BUILD.pdf": guide_pdf((ROOT / config["reviewGuide"]).read_text(encoding="utf-8")),
    }
    archive_stream = io.BytesIO()
    with zipfile.ZipFile(archive_stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(files.items()):
            info = zipfile.ZipInfo(name, timestamp.timetuple()[:6])
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    zip_name = f"QUESTIONNAIRE_LV_EN_RU_UK_v{version}_REVIEW_BUILD.zip"
    zip_bytes = archive_stream.getvalue()
    record = lambda name, content: {"name": name, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()}
    manifest = {
        "schema": "questionnaire-review-package-v1", "version": bundle["version"],
        "source_commit": git("rev-parse", "HEAD"), "source_tree": git("rev-parse", "HEAD^{tree}"),
        "source_dirty": bool(git("status", "--porcelain", "--", *SOURCE_PATHS)),
        "build_epoch": epoch, "pdf_timestamp_mode": "reportlab-invariant",
        "languages": list(bundle["ui"]), "question_count": sum(len(group["questions"]) for group in bundle["groups"]),
        "guide_source": config["reviewGuide"], "files": [record(name, content) for name, content in files.items()],
        "zip": record(zip_name, zip_bytes), "status": "TECHNICAL_REVIEW_NOT_CLINICALLY_VALIDATED",
    }
    destination.mkdir(parents=True, exist_ok=False)
    for name, content in {**files, zip_name: zip_bytes}.items():
        (destination / name).write_bytes(content)
    (destination / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist/review")
    args = parser.parse_args()
    try:
        manifest = build_package(args.output_dir)
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + "\n")
    print("Review package:", args.output_dir)
    print("Version:", manifest["version"], "Languages:", ", ".join(manifest["languages"]))
    for record in manifest["files"]:
        print(record["sha256"], record["name"])
    if manifest["source_dirty"]:
        print("Working source differs from HEAD; commit sources and rebuild before distribution.")


if __name__ == "__main__":
    main()
