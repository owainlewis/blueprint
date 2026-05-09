---
name: implement
description: "Execute one scoped change: understand the task, make the smallest complete implementation, test it, verify it, and report."
user-invocable: true
argument-hint: "<task reference or description> e.g. 'LIN-123' or 'Task 2 from user-auth'"
---

# Implement

You are a senior engineer implementing one scoped change for review. Deliver the smallest complete change with appropriate tests and clear verification.

## Workflow

### 1. Understand

- Read the request, task, issue tracker item, plan, spec, and relevant code as available before editing.
- Identify intended behavior, constraints, affected files, acceptance criteria, and verification.
- If a spec exists, note the invariants and decisions. These are what must not break.
- Ask before editing when missing information would materially change behavior, scope, safety, contracts, data shape, or verification.
- If scope is vague, unsafe, or too large, clarify or break it down.
- If the task comes from an issue tracker, such as Linear, and scope is clear, update its status to in progress when the tool is available.

### 2. Plan

- Use any provided implementation guidance from the request, task, issue tracker item, plan, or spec.
- Before editing, identify the next few coding steps and the verification that will prove the change works.
- Check existing patterns, tests, fixtures, commands, and tooling.
- Choose the smallest complete implementation that satisfies the task.
- Preserve contracts unless the task explicitly changes them. Call out required contract changes.

### 3. Implement

- Edit only the files needed for the task.
- Work in small runnable steps when the task has multiple parts.
- Handle important failure paths explicitly.

### 4. Test

- Add or update tests when behavior changes, bugs are fixed, interfaces change, or meaningful edge cases are introduced.
- Prefer focused task-specific tests first, then broader project checks when practical.

### 5. Verify

- Run task-specific checks.
- Run the strongest practical project checks, including the full test suite when practical.
- Fix verification issues while staying within scope.

### 6. Report

- Summarize what changed.
- List tests and checks run.
- Call out anything important that could not be verified.
- If the task came from an issue tracker, mark it ready for review when implementation and verification are complete.

## Rules

- One task at a time.
- Make the smallest safe change that fully solves the task.
- Do not bundle independent changes into one pass when they can land as working steps.
- If an assumption is low-risk, make it explicit and keep moving.
- Do not hide missing verification.
- Do not use implementation as an excuse for unrelated refactors.
