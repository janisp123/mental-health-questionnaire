# Active development changelog — mental-health-questionnaire

**Active branch:** `develop`. Main and the historical Google Drive release remain untouched.
**Current build:** one self-contained offline HTML with all 48 modules and 712 original questions. Automated desktop Chromium checks pass. This is a technical-review build, not a release or clinical validation.
**Outstanding external checks:** actual Android Chrome use; human review of LV interface wording and EN/RU drafts; professional/clinical review. Do not mark those complete without evidence.
**History:** the prior pilot and full-build chronology is preserved in [CHANGELOG_HISTORY_2026-11-06.md](history/CHANGELOG_HISTORY_2026-11-06.md). Read it only when a task needs that history.

## 2026-11-06 · RUNTIME-MODULARITY-AND-FOCUSED-TESTS · IN_PROGRESS

**Goal:** make current project status unambiguous, separate runtime tests by behavior, and split shared runtime logic only along independently testable boundaries. Preserve the 48-module bank and single-file offline build.

**Baseline:** `d250271a83dfcb17799fdbf66f26bf416488722a` on `develop`; it matches the GitHub branch. Checklist commit: `5ef185a`.

**Verified baseline:** component workflow 42247708071 and full offline Chromium workflow 42247707973 passed at code commit `4d6ff92002b1b3a686954eaf95743b0d61c5f398`. Source integrity confirmed 48 modules/712 IDs; no physical Android check was run.

**Checklist:**

1. [DONE] Audit current source, test, and branch state.
2. [DONE] Replace pilot-first status with this active handoff and archive the previous chronology.
3. [IN_PROGRESS] Split runtime browser checks into focused synthetic-data cases; browser run awaits CI.
4. [IN_PROGRESS] Extract query/model, answer-flow, and recovery behavior into tested modules.
5. [TODO] Add a focused browser layout check for CSS changes.
6. [TODO] Update architecture, file index, manifest, and CI routing as needed.
7. [TODO] Run the relevant GitHub checks and one full integration run after structural work.
8. [BLOCKED] Physical Android testing and human language/clinical review require a device or reviewers.

**Guardrails:** keep source questions, IDs, codes, conditions, and frozen references unchanged; preserve recovery compatibility; keep script and style order explicit in `src/app/build.json`; add no runtime dependencies. Work in small verified commits.

**Checkpoint 1 — changelog cleanup:** moved the previous 495-line chronology byte-for-byte to docs/history/CHANGELOG_HISTORY_2026-11-06.md; the active changelog is now a concise current status/checkpoint. Updated docs/FILE_INDEX.md so archived pilot IN_PROGRESS entries cannot be mistaken for current work.

**Files:** docs/CHANGELOG.md, docs/history/CHANGELOG_HISTORY_2026-11-06.md, docs/FILE_INDEX.md.
**Checks:** archive compared byte-for-byte with the starting changelog; git diff --check PASS. No application test needed.
**Commit:** e77f79ae1f136574dfb15185a98bd452412f6512.
**Next action:** add focused synthetic feedback/recovery cases; retain the existing full-bank browser journey as the integration gate.

**Checkpoint 2 — focused runtime test foundation:** added a three-question synthetic bundle and an isolated browser case for one-tap choice, deferred multi-select save, skip, and offline operation. Added a focused app workflow so screen/style/locale edits run the app checks without automatically triggering the full 712-question integration workflow. The full-bank workflow remains the integration gate and can still be run manually.

**Files:** .github/workflows/app-components.yml, .github/workflows/questionnaire-checks.yml, tests/app/runtime_fixture.py, tests/app/test_runtime_answers.py, docs/FILE_INDEX.md, docs/QUESTIONNAIRE_ARCHITECTURE.md, docs/CHANGELOG.md.
**Checks:** app source manifest, locale catalogs, all isolated screen renderers, Python syntax, synthetic bundle assembly, and `git diff --check` PASS. Browser execution is pending CI: local Playwright Chromium download returned a truncated archive, so no local browser result is claimed.
**Commit:** pending.
**Next action:** extract question visibility, active queue, and progress queries into an independently tested model module; then extend the synthetic cases for feedback and recovery.

**Checkpoint 3 — question model extracted:** moved lookup tables, conditional visibility, active/report question lists, safety tagging, and progress counts into `src/app/core/model.js`. `app.js` now delegates those queries. Added the module to the explicit build manifest and a Node test for parent conditions, optional sections, progress, order, and duplicate IDs.

**Files:** src/app/core/model.js, src/app/core/app.js, src/app/build.json, tests/app/test_model.js, .github/workflows/app-components.yml, docs/QUESTIONNAIRE_ARCHITECTURE.md, docs/CHANGELOG.md.
**Checks:** model behavior, app source manifest, UI catalogs, isolated screen tests, JS syntax, synthetic bundle assembly, and `git diff --check` PASS. Chromium browser execution still awaits CI because local browser download failed.
**Commit:** pending.
**Next action:** split feedback/recovery browser behavior into focused synthetic cases, then move validated recovery parsing out of the coordinator.
