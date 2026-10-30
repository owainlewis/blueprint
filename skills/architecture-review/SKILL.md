---
name: architecture-review
description: "Reviews a technical proposal before any code is written: an architecture, spec, RFC, ADR, or design issue. Finds choices that would make it wrong, unsafe, or impossible to prove, and the open questions that block building it."
user-invocable: true
argument-hint: "[architecture, spec, RFC, ADR, or issue]"
disable-model-invocation: true
---

# Architecture review

Find the choices that would make a design wrong, unsafe, or impossible to prove, while they are still cheap to change. Judge the decisions, not the document's length or format.

## Reviewer

Someone who did not write the proposal: a fresh subagent, or another agent CLI run read-only (`codex exec "<prompt>"` or `claude -p "<prompt>"`). If neither is available, say review is blocked. The reviewer changes nothing.

## Steps

1. Read the proposal, `REQUIREMENTS.md`, `ARCHITECTURE.md`, and the code, schemas, and config it touches. Check every claim about the current system against them.
2. Write down the problem, who it affects, the intended outcome, and the main tradeoff. Flag any the proposal leaves unclear.
3. Walk one real request from input to what the user sees, including what happens when a step fails, is retried, or runs twice at once.
4. Check data ownership, interfaces, migrations, rollback, security (auth, untrusted input, secrets), and the scale the proposal claims.
5. Look for a simpler design that gets the same result with less state or fewer moving parts.
6. Check that each important rule and failure has an acceptance check.

## Findings

Report only what could change the design:

- **Blocker:** unsafe, contradicts the goal or the current system, or cannot recover from a likely failure.
- **Important:** two capable engineers could build it in ways that differ for users, data, or security.

For each: where it is, what goes wrong and when, the evidence, and the smallest fix or your recommended answer. Skip wording preferences and questions that cannot change the design.

## Verdict

End with `Approve`, `Request changes`, or `Blocked` (missing context or reviewer), then what you could not verify. A detailed document is not a reason to approve.
