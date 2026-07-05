---
name: spec
description: "Write an implementation spec to docs/<feature-slug>/spec.md and pause for human review."
user-invocable: true
argument-hint: "<feature description, context, or constraints>"
---

# Spec

1. Read the request, referenced files, and relevant code.
2. Ask one question at a time, with a recommended answer, only when a missing decision would change behavior, interfaces, dependencies, or checks.
3. Write `docs/<feature-slug>/spec.md`, short unless the decisions need detail, using the template below. Omit sections that don't apply.
4. Check current versions when the spec pins runtimes, frameworks, or dependencies.
5. Stop and ask for review. Do not plan or implement.

## Rules

- Specify the smallest safe change that solves the problem.
- If two implementations would behave differently, choose a default.
- Match existing code patterns or explain why a new one is needed.
- Split the task when the spec gets too long.

## Template

    # <Feature>

    ## Summary
    What this does and why, in a few sentences.

    ## Requirements
    What must be true when done. Observable, testable statements.

    ## Design
    Components touched, data flow, interfaces, file paths. Skip anything the code will make obvious.

    ## Decisions
    Choices made where implementations could differ, each with the chosen default and why.

    ## Must not change
    Existing behavior, interfaces, and data shapes this work must preserve.

    ## Error behavior
    What happens on bad input, failure, or partial completion.

    ## Test plan
    How each requirement gets verified: specific tests or runnable checks.
