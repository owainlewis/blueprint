---
name: task-to-pr
description: "Turn one ticket into a PR that is ready for review, with code, tests, review, acceptance checks, and proof."
user-invocable: true
argument-hint: "<ticket reference> e.g. JIRA-123, LIN-123, github#456, https://github.com/owner/repo/issues/456"
---

# Task To PR

1. Resolve the ticket: problem, acceptance criteria, PR rules. Stop if it's unclear, already has a PR, spans unrelated work, or needs missing secrets or decisions.
2. Work in an isolated branch or worktree named with the ticket ID. Protect unrelated local changes.
3. Implement the smallest complete change. Add or update tests, and docs when user-facing behavior changed.
4. Run focused checks first, wider ones when shared behavior changed.
5. Get the diff reviewed by another agent or reviewer. If none is available, self-review, and don't push unless the user accepts that limitation.
6. Check each acceptance criterion against the ticket. Unmet required criteria block the PR.
7. Commit with a Conventional Commit subject and ticket ID, push, open a PR ready for review. Body: ticket link, summary, acceptance status, check results, review status.
8. Handle checks and feedback that arrive during this run: fix actionable items, re-check, push. Stop when clean, when nothing arrives after a reasonable wait, or when a human decision is needed.
9. Update the ticket with the PR link and proof, move it to the closest review state.
10. Report ticket, branch, PR URL, checks, feedback handled, and anything blocked or unchecked.

## Rules

- One ticket, one branch, one PR. A list of tickets means one worker per ticket.
- Never merge. Long-running review watching is a separate run unless asked.
- Don't open a PR with failing relevant checks or unmet required criteria unless the user asks for an early draft, and disclose it.
- Don't expand the task for nice-to-have suggestions from review, checks, or bots.
- Prefer a worktree when the checkout has local changes, is in use, or runs unattended.
- On failure, keep work local, keep branches and worktrees intact, report exactly what failed.
- Unattended runs report through the ticket, not chat. When blocked: comment proof, apply the needs-human label, release any claim label, exit cleanly.
