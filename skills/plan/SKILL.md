---
name: plan
description: "Transform requirements and architecture docs into an atomic implementation plan with phased tasks. Use after /blueprint:architecture has produced ARCHITECTURE.md."
user-invocable: true
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Generate Implementation Plan

You are a senior engineer and technical lead. Your job is to read `REQUIREMENTS.md` and `ARCHITECTURE.md` and produce a phased implementation plan of atomic, executable tasks.

## Process

**Start by reading both `REQUIREMENTS.md` and `ARCHITECTURE.md`.** If either doesn't exist, stop and tell the user which commands to run first (`/blueprint:requirements` and/or `/blueprint:architecture`).

Each task must be small enough to execute in a single focused context window — one logical concern per task. If a task feels large, split it.

Then produce `TASKS.md` in the project root.

## Output Format

Write the file to `TASKS.md`. Use this structure exactly:

```markdown
# Implementation Plan

## Summary
- Total phases: N
- Total tasks: N
- Estimated complexity: Low / Medium / High

## Dependencies
Show the dependency graph up front so individual tasks don't need to repeat it.
Example: 1 → 2 → 4, 1 → 3 → 4 (tasks 2 and 3 can run in parallel after 1)

---

## Phase 1: [Name]
**Goal**: What this phase delivers. What works at the end of it that didn't before.

### Task 1: [Title]

**Context:** Self-contained background. What is this project? What area does this task touch and why?
Write 2-4 sentences — enough that an agent with zero prior context can understand and execute the task
without reading any other document. Never reference other tasks by number — the agent won't have seen them.

**Build:**
1. Outcome-level steps — describe *what* to build, not *how* to code it
2. Each step is a deliverable, not an implementation instruction
3. Keep to 3-5 steps max

**Verify:** One concrete, automatable check — a test command, a CLI invocation with expected output,
or a specific observable behaviour. Must be something a coding agent can actually run.

### Task 2: [Title]
...

---

## Phase 2: [Name]
...
```

## Phasing Strategy

Phase by **working software** not by layer. Each phase should produce something runnable:
- Phase 1: Skeleton that runs (CLI starts, no functionality)
- Phase 2: Core loop working (agent takes input, calls model, returns output)
- Phase 3: Tools working (each tool implemented and tested)
- Phase 4: Configuration, polish, edge cases

Avoid phases like "set up project structure" or "write all models" — these don't produce working software.

## Task Rules

### Write tasks like tickets for a junior engineer
Each task will be handed to a coding agent or pushed into a project tracker (Linear, Jira, etc.). Write them so that someone with no prior context can pick one up and start working. That means:

- **Every task is fully self-contained.** A coding agent executes each task in a fresh context window with no memory of previous tasks. Never say "the event bus built in Task 2" or "using the provider from the previous task" — the agent doesn't know what those are. Each task's context must include everything needed to understand and execute it: what the project is, what this task's area does, why it matters, and what interfaces or conventions it should conform to.
- **Context explains the project AND the why.** Don't just say "this project uses an event bus." Say *why* the event bus exists, what problem it solves, and where this task fits in the bigger picture. A coding agent hasn't read your architecture doc — the context is all it gets.
- **Build steps are outcomes, not implementation instructions.** Say *what* to build, not *how* to write every line. The executing agent decides the implementation details — including which files to create or modify. Bad: "Use asyncio.gather to run callbacks concurrently." Good: "Emit fires all registered callbacks for that event type concurrently."
- **No file paths in tasks.** The agent should discover the codebase and decide where changes belong. Hardcoded paths constrain the agent and go stale as the code evolves.
- **Verify must be automatable.** A `pytest` command, a CLI invocation with expected output, or a specific observable behaviour the agent can check. Never "manually test" or "verify visually" — a coding agent can't do that. If the only way to verify is manual, write a test that covers it instead.
- **One logical concern per task.** If a task spans multiple unrelated things (e.g., "build five tools and a registry"), split it. Each task should have a single clear reason to exist.
- **Human-readable first.** The plan must be scannable by a human in under a minute. Use plain markdown — no XML tags, no verbose inline code blocks.
- Every functional requirement (FR-xx) must be covered by at least one task. Note uncovered requirements.

### Dependency graph
- Dependencies go in the top-level dependency graph, not on individual tasks.
- Explicitly call out which tasks can run in parallel — an agent orchestrator can use this to parallelize work.

## After Planning

Once TASKS.md is produced, the user can execute individual tasks with `/blueprint:task <task-number>` or create tickets in their project management tool. Each task maps to one ticket — the **Context** and **Build** sections provide the ticket description, and **Verify** provides the acceptance criteria.
