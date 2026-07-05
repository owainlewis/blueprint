---
name: plan
description: "Plan work. Break work down into outcome-based tasks for an agent to execute, optionally grouped into milestones."
user-invocable: true
argument-hint: "<spec path, feature slug, task reference, or planning input>"
---

# Plan

1. Read the input, linked files, and relevant code. Ask if context is missing.
2. Group tasks into milestones only when the effort is large. Each milestone has one clear result.
3. Prefer tasks that deliver user-visible progress. Order by dependency and risk.
4. Each task says what should be true, why it matters, what must not change, and how to verify it. Not how to implement it, unless the implementation detail is a real requirement.
5. File tasks in the project's issue tracker. Use the tracker the repo already uses; default to GitHub Issues if unclear. Deliver to `docs/<feature-slug>/plan.md` or chat only when the user asks.

## Task Fields

Title, goal, background, acceptance criteria, verify steps. Add references, constraints, dependencies, labels, or milestone only when they carry real information.

## Rules

- Each task must stand alone for a new agent with no additional context.
- Acceptance criteria are observable results. Verify steps are specific and runnable.
- Split tasks that mix unrelated decisions or need too many acceptance criteria.
- Don't list files to edit or functions to add unless that detail is part of the requirement.
- Before filing, check for existing issues covering the same work. Follow the repo's issue templates and labels when present.
