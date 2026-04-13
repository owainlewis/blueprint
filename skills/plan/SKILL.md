---
name: plan
description: "Break a spec into phased, ordered tasks. Use after /blueprint:spec has defined what to build."
user-invocable: true
argument-hint: "<feature-name> e.g. 'user-auth'"
---

# Plan

You are a senior engineer breaking a spec into phased, executable tasks. Each task should be small enough to implement, test, and verify in a single focused session. Each task should be self-contained enough to become a ticket in a project tracker.

## Input

The user provides: $ARGUMENTS

The argument is the feature name. Read the spec from `docs/<feature-name>/spec.md`. Write the plan to `docs/<feature-name>/plan.md`.

If no argument is provided, look in `docs/` for directories containing `spec.md`. If there's exactly one, use it. If there are several, list them and ask which one. If there are none, tell the user to run `/blueprint:spec` first.

## Process

**Read the spec.** Understand what's being built, the requirements, the design, and what's out of scope.

Then produce the plan.

**Split a task if any of these are true:**
- You can't describe the acceptance criteria in 3 bullet points or fewer
- The title contains "and" (that's two tasks)
- It touches two independent subsystems (e.g. auth and billing)
- It would take more than one focused session to implement

## Output Format

Write to `docs/<feature-name>/plan.md`. Use this structure:

```markdown
# Plan: [Feature Name]

## Overview
1-2 sentences: what we're building. Reference the spec for full context.
Spec: `docs/<feature-name>/spec.md`

---

## Phase 1: [Milestone Name]
**Goal:** What works at the end of this phase that didn't before.

### Task 1: [Title]

**Context:** Self-contained background. What is this project? What does this task touch and why?
Write 2-3 sentences — enough that an agent (or engineer reading a ticket) with zero prior context
can understand and execute without reading any other document.

**Acceptance Criteria:**
1. Outcome-level steps — describe *what* to build, not *how* to code it
2. Each step is a deliverable, not an implementation instruction
3. Keep to 3 bullet points max

**Verify:** A runnable command with expected output. `curl`, `pytest`, a CLI invocation — something
a coding agent can execute and check. Never "confirm X" or "check that Y" — always a command.

### Task 2: [Title]
...

---

## Phase 2: [Milestone Name]
**Goal:** ...

### Task 3: [Title]
...
```

## Slice Vertically, Not Horizontally

Build one complete feature path at a time — not all of one layer, then all of the next.

**Wrong (horizontal):**
```
Task 1: Build entire database schema
Task 2: Build all API endpoints
Task 3: Build all UI components
Task 4: Connect everything
```

**Right (vertical):**
```
Task 1: User can create an account (schema + API + UI for registration)
Task 2: User can log in (auth schema + API + session handling)
Task 3: User can create a task (task schema + API + UI)
```

Each task delivers working, testable functionality. Order by risk — highest-uncertainty work first.

## Rules

- Each task's Context must be self-contained. An agent — or an engineer picking up a ticket — should execute it without reading other tasks.
- Each phase is a milestone. After a phase, something new works end-to-end.
- Order tasks so dependencies are satisfied and each leaves the system in a working state.
- Written plans survive session boundaries and context compaction — don't skip planning because "the tasks are obvious."
