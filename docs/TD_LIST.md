# TD list — pending tasks for Codex

**Single source of truth:** `docs/TD_LIST.md` on `main`. Add approved tasks here when the project owner asks; Codex may implement them when explicitly instructed. The list is **not** a changelog or a record of completed work.

- Before acting on a task, read `AGENTS.md`, `docs/WORK_CHECKPOINT.md` and relevant project/release rules, and check whether the task is still necessary.
- **Conflict check:** Compare each TD request against the current `main` product, active work, other queued tasks, existing changes, safety/privacy rules and release gates. If anything conflicts or could overwrite existing work, **explain the conflict, consequences and safe options to the owner *before implementation***. Do not choose a resolution silently. Leave that task pending until the owner decides.
- If a task is already completed or outdated, do not repeat it; report evidence and clarify whether it should be removed.
- For non-conflicting, authorized work: use a short-lived branch from current `main`, verify changes, and follow the project PR/release workflow. After a task is implemented and verified, remove it from TD and record the result in `docs/CHANGELOG.md`.
- Unapproved possibilities belong only in `docs/FUTURE_IDEAS.md`. TD edits do not by themselves start Codex.

## To do

- [ ] **Add the public GitHub source link to the app's project information and the companion PDF user guide.**
  - Link to the repository: https://github.com/janisp123/mental-health-questionnaire (current source is `main`).
  - Add a discreet, accessible source/development link in the application's project-information/about area, with appropriate labels in **Latvian, English, Russian and Ukrainian**. Keep it out of the question flow.
  - Update the **current** four-language guide source, `docs/review/GUIDE_LV_EN_RU_UK.md` (or verified successor), and regenerate its clickable PDF link when this is implemented.
  - **Do not** put this link in the patient's/clinician's answer-report PDF; do not modify immutable references.
  - Retain the disclaimer that this is a technical-review questionnaire, not a clinically validated diagnostic test. Clicking an external link must be deliberate and must never transmit answers or introduce an automatic network request into the offline app.
  - Test link destinations, locale coverage, offline behavior and PDF readability. Use the existing build/checks and reviewer-package process; do not replace the current distributed package without the required verification and release steps.

## Already resolved during branch migration (not a pending task)

The former TD request to bring `main` up to date for employers has already been substantially fulfilled by the verified v0.2.2 four-language promotion and updated main README. It was **not** carried over as unfinished work. Any further portfolio improvements should be raised as a new, specific TD request.
