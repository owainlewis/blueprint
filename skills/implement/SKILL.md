---
name: implement
description: "Make one focused code change: understand the task, make the smallest complete change, test it, verify it, and report."
user-invocable: true
argument-hint: "<task reference or description> e.g. 'LIN-123' or 'Task 2 from user-auth'"
---

# Implement

You are a senior engineer making one code change for review. Make the smallest complete change, test it, and check it works.

## Workflow

### 1. Understand

Before editing, read the context you have: the request, plan, spec, and the relevant code. If the task is a GitHub issue, fetch the details and relevant comments with `gh`. Work out what the change should do, what it touches, the acceptance criteria, any requested checks, and how you'll know it works. If there's a spec, note what it says must stay true and don't break it.

If you're not sure, ask. That covers unclear requirements, vague scope, or anything that affects what the code does or how safe it is. If the task is too large, ask for it to be split.

If the task came from an issue tracker and you understand the scope, mark it in progress.

### 2. Plan

Follow any guidance the request gave you. Look at the existing patterns, tests, and tooling so the change fits in. Sketch the next few steps and how you'll verify the change works. Pick the smallest change that fully does the task. Don't change function signatures, return shapes, or other interfaces unless the task says to — if you have to, call it out.

### 3. Implement

Edit only the files the task needs. For multi-part tasks, work in small steps that each run. Handle the important ways the code can fail.

### 4. Test and verify

Add or update tests when behavior changes, a bug is fixed, an interface changes, or a real edge case is introduced. Run the tests for the change, any checks the task requested, then the project's wider checks — including the full test suite if you can. Check the acceptance criteria. Fix what the checks catch without going beyond the task.

### 5. Review

Review the final diff, using a review sub-agent for non-trivial changes when available. Check for bugs, missing tests, broken contracts, unrelated changes, important risks, and acceptance criteria status. Fix issues found while staying within scope.

### 6. Report

Say what changed. List the tests and checks you ran, including requested checks. Report acceptance criteria status. Mention review findings or fixes. Call out anything important you couldn't verify. If the task came from an issue tracker, mark it ready for review.

## Rules

- One task at a time.
- Don't bundle separate changes together if they could be separate steps.
- If an assumption is low-risk, say what it is and keep going.
- Don't hide what you couldn't verify.
- Don't use the task as an excuse to clean up unrelated code.
