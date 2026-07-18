---
name: implement
description: "Turn one ticket or task into a PR ready for human merge: create missing GitHub issues with gh when available, isolate, implement, test, review, publish, and handle feedback."
user-invocable: true
argument-hint: "<ticket, task description, or open PR> e.g. 'LIN-123', 'add retry limits', or 'PR #42'"
---

# Implement

1. Resolve the input as an existing ticket, a task description, or an open PR to resume. Capture the goal, acceptance criteria, checks, constraints, and PR rules. For an open PR, use the live PR and linked context as the source of truth; do not create a ticket only to resume it. For a new task with no ticket, search for an existing issue, then use `gh issue create` with this context when `gh` is available and authenticated. If not, continue with the task description as the source of truth and disclose that no ticket was created. Stop for missing product decisions, secrets, permissions, or unrelated work bundled together.
2. Inspect the repo, remotes, default branch, worktrees, and open branches or PRs for the task or ticket. Resume existing work. Otherwise fetch and create a dedicated branch and worktree from the latest remote default branch, named with the ticket ID when available or a short task slug otherwise. Work only in that worktree.
3. Mark the ticket in progress when one exists and the tracker supports it. Make the smallest complete change. Add or update tests for changed behavior and docs for user-facing changes. If a useful test is impractical, explain why and verify manually.
4. Run focused checks first, then wider checks when shared or user-facing behavior changed. For browser-facing work, run `browser-verify` to exercise main and failure flows at desktop and mobile sizes, checking layout, console errors, and failed requests. If no real-browser path is available, stop and report the blocker unless the user explicitly accepts a documented manual check. Fix relevant failures without expanding the task.
5. Have a fresh subagent or reviewer inspect every non-trivial diff, using the separate `code-reviewer` agent when installed. Judge each finding, fix valid in-scope issues, and rerun affected checks. If no fresh reviewer is available, stop and report the blocker unless the user explicitly accepts a documented exception.
6. Check every acceptance criterion and record proof. Unmet required criteria block the PR.
7. Commit only intended changes with a Conventional Commit subject and ticket ID when available. Push and open one PR ready for review. Include the ticket link or task reference, summary, acceptance proof, checks, review status, and anything not verified.
8. Wait for checks and review feedback. Inspect reviews, unresolved threads, comments, mergeability, and required checks. Classify feedback as actionable, disputed, resolved, outdated, informational, or needs-human. Fix important in-scope items; push back only on factual or technical disputes with a concrete reason, and route preference disagreements to the human reviewer. Re-check, push, and reply on each addressed thread with what changed. Repeat until required checks pass and no actionable feedback remains, nothing new arrives after a reasonable wait, or a human decision is needed. A later invocation resumes the same PR.
9. Update the ticket with the PR and proof and move it to the closest review state when a ticket exists. Otherwise report the same handoff in chat. Report the source, base, branch, worktree, PR, checks, review, and blockers. Leave the worktree for later feedback.
10. Leave merging to a human unless the user explicitly asks for merge. With explicit permission, merge only after required checks and review are clean, then update the ticket and remove the worktree.

## Rules

- One task, one branch, one worktree, one PR, and one ticket when a tracker is available. Use separate workers for several independent tasks.
- Do not create a duplicate delivery path when a branch, worktree, or PR already exists.
- New work starts from the latest remote default branch unless the task explicitly depends on unmerged work.
- Do not open a PR with failing relevant checks or unmet required criteria unless the user asks for an early draft; disclose the gaps.
- Do not hide unchecked work, overwrite user changes, or expand the task for nice-to-have feedback.
- Do not claim ready while required checks fail or actionable feedback remains.
- Preference disagreements from a human reviewer need human judgment, not an agent rebuttal.
- Keep failed work intact and report exactly what blocked it.
- If the task, spec, or plan is wrong, stop and update the source of truth before continuing.
