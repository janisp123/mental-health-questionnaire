# Active development changelog — mental-health-questionnaire

**Active branch:** `develop`; `main` and the frozen v16 Git reference remain unchanged. The old Drive v16 copies were removed from the link-shared review folder; the current technical-review candidate is indexed in the manifest.
**Current build:** one self-contained offline HTML with 48 unchanged source modules / 712 questions grouped into 15 user-facing sections. GitHub app and full-bank workflows passed; the current technical-review HTML and Latvian PDF are in the linked Drive folder. This is not a public release or clinical validation.
**Outstanding external checks:** actual Android Chrome use; human review of LV interface wording and EN/RU drafts; professional/clinical review. Do not mark those complete without evidence.
**History:** the prior pilot and full-build chronology is preserved in [CHANGELOG_HISTORY_2026-11-06.md](history/CHANGELOG_HISTORY_2026-11-06.md). Read it only when a task needs that history.

## 2026-11-07 · SECTION-END-SAVE-PROMPT · IN_PROGRESS

**Starting commit:** `b2964d660afdb319e4dd695485e2be50797489f9` on `develop`.

**Change:** removed automatic recovery-file downloads while answering. When a user reaches the end of a section, the app now recommends saving and offers “Save and continue” or “Continue without saving” in LV/EN/RU. The existing manual save control remains. A section-boundary recovery file points to the next question so it resumes in the right place.

**Files:** `src/app/core/app.js`, `src/app/i18n/ui.lv.json`, `src/app/i18n/ui.en.json`, `src/app/i18n/ui.ru.json`, `tests/app/runtime_fixture.py`, `tests/app/test_runtime_answers.py`, `tests/full_bank/browser_helpers.py`, `docs/QUESTIONNAIRE_ARCHITECTURE.md`, `docs/CHANGELOG.md`.

**Checks:** locale-catalog check PASS; complete 712-question offline HTML build PASS. The focused browser test could not run locally because this workspace has no Chromium executable; browser behavior remains unverified here. Full-bank regression was not run.

**Next action:** run the focused browser workflow in CI or a machine with Chromium. No Google Drive copy was updated.

## 2026-11-06 · FULL-GIT-REVIEW-CANDIDATE · PREPARED

**Source:** GitHub `develop` application and question sources, commit `7e236310e4b57ceb7f2e9e8e3e8988387e6c1814` (48 modules, 712 questions). Manifest checkpoint `af284d880efeb0032e4ad4391e43aa6d33d992d4`.

**Candidate:** [Google Drive review folder](https://drive.google.com/drive/folders/1BUlc5W7tRw06JOUE250wCuTe-1ick9xb). It contains `187_Questionnaire_FULL_712Q_v0.2.0_REVIEW_BUILD.html` (SHA-256 `a6998ab5539d037493b97e724b7dda6080196d67fb7cb5b75f905dbc9b4bbb70`) and `188_README_LV_v0.2.0_REVIEW_BUILD.pdf`. The editable Markdown source is kept privately in `04_DOCUMENTATION`. Latvian is the reference language; EN/RU are unreviewed drafts. This is not a final or clinically validated release.

**Old Drive copies:** The frozen v16 HTML and README had direct “anyone with the link” reader access and were permanently removed from the shared Drive folder. Their unchanged frozen copies remain under `reference/baseline/` in Git.

**Verification:** Local builder, `test_build.py`, `test_source_adapter.py`, and `test_source_audit.py` PASS. Full GitHub workflow 42276293734 PASS on `af284d880efeb0032e4ad4391e43aa6d33d992d4`, including full offline desktop Chromium journey; focused app workflow 42258847072 PASS. Local Playwright was unavailable, so no separate local browser run. Native Android and clinical review remain outstanding.

**Next action:** Share this candidate with professionals if you choose; collect review notes against the candidate version. Do not treat the build as clinical validation.

## 2026-11-06 · RUNTIME-MODULARITY-AND-FOCUSED-TESTS · IN_PROGRESS

**Goal:** make current project status unambiguous, separate runtime tests by behavior, and split shared runtime logic only along independently testable boundaries. Preserve the 48-module bank and single-file offline build.

**Baseline:** `d250271a83dfcb17799fdbf66f26bf416488722a` on `develop`; it matches the GitHub branch. Checklist commit: `5ef185a`.
**Latest verified implementation commit:** `731455a`. GitHub `develop` is `af615ac8ca0573aae4f2744d4b2e4429deef2364`; local and remote trees match exactly.
**Latest verified workflow commit:** focused workflow 42258847072 passed on the current branch head.

**Verified baseline:** component workflow 42247708071 and full offline Chromium workflow 42247707973 passed at code commit `4d6ff92002b1b3a686954eaf95743b0d61c5f398`. Source integrity confirmed 48 modules/712 IDs; no physical Android check was run.

**Checklist:**

1. [DONE] Audit current source, test, and branch state.
2. [DONE] Replace pilot-first status with this active handoff and archive the previous chronology.
3. [DONE] Split runtime browser checks into focused synthetic-data cases; answer, feedback, and recovery browser cases passed CI.
4. [DONE] Extract query/model, answer-flow, and recovery behavior into tested modules.
5. [DONE] Add a focused browser layout check for CSS changes.
6. [DONE] Update architecture, file index, manifest, and CI routing as needed.
7. [DONE] Run focused checks and the full integration workflow after structural work.
8. [BLOCKED] Physical Android testing and human language/clinical review require a device or reviewers.
9. [DONE] Isolate delegated DOM event wiring behind tested callbacks; focused and full CI passed.
10. [DONE] Reuse runner-provided Chrome in focused CI; install bundled Chromium only when unavailable.
11. [DONE] Use plain-language file save/resume labels and explicitly warn that session progress is lost when the browser closes unless saved to a file.

**Guardrails:** keep source questions, IDs, codes, conditions, and frozen references unchanged; preserve recovery compatibility; keep script and style order explicit in `src/app/build.json`; add no runtime dependencies. Work in small verified commits.

**Checkpoint 1 — changelog cleanup:** moved the previous 495-line chronology byte-for-byte to docs/history/CHANGELOG_HISTORY_2026-11-06.md; the active changelog is now a concise current status/checkpoint. Updated docs/FILE_INDEX.md so archived pilot IN_PROGRESS entries cannot be mistaken for current work.

**Files:** docs/CHANGELOG.md, docs/history/CHANGELOG_HISTORY_2026-11-06.md, docs/FILE_INDEX.md.
**Checks:** archive compared byte-for-byte with the starting changelog; git diff --check PASS. No application test needed.
**Commit:** e77f79ae1f136574dfb15185a98bd452412f6512.
**Next action:** add focused synthetic feedback/recovery cases; retain the existing full-bank browser journey as the integration gate.

**Checkpoint 2 — focused runtime test foundation:** added a three-question synthetic bundle and an isolated browser case for one-tap choice, deferred multi-select save, skip, and offline operation. Added a focused app workflow so screen/style/locale edits run the app checks without automatically triggering the full 712-question integration workflow. The full-bank workflow remains the integration gate and can still be run manually.

**Files:** .github/workflows/app-component-checks.yml, .github/workflows/questionnaire-checks.yml, tests/app/runtime_fixture.py, tests/app/test_runtime_answers.py, docs/FILE_INDEX.md, docs/QUESTIONNAIRE_ARCHITECTURE.md, docs/CHANGELOG.md.
**Checks:** app source manifest, locale catalogs, all isolated screen renderers, Python syntax, synthetic bundle assembly, and `git diff --check` PASS. Focused Chromium run 42252272675 exposed a test expectation issue: the browser preserves selection order, so the assertion was corrected to compare the selected codes without ordering. Local Playwright Chromium download returned a truncated archive.
**Commit:** 19afae8; focused test correction: fa5207b.
**Next action:** extract question visibility, active queue, and progress queries into an independently tested model module; then extend the synthetic cases for feedback and recovery.

**Checkpoint 3 — question model extracted:** moved lookup tables, conditional visibility, active/report question lists, safety tagging, and progress counts into `src/app/core/model.js`. `app.js` now delegates those queries. Added the module to the explicit build manifest and a Node test for parent conditions, optional sections, progress, order, and duplicate IDs.

**Files:** src/app/core/model.js, src/app/core/app.js, src/app/build.json, tests/app/test_model.js, .github/workflows/app-component-checks.yml, docs/QUESTIONNAIRE_ARCHITECTURE.md, docs/CHANGELOG.md.
**Checks:** model behavior, app source manifest, UI catalogs, isolated screen tests, JS syntax, synthetic bundle assembly, and `git diff --check` PASS. Focused CI workflow 42252272675 passed after the test assertion correction; it did not execute the newly added model test in this checkpoint.
**Commit:** de529e8; checkpoint note: 077bbf7.
**Next action:** split feedback/recovery browser behavior into focused synthetic cases, then move validated recovery parsing out of the coordinator. Consolidate the new focused steps into the repository's existing app-component workflow; remove the redundant duplicate workflow file.

**Checkpoint 4 — recovery, flow, and layout boundaries:** extracted recovery validation/normalization to `src/app/core/recovery.js` and queue/back/next transitions to `src/app/core/answer-flow.js`, each with direct Node tests. Added a small synthetic browser layout check for mobile/desktop overflow, fixed Skip placement, and the question-feedback flag's accessible label. Removed the accidental duplicate workflow and extended the repository's original app-component workflow instead.

**Files:** src/app/core/recovery.js, src/app/core/answer-flow.js, src/app/core/app.js, src/app/build.json, tests/app/test_recovery.js, tests/app/test_answer_flow.js, tests/app/test_runtime_layout.py, .github/workflows/app-component-checks.yml, .github/workflows/questionnaire-checks.yml, docs/FILE_INDEX.md, docs/QUESTIONNAIRE_ARCHITECTURE.md, docs/CHANGELOG.md.
**Checks:** model, recovery, and answer-flow pure tests plus app/component checks PASS. First full workflow run 42253582892 failed because the source audit expected medication recovery validation in `app.js`; the audit now checks `recovery.js`.
**Commit:** b240504; source-audit correction: 873438f.
**Next action:** rerun the complete source/build/report/offline Chromium workflow after the audit correction.

**Checkpoint 5 — integration verified:** full workflow 42253832767 passed on GitHub, including source integrity, all 48 modules/712 IDs, report/build checks, and the offline Chromium journey. Focused workflow 42253582837 passed on the same code tree, including pure model/flow/recovery tests and synthetic answer, feedback, recovery, and layout browser checks. The local tree matches GitHub `develop`.

**Files:** docs/CHANGELOG.md.
**Checks:** full workflow 42253832767 PASS; focused workflow 42253582837 PASS; local/remote Git tree match PASS; working tree clean at checkpoint.
**Commit:** 873438f locally; GitHub `develop` 42f658c.
**Next action:** hands-on Android Chrome check and human review of LV interface wording, EN/RU drafts, and clinical content; those need a device and human reviewers.


**Checkpoint 6 — final coordinator boundary:** user-facing screens, question model, answer transitions, recovery validation, reports, and styles are separate. One clean boundary remains: move delegated click/change/input routing to `core/events.js` and test its callback dispatch with synthetic events. Keep UI and answer state in the coordinator.

**Files:** docs/CHANGELOG.md.
**Checks:** prior code verification remains at implementation commit 873438f; no application code changed in this checkpoint.
**Commit:** f2a59f7.
**Next action:** extract and test event delegation, then rerun both CI workflows.

**Checkpoint 7 — event routing extracted:** moved delegated click/change/input listeners into `src/app/core/events.js`; the coordinator supplies the existing behavior as callbacks. Added a synthetic dispatch test for radio taps, actions, section jumps, medicine controls, restore, locale, modules, answers, and text inputs. The module is in the explicit script order.

**Files:** src/app/core/events.js, src/app/core/app.js, src/app/build.json, tests/app/test_events.js, .github/workflows/app-component-checks.yml, docs/FILE_INDEX.md, docs/QUESTIONNAIRE_ARCHITECTURE.md, docs/CHANGELOG.md.
**Checks:** event-routing test, model/flow/recovery tests, screen renderers, manifest, catalogs, JS syntax, and `git diff --check` PASS locally. Focused workflow 42254680909 and full workflow 42254680875 PASS.
**Commit:** 972b3f1.
**Next action:** hands-on Android Chrome check and human review of LV interface wording, EN/RU drafts, and clinical content; those need a device and human reviewers.

**Checkpoint 8 — CI startup cost:** the focused app workflow now uses the runner's Google Chrome when present and downloads Playwright Chromium only as a fallback. GitHub run 42255642293 used preinstalled Chrome 156.0.8078.79 and passed all focused checks.

**Files:** .github/workflows/app-component-checks.yml, docs/CHANGELOG.md.
**Checks:** focused workflow 42255642293 PASS; its logs show `/usr/bin/google-chrome`, with no Playwright browser download step. Full integration remains covered by 42254680875.
**Commit:** 863ae0d; GitHub `develop` 71c8107.
**Next action:** hands-on Android Chrome check and human review of LV interface wording, EN/RU drafts, and clinical content; those need a device and human reviewers.

**Checkpoint 9 — plain-language progress controls:** starting implementation commit `e70d0f427c159a01d40ede1f35b778ca1a780cd0` on `develop`. Changed save/resume labels to plain language, removed `.json` from visible labels, and explained that closing the browser loses session answers unless a progress file is saved. Updated guide, privacy, backup, restore, and related prompts in LV/EN/RU. The recovery file schema and behavior are unchanged.

**Files:** src/app/i18n/ui.lv.json, src/app/i18n/ui.en.json, src/app/i18n/ui.ru.json, docs/CHANGELOG.md.
**Checks:** UI catalog consistency, offline app assembly, start/section screen rendering, question/medicine/feedback screen rendering, `git diff --check`, and focused GitHub app workflow 42258847072 PASS. Full questionnaire workflow was not needed for copy-only changes.
**Commit:** 731455a.
**Next action:** human review of EN/RU draft wording; the LV progress warning is now explicit and the save/resume labels are plain language.


## 2026-11-07 · REVIEW-PACKAGE-FORMAT · DONE

**Change:** set the reviewer guide format to a concise, visually checked PDF; kept editable Markdown private; updated the review-candidate listing to match the Drive folder. The reviewer folder contains the self-contained HTML and PDF only.

**Files:** `AGENTS.md`, `docs/CHANGELOG.md`, Google Drive review package.
**Verification:** PDF rendered and visually inspected; A4 one-page layout and extracted text checked. The review folder listing and project index were read back. No application tests run; this change does not affect runtime behavior.
**Commit:** `db72f2134c58383b46cf384be6b0bf0b31b62e27` (review-package standard in `AGENTS.md`).
**Next action:** use this standard for future reviewer-facing document updates.


## 2026-11-07 · LIVE-GITHUB-STATUS-CHECK · DONE

**Change:** added a rule to check the live GitHub branch before reporting ahead/behind counts or push status. Local tracking refs are used only after a successful fetch; API/CLI updates are confirmed by reading back the remote branch/files.

**Files:** `AGENTS.md`, `docs/CHANGELOG.md`.
**Checks:** GitHub readback confirmed the new instruction; documentation-only change, no application tests run.
**Commit:** `e55f4e52163e8bdc1afbf4811583c3c2e0244bad` (branch-status verification rule).
**Next action:** use the live-branch check before future push/status reports.



## 2026-11-07 · UI-CLARITY-PRIVACY-SUPPORT · DONE

**Starting commit:** `ef4f0fc947cbd4fe9a0b5f5c00cbc0361402456a` on GitHub `develop`.
**Change:** removed the guided picker and the non-clickable footer progress chips, retaining completion counts in section selection. Rewrote privacy/review-status text in LV/EN/RU, replaced stale version history with the Riga last-change timestamp and brief categories, clarified the 116123 six-digit number and anonymity/confidentiality limits, and fixed its dial link to `tel:116123`. Added a repository rule to keep future localized change timestamps current.

**Files:** `AGENTS.md`, `src/app/core/app.js`, `src/app/screens/start.js`, `src/app/screens/section-selector.js`, `src/app/styles/base.css`, `src/app/i18n/ui.lv.json`, `src/app/i18n/ui.en.json`, `src/app/i18n/ui.ru.json`, `tests/app/test_screens.js`, `tests/app/test_runtime_layout.py`, `tests/app/test_ui_catalogs.py`, `tests/full_bank/test_runtime.py`, `docs/CHANGELOG.md`.
**Local verification:** app manifest/catalog/screen/model/flow/recovery/event tests, source-integrity audit (48 modules/712 IDs), module titles/conditions, full-bank layout/report checks, full offline HTML build, JS/Python syntax, and `git diff --check` PASS. Built HTML SHA-256: `46417a3a2a6d4972cf30e6e26201597d1ea7ef4e14c39baeb39ba73a0b80b6e5`.
**Browser verification:** local Playwright unavailable. GitHub focused app workflow `42341713103` PASS on selector-test fix `3449505000586957ea8e7dbabc48ab7d8f9866cb`; full questionnaire workflow `42341599375` PASS on `1afb5328c3b1207c9e2065537ba92399e36b6738`, including the full offline 712-question Chromium journey. Initial runs `42341394945` and `42341394954` failed only on newly added brittle assertions; both were corrected and rerun successfully.
**Implementation commits:** `40637a3188905c6e139c9e698d040c4e3304ff1e`, `1afb5328c3b1207c9e2065537ba92399e36b6738`, `3449505000586957ea8e7dbabc48ab7d8f9866cb`.
**Limitations:** Android-device use and human EN/RU, interface, and clinical review remain outstanding. The wording does not promise absolute anonymity; call history or a phone bill may show the call.
**Next action:** compile the next review build from GitHub `develop`; do not use the old Drive HTML. Human and Android checks remain separate review steps.


## 2026-11-07 · GOOGLE-DRIVE-REVIEW-CANDIDATE-REFRESH · DONE

**Starting GitHub commit:** `805e0873ec97881bba2cb042a9b01ff75926be8e` on `develop`.
**Change:** rebuilt the full offline HTML from `develop` application sources at `40637a3188905c6e139c9e698d040c4e3304ff1e`, then replaced the current HTML and Latvian PDF in the existing Drive review folder in place. Their Drive IDs and existing links were preserved. The folder contains the two current review files only; no historical v16 reference was changed.

**Files in Drive:** `187_Questionnaire_FULL_712Q_v0.2.0_REVIEW_BUILD.html` (SHA-256 `46417a3a2a6d4972cf30e6e26201597d1ea7ef4e14c39baeb39ba73a0b80b6e5`) and `188_README_LV_v0.2.0_REVIEW_BUILD.pdf` (SHA-256 `f4639c80d9ea36e37632638913b29f6618f9808891a5f522dc86501725947e21`). The PDF was text-checked, confirmed as one A4 page, and visually inspected after rendering.
**Git files:** `project-manifest.json`, `docs/FILE_INDEX.md`, `docs/CHANGELOG.md`. The manifest now records the current candidate checksums and distinguishes it from a public release; the file index no longer describes the folder as v16-only.
**Local checks:** `tools/verify_project_index.py` (79/79 originals, 48 modules, 712 IDs), app build manifest, UI catalogs, and `git diff --check` PASS. Drive readback confirmed the updated HTML/PDF names and modification dates.
**Git commit:** `f0260ff752a2d6182a5e2fa28bfb10042009936d` updates the manifest and file index. The following changelog checkpoint records the workflow result.
**GitHub verification:** full questionnaire workflow `42344703148` PASS on `f0260ff752a2d6182a5e2fa28bfb10042009936d`, including source integrity, complete build, and offline Chromium journey. Drive readback confirmed both files and current content.
**Next action:** use this Drive pair for professional technical review when ready; Android-device testing and human review of translations/clinical content remain outstanding.


## 2026-11-07 · GENTLE-ENTRY-AND-SECTION-CONSOLIDATION · DONE

**Starting commit:** `8728cdced85f402b89ac733f1bb44816af540835` on GitHub `develop`.
**Tasks:** 1) make Start lead directly to section choice, with one-tap “select all and continue” and a separate selected-sections continue action; 2) consolidate the 48 immutable source modules into 15 user-facing sections containing 36–70 source questions each; 3) use concise completion-only results; 4) revise friendly introduction, privacy, backup and soft-language explanations in LV/EN/RU; 5) add and follow a reusable language-style guide for future text edits; 6) rebuild and replace the current Drive HTML/PDF after Git changes and full verification. **All tasks complete.**
**Source audit:** the screenshot’s `0/1` is a count of currently visible questions before conditional follow-ups; it does not mean the source module has one question. The source bank has 48 modules and 712 questions, with several modules genuinely under 30. The final balanced grouping changes navigation only; frozen question wording, IDs, answer codes, conditions and periods remain untouched.
**Checkpoint 1 — implemented:** Start now opens section choice; the picker offers select-all-and-continue and continue-with-selected. The 48 source modules are grouped into 15 user-facing sections (36–70 questions each). Results show completed answers only. Localized copy covers gentle tone, backup-loss risk, file privacy, and formal address. Added `docs/LANGUAGE_STYLE_GUIDE.md`; recovery maps older selected-module files to the new groups.
**Files changed:** `src/app/`, `src/questionnaire/layout.json`, `src/questionnaire/presentation.json`, `src/app/i18n/`, `tools/build_questionnaire.py`, focused tests, `AGENTS.md`, `README.md`, manifest, architecture and file index.
**Verification:** source integrity (79 original files, 48 module hashes, 712 IDs/orders), source fidelity, user-section counts/order, report semantics, UI catalogs, isolated runtime rules and the full HTML build passed. GitHub App Component Checks `42350377334` passed; Offline Questionnaire Checks `42350796659` passed, including the full offline Chromium journey. Local browser execution was unavailable. The initial full-browser run exposed a test that assumed a merged section began at `M06_01`; the test now navigates within the section to that question.
**GitHub commits:** implementation `2339b3f`; grouped-section browser-test correction `1f87aba`; reviewer-guide source and index `96e69e1`, then wording refinement `cc04a9e`. All on `develop`.
**Drive refresh:** replaced HTML and PDF in place; existing file IDs preserved. HTML SHA-256 `b18e843582f5d5de46c554decf939ad36d9b91c6289c2adcd0efd0ee33adf202`; PDF SHA-256 `842ca0d54432c9fdbab933070992335c269c75f44b9cc5245fc3b5ead4bda136`. Readback bytes and hashes match the local artifacts. Versioned PDF source: `docs/review/README_LV_v0.2.0.md`.
**Remaining limitations:** actual Android-device testing and human review of language and clinical content remain outstanding. This is technical readiness for professional review, not clinical validation.
**Next action:** use this current Drive candidate for professional technical review when ready.
