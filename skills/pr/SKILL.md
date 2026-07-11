---
name: pr
description: "Commit, push, and open a pull request. Use when finished work on the current branch needs to become a PR."
user-invocable: true
argument-hint: "[optional: PR title, base branch, or draft|ready]"
---

# PR

1. If still on the default branch, create or switch to a task branch first.
2. Commit intended changes with a Conventional Commit subject. Stage only intended files.
3. Before writing the PR body, read the repo's PR template if one exists. Check `.github/pull_request_template.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `pull_request_template.md`, `docs/pull_request_template.md`, and `.txt` variants. If a `PULL_REQUEST_TEMPLATE/` directory exists under `.github/`, the repo root, or `docs/`, pick the template named by the repo or user; otherwise use the default template if present.
4. Push and open the PR, ready for review by default, draft only when asked or the work is known incomplete. Title reads like a commit subject: in squash-merge repos it becomes the commit on the default branch.
5. Write the body from the template when one exists. Preserve headings and fill relevant sections from the diff and work done: what changed and why, ticket link when one exists, checks run with results, review issues fixed, and anything not checked. If no template exists, write a concise body with those same details.
6. Report the PR URL.

## Rules

- One PR per branch. If one is open, push and update it. Preserve human edits to the body: update only what the new commits change.
- Follow the repo's PR template when one exists.
- Never claim checks that did not run.
- If push or PR creation fails, keep the work local and report the exact failure.
