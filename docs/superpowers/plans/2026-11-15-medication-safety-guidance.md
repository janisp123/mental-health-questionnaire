# Medication and Safety Guidance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Clarify existing medicine entry and help users find separate safety questions without changing answers or navigation.

**Architecture:** Keep frozen questions intact. Add narrowly validated localized `help` to M14_02/M02_09 after language packs load, using the existing question-help renderer. Correct existing medicine UI instructions and labels in each active locale. Release v0.2.14 through the existing checked PR/package/Drive workflow.

**Tech Stack:** Python builder/validation, JSON locale catalogs, existing JavaScript screens/reports, Playwright/PDF checks.

**Spec:** Approved focused-audit proposals 1 and 2, captured in Scope below. Optional general-context question is explicitly deferred.

## Scope and global constraints

- Medicine instruction: “Copy the information from the package if you can. If you are unsure, write ‘I don’t know’ rather than guessing.” Strength label: “Medicine strength and form, if known”. Clarify dose changes explicitly in the existing changes field.
- Optional M14_02 help: “What improved, stayed difficult, or changed? If relevant, include feeling less emotion, sleepiness, or fatigue. Note when you noticed changes—for example after starting a medicine, changing the dose, or before the next scheduled dose. You do not need to know the cause.”
- Optional M02_09 help: “These thoughts can mean different things. If you want to describe them in more detail, the ‘Wellbeing, safety and unusual experiences’ section asks separately about wishing to be dead, self-harm and suicidal intent.” Use each locale’s actual section title.
- Preserve every original question ID/title/choice/code/condition/order, all 712 questions, recovery schema/medicine keys, report inclusion/priority and support behavior. No new clinical question, score, dose advice or automatic section selection.
- All active locales: LV/EN/RU/UK. Formal address according to LANGUAGE_STYLE_GUIDE; translations remain draft. Prepend patient-facing notes, retaining latest ten; no private coordination in public logs.
- Shared release 0.2.14; keep version-ending filenames, single stable Drive-folder download action and unchanged guide content. Preserve prior pair and stable Drive file IDs/sharing; read back both bytes before claiming delivery.

## Review focus

- Negative/uncertain/refused answers retain original report meaning; help is never an answer.
- Optional safety section remains optional and its name matches the hint in each locale.
- Missing/empty/extra-locale guidance fails build rather than silently dropping a language.
- Current No medication answer still permits past medication records; field keys/backups remain compatible.
- Long guidance remains readable at 320/390px and causes no network requests.

### Task 1: Guidance and localized wording

**Files:** new `src/questionnaire/appointment-guidance.json`; `tools/build_questionnaire.py`; medicine/UI catalogs under `src/app/i18n/` and `translations/uk/`; `src/questionnaire/build.json`; existing source-preservation tests; focused `tests/full_bank/test_appointment_guidance.py` and runtime guidance test.

**Interfaces:** Input existing normalized bundle; output only two added translation `help` fields. Reuse existing `QuestionnaireScreens.question` and shared report/recovery interfaces unchanged.

- [ ] Add/run focused failing regression for guidance presence and original answer/report contracts.
- [ ] Add strict narrow help overlay; edit locale catalogs one language at a time; bump source to 0.2.14 and add aligned change notes.
- [ ] Verify focused tests plus synthetic runtime/print/save compatibility; record evidence in changelog and commit/push checkpoint.
- [ ] Run full maintained checks once after focused checks; obtain one fresh branch review; fix material findings with regressions.

### Task 2: Reviewed package and delivery

**Files:** archive previous pair, new `MH_Public_version/` pair/manifest, README current pointer, project manifest, concise checkpoint/changelog and delivery evidence.

**Interfaces:** Consume clean verified source commit; output checked v0.2.14 pair and actual Drive readback record.

- [ ] Commit clean source; build/verify unique `dist/review-0.2.14` and inspect guide/clinician output.
- [ ] Preserve v0.2.13, stage current pair/README/manifest and push checked PR; wait for exact-head CI and merge authorized update.
- [ ] Replace same Drive IDs, preserving folder/sharing; read back both files and compare bytes; create version snapshot.
- [ ] Record exact commits/hashes/CI/readback, reconcile active TD only where warranted, and leave one precise next action.

## Resume ledger

- Start: base `6032f999587532e1e709cda85a4b5b8a04d7b437`; no product edits yet. Current distribution remains v0.2.13. Execute Task 1 first.
- Execution: use current clean checkout on a dedicated short-lived branch; avoid an unnecessary second checkout. Changelog and this checklist are the durable ledger; push checkpoints so recovery does not depend on the current machine/chat.
