---
name: task-to-pr
description: "Turn one ticket into a draft PR. Use when the user passes a ticket reference (JIRA-123, LIN-123, github#456, an issue URL) and expects code, tests, review, and a PR. Use implement when no PR is expected; use multitask for several tickets at once."
user-invocable: true
argument-hint: "<ticket reference> e.g. JIRA-123, LIN-123, github#456, https://github.com/owner/repo/issues/456"
---

# Task To PR

Turn one user-provided ticket into a draft PR. The user supplies the ticket; do not hunt for work by labels or backlog queries. Treat the ticket as the audit trail: a teammate should be able to follow the work without reading the diff.

## Workflow

1. **Resolve the ticket.** Fetch it from GitHub, Linear, or Jira; treat plain text as the ticket itself. Capture the problem, acceptance criteria, linked context, and any explicit PR policy. Move it to the closest existing in-progress state and comment that work has started. Stop and report if the ticket is unclear, already has an open PR for the same work, spans unrelated changes, or needs secrets or decisions it does not answer.
2. **Run `branch`.** Start from a clean tree. Never overwrite or discard unrelated local changes.
3. **Run `implement`** with the ticket as the task. The acceptance criteria are the definition of done.
4. **Run `review`** with a fresh subagent. Judge every finding, fix the valid in-scope ones, and re-verify. If no subagent capability exists, self-review and say so in the PR.
5. **Run `pr`.** The body must include the ticket link and acceptance criteria status.
6. **Update the ticket.** Comment with the PR link and the verification evidence, then move it to the closest existing review state. Do not invent tracker states or labels.
7. **Report:** ticket, branch, commit, PR URL, verification run, and anything blocked or unverified.

## Boundaries

- One ticket, one branch, one PR. For a list of tickets, use `multitask`.
- Pause at the opened PR. Merging, CI triage, and post-review follow-up are separate work; use `pr-to-ready` when feedback arrives.
- Open PRs only after verification has run, or state clearly what could not be verified.
- If a status update, push, or PR creation fails, keep the work local when safe and report exactly what failed.
