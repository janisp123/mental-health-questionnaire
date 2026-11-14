# Helpline reassurance implementation plan

> **For agentic workers:** Use superpowers:executing-plans for this single text-only task, with one fresh whole-branch review before integration.

**Goal:** Make the shared helpline guidance approachable before the existing short opening phrase.

**Architecture:** Extend only each locale's existing `supportBody`; footer, manual Support and answer-triggered cards already share it. Preserve the runtime and all question/recovery contracts. Build and deliver the next technical-review package after verification.

**Tech Stack:** JSON locale catalogs, existing JavaScript renderer, Python/Playwright verification and package tooling.

**Spec:** The helpline reassurance task in `docs/TD_LIST.md`, selected for implementation. No prepared speech; listening/help without judgment; possible specialist/local-support suggestions; ask about confidentiality before personal disclosure.

## Global constraints

- LV/EN/RU/UK meanings stay aligned with formal address per `docs/LANGUAGE_STYLE_GUIDE.md`.
- Keep urgent local-emergency guidance first, trusted-local-service search instructions and the existing opening phrase.
- No universal anonymity, secrecy or referral guarantee; no new network calls.
- Preserve all question IDs, choices, time windows, conditions, answers and recovery schema. Frequency-wording work stays deferred.
- Update dated in-app notes in all four catalogs, retaining ten entries. Follow normal checked PR and Drive exact-byte readback workflow; existing offline copies require a new download.

## Review focus

- Four translations communicate the same qualified support/confidentiality message.
- Manual, footer and answer-triggered support display the complete new text after urgent guidance.
- Longer text stays readable at phone widths and does not hide navigation.
- Existing saved answers, feedback and recovery survive unchanged.
- Repo and Drive contain the same verified package; guide bytes remain unchanged if its source does not change.

## Task 1: Update, verify and distribute shared support wording

**Files:** Modify `src/app/i18n/ui.{lv,en,ru}.json`, `translations/uk/ui.json`, `src/questionnaire/build.json`; update current package, archive, README and delivery documentation after verification.

**Interfaces:** Existing `strings.supportBody` and `strings.notesHistory`; no new runtime interface. Keep the existing `supportLinks(true)` consumers and answer storage intact.

- [x] Read all four current support paragraphs and existing support tests; confirm the source branch starts at current main.
- [x] Insert the aligned reassurance immediately before the opening phrase; prepend patient-relevant notes and set v0.2.8. This is a reversible prose change: use direct copy review and existing tests, without adding tests that duplicate the prose.
- [x] Run existing support/source checks and `QUESTIONNAIRE_BROWSER=/usr/bin/chromium python tools/run_checks.py --load-mode memory --output-dir dist/checks-helpline-reassurance`. Expected: all maintained checks pass; record memory mode separately from CI file opening.
- [x] Independently review the scoped diff; inspect all four rendered support paths and phone widths. Expected: no material issue, overlap, missing text, errors or network requests.
- [ ] Record verified source in the changelog, archive exact v0.2.7 and commit clean source; build `dist/review-0.2.8` and run `python tools/verify_review_package.py dist/review-0.2.8 --with-zip`. Expected: clean provenance and exact current-source package equivalence. Inspect guide; unchanged bytes retain prior review evidence.
- [ ] Promote the verified pair and pointers through a PR with all required checks; verify merged tree equals checked head and tag `review/v0.2.8`.
- [ ] Replace the same Drive IDs deliberately, preserving sharing/folder; download both and compare exact bytes. Expected: current HTML/PDF only and exact package hashes.
- [ ] After delivery, remove the completed helpline TD task, record checksums/commits/CI in the changelog and manifest, and update the checkpoint through a checked docs PR. Keep the deferred frequency task intact.

## Execution record

- Start: main `ffcd5e32cbc13279e96b0605fd5c00a0258e4e91`; deferred frequency wording saved by PR #34. Existing support paths share `supportBody`; no runtime edits needed.

- Source verification: 34/34 maintained checks passed in labelled memory mode; existing support checks cover footer/manual/triggered paths. Four-language support panels visually inspected at 390px, overflow checked at 320/390px. Independent review found no Critical/Important or actionable minor concerns.
