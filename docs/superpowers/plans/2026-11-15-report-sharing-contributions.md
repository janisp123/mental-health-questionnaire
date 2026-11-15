# Report actions, sharing and contributions

Approved scope: report-page New questionnaire with confirmation; Share questionnaire opens public-link sharing/copy controls, never answer/report/progress/feedback data; restore always-visible Contributions on the first page even without names; use multilanguage wording rather than fixed language counts. Clinician report keeps every provided choice (including No, Never, uncertain and refused), omits only skips/unanswered, replaces covered/skipped statistics and long coverage text with provided-answer count and a brief omission explanation. Empty clinician reports offer return/reset/share without printing an empty PDF. All active locales align; question IDs/content/scales/conditions and recovery remain frozen.

Execution: inline using existing runtime/screens and a focused public-only sharing module. Native sharing is feature-detected; copying and selectable text remain available after unavailable/rejected APIs. No automatic transmission, HTML/report attachment or tracking. Contributor names require consent; no private email is displayed.

- [x] Add focused report/screen/runtime regressions and observe relevant failures.
- [x] Implement provided-answer report, reset/share controls, public-only delivery and contributions; align locales/current public copy and release notes.
- [x] Run focused and full checks, inspect report/share/empty/first-page layouts and PDF, obtain independent review.
- [ ] Commit clean source, build/archive/version v0.2.12, merge required checked PR, publish Pages wording and replace same Drive IDs; verify readback.
- [ ] Merge delivery records with actual source, CI, deployment and Drive hashes.

Keep existing summary/section progress counts unchanged. Frequency wording and unrelated TD remain deferred. Existing saved progress retains every record. Native device share-sheet behavior on physical phones remains unverified unless actually tested; synthetic API checks must be labelled.
