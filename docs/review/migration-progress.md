# Execution ledger — four-language main migration

Plan: `docs/superpowers/plans/2026-11-09-four-language-main.md`. Owner approved execution and main promotion on 9 November 2026.

- Task 1: complete. Main history reconciled at 89c5e38; develop docs preserved by a normal merge. Six archive-file hashes and immutable source verification pass.
- Ruling: preserve original legacy `downloads/` paths as explicitly historical links, rather than moving them, to avoid breaking existing file URLs. They are excluded from the current build/package.
- Pre-flight: tasks 2/4 share default-bundle locale expectations; update source-fidelity tests separately from active-language tests. Task 3/5 share current package names and manifest metadata. Task 6 tests the combined source tree before main promotion.
- Initial Tasks 2–6 entry was pending; completion checkpoints follow below.
- Task 2: complete. Default four-language CLI, immutable-source audit/adapter and translation-pack tests pass. Candidate profiles are historical; no question/runtime semantics changed.
- Task 3 builder: complete. Three package CLI tests pass. Ruling: PDF invariant timestamps use ReportLab's deterministic mode; ZIP timestamps use buildEpoch. Both are recorded explicitly, with pinned fonts/dependency.
- Tasks 3–5: complete. Clean-source package/source verification, PDF visual/text review and immutable-source checks pass. All 28 scripts pass in memory mode; the maintained layout sweep renders 5,696 cases. Current docs/manifest distinguish repository v0.2.2 from Drive v0.2.1 until update.
- Task 6: complete. PR #2 merged as 1a68d31f385208263be79de5da8c27e3df90354a after both GitHub workflows passed at head 505187b. Merge tree equals checked tree. Both Drive readbacks match the exact v0.2.2 pair, with IDs/sharing preserved. PR #1 is closed as superseded. Distribution snapshot tag: review/v0.2.2.
- Final review: important package-verifier gap reproduced. Three negative tests failed for stale runtime, stale guide, and invalid HTML/PDF pairing. Exact full-HTML and regenerated-PDF comparisons plus one-of-each enforcement make all six package tests pass. Active FILE_INDEX/develop instructions and Ukrainian checkpoint header corrected. No app runtime/source-question changes were required.
