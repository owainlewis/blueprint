---
name: pr
description: "Commit, push, and open a pull request. Use when finished work on the current branch needs to become a PR."
user-invocable: true
argument-hint: "[optional: PR title, base branch, or draft|ready]"
---

# PR

1. If still on the default branch, create or switch to a task branch first.
2. Commit intended changes with a Conventional Commit subject. Stage only intended files.
3. Push and open the PR, ready for review by default, draft only when asked or the work is known incomplete. Title reads like a commit subject: in squash-merge repos it becomes the commit on the default branch.
4. Write the body from the diff: what changed and why, ticket link when one exists, checks run with results, anything not checked.
5. Report the PR URL.

## Rules

- One PR per branch. If one is open, push and update it. Preserve human edits to the body: update only what the new commits change.
- Follow the repo's PR template when one exists.
- Never claim checks that didn't run.
- If push or PR creation fails, keep the work local and report the exact failure.
