# Clean versioned download names

**Goal:** Publish a clearly named questionnaire and PDF guide with the shared version immediately before the extension; remove internal sequence numbers and build-detail suffixes.

**Approved names:** `Mental_Health_Questionnaire_v0.2.10.html` and `Mental_Health_Questionnaire_Guide_v0.2.10.pdf`. The optional repository ZIP follows `Mental_Health_Questionnaire_Package_v0.2.10.zip`. Subsequent delivered patches increment the shared release version and record it in changelog/manifest/checkpoint. Commit checkpoints track individual implementation/documentation steps.

**Architecture:** One filename helper in the package builder; verifier enforces that convention and the version from the embedded bundle. Preserve historical archive names and stable Drive IDs/URLs. App changes are limited to build version and latest-ten download-related notes in LV/EN/RU/UK; questions, answers, runtime and guide content stay unchanged.

- [x] Extend existing package tests to prove clean filenames and reject a prefixed current package; observe failures before the fix.
- [x] Implement shared naming, assign v0.2.10, align four-language notes and document the version/checkpoint rule. Verify focused tests and all maintained checks.
- [x] Obtain a focused independent review; commit clean source, archive exact v0.2.9, build/verify HTML/PDF/ZIP and inspect the unchanged guide render.
- [x] Promote package/README pointers through checked PR integration, preserve a review tag, replace the same Drive IDs and verify exact downloaded bytes and names.
- [x] Record delivery and update current checkpoint/manifest through a checked docs PR; keep unrelated TD and deferred wording work unchanged.

- Source verification: both original naming regressions failed before implementation, then all eight package tests passed. Added direct negative ZIP-name coverage after independent review. All 35 maintained checks passed in labelled memory mode. Independent review found no Critical/Important issue; only build version and latest-ten download-related notes change in the app data. Exact v0.2.9 archived under original names.

- Clean package: source `538427b6eb0a3dfa65be50a5b830194605a5d69e`, verified HTML/PDF/ZIP. Compared with archived v0.2.9: only embedded version and four note lists differ; all questionnaire data/runtime outside that JSON and guide PDF bytes are unchanged. Guide render visually inspected.

- Delivery: PR #40 merge `d89cb1848df11223c0e571111bb689155a7156e3`, checked head `9a277bc846e17dec90ca691f4b7b49764b813683`. Clean names, exact byte readback and unchanged IDs/folder/sharing verified. Final records are integrated through the checked documentation follow-up.
