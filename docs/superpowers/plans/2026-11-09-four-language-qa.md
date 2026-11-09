# Four-language QA fixes implementation plan

Goal: correct the four reproduced issues in the candidate at 9f62ed8, as requested by the owner after the audit.

Use the existing application, without changing question content, IDs, conditions or recovery format. Work on `codex/fix-four-language-qa`, based on the requested candidate rather than the older develop branch. The cloud checkout is dedicated to this task; implement inline.

- [x] Add real-browser regressions for medication widths, Russian title/flag wrapping, feedback preservation on language changes, and report-heading language. Run and observe all four failures.
- [x] Constrain medication controls and fieldset sizing; allow question titles and option text to wrap. Verify controls and flag stay within their card at 320/390 pixels.
- [x] Capture unfinished feedback before language rendering and restore it without saving it as submitted feedback or including it in recovery files. Test switching repeatedly, including editing saved feedback, and explicit submission.
- [x] Render the clinician heading using the report locale. Verify the separate feedback report remains in the interface language.
- [x] Add dated update notes in all four UI catalogs and record the audit, evidence and exact artifact in the changelog/checkpoint.
- [x] Run active app/full-bank/translation checks, using the documented in-memory browser adapter only where file navigation is blocked. Rebuild a separate four-language artifact; check PDF separation, offline behavior and the complete question layout sweep.
- [x] Review the diff, commit the fix branch, and make the changes available in GitHub without promoting main or replacing the previously shared reviewer package.

Physical-device file opening and human clinical/language review remain separate release checks.

Execution evidence is recorded in `docs/review/checks/2026-11-09-four-language-qa.json`. Integration is through a separate fix branch and draft PR; no main promotion or shared reviewer replacement.
