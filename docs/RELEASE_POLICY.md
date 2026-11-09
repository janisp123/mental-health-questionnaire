# Release gate — FAIL CLOSED

**Policy exists, but full automated CI enforcement is NOT yet implemented.** Do not infer readiness from this document alone.

1. JavaScript/HTML syntax checks alone are never a sufficient release test.
2. Require actual passing **structural checks**: all 48 source modules and 712 question IDs, the configured user-facing section count (currently 15), stable IDs and answer codes, valid conditional graph, safety semantics, and backup version/schema compatibility.
3. Require actual passing **critical behavior tests**: start/section selection, one-at-a-time questions, selection not autosaving, skip/resume, multi-select exclusivity, recovery download/import, language switching preserving answers, doctor report and separate project-feedback export, A4 printing, sensitive prompts and fully offline Android Chrome.
4. Require actual **translation checks** in LV/EN/RU/UK for questions, answers, navigation, reports, filenames and documentation. No missing strings or unmarked mixed-language fallback. Standardized tools and clinically important safety language receive appropriate human review.
5. Store real test reports with case, status, tested build SHA256, tester/tool, time and evidence. Unknown, missing or failed results mean BLOCKED. Never fabricate test PASS records.
6. Before a **professional-review candidate** is shared, all required nonclinical tests must pass and it must clearly identify itself as an unvalidated review project.
7. Before any claim of **clinical validation/approved clinical public release**, separately require appropriate qualified human clinical and safety review, plus human release approval. Automated tests cannot establish clinical validity.
8. Publishing requires an explicit promotion step after successful checks, a tagged commit, reproducible artifact and rollback copy.
9. Freeze the review/public candidate until planned releases, except documented critical hotfixes that still pass the gate.
10. Never commit users' questionnaire results or recovery files. The HTML must not transmit answers without explicit user action.

Existing working policy and evidence checker in the Drive archive must be reconciled and imported. Do not say CI is active until an actual workflow is added, executed and tested for failing outcomes.


## Main-based working and distribution

Main is the single active four-language technical-review product. Feature branches merge through checked PRs. The default build enables Ukrainian and fails on an invalid/stale active pack. Source v16 references remain frozen and previous product packages are archived separately.

Run `python tools/run_checks.py`, then build and verify the matching package. For distribution, use committed relevant source (`source_dirty: false`), record source commit/tree and actual HTML/PDF/ZIP hashes, inspect the PDF, and replace existing Drive files only as a deliberate reviewer update. Preserve IDs/sharing and verify both readbacks. No automatic Drive publication occurs on ordinary commits. Tag distributed technical-review source snapshots and retain exact rollback files. Physical device checks and human language/clinical review retain their actual status.
