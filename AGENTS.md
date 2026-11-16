# Project working rules for AI development

These rules apply to future development work in this repository, particularly long or multi-file tasks.

## Resume before starting

- Read `docs/WORK_CHECKPOINT.md` first when present. It records the last verified section, exact next action, local-versus-remote synchronization state and outstanding blockers. Then consult the referenced section audit/test evidence and `docs/CHANGELOG.md`.
- A local checkpoint does not imply that changes reached GitHub or Drive. State the actual synchronization status, and never restart completed sections solely because the chat history is missing.
- Keep `docs/WORK_CHECKPOINT.md` limited to current product/package pointers, applicable verification, actual synchronization, blockers and one next action. Put earlier completion narratives in the changelog/history and link them; do not append successive release summaries to the active checkpoint. Preserve an exact historical copy before a substantial checkpoint rewrite.

## Shared TD-list handoff (ChatGPT and Codex)

- **One canonical list:** Both agents read and write only `docs/TD_LIST.md` in this repository, with the latest remote `main` as the source of truth. Always fetch/refresh `main` before reading or modifying it; do not rely on a local checkout, cached response, historic `develop`, other project, or an unmerged feature branch as the current TD list.
- **Before adding or changing a task:** Read current `main`, check whether the request is already present/completed, and inspect any open TD-related pull requests that could carry a pending change. Avoid duplicates or overwriting concurrent updates; coordinate with an existing PR when applicable.
- **Write path:** Do not push directly to protected `main`. Create or update a short-lived branch based on fresh `main`, change the canonical TD file there, open a PR targeting `main`, wait for required checks, then merge through the allowed PR workflow. Never bypass branch protection or silently choose a conflicting resolution.
- **Publication proof:** A TD edit is **DONE** only after the PR is merged **and** the exact requested text is fetched back from `docs/TD_LIST.md` on remote `main`. Report the verified path and merge PR/commit. Until then say **PENDING PR** (and give its URL/branch), not “saved to the TD list.” If checks or permissions block merging, report **BLOCKED**, with the precise blocker.
- **Cross-agent read:** Codex should fetch latest remote `main` at the beginning of a TD session. If an owner-mentioned task is absent, check open TD PRs before declaring it missing. A pending PR is a proposed change, not an official task on `main`; do not independently implement it unless the owner has explicitly authorized that work and all project gates allow it.

## Pending TD work and conflicts

- `docs/TD_LIST.md` on **main** is the sole active backlog of owner-approved tasks for later Codex implementation. `docs/FUTURE_IDEAS.md` is not a task list and `docs/CHANGELOG.md` records completed work. Do not add new tasks to historical `develop`.
- When explicitly asked to work through TD, read the current `docs/WORK_CHECKPOINT.md` and relevant code/release instructions first. Before implementation, compare each task with active work, latest `main`, existing features, other TD tasks, release gates, privacy/safety rules and any pending unsynchronized changes.
- **If material conflict, ambiguity or overwrite risk exists, stop that task and explain the precise conflict, impact and safe alternatives to the project owner; wait for a decision before changing implementation or deciding how to reconcile the conflict.** Keep the task pending. Do not silently override the checkpoint, merge/rewrite branches, or publish an unapproved release.
- If a task is already complete or obsolete, report the evidence and avoid repeating it. Unrelated clearly safe, already authorized tasks can proceed.
- For non-conflicting tasks, follow the main-based short-lived branch and checked-PR workflow. Record finished changes in the changelog and remove the corresponding TD task only after verification. TD updates alone do not start background work.

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

- `main` is the sole active four-language source. Start short-lived feature/fix branches from current main; use checked PRs to integrate. Older develop/candidate branches are historical. Read `docs/FEATURE_DEVELOPMENT.md` for stable module/data contracts.
- Before significant edits, inspect the relevant parts of `docs/FILE_INDEX.md`, `project-manifest.json`, and the active entry at the end of `docs/CHANGELOG.md`. Do not load or print those whole files by default.
- Work on one module and language at a time wherever possible. Preserve original IDs, answer codes, validation logic and backup compatibility.
- Do not silently modify the current four-language Google Drive review package, the frozen v16 reference baselines, or the original Drive archive. Follow `docs/RELEASE_POLICY.md` for deliberate, readback-verified reviewer updates.
- Never publish questionnaire responses or identifiable patient information to this public repository.
- EN, RU and UK translations remain drafts until human review and release-gate requirements are satisfied.
- Do not claim an untested feature, translation or release passed verification.
- When user-facing questionnaire text or behavior changes, prepend a dated entry to notesHistory and an aligned, very brief plain-language entry to notesBriefHistory in all active locales (currently LV/EN/RU/UK) together and retain the latest ten entries. The displayed brief entries use actual DD.MM.YYYY dates; retain truthful detailed records in source history. Use Riga local time and verify the visible text and all active catalogs before committing.
- Before editing user-facing wording or translations, read `docs/LANGUAGE_STYLE_GUIDE.md` and apply its LV/RU/EN/UK address and tone conventions. Preserve frozen source question content unless explicitly asked to edit the question bank.

## Durable public descriptions

- Public app descriptions, footer, README, landing-page body/metadata and repository summaries use “over 700 questions in more than 10 sections” or its localized equivalent. Avoid exact question/section totals in promotional prose. Keep exact counts in technical manifests, tests, release evidence and actual progress indicators. Recheck that the broad thresholds remain true when changing the bank/layout.

## Audience and privacy in update notes

- Use “multilanguage” or its localized equivalent in current public-facing descriptions, sharing text, README and landing page instead of a fixed language count. Language selectors and technical inventories may list the actual supported locales. Historical archives retain their original text.

- The application's `notesHistory` is for patients and doctors. Include only concise descriptions of changes relevant to using the questionnaire, guide or reports.
- Keep employer/portfolio/career goals, repository presentation or settings, branch/CI logistics, AI development workflow and private project coordination out of the application's update list and downloadable guide.
- Repository-only maintenance does not require an in-app update entry or a new reviewer package. Do not add an app entry announcing this rule or a cleanup of private information.
- Public repository logs may record neutral technical outcomes. Do not copy private conversations, prompts, personal motives or owner decisions into public files unless explicitly authorized for publication. Permission to implement a request is not permission to publish the conversation behind it.
- Before publishing, read the actual update notes in every active locale and confirm they fit the intended audience. A keyword scan alone is insufficient; preserve unrelated clinical and privacy wording.

## Attribution and creator-credit preference

- Keep accurate AI/Codex implementation attribution in repository documentation only. Do not add authorship/AI-assistance disclosures to the downloadable questionnaire UI, user guide, reports or their metadata.
- In the app footer, keep the short GitHub link immediately after “made by Janis Paegle” and before the year. Preserve localized accessible labels, deliberate HTTPS navigation, no-referrer and noopener/noreferrer. Do not duplicate the source link in About or insert it into clinician answer reports.
- This preference concerns product attribution; do not edit frozen question content or remove unrelated research/clinical wording based on a keyword search.

## Review package and document output

- The public README and GitHub Pages download action must link only to the stable Google Drive review folder, which contains both HTML and PDF. Use one download link per page; no separate PDF button, raw GitHub artifact download or individual Drive-file download link. Keep opening instructions aligned and version independent. Technical source/provenance links are not download actions.
- A separate “Open questionnaire” action may launch the same verified package HTML at the stable Pages `/questionnaire/` route. Never maintain a second application source. Website publication must verify parity with the recorded Drive distribution; release follow-up commits include `docs/review/checks/*-drive-sync.json` to refresh the hosted copy automatically after Drive readback. Do not publish an unverified newer package ahead of that record.
- Public download names are `Mental_Health_Questionnaire_v<version>.html` and `Mental_Health_Questionnaire_Guide_v<version>.pdf`, with the version immediately before the extension. The optional ZIP is `Mental_Health_Questionnaire_Package_v<version>.zip`. Do not add internal numeric prefixes, question counts, language lists or build-status suffixes to these public filenames; retain accurate technical-review status in the manifest/docs.
- Every delivered change to the app, guide or download package gets a new shared release version, reflected in both filenames, the manifest, changelog and current checkpoint. Internal work steps and documentation-only updates use exact Git commit checkpoints in the changelog; do not repeatedly republish identical downloads for those records. Preserve original names in historical archives.
- Choose document formats for the intended reader and delivery channel; do not assume a file called `README` should be Markdown.
- A professional-review package contains the self-contained questionnaire HTML and a concise, readable PDF guide. Keep editable Markdown source in the repository or private project documentation; do not put it in the reviewer folder unless requested.
- The downloadable four-language PDF guide contains HTML download/browser-opening instructions and a concise privacy/medical-purpose notice: the app does not collect or send data, helps prepare for a medical visit rather than diagnose, and only a medical professional may interpret the answers. Keep all four language sections aligned. Do not add GitHub links, AI attribution, version/review-status statements or other project information to this guide. Keep technical status documented accurately in the repository.
- Before sharing a PDF, render it and inspect the page visually at normal reading size. Check that text is legible, page breaks are clean, and the instructions match the current build and button labels.
- Keep the reviewer folder limited to the current files intended for reviewers. After replacing a deliverable, verify the folder contents and update its current-state/archive index so filenames and formats agree.
- The user tests the current questionnaire from the Google Drive review folder. After every verified implementation batch intended for user testing, rebuild the HTML and matching PDF from the verified main-based source commit, deliberately replace the Drive files in place for a reviewer distribution update, and verify both uploaded files by readback before handing off. Do not defer Drive refresh until a major release.
- Clearly label technical review status and limitations. Never imply clinical validation, human translation review, or device testing that has not happened.

## Keep each work session focused

- Read the active changelog checkpoint with `tail` or a narrow line range. Search older history with `rg` only when the current task depends on it. Preserve the existing task ID and exact next action in handoffs.
- Query only the relevant `current_versions` fields from `project-manifest.json`; avoid printing the full imported-file hash inventory. Run `tools/verify_project_index.py` when source/index integrity is affected or specifically required.
- Start with focused tests. Run `python tools/run_checks.py` for shared runtime, locale or source-data changes. Build with `python tools/build_review_package.py --output-dir dist/review-<version>` and verify with `python tools/verify_review_package.py <folder> --with-zip`; the package refuses existing output directories. Explicit `--load-mode memory` is a documented managed-browser fallback, never proof of file/device testing.
- For CI, inspect run status and failed step summaries first. Fetch logs for the failing step when available; fetch complete job logs only if the failure cannot be diagnosed from that step.
- Avoid repeating successful checks after documentation-only edits. Record the exact commit, verification performed, any unverified areas, and one next action in the changelog.
