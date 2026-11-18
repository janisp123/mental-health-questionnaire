# Start a new project with the same AI-agent rules

**Permanent setup:** Create a separate GitHub repository `janisp123/ai-project-template`, populate it with the supplied minimal starter files, and enable **Settings → General → Template repository**. In GitHub use **Use this template** for each future project. A blank GitHub repository does not inherit other repositories' `AGENTS.md`.

The starter must include `AGENTS.md`; `docs/TD_LIST.md`, `WORK_CHECKPOINT.md`, `CHANGELOG.md`, `DECISIONS.md`, `PROJECT_PLAYBOOK.md`, `AGENT_PROTOCOL.md` and `NEW_PROJECT_SETUP.md`; `tools/check_project_protocol.py`; and `.github/workflows/project-protocol.yml` plus `.github/pull_request_template.md`.

On every new repository: (1) customize project name/purpose and project-specific safety rules, (2) retain all exact paths, including an initially empty TD, (3) record owner decisions and initial checkpoint, (4) run `python tools/check_project_protocol.py`, (5) check the PR workflow, and (6) optionally make its check required under branch protection.

Until the dedicated template repository exists, use the separate starter package supplied with this protocol rollout. **Do not clone an entire existing application** to start a new project. Keep protocol revisions deliberate and versioned; never overwrite project-specific rules blindly.
