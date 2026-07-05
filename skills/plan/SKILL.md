---
name: plan
description: "Break a spec, brief, issue, or user request into outcome-based tasks small enough for one agent run and put them in one place."
user-invocable: true
argument-hint: "<spec path, feature slug, task reference, or planning input>"
---

# Plan

Goal: turn the input into outcome-based tasks a new agent can do.

## Workflow

1. Read the input, linked files, and relevant code. Stop if missing information would change task boundaries, order, acceptance criteria, or checks.
2. Use phases only when they make a large effort easier to understand. Each phase needs one clear result. Skip phases for small work.
3. Split tasks by result. Prefer tasks that deliver user-visible progress. Order by dependency and risk. Put shared decisions before the tasks that need them.
4. Describe what should be true, why it matters, what must not change, and how to verify it. Avoid telling the agent how to implement the change unless the implementation detail is a real requirement.
5. Deliver to exactly one place: tracker issues when asked, `docs/<feature-slug>/plan.md` when there is a feature directory, or chat otherwise.

## Task Fields

- Title, when filing issues
- Goal
- Background
- Starting points or references, only when useful as hints
- Constraints, only when they are real product, technical, compatibility, security, migration, or operational limits
- Acceptance criteria
- Verify
- Depends on or what not to change, when needed
- Labels or milestone, when the destination supports them and the repo documents them

## Rules

- Each task must stand alone for a new agent.
- Acceptance criteria describe observable results, not implementation steps.
- Check steps must be specific and runnable.
- Split tasks that mix unrelated decisions or need too many acceptance criteria.
- Do not create phase issues unless the phase itself is executable.
- Do not include a proposed approach by default.
- Do not list exact files to edit, functions to add, or steps to follow unless that detail is part of the requirement.
- File references are context, not required edit locations.
