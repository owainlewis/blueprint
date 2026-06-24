# Goal Ideas For Blueprint

This document collects high-quality ways to use `/goal` to improve Blueprint itself.

It is intentionally short.

Most useful agent work should still be a normal prompt, a Blueprint skill, or a scheduled loop.

`/goal` is for the cases where Codex should keep checking a completion condition and continue without a new human prompt.

## Prompt, Goal, Or Loop

Use this rule before reaching for `/goal`.

| Primitive | Use When | Blueprint Example |
| --- | --- | --- |
| Prompt | One bounded pass is enough. | "Review the README and list unclear sections." |
| Goal | The agent should keep repairing and re-checking until a condition is true, blocked, or budget-limited. | "Make README, AGENTS, CLAUDE, guides, and skills agree on the installed skill set." |
| Scheduled loop | The trigger is time or external state. | "Every Friday, check for docs drift and report findings." |
| Issue-tracker loop | Labels, comments, PRs, and assignments are the state machine. | "Claim one `agent:ready` issue and run `task-to-pr`." |
| Skill invocation | Blueprint already has the workflow. | Use `review`, `task-to-pr`, `multitask`, `pr-to-ready`, or `loop-design` directly. |

A goal makes sense when the valuable part is the repeated self-check:

```text
Is the condition true yet?
If not, what is the next safe bounded action?
If continuing is unclear or unsafe, what evidence should be reported?
```

If the task does not need that loop, it is probably just a prompt.

## Goal Template

```text
/goal <outcome>, verified by <specific evidence>, while preserving <constraints>.
Use <allowed files, tools, and boundaries>.
Between iterations, <how to choose the next bounded action>.
If blocked, repeated failures occur, or no valid paths remain, stop with <evidence gathered>, <blocker>, and <input needed>.
```

Good goals include:

- a concrete end state
- a verifier the agent can actually run
- one bounded action per pass
- scope boundaries
- a human-decision stop
- a budget or repeated-failure stop

## Recommended Goals

These are tangible goals that should improve this repository.

They are written as prompts you can paste into Codex.

### 1. Documentation Consistency Repair

Use this when README, AGENTS, CLAUDE, guides, and skill files may describe different workflows.

This is a real goal because the agent must find a mismatch, patch it, re-scan, and continue until no unexplained contradictions remain.

```text
/goal Blueprint's public workflow docs are internally consistent, verified by targeted `rg` scans and a final diff summary showing no unexplained mismatch in skill names, workflow names, loop phases, or install guidance.

Use README.md, AGENTS.md, CLAUDE.md, guides/*.md, skills/*/SKILL.md, and agents/code-reviewer.md.
Between iterations, find the smallest real contradiction, patch only the owning doc, then re-run the relevant scan.
Preserve current skill names and public workflow intent.
Do not edit generated files, examples, lockfiles, vendored files, or unrelated prose.
Stop after 6 patches, if the same mismatch repeats twice, or if resolving a contradiction would change the intended product direction.
Report changed files, scans run, remaining risks, and any needs-human decision.
```

Good verification scans:

```bash
rg "goal-skill|loop-design|task-to-pr|multitask|pr-to-ready|address-pr-feedback|codex-run-loop" README.md AGENTS.md CLAUDE.md guides skills
rg "agent:ready|agent:working|agent:complete|needs:spec|needs:human|blocked" AGENTS.md guides
```

### 2. Skill Quality Repair

Use this when the skill set has drifted from Blueprint's own quality bar.

This is a real goal because the agent works one skill at a time, patches only clear failures, and re-checks each changed skill before moving on.

```text
/goal Every skill file passes Blueprint's review bar, verified by a report that marks each skill pass, patched, or needs-human.

Use REVIEW.md, AGENTS.md, and skills/*/SKILL.md.
For each skill, check trigger clarity, scope boundary, verification evidence, failure behavior, and unnecessary ceremony.
Between iterations, patch one skill only when the fix is clear and behavior-preserving, then re-read the changed skill before continuing.
Keep skills short and portable.
Do not change skill names, public workflow contracts, generated files, or examples.
Stop after 5 skill patches, if a skill's intended contract is ambiguous, or if concision would weaken safety.
Report pass/patched/needs-human for every inspected skill, plus checks run.
```

### 3. Skill Metadata Normalizer

Use this when installed skills need predictable frontmatter for discovery.

This is a good goal because the verifier is concrete and the agent can keep normalizing until every skill matches the schema or an intentional exception appears.

```text
/goal Every skill in skills/*/SKILL.md has consistent required frontmatter, verified by a parser or explicit scan confirming `name`, `description`, `user-invocable`, and `argument-hint` fields are present and consistently ordered.

Use skills/*/SKILL.md only.
Between iterations, fix one skill's frontmatter, then re-run the metadata check.
Do not rewrite skill bodies except where a field value needs a clearer description.
Do not change skill names or public trigger behavior.
Stop when all skill metadata is consistent, after 10 skill patches, or if a skill intentionally needs a different schema.
Report the command or scan used, files changed, and any intentional exception.
```

Useful verification:

```bash
rg -n "^(name|description|user-invocable|argument-hint):" skills/*/SKILL.md
```

### 4. Markdown Link Repair

Use this when local docs have drifted after file renames or guide changes.

This is a real goal because link repair is naturally iterative: check, fix one class of broken links, check again.

```text
/goal All local Markdown links in README.md, AGENTS.md, CLAUDE.md, REVIEW.md, guides/*.md, and skills/*/SKILL.md resolve, verified by a link checker or documented fallback scan.

Use repo-authored Markdown only.
Between iterations, identify one broken local link or stale path, patch the owning source, then re-run the link check.
Do not validate external URLs unless network access and policy are explicit.
Do not edit generated files or examples unless the broken link is in the source of truth.
Stop when all local links resolve, after 8 link fixes, or if a target appears intentionally future-facing.
Report the checker used, fixed links, skipped links, and any needs-human target.
```

### 5. Example Artifact Boundary Repair

Use this when examples and docs are unclear about what is source material, generated output, or hand-editable guidance.

This is a real goal because the agent may need to inspect several files, patch one boundary explanation, and re-check that the docs no longer contradict each other.

```text
/goal Blueprint's example artifact boundaries are clear and consistent, verified by docs that distinguish source prompts, regeneration scripts, generated examples, and hand-edited examples without contradiction.

Use README.md, AGENTS.md, guides/*.md, examples/input.md, examples/regenerate.sh, examples/rag-chatbot/*.md, and examples/dispatch-control-plane/*.md.
Between iterations, find one unclear or contradictory boundary, patch the owning doc, and re-scan for references to generated examples, regenerate scripts, and no-edit policy.
Do not regenerate examples.
Do not edit generated examples unless the repo already treats them as hand-edited sources.
Stop if the intended source of truth cannot be inferred from the repo.
Report the boundary rules, files changed, scans run, and any needs-human decision.
```

### 6. Release Dry-Run Repair

Use this before tagging a Blueprint release.

This is a goal because release readiness often reveals a sequence of small blockers, and the agent should repair clear local blockers while stopping before publish authority.

```text
/goal Blueprint is locally ready for a release dry run, verified by a report covering changed skills, docs consistency, example boundaries, install manifest expectations, and unresolved risks.

Use git status, git diff, README.md, AGENTS.md, CLAUDE.md, guides/*.md, skills/*/SKILL.md, agents/code-reviewer.md, and examples/.
Between iterations, fix one clear local release blocker, run the relevant check, and update the release-readiness evidence.
Do not tag, publish, push, edit lockfiles, or change generated files.
Do not invent a changelog if the repo prefers generated release notes.
Stop when local readiness is proven, after 5 fixes, if publish tooling or network access is required, or if release policy needs human approval.
Report ready/not ready, fixes made, checks run, and the exact human decision needed before release.
```

### 7. Working Tree Reviewability Repair

Use this when the repo has several local changes and you want it made reviewable without losing human work.

This is a goal because the agent must inspect current state, group changes, fix only safe inconsistencies, and stop rather than discard unrelated work.

```text
/goal The working tree is reviewable, verified by `git status --short` plus a report that explains every remaining changed file as intended, unrelated, generated, blocked, or needs-human.

Use git status, git diff, repo instructions, and touched files only.
Between iterations, inspect one changed-file group, fix only clear inconsistencies inside that group, and update the reviewability report.
Never discard, revert, reset, checkout, or overwrite user changes.
Do not stage, commit, push, or edit unrelated files.
Stop when every changed file is explained, after 4 repair patches, or if a change belongs to another human task.
Report groups, files touched, checks run, and what should happen next.
```

## Adjacent Non-Goals

These are useful, but they are not good `/goal` examples.

Keep them out of the goal demo set.

### Good Prompts

Use normal prompts for one-pass work:

- create a repo map
- write a release notes draft
- inventory runnable checks
- audit public claims
- write a quickstart
- compare Claude, Codex, and Hermes docs
- draft a video or blog outline

These can still be excellent prompts.

They just do not need persistent continuation.

### Good Scheduled Loops

Use Codex Automations, thread wakeups, GitHub Actions, cron, or another scheduler when time or external state is the trigger:

- weekly maintenance sweep
- PR feedback watcher
- stale claim recovery
- post-release verification
- daily low-risk fixer

The prompt inside the scheduled loop can call `pr-to-ready`, `task-to-pr`, or another skill.

The schedule owns the wakeup.

The goal should not sit there pretending to be a timer.

### Good Skill Invocations

Use the skill directly when Blueprint already has the workflow:

- `task-to-pr` for one ready ticket
- `multitask` for several independent tickets
- `pr-to-ready` for an open PR with feedback
- `review` for a release diff
- `loop-design` for designing a new loop

Wrapping these in `/goal` is only useful when a coordinator must repeat the skill until a larger condition is true.

## Recommended Order

Start with goals that touch docs only.

1. Documentation Consistency Repair.
2. Skill Metadata Normalizer.
3. Skill Quality Repair.
4. Markdown Link Repair.
5. Example Artifact Boundary Repair.
6. Working Tree Reviewability Repair.
7. Release Dry-Run Repair.

That order moves from low-risk, mechanical cleanup toward broader release judgment.

It also demonstrates the real value of `/goal`: repeated repair against evidence, not a long prompt with a slash command.
