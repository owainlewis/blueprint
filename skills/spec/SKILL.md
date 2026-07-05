---
name: spec
description: "Write an implementation spec to docs/<feature-slug>/spec.md and pause for human review."
user-invocable: true
argument-hint: "<feature description, context, or constraints>"
---

# Spec

Goal: write a short spec before coding starts.

## Workflow

1. Read the request, referenced files, and relevant code. Derive a kebab-case feature slug if needed.
2. Ask one question at a time, with a recommended answer, only when a missing decision would change behavior, function signatures, return values, data shapes, dependencies, or checks.
3. Write `docs/<feature-slug>/spec.md`. Keep it short unless decisions, behavior that must not change, or interfaces need detail.
4. Include: summary, background, requirements, design, decisions, behavior that must not change, error behavior, test plan, and what not to change. Omit sections that do not apply.
5. Check current official versions when the spec pins runtimes, services, frameworks, or dependencies.
6. Stop after writing and ask for review. Do not plan or implement.

## Rules

- Specify the smallest safe change that solves the problem.
- If two implementations would behave differently, choose a default.
- Match existing code patterns or explain why a new one is needed.
- Split the task when the spec gets too long.
