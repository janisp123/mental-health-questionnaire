# TD list

This is a **running list of tasks requested for later**, especially when Codex usage is available. Add new tasks here when the project owner asks. This file is **not a changelog**, progress diary, or archive of completed work.

- Keep entries short, actionable, and unchecked until verified.
- When a task is finished, remove it from this list and record the implementation details in `docs/CHANGELOG.md`.
- The current in-progress action and handoff stay in `docs/WORK_CHECKPOINT.md`. Future possibilities that are **not** approved tasks stay in `docs/FUTURE_IDEAS.md`.

**Preflight rule for Codex:** Before starting a TD task, compare it with current work, project rules, release gates, and other TD tasks. If it conflicts or might overwrite work, **report the exact conflict and safe options to the owner and wait for their decision before implementing that task**. Do not silently resolve or bypass the conflict. Leave blocked items unchecked.

## To do

- [ ] **Add the project's GitHub link to the in-app project information and the trilingual PDF user guide.**
  - Link: https://github.com/janisp123/mental-health-questionnaire (current working code: `develop`).
  - Add a small, localized source-code/development link in the app's project information (LV, EN, RU).
  - Update the maintained trilingual reviewer-guide source and regenerate the guide PDF with a clickable link.
  - **Do not** add the link to the patient's/doctor's answer report PDF or modify frozen reference files.
  - Keep the non-diagnostic disclaimer; opening GitHub must require a deliberate click and must not transmit answers.
  - Verify links, translations, offline operation, PDF appearance, and relevant automated tests before marking complete.

- [ ] **Bring `main` up to date and make GitHub presentable to potential IT employers.**
  - Review the differences between `develop` and `main`; promote the most recent **verified, stable** project state to `main` instead of leaving the main branch on the older Latvian v16 snapshot.
  - First pass the relevant automated checks and release safeguards; resolve branch divergence carefully without losing current release files, history or ongoing work. Keep active experimentation on `develop`.
  - Update the main README so a visitor immediately understands the purpose, screenshots/demo or how to try the offline app, technical stack, architecture, tests, AI-assisted development role, and honest status/limitations. Link to the technical documentation and development history.
  - Improve repository presentation (clear description, sensible topics, current instructions and a tidy file layout) without adding misleading professional or clinical validation claims.
  - Preserve privacy protections and do not call an unreviewed translation or clinically unvalidated questionnaire a medically approved release. If a release gate is not met, document the blocker and publish only an explicitly labeled review/portfolio state when appropriate; do not silently claim a final public release.
  - Verify the resulting `main` branch, links and build, record the completed work in `docs/CHANGELOG.md`, then remove this item from the TD list.
