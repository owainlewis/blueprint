---
name: implement
description: "Finish one code task: understand it, make the smallest change, test it, review it, and report or open the requested PR."
user-invocable: true
argument-hint: "<task reference or description> e.g. 'LIN-123' or 'Task 2 from user-auth'"
---

# Implement

1. Read the request, its sources, and the relevant code. Capture the goal, acceptance criteria, checks, and what not to change.
2. Ask only when requirements, safety, ownership, or product behavior are unclear. State low-risk assumptions and continue.
3. Make the smallest complete change in the right module. Don't change public interfaces or data shapes unless the task requires it.
4. Add or update tests for changed behavior. If a useful test isn't practical, say why and verify manually.
5. Run the most relevant checks first, wider checks when shared or user-facing behavior changed. Fix relevant failures without expanding the task.
6. Get the diff reviewed by another agent or reviewer before reporting or opening a PR. If none is available, self-review, and don't push or open a PR unless the user accepts that limitation.
7. If the task expects a PR: task branch, Conventional Commit with ticket ID when available, push, open a PR ready for review. Otherwise report changed files, checks, acceptance status, review status, and anything not checked.

## Rules

- One task at a time. Don't touch unrelated code.
- Don't hide unchecked work.
- Don't overwrite or discard user changes.
- If the task, spec, or plan is wrong, stop and update the source of truth before continuing.
