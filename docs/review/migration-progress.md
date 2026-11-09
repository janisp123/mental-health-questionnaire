# Execution ledger — four-language main migration

Plan: `docs/superpowers/plans/2026-11-09-four-language-main.md`. Owner approved execution and main promotion on 9 November 2026.

- Task 1: complete. Main history reconciled at 89c5e38; develop docs preserved by a normal merge. Six archive-file hashes and immutable source verification pass.
- Ruling: preserve original legacy `downloads/` paths as explicitly historical links, rather than moving them, to avoid breaking existing file URLs. They are excluded from the current build/package.
- Pre-flight: tasks 2/4 share default-bundle locale expectations; update source-fidelity tests separately from active-language tests. Task 3/5 share current package names and manifest metadata. Task 6 tests the combined source tree before main promotion.
- Tasks 2–6: pending.
- Task 2: complete. Default four-language CLI, immutable-source audit/adapter and translation-pack tests pass. Candidate profiles are historical; no question/runtime semantics changed.
- Task 3 builder: complete. Three package CLI tests pass. Ruling: PDF invariant timestamps use ReportLab's deterministic mode; ZIP timestamps use buildEpoch. Both are recorded explicitly, with pinned fonts/dependency.
