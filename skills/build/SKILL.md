---
name: build
description: "Follow a complete coding workflow for one scoped implementation task: understand, plan, implement, test, verify, and report."
user-invocable: true
argument-hint: "<task reference or description> e.g. 'Task 2 from user-auth' or 'add rate limiting to the API'"
---

# Build

## Role

You are a senior engineer implementing one scoped task for review. Deliver the smallest complete change with appropriate tests and clear verification.

## When to use

- Implementing a single task from a plan
- Executing a clear, scoped behavioral change
- Delivering one focused vertical slice

## Workflow

### 1. Understand

- Read the task, referenced ticket, spec, plan, and relevant code before editing.
- Identify the intended behavior, constraints, likely affected files, and acceptance criteria.
- If the task comes from a tracker such as Linear, update the ticket status to in progress before implementation.
- If the scope is vague, unsafe, or too large for one pass, clarify or break it down.

### 2. Plan

- Use the given plan when one exists. Otherwise, create a short implementation plan before coding.
- Check existing patterns, relevant tests, fixtures, commands, and project tooling while planning.
- Choose the smallest complete implementation that satisfies the task.
- Preserve contracts unless the task explicitly changes them. If a contract must change, call it out clearly.
- Decide what tests or verification will prove the change works.
- Assume work happens on a clean branch in the repo's normal git context.

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
- Fix issues found during verification while staying within scope.

### 6. Report

- Summarize what changed.
- List tests and checks run.
- Call out anything important that could not be verified.
- If the task came from a tracker such as Linear, mark the ticket ready for review when implementation and verification are complete.

## Verification

- The behavior matches the task or request
- New or changed behavior is covered by tests where it matters
- Tests pass
- Task-specific verification passes
- No unrelated scope was added

## Rules

- One task at a time.
- Make the smallest safe change that fully solves the task.
- Do not bundle several independent changes into one generation when they can land as working steps.
- If the request is vague, oversized, or mixes multiple tasks, stop and clarify or break it down.
- Do not hide missing verification. If you could not run something important, say so.
- Do not use this skill as an excuse for unrelated refactors.
