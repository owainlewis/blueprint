---
name: design
description: "Designs what to build and how it should work, including requirements, acceptance criteria, interfaces, data, errors, technical choices, constraints, risks, and scope. Use when the user asks to design or architect a feature, write a spec or design doc, define requirements, or resolve important product or technical decisions before implementation."
user-invocable: true
argument-hint: "<feature, problem, or brief>"
---

# Design

## Workflow

1. Read the request, repository instructions, relevant code, and linked material.
2. Resolve choices that would change behavior, interfaces, data, errors, security, operations, or tests. Ask only questions whose answers materially change the design. Recommend an answer when asking.
3. Write `docs/<feature-slug>/design.md` using the shape below. Keep it short and omit sections that do not apply.
4. Run the review pass. Fix what you can. List the rest under Open questions.
5. Stop for human review. Do not plan or implement.

## Document shape

```markdown
# <Title>

## What and why
The problem, who it affects, and what changes once this ships. Plain prose.

## How it works
Walk one real case from start to finish. Name the thing that arrives, what handles it, what gets written down, and what the user sees. A reader should be able to picture the system running before they read any requirements.

## Decisions
For each choice that could reasonably have gone another way: what you chose, what you rejected, and what it costs. One short paragraph each. Skip the choices nobody would argue about.

## Invariants
Numbered statements that must hold at all times. These are what a reviewer checks a diff against, so keep them short and testable.

## Requirements
- Observable behavior and constraints.

## Interfaces and data
APIs, commands, events, schemas, config, compatibility, or migration.

## Naming and identity
How every durable name or ID is derived, what happens when derivation fails, and what happens if the source of the name changes after state exists.

## Failure behavior
What can fail, what state it moves to, whether it retries and how, and how it recovers. Say what happens when everything fails at once, not just one thing.

## Limits and budgets
Anything shared and finite: rate limits, connections, disk, memory, cost. Say what happens when it runs out.

## Acceptance criteria
- Testable conditions that prove the work is complete.

## Test approach
How each invariant and each important requirement will be proved.

## Risks
- Risk and mitigation.

## Open questions
- Question, and whether it blocks starting work.

## Out of scope
- Related work this design does not include.
```

## Writing rules

- Prose is the default. Use bullets only for content that is genuinely a list, such as config fields, acceptance criteria, risks, and out of scope.
- A bullet cannot carry a decision by itself. Write the reason next to it in a sentence.
- Use plain words. Say "the process crashed" instead of "an availability event occurred". Prefer short sentences.
- Define a term the first time you use it, or do not use it.
- Prefer one clear recommendation over a list of options.
- Record rejected options only when the tradeoff matters later.
- Do not repeat the same fact in several sections with different wording.
- Do not use em dashes.

## Review pass

Reread the draft once and check each category. Fix any gap you can resolve from the available evidence.

1. **Names and identity.** Where does every durable identifier come from? What happens when it is missing, ambiguous, or changes after state exists?
2. **Failure and recovery.** What creates a bad state? Does the system retry, with what backoff, and can it recover without a restart? What happens when everything is bad at startup?
3. **Shared resources.** What finite resource does the feature consume? State the budget and the behavior at the limit.
4. **Timing and fairness.** Replace words such as "eventually" and "will not starve" with a bound someone can test.
5. **Lifecycle.** Cover config reload, enable and disable behavior, work already in flight, and shutdown.
6. **Undefined terms.** Define words that carry a specific meaning in the design.
7. **Either/or acceptance criteria.** Do not allow both sides of "recovers or retains" to pass. Choose one observable behavior.

Put anything you cannot resolve under Open questions and state whether it blocks task breakdown.
