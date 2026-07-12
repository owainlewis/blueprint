---
name: task-to-pr
description: "Turn one ticket from GitHub, Linear, Jira, or complete pasted context into a tested and reviewed GitHub pull request in a dedicated branch and worktree."
user-invocable: true
argument-hint: "<ticket reference or pasted ticket>"
---

# Task To PR

Move one ticket as far as possible toward a reviewed PR. Resume existing work instead of creating duplicates. Never merge.

## Resolve

1. Read the ticket and every linked source. Use the available tracker integration for GitHub, Linear, or Jira. If the tracker is unavailable, ask for the complete ticket text.
2. Capture the outcome, context, acceptance criteria, verification, boundaries, dependencies, and ticket ID. Normalize a source ID for Git names, such as `123` or `LIN-123`. If pasted work has no ID, derive a stable `LOCAL-<short-slug>` from its title and treat the current chat as its record. Stop when decisions, acceptance criteria, usable verification, permission, or secrets are missing.
3. Inspect the repository, remotes, worktrees, branches, and open PRs. A merged PR means complete. An open PR or existing branch means resume that work.
4. Confirm dependencies have landed. Do not start from unmerged work unless the ticket explicitly requires it.

## Workspace

1. Fetch the remote. For new work, create `<ticket-id>-<short-kebab-summary>` from the latest remote default branch and attach a dedicated worktree.
2. Never include an agent name or prefix in the branch. Never implement in the caller's checkout.
3. Reuse the same branch, worktree, and PR for follow-up work on this ticket.
4. Keep one ticket, branch, worktree, and PR. Preserve unrelated changes. Keep the worktree after opening the PR; remove it only after merge or an explicit request.

## Implement And Verify

1. Mark the ticket in progress when its tracker supports it.
2. Make the smallest complete change that satisfies the ticket. Follow established project patterns.
3. Write or update tests for changed behavior and important failure paths. For a bug, reproduce it and add a regression test first when practical. For a refactor, run focused tests before and after.
4. Update documentation when commands, configuration, interfaces, or user-visible behavior change.
5. Run focused checks first, then wider checks when shared or user-facing behavior changed. Fix relevant failures without expanding scope.

For browser-facing work, use a real browser. Exercise the main flow and failure states at desktop and mobile sizes. Check forms, navigation, overflow, overlap, clipping, readable text, console errors, and failed requests. Capture useful evidence. Never expose cookies, tokens, or stored credentials.

## Review Gate

Give a fresh reviewer the ticket, acceptance criteria, diff, tests, and verification results. Use this prompt:

```text
Review this change without editing it. Read the ticket and acceptance criteria,
then read the tests before the implementation. Try to disprove the change.
Check correctness, failure paths, security boundaries, interfaces, regressions,
scope, unnecessary complexity, and whether tests prove the requested behavior.
Report only blocker and important findings. For each finding give the exact
location, impact, evidence, and fix direction. End with approve or request changes
and state anything you could not verify.
```

Fix valid in-scope findings and rerun affected checks. Re-review when a fix materially changes behavior or design. If no independent reviewer is available, perform the same structured review yourself and disclose that in the PR.

## Acceptance Gate

Check every acceptance criterion against the final code and record concrete proof. Required criteria, relevant checks, browser flows, and review must pass before a ready PR opens. If the ticket is wrong, update it before continuing.

## Commit And PR

- Stage only intended files.
- Use a Conventional Commit and include the ticket ID: `type(scope): summary (<ticket-id>)`.
- Use the repository's PR title convention, or the same format as the commit when none exists.
- Push and open one PR ready for review. Open a draft only when the user explicitly asks for incomplete work.
- Follow an existing PR template. Otherwise use the template below.
- Never add agent attribution or a co-author line.
- Never claim checks or review that did not run.

```markdown
## Ticket
<ticket link or ID>

## Why
Why this work matters.

## Summary
- What changed.

## Acceptance
- [x] Criterion - proof

## Checks
- `command` - result
- Manual or browser check - result

## Review
- Reviewer verdict and findings fixed.

## Risks
- Anything not verified, deferred, or worth close review.
```

## Feedback And Handoff

Inspect reviews, unresolved threads, comments, required checks, mergeability, and the latest commit. Fix only actionable in-scope findings, rerun proof, push, and reply with what changed. Do not absorb optional suggestions. Stop for product, security, ownership, or risk decisions.

Update the source ticket with the PR link, acceptance proof, checks, review result, and any blocker. Move it to the closest review state when supported. For pasted work with no tracker, provide the same handoff in chat. Report the ticket, base, branch, worktree, PR, checks, review, and blockers.

If given several tickets, stop and ask the user to select one. Never combine tickets only for convenience.

## Stop Conditions

Stop without merging when work is unclear, duplicated, blocked by an unmerged dependency, missing access, repeatedly failing for the same reason, growing beyond the ticket, or waiting on a human decision. Keep all work intact and report exact evidence.
