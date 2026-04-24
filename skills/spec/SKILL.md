---
name: spec
description: "Write an implementation spec when a task has decisions, invariants, or boundaries worth surfacing before coding."
user-invocable: true
argument-hint: "<feature-name> <description> e.g. 'user-auth add OAuth login with Google and GitHub'"
---

# Spec

## When to use

- A task has decisions the agent would otherwise make alone
- Invariants, contracts, schemas, or error behavior need to be preserved
- Requirements, boundaries, or success criteria are unclear
- The change touches multiple files, components, interfaces, or data shapes

Skip this skill for tiny, decision-complete changes. Prompt the agent directly.

## Process

1. Use the first argument as the feature name and everything after it as the request.
2. Read the task and relevant code first so the spec fits the project as it exists.
3. Choose the lightest useful output:
   - no spec: say the work is prompt-ready
   - short spec: return one concise instruction in chat
   - full spec: write `docs/<feature-name>/spec.md`
4. For a full spec, include:
   - What
   - Context
   - Requirements
   - Design
   - Decisions
   - Invariants, when relevant
   - Error Behavior, when relevant
   - Testing Strategy
   - Out of Scope
5. Keep it brief. Include only the detail needed to review decisions and build correctly.

## Verification

- The output weight matches the task's decision weight
- Requirements are specific and testable
- Decisions the agent would otherwise make are explicit
- Invariants say what must not break and how to check it
- Error behavior is covered where it matters
- The design matches existing project patterns
- Assumptions are marked instead of hidden

## Rules

- Make the smallest safe change to the system description that fully solves the problem.
- If two reasonable implementations would behave differently, specify the default.
- Call out interface, schema, config, CLI, or file-format changes explicitly.
- Document public success shapes and important error shapes for external interfaces.
- Include failure paths where they matter instead of leaving them implicit.
- Do not write a greenfield design if the codebase already has patterns to follow.
- Skip the spec for tiny, self-contained changes with obvious behavior.
- If the request is missing a decision that would materially change the build, ask.
- If the spec starts getting long, split the task instead of expanding the document.
- Compress wording aggressively without dropping behavior, constraints, names, or examples that carry meaning.
