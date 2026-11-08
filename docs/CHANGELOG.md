# Active development changelog — mental-health-questionnaire

**Active branch:** `develop`; `main` and the frozen v16 Git reference remain unchanged. The old Drive v16 copies were removed from the link-shared review folder; the current technical-review candidate is indexed in the manifest.
**Current build:** one self-contained offline HTML with 48 unchanged source modules / 712 questions grouped into 15 user-facing sections. GitHub app and full-bank workflows passed; the current technical-review HTML and trilingual PDF are in the linked Drive folder. This is not a public release or clinical validation.
**Outstanding external checks:** actual Android Chrome use; human review of LV interface wording and EN/RU drafts; professional/clinical review. Do not mark those complete without evidence.
**History:** the prior pilot and full-build chronology is preserved in [CHANGELOG_HISTORY_2026-11-06.md](history/CHANGELOG_HISTORY_2026-11-06.md). Read it only when a task needs that history.

## 2026-11-07 · TRANSLATION-AUDIT-RECOVERY · IN_PROGRESS

Resumed from `85f4332`. Verified GitHub's last successful checkpoint is S10 (`d0ac047`); S13's three subsequent runs failed. Reproduced the index failure: `tests/fixtures/181_MODULE_INDEX_v16.json` is 11906 bytes, but the manifest recorded 11816. Its recorded Git blob hash was already correct. Repaired only the byte count.

Established local Python/Playwright/Chromium checks on Windows. Restored exact Git text bytes after checkout CRLF conversion; frozen reference content is unchanged. Fixed the CLI build test to invoke the current Python interpreter instead of assuming `python3`. Source-audit failures now identify the affected question and language, and the audit checks every LV record against the frozen 712-question baseline.

Baseline after the manifest repair: 23/24 local checks passed, including full offline browser journey, recovery, report, print PDF, responsive layout and all three locales. The remaining source-audit failure identifies malformed RU keys (`choices.E`, `choices.F`, `choices.B`) on M32_36, M32_40 and M32_42. S13 review and repair are in progress; do not mark it complete from the browser pass alone.

Drive folder read on this session: HTML modified 14:18, PDF 13:57. Read access works; write access awaits a connected Drive session. No files uploaded in this recovery session yet. Exact next action: complete S13 corrections, refresh indexes, rerun all checks, commit the verified checkpoint, then S12. Detailed task checklist: `docs/superpowers/plans/2026-11-07-translation-completion.md`.

## 2026-11-07 · REPORT-AND-ANSWER-VISIBILITY · IN_PROGRESS

**Starting commit:** `b78a9c278bc4cb75ca5a39150f95f3d2e1139e85` on GitHub `develop`.

1. [DONE] Make single-choice selection unmistakable before delayed advance; preserve immediate Skip and duplicate-tap protection.
2. [DONE] Put selected / completed / skipped counts at the top of the clinician report, omit skipped answers, place technical feedback after answers, and retain explicit safety-answer bolding.
3. [DONE] Place name and surname at the report’s upper left if provided; show writable name/date lines when absent.
4. [DONE] Keep the report screen to Print / save PDF, Back to answers, and Select sections; remove the contact email from results and the reviewer PDF while retaining it in the legal notice and project-feedback copy.
5. [DONE] Explain the accuracy-review workflow in the Latvian, English, and Russian in-app guides and the Latvian reviewer PDF.
6. [DONE] Run focused report/screen/selection checks and the full offline Chromium journey; refresh both Drive files in place and verify their readback hashes.
7. [TODO] User check on Android Chrome: confirm the single-choice cue and Print / save PDF flow are clear on their device.

**Workflow:** work in small verified batches on `develop`; refresh the Google Drive HTML/PDF after each user-testable batch. Preserve the 48 source modules, 712 question IDs, recovery schema, and frozen references.

**Batch 1 — selection cue:** the selected radio renders checked with a stronger green card and a separate checkmark, then advances after about 1.3 seconds. Skip cancels the pending timer; duplicate taps are coalesced.
**Checks:** app-component workflow `42361043110` PASS and full offline questionnaire workflow `42361043037` PASS on `cfb8f6868fc04a801339063faea79614861bd166`.
**Drive refresh:** replaced HTML and one-page A4 Latvian reviewer PDF in place, preserving their IDs. Readback hashes matched: HTML `5e4ee429be88e60d7a2e11b91d1384e1e096882ae103a1478bcecb5192749fa3`; PDF `38a2e723364211863f9a0aaa4c9907d7b1815e1709ec1d226c44d8a16263b0bf`. PDF rendered and visually inspected.
**Reviewer guide:** records the build commit, describes the visible selection cue, and contains no contact email.

**Batch 2 — concise report:** the report screen now exposes only Print / save PDF, Back to answers, and Select sections. Print output puts name/date lines and selected/completed/skipped counts at the top; skipped responses are omitted. Technical feedback appears after medical answers. Explicit configured bolding remains applied to designated safety answers. The visible results page has no project contact email; project-feedback copy retains the project contact.
**Accuracy-review instructions:** in-app guides in LV/EN/RU and the trilingual reviewer PDF tell reviewers to skip acceptable questions, flag unclear or incorrect items, choose a reason, then print/save and return the PDF. The reviewer PDF states that skipped responses are omitted and that technical feedback is separated after answers.
**Checks:** report/component checks and syntax/locale checks passed. Full offline Chromium workflow `42365207780` PASS after correcting a stale test assertion: the test opened the app in English but compared Latvian labels. Full workflow `42365507785` PASS on source/test commit `3e7e1f402d7d396477fe70f99fa8698075eeffe7`; it verified the report and all three accuracy-guide translations. App-component workflow `42365400460` PASS.
**Drive refresh:** replaced the existing HTML and PDF in place, preserving IDs. Readback SHA-256 values match: HTML `57101a80db86081f6e44d158cdf6b80519ec15796bb85c86ca4916c37086652e`; PDF `60bb9aeec4a12735999d96daf90db246559da4ee7c74b96b40fce7d9624c8333`. The Latvian reviewer PDF was rendered and visually inspected as a clean one-page A4 document.
**Trilingual README:** consolidated the reviewer instructions into one file, `docs/review/README_LV_EN_RU_v0.2.0.md`, with Latvian, English, and Russian sections. Replaced the Latvian-only PDF in the existing Drive entry with one A4 page per language; its ID/link stayed the same. The trilingual PDF readback hash matches: `9c3cd316081dfa830e71be4de4d33172e1ecf3aad6f8c1a5cfbd7d8f4cc5a5d6`. Both PDF guides were visually inspected.
**Translation audit — Section S11:** reviewed all 62 questions and answer options in Latvian, English, and Russian. The structure was complete, but the review found meaning, grammar, time-frame, and gender-agreement problems. Corrected the identified English/Russian strings in source modules 16, 17, 23, 33, and 43; Latvian source text, question IDs, and answer codes were preserved. Updated the module and fixture integrity indexes. This is a section-by-section audit; English and Russian remain marked as drafts until the full bank is reviewed.
**Checks:** full offline Chromium workflow `42368219970` PASS on `d6c60525c3ec2c6a39e0c4f80a3c7ce9c161ca20`. It verifies the rebuilt 712-question application and targeted translation corrections. The generated HTML was independently checked for all 62 S11 questions and 11 corrected-string checks.
**Drive refresh:** replaced the existing HTML and trilingual reviewer PDF in place, preserving their IDs. Readback SHA-256 values match: HTML `d5d319dcbe51340d66ce6e24b89a5abfa7bee9437a07bba74bbe8999ae70b897`; PDF `1db6de44a7110117ba5e25d477ef35d41648cc8cb0815e93c35f7299bc6fa294`.
**Translation audit progression:** compare Latvian source meaning, timeframe, and answer-option intent against English and Russian; check grammar and natural phrasing; change only translation strings; preserve Latvian text, IDs, codes, and conditions. After each section, update source/fixture integrity indexes, run full CI and inspect the built section, then refresh Drive HTML and reviewer PDF. Record findings and stop point here before moving on.
**Audit build checkpoint:** `d6c60525c3ec2c6a39e0c4f80a3c7ce9c161ca20`; Section S11 corrections are verified and distributed.

| Order | Section | Questions | Status |
|---:|---|---:|---|
| 1 | S11 — Everyday life, goals, digital habits and spending | 62 | DONE |
| 2 | S01 — Health history, medicines and memory | 61 | DONE |
| 3 | S09 — Sleep, fatigue and pain | 50 | DONE |
| 4 | S06 — Attention, learning and development | 43 | DONE |
| 5 | S10 — Alcohol, nicotine and other substances | 37 | DONE |
| 6 | S13 — Family, social context and caregiving | 70 | DONE locally |
| 7 | S12 — Relationships and emotional patterns | 42 | DONE |
| 8 | S14 — Eating, appearance and health concerns | 49 | DONE |
| 9 | S15 — Sexuality and reproductive health | 47 | DONE |
| 10 | S07 — Intrusive thoughts and repetitive habits | 45 | DONE |
| 11 | S08 — Trauma, loss and life changes | 48 | DONE |
| 12 | S02 — Mood and energy | 38 | IN PROGRESS (21/38) |
| 13 | S03 — Anxiety, panic-like episodes and stress | 40 | TODO |
| 14 | S04 — Wellbeing, safety and unusual experiences | 44 | TODO |
| 15 | S05 — Anger and impulses | 36 | TODO |

**Translation audit — Section S01:** reviewed all 61 questions and answer options across source modules 01, 14, and 30. Corrected identified EN/RU meaning, grammar, inclusivity, and timeframe issues, including the exact one-month boundary, diagnosis-status wording, medication-dose reasons, memory terminology, and the urgent hand-movement note. Latvian wording, question IDs, answer codes, and conditions were preserved. All EN/RU option-code sets match Latvian.
**Checks:** full offline Chromium workflow `42369805843` PASS on source commit `421c526e0eaee40dddd2e16cee4669faeeb0ee7a`. The run rebuilt and exercised all 712 questions; S01-specific assertions cover 61 questions, corrected wording, and Russian gender-neutral uncertainty. The generated HTML was checked for the S01 corrections.
**Distribution:** refreshed the existing Drive technical-review HTML and trilingual PDF in place. Read-back SHA-256 matched the uploaded files: HTML `8ededc611dc63fdc495d72b2a5bbf936550824b13028c8aa1dcf49e0738d26f2`; PDF `8613fd1ce73767ada568d464541862a0f5398f048840f6e6e281bda98b7851d0`. The README now makes feedback voluntary and unpaid, directs feedback to the project email, and removes the statement that Latvian is primary while EN/RU are untranslated. The answer PDF is described as material for the user’s appointment; it does not need to be sent to the project.
**Audit build checkpoint:** `421c526e0eaee40dddd2e16cee4669faeeb0ee7a`; S11 and S01 are verified and distributed.
**Translation audit — Section S09:** reviewed all 50 questions and answer options in source modules 11, 12, and 13. Corrected EN/RU wording for the workday/weekend sleep comparison, the exact one-month onset boundary, the lifetime timeframe, and variable pain responses. Standardized gendered Russian uncertainty options to gender-neutral wording. Latvian text, question IDs, answer codes, and conditions were preserved; EN/RU option-code sets match Latvian.
**Checks:** full offline Chromium workflow `42370999829` PASS on source commit `337746c23b27ff9d07396243a9bed7fb581354af`. It rebuilt and exercised the full 712-question application; the S09 browser assertions cover all 50 questions and key corrected strings. The generated HTML was checked for the corrections.
**Distribution:** refreshed the existing Drive technical-review HTML in place and verified read-back SHA-256 `1d7e964db1996edb536afc405a61181d3efce7e11eb36714648560ae5273fa14`. The trilingual PDF remains the refreshed S01 copy, SHA-256 `8613fd1ce73767ada568d464541862a0f5398f048840f6e6e281bda98b7851d0`.
**Audit build checkpoint:** `337746c23b27ff9d07396243a9bed7fb581354af`; S11, S01, and S09 are verified and distributed.
**Translation audit — Section S06:** reviewed all 43 questions and answer options in source modules 07, 08, 25, and 46. Corrected EN/RU meaning and grammar for social exhaustion, childhood dialogue, mathematical calculation difficulties, developmental and language concerns, and previous assessments. Standardized Russian uncertainty options to gender-neutral wording and made M46_04 responses grammatically consistent. Latvian text, question IDs, answer codes, and conditions were preserved; EN/RU option-code sets match Latvian.
**Checks:** full offline Chromium workflow `42371371509` PASS on source commit `60921b9cd256a3fb76a57beb58d26f7b54dea6e1`. It rebuilt and exercised all 712 questions; S06-specific assertions cover all 43 questions and key corrected strings. The generated HTML was checked for the corrections.
**Distribution:** refreshed the existing Drive technical-review HTML in place and verified read-back SHA-256 `e6469902184583c123f5c2d6a5654c1d3729adeae123320e519f57ac50574dba`. The trilingual PDF remains unchanged from the refreshed S01 copy, SHA-256 `8613fd1ce73767ada568d464541862a0f5398f048840f6e6e281bda98b7851d0`.
**Audit build checkpoint:** `60921b9cd256a3fb76a57beb58d26f7b54dea6e1`; S11, S01, S09, and S06 are verified and distributed.
**Translation audit — Section S10:** reviewed all 37 questions and answer options in source module 15. Corrected EN/RU meaning and grammar for “none” options, lifetime wording, alcohol-use frequency, use outside medical instructions, and the distinction between general substances and narcotics. Fixed the repeated “occasion” wording and the “for other substances” answer fragments. Standardized Russian uncertainty options. Latvian text, question IDs, answer codes, and conditions were preserved; EN/RU option-code sets match Latvian.
**Checks:** full offline Chromium workflow `42371760581` PASS on source commit `3e024abc12c040a1024690f66c817c9d7e2b76fc`. It rebuilt and exercised all 712 questions; S10-specific assertions cover all 37 questions and key corrected strings. The generated HTML was checked for the corrections.
**Distribution:** refreshed the existing Drive technical-review HTML in place and verified read-back SHA-256 `31d49bc94a520e15e9d2d638e5b4e66f9a4189a00504c6cb42340ed08221f927`. The trilingual PDF remains unchanged from the refreshed S01 copy, SHA-256 `8613fd1ce73767ada568d464541862a0f5398f048840f6e6e281bda98b7851d0`.
**Audit build checkpoint:** `3e024abc12c040a1024690f66c817c9d7e2b76fc`; S11, S01, S09, S06, and S10 are verified and distributed.
**Exact next action:** begin S13 — Family, social context and caregiving (70 questions). Continue in section order only after the source/index checks, full CI, and built-section inspection pass. External human and clinical reviews remain outstanding.

## 2026-11-07 · QUESTION-ANSWER-CLARITY · IN_PROGRESS

**Starting commit:** `50b3f7ca6162c65b870a26702c638a1f31fd7dd0` on `develop`.

1. [DONE] Add localized per-question instructions for multiple-choice questions, using the original `maxChoices` value where defined and otherwise saying multiple answers are allowed.
2. [DONE] Keep a single-choice answer visibly selected for one second before saving and advancing. Preserve Skip and ensure a pending timer cannot overwrite a later action.

**Workflow:** verify and record each task separately, then rebuild and refresh the Drive HTML/PDF after each completed task so the user can test that checkpoint.

**Task 1 checkpoint — multi-answer guidance:** added LV/EN/RU help beside each multi-select question. Questions with `maxChoices` state the exact limit; questions without it say multiple answers are allowed. The synthetic fixture verifies the three-answer cap and rejected fourth choice.
**Files:** `src/app/screens/question.js`, `src/app/i18n/ui.lv.json`, `src/app/i18n/ui.en.json`, `src/app/i18n/ui.ru.json`, `tests/app/runtime_fixture.py`, `tests/app/test_question_screens.js`, `tests/app/test_runtime_answers.py`.
**Checks:** screen renderer, locale catalog, app build manifest, model/flow/recovery/events checks, JS/Python syntax, offline HTML build and `git diff --check` PASS. Focused browser workflow `42357466056` PASS on `cee47ce3e3e5f7de740dbd9f2b3045ef7816f85d`; local browser unavailable. Two initial browser failures were test expectation issues and corrected before the passing run.
**GitHub commits:** feature `e57b866aae511658b94d478f1b2e4e554a94d5eb`; test corrections `379a7b86585193c4f51dfe8b54bde0697d4a17ab`, `21c1d2650fec887d60209839a609801c08ca075d`, `cee47ce3e3e5f7de740dbd9f2b3045ef7816f85d`.
**Drive refresh:** replaced the current HTML and PDF in place, preserving their file IDs. HTML SHA-256 `5f97ae67e6099776ae6aa48e13cf9a9464903814c208d0c3334e43638ed2476c`; PDF SHA-256 `791cb6deb85b5b32ea600044a6aa4ce3cf5a4e11660e250bcfa0b7eba2df5e46`. Downloaded Drive readbacks match both local hashes.
**Manifest/README:** updated source commit to `cee47ce3e3e5f7de740dbd9f2b3045ef7816f85d` and recorded current artifact checksums; reviewer PDF now describes the multiple-answer guidance.
**Metadata Git commit:** `035d5bcae48e66e0094f0f814973938532373953`.
**Next action:** finish task 2, run the focused and full-bank browser checks, then rebuild and refresh Drive.

**Task 2 checkpoint — visible single-choice selection:** implementation started from `035d5bcae48e66e0094f0f814973938532373953` on `develop`. The selected radio is now left native and highlighted for one second before saving and advancing. Skip/navigation cancels a pending timer; duplicate click/change events for the same choice are coalesced.
**Tests added/updated:** focused browser case checks immediate highlight, no early advance, one-second advance, and Skip winning over a pending answer; full-bank helper now waits for the delayed transition and keeps the double-tap case.
**Local checks:** event, answer-flow, app-build-manifest, locale-catalog, screen-renderer, JavaScript/Python syntax, and `git diff --check` PASS. Local Chromium is unavailable, so browser tests remain pending in GitHub Actions.
**CI findings:** app-component workflow `42358174072` PASS. Full-bank runs `42358094071` and `42358174069` exposed test-harness assumptions: multi-select remains on the question, and this offline app CSP blocks Playwright string-evaluation waits. The helper now uses a fixed 1.1-second wait for single-choice only; multi-select remains manual-save.
**Final CI:** focused app workflow `42358261344` PASS and full offline questionnaire workflow `42358261312` PASS on `65797713807f273ef61d31d8bb3684844248e197`. The focused browser case confirmed immediate visual selection, no early advance, one-second advance, and Skip cancelling the pending answer. Full 712-question Chromium journey passed. Earlier failures were test assumptions and were corrected before this pass.
**Verified artifacts:** HTML SHA-256 `40f3b74ae1284388ea3f4f880f722a102005fd82c7fc326e3d3559d893def614`; Latvian PDF SHA-256 `0aed2c2006ea9e16a6d9ee34ba7cb5e38cb1c30ae934bc166bde198d81b81958`. Both files replaced in Drive in place; readback hashes match. The PDF renders as one A4 page and was visually inspected.
**Commits:** runtime `e2e44e24fd32aa02d3893415b41cbb92053ab4e7`; browser-helper corrections `4abccbc0821fa106d3c31cc87955461ebd0e44a2`, `65797713807f273ef61d31d8bb3684844248e197`.
**Remaining limitation:** actual Android-device testing is not done. Desktop Chromium verified the offline build; human review of language and clinical content remains separate.
**Exact next action:** test the refreshed Drive HTML on your devices and report any issues.

## 2026-11-07 · SECTION-END-SAVE-PROMPT · DONE

**Starting commit:** `b2964d660afdb319e4dd695485e2be50797489f9` on `develop`.

**Change:** removed automatic recovery-file downloads while answering. When a user reaches the end of a section, the app now recommends saving and offers “Save and continue” or “Continue without saving” in LV/EN/RU. The existing manual save control remains. A section-boundary recovery file points to the next question so it resumes in the right place.

**Files:** `src/app/core/app.js`, `src/app/i18n/ui.lv.json`, `src/app/i18n/ui.en.json`, `src/app/i18n/ui.ru.json`, `tests/app/runtime_fixture.py`, `tests/app/test_runtime_answers.py`, `tests/app/test_runtime_layout.py`, `tests/full_bank/browser_helpers.py`, `tests/full_bank/test_runtime.py`, `docs/QUESTIONNAIRE_ARCHITECTURE.md`, `docs/CHANGELOG.md`.

**Checks:** locale catalogs, app source/screens/logic, JavaScript syntax, offline HTML build, and `git diff --check` PASS. The first CI runs exposed outdated test assumptions; updated the synthetic section fixture and full-bank recovery check. Focused workflow 42353404253 and full-bank workflow 42353404241 PASS. Local Chromium is unavailable; the browser checks ran in CI with desktop Chrome. Android device testing was not done.

**Latest verified code commit:** `706f335e7ca3de752db306b138fcb89c0a68a5f7` on `develop`. The regenerated 712-question HTML has SHA-256 `65fc98d91471bea56bffe21d7f8e839822a7749da59a675f2949835dccdb7b32`.

**Next action:** user-facing Android check if desired; no Google Drive copy was updated.

## 2026-11-07 · SECTION-SAVE-DRIVE-REFRESH · DONE

**Source:** verified application code commit `706f335e7ca3de752db306b138fcb89c0a68a5f7` on `develop`.
**Change:** updated the Drive HTML and matching Latvian PDF in place for testing. The PDF now describes the end-of-section save choices and identifies the matching source commit. Added a standing rule to refresh the Drive test files after every verified batch intended for user testing.
**Files:** `AGENTS.md`, `docs/review/README_LV_v0.2.0.md`, `project-manifest.json`, `docs/CHANGELOG.md`, Google Drive review candidate.
**Artifacts:** HTML SHA-256 `65fc98d91471bea56bffe21d7f8e839822a7749da59a675f2949835dccdb7b32`; PDF SHA-256 `b62fa740bb39307816f8232f0abaa0500f2a79fa86ba4d1afdaf456ccf9ccd3e`.
**Verification:** PDF rendered and visually inspected as one A4 page; Drive file bytes and hashes read back after replacement. App behavior checks remain those recorded for the source commit above.
**Git commit:** `247c503695fd59e96c33619433be59ff92375838` (artifact metadata, review PDF source, and automatic Drive-refresh handoff rule).
**Next action:** continue Android and human review; refresh Drive after each future verified testing batch.

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

### Recovery checkpoint — S13 complete locally
All 70 S13 questions and 423 option labels per language reviewed. Corrected meanings and formal address; repaired five invalid RU option keys. Independent review findings applied. Full local 24/24 checks PASS, including browser and print/recovery journeys, index integrity and exact frozen LV record parity. Evidence: docs/review/audit-S13.md and docs/review/checks/S13-local.txt. Drive/GitHub not updated; user requests local work until 8 November evening. Next: S12 (42 questions).

### 2026-11-08 · S13 repository synchronization

Verified S13 source checkpoint: `eecfc0f`. The repository review package is in `MH_Public_version`. The HTML is the exact build from the 24/24 local checks (SHA-256 `2975ab219d501726874e76dd5529edf4c5a86ae177c1825ac40b114660c4ec0c`); the existing trilingual guide remains applicable (SHA-256 `8613fd1ce73767ada568d464541862a0f5398f048840f6e6e281bda98b7851d0`). The owner copies the two files to the shared Drive folder. Next translation audit: S12.

### 2026-11-08 · S12 checkpoint 1 · module 19

Audited all 19 module 19 questions and their English and Russian options and time notes. Corrected the Russian day counts and formal address, clarified controlling behavior and privacy wording, and preserved the Latvian records, answer codes and ordering, and questionnaire logic. Updated module integrity metadata and all three in-app change notes. Source integrity, frozen Latvian parity, the source adapter, UI catalogs, and the full offline HTML build passed. S12 remains in progress. Next: module 24, then module 38 and section-level browser verification. The reviewer package still represents S13.

### 2026-11-08 · S12 complete · modules 24 and 38

Reviewed the remaining 23 questions, completing all 42 in S12. Clarified long-standing patterns and formal Russian address. Corrected the separation-fear frequency scale (more than half of the days) and changed the duration question from a future prediction to elapsed duration in both draft languages. Preserved Latvian source, IDs, option codes, conditions and logic. Source integrity, frozen Latvian parity, source adapter, UI catalogs, full HTML build and Chromium offline journey passed. The built HTML was also inspected for the corrected frequency option in all three languages.

Repository reviewer HTML: SHA-256 `6004e75f72d30525105da6ca0713e3f228896c158efba84827fe803e22e9dd86`. The existing trilingual PDF guide remains applicable. The owner copies the HTML to the shared Drive folder. Next: S14.

### 2026-11-08 · S14 checkpoint 1 · module 20

Reviewed all 16 questions and answer labels in module 20. Corrected Russian wording that asked about the urge to eat rather than eating, day-count choices that could imply a continuous spell, and the zero-episodes answer. Clarified night-eating wording in both drafts and used formal Russian address. Latvian records, answer codes, ordering and logic are unchanged. Source integrity, frozen Latvian parity, source adapter, UI catalogs and offline HTML build passed. The reviewer package remains at S12. Next: module 28.

### 2026-11-08 · S14 checkpoint 2 · module 28

Reviewed the 12 health-concern questions in English and Russian. Clarified day-count responses, wording about medical tests and ongoing health worries, and respectful Russian address. Preserved Latvian wording, conditions, IDs and answer codes. Source integrity, frozen Latvian parity, source adapter, locale catalogs and full offline HTML build passed. S14 is at 28 of 49 questions. Next: module 36. The repository reviewer package remains at S12 until the S14 browser check.

### 2026-11-08 · S14 checkpoint 3 · modules 36 and 37

Reviewed 11 questions on eating restrictions and appearance concerns. Corrected the elapsed-duration question in both drafts and repaired appearance answer labels that referred to skis or asked a question instead of naming a body feature. Preserved Latvian wording, conditions, IDs and answer codes. Source integrity, frozen Latvian parity, source adapter, locale catalogs and the full offline HTML build passed. S14 is at 39 of 49 questions. Next: modules 44 and 45, followed by browser verification and the reviewer HTML refresh.

### 2026-11-08 · S14 complete · modules 44 and 45

Reviewed the remaining 10 questions, completing all 49 in S14. Corrected duration versus future frequency, medical assessment wording, and the existing safety note about poisoning, choking and inability to take in fluids. Clarified the body-odour questions and formal Russian address. Preserved the Latvian source, IDs, answer codes and branching. Source integrity, frozen Latvian parity, locale catalogs, full HTML build and Chromium offline journey passed. Inspected the built HTML for all 49 S14 questions and the corrected appearance, duration and safety wording.

Repository reviewer HTML: SHA-256 `0668b4d7a97c11708db1cef236a0c70b9f0b9cfb8e302e1397b5f1ecd5d632fb`. The existing trilingual PDF guide remains applicable. The owner copies the HTML to the shared Drive folder. Next: S15.

### 2026-11-08 · S15 checkpoint 1 · module 26

Reviewed all 10 questions and answer labels in module 26. Distinguished asking for a separate conversation from the following question that explicitly asks for a private conversation. Clarified questions about personal distress and quality of life and used formal Russian address. Preserved the frozen Latvian records, IDs, options and branching. Source integrity, Latvian parity, source adapter, locale catalogs and the full offline build passed. The reviewer build remains at S14. Next: module 27.

### 2026-11-08 · S15 checkpoint 2 · module 27

Reviewed 19 questions about hormonal and reproductive health. Fixed the Russian psychosis response that attributed the experience to the specialist, the cycle response that incorrectly referred to commitments, and the family-history note that referred to the respondent instead of relatives. Clarified the postpartum time ranges and who is in the respondent's care. Preserved Latvian records, conditions, IDs and answer codes. Source integrity, frozen Latvian parity, source adapter, locale catalogs and full offline HTML build passed. S15 is at 29 of 47 questions. Next: modules 34 and 40. The reviewer build remains at S14.

### 2026-11-08 · S15 complete · modules 34 and 40

Reviewed the remaining 18 questions, completing all 47 in S15. Corrected form of address versus physical address, gender expression versus identity, peers versus coworkers, and elapsed duration versus future duration. Preserved voluntariness, Latvian records, IDs, options and branching. Source integrity, frozen Latvian parity, source adapter, locale catalogs, full HTML build and Chromium offline journey passed. Inspected the built HTML for all 47 S15 questions and key corrected labels.

Repository reviewer HTML: SHA-256 `d8173b058cdd1575caa110e058df793ff4177d0c1ea46b712bbae8b0e2c9200f`. The existing trilingual PDF guide remains applicable. The owner copies the HTML to the shared Drive folder. Next: S07.

### 2026-11-08 · S07 checkpoint 1 · module 09

Reviewed all 17 questions and answer labels. Preserved the distinction between helpful routines and actions the respondent feels compelled to repeat, clarified day counts and time boundaries, and improved formal Russian address. Frozen Latvian records, IDs, option codes and branching are unchanged. Source integrity, Latvian parity, source adapter, locale catalogs and full offline HTML build passed. The reviewer package remains at S15. Next: module 29.

### 2026-11-08 · S07 checkpoint 2 · module 29

Reviewed all 12 questions about repetitive habits. Clarified skin picking, hair pulling, interference with everyday activities and exact duration boundaries. Preserved the frozen Latvian records, IDs, answer codes and branching. Source integrity, Latvian parity, source adapter, locale catalogs and the full offline HTML build passed. S07 is at 29 of 45 questions. Next: modules 39, 47 and 48, then browser checks and the reviewer HTML refresh.

### 2026-11-08 · S07 complete · modules 39, 47 and 48

Reviewed the remaining 16 questions, completing all 45 in S07. Clarified age of onset, movements and sounds, and urges that are hard to control. The translation no longer treats the movements as an established disease or limits unexplained episodes to convulsions. Preserved the Latvian source, answer codes and branching. Source integrity, frozen Latvian parity, source adapter, locale catalogs, full HTML build and Chromium offline journey passed. Inspected the built HTML for all 45 S07 questions and key corrected labels.

Repository reviewer HTML: SHA-256 `fefb5156df1bb3c924393708ca6230584e898572d80c8329a3f4bc3ad45c40c2`. The existing trilingual PDF guide remains applicable. The owner copies the HTML to the shared Drive folder. Next: S08.

### 2026-11-08 · S08 checkpoint 1 · M10_01–M10_14

Reviewed the first 14 questions in module 10. Corrected the inclusive one-month boundary, the response meaning more than half of the days, and the distinction between a threat to life and a serious medical situation. Preserved the Latvian source, IDs, answer codes and branching. Source integrity, frozen Latvian parity, source adapter, locale catalogs and full offline HTML build passed. Reviewer package remains at S07. Next: M10_15–M10_28.

### 2026-11-08 · S08 checkpoint 2 · M10_15–M10_28

Reviewed the remaining 14 questions of module 10. Corrected day-count units, the rolling-month label, elapsed duration, and persistent difficulties with closeness versus sexual intimacy. Clarified the distinction between the respondent's actions and the actions of others. Preserved Latvian source, IDs, options and branching. Source integrity, Latvian parity, source adapter, locale catalogs and full offline HTML build passed. S08 is at 28 of 48 questions. Next: modules 35, 41 and 42. Reviewer package remains at S07.

### 2026-11-08 · S08 complete · modules 35, 41 and 42

Reviewed the final 20 questions, completing all 48 in S08. Corrected the grief day count, timing of difficulties after an event, the distinction between observing oneself and being observed, and episodes around falling asleep or waking rather than difficulty sleeping. Preserved the Latvian source, IDs, answer codes and branching. Source integrity, frozen Latvian parity, source adapter, locale catalogs, full HTML build and Chromium offline journey passed. Inspected all 48 S08 records in the build and checked the corrected wording at the artifact boundary.

Repository reviewer HTML: SHA-256 `54aec5d8b8477d959031001b1ede5c5babb533921676ba89f72ab708c7a3fd2c`. The existing trilingual PDF guide remains applicable. The owner copies the HTML to the shared Drive folder. Next: S02.

### 2026-11-08 · S02 checkpoint 1 · module 02

Reviewed 21 questions in module 02. Preserved the first nine legacy screening records in all languages. The source and reuse conditions for named instruments still need confirmation before a translated release. Corrected elapsed duration boundaries, the day-count answers, concurrent events versus causal claims, and low mood versus a diagnosis of depression. Preserved all Latvian records, IDs, answer codes and branching. Source integrity, frozen Latvian parity, source adapter, locale catalogs and full offline HTML build passed. Reviewer package remains at S08. Next: module 05.
