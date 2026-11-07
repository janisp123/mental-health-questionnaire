# Translation completion implementation plan

**Goal:** Finish the interrupted EN/RU audit and produce a tested technical-review package for all 712 questions.
**Spec:** docs/CHANGELOG.md translation audit progression; docs/LANGUAGE_STYLE_GUIDE.md; AGENTS.md.
**Architecture:** Preserve the existing module/builder/runtime separation. Edit only EN/RU question strings, integrity metadata, regression coverage and review documentation. Existing LV source, IDs, codes, conditions and frozen references remain unchanged.
**Execution:** Use subagent-driven-development for one section at a time, with root coordination and verification. The fresh task-specific clone on develop is the isolated workspace. Do not recreate work from completed checkpoints.

## Tasks
- [ ] Reproduce S13 failure, repair metadata, establish working local Python/browser tools.
- [ ] Review and verify S13 (70 questions).
- [ ] Review and verify S12 (42 questions).
- [ ] Review and verify S14 (49 questions).
- [ ] Review and verify S15 (47 questions).
- [ ] Review and verify S07 (45 questions).
- [ ] Review and verify S08 (48 questions).
- [ ] Review and verify S02 (38 questions).
- [ ] Review and verify S03 (40 questions).
- [ ] Review and verify S04 (44 questions).
- [ ] Review and verify S05 (36 questions).
- [ ] Final independent review, full regression, built HTML and PDF visual verification, Git/Drive readback.

## Per-section completion contract
Read every question and option in LV/EN/RU for the selected section; correct demonstrable meaning, time-frame, grammar and respectful-address defects. Record IDs and rationale. Check original LV and nontranslation fields against starting commit 85f4332. Update source SHA256 and Git blob/byte indexes. Run source/index/build and full browser checks, inspect embedded translations, commit a durable changelog checkpoint before advancing. Never equate technical checks with human or clinical validation.

## Review focus
Preserve negation, onset boundaries, frequency/duration units, sensitive-question meaning, and answer-option intent. Preserve safety answer mappings and backup compatibility. Verify Unicode and offline rendering on Windows as well as CI.

## Execution ledger
- Baseline: 85f4332, five sections previously verified; S13 committed but CI source-integrity check fails.
- Local baseline: Git autocrlf converted checkout text to CRLF, causing a separate local hash failure; restore exact repository bytes before comparing with CI.
- Ruling: continue using the fresh dedicated clone on develop, as required by AGENTS.md; no additional worktree needed.
- Distribution blocker: no Drive tools exposed in this session and the in-app browser previously returned a session error. Prepare and verify local deliverables while attempting access; do not claim upload without readback.
