<div align="center">

# Blueprint

**A small, principles-first workflow for AI coding.**

Clear decisions. Bounded work. Real proof. Independent review.

</div>

Blueprint gives coding agents the engineering boundaries that matter without turning software delivery into a catalogue of tiny skills. It separates repository policy, reusable phases, and end-to-end workflows so each instruction has one clear job.

## Start with the work, not the process

Use the smallest entry point that resolves the uncertainty in front of you.

| If you need to… | Start with | Result |
| --- | --- | --- |
| Explain, document, or audit how an implemented system works | `/architecture` | A verified current-state report or architecture reference |
| Specify a feature or change to part of a system | `/design` | A reviewed design with requirements and acceptance criteria |
| Split a decided feature into work for several agent runs | `/plan` | Ordered tasks in chat or tracker tickets |
| Take one task through delivery | `/task-to-pr` | A tested, reviewed, green pull request |
| Complete every issue in a GitHub milestone | `/milestone` | One green pull request at a time, with human merge checkpoints |
| Prove a change works | `/test` | Acceptance criteria mapped to evidence |
| Get an independent second opinion | `/review` | Findings and a pre-merge verdict from a fresh subagent |
| Simplify existing code without changing behavior | `/improve` | Clearer, smaller, better-structured code |

Small, decided work can go straight to `/task-to-pr`. Use `/architecture` for implemented reality, `/design` when proposed behavior needs review, and `/plan` only when the work needs splitting.

## How Blueprint fits together

```mermaid
flowchart TB
    Existing([Implemented system]) --> Architecture["/architecture"]
    Architecture --> Current["Current architecture"]

    subgraph Decide["Decide only as much as needed"]
        Idea([Idea or problem]) --> Design["/design"]
        Idea -->|already decided| Task([One task])
        Current -.-> Design
        Design -->|one task| Task
        Design -->|needs splitting| Plan["/plan"] --> Task
    end

    subgraph Deliver["Deliver with /task-to-pr"]
        Task --> Isolate["isolate"] --> Code["code"] --> Test["/test"] --> Review["/review"]
        Review -->|findings| Fix["fix"] --> Test
        Review -->|clean| Publish["publish PR"] --> Validate["CI + current feedback"]
        Validate -->|failure or finding| Fix
        Validate -->|clean| PR["green PR"]
    end

    PR --> Merge([Human merge])
```

`/architecture` is a current-system documentation path, and `/improve` is a behavior-preserving maintenance path. Neither is a step every change must pass through.

The model has two layers:

1. **Repository instructions define policy.** `AGENTS.md` says what good work means in a codebase.
2. **Skills define phases and workflows.** Each skill has one durable engineering outcome and a clear stopping point. `/task-to-pr` and `/milestone` compose the phases into delivery paths.

## The six phase skills

| Skill | Owns | Stops when |
| --- | --- | --- |
| `/architecture` | Current system context, invariants, components, dependencies, flows, boundaries, operations, and verified limitations | The requested report or architecture reference is ready for human review |
| `/design` | A proposed feature or system-part specification: executive summary, system fit, behavior, boundaries, decisions, requirements, proof, and scope | The design is ready for human review |
| `/plan` | Vertical, ordered tasks and optional milestones | The work is ready to hand off |
| `/test` | Automated checks, failure paths, and real-browser proof when relevant | Every criterion is pass, fail, or explicitly unverified |
| `/review` | Independent review of correctness, security, regressions, complexity, and proof | Findings and a verdict are reported |
| `/improve` | Behavior-preserving simplification of existing code | Relevant checks prove behavior was preserved |

Writing code is a base capability, not a phase skill. Branching, committing, opening a PR, debugging, TDD, browser checking, and addressing feedback are techniques or workflow steps, not separate product concepts.

## One task to one pull request

[`skills/task-to-pr/SKILL.md`](skills/task-to-pr/SKILL.md) is the single authority for delivery. Given a ticket, task, or existing PR, it:

1. resolves the source and isolates work before editing;
2. implements the smallest complete change;
3. runs `/test` and independent `/review` loops;
4. creates Conventional Commits and opens or updates a reviewer-focused PR that explains what changed, why it matters, what to review, and the evidence checklist;
5. waits for CI, handles feedback that exists, and records evidence;
6. stops at a green, mergeable PR for a human to merge.

It does not wait forever for future human feedback, manufacture tracker artifacts for trivial work, or merge without explicit permission.

## One milestone to completed issues

`/milestone` is the release-slice workflow. It reads a GitHub milestone, orders open issues by dependency and risk, then runs `/task-to-pr` for one issue at a time. It stops for human merge after each green pull request unless the user explicitly delegates merging for that run.

## Install

Install all eight skills:

```bash
npx skills add owainlewis/blueprint
```

Upgrading from the older skill catalogue? Follow the [migration guide](MIGRATION.md). Removed skills can remain installed after a normal update, so the cleanup step matters.

## Repository map

```text
skills/                 six phase skills and two delivery workflow skills
AGENTS.md                portable repository policy
CLAUDE.md                Claude Code adapter
REVIEW.md                review standard for Blueprint itself
MIGRATION.md             clean upgrade from the old catalogue
examples/                reviewed design and planning examples
```

## Examples

The RAG chatbot example follows one idea through the decision flow:

1. [rough project notes](examples/input.md)
2. [reviewed design](examples/rag-chatbot/design.md)
3. [captured chat plan](examples/rag-chatbot/plan.md)

For a larger system-part specification, read the [Dispatch local control-plane design](examples/dispatch-control-plane/design.md).

## Principles

- **Encode process, not knowledge.** Give agents outcomes, constraints, and proof; trust them with local mechanics.
- **One skill per phase or delivery outcome.** Skills share one installation and invocation model.
- **Separate current state from proposals.** Architecture documents describe verified implemented reality. Design documents specify future changes.
- **Keep changes reviewable.** Deliver one focused, self-contained outcome with its related proof. A reviewer should not need to separate unrelated work first. Separate refactoring when it would obscure the behavior diff. Small local cleanup may remain when it makes the changed behavior easier to review.
- **Use concrete review standards.** Check correctness. If the same outcome and proof can be delivered with less state, indirection, duplication, or operational work, request the simpler design. Do not block on personal taste. Cite technical evidence or repository conventions.
- **Proof is part of the work.** Test changed behavior, failure paths affected by the change or named in its acceptance criteria, and behavior a refactor must preserve. If the change has no executable behavior, or the affected behavior cannot be exercised through available automated interfaces, state the concrete reason and substitute evidence.
- **Use the real surface.** Browser behavior is checked in a browser. Live PR feedback is read from the PR.
- **Fix the source of truth.** If implementation exposes a bad requirement, update the task or design before continuing.
- **Prefer less.** Keep the smallest complete change, shortest useful instruction, and no duplicate entry points.
- **Keep irreversible judgment human.** Agents prepare the decision. Humans review designs and merge pull requests unless they explicitly delegate it.

Blueprint is not an issue tracker, agent framework, release system, or reviewer-persona library. It is a compact engineering process for capable coding agents.
