## What

<!-- 1–2 sentences: the change a user or caller notices. -->

## Why

<!-- 1 sentence: the problem. Link the spec or ticket. -->

## What changed

<!-- At most 5 bullets, grouped by behavior, not by file.
For multi-part changes, add one small diagram, tree, or before/after table showing the shape of the change. -->

## Where to look closely

<!-- Optional: 1–2 trickiest files, tradeoffs, or assumptions. Delete if not needed. -->

## Verification

<!-- Exact commands run and their results. Screenshots or terminal output for anything visible.
Independent review verdict and CI state.
Not verified: <what you could not check, or None>. -->

## Risk

<!-- Low, Medium, or High, then one line on blast radius and reversibility
(cheap rollback vs. one-way migration or contract change).
High: database schema or migration, API or event contract, auth, payments, deleting data.
Medium: shared code with many callers, configuration, dependencies.
Low: one screen, one endpoint's internals, docs, tests. -->

<!-- Add Closes #... (or Linear/Jira key) when this pull request completes an issue. -->
