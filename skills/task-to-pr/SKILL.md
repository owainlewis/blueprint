---
name: task-to-pr
description: "Turn one ticket into a draft PR. Use when the user passes a ticket reference (JIRA-123, LIN-123, github#456, an issue URL) and expects code, tests, review, verification, and a PR. Use implement when no PR is expected; use multitask for several tickets at once."
user-invocable: true
argument-hint: "<ticket reference> e.g. JIRA-123, LIN-123, github#456, https://github.com/owner/repo/issues/456"
---

# Task To PR

Turn one user-provided ticket into a draft PR. The user supplies the ticket; do not hunt for work by labels or backlog queries. Treat the ticket as the audit trail: a teammate should be able to follow the work without reading the diff.

You are the coordinator. Use tools directly to inspect, prepare the workspace, edit, test, push, open the PR, and update the ticket. Delegate only bounded review and acceptance-verification tasks to fresh subagents; do not delegate overall coordination.

## Workflow

1. **Resolve the ticket.** Fetch it from GitHub, Linear, or Jira; treat plain text as the ticket itself. Capture the problem, acceptance criteria, linked context, and any explicit PR policy. Move it to the closest existing in-progress state and comment that work has started when tracker access and repo convention support that. Stop and report if the ticket is unclear, already has an open PR for the same work, spans unrelated changes, or needs secrets or decisions it does not answer.
2. **Prepare an isolated workspace.** Inspect `git status --short` before changing anything. Never overwrite, discard, or mix with unrelated local changes. Prefer a git worktree when the current checkout is dirty, the user is already on another task, the task is long-running, or unattended isolation would reduce risk. If using a worktree, create a new branch there from the intended base branch. If using the current checkout, require a clean tree and create a dedicated branch. Use a short descriptive branch name that includes the ticket ID when available. Stop and report if the base branch, existing branch, or dirty state is ambiguous.
3. **Run `implement`** with the ticket as the task. The acceptance criteria are the definition of done. Keep changes narrow. Add or update tests with the code. Update docs or generated-doc sources when behavior, configuration, public APIs, or user-visible commands change. The review and acceptance steps below belong to this PR loop.
4. **Verify locally.** Run the narrowest relevant tests first, then broader checks when shared behavior, public APIs, generated docs, or user-visible flows changed. If behavior changed, require tests or explicitly record why tests were not practical. Do not proceed to PR with known failing relevant tests or missing required acceptance criteria unless the user explicitly asked for an early draft with disclosed failures.
5. **Run `review`** with a fresh subagent. Judge every finding, fix valid in-scope blockers, and re-verify. If no subagent capability exists, self-review and say so in the PR.
6. **Run acceptance verification** with a separate fresh subagent. Give it the ticket, acceptance criteria, current diff, and verification run. Ask it to mark each acceptance criterion as satisfied, partial, missing, or not verifiable. Treat missing or partial required criteria as blockers. Fix valid blockers and re-run relevant verification.
7. **Repair loop.** Repeat implementation, local verification, review, and acceptance verification until the work is clean or blocked. Do not loop indefinitely; after repeated failed attempts, stop, leave the branch/worktree intact, and report the blocker with evidence.
8. **Run `pr`.** Open a draft PR unless the user or repository convention says otherwise. The body must include the ticket link, acceptance criteria status, summary of changes, verification commands/results, and review/verification status.
9. **Update the ticket.** Comment with the PR link and the verification evidence, then move it to the closest existing review state. If the repo documents a project board or tracker field, keep it in sync with the ticket state. Do not invent tracker states or labels.
10. **Report:** ticket, workspace or worktree path, branch, commit, PR URL, verification run, and anything blocked or unverified.

## Boundaries

- One ticket, one branch, one PR. For a list of tickets, use `multitask`.
- Pause at the opened PR. Merging, CI triage, and post-review follow-up are separate work; use `pr-to-ready` when feedback arrives.
- Prefer worktrees for isolation when the current checkout is dirty, risky, unattended, or already in use.
- Do not open a PR with known failing relevant tests or missing required acceptance criteria unless explicitly asked to create an early draft, and disclose the failure prominently.
- Do not broaden scope because review, verification, or a bot suggested a nice-to-have refactor.
- If a status update, push, or PR creation fails, keep the work local when safe and report exactly what failed.
- Keep branches and worktrees intact on failure; do not clean them up unless the user asks.
- Unattended runs report through the ticket, not the chat. On a blocker, comment what blocked you on the ticket, apply the repo's documented needs-human label, release any claim label, and exit cleanly instead of waiting for input.
