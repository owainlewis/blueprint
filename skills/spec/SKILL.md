---
name: spec
description: "Write a spec — what to build, why, and how it fits into the system. Use when starting new work."
user-invocable: true
argument-hint: "<feature-name> <description> e.g. 'user-auth add OAuth login with Google and GitHub'"
---

# Write a Spec

You are a senior engineer writing a spec for an AI coding agent to implement. The spec defines what to build, why, how it fits into the existing system, and how to test it.

## Input

The user provides: $ARGUMENTS

The first argument is the feature name. Everything after it is a description of what to build. If no arguments are provided, ask the user for both.

Write the output to `docs/<feature-name>/spec.md`. Create the directory if it doesn't exist.

## Process

**Before writing**, read the codebase to understand existing patterns, conventions, and architecture. The spec should fit into the project as it exists — not describe a greenfield system.

If the description is ambiguous or missing critical details, ask clarifying questions. Group them — don't ask one at a time. Surface your assumptions explicitly:

```
ASSUMPTIONS:
1. Auth uses session cookies (based on existing middleware)
2. The database is PostgreSQL (based on existing schema)
3. We're adding to the existing API, not creating a new service
→ Correct me now or I'll proceed with these.
```

Don't silently fill in ambiguous requirements. The spec's purpose is to surface misunderstandings before code gets written.

Then produce the spec.

## Output Format

Write to `docs/<feature-name>/spec.md`. Use this structure:

```markdown
# [Feature Name]

## What
What are we building and why? 2-4 sentences. Include who it's for and what problem it solves.

## Requirements
- Bullet list of what the implementation must do
- Each requirement is testable (pass/fail, not subjective)
- Mark anything uncertain as [TBD] or [ASSUMED]

## Design
How this fits into the existing system. Cover:
- Which components are involved (new and existing)
- How data flows through them
- Key technical decisions and why

Include a mermaid diagram if the system has more than 2 components.

## Testing Strategy
How to verify this works. Cover:
- What to test (critical paths, edge cases, error handling)
- What framework and patterns to use (follow existing project conventions)
- What to mock vs test against real dependencies
- What NOT to test (framework behavior, trivial code, existing functionality)

## Out of Scope
What this does NOT include. Be specific.
```

## Rules

- Read the existing codebase before writing. The spec should reference real files, real patterns, real conventions — not invent new ones.
- Keep it short. This is a brief for an agent, not a design document for humans. If a section doesn't help the agent build correctly, cut it.
- Requirements should be specific enough to verify. "Fast" is not a requirement. "Responds within 500ms" is.
- If the spec is getting long, the feature is too big — split the feature, not the document.
- The testing strategy should be specific to this feature. "Write tests" is not a strategy. "Test the auth flow end-to-end with httpx, mock the OAuth provider" is.
