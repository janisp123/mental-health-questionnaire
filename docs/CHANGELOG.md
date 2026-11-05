# Development changelog — mental-health-questionnaire

**Active task log:** This file on GitHub `develop`, effective 2026-11-05.
**Development edits:** GitHub only, after the relevant sources have been imported and verified.
**Google Drive:** distribution of Latvian public files only. Existing Drive archives are read-only source references until migration is complete; do not update its old changelog for routine work.

## 2026-11-05 · GITHUB-CHANGELOG-HANDOFF · TASK_DONE

**Goal:** switch ongoing task tracking to GitHub, without pretending that the questionnaire source migration is complete.

**Scope:** `docs/CHANGELOG.md`, `docs/MIGRATION_STATUS.md`, `docs/MIGRATION_PLAN.md`, `README.md` (only repository docs). Do not modify published `main`, Google Drive questionnaire or questionnaires.

**Steps:**
1. Create this active changelog with a verified checkpoint.
2. Update conflicting repository instructions and migration status.
3. Read back from GitHub and mark `TASK_DONE` only if all intended documentation is verified.

**Current verified state:** GitHub contains repository scaffolding but **0/48 questionnaire modules**. Direct transfer from Drive to GitHub was blocked. Existing ZIP import package is ready for manual upload; GitHub source is not yet authoritative.
**Next:** revise repository instructions, verify, then close task.

## Carried-forward pending work

- **GITHUB-SOURCE-MIGRATION — BLOCKED:** 48/48 multilingual source modules, HTML reference baselines, translation catalogs, QA tools and archival materials remain on Drive. The verified ZIP package `190_GITHUB_MIGRATION_READY_MANUAL_UPLOAD.zip` must be extracted and manually uploaded on `develop`, then checked against hashes and counts. Do not claim GitHub holds code until file readback.
- **ENRU-V16-RELEASE — IN_PROGRESS:** EN/RU are drafts and require linguistic, functional and safety checks; never publish as ready.
- **RELEASE-GATE-POLICY — PARTIALLY IMPLEMENTED:** documented fail-closed policy and evidence checker exist, but GitHub Actions and enforced branch protection are not yet installed. Syntax passes alone cannot authorize release.
- **LV public distribution:** Google Drive main folder currently contains exactly `162_Sagatavosanas_vizitei_LV_v16.html` and `163_README_LV_v16.md`. Development changes must not silently modify those releases.

## Prior history — immutable reference

Complete detailed historical Latvian changelog remains in the [archived Drive `166_CHANGELOG_LV.md`](https://drive.google.com/file/d/1rfJWIhSogO-vxiabkZWgE0zmFMuk6MBd/view). That file is **read-only** and is not a competing live changelog. Import a historical snapshot into `docs/history/` only after public-repository privacy checks; never overwrite the active log.

## Required operating procedure

1. Start every new editing task by adding a dated `IN_PROGRESS` entry with scope, source paths, plan and next action.
2. Commit and checkpoint after each meaningful, verified step.
3. After actual tests and remote readback, set `TASK_DONE`; for interruptions or failed actions leave `IN_PROGRESS` or `BLOCKED` with exact next action.
4. Only one active task log: `docs/CHANGELOG.md`. `docs/MIGRATION_STATUS.md` may remain a concise directory/reference but is not a second mutable task log after this handoff.
5. `develop` is the work branch; `main` is not a workbench. Publishing to Drive occurs only from an approved tested release candidate, never directly from unverified development.
6. No real patient information, user answers, recovery files, personal medical records, credentials or private correspondence in this public repository.
