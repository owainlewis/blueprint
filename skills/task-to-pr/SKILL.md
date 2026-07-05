---
name: task-to-pr
description: "Turn one ticket into a PR that is ready for review, with code, tests, review, acceptance checks, and proof."
user-invocable: true
argument-hint: "<ticket reference> e.g. JIRA-123, LIN-123, github#456, https://github.com/owner/repo/issues/456"
---

# Task To PR

Goal: turn one ticket into a PR that is ready for review, or explain why it cannot be done.

## Workflow

1. Resolve the ticket. Capture the problem, acceptance criteria, background, and PR rules. Stop if it is unclear, already has a PR, spans unrelated work, or needs missing secrets or decisions.
2. Prepare an isolated workspace. Inspect `git status --short`, protect unrelated changes, and use a dedicated branch or worktree with the ticket ID when available.
3. Implement the smallest complete change. Add or update tests. Update docs or generated-doc sources when behavior, config, public functions, commands, routes, or user-facing flows change.
4. Check locally. Run focused tests first, then wider checks when shared behavior changed. Do not open a PR with failing relevant checks or missing acceptance criteria unless the user explicitly asks for an early draft.
5. Ask another agent or reviewer to review the code before PR. Fix real issues about this ticket and re-check. If no other reviewer is available, self-review for obvious issues, but do not push or open a PR unless the user explicitly accepts that limitation.
6. Separately check each acceptance criterion against the ticket. Treat missing or partly done required criteria as things that block the PR. Fix real blocking issues and re-check.
7. Commit intended changes with a Conventional Commit subject, include the ticket ID when available, push, and open a PR ready for review. Use draft only when the user explicitly asked for an early or incomplete PR. The PR body must include ticket link, summary, acceptance status, check results, and review status.
8. After opening the PR, wait for checks and review feedback available during this run. Fix actionable feedback as it arrives, re-check, and push updates. Stop when checks pass, no current actionable feedback remains, feedback has not arrived after a reasonable wait, or a human decision is needed.
9. Update the ticket with PR link and proof, then move it to the closest existing review state when accessible.
10. Report ticket, branch or worktree, commit, PR URL, checks, review feedback handled, and anything blocked or unchecked.

## Boundaries

- One ticket, one branch, one PR. For a list of tickets, split the work into one separate worker per ticket.
- Do not merge. After the PR opens, handle checks and review feedback that arrive during the run. Long-running review watching is separate unless the user asks for it.
- If a coordinator or goal is watching the PR, report the PR and proof instead of polling inside this workflow.
- Prefer worktrees when the current checkout has local changes, is risky, is already in use, or will run without a human present.
- Do not open a PR with known failing relevant tests or missing required acceptance criteria unless explicitly asked to create an early draft, and disclose the failure clearly.
- Do not expand the task because review, checks, or a bot suggested a nice-to-have refactor.
- If a status update, push, or PR creation fails, keep the work local when safe and report exactly what failed.
- Keep branches and worktrees intact on failure; do not clean them up unless the user asks.
- Runs without a human present report through the ticket, not chat. When blocked, comment proof, apply the documented needs-human label, release any claim label, and exit cleanly.
