---
name: implement
description: "Finish one code task: understand it, make the smallest change, test it, review it, and report or open the requested PR."
user-invocable: true
argument-hint: "<task reference or description> e.g. 'LIN-123' or 'Task 2 from user-auth'"
---

# Implement

Goal: finish one code task with tests and review.

## Workflow

1. Read the request, ticket, spec, plan, and relevant code. Capture the goal, acceptance criteria, checks, and what not to change.
2. Ask only when requirements, what to change, safety, code ownership, or product behavior are unclear. State low-risk assumptions and continue.
3. Make the smallest complete change in the right module. Preserve public functions, commands, config, routes, return values, and data shapes unless the task requires changing them.
4. Add or update tests for changed behavior. If a useful test is not practical, say why and verify manually.
5. Run the most relevant checks first, then wider checks when shared behavior, public functions, commands, config, routes, generated docs, or user-facing flows changed. Fix relevant failures without expanding the task.
6. Ask another agent or reviewer to review the diff before reporting back or opening a PR. Fix real issues about this task and rerun checks. If no other reviewer is available, self-review for obvious issues, but do not push or open a PR unless the user explicitly accepts that limitation.
7. If the task expects a PR, use a task branch, commit intended changes with a Conventional Commit subject, include the ticket ID when available, push, and open a PR ready for review with a clear title and body. Otherwise report changed files, checks, acceptance status, review status, and anything not checked.

## Rules

- One task at a time.
- Do not touch unrelated code.
- Do not hide work that was not checked.
- Do not overwrite or discard user changes.
- Stop if the task, spec, or plan is wrong; update the source of truth before continuing.
