---
name: pr
description: "Writes and opens or updates a high-quality pull request from the branch diff: plain summary, visual change shape, verification proof, and merge risk. Use when opening, rewriting, or tightening a PR description."
user-invocable: true
argument-hint: "[branch, base, issue, or PR]"
disable-model-invocation: true
---

# Pull request

Write a pull request a reviewer can understand in under a minute. Write in plain, simplified technical English.

## Steps

1. Inspect `git diff <base>...HEAD`, the branch commits, and the linked spec or ticket. Never write a PR description from memory.
2. Check the diff for stray debug logs, unintended files, or out-of-scope edits. Flag or clean them before opening.
3. Write the PR title and body using the repository's PR template, or the template below if it has none.
4. Link any completed issue (`Closes #...`, Linear ID, or Jira key).
5. Push the branch and open or update the PR (mark it draft if checks or review are not yet green), unless the user only asked for the text. Never merge.

## Template

```markdown
## What
<!-- 1–2 sentences: the change a user or caller notices. -->

## Why
<!-- 1 sentence: the problem. Link the spec or ticket. -->

## What changed
<!-- At most 5 bullets, grouped by behavior, not by file.
For multi-part or architectural changes, include one small visual
(Mermaid diagram, call/component tree, or before/after table) showing the shape of the change. -->

## Where to look closely
<!-- Optional: 1–2 trickiest files, tradeoffs, or assumptions for the reviewer. Omit if obvious. -->

## Verification
<!-- Exact commands run and results. Screenshots or terminal output for anything visible.
Independent review verdict and CI state.
Not verified: <what you could not check, or None>. -->

## Risk
<!-- Low, Medium, or High, then one line on blast radius and reversibility
(two-way door / cheap rollback vs. one-way door / migration or contract change).
High: database schema or migration, API or event contract, auth, payments, deleting data.
Medium: shared code with many callers, configuration, dependencies.
Low: one screen, one endpoint's internals, docs, tests. -->
```

## Rules

- Lead with the user-visible outcome, not a file-by-file tour.
- State only checks you actually ran. List anything skipped under `Not verified`.
- Keep the title under 72 characters and outcome-focused.
- Delete placeholder comments before posting.

## Return

The PR URL (or drafted title and body), linked issues, risk level, and anything unverified.
