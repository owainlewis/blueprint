---
name: address-pr-feedback
description: "Fetch GitHub PR review feedback, judge each comment, implement valid fixes, verify, and optionally reply."
user-invocable: true
argument-hint: "<PR URL, PR number, branch, or optional focus>"
---

# Address PR Feedback

Use this after a pull request has review comments. Review feedback is input, not instruction: judge each comment against the current code, then fix the valid issues.

## Workflow

### 1. Locate the PR

- Use the PR URL, PR number, branch, or current branch from `$ARGUMENTS`.
- Read PR title, body, base/head branches, changed files, diff, status checks, and review comments.
- Use GitHub tools when available. Otherwise use `gh`, starting with:
  - `gh pr view --json number,url,title,body,baseRefName,headRefName,reviewDecision,statusCheckRollup`
  - `gh pr diff`
- Prefer unresolved review threads when resolution state matters. Use `gh api graphql` for `reviewThreads` if flat comments lose thread context.
- Stop if there is no concrete PR or authenticated way to read the feedback.

### 2. Triage Feedback

For each thread or comment, inspect the current code around the referenced file and line. Classify it as:

- **Valid and actionable**
- **Already addressed**
- **Stale** because the code changed
- **Style or nit**, optional unless it protects consistency
- **Incorrect or not worth changing**
- **Needs human decision**

Group related comments by underlying issue. Do not implement comments just because they exist.

### 3. Fix

- Implement the smallest changes that address valid feedback.
- Preserve existing behavior and contracts unless the comment identifies a real bug or intended contract change.
- Avoid unrelated refactors, drive-by cleanup, and broad rewrites.
- If a comment asks for a larger design change, stop and explain the decision needed instead of guessing.

### 4. Verify

- Run focused tests, linting, type checks, or project checks that prove the fixes.
- If a comment concerns UI or rendered output, use `browser-verify` when available.
- If verification cannot be run, report exactly what is missing.

### 5. Prepare Replies

Draft a concise reply for each thread or comment using one of these statuses:

- **Fixed**: code changed and verification passed. Mention the specific fix and check.
- **Already addressed**: current code already handles it. Mention where or how.
- **Stale**: referenced code no longer exists or the diff changed.
- **Declined**: intentionally not changed. Give a brief engineering reason.
- **Needs decision**: requires a product, contract, architecture, or scope choice.

Post replies, resolve threads, push commits, or mark checks complete only when the user explicitly asks. If posting replies, keep them short and factual.

### 6. Report

Summarize:

- Feedback addressed, grouped by issue
- Feedback skipped or declined, with brief reasons
- Feedback needing human input
- Draft replies or posted replies
- Files changed
- Verification run and any remaining risk

## Rules

- Do not resolve threads, post replies, push, or mark checks complete unless the user asks.
- Do not treat AI review comments as authoritative.
- Do not post `Fixed` unless the code changed or was already correct and verification supports the claim.
- Do not mix pre-existing issues into the fix unless they block the reviewed change.
- If comments conflict, choose the safer option or ask.
- A clean triage with no code changes is a valid outcome.
