---
name: spec
description: "Write an implementation spec for a requested task and pause for human review before planning or coding."
user-invocable: true
argument-hint: "<feature-name> <description> e.g. 'user-auth add OAuth login with Google and GitHub'"
---

# Spec

## When to use

- A task has decisions the agent would otherwise make alone
- Invariants, contracts, schemas, or error behavior need to be preserved
- Requirements, boundaries, or success criteria are unclear
- The change touches multiple files, components, interfaces, or data shapes

Use this skill when the user explicitly asks for a spec.

## Workflow

### 1. Understand

- Use the first argument as the feature name and everything after it as the request.
- Read the task and relevant code first so any spec fits the project as it exists.
- Identify the decisions, invariants, requirements, contracts, boundaries, and error behavior that may need review before coding.

### 2. Write

- Write `docs/<feature-name>/spec.md`.
- Include:
  - What
  - Context
  - Requirements
  - Design
  - Decisions
  - Invariants, when relevant
  - Error Behavior, when relevant
  - Testing Strategy
  - Out of Scope
- Keep it brief. Include only the detail needed to review decisions and build correctly.
- Ask before writing only if the request is missing a decision that would materially change the spec.

### 3. Pause For Review

- After writing the spec, stop and ask the human to review it.
- Do not continue into planning or implementation until the human confirms or requests changes.

## Verification

- The spec is written in `docs/<feature-name>/spec.md`
- Requirements are specific and testable
- Decisions the agent would otherwise make are explicit
- Invariants say what must not break and how to check it
- Error behavior is covered where it matters
- The design matches existing project patterns
- Assumptions are marked instead of hidden
- Specs are left for human review before planning or coding continues

## Rules

- Make the smallest safe change to the system description that fully solves the problem.
- If two reasonable implementations would behave differently, specify the default.
- Call out interface, schema, config, CLI, or file-format changes explicitly.
- Document public success shapes and important error shapes for external interfaces.
- Include failure paths where they matter instead of leaving them implicit.
- Do not write a greenfield design if the codebase already has patterns to follow.
- If the spec starts getting long, split the task instead of expanding the document.
- Compress wording aggressively without dropping behavior, constraints, names, or examples that carry meaning.
