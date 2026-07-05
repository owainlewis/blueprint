---
name: design-doc
description: "Write a short design document for unclear or important architecture decisions before implementation. Use when a decision is expensive to reverse or crosses team boundaries."
user-invocable: true
argument-hint: "<system, feature, architecture question, repo path, or design brief>"
---

# Design Doc

1. Read the brief and any linked docs, code, or plans. Ask a question, one at a time with a recommended answer, only when a missing fact would change the design.
2. Write `docs/<design-slug>/design.md`, 1-3 pages, using the template below. Omit sections that don't apply.
3. Stop after writing. Don't continue into spec, plan, or implementation until the human confirms.

## Rules

- Focus on decisions code won't explain later.
- Don't copy full schemas, APIs, or code unless the exact shape is central.
- Leave Status as Draft and Decision empty. Both are filled during review.

## Template

    # <Title>

    **Status:** Draft | In review | Approved
    **Author:** <name>  **Date:** <date>

    ## Summary
    One paragraph: the problem, the proposed solution, and why.

    ## Goals
    What this design must achieve.

    ## Non-goals
    What it deliberately does not solve.

    ## Proposed design
    How it works. Structure, data flow, key interfaces. Diagram only if it clarifies.

    ## Alternatives and tradeoffs
    Each option considered, why it lost. This is the section reviewers judge.

    ## Risks
    What could go wrong and how it's mitigated.

    ## Rollout
    How it ships: migration, flags, backout.

    ## Open questions
    Decisions still needed and from whom.

    ## Decision
    Filled in after review: what was decided, by whom, when.
