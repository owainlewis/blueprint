# Improve Blueprint as an AI engineering foundation

> Status: Proposed roadmap, 6 September 2026. The lifecycle guide and this plan are documentation delivered now. Skill changes, evaluations, website work, and courses below are planned, not implemented.

## 1. Outcome

Make Blueprint a practical foundation for learning and applying AI software engineering. A developer should be able to understand the lifecycle, choose an appropriate skill, complete a worked example, and judge the result using evidence.

"10x quality" is an ambition, not a measured result. Improve successful task outcomes and reduce unnecessary human supervision before making numerical or competitive claims. A larger skill catalog or a more polished website alone cannot establish that improvement.

The shared model is [Design → Plan → Build → Test → Review → Ship → Scale](lifecycle.md). Blueprint owns the explanation, engineering practices, skills, and teaching examples. Machinist executes selected workflows in code. Blueprint remains useful without Machinist.

## 2. Starting point

Blueprint currently has ten skills, a README, selection and workflow guides, examples, repository validation, and a tested Markdown-to-HTML renderer. Its skills separate existing architecture from proposed design, support small tasks that skip unnecessary phases, and require execution evidence and independent review.

The current checks validate metadata, links, Markdown, and supporting tools. This is useful repository hygiene, but it does not measure whether the engineering skills improve agent behavior. The standalone delivery skill and Codex coordinator also have different dependency and execution rules that need clear routing.

The main gaps are behavioral evidence, coverage of acceptance and release, a consistent learner journey, and a public reading experience that brings the method and examples together.

## 3. Product boundaries

Maintain a small set of skills organized around meaningful engineering outcomes. Writing code, branching, debugging, and repairing remain normal agent activities inside delivery. Add a public skill only when it owns a distinct outcome and has evidence that separate packaging helps.

Repository-specific commands and permissions stay in the consumer repository. Requirements essential to a portable skill must be present in that skill or its shipped references; installing skills does not install Blueprint's own maintainer `AGENTS.md` as policy everywhere.

Keep the Codex coordinator explicitly identified as an optional, harness-specific adapter. Naming a skill must not be confused in teaching material with technical enforcement of permissions. Document the current merge behavior accurately until an intentional policy change is approved and tested.

The website teaches and distributes Blueprint. It is not a hosted coding platform, a task tracker, or a prerequisite for using the skills.

## 4. Milestones and acceptance checks

### B1. Establish the lifecycle and learner entry points

**Result.** A developer can understand the seven stages, the human handoff, and the maker/checker relationship before installing anything.

Publish the lifecycle guide, link it from the README and guides, and make the distinction between specification, ticket, PR, and release consistent across public documentation. Mark current behavior separately from proposed improvements. Use the archive-project example across later lessons so readers do not repeatedly learn a new domain.

**Done when:** a reader can choose a path for a small bug, a feature with open decisions, and an existing PR that needs review; each path names its next artifact and stopping point. The lifecycle document explains QA, missing decisions, and release authority.

**Check:** independent editorial review, repository link checks, and a short walkthrough with community members. Record points where learners choose the wrong stage rather than treating a successful document build as teaching proof.

**Dependencies:** none. The lifecycle guide and navigation changes in this documentation work cover the initial artifact; learner validation remains planned.

### B2. Establish a behavioral baseline

**Result.** Skill improvements can be compared against observed agent behavior.

Start with `test`, `review`, and `task-to-pr`. Build at least ten scenario families: a correct change needing approval; a seeded logic defect; a passing suite that misses a requirement; a browser-only failure; an ambiguous product decision; a scope-expanding review comment; a stale review; an interrupted delivery; an infrastructure failure; and an unauthorized consequential action.

Compare a plain task prompt, Blueprint, and the relevant Addy skills with the same starting repository, model, tools, permissions, and resource budget. Pin the skill versions, include each setup's required references, and record which scenarios are comparable. Run at least three repetitions per comparable scenario and configuration. Start with one supported harness; test a second before claiming portability of measured results.

Use deterministic checks for observable behavior and repository mutations. Use blind human adjudication for scope, findings, and missing decisions; an agent grader may assist but cannot be the only judge. Keep held-out scenarios and add independent cases beyond our own workflow failures. Separate trigger selection tests from execution tests.

**Done when:** another maintainer can reproduce the baseline from documented commands, retrieve traces and artifacts, and see failures as well as successes. No task claims completion solely because the agent wrote the expected phrase.

**Check:** rerun a seeded failure and a correct-change case from clean fixtures. Confirm the evaluator catches the defect and does not reward invented findings. Run mutating GitHub scenarios only in an explicitly disposable repository with a cleanup procedure; local fixtures are the default.

**Dependencies:** B1 terminology and evidence definitions.

### B3. Improve skills using the baseline

**Result.** Existing skills produce more useful decisions and evidence with fewer unnecessary steps.

Review each skill's entry conditions, required context, result, evidence, and stopping behavior. Keep concise core instructions; move substantial examples and specialist guidance into linked references. Avoid introducing a public skill for every technique.

| Area | Improvement to investigate | Evidence required |
| --- | --- | --- |
| Design and plan | Scale the document to the decision; make shared decisions and ticket readiness explicit | A new maker can implement without inventing consequential decisions |
| Test | Connect requirements to meaningful execution, including failure cases and browser behavior | Detect a change that passes existing tests but violates the task |
| Review | Require supported findings and permit approval of sound changes | Catch seeded defects without increasing false findings |
| Task to PR | Clarify completion, handling of feedback, and handoff limits | Ready PR or explicit blocker, with no unauthorized merge or repeated work |
| Coordinator | Make harness requirements and dependency strategy explicit | Missing capabilities fail clearly; dependencies and authority remain correct |
| Architecture and improve | Preserve the distinction between facts, proposals, and behavior-preserving changes | Claims trace to code; refactors preserve observable behavior |

**Done when:** proposed revisions improve a predeclared primary measure and do not regress correctness or authority checks on the selected evaluation set. Publish tradeoffs and uncertainty. A target for the first iteration is lower median human intervention time at equal or better accepted-outcome rate; establish the numerical goal after measuring B2 and before tuning prompts.

**Check:** repeat B2 with versioned revisions and inspect held-out cases. Investigate regressions instead of changing expectations merely to make a new skill pass.

**Dependencies:** B2. Work on unrelated skills need not wait for a complete catalog rewrite.

### B4. Complete useful SDLC coverage and course examples

**Result.** Learners can connect requirements to release, with enough practice to assess their own work.

Map existing skills to the lifecycle. Extend existing material where it already owns the outcome. Design an acceptance-and-release guide covering human acceptance, target environments, smoke checks, rollback, and post-release verification. Decide through an example whether release needs a dedicated portable skill. Record that decision before adding one. Keep production monitoring and incident response outside the first course unless a lesson needs them to close its release example.

Build seven lessons in lifecycle order. The Scale lesson turns the familiar delivery loop into a proposed executable workflow with explicit inputs, checks, limits, and recovery. It introduces Machinist as the implementation path; the earlier lessons remain useful without it. Each has a learner outcome, one worked example, an exercise, and a completion check. The capstone uses a small application and a ready ticket, includes an intentionally seeded defect for the checker, and ends with explicit release verification or a clearly stated simulated release, followed by an automation exercise using the same task. Label simulated evidence.

**Done when:** each of the seven lifecycle stages has teaching material and a credible way to perform the work; skill coverage does not depend on pretending every stage needs a new skill. A learner can complete the capstone with the supplied starting code and instructions.

**Check:** pilot with community members, record where help was needed, and revise the lessons. Do not publish student quotes or results without their permission.

**Dependencies:** B1; B3-tested practices feed the examples. Course outlines can be prepared while evaluations run.

### B5. Publish a focused Blueprint website

**Result.** Visitors can understand the method, try it, and inspect evidence without reading the entire repository.

Use a static documentation site generated from repository content. Select the static-site tool in the website implementation proposal based on Markdown reuse, accessibility, preview deployment, and maintainer familiarity. This roadmap does not choose a hosting provider or purchase a domain.

| Page | Reader's next action |
| --- | --- |
| Home | Understand Blueprint's purpose and choose Learn or Use |
| Lifecycle | Follow the seven stages and inspect their artifacts |
| Get started | Install a pinned release and complete one small example |
| Skills | Choose by outcome, with inputs, stopping points, and examples |
| Workflows | Follow a small fix, a feature, or an independent review |
| Examples | Inspect a specification, tickets, PR evidence, and release check |
| Evaluations | Read reproducible methods, results, limitations, and versions |
| Teaching | Start an exercise or course module |

Use readable typography, restrained visual design, working mobile navigation, and a clear version indicator. Keep source Markdown authoritative; avoid manually maintaining different lifecycle text in the repository and website. Link to Machinist as the automation path after a learner understands delivery.

**Done when:** a new visitor can choose the correct skill and complete the getting-started example; all published examples and install commands are verified; no superiority claim appears without supporting results. The site works on mobile and desktop, with keyboard navigation and readable code, tables, and diagrams.

**Check:** content/link validation, a production build, desktop and mobile browser checks, keyboard checks, and a learner walkthrough. Treat deployment and domain setup as explicit implementation work with their own review, not as part of creating this plan.

**Dependencies:** B1 for information structure; publish evaluation claims only after B2/B3. A content prototype can proceed alongside evaluations.

### B6. Release and maintain the method

**Result.** Users know what changed and maintainers can detect behavioral regressions.

Version skill releases and website documentation together. Keep compatibility guidance, migration notes, and representative evaluations with each release. Turn confirmed community failure reports into regression scenarios after removing private code and data. Revisit evaluations when a harness or model changes; attribute results to the exact tested combination.

**Done when:** a release can be installed and reproduced, its changes and known limits are documented, and maintainers have a repeatable process for accepting or rejecting skill changes.

**Check:** release rehearsal in a clean environment and rerun of the held-out evaluation set.

**Dependencies:** B3 and B5; incorporate B4 lessons as they are validated.

## 5. Measures that matter

Track accepted task outcomes, missed defects, false review findings, unnecessary human questions, active human intervention time, elapsed time, token usage, and cost when prices are available. Report counts and per-scenario results, not just a blended score. A small benchmark supports conclusions about those scenarios, not all software development.

For the website, observe whether learners find the right starting point and finish an example. Traffic and skill count are secondary. Measure "10x" only against a defined baseline and quantity; do not turn the phrase into an unsupported launch claim.

## 6. Decisions and sequencing

Start with B1 and B2. Begin website content structure and course outlines in parallel, then incorporate evaluated practices before making quality claims. Improve `test`, `review`, and `task-to-pr` before expanding the catalog.

The website implementation still needs a selected tool, hosting arrangement, and visual design. The initial proposed audience is developers who know Git and tests but are learning to delegate work to AI. Validate that audience in the pilot. These decisions do not block writing the lifecycle or measuring existing skills.

This is a roadmap, not an implementation-ready ticket batch. Each milestone should become scoped tasks only after its remaining product and technical choices are settled. No tracker issues, website, or skill changes are created by this plan.

## References

- [Blueprint lifecycle](lifecycle.md), [current skill selection](choosing-a-skill.md), and [repository checks](../scripts/check_repo.py).
- Addy Osmani's [skills](https://github.com/addyosmani/agent-skills/tree/main/skills) and [evaluation approach](https://github.com/addyosmani/agent-skills/blob/main/evals/README.md). They are comparison inputs, not evidence that Blueprint already performs better.
