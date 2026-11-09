# Project TODO — approved pending work

This is the central list of approved, pending implementation tasks on `develop`. Unlike [FUTURE_IDEAS.md](FUTURE_IDEAS.md), entries here are intended for implementation when work resumes. Do not treat them as completed without testing. Follow [WORK_CHECKPOINT.md](WORK_CHECKPOINT.md) for the current in-progress action and avoid interrupting a release-blocking test or review.

## Pending

- [ ] **Add a GitHub source link to project information and the PDF user guide.**
  - **Why:** Help clinicians, contributors, and potential employers inspect the project's source code, documentation, and development history.
  - **Link:** https://github.com/janisp123/mental-health-questionnaire (the current working code is on the `develop` branch).
  - **In-app:** Include a small, accessible, localized "Source code and development" link within the project information/about area (LV, EN, RU), not in the questionnaire question flow.
  - **PDF:** Add the clickable link discreetly to the **project/reviewer information PDF guide** in all three languages. Update the maintained Markdown source (`docs/review/README_LV_EN_RU_v0.2.0.md` or its current successor) before regenerating the corresponding PDF.
  - **Do not add** the GitHub link to the patient/clinician answer report PDF; keep that focused on the respondent's answers. Do not modify the frozen v16 references.
  - **Safety and claims:** Keep the existing disclaimer that the questionnaire is not a clinically validated diagnostic tool. Do not make the offline app automatically request the network or send user answers when it displays the link; following the external link must be a deliberate user action.
  - **Acceptance checks:** Review link text and destinations in LV/EN/RU, verify the built HTML still functions offline, render and visually inspect the PDF, run relevant checks, and record the completed work in `docs/CHANGELOG.md`. Refresh shared reviewer artifacts as required by `AGENTS.md` when the change is implemented.
  - **Status:** Pending; documentation task recorded 2026-11-09. No application or PDF changes made yet.

## Completed

Move an item here only after implementation and verification, with a reference to the changelog or commit.
