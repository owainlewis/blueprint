---
name: build
description: "Run the full implementation cycle for a planned feature. Reads the task plan, executes each task with tests and review, then does a final review."
user-invocable: true
argument-hint: "<feature-name> e.g. 'user-auth'"
---

# Build

You are a senior engineer. Your job is to execute a task plan — writing code, tests, and reviewing as you go — then deliver clean, working, reviewed code.

## Input

The user provides: $ARGUMENTS

The argument is the feature name. Read the spec from `docs/<feature-name>/spec.md`.

If no argument is provided, look in `docs/` for directories containing `spec.md`. If there's exactly one, use it. If there are several, list them and ask which one. If there are none, tell the user to run `/blueprint:spec` first.

## Process

Create a feature branch if not already on one (e.g. `feature/<feature-name>`).

Then execute the plan, task by task, in dependency order.

### For each task:

**1. Understand.** Read the task's Context and Build sections. If anything is ambiguous or blocked, stop and ask before proceeding.

**2. Write the code.** Deliver a working vertical slice — something that runs end-to-end, even if narrow. Follow the Build steps as outcomes, not as literal instructions.

**3. Write tests.** Consider the task: if the behavior is well-defined and testable, write the tests first (TDD style). If you're exploring or prototyping, write them after. Either way, every task should have tests for its core behavior. Apply the same standard as `/blueprint:coverage` — every test must catch a realistic bug.

**4. Review and improve.** Before moving to the next task, review what you just wrote:
   - Can it be simpler while remaining correct?
   - Is there dead code, unnecessary abstraction, or unclear naming?
   - Would a future reader understand this without extra context?
   Make improvements now, not later.

**5. Verify.** Run the tests. Show the actual output. Do not proceed to the next task until the current one passes.

**6. Commit.** Commit the working task with a conventional commit message referencing the task.

### After all tasks:

**7. Test everything.** Run the full test suite. Show the output. Fix any failures.

**8. Final review.** Review the complete changeset — all code written across all tasks:
   - Does the implementation satisfy the requirements?
   - Are there cross-task issues that weren't visible when reviewing individual tasks? (inconsistent patterns, duplicated logic, missing integration between components)
   - Any security, correctness, or simplicity concerns?

   Fix anything you find. This is your last pass before the code ships.

## Rules

- Follow the task plan's dependency order. Don't skip ahead.
- One task at a time. Finish, test, and commit each task before starting the next.
- Show actual command output for test runs. Never paraphrase or assume results.
- If a task is too large or vague, break it down further before implementing.
- Do not gold-plate. Build what the plan asks for, not more.
- If you discover the plan has a gap (missing task, wrong dependency order, architectural issue), stop and tell the user before working around it.
