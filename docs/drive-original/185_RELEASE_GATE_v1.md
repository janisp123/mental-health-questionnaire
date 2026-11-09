# Mandatory release gate — psychiatric pre-appointment questionnaire

**Status: POLICY ACTIVE · 2026-11-05.** This policy governs every proposed main-folder replacement, whether one multilingual HTML or the earlier separate LV/EN/RU HTML files. It does **not** certify the current drafts. The Latvian v16 reference and current EN/RU drafts remain unchanged.

## Hard rule

**A questionnaire is NOT ready to share or publish merely because the code runs, `node --check` succeeds, the HTML opens, or question totals match.** Every release candidate must first pass *all* mandatory structural, critical-behavior, translation, and safety checks, with evidence tied to the exact candidate SHA-256. Missing, pending, failed, stale, unreviewed, or ambiguous results BLOCK promotion to the main folder. No silent overrides, no inferred passes, no `TASK_DONE` before verified readback.

## Release stages

1. `DEVELOPMENT`: edit modules only, no public change.
2. `RELEASE_CANDIDATE`: freeze candidate bytes; compute SHA-256; run all tests. Do not use public file IDs for experiments.
3. `PROFESSIONAL_REVIEW_CANDIDATE`: optional limited distribution to invited professionals **only after all structural, critical-behavior, complete-translation and safety gates pass**, with a visible notice: "For professional feedback; not clinically validated; no diagnosis" and no unsupported validation claims. Clinical evaluation can be pending because that is the purpose of this phase. A human language/terminology review must be recorded to the extent performed; unresolved clinical questions must be transparent rather than falsely marked approved.
4. `PUBLIC_RELEASE`: additionally requires documented **qualified human clinical review** (scope, reviewer, date, findings, disposition) of the candidate and any safety-sensitive wording, as well as resolved critical findings and a product owner decision. Human review is necessary but does not make a nonvalidated questionnaire a validated diagnostic instrument.
5. `ARCHIVED`: preserve last good release with immutable name and checksum for rollback.

## Required groups (IDs must match the machine-readable checklist)

### Structural
- `question_bank_sections`: exact intended module/question count and schema, required fields present.
- `unique_ids_codes`: stable unique IDs, choice keys and answer statuses; no accidental changes without migration.
- `conditional_dependencies`: every referenced question, answer code and conditional target resolves; no broken/looping paths.
- `scoring_and_safety_semantics`: established scale scoring only when correctly implemented; no unauthorized risk classification.
- `offline_self_contained`: one downloadable HTML with no network/file dependencies at runtime.
- `backup_schema_compatibility`: prior response backups remain decodable or a verified migration is provided.

### Critical user behaviors — verify actual interactions, not just syntax
- `start_and_section_navigation`
- `selection_does_not_autosave`
- `save_next_and_resume`
- `conditional_branches_and_skips`
- `backup_download_and_restore`
- `language_switch_keeps_answers`
- `doctor_and_ai_exports`
- `a4_summary_and_print`
- `safety_prompts_and_help`
- `offline_android_chrome`
- `old_backup_migration`

### Translation — all three languages
- `all_questions_and_choices`
- `all_interface_buttons_navigation`
- `all_reports_exports_and_filenames`
- `instructions_legal_resources_privacy`
- `no_missing_or_unmarked_fallbacks`
- `sensitive_wording_review_recorded`

### Safety
- `no_diagnosis_or_automatic_suicide_risk_score`
- `correct_emergency_and_medical_disclaimers`
- `review_candidate_label_visible` (only required for professional-review candidates)

## Required evidence and blocking mechanism

- Create a per-candidate JSON checklist with every required test ID listed below (all initially `PENDING`); never pre-mark PASS. Use JSON keys `schema`, `mode`, `candidate_name`, `candidate_sha256`, and `tests`; each test record contains `status`, `tester`, `method`, `checked_at`, `evidence_file`, `evidence_sha256`. Use schema value `questionnaire-release-gate-1`. A final public release also requires a `clinical_review` object with documented qualified reviewer sign-off.
- Store real browser/test reports and human review notes in `03_TESTS`, then fill the evidence JSON with PASS, tester, method, UTC time, evidence file path and SHA-256 of that evidence file. Each item MUST point to existing evidence on disk and match its checksum.
- The checker's `candidate_sha256` binds evidence to the **exact HTML bytes**. Any change after testing invalidates the results and blocks release until retested.
- Run `python 186_RELEASE_GATE_CHECK_v1.py --candidate path/to/candidate.html --evidence path/to/filled-evidence.json --mode professional_review` or `--mode public_release`. A nonzero exit code means **NO RELEASE**. `--self-test` checks the gate's own refusal behavior with synthetic fixtures; it does not test the questionnaire.
- For `public_release`, include a separate signed/dated human clinical review record; a checkbox cannot replace that review. The machine checks the presence and integrity of the record, not the quality or qualifications of the clinician. Human accountability and editorial judgement remain required.
- The script verifies evidence completeness and hashes; it does **not** itself execute browsers, translate medical terms, or certify clinical accuracy. Those independent tests and reviews must actually be performed and documented.

## Release operator checklist

1. Record a task start in main `166_CHANGELOG_LV.md` **before** editing.
2. Freeze a candidate in development, keep existing public main-folder files untouched.
3. Generate fresh automated and hands-on evidence for all required tests; check language quality and every high-impact safety phrase.
4. Run the release gate and **read its decision**. On FAIL, fix in development and rerun affected checks, plus all regression checks impacted by the change.
5. For a reviewer build, visibly label it as unvalidated and distribute only after the `professional_review` gate passes. For an ordinary public release, require the separate clinical-review sign-off and `public_release` gate.
6. Archive previous published file; replace main-folder artifact only after explicit publication decision, preserving stable user links if possible; verify Drive readback and hash.
7. Record exact file ID/version/hash, performed checks, known limitations and `TASK_DONE` in changelog. During professional review, freeze the distributed version; urgent safety, data-loss or broken-button fixes may trigger a new fully checked patch release.

**Never** claim professional clinical validation, authorized translated scale wording, real Android testing or all-path coverage without actual records. Unreviewed EN/RU draft strings and current incomplete end-to-end checks must remain labeled incomplete.
