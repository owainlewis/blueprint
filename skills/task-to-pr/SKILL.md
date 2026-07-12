---
name: task-to-pr
description: "Turn one ticket from GitHub, Linear, Jira, or pasted context into a tested and reviewed GitHub pull request in a dedicated branch and worktree."
user-invocable: true
argument-hint: "<ticket reference or pasted ticket>"
---

# Task To PR

Turn one ticket into one PR. Never merge.

1. Read the ticket and linked context. Capture the goal, acceptance criteria, checks, constraints, dependencies, and ticket ID. Ask for pasted ticket text when its tracker is unavailable. Stop if the work still needs a decision or mixes unrelated outcomes.
2. Check for an existing branch, worktree, or PR and resume it. Otherwise fetch the remote, create a short ticket-named branch from the latest remote default branch, and attach a dedicated worktree. Keep the original checkout untouched. Use a task slug when no ticket ID exists.
3. Implement the smallest complete change. Add or update tests for changed behavior and important failures. Update documentation when user-facing behavior, interfaces, commands, or configuration change.
4. Run focused checks, then wider checks when the change affects shared behavior. For browser-facing work, exercise the main flow and failure states in a real browser at desktop and mobile sizes; check layout, console errors, and failed requests.
5. Give the ticket, diff, tests, and check results to a fresh reviewer. Fix valid in-scope findings and rerun affected checks. If no reviewer is available, self-review and disclose it.
6. Check every acceptance criterion and record proof. Unmet criteria or failing relevant checks block a ready PR.
7. Commit intended files with a Conventional Commit that includes the ticket ID when available. Push and open a ready GitHub PR with the ticket link or reference when available, why, summary, acceptance proof, checks, review result, and risks. Open a draft only when asked.
8. Handle actionable feedback and checks that arrive during the run. Update the source ticket with the PR and proof when possible; otherwise report the same handoff in chat.

Keep one ticket, branch, worktree, and PR. If given several tickets, ask the user to choose one. Do not add agent attribution. Keep work intact and report the blocker when access, dependencies, or required decisions prevent completion.
