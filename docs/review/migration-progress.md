# Execution ledger — four-language main migration

Plan: `docs/superpowers/plans/2026-11-09-four-language-main.md`. Owner approved execution and main promotion on 9 November 2026.

- Task 1: complete. Main history reconciled at 89c5e38; develop docs preserved by a normal merge. Six archive-file hashes and immutable source verification pass.
- Ruling: preserve original legacy `downloads/` paths as explicitly historical links, rather than moving them, to avoid breaking existing file URLs. They are excluded from the current build/package.
- Pre-flight: tasks 2/4 share default-bundle locale expectations; update source-fidelity tests separately from active-language tests. Task 3/5 share current package names and manifest metadata. Task 6 tests the combined source tree before main promotion.
- Tasks 2–6: pending.
