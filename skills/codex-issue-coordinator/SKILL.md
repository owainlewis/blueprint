---
name: codex-issue-coordinator
description: "Coordinates a large batch of GitHub issues through separate Codex worker threads, tested pull requests, review loops, and gated merges. Use when the user asks one Codex thread to manage several coding sessions or complete a parent issue, milestone, or issue batch."
user-invocable: true
argument-hint: "<parent issue, milestone, or issue list>"
---

# Codex Issue Coordinator

Use one Codex thread as the coordinator. Give each active GitHub issue its own
Codex worker thread, worktree, branch, and pull request. Keep implementation
context in workers and dependency state in GitHub.

Explicitly naming `/codex-issue-coordinator`, or explicitly telling the
coordinator that agents may merge, authorizes in-scope workers to merge their
own pull requests after every merge gate below passes. An implicit skill match
does not grant merge authority: run in no-merge mode unless the user's words
grant it.
Neither mode authorizes deployment, release publication, destructive
operations, branch-protection bypasses, or changes outside the supplied batch.

## Preconditions

1. Read the repository instructions, parent issue, native sub-issues, declared
   dependencies, project board, issue state, and linked open or merged pull
   requests. A merged pull request is only evidence of completion when it
   closes or explicitly references the issue and its final change and proof
   satisfy the issue scope. Reconcile that issue and project state instead of
   dispatching it again. Do not infer completion from a link alone.
2. Use Codex thread tools. If visible Codex threads and Codex-managed worktrees
   are unavailable, stop. Do not replace workers with hidden subagents.
3. Make every issue a complete task before dispatch. If a missing product or
   technical decision could change behavior, data, security, compatibility,
   operations, cost, or proof, mark that issue as needing human input.
4. Build a dependency graph. Treat GitHub as the durable source of issue, pull
   request, review, and merge state. Stop for human correction if the graph
   contains a dependency cycle. Do not create a second local tracker.
5. Default to two active workers. Use another limit only when the user asks or
   the repository gives a stricter limit.

## Coordinator workflow

1. Keep the calling thread as coordinator. Name it `#<parent> Coordinator` when
   the batch has a parent issue. Use `set_thread_pinned` to pin it at the start
   of every new or resumed coordinator run, before inspecting or dispatching
   workers.
2. Reuse an existing active worker for the same issue. Inspect an unclear or
   interrupted worker before creating another. If the issue already has an
   open pull request, create or resume its worker on that pull request's exact
   head branch and include the branch and pull request URL in its prompt.
   Otherwise create a Codex project thread in a managed worktree from the
   latest remote default branch and include the required new branch name.
3. Name every worker `#<issue-number> <short title>`.
4. Start only issues whose prerequisites are merged. Independent issues may
   run together up to the worker limit. Do not stack dependent branches in
   this workflow.
5. Give the worker the full issue URL, dependency state, repository location,
   resolved branch and pull request state, and the worker contract below. Tell
   it to use `/task-to-pr` and pass the coordinator's explicit merge or
   no-merge mode. Merge mode grants authority only for that worker's issue.
6. Monitor workers with compact `wait_threads` snapshots. Use `read_thread`
   only when a worker needs help. Send decisions or corrected scope back with
   `send_message_to_thread`; do not edit the worker's files from the
   coordinator.
7. Continue independent work when one issue is blocked. After three failed
   attempts at the same check or review finding, pause that issue, record the
   evidence on GitHub, and request human input.
8. In merge mode, when a worker reports completion, verify GitHub says the pull
   request is merged, the issue contains final proof, and the issue is closed.
   Close it explicitly if the merged pull request did not close it. Then mark
   the issue Done when the project supports it and archive the worker thread.
   In no-merge mode, stop that worker after its pull request passes all
   agent-completable gates, leave the issue in Review, record any pending human
   approval or merge as its blocker, and leave the thread available.
9. Refresh the dependency graph after every merge and dispatch newly ready
   issues from the updated remote default branch. In no-merge mode, when a
   dependent issue is waiting only for a passing prerequisite pull request to
   be merged, record that human-merge dependency as its blocker. Do not wait
   indefinitely or dispatch the dependent from an unmerged branch.
10. In merge mode, finish only when every in-scope issue is merged, closed, and
    Done when the project supports that state, or every unfinished issue has a
    recorded blocker that needs human action. In no-merge mode, finish when
    every in-scope issue has a ready pull request with all agent-completable
    gates passing or a recorded human blocker.

## Worker contract

Each worker owns one issue and follows this order:

1. Read the issue, repository instructions, relevant design, code, tests, and
   dependency pull requests. Move the issue to In Progress when possible.
2. Use the Codex-managed worktree. If the issue has an open pull request, reuse
   its exact head branch and pull request. Otherwise create the repository's
   required issue-linked branch from the updated default branch.
3. Implement only the issue. Add or update tests for every acceptance
   criterion, affected failure path, regression risk, and named edge case.
4. Use `/test`. Browser-facing work requires a real browser check of the
   affected success and failure flows, responsive widths, keyboard behavior,
   console errors, and failed requests when relevant.
5. Commit and push the tested change. Open a draft pull request if one is not
   already open. Include a short summary and current proof.
6. Mark the pull request ready for review and move the issue to Review. Do this
   before requesting independent review or waiting for GitHub review.
7. Use `/review` with a fresh subagent that did not implement the change. Wait
   for required CI and automated review. In merge mode, also wait for every
   repository-required approval. In no-merge mode, do not wait indefinitely
   for human feedback; record a pending required approval as a human blocker.
8. Address every valid in-scope finding. Reply to review threads with the fix
   or evidence for making no change. Resolve a thread only when it is fully
   addressed.
9. After any code change, repeat affected `/test` proof and fresh `/review`,
   commit and push, update the pull request evidence, and wait for CI and
   automated review again. Iterate until the mode's gates pass; do not
   manufacture extra rounds or wait indefinitely for optional human feedback.
10. In merge mode, merge the pull request using the repository's preferred
    method after every merge gate passes. Never use an admin bypass. Wait until
    GitHub reports the pull request as merged, record final proof, and verify
    the issue is closed. Close it explicitly if the pull request did not. In
    no-merge mode, leave the passing pull request open for a human to merge.
    Report the final state to the coordinator.

## Merge gates

A worker may merge only when all of these are true:

- The pull request is ready for review, not draft.
- The complete issue scope and acceptance criteria have recorded proof.
- Focused and required wider tests pass on the final commit.
- A fresh `/review` verdict is `Approve` on the final code.
- Every required GitHub check passes.
- Every actionable automated or human review thread is resolved.
- Every repository-required approval is present.
- The pull request is mergeable and current with its required base.
- No security, data-loss, compatibility, operational, or product decision is
  unresolved.
- The pull request changes only the worker's issue.

If a gate cannot pass, do not merge. Record the blocker and continue other
independent work.

## Worker prompt

Use this shape and replace every placeholder:

```text
Use /task-to-pr to complete <issue URL> in this Codex-managed worktree.

Your thread owns only this issue, branch, worktree, and pull request.
Branch state: <reuse PR head branch and PR URL, or create new branch name>.
Delivery mode: <merge after all gates pass, or leave the passing PR open>.
Read the issue and repository instructions as the source of truth.
Implement the smallest complete change and prove acceptance criteria, edge
cases, failure paths, and regressions.

After local proof passes, commit, push, open or update the pull request, and
mark it ready for review. Only then run fresh independent /review and wait for
CI and GitHub review. Address valid findings and repeat test and review after
every code change.

<If merge mode: The user explicitly authorized this /codex-issue-coordinator run to
merge this issue's pull request after every merge gate passes. Wait until
GitHub reports the merge, update and close the issue, and return the result.>
<If no-merge mode: Leave the passing pull request open for human merge and
return its URL and proof.>
Do not deploy, publish a release, bypass repository rules, or change unrelated
work.
```

## Boundaries

- Use visible Codex threads for workers. Fresh subagents are only for the
  independent `/review` inside a worker.
- Never dispatch two workers for one issue or let two workers share a worktree.
- Never replace or duplicate an existing pull request for the issue. Resume it.
- Reconcile already-merged pull requests and closed issues before dispatch,
  but only after their change and proof satisfy the issue scope.
- Never start dependent work from an unmerged pull request in this workflow.
- Never merge an unrelated pull request merely because it blocks the batch.
- Never infer deployment or release authority from merge authority.
- Do not archive a worker until its merge and final issue state are verified.
