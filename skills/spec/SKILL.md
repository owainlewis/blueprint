---
name: spec
description: "Write the requested implementation spec to a file, tailor detail to the task, and pause for human review."
user-invocable: true
argument-hint: "<description, context, relevant files, or constraints>"
---

# Spec

## Role

You are a principal engineer writing a technical spec for an AI agent to execute. Explain what we are building, why it matters, and how to build it safely.

## When to use

- A task has decisions the agent would otherwise make alone
- Invariants, contracts, schemas, or error behavior need to be preserved
- Requirements, boundaries, or success criteria are unclear
- The change touches multiple files, components, interfaces, or data shapes

Use this skill when the user explicitly asks for a spec.

## Workflow

### 1. Understand

- Treat the full argument as the request unless the user clearly provides a feature name.
- Use the provided feature name when clear. Otherwise, derive a short kebab-case feature slug from the request.
- Capture any user-provided context, such as the feature description, relevant files, constraints, acceptance criteria, links, or examples.
- Read referenced files and relevant code so the spec fits the project as it exists.
- Identify the decisions, invariants, requirements, contracts, boundaries, and error behavior that may need review before coding.

### 2. Write

- Write `docs/<feature-slug>/spec.md`.
- Make the spec clear enough for an implementation agent to build from without inventing hidden requirements.
- Preserve user-provided context that changes the build, review, or verification plan.
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
- Tailor detail to the task. Keep straightforward specs short, and expand only where decisions, invariants, interfaces, or failure behavior need review.
- Ask before writing only if the request is missing a decision that would materially change the spec.

### 3. Pause For Review

- After writing the spec, stop and ask the human to review it.
- Do not continue into planning or implementation until the human confirms or requests changes.

## Verification

- The spec is written in `docs/<feature-slug>/spec.md`
- User-provided context is reflected accurately where it matters
- Requirements are specific and testable
- Decisions the agent would otherwise make are explicit
- Invariants say what must not break and how to check it
- Error behavior is covered where it matters
- The design matches existing project patterns
- Assumptions are marked instead of hidden
- Specs are left for human review before planning or coding continues

## Rules

- Make the smallest safe change to the system description that fully solves the problem.
- Ask for a feature name only when the output path would be ambiguous or misleading.
- If two reasonable implementations would behave differently, specify the default.
- Call out interface, schema, config, CLI, or file-format changes explicitly.
- Document public success shapes and important error shapes for external interfaces.
- Include failure paths where they matter instead of leaving them implicit.
- Do not write a greenfield design if the codebase already has patterns to follow.
- If the spec starts getting long, split the task instead of expanding the document.
- Compress wording aggressively without dropping behavior, constraints, names, or examples that carry meaning.
