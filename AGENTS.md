# Project working rules for AI development

These rules apply to future development work in this repository, particularly long or multi-file tasks.

## Progress updates — visible to the user

- While actively working, send a brief user-visible progress message **approximately once per minute**, even if there is no major milestone. When practical, send updates more frequently (about every 20 seconds) during lengthy tool operations.
- Use a clear, short update such as **"Still working — finished 2/5 sections; checking translations next."**
- Show actual progress and the next step. If nothing changed, say **"Still working — no new checkpoint yet; currently checking X."**
- Report blockers immediately. Do not hide errors, imply that work was finished, or repeat a meaningless success message.
- At every durable completed batch, record the exact Git commit or file checkpoint in `docs/CHANGELOG.md` before starting the next batch. Mark completed stages only after readback and verification.
- If the conversation or tool execution ends, **do not claim that monitoring or development continues in the background**. A chat assistant cannot guarantee a timed heartbeat, predict usage limits, or send messages once it is no longer actively running.
- At the end of a work period, clearly state **DONE / PARTIAL / BLOCKED**, what changed, what remains, and the exact next action.
- If a task is interrupted, the GitHub changelog should make it possible to continue without rereading unrelated files.

## Development safety and source of truth

- Work on `develop`, not `main`, unless an approved release is being published.
- Read `docs/FILE_INDEX.md`, `project-manifest.json`, and `docs/CHANGELOG.md` before significant edits.
- Work on one module and language at a time wherever possible. Preserve original IDs, answer codes, validation logic and backup compatibility.
- Do not silently modify the public Google Drive Latvian release, the frozen v16 reference baselines, or the original Drive archive.
- Never publish questionnaire responses or identifiable patient information to this public repository.
- EN and RU translations remain drafts until human review and release-gate requirements are satisfied.
- Do not claim an untested feature, translation or release passed verification.
