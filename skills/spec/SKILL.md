---
name: spec
description: "Write an implementation spec to docs/<feature-slug>/spec.md and pause for human review. Use when the user asks for a spec, or when a task has decisions, invariants, or contracts that should be reviewed before code is written."
user-invocable: true
argument-hint: "<feature description, context, or constraints>"
---

# Spec

You are a principal engineer writing a technical spec for an AI agent to execute. Cover what we are building, why it matters, and how to build it safely. The spec combines requirements and technical design: one document, one read.

## Workflow

### 1. Align

- Treat the full argument as the request unless the user names a feature.
- Derive a kebab-case feature slug if no name is given.
- Read referenced files and relevant code so the spec fits the project as it exists.
- Identify decisions, dependencies, invariants, contracts, and error behavior that need review before coding.
- If code can answer a question, inspect the code instead of asking.
- Ask only when a missing decision would materially change the spec.
- Ask one question at a time, with your recommended answer.
- Continue only when the spec can be written without guessing.

### 2. Write

Write `docs/<feature-slug>/spec.md` using the sections below. Tailor detail to the task: keep simple specs short, expand only where decisions, invariants, or interfaces need review.

- **What**: one-paragraph summary.
- **Context**: why this matters, what exists today, links to relevant code.
- **Requirements**: specific, testable statements of what the system must do.
- **Design**: the chosen approach: components, data flow, interfaces, file changes.
- **Decisions**: choices the agent would otherwise make alone, with the option taken and why. Mark assumptions explicitly.
- **Invariants** *(when relevant)*: what must not break, and how to check it.
- **Error Behavior** *(when relevant)*: failure paths, error shapes, recovery.
- **Testing Strategy**: what proves the change works.
- **Out of Scope**: what this spec deliberately does not cover.

### 3. Pause

Stop after writing. Do not continue into planning or implementation until the human confirms.

## Rules

- Smallest safe change that fully solves the problem.
- If two implementations would behave differently, specify the default.
- Do not write a greenfield design if the codebase has patterns to follow.
- Write for a human who will read this in six months and has forgotten the thread.
- If the spec is getting long, split the task instead of expanding the document.
