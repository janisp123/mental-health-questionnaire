Warning: truncated output (original token count: 8568)
Total output lines: 222

Warning: truncated output (original token count: 8149)
Total output lines: 212

# Development changelog — mental-health-questionnaire

**Active task log:** This file on GitHub `develop`, effective 2026-11-05.
**Development edits:** GitHub only, after the relevant sources have been imported and verified.
**Google Drive:** distribution of Latvian public files only. Existing Drive archives are read-only source references following the completed migration; do not update its old changelog for routine work.

## 2026-11-06 · UX-SUPPORT-REPORT-REDESIGN · IN_PROGRESS

Scope: the existing 60-question pilot. Preserve original wording/codes and all pilot recovery records. Make all groups optional, redistribute opening items by original theme with personal details last, single-tap single-choice navigation, fixed Skip/Back, persistent gentle support, independent readable AI export, ascending answer-level report presentation priorities. Include previously requested bottom guide/version notes. Verify helpline facts, all three languages, and structural/fidelity/browser regressions. No release or frozen-source edits.

Stages: (1) inspect and pin design/source mappings plus failing acceptance tests; (2) navigation and recovery; (3) support and reports; (4) mobile-width offline regression, documents and checkpoint. Current: inspected AGENTS, changelog, manifest, file index and architecture. Next: fetch current sources and establish the test baseline.

## 2026-11-05 · SOURCE-FIDELITY-AND-SECTION-21 · TASK_DONE

Plan: verify active modules against frozen v16 by ID and exact codes, demonstrate rejection of swapped labels, inspect section 21 dependencies, import its three existing locales, verify in offline Chromium and checkpoint the artifact. Checkpoint: 41 active questions passed exact v16 logic and LV/EN/RU text comparisons locally. Deliberately swapping English labels B/C at M02_01 failed at the expected ID, locale and field. The gate runs in pilot CI. Section 21 has 19 questions (orders 387–405), no opening overlap or condition parents, and an incompatible A/E pair at M21_06 requiring generic runtime enforcement. Source gate committed at c7e0f37804c93013fb44bff9e776b205012e6594.

Imported real section 21 directly from v16 in its three languages. All 60 questions passed the structural and independent fidelity checks locally. Runtime now rejects incompatible selections on both save and restore. M21_15 retains the v16 immediate-help trigger B. Browser test exercises all 19 items, reports and recovery. Verified commit 5c851b0d1d7a273dabc7ed3563db68c42a449cd2 in [passing run 42067275015](https://github.com/janisp123/mental-health-questionnaire/actions/runs/42067275015). All three browser suites passed. The workflow uploaded artifact 13433203221. Built HTML SHA256 95019a68bda97bdc1f15d9d8e6dcb5d0f67bf6e76e6a24847d253369fbe24055 matches the local build. Next device check: open the 60-question pilot in Android Chrome and test downloading/restoring a backup.

## 2026-11-05 · PILOT-GENERIC-MODULE-AUDIT · TASK_DONE

**Goal:** audit the existing pilot against LV v16; remove module-specific engine/build assumptions; verify translation independence and additional-module registration; document remaining parity gaps and active source pointers.
**Plan:** inspect sources and successful CI evidence; checkpoint findings; make targeted generic changes; run structural and browser regressions; update architecture/index/manifest and verified status. Preserve original IDs, codes, conditions and recovery semantics. No release, Drive edits or main changes.
**Final verified checkpoint:** All pilot checks passed at b7a627b9e86ce97cf079fe272e5de59efe5b22b6 in [run 42064471277](https://github.com/janisp123/mental-health-questionnaire/actions/runs/42064471277). The third-module fixture, English-only edit, cross-build backup, safety review, conditional status, real mood multi-select, print PDF page count and copy payload all passed. The distributable test HTML is the workflow artifact. The production registry still enables only opening and section 02.

**Broader pilot status: PARTIAL.** See PILOT_ARCHITECTURE.md for scope. Next: check the artifact on Android Chrome (local opening, automatic recovery download, restore, clipboard and print), compare legacy v16 recovery and clinician-report requirements, then complete professional wording checks before any release. Full v16 backups cannot be loaded into this two-section pilot. EN/RU remain drafts.

**At registration:** the implementation had not yet been audited. See verified checkpoints below.
**Audit checkpoint:** Verified CI run 42057715895 passed on 231f537 (browser smoke + structure). Found fixed section counts and section-specific selector, reports and restore. LV v16 skip-section continues to the next eligible section. Pilot previously finished immediately.

**Implementation checkpoint:** Registry drives selection, progress, report section lines, skip continuation and recovery. Module locale files own their titles. Existing structural checks and JS syntax pass locally. Verified registry implementation on develop at 9ddc7d87681e4313ca7a497e685e65ad2a179b78. Added a disposable third-module + locale-edit Chromium test with cumulative tenth-save check and cross-build restore. CI run 42062287500 passed at f996d9ce739125d81bdf297f0311144ccdbb8c59, including the new browser regression.

**Next batch:** match opening safety prompts, flag incomplete safety coverage, validate restored choices, preserve status precedence, and print the full report. Structural checks and JavaScript syntax pass. Verified A4 PDF and opening safety behavior at b06f42271a2fd7905dbb6d08f69b6f1aa8f58eb7 in run 42062504929.

**Next batch:** verify optional topic guidance, section jumping and omitted/hidden report statuses. Manifest and file index now point to active pilot sources. Remaining parity and device limitations are listed in docs/PILOT_ARCHITECTURE.md. Run 42062907339 at 0ac0dd3 passed the smoke journey but the expanded test found two valid section controls and stopped on an ambiguous selector. Target the toolbar control and verify again.

**Safety review:** traverse all eleven opening safety items even when previously answered, restore the review queue from a pilot backup, and show saved timestamps on flagged answers. Require confirmation before replacing a session containing saved answers. CI run 42063169851 passed at d2456a4a2394cb9ae57cc1f2cd9b75c08398422d. Confirmed the toolbar fix, safety review sequence, third-module registration, guided selection, conditional parent edit, section jump, omitted/hidden exports and restoration.

**Source comparison:** verified all 41 IDs and original order, LV/EN/RU prompt/choice/time/help text, multiple-choice/exclusive/incompatible settings, conditions, type, maximum choices and answer statuses against the frozen source modules. Zero differences in those fields.

**Final browser batch:** exercise real section 02 multiple-choice combinations, exclusive options, save/back/edit, and doctor-copy payload at phone width and offline. Mobile-width offline run 42063375002 passed at a3e4582042aa670e16bbac5c312f6ef4e62ad57e. Native Android and legacy v16 migration remain separate acceptance items.

**Recovery guard:** reject backups referencing unavailable selected sections before replacing the current answers. If a backup points beyond an incomplete required opening, resume the opening first. A Chromium regression checks that a rejected backup preserves the current session.

**Clinician summary:** include opening visit context and priorities, each safety answer and its original saved time, and uncertain/refused counts. Test the representative completed report for one A4 page. Long responses may continue onto further pages to retain their text. Recovery guard passed on f23aafc in run 42063533966.

**CI runtime:** use installed Chrome when the runner provides it and fall back to installing Playwright Chromium if absent. This avoids downloading a second browser on supported runners. Repeat the full PDF and offline browser suites.

## 2026-11-05 · PROGRESS-UPDATES-RULE · TASK_DONE

Added `AGENTS.md` to require brief user-visible updates approximately every minute during active multi-step tasks (more frequently when practical), actual progress details, immediate blocker notices, and durable changelog checkpoints after verified batches. This is a workflow instruction rather than a guaranteed timer or background process. The active two-section pilot remains `IN_PROGRESS`.

## 2026-11-05 · MODULAR-THREE-LANGUAGE-TWO-SECTION-PILOT · IN_PROGRESS

**Goal:** a self-contained offline three-language HTML prototype with the authentic original 20-question required opening sequence and one additionally selectable section (02, depression). Preserve user-visible button workflows and build the application from independent question logic + LV/EN/RU text per section, so a one-language one-section edit never touches other language files or module logic.

**Scope:** new `src/pilot/` architecture, localized text and core files, `tools/build_pilot.py`, `tests/pilot/`, `dist/` prototype, `docs/PILOT_ARCHITECTURE.md`, version pointers, changelog. Current `src/modules/182_*` and `reference/baseline/` remain immutable. Do NOT edit distribution Drive or GitHub main. Draft language status retained.

**Workflow:** checkpoint each independently verifiable part; extract original 20 opening questions by original global order 0-19 from six source modules and section 02 by original section number; split logic/text, ensure IDs/codes/branch conditions remain stable; implement shared UI and all existing controls, localized LV/EN/RU interface, offline output; run structural and functionality checks without asserting unperformed clinical review. Add an extensible module registry where more sections can be activated without changing the engine.

**At registration:** source migration verified, before the pilot was built. See PILOT-GENERIC-MODULE-AUDIT above for current progress.
**Next:** create independent per-module per-language source and registry; verify ID and answer-code equality.

## 2026-11-05 · GITHUB-FULL-SOURCE-IMPORT-AND-LV-DISTRIBUTION-NAME · TASK_DONE

**Goal:** import all relevant Google Drive project source/reference files to GitHub `develop`, organize under clearly separated source, test, document, translation and immutable reference/history folders, establish a stable CURRENT file/version index so future work needs no Drive reads; rename the public Latvian Google Drive distribution folder for Latvian-language outreach.

**Boundaries:** preserve existing Drive files; rename the distribution FOLDER only. Do not modify GitHub `main`, publish unreviewed EN/RU, claim complete source migration without 48/48 files and SHA256 readback, or accidentally publish real user answers or private communication. Existing archived Drive source is read-only pending verified Git migration.

**Steps:** (1) inventory Git and ZIP/Drive sources; (2) rename Drive folder and verify; (3) attempt approved source import on `develop`, verify full source list/checksums; (4) create or update manifest/index with active versions, archived versions and exact Git paths; (5) document any blocked operation and a reproducible one-time manual import path; (6) read back GitHub changes, close `TASK_DONE` only if fully satisfied, otherwise `BLOCKED`.

**Historical obstacle (resolved):** previous Google Drive -> public GitHub imports failed with connector safety checks; GitHub held 0/48 modules at that point. Recovery ZIP `190_GITHUB_MIGRATION_READY_MANUAL_UPLOAD.zip` exists locally, 79 Drive-origin reference/source files. Current original documents and completed Latvian HTML are on Drive; development work log is here.

**Verified checkpoint:** Google Drive distribution folder renamed and read back (2 Latvian files). All 79 of 79 Drive-origin development files imported on GitHub `develop` at commit `24d25c992cd866daf0589e16b4c4a1a9b8b7d63f`. Remote and local Git file hash inventories match, with 48 modules present. This validates transfer integrity only, not any release. **Final verification:** 79/79 source/reference files committed on `develop`, with matching local and remote Git file hashes and 48/48 original modules, v16 712-question baseline. Established `project-manifest.json` (79 paths, exact Git SHA1 and byte sizes, version/status roles), `docs/FILE_INDEX.md` (human navigation), and `tools/verify_project_index.py` (local checkout checker). Updated and read back README, migration plan/status, import checklist and integrity script. The verification script was saved and read back; it has not been executed against a local fresh Git checkout in this session. Git `main` untouched. Drive public folder renamed in Latvian, unchanged two LV distribution files. Source transfer task complete; all EN/RU language review, new unified app build, release CI and browser/clinical tests remain separate pending tasks.

## 2026-11-05 · GITHUB-CHANGELOG-HANDOFF · TASK_DONE

**Goal:** switch ongoing task tracking to GitHub, without pretending that the questionnaire source migration is complete.

**Scope:** `docs/CHANGELOG.md`, `docs/MIGRATION_STATUS.md`, `docs/MIGRATION_PLAN.md`, `README.md` (only repository docs). Do not modify published `main`, Google Drive questionnaire or questionnaires.

**Steps:**
1. Create this active changelog with a verified checkpoint.
2. Update conflicting repository instructions and migration status.
3. Read back from GitHub and mark `TASK_DONE` only if all intended documentation is verified.

**At the time of this historical entry:** GitHub contained repository scaffolding but **0/48 questionnaire modules**. Direct transfer from Drive to GitHub was blocked. Existing ZIP import package is ready for manual upload; GitHub source is not yet authoritative.
**Next:** revise repository instructions, verify, then close task.

## Historical pending list from before the verified import

- **GITHUB-SOURCE-MIGRATION — subsequently completed (24d25c9):** 48/48 multilingual source modules, HTML reference baselines, translation catalogs, QA tools and archival materials remain on Drive. The verified ZIP package `190_GITHUB_MIGRATION_READY_MANUAL_UPLOAD.zip` must be extracted and manually uploaded on `develop`, then checked against hashes and counts. Do not claim GitHub holds code until file readback.
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
5. `develop` is the work branch; `main…568 tokens truncated… structural/source-fidelity/layout/report tests and JS syntax; offline Chromium UX journey (single/multi/text, physical double click, back/edit, 320/390/540 px repeated Skip, every-ten recovery, legacy/invalid restore, support accessibility, clipboard, HTML/PDF print, all language structures); module/locale independence and real section 21 journeys passed. Source wording and code mappings are compared to frozen originals. Inspected mobile screenshot and extracted printed sample text.
- An alternate Playwright download succeeded: local browser is Chromium Headless Shell 141 on Linux. This does NOT verify native Android Chrome or human translation quality.
- Next: full develop CI (including all 79 imported-file hashes/712-question inventory), final browser regressions and recorded exact commit/run. TASK_DONE not yet claimed.
- Stage 2 implementation commit: `ee84b5e0f25e2ce52cf3154daa3aaf52b837b19d`; develop head readback confirmed. Local final browser regressions all passed. Built HTML SHA256: `4dca1ed7b0b8d50dfaaad098dd8e2a2e048d2f322d7f94ae7e815282035c737c`. Full CI status pending.

### UX-SUPPORT-REPORT-REDESIGN — final verification update (IN_PROGRESS)
- Final review separated ordinary support from emergency guidance: 116 123 appears for supportive prompts; 112 appears only for immediate-danger triggers, while remaining available in the expanded support details. This preserves 112 without suggesting every distressed response means emergency danger.
- Reran all three local Chromium suites after the change: general browser UX, registry/condition independence, real section 21. All passed. Rebuilt artifact SHA256: `9247828dd55f100c12c449154ee77686397b280139fc2eb28c297c2230c0b0a0`. Full develop CI for this last adjustment pending.
- Native Android Chrome remains UNVERIFIED. Human translation and professional review of source wording and provisional report priorities remain outstanding.

### UX-SUPPORT-REPORT-REDESIGN — TASK_DONE

**Pilot v0.2 implementation complete on `develop`.** The current test pilot contains 60 original questions; the larger 712-question bank is not implemented by this change. No frozen original question data, public `main`, or Google Drive files were changed.

**Verified:**
- Full GitHub Actions run `42162346126` passed at implementation checkpoint `ee84b5e0f25e2ce52cf3154daa3aaf52b837b19d`: all 79 imported file hashes, 48 sections/712 questions, structural/source fidelity, layout/report tests, offline Chromium user journeys, independence and section 21 report journey; prototype artifact built and uploaded as an expiring test artifact.
- The final safety-card adjustment and regression expectation are at `60cc44f429697bc3711a9c80c85ac1504e40b40b`. After that adjustment, all three local Chromium suites passed with Chromium Headless Shell 141: single/multi/text, double taps, Skip/back, 116123 versus 112 display, recovery migration, condition handling, clipboard/print, independence, and frozen section 21 report mapping. Structural, source-fidelity, layout and report tests also passed; final built HTML SHA256 `9247828dd55f100c12c449154ee77686397b280139fc2eb28c297c2230c0b0a0`.
- The final small adjustment was not observed in a new Actions run. Its browser regressions passed locally; do not describe the final code SHA as having a separate green CI run.

**Still unverified:** native Android Chrome touch/file-picker/clipboard/printing; human review of EN/RU and the new interface/report translations; psychiatrist review of provisional question wording and report-priority rules; all imported modules outside the 60-question pilot. This build is ready for another desktop/mobile UX test, not a clinical validation or public release.


## 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · IN_PROGRESS

**Starting commit:** `fd61b0504c8396d5f53fdb9aba5c44dcdefa5414` on `develop`. Current implementation is pilot v0.2: 60 active questions. The frozen source bank has 48 modules/712 questions. Do not call the full questionnaire complete until all modules, behavior and exports are checked.

**Critical design decisions:** Remove the pilot's AI/coded export and presentation weights; use a small, explicit, answer-code allowlist to bold only clearly serious reported answers. Keep one compact clinician report. Green-flag feedback is separate from medical answers, optional, locally backed up, and exports no medical responses or personal details. Feedback Save & Continue preserves an existing answer; if no answer exists it records a skip. Backward compatibility means new code continues to restore pilot-v1 files; old code is not assumed to preserve new feedback fields. Add source modules by stable batches, not one large import, and preserve exact original text/IDs/codes/conditions.

**Numbered checklist**
1. [DONE] Remove AI/coded-answer UI/export and weighting; retain one clinician report with explicit bold-answer mappings.
2. [DONE] Add per-question project-feedback flag and non-destructive Save & Continue; persist in new recovery fields and restore old pilot-v1 backups.
3. [DONE] Add isolated project-feedback copy/export and clinician-report ordering/privacy checks.
4. [DONE] Audit the full 48-module schema against engine capabilities (types, conditions, status, choice constraints, language coverage); register gaps before integration.
5. [IN_PROGRESS] Integrate the original 712 questions in small tested batches; update fidelity/navigation tests after each batch.
6. [TODO] Build the complete offline HTML; update manifest, architecture/index and minimal user-facing documentation after functionality works.
7. [TODO] Run full source-integrity, browser/export/privacy/offline regressions; record unverified Android and human review.

**Next action:** checklist item 5 — add support for the one full-bank question type the pilot cannot represent: `medicineList`. Preserve the frozen 13-field repeating record and discussion note, and cover save, restore and doctor report before registering any new module. No frozen source, `main`, or Drive release edits.


### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 1

**Checklist:** 1 [DONE] · 2 [IN_PROGRESS] · 3–7 [TODO].

**Task 1 — remove AI export/weights; simplify clinician report**
- **Commit:** `6ec21edfa7daec196ba8f601a5c4b9130bce6f21` on `develop` (read back as current head at commit time).
- **Files:** `src/pilot/core/app.js`, `src/pilot/core/styles.css`, `src/pilot/reports/reports.js`, `src/pilot/reports/presentation.json`, `src/pilot/i18n/ui.{lv,en,ru}.json`, `tools/build_pilot.py`, `tests/pilot/test_reports.js`, `tests/pilot/test_browser.py`, `tests/pilot/test_independence.py`, `tests/pilot/test_section21.py`.
- **Completed:** removed AI/coded, all-results TXT and decoding-key UI/routes; removed presentation-weight tables and sort calculations; retained a single compact clinician report. Added a 13-question answer-code allowlist that bolds only explicit selected answers. The report keeps language/topic order, original selected answer wording and periods. No IDs, scores or category totals are printed.
- **Checks:** `node tests/pilot/test_reports.js` PASS; `python tests/pilot/test_build.py` PASS; `python tests/pilot/test_source_fidelity.py` PASS for the seven source modules present in this local worktree; `python tests/pilot/test_layout.py` PASS; JS syntax PASS; three offline Chromium browser suites (general UX, independence/conditions, real section 21) PASS; artifact built, SHA256 `982712c11f7964e2f117f9bebb177cdd304370ab9fbd7f6eb94f658e196f7f0d`. This does not verify the absent 41 original modules locally or native Android.
- **Remaining:** feedback form/recovery/report isolation; audit and integration of the remaining full question bank; full-project CI hash verification.
- **Next action:** task 2 — implement the green flag/edit/remove feedback form and a separate optional feedback object in recovery. Test that Save & Continue never overwrites a medical answer and skips only when no answer exists.

At checkpoint 1, checklist item 2 became [IN_PROGRESS]. See the following checkpoint for its completion.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 2

**Checklist:** 1 [IN_PROGRESS—metadata follow-up] · 2 [DONE] · 3–7 [TODO].

**Task 2 — per-question project feedback**
- **Implementation commit:** `742f93cb61a4248b86c05ad67a05140fd10f336c` on `develop`.
- **Files:** `src/pilot/core/app.js`, `src/pilot/core/styles.css`, `src/pilot/i18n/ui.{lv,en,ru}.json`, `tests/pilot/test_feedback.py`.
- **Completed:** added a compact green flag beside each question; selectable reasons include question wording, grammar/translation, dynamically generated answer choices, and other, with an optional 500-character comment. Existing flags reopen for editing and have an explicit remove action. Save & Continue records a skipped status only when the question has no existing record; any existing medical answer or skip record is preserved. New recovery files carry an optional `feedback` object under the existing pilot-v1 schema; old files without it still restore. Feedback records are validated before replacing the current session.
- **Checks:** new test first failed because the flag was absent, then passed after implementation. Feedback browser test passed across LV/EN/RU labels, edit/remove, skip/preserve, old recovery restore and invalid-record rejection. Existing report, builder, layout, JS syntax, pilot source fidelity, general browser, independence and section 21 checks passed. `tools/verify_project_index.py` confirmed all 79 imported source files and the full 48-module/712-question inventory. Desktop offline Chromium only; native Android remains unverified.
- **Remaining:** question feedback is not yet included in a separate project-feedback export or the clinician report. Two unused `textWeight: 0` entries remain in presentation metadata; they do not drive the current report, but must be removed and rejected by the builder before checklist item 1 is closed.
- **Exact next action:** remove the two unused `textWeight` entries, make the builder reject any weight-named presentation key, add a regression test, run the relevant checks, commit and append the exact checkpoint. Then proceed to checklist item 3.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 3

**Checklist:** 1 [DONE] · 2 [DONE] · 3 [IN_PROGRESS] · 4–7 [TODO].

**Task 1 follow-up — remove all weighting metadata**
- **Implementation commit:** `a470eef5fcb412ccda1c2b0064737297239ab871` on `develop`.
- **Files:** `src/pilot/reports/presentation.json`, `tools/build_pilot.py`, `tests/pilot/test_build.py`, `tests/pilot/test_reports.js`.
- **Completed:** removed two unused `textWeight: 0` keys. The builder now rejects any recursively nested presentation key containing “weight”; report tests reject such keys in generated data.
- **Checks:** the new guard assertion failed before implementation, then passed. Builder, report, layout, three-language pilot source fidelity, JS syntax, feedback browser, general browser, locale/condition independence, section 21, and full project index/hash checks all passed. The last integrity check confirms all 79 imported originals, 48 modules and 712 IDs/orders.
- **Remaining:** none for checklist item 1; clinical review and native Android testing remain separate overall limitations.
- **Exact next action:** checklist item 3 — add the isolated project-feedback export and place submitted question feedback first in the clinician report. Verify the feedback export contains no medical answers or personal details, works with zero answers, and clinician content remains ordinary-to-sensitive.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 4

**Checklist:** 1 [DONE] · 2 [DONE] · 3 [DONE] · 4 [IN_PROGRESS] · 5–7 [TODO].

**Task 3 — feedback exports and report ordering**
- **Implementation commit:** `5cec85f3024d1fe04029dcd68cc29924adb5fa50` on `develop`.
- **Files:** `src/pilot/core/app.js`, `src/pilot/reports/reports.js`, `src/pilot/reports/presentation.json`, `src/pilot/i18n/ui.{lv,en,ru}.json`, `tools/build_pilot.py`, `tests/pilot/test_build.py`, `tests/pilot/test_reports.js`, `tests/pilot/test_feedback.py`.
- **Completed:** added a separate manual “Copy feedback for the project” action that works from the results screen with no medical responses. Its payload is built only from question feedback, original wording/time, question ID, reason, optional comment, reported language/version, current questionnaire version and project contact. The email `janis.paegle.email@gmail.com` matches the address recorded in `src/i18n/working/Temporary translation workspace — questionnaire text only.csv`. The feedback form warns users not to include identifying or answer information. Clinician reports show question feedback before compact medical answers; medical entries keep the existing ordinary-to-sensitive topic order and explicit bold-answer allowlist.
- **Checks:** report-format checks passed for three locales, dynamic answer-choice reasons, feedback language/version, contact email, empty-feedback output and report ordering. Offline Chromium confirmed export works with no medical answers, excludes a synthetic personal-data sentinel from project feedback even when it is stored in a medical response, and places feedback before ordinary-to-sensitive medical answers. Builder, source/layout, all three pilot browser suites, and full 79-file/48-module/712-question integrity checks passed.
- **Remaining:** the pilot still runs only 60 questions; full source-bank integrity is not full runtime integration. Native Android Chrome and clinical/professional review are unverified.
- **Exact next action:** audit each source module's question/condition/status/choice schema and the engine's supported behaviors before integrating any new modules.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 5

**Checklist:** 1 [DONE] · 2 [DONE] · 3 [DONE] · 4 [DONE] · 5 [IN_PROGRESS] · 6–7 [TODO].

**Task 4 — all-source schema and capability audit**
- **Audit commit:** `cf01df3cc16869fea1955918b01bbc3bc37e08f3` on `develop`; added `tests/pilot/test_full_bank_audit.py` to CI.
- **Findings:** the source is structurally consistent: 48 modules, 712 unique IDs/orders, locale choice-code parity, valid conditions with earlier parents, known answer statuses, and valid multi-choice/exclusive/incompatible constraints. It contains 709 ordinary choice items, 2 `shortText` items and one `medicineList` item (`M14_02`). Five conditional items have multi-select parents; there are no cross-section conditional parents. The full-project hash verifier confirms all 79 imported originals.
- **Important source detail:** one source entry (`M32_02`) is stored under module 33 with `section: 33`; IDs must be preserved as supplied, without deriving them from file paths or renumbering. The audit deliberately checks uniqueness, not ID-prefix-to-file equality.
- **Engine gap:** the existing pilot supports choice and short text, but not the frozen medicine list's 13 fields per record, repeated records, benefit status, or optional discussion note. The frozen v16 HTML defines its Latvian labels; EN/RU source help is draft and the structured labels need careful locale-source review. The original files remain unchanged.
- **Checks:** `python tests/pilot/test_full_bank_audit.py` PASS; `python tools/verify_project_index.py` PASS (79 source hashes, 48 modules, 712 IDs/orders). These are structural/source checks, not translation, clinical or browser verification.
- **Exact next action:** implement and test `medicineList` rendering, save/restore validation and clinician-report output while the current 60-question registry stays unchanged. Then integrate the full bank directly from the immutable 48 source modules in small batches, avoiding duplicate copies of the 20 questions already repositioned in the pilot.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 6

**Task 5a — prepare minimal medicine-list locale data and builder support.**
- **Starting commit:** `1ba5bb0b1fd73aa0f5f8170d1ff269fde3ce8f46` on `develop`.
- **Implementation commit:** `c27f82bdbe1567d266700ce4f4f309c0d7973013` on `develop` (remote branch readback and local reset confirmed).
- **Files:** `src/pilot/i18n/medicine.{lv,en,ru}.json`, `tools/build_pilot.py`, `tests/pilot/test_build.py`, this changelog.
- **Completed:** the bundle now includes minimal medication-list fields, statuses, benefit choices and related form/report labels. Test comparisons verify these match the corresponding frozen v16 LV/EN/RU text exactly. The 60-question registry is unchanged.
- **Checks:** `python3 tests/pilot/test_build.py` PASS (60 questions, 3 languages, offline/no imports); `python3 tests/pilot/test_full_bank_audit.py` PASS (48 modules/712 source questions; also reports medicineList as the remaining engine gap); `python3 tools/verify_project_index.py` PASS (79 original hashes); `git diff --check` and all three locale JSON parses PASS. These do not verify language quality or interactive medicine form behavior.
- **Remaining:** `medicineList` rendering and save/restore/report behavior remain to be implemented. Full question-bank integration has not begun; the pilot still runs only 60 questions.
- **Next action:** Task 5b — implement medicine-list editing and validation, compatible backup restore, and compact clinician-report serialization with focused tests; keep the active registry unchanged until this passes.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 7

**Task 5b — `medicineList` engine support.**
- **Starting commit:** `c27f82bdbe1567d266700ce4f4f309c0d7973013` on `develop`.
- **Implementation commit:** `a1bce9901ff42ec684dd3d4c1a1cef3ca6a3fc73` on `develop` (remote branch readback and local reset confirmed).
- **Files:** `.github/workflows/pilot-checks.yml`, `src/pilot/core/app.js`, `src/pilot/i18n/medicine.{lv,en,ru}.json`, `src/pilot/reports/reports.js`, `tests/pilot/test_build.py`, `tests/pilot/test_full_bank_audit.py`, new `tests/pilot/test_medicine.py`, new `tests/pilot/test_medicine_report.js`, this changelog.
- **Completed:** added repeatable medication records with 13 source-labeled fields, current/past/unknown status, optional benefit and discussion; manual save rejects an empty form, Skip remains separate, and the clinician report prints only entered details in compact localized text. Recovery validates record keys, enums, sizes and emptiness atomically. Original pilot-v1 choice/text/skip and feedback records continue restoring. The audit now identifies medicineList as supported while explicitly noting only 60 questions are active.
- **Checks:** test-first report and browser tests failed before their respective support was added. Then `python3 tests/pilot/test_build.py`, `python3 tests/pilot/test_source_fidelity.py`, `python3 tests/pilot/test_layout.py`, `python3 tests/pilot/test_full_bank_audit.py`, `python3 tools/verify_project_index.py`, JavaScript syntax, `node tests/pilot/test_reports.js`, `node tests/pilot/test_medicine_report.js` and offline Chromium `test_medicine.py`, `test_feedback.py`, `test_browser.py`, `test_independence.py`, `test_section21.py` all passed. Browser tests were run serially on desktop Chromium. The source index still verifies 79 originals / 48 modules / 712 IDs; this is not full runtime integration.
- **Regression found and fixed:** a stricter restore check initially rejected ordinary original answers because their choice type is implicit; validation now excludes only text and medicine records. Existing recovery and browser suites pass.
- **Unverified/pending:** GitHub Actions for this commit, native Android Chrome, EN/RU human-language review, professional review, and full 712-question browser behavior.
- **Next action:** Task 5c — design a read-only adapter that maps the immutable source-bank question schema into the existing engine bundle and prove exact ID/code/text/condition fidelity on the first small module batch without changing the active 60-question pilot.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 8

**Task 5c — direct source-bank adapter, first batch.**
- **Starting commit:** `a1bce9901ff42ec684dd3d4c1a1cef3ca6a3fc73` on `develop`.
- **Technical choice:** adapt the immutable `src/modules/182_MODULE_XX_LV_EN_RU_v16.json` data at build time. Do not copy the 712 question records into a second active source tree. Preserve the existing pilot builder/mode for current regression coverage while testing the adapter separately.
- **Implementation commit:** `e87760abe9971c916678d34b0eeb37fafc727d1c` on `develop` (remote branch readback confirmed).
- **Files:** `tools/build_pilot.py`, `tests/pilot/test_source_adapter.py`, `.github/workflows/pilot-checks.yml`, this changelog.
- **Completed:** added a small pure adapter for one source entry. It maps the original ID/order/section/profile/type, conditions, choices/codes, statuses, limits and all three localized titles/time periods/choices/help into the existing engine shape. It does not duplicate or modify the source bank, activate modules or alter the current pilot.
- **Checks:** test-first adapter test failed before the converter existed, then passed for all 68 questions in modules 01–04. Exact source comparisons, unique IDs/orders, translated text, earlier condition parents, current 60-question pilot builder, full-bank audit, 79-file source hash verifier, source fidelity/layout/report tests and JavaScript syntax all passed. GitHub Actions has not yet been observed for this commit.
- **Remaining:** this is a build adapter only; no additional source questions are active. Full group titles and report ordering for all 48 modules still need a source-grounded solution before full activation.
- **Next action:** Task 5d — extend the adapter fidelity batch to modules 05–08, recording any source variations without changing the active pilot.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 9

**Task 5d — source-adapter batch 2.**
- **Starting commit:** `e87760abe9971c916678d34b0eeb37fafc727d1c` on `develop`.
- **Implementation commit:** `56fbefcb5fd99649044f83e83fabc98d28306100` on `develop` (remote readback confirmed).
- **Files:** `.github/workflows/pilot-checks.yml`, `tests/pilot/test_source_adapter.py`, this changelog.
- **Completed:** expanded adapter checks to modules 01–08. Modules 05–06 add hide-condition branches and module 06 has more nested follow-ups; all records match the unchanged source exactly.
- **Checks:** `python3 tests/pilot/test_source_adapter.py` PASS for 135 questions, unique IDs/orders, translations, answer/status/type data and valid earlier condition parents. `python3 tests/pilot/test_full_bank_audit.py` and `python3 tools/verify_project_index.py` PASS. Active pilot remains 60 questions.
- **Next action:** verify the next source batch; do not activate it until the adapter comparisons pass.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 10

**Task 5e — source-adapter batch 3.**
- **Starting commit:** `56fbefcb5fd99649044f83e83fabc98d28306100` on `develop`.
- **Implementation commit:** `2dff096fb92ca358615154eeaa34b1236ed7004b` on `develop` (remote readback confirmed).
- **Files:** `tests/pilot/test_source_adapter.py`, `.github/workflows/pilot-checks.yml`, this changelog.
- **Completed:** extended exact source comparisons through module 16. The batch includes 26 conditional questions in module 10, M14_02 medicineList, and conditions in modules 09, 12 and 15; adapter output retains each unchanged.
- **Checks:** source-adapter PASS for 293 questions in modules 01–16; all IDs/orders unique; each condition parent exists in the batch and precedes its child. Full source audit and original-file hash verifier PASS. Active pilot remains 60 questions.
- **Next action:** verify the next source batch before enabling it in runtime.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 11

**Task 5f — source-adapter batch 4.**
- **Starting commit:** `2dff096fb92ca358615154eeaa34b1236ed7004b` on `develop`.
- **Implementation commit:** `181e00c6eabc6ff784dfe9247f67913de58749bd` on `develop` (remote readback confirmed).
- **Files:** `tests/pilot/test_source_adapter.py`, `.github/workflows/pilot-checks.yml`, this changelog.
- **Completed:** extended exact source comparisons through module 24, including module 18's conditional group; no source entries or pilot registry were copied or changed.
- **Checks:** adapter PASS for 449 questions in modules 01–24; all condition links resolve to earlier source questions in the tested batch. Full source audit and all 79 original-file hashes PASS.
- **Next action:** test the next source batch, which contains several multi-choice modules and the largest section so far.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 12

**Task 5g — source-adapter batch 5.**
- **Starting commit:** `181e00c6eabc6ff784dfe9247f67913de58749bd` on `develop`.
- **Implementation commit:** `e15890bfc2877e25fcf10d1d966a69853112a722` on `develop` (remote readback confirmed).
- **Files:** `tests/pilot/test_source_adapter.py`, `.github/workflows/pilot-checks.yml`, this changelog.
- **Completed:** extended exact adapter checks through module 32. The batch contains multi-select rules in modules 27, 30, 31 and 32, with 15 conditional entries each in 31 and 32; all source mappings and earlier-parent checks pass.
- **Checks:** adapter PASS for 610 questions in modules 01–32. Full source audit and original-file hash verifier PASS. Active pilot remains 60 questions.
- **Next action:** test modules 33–40, including the two short-text entries and conditional branches.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 13

**Task 5h — source-adapter batch 6.**
- **Starting commit:** `e15890bfc2877e25fcf10d1d966a69853112a722` on `develop`.
- **Implementation commit:** `3c0506de0831e8223437b56ec8fb5ac9978b5add` on `develop` (remote readback confirmed).
- **Files:** `tests/pilot/test_source_adapter.py`, `.github/workflows/pilot-checks.yml`, this changelog.
- **Completed:** extended adapter checks through module 40, including both `shortText` records in module 33 and the many conditional/multi-select records in modules 34–40.
- **Checks:** adapter PASS for 668 questions in modules 01–40; earlier condition parents resolve. Full source audit and 79-file hash verifier PASS.
- **Next action:** complete the adapter audit with modules 41–48.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 14

**Task 5i — source-adapter final batch.**
- **Starting commit:** `3c0506de0831e8223437b56ec8fb5ac9978b5add` on `develop`.
- **Implementation commit:** `a80595f419d535eb96af92ccdf67cc203c5bcae5` on `develop` (remote readback confirmed).
- **Files:** `tests/pilot/test_source_adapter.py`, `.github/workflows/pilot-checks.yml`, this changelog.
- **Completed:** adapter fidelity checks now cover every original question in all 48 source modules. The test asserts all 712 IDs/orders, translations, codes, statuses, types, condition references and earlier-parent order; the active pilot remains 60 questions.
- **Checks:** `python3 tests/pilot/test_source_adapter.py` PASS for all 712; `python3 tests/pilot/test_full_bank_audit.py` PASS; `python3 tools/verify_project_index.py` PASS for all 79 original hashes. This is source mapping verification, not application integration or translation/clinical review.
- **Next action:** resolve source section labels from the frozen references, then build full groups directly from the source without maintaining duplicate question copies.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 15

**Task 5j — source-grounded full-module labels.**
- **Starting commit:** `a80595f419d535eb96af92ccdf67cc203c5bcae5` on `develop`.
- **Finding:** module JSON contains question text but no section title. The frozen LV/EN/RU references each have 48 exact title strings; avoid inventing or translating the headings.
- **Implementation commit:** `a958ee76a3203196047c2b9255d77407d3e92212` on `develop` (remote readback confirmed).
- **Files:** `src/pilot/i18n/module-titles.{lv,en,ru}.json`, `tools/build_pilot.py`, `tests/pilot/test_module_titles.py`, `.github/workflows/pilot-checks.yml`, this changelog.
- **Completed:** stored the 48 original section titles for LV/EN/RU without editing the references. The builder validates complete ordered title maps for future full-bank groups.
- **Checks:** the new test failed before the loader existed, then passed exact string/order comparisons against all three frozen HTML baselines (144 titles total). Full source adapter and hash verifier also passed. No runtime questions or pilot UI changed.
- **Next action:** build source-backed groups for all modules as a separate bundle function and verify question count, group coverage, conditions, and no duplicate or omitted IDs before activation.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 16

**Task 5k — assemble full source groups without activation.**
- **Starting commit:** `a958ee76a3203196047c2b9255d77407d3e92212` on `develop`.
- **Implementation commit:** `462b9aea043110aeb7f57c91b8a846ad4cfc2193` on `develop` (remote readback confirmed).
- **Files:** `tools/build_pilot.py`, `tests/pilot/test_full_groups.py`, `.github/workflows/pilot-checks.yml`, this changelog.
- **Completed:** added read-only group assembly directly from the original module files and title catalogs. It produces 48 optional groups and all 712 questions once. It preserves `M32_02` in section 33 according to its source `section` field rather than deriving placement from its ID. The current pilot builder still emits 60 questions.
- **Checks:** new full-group test PASS (48 groups, 712 unique IDs/orders, valid earlier condition parents, exact LV/EN/RU titles and source-section oddity); source audit, all 79 original hashes and existing 60-question builder PASS.
- **Remaining:** full groups are not yet selected by `build_bundle`/HTML; no complete questionnaire artifact exists yet.
- **Next action:** Task 5l — set complete, separate question-navigation and clinician-report topic orders. Start questions with approachable topics, keep personal details late in the questionnaire, and put safety-sensitive topics toward the end of the doctor report.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 17

**Task 5l — full topic order.**
- **Starting commit:** `462b9aea043110aeb7f57c91b8a846ad4cfc2193` on `develop`.
- **Implementation commit:** `1b221edddd858986f21aae5e1e8de3010d223645` on `develop` (remote readback confirmed).
- **Files:** `src/pilot/modules/layout.json`, `src/pilot/reports/presentation.json`, `tests/pilot/test_layout.py`, `tools/build_pilot.py`, this changelog.
- **Completed:** added an explicit 48-module full navigation order beginning with everyday/physical topics and leaving personal information last, plus a separate 48-topic report order beginning with personal/everyday content and moving safety-sensitive modules toward the end. No weights were added. The existing 7-module pilot order remains unchanged; a first attempt to reuse the new order there failed its browser sequence check and was corrected by separating `full_order`.
- **Checks:** layout/source order test, builder, report tests, source adapter, full-group test and desktop offline browser journey PASS. Report-order rules verify all 48 modules exactly once and sensitive topics after routine modules. Native Android remains unverified.
- **Next action:** Task 5m — add an opt-in `full_bank` bundle/build mode using the source groups, keep pilot mode intact, and verify its 712-question data and one-file HTML before switching any default artifact.

### 2026-11-06 · COMPLETE-QUESTIONNAIRE-REVIEW-FEEDBACK · checkpoint 18 (IN_PROGRESS)

**Task 5m — opt-in full-bank bundle.**
- **Starting commit:** `1b221edddd858986f21aae5e1e8de3010d223645` on `develop`.
- **Scope:** let the existing builder assemble a full 712-question bundle from source groups, apply `full_order`, and package a full-bank HTML in an explicit mode. Keep the current pilot mode and default artifact unchanged until full runtime checks pass.
- **Tests planned:** 712 unique question IDs/orders, every locale, 48 optional groups, exact conditions and answer maps, all report mappings resolve, complete embedded HTML with no external runtime requests, pilot output remains 60.
- **Files expected:** builder, focused full-bundle/build test, workflow and changelog.
- **Next action:** add a `full_bank` argument and preserve the existing pilot branch; test the full bundle and HTML without changing distribution or public release.
- **Resumed 2026-11-06:** confirmed clean `develop` checkout at `608bdbbf5e97865f9dbf057a1214f56ebcf37602`, the descendant of checkpoint 17. Read current `AGENTS.md`, file index, manifest, architecture and builder state. Next: add a failing focused test for explicit full-bank bundle/HTML mode, then implement and verify it.
- **Implementation checkpoint:** added `build_bundle(full_bank=True)`, `make_html(full_bank=True)`, and `--full-bank`. The opt-in artifact uses a distinct schema/version and output filename; default CLI output and pilot bundle shape remain the existing 60-question build. Added structural/embedded-data/CLI coverage to CI and documented that the 712-question runtime still needs a separate behavior audit. Focused test first failed because the mode did not exist, then passed after implementation.
- **Local verification:** source integrity, 48-module audit/adapter/group/title checks, full-bank bundle/HTML/CLI test, unchanged 60-question pilot structural/fidelity/layout checks, report tests, JavaScript syntax, default and full-bank CLI builds, and `git diff --check` all PASS. Read both temporary output files back: default pilot embeds 60 questions; full-bank embeds 712 and has no runtime network imports. Existing browser journeys could not start locally because Playwright is not installed; the CI workflow installs it. **CI and remote readback pending.**
- **CI regression and fix:** run `42220255836` passed the new full-bank test and default browser smoke, then exposed an extensibility check: adding a pilot module and its report topic made the fixed 48-topic map reject the appended topic. Added a focused fixture to the full-bank test, and changed validation to require the exact 48 source modules once while allowing additional registered pilot topics. The focused full-bank/extension test, layout test, default bundle test and diff check PASS locally.
- **Verified checkpoint:** Task 5m is DONE. Implementation commit `0b825f33a8e5c85397e0c40f5b69f73bf8e7c2b2`; compatibility fix `7284e4a9f7d2b716703f9619d298a9fdf20c1051`. Remote branch readback confirmed both. [CI run 42220636242](https://github.com/janisp123/mental-health-questionnaire/actions/runs/42220636242) passed all source, bundle, report, syntax and pilot browser checks, including the extensibility journey. The optional full-bank HTML embeds all 712 questions in 48 groups; the default pilot remains 60. No distribution artifact was changed. This verifies packaging and existing pilot behavior, not full-bank runtime behavior.
- **Next action (overall goal still IN_PROGRESS):** Task 5n — run offline-browser behavior checks against the 712-question build, covering group selection, question types, conditional branches, recovery and clinician reports; fix any full-bank-only issues. Keep the default artifact unchanged until that runtime audit passes.

### 2026-11-06 · WORKFLOW-CONTEXT-LOAD-REDUCTION · TASK_DONE

**Goal:** reduce Work chat loading and tool-output overhead while keeping the project's resumable checkpoints and verification intact.
- **Starting commit:** `cb2ede2ecb6faf5b2cab04f1e72c24e86501edc8` on `develop`.
- **Implementation commit:** `3b437e9bc0c6f1334507b13d376b91dd0f5c0c42` on `develop` (remote readback confirmed).
- **Scope:** revise `AGENTS.md` to require targeted changelog/manifest/index reads, focused tests before full checks, and CI step summaries before full logs. No questionnaire or CI behavior changes.
- **Completed:** future work should read the active changelog entry and relevant manifest/index sections, run a focused test first, and inspect CI step summaries before requesting logs. This prevents routine turns from loading the full 50 KB changelog, full manifest hash inventory, or entire workflow log.
- **Checks:** `git diff --check` PASS. Documentation-only change; no code tests or CI run needed. `AGENTS.md` and the changelog were read back from `develop`.
- **Next action:** resume overall project Task 5n — offline-browser behavior audit of the 712-question build.

### 2026-11-06 · FULL-BUILD-FIRST · IN_PROGRESS

**Goal:** make the 712-question application the active build, archive the 60-question pilot, remove pilot-only checks/artifacts from the active workflow, and keep reusable design/runtime code separate from the immutable question bank.
- **Starting commit:** `4f51b0e0498a64669c21dab8c10c1839f8bfec99` on `develop`.
- **Checklist:** (1) [DONE] confirm the 48 source modules/712 questions remain the canonical untouched bank; (2) [DONE] isolate reusable UI/runtime and design assets from question content; (3) [IN_PROGRESS] make the full bank the primary build and add browser verification; (4) [TODO] archive pilot-only data/artifact/tests and remove pilot-only checks/artifacts from active CI; (5) [IN_PROGRESS] update the manifest/index/architecture and verify the complete workflow.
- **Approach:** keep `src/modules/` unchanged as question/answer source; move only reusable UI/runtime out of the pilot namespace; use the existing source adapter and full-module ordering. Preserve the pilot files in an archive until equivalent full-build checks pass, then remove them from active CI.
- **Step 1 complete:** moved reusable app/runtime/style/report code and shared UI/medicine labels into `src/app/`; moved full-bank layout, report rules and frozen module titles into `src/questionnaire/`. Updated the builder, tests, manifest, file index and architecture paths. Original question modules were untouched.
- **Verification:** 79-file source integrity, 48-module audit/adapter/group/title checks, full-bank packaging, 60-question pilot structural/fidelity/layout checks, report/medicine report tests, JavaScript syntax and `git diff --check` all PASS. Full-browser journey has not yet been retargeted to the full build.
- **Verified checkpoint:** commit `b81d22411a336fe4cd1ddd68650bb3eea875400c` on `develop`; [CI run 42233108862](https://github.com/janisp123/mental-health-questionnaire/actions/runs/42233108862) passed, including the existing pilot browser journey. The relocated runtime/data boundary is verified with no original question content changed.
- **Next action:** add a full-bank offline-browser journey using the same app shell; switch active CI to full-bank checks and archive the pilot only after those checks pass.

### 2026-11-06 · FULL-BUILD-FIRST · browser coverage added (IN_PROGRESS)

- **Starting commit:** `27209acb1b35c869b494d695952f76aa160be4c2` on `develop`.
- **Task:** add a real offline-browser journey for the complete build before removing pilot checks.
- **Files:** `.github/workflows/pilot-checks.yml`, `tests/full_bank/browser_helpers.py`, `tests/full_bank/test_runtime.py`, this changelog.
- **Completed:** added a full-bank browser test covering 48 optional sections, all 712 embedded questions, multi/single answering and double-tap handling, the real medication-list and short-text items, and report inclusion. CI now runs this journey with Playwright Chromium.
- **Local checks:** Python compilation, full-bank structural build test (712 questions/48 groups), and `git diff --check` PASS. Browser execution is **pending CI** because Playwright/Chromium is unavailable in this local environment.
- **Remaining:** CI must pass the new full-bank browser journey; fix any runtime issue before archiving pilot files or removing pilot-only CI coverage.
- **Exact next action:** commit this checkpoint, inspect the resulting CI step summary, and resolve any full-bank runtime failures.

- **CI result:** first complete-workflow run [42234413055](https://github.com/janisp123/mental-health-questionnaire/actions/runs/42234413055) passed all existing checks and the 60-question Chromium journey, but the new complete-bank journey failed after answering `M14_01`; it did not reach expected `M14_02`. The failure occurs before medicine/report assertions, so the full-bank runtime audit remains blocked. Updated the assertion to report the actual reached ID.
- **Diagnosis:** rerun [42234679971](https://github.com/janisp123/mental-health-questionnaire/actions/runs/42234679971) showed the current ID remained `M14_01`; its test clicked the parent label, unlike the reliable input activation used elsewhere. Changed this one test action to Playwright's explicit radio `check()`.
- **Exact next action:** rerun the complete-bank Chromium journey; if it still fails, inspect question rendering/state transitions before archiving anything.
