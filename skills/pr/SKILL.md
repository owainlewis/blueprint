---
name: pr
description: "Commit, push, and open a pull request. Use when finished work on the current branch needs to become a PR."
user-invocable: true
argument-hint: "[optional: PR title, base branch, or draft|ready]"
---

# PR

Goal: open a pull request for the finished branch.

## Workflow

1. If still on the default branch, create or switch to a task branch before pushing.
2. Commit uncommitted intended changes with a Conventional Commit subject. Stage only intended files.
3. Push the branch.
4. Open the PR with `gh` or GitHub tools. Open it ready for review by default. Use draft only when the user asks or the work is known to be incomplete. Write the title like a commit subject: in squash-merge repos it becomes the commit on the default branch.
5. Write the body from the diff and work done: what changed and why, ticket link when one exists, tests and checks run with results, review issues fixed, and anything not checked.
6. Report the PR URL.

## Rules

- One PR per branch. If one is already open, push and update its description instead of opening another. Preserve human edits to the body: update only what the new commits change, never rewrite the whole description.
- Follow the repo's PR template when one exists.
- Do not claim checks that did not run.
- If push or PR creation fails, keep the branch and commit local and report the exact failure.
