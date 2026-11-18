# Shared AI project protocol — v1.0

**Owner-approved 2026-11-18.** This convention governs coordination; project-specific privacy, product and release rules in `AGENTS.md` still apply.

## Fixed paths and one source of truth

- `AGENTS.md`: mandatory project instructions and constraints.
- `docs/TD_LIST.md`: the **only active backlog**; read the version on remote `main`, not an old branch, previous conversation or unmerged PR.
- `docs/WORK_CHECKPOINT.md`: latest verified state, revision, blocker and one next action.
- `docs/CHANGELOG.md`: evidence of verified completed work.
- `docs/DECISIONS.md`: owner-approved durable decisions; preserve superseding history.
- `docs/PROJECT_PLAYBOOK.md`: evidence-based lessons, not another TD list.
- `docs/AGENT_PROTOCOL.md`: this shared protocol.

## Mandatory project preflight for chat, cw and codex

Before **any project-specific action**, including reading task status, modifying TD, making code/docs changes, publishing or delegating:

1. Identify the repository. **Fetch remote `main:docs/TD_LIST.md` first.** If unavailable, report the limitation and do not act from a stale task list.
2. Read `AGENTS.md`, the current `WORK_CHECKPOINT.md`, applicable `DECISIONS.md` and relevant rules. Check latest `main` revision, implemented behavior and overlapping open PRs. A task absent from `main` may be **PENDING PR**; it is not yet recorded.
3. Confirm task ID, dependencies, authorization and conflicts. Adding a task or discussing an idea is **not** authorization to implement it. The owner approves work, sensitive changes, merges and releases.
4. For authorized writes, use a fresh main-based branch, small testable scope, a checked PR, and explicit evidence. Do not override branch protection or silently resolve conflicts.
5. After verification, record files, commit/PR, checks (PASS / FAIL / NOT RUN), remaining blockers and one exact next step. Remove completed tasks from TD only after checked integration and remote `main` readback. Distinguish local, pushed, PR, merged and deployed.

For read-only requests, do not open unnecessary branches. If an action is unavailable, state so; never assume another agent executed it.

## Vocabulary and attribution

- **Owner** = human project owner and final approver.
- **chat** = regular ChatGPT conversation. “I'll ask chat” means this, not CW or Codex.
- **cw** = ChatGPT Work, a distinct agent/workflow.
- **codex** = Codex coding agent.

For new TD items, `Added by` identifies the agent actually saving the entry (`chat`, `cw`, `codex`, or `Owner`). `Requested by: Owner` may be recorded separately. `Implemented by` requires an actual commit and verified work. Keep historical labels unchanged; do not guess who did old work. Assignment is not automatic delegation or background execution.

Keep stable task IDs and record status (TODO / IN_PROGRESS / PARTIAL / BLOCKED / IN_REVIEW / DONE) without rewriting established project-specific statuses. Handoffs include repository, task ID, branch, SHA, changed files, real test results, blockers and one next action. Cross-agent communication is only confirmed when an actual durable file/PR or explicit connector action exists.

Never put private transcripts, health answers, credentials or sensitive personal data into a public repository. Preserve the project's existing safeguards.

## Enforcement and new projects

`python tools/check_project_protocol.py` and GitHub Actions check the required structure and canonical TD location. They **cannot prove** that an agent read or understood the instructions. PRs use the preflight checklist. For future projects, create and use the dedicated GitHub template described in `docs/NEW_PROJECT_SETUP.md`; blank repositories do not inherit these files.
