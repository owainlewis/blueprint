---
name: plan
description: "Plan work. Break work down into a number of tasks for an agent to execute."
user-invocable: true
argument-hint: "<spec path, feature slug, task reference, or planning input>"
---

# Plan

Goal: Plan work by creating outcome-based tasks optionally grouped into logical milestones.

## Workflow

1. Read the input, linked files, and relevant code. Stop and ask the user if you need more clarification or context.
2. Break work into milestones when they make a large effort easier to understand. Each milestone needs one clear result. Skip milestones for small work.
3. Prefer tasks that deliver user-visible progress. Order by dependency and risk. 
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

- Each task must stand alone for a new agent to execute without additional context.
- Acceptance criteria describe observable results, not implementation steps.
- Check steps must be specific and runnable.
- Split tasks that mix unrelated decisions or need too many acceptance criteria.
- Tell the agent what you want not how to do it. 
- Do not list exact files to edit, functions to add, or steps to follow unless that detail is part of the requirement.
- When important - reference related local files the agent should read (e.g. a plan or design doc). 
