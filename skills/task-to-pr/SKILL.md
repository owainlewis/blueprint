---
name: task-to-pr
description: "Turns explicit ticket references into draft or ready-for-review PRs. Use when the user passes tickets such as JIRA-123, LIN-123, a GitHub issue number or URL, a Linear issue, or a short ticket list, and wants code written, tests added, fresh subagent review, fixes applied, and a PR opened. The outer delivery loop — it owns branch and worktree creation, the PR, and ticket updates. Use implement when the workspace is already prepared and no PR is expected."
user-invocable: true
argument-hint: "<ticket reference or list> e.g. JIRA-123, LIN-123, github#456, https://github.com/owner/repo/issues/456"
---

# Task To PR

Turn user-provided tickets into PRs. The user supplies the ticket reference or list; do not hunt
for work by labels or backlog queries unless the user explicitly asks for backlog management.

Examples:

```text
task-to-pr JIRA-123
task-to-pr LIN-123
task-to-pr github#456
task-to-pr https://github.com/owner/repo/issues/456
task-to-pr LIN-123, LIN-124
```

The core promise is: fetch the ticket, move it to in progress, understand the acceptance criteria,
write the code, add or update tests, verify the change, get a fresh subagent review, fix valid
findings, open a PR, then move the ticket to a review status.

## Workflow

### 1. Resolve The Ticket

Treat each argument as an explicit ticket reference. Resolve it using the best available source:

- GitHub issue number or URL: use GitHub tools or `gh` to read the issue, comments, linked PRs, and
  relevant labels only as context.
- Linear issue key or URL: use Linear tools when available, or ask for the missing context if the
  ticket cannot be fetched.
- Jira issue key or URL: use Jira tools when available, browser/authenticated CLI if available, or
  ask for the ticket content if the ticket cannot be fetched.
- Plain text task: treat the text itself as the ticket source.

Capture the problem statement, acceptance criteria, relevant comments, linked designs, requested
verification, and any explicit PR policy such as draft vs ready for review. If the ticket is
unclear, already has an open PR for the same work, requires secrets or product decisions, or spans
multiple unrelated changes, stop and report the blocker.

If the tracker supports status updates, move the selected ticket to the existing in-progress state
before writing code. Prefer an exact `In Progress` state when available; otherwise use the closest
available active-work status. Leave a short comment saying work has started. Do not create workflow
states, labels, or tracker conventions. If the status cannot be changed, keep working only when the
ticket content is clear, and report the status update failure.

### 2. Prepare The Branch

Work from a clean repository state. Inspect `git status`, current branch, remotes, and existing
worktrees before editing. Do not overwrite, discard, or stage unrelated user changes.

For each ticket, create a traceable branch name from the ticket ID and a short slug, prefixed with
the repository's normal branch prefix when one exists. Use one branch per ticket unless the user
explicitly asks for a combined PR.

When multiple tickets are provided:

- Run independent tickets in separate worktrees when full-session subagents or worker threads are
  available.
- Run dependent or overlapping tickets sequentially.
- Stop dependent tickets when an earlier ticket fails or changes shared assumptions.

If a clean branch or worktree cannot be created, stop before implementation and report the exact
reason.

### 3. Implement The Ticket

Read the relevant code and tests before editing. Make the smallest complete change that satisfies
the ticket. Follow the repository's existing patterns, helpers, framework conventions, and style.

Add or update tests whenever behavior changes, a bug is fixed, an interface changes, or an edge
case is introduced. Prefer tests that prove the ticket's acceptance criteria instead of broad
snapshot or smoke coverage.

Run the focused tests for the changed area first, then the wider project checks that are practical
for the repo. If the ticket names specific verification commands, run those. Fix failures caused by
the change; report unrelated failures clearly.

### 4. Review With A Fresh Subagent

Use a fresh review subagent or separate agent context to review the diff before opening the PR.
The reviewer should check:

- Correctness against the ticket and acceptance criteria.
- Missing, weak, or misleading tests.
- Broken interfaces, migrations, permissions, security issues, or edge cases.
- Unrelated changes or accidental formatting churn.

Judge every finding. Fix valid in-scope issues, rerun the relevant checks, and request another
review pass when the fixes are non-trivial. If no subagent capability exists, perform a careful
self-review and say in the PR/report that independent review was unavailable.

### 5. Open The PR

Stage only intended files. Create one clear commit for the ticket unless the repo has a different
local convention. Push the branch and open a PR with GitHub tools or `gh`.

Open a draft PR by default. Mark it ready for review only when the user requested ready-for-review
behavior or the ticket policy clearly requires it. Do not merge unless the user explicitly asks.

The PR body should include:

- Ticket link or reference.
- Summary of the change.
- Acceptance criteria status.
- Tests and checks run.
- Review method and valid findings fixed.
- Anything not verified or any known follow-up.

After the PR is created, update the source ticket when the tracker supports it:

- Comment with the PR link, a summary of the change, and the verification evidence: tests and
  checks run with their results, browser or manual verification when relevant, and any known risks
  or follow-ups. The ticket should read as a complete record of what happened without opening the
  PR.
- Move the ticket to a suitable existing review state. Prefer `In Review` when available; otherwise
  use the closest available review/PR state such as `Review`, `Code Review`, `PR Open`, or
  `Ready for Review`.
- Do not add or remove labels unless the user or repository policy explicitly says to.

Verify the final ticket status after updating it. If the status update fails, leave a comment with
the PR link when possible and include the failure in the run report.

If push or PR creation fails, keep the branch and commit local, then report the missing remote,
auth, command, or tool capability.

### 6. Report

Finish with a concise run report:

- Ticket reference and source.
- Branch, commit, and PR URL.
- What changed.
- Tests and checks run.
- Review findings fixed, or why independent review was unavailable.
- Tracker updates made.
- Anything blocked or not verified.

## Rules

- The user supplies the ticket; do not select work by labels, queues, or backlog searches by
  default.
- Treat the ticket as the audit trail: clear comments, verification evidence, and links, so a
  teammate can follow the work without reading the diff.
- One ticket maps to one branch and one PR unless the user explicitly asks for a combined PR.
- Keep unrelated local changes intact.
- Do not invent tracker states, labels, issue links, or acceptance criteria.
- Update ticket status as work progresses: move to in progress before coding, then to the best
  available review status after opening the PR.
- Add or update tests for meaningful behavior changes.
- Use a fresh subagent review when available, and fix valid in-scope findings before opening the
  PR.
- Open PRs only after verification has run, or clearly state what could not be verified.
- Stop and ask or report a blocker when the ticket needs credentials, secrets, paid services, or
  product, architecture, or security judgment not already answered in the ticket.
- Pause at the opened PR. Merging, extended CI triage, and post-review follow-up are separate work
  unless the user explicitly asks for them.
