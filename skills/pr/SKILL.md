---
name: pr
description: "Commit, push, and open a pull request with a clear description. Use when finished work on the current branch needs to become a PR."
user-invocable: true
argument-hint: "[optional: PR title, base branch, or draft|ready]"
---

# PR

Take the finished change on the current branch to an open pull request.

## Workflow

1. Run `branch` first if still on the default branch.
2. Run `commit` for any uncommitted intended changes.
3. Push the branch.
4. Open the PR with `gh` or GitHub tools. Draft by default; ready only when the user or ticket policy asks. Write the title like a commit subject: in squash-merge repos it becomes the commit on the default branch.
5. Write the body from the diff and the work actually done, not from memory: what changed and why, ticket link when one exists, tests and checks run with results, review findings fixed, and anything not verified. A reviewer should be able to judge the change without reading the conversation.
6. Report the PR URL.

## Rules

- One PR per branch. If one is already open, push and update its description instead of opening another. Preserve human edits to the body: update only what the new commits change, never rewrite the whole description.
- Follow the repo's PR template when one exists.
- Do not claim verification that did not run.
- If push or PR creation fails, keep the branch and commit local and report the exact failure.
