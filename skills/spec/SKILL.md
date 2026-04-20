---
name: spec
description: "Write a short implementation spec before coding. Use when starting new work, when requirements are unclear, or when a change needs explicit boundaries."
user-invocable: true
argument-hint: "<feature-name> <description> e.g. 'user-auth add OAuth login with Google and GitHub'"
---

# Spec

## When to use

- Starting a new feature or meaningful change
- Requirements, boundaries, or success criteria are unclear
- The change touches multiple files, components, or interfaces

## Process

1. Use the first argument as the feature name and everything after it as the request.
2. Read the codebase first so the spec fits the project as it exists.
3. If important details are ambiguous, ask concise clarifying questions. State assumptions explicitly instead of inventing requirements silently.
4. Write `docs/<feature-name>/spec.md` with:
   - What
   - Requirements
   - Design
   - Testing Strategy
   - Out of Scope
5. Keep it brief. Include error behavior, concrete success conditions, and only the design detail needed to build correctly.

## Verification

- The spec is saved to `docs/<feature-name>/spec.md`
- Requirements are specific and testable
- Error behavior is covered where it matters
- The design matches existing project patterns
- Assumptions are marked instead of hidden

## Rules

- Make the smallest safe change to the system description that fully solves the problem.
- Call out interface, schema, config, CLI, or file-format changes explicitly.
- Include failure paths where they matter instead of leaving them implicit.
- Do not write a greenfield design if the codebase already has patterns to follow.
- Skip the spec for tiny, self-contained changes with obvious behavior.
- If the request is missing a decision that would materially change the build, ask.
- If the spec starts getting long, split the work instead of expanding the document.
