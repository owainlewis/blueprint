# Changelog

## Unreleased

### Added

- `/requirements` for system product needs and `/spec` for one feature or major change. The spec serves as the ticket.
- `/codex-issue-coordinator` for GitHub issue batches across visible Codex workers.
- `/html-doc` for verified static HTML views of Markdown requirements and designs.
- Public guides, contribution and security guidance, issue forms, and repository CI checks.

### Changed

- The README leads with Blueprint's take and a four-step quick start, then groups the skills by stage: Design, Plan, Build, Verify. Verify is Test (does it work?) then Review (is it right?).
- New [verification guide](guides/verification.md) for setting up testing and review in any repository.
- `/architecture` is now a fill-in template with a required Mermaid diagram and a decisions table.
- `/architecture-review` and `/plan` are shorter, in plain words. `/plan` keeps its task template.
- `/requirements` is now a fill-in template built on user stories, each with a `REQ-n` ID and "Done when" conditions.
- `/spec` is now a fill-in template: a short PRD for the feature (Problem, Goals, Non-goals, User journeys in Given, When, Then form) plus the Technical design an agent needs, with a diagram for the human reviewer, then a Decisions table that names each rejected alternative, Risks and rollout, Acceptance, and Open decisions. Each acceptance row names the journey, requirement, or invariant it proves. The template is its own file, `skills/spec/references/spec.md`, with an Author, Status, and Date header.
- `/review` runs two parts, spec fit and correctness, with bad-input probes, a revert check for new tests, and a fixed verdict block. It can use another agent CLI (`codex exec` or `claude -p`) as the independent reviewer.
- `/test` runs every repository check until green before proving acceptance, and runs the real app the way a user would: the repository's own end-to-end tests first, otherwise a real browser, a terminal, or HTTP requests.
- `/task-to-pr` reads its skills by file path so it works the same in Claude Code and Codex, and stops after three repair rounds on the same failure.
- The PR template uses What, Why, What changed, Verification, and Risk.
- `/requirements` and `/architecture` keep their templates in `references/`, with the same Author, Status, and Date header as `/spec`. Status is Draft, Proposed, In Review, or Approved in all three; "Accepted" is now "Approved".
- `/review` and `/architecture-review` say how each finding was proven and accept "no findings" as a result. `/architecture-review` ends with a fixed verdict block. `/review` derives bad inputs from the contract and no longer forbids the temporary revert it asks for.
- `/improve` deletes first and checks that a reader can trace each important value.
- All eleven skills are opt-in, with Codex and Claude Code invocation settings. Selected workflows retain their internal skill calls; ordinary code requests no longer require `/task-to-pr`.

- `/architecture` designs the intended system and data model, with decision status separate from implementation status. Claims about existing code require verification.
- Delivery includes tests, fresh independent review, CI, and repairs. `/task-to-pr` leaves passing PRs open by default; explicit `/factory` or `/codex-issue-coordinator` use grants scoped merging after all gates and required approvals pass.
- Dependent tasks may stack on open, independently reviewed prerequisite PRs. The Codex coordinator waits for prerequisite merges instead.
- Requirements, specs, planning, tests, and review preserve stable requirement, acceptance, and invariant IDs.
- Replaced the legacy examples with one consulting CRM showing requirements, architecture and data flow, a data model, a feature spec, and a plan with vertical slices.
- Removed duplicated review and setup guidance. Migration keeps upgrade instructions without repeating the skill inventory.

### Removed

- `/factory`. Ask `/task-to-pr` to merge instead.
- `/design`, replaced by `/spec` for features and `/requirements` for system product needs.
- `/milestone`. Pass a milestone to `/task-to-pr` instead.
- The example prompt-printing script and its pre-push reminder. Example maintenance is described in `examples/README.md` and contribution guidance.
