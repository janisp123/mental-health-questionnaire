# TD list — pending tasks for Codex

**Single source of truth:** `docs/TD_LIST.md` on `main`. Add approved tasks here when the project owner asks; Codex may implement them when explicitly instructed. The list is **not** a changelog or a record of completed work.

- Before acting on a task, read `AGENTS.md`, `docs/WORK_CHECKPOINT.md` and relevant project/release rules, and check whether the task is still necessary.
- **Conflict check:** Compare each TD request against the current `main` product, active work, other queued tasks, existing changes, safety/privacy rules and release gates. If anything conflicts or could overwrite existing work, **explain the conflict, consequences and safe options to the owner *before implementation***. Do not choose a resolution silently. Leave that task pending until the owner decides.
- If a task is already completed or outdated, do not repeat it; report evidence and clarify whether it should be removed.
- For non-conflicting, authorized work: use a short-lived branch from current `main`, verify changes, and follow the project PR/release workflow. After a task is implemented and verified, remove it from TD and record the result in `docs/CHANGELOG.md`.
- Unapproved possibilities belong only in `docs/FUTURE_IDEAS.md`. TD edits do not by themselves start Codex.

## To do

- [ ] **Update the GitHub repository About description and topics — blocked by integration permissions.**
  - App/PDF source links and README portfolio improvements are completed and verified in main via PR #7; do not repeat them. Completion and Drive readback evidence is in the changelog.
  - Description and topic edits were attempted using the authenticated GitHub API. Both returned **HTTP 403: Resource not accessible by integration**; repository settings were not changed.
  - Requires the repository owner to edit About manually, or an integration with the appropriate repository-settings permissions. Do not mark complete until metadata readback confirms the change.
  - Proposed description: “Free offline pre-appointment questionnaire in Latvian, English, Russian and Ukrainian. HTML/CSS/JavaScript, Python tooling and automated tests. Technical-review project; not a diagnostic tool.”
  - Proposed topics: `offline-first`, `questionnaire`, `mental-health`, `javascript`, `python`, `multilingual`, `playwright`, `github-actions`, `ai-assisted-development`.

## Already resolved during branch migration (not a pending task)

The former TD request to bring `main` up to date for employers has already been substantially fulfilled by the verified v0.2.2 four-language promotion and updated main README. It was **not** carried over as unfinished work. Any further portfolio improvements should be raised as a new, specific TD request.
