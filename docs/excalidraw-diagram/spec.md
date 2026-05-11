# Excalidraw Diagram Skill Spec

## What

Add a new `excalidraw-diagram` skill that helps an agent turn a repo, spec, architecture, workflow, or concept into a clear Excalidraw diagram. The skill should produce an editable diagram artifact that teaches the idea visually, using simple labels, deliberate layout, and source-grounded claims.

## Context

Blueprint now has `explain-visually`, which creates responsive HTML explainers, and `browser-verify`, which checks rendered browser output. A separate `excalidraw-diagram` skill is useful when the desired artifact is a standalone diagram rather than a full HTML page.

The implementation should use `coleam00/excalidraw-diagram-skill` as a reference point, especially its emphasis on choosing a visual pattern, making a diagram that communicates a specific claim, and validating the rendered output. Blueprint should borrow the useful craft, not the full length or taxonomy.

The new skill should follow the existing Blueprint skill shape described in `docs/skill-anatomy.md`: frontmatter, a short role/introduction, ordered workflow, and compact rules. It should live at `skills/excalidraw-diagram/SKILL.md`.

## Requirements

- The skill must be named `excalidraw-diagram`.
- The skill must be user-invocable.
- The skill must accept source material such as a repo, spec, architecture, workflow, concept, PR, or pasted text.
- The skill must create a clear Excalidraw diagram that explains the source material visually.
- The skill must default to an editable `.excalidraw` artifact unless the user requests another format.
- The skill must choose the diagram type that best explains the idea: flow, system map, lifecycle, before/after, dependency map, or concept model.
- The skill must state the core claim or lesson before drawing.
- The skill must use simple, concrete labels rather than abstract phrases.
- The skill must ground claims in the source material and avoid decorative diagrams that do not teach.
- The skill must verify that the output file is valid JSON when writing `.excalidraw`.
- The skill must render or open the diagram for visual inspection when local tooling is available.
- The skill must report where the diagram was written and what idea it is meant to teach.

## Design

Create `skills/excalidraw-diagram/SKILL.md` with frontmatter:

- `name: excalidraw-diagram`
- description that mentions Excalidraw diagrams and common triggers such as "make a diagram", "diagram this", "visualize this architecture", and "turn this into Excalidraw"
- `user-invocable: true`
- `argument-hint: "<repo, spec, architecture, workflow, concept, or source material>"`

Use this workflow:

1. **Understand**: read the source, identify the audience, core claim, entities, relationships, flow, and what the reader should remember. For repo or architecture diagrams, gather evidence from files before drawing.
2. **Choose Shape**: select the smallest visual pattern that explains the idea. Prefer before/after, flow, system map, lifecycle, dependency map, concept model, or layered architecture.
3. **Draft**: create an Excalidraw diagram with a clear hierarchy, readable labels, aligned shapes, and enough spacing.
4. **Verify**: ensure the artifact is valid JSON. When tooling is available, render or open it and inspect for overlapping text, unclear labels, missing relationships, broken arrows, or decorative clutter.
5. **Report**: state the output path, the chosen diagram shape, and the core idea the diagram teaches.

The skill should include rules that mirror the lessons learned from `explain-visually`:

- Explain, do not decorate.
- One diagram should teach one main idea.
- A diagram should make a claim, not merely list parts.
- Use simple nouns and verbs in labels.
- Prefer fewer nodes with clearer relationships.
- Show transformation when the source is about change.
- Use grouping, arrows, and spatial position to carry meaning.
- Avoid tiny labels, overlapping elements, and dense walls of nodes.
- Use restrained visual style: hand-drawn Excalidraw feel, few colors, consistent shape language, and clear hierarchy.
- If the diagram would need multiple unrelated ideas, split it into multiple diagrams.

## Decisions

- **Choice**: Add `excalidraw-diagram` as a separate engineering productivity skill rather than extending `explain-visually`.
  - **Alternatives considered**: Extend `explain-visually`; add a generic `visualize` skill.
  - **Why this one**: Excalidraw output is a different artifact from responsive HTML. A focused skill keeps routing clear and avoids bloating `explain-visually`.
  - **Reversible**: Yes. If the two skills overlap too much, `excalidraw-diagram` can later be merged into `explain-visually`.

- **Choice**: Default output is editable `.excalidraw`.
  - **Alternatives considered**: PNG/SVG export, embedded Markdown, HTML canvas.
  - **Why this one**: The user asked for Excalidraw, and editable source is more useful for iteration than a static export.
  - **Reversible**: Yes. The skill can later add optional exports without changing the core workflow.
  - **Assumption:** Agents can produce Excalidraw-compatible JSON directly or through available local tooling.

- **Choice**: Require JSON validation and opportunistic visual inspection.
  - **Alternatives considered**: Only validate JSON; always require browser rendering.
  - **Why this one**: JSON validity catches broken artifacts, but visual diagrams often fail through overlap, bad spacing, or unclear arrows. Visual inspection should happen when tooling is available, but the skill should not require a specific renderer.
  - **Reversible**: Yes. If the repo adopts a standard Excalidraw renderer, rendering can become mandatory.

- **Choice**: Treat `excalidraw-diagram` as an engineering productivity skill in docs, not part of the delivery spine.
  - **Alternatives considered**: Put it under Design or Review.
  - **Why this one**: The skill communicates ideas; it does not directly move code through delivery.
  - **Reversible**: Yes. Documentation placement can change without changing the skill behavior.

- **Choice**: Use the external Excalidraw skill as inspiration, not as a template to copy wholesale.
  - **Alternatives considered**: Port the full reference skill structure and pattern catalogue.
  - **Why this one**: Blueprint values density. The reference has useful craft guidance, but this skill should remain a short workflow with rules that change behavior.
  - **Reversible**: Yes. More pattern guidance can be added later if real outputs need it.

## Invariants

- Blueprint skills remain dense workflows, not reference manuals.
- `explain-visually` remains responsible for full HTML explainers.
- `excalidraw-diagram` remains responsible for standalone Excalidraw diagrams.
- The skill must not require a specific issue tracker, app, or external service.
- The skill must not become a long visual-design reference manual.

## Error Behavior

- If the source material is missing or too vague to diagram, ask one clarifying question with a recommended answer.
- If the requested diagram would be too dense, split it into multiple diagrams or ask which slice matters most.
- If `.excalidraw` output cannot be validated as JSON, fix it before reporting success.
- If visual inspection shows overlap, clipped labels, ambiguous arrows, or unreadable scale, revise the diagram before reporting success.
- If the user requests a format other than Excalidraw, follow the request but make clear that the default skill output is Excalidraw.

## Testing Strategy

- Validate `skills/excalidraw-diagram/SKILL.md` frontmatter has the expected fields.
- Run the skill against an existing Blueprint document such as `README.md` or `docs/skill-anatomy.md`.
- Confirm the generated artifact is valid JSON when the output is `.excalidraw`.
- If local tooling can render or open Excalidraw files, visually inspect the generated diagram.
- Inspect the generated diagram for readable labels, non-overlapping elements, clear relationships, and one main teaching idea.
- Run `git diff --check`.

## Out of Scope

- Building a general-purpose drawing engine.
- Adding Excalidraw rendering or export tooling unless needed for a minimal valid implementation.
- Creating Mermaid diagrams; this skill is specifically for Excalidraw.
- Replacing `explain-visually`.
- Adding a new lifecycle category to Blueprint's core workflow.
