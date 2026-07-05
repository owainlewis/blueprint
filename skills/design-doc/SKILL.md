---
name: design-doc
description: "Write a short design document for unclear or important architecture decisions before implementation."
user-invocable: true
argument-hint: "<system, feature, architecture question, repo path, or design brief>"
---

# Design Doc

Goal: write a short design doc for human review.

## Workflow

1. Read the brief, linked docs, code, specs, plans, and design notes. Derive a kebab-case design slug if needed.
2. Identify goals, what not to solve, limits, options, tradeoffs, risks, and open questions. Ask one question at a time, with a recommended answer, only when a missing fact would change the proposed design.
3. Write `docs/<design-slug>/design.md`. Prefer 1-3 pages.
4. Include: status, summary, background, goals, what not to solve, limits, proposed design, other options, tradeoffs, risks, rollout, open questions, and decision. Omit sections that do not apply.
5. Stop after writing. Do not continue into spec, plan, or implementation until the human confirms the design.

## Rules

- Make the design choice easy to review.
- Focus on decisions code will not explain later.
- Use diagrams only when they clarify structure, flow, or deployment.
- Do not copy full schemas, APIs, or code unless the exact shape is central.
