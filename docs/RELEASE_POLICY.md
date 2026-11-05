# Release gate — FAIL CLOSED

**Policy exists, but full automated CI enforcement is NOT yet implemented.** Do not infer readiness from this document alone.

1. JavaScript/HTML syntax checks alone are never a sufficient release test.
2. Require actual passing **structural checks**: 48 sections / 712 question IDs (until formally changed), stable IDs and answer codes, valid conditional graph, safety semantics, and backup version/schema compatibility.
3. Require actual passing **critical behavior tests**: start/save/next, one-at-a-time questions, selection not autosaving, skip/resume, multi-select exclusivity, recovery download/import, language switching preserving answers, doctor/AI exports, A4 printing, sensitive prompts and fully offline Android Chrome.
4. Require actual **translation checks** in LV/EN/RU for questions, answers, navigation, reports, filenames and documentation. No missing strings or unmarked mixed-language fallback. Standardized tools and clinically important safety language receive appropriate human review.
5. Store real test reports with case, status, tested build SHA256, tester/tool, time and evidence. Unknown, missing or failed results mean BLOCKED. Never fabricate test PASS records.
6. Before a **professional-review candidate** is shared, all required nonclinical tests must pass and it must clearly identify itself as an unvalidated review project.
7. Before any claim of **clinical validation/approved clinical public release**, separately require appropriate qualified human clinical and safety review, plus human release approval. Automated tests cannot establish clinical validity.
8. Publishing requires an explicit promotion step after successful checks, a tagged commit, reproducible artifact and rollback copy.
9. Freeze the review/public candidate until planned releases, except documented critical hotfixes that still pass the gate.
10. Never commit users' questionnaire results or recovery files. The HTML must not transmit answers without explicit user action.

Existing working policy and evidence checker in the Drive archive must be reconciled and imported. Do not say CI is active until an actual workflow is added, executed and tested for failing outcomes.
