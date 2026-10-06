# Changelog

## Unreleased

### Added

- `/requirements` for system product needs and `/spec` for one feature or major change. The spec serves as the ticket.
- `/factory` for delivery through gated merge, reusing `/task-to-pr`. Explicit invocation grants scoped merge authority.
- `/codex-issue-coordinator` for GitHub issue batches across visible Codex workers.
- `/html-doc` for verified static HTML views of Markdown requirements and designs.
- Public guides, contribution and security guidance, issue forms, and repository CI checks.

### Changed

- `/architecture` designs the intended system and data model, with decision status separate from implementation status. Claims about existing code require verification.
- Delivery includes tests, fresh independent review, CI, and repairs. `/task-to-pr` leaves passing PRs open by default; explicit `/factory` or `/codex-issue-coordinator` use grants scoped merging after all gates and required approvals pass.
- Dependent tasks may stack on open, independently reviewed prerequisite PRs. The Codex coordinator waits for prerequisite merges instead.
- Requirements, specs, planning, tests, and review preserve stable requirement, acceptance, and invariant IDs.
- Replaced the legacy examples with one task-list project showing requirements, architecture, and a feature spec.
- Removed duplicated review and setup guidance. Migration keeps upgrade instructions without repeating the skill inventory.

### Removed

- `/design`, replaced by `/spec` for features and `/requirements` for system product needs.
- `/milestone`. Pass a milestone to `/task-to-pr` instead.
- The example prompt-printing script and its pre-push reminder. Example maintenance is described in `examples/README.md` and contribution guidance.
