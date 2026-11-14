# Current working checkpoint

Updated 14 November 2026. Main is the sole active application source.

## Product and distribution

- Source v0.2.5, LV/EN/RU/UK, 712 questions, 48 frozen source modules, 15 optional sections. Technical review only; human language/clinical review and physical-phone/email-client tests remain pending.
- Feedback implementation PR #21 is merged as `217a777ce874207d65b5a1022bf1d57aa3d37a99`, with tree equal to checked head `4c52ef2d6f38f6fcdfc982621e8785f88f163a83`. All 30 local checks pass in labelled memory mode. PR CI passed with real offline file opening.
- Drive has the verified v0.2.5 HTML and matching PDF at the existing IDs/folder/sharing. Both downloaded byte-identical. Guide PDF bytes unchanged. Evidence: [Drive readback](review/checks/2026-11-14-feedback-drive-sync.json).
- HTML includes the dated feedback patch note in all four locales, ten entries per locale. Send feedback opens a deliberate email draft; Copy feedback/manual selection provides fallback; questionnaire answers remain excluded. No actual email was sent during testing.
- Package built from clean main source `217a777ce874207d65b5a1022bf1d57aa3d37a99`. Manifest: [current branch package](../MH_Public_version/manifest.json). Prior exact pair is archived at `archive/four-language/v0.2.4-guide-medical-purpose/`.

## Integration boundary and next action

Drive publication is complete. Repository package/README/changelog/synchronization records are on `release/feedback-0.2.5`, PR #23. Full/app CI on checked package head `63fb13e43d1067064abe9dd8723532215d1f367c` passed (43600760165 / 43600760248). Automatic approval review rejected merging the package into public main until explicit integration approval. Main still has the older repository download pair despite its updated app source; do not mistake that for an uncompleted Drive update or repeat uploads.

Next action: obtain explicit approval to merge PR #23 and integrate the checked publication record. Subsequent documentation-only verification does not require another Drive upload. Discovery PR #22 remains an unpublished preview. Frozen-help conflict, wording/audit fixes, human review and settings access remain separate pending decisions; consult [TD](TD_LIST.md). About description/topics writes still return HTTP 403.
