# Project navigation — start here

**Current date of this navigation file:** 2026-11-05. **AUTHORITATIVE TASK STATUS: archive-root `166_CHANGELOG_LV.md` only (Drive ID `1rfJWIhSogO-vxiabkZWgE0zmFMuk6MBd`).** Do not use an old recovery manifest to decide where work ended. This file is a directory guide, not a second changelog.

## Where files live

- **PUBLIC (exactly 2 files):** https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb — Latvian `162_Sagatavosanas_vizitei_LV_v16.html` and Latvian `163_README_LV_v16.md` only. EN/RU drafts are NOT in this public folder until translation/release checks pass.
- **ARCHIVE / DEVELOPMENT ROOT:** https://drive.google.com/drive/folders/1GxGJBMYRMz0WbjBlYx_XVtXmlSdFvGQy — this file, `180_ARCHIVE_INDEX_2026-11-05.md`, and **authoritative `166_CHANGELOG_LV.md`** (unchanged Drive file ID).
- **01_SOURCE:** https://drive.google.com/drive/folders/1vMwhcFhL1_m4CStsZvWs-QMHlxm31Wl6 — module validator/build tool, module index, development instructions.
- **48 TRI-LANGUAGE QUESTION MODULES:** https://drive.google.com/drive/folders/14r888FSYwahZEulnjeA__kSgkdd2qTvj — `182_MODULE_XX_LV_EN_RU_v16.json` for section XX.
- **02_TRANSLATIONS:** https://drive.google.com/drive/folders/1NbBgbpBfchYM9QAlVxKpxTZwT-qERUkS — EN/RU v16 HTML drafts + EN/RU draft README, full question catalogs, translation memory, corrections, the 1,202-row Google Sheet, audit and plan.
- **03_TESTS:** https://drive.google.com/drive/folders/1LN_GnEeZSN6dxTolqZ7oV8e5nRVukGlC — testing and build diagnostics.
- **04_DOCUMENTATION:** https://drive.google.com/drive/folders/17IZYMOHzJFci-EU3cxE2fSco5iTqmzh4 — LV v16 information PDF and draft EN/RU information PDFs.
- **05_HISTORY:** https://drive.google.com/drive/folders/1bOlPni_6VkdF90bIjVG1i7kDf75Rs4Ub — older published versions / superseded PDFs / outdated manifest (historical only).

## Efficient AI workflow

1. Read the **top of the archive-root changelog** to identify `IN_PROGRESS`/`BLOCKED` and the last *verified* checkpoint; this file gives routing links only.
2. For an ordinary wording edit in section 11, read only `182_MODULE_11_LV_EN_RU_v16.json` and, if needed, the relevant neighboring module. Do not reload the entire HTML and all prior translations just to change a word.
3. Keep stable IDs, answer codes, medical timeframe, conditional logic, and answer-status semantics. Track all LV→EN/RU effects before publication. Review translation provenance before trusting a phrase.
4. Use `183_MODULE_TOOLS_v16.py` with all 48 module files and the current HTML as *templates* to validate or prepare new HTML drafts. The tool never publishes, never changes existing HTML, and does not translate the non-question UI text.
5. Only check complete HTML and end-to-end tests when preparing a release. Record finished steps and blockers in the changelog. Until verified multilingual release, keep **exactly 2 LV files** in public folder; all drafts, changelog and development material are in the archive.

## Release safety

Latvian v16 is the functional source baseline (712 questions, 48 sections). English/Russian v16 remain DRAFT and have NOT passed full clinical or functional verification; `ENRU-V16-RELEASE` is still `IN_PROGRESS` in the changelog. The modular data is a lossless question-bank snapshot only, not independent app code. No question wording was edited by the folder reorganization.

## Public folder language-release rule (2026-11-05)

User requested Latvian-only public distribution until English and Russian translations pass all required checks. Moving drafts does not change their bytes or certify them. GitHub source migration remains BLOCKED/unfinished; Drive archive is authoritative.
