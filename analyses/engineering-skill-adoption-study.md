---
domain: analyses
type: analysis
status: draft
last-reviewed: 2026-10-27
---

# Engineering skills: what to reuse and what to own

This is a source-based study of six local repositories, not an installation recommendation based on popularity. The companion [catalogue](engineering-skill-catalogue.md) inventories every tracked SKILL.md in the selected source trees, including internal skills and runtime variants. It excludes Compound and Gstack test fixtures, Anthropic's blank template and Pstack's generated harness copy. Aliases and runtime variants are explicitly not independent capabilities.

**Coverage matters:** the catalogue inventories 281 source paths across six repositories plus 235 skill files in the purchased PM OS package. The six-repository reviews inspect skill-body semantics and map individual skills or tightly related families to inputs, outputs, dependencies, side effects and dispositions. PM OS is supplementary: all 235 files are classified, with deeper review of selected workflows and action-bearing system commands rather than equivalent deep coverage of every body. These counts include aliases, internal skills and runtime variants. This is not an exhaustive audit of every reference, script or runtime. No skills were executed, installed, copied into a shared plugin, or used to modify external systems. Cross-family synthesis review and behavioral trials remain outstanding. Keep this analysis draft.

## The choice is not simply copy or write

There are four different decisions:

1. **Use the upstream skill.** Its behavior already fits. Keep one maintained source and avoid a renamed duplicate.
2. **Configure or adapt the integration.** The method fits, but it needs our repository paths, tracker, tools and approval rules. Prefer a supported configuration mechanism before a fork.
3. **Vendor a selected skill.** A deliberate, attributed copy with its dependencies and source revision is useful when the team needs a controlled release or must change behavior upstream does not configure. Owning the copy also means reviewing upstream changes and maintaining it.
4. **Write a new workflow.** The job is specific to this team or materially different from what exists. Reuse proven methods inside it; do not recreate generic engineering advice.

Installing every pack simultaneously would give the agent several competing answers to when to interview, where to save plans, whether to implement immediately, which review tools to run, and what constitutes approval. The aim should be a small, coherent set of behaviors with clear entry points.

## Matt Pocock focuses on turning ambiguity into executable work

The intended path is clarification and domain modeling → PRD → independently verifiable issues → implementation and review. However, the plugin manifest registers only 17 skills: on-disk `implement` and its in-progress `review` dependency are not in that registered set. The latter compares committed HEAD, so invoking it before committing can miss uncommitted implementation. It is a collection of composable practices rather than an entire hosting environment. The engineering source includes `to-prd`, `to-issues`, `triage`, `domain-modeling`, `codebase-design`, `diagnosing-bugs`, `tdd`, `prototype`, `implement`, and architecture improvement; productivity skills cover questioning, handoff, teaching and skill authoring. Deprecated and in-progress directories should not be treated as the supported default set.

The useful idea in **to-issues** is a vertical slice: one small piece of behavior that can be demonstrated through the relevant layers. For supplier ingestion, that might be “import one supplier's sample file and show validation failures,” rather than separate disconnected tickets called database, API and UI. It presents proposed slices and dependencies for approval before creating issues, then creates blockers first so subsequent tickets can link real identifiers. It explicitly leaves the parent issue unchanged.

Two adaptations matter. **to-prd** synthesizes the conversation and publishes with a ready-for-agent label; that label must not mean an unreviewed exploratory discussion has become approved implementation scope. **domain-modeling** defaults to CONTEXT.md and docs/adr. Keep the practice of resolving ambiguous terms and preserving consequential rationale, but route it into the workspace's existing terminology and decision documents instead of imposing another taxonomy. **codebase-design** also prescribes a vocabulary that avoids “component” and “service”; use it for module design without erasing the team's established system vocabulary.

**Disposition:** strong candidate for selected reuse/adaptation. Test the clarification → draft epic → issues path first. Do not copy its readiness policy unchanged.

Sources: [[artifacts/plugins/mattpocock-skills]], [[sources/mattpocock--skills]]. Direct bodies: `skills/engineering/{to-prd,to-issues,triage,domain-modeling,codebase-design,implement}/SKILL.md` in the pinned catalogue revision.

## Compound Engineering connects delivery to reusable team knowledge

Its main loop separates what to build (`ce-brainstorm`), how to build it (`ce-plan`), execution (`ce-work`), review, and recording reusable lessons (`ce-compound`). Related skills handle documentation review, stale-learning refresh, debugging, visual evidence, browser testing, PR delivery and product pulse reports. Tool-specific skills such as Rails style, Xcode testing, Gemini images and Proof integration are separate choices, not prerequisites for adopting the general methods.

The important distinction is between a **plan** and **a reusable solution**. A plan coordinates a particular effort. A solution explains an established problem, what resolved it, why it worked and when that knowledge applies. `ce-compound` searches for overlap before writing and can update discoverability instructions. `ce-compound-refresh` exists because saved lessons can drift as code changes. This directly addresses the risk of a stale statement becoming permanent agent guidance.

The package has real carrying costs. It defines its own configuration, brainstorm/plan/solution paths, review personas and interaction rules. The examined brainstorming and planning bodies have blocking question conventions that may be more interruptive than the team's desired workflow. Some QA skills require a particular browser CLI and can fix and commit changes rather than merely report findings. `ce-code-review` is strictly no-write only in report-only mode; its default interactive mode may apply safe fixes. `ce-demo-reel` can upload a public preview before asking the sharing destination; local save is offered after that transmission. That sequence needs changing for private engineering evidence. Cleanup and learning refresh also have deletion/publication behaviors requiring separate treatment. These need mode and tool checks, not a simple filename copy.

**Disposition:** reuse the separation of requirements, plans and learned knowledge; consider selected review and documentation-maintenance workflows. Adapt artifact placement and authorization explicitly before adoption; do not assume arbitrary path configuration is supported. Avoid adding parallel status trackers to GitHub.

Sources: [[artifacts/plugins/compound-engineering]], [[sources/every--compound-engineering-plugin]]. The [detailed review](engineering-skills-compound-anthropic-review.md) maps all 39 bodies and records source spans for the action-bearing findings.

## HumanLayer preserves a chain of reasoning across sessions

RPI separates research questions, factual research, design discussion, structure outlines or plans, implementation, and PR description. Creation and iteration are separate skills so a later agent can revise an artifact instead of rebuilding context. Product and technical design are distinct artifacts. The repository also includes internal development skills and a Pi extension; those are not additional independent RPI workflow stages.

**create-research** deliberately documents the current system rather than prematurely designing its replacement. It restricts which task documents it reads to avoid letting a proposed solution bias the factual investigation. **implement-outline** carries an explicit document precedence order and verifies each phase, with human checks before continuing unless multiple phases were explicitly requested.

This is especially useful for decisions such as whether an existing calendar integration should remain on SharePoint or connect to a future PIM. Establish current behavior first, then compare alternatives, then record the decision and implementation scope. A researched fact and an agreed decision should not be interchangeable.

HumanLayer already handles business-success alignment: `create-prd` settles the problem and measurable success before the solution, while `create-tdd` means technical design document, not test-driven development. `describe-pr` is more than writing: the Claude variant can commit, push, open the PR and repair CI; the Pi variant omits that CI-repair phase.

Copying the plugin alone does not supply HumanLayer's environment. The bodies expect `.humanlayer/tasks`, specific agent roles, templates, task context and cloud artifact links. One implementation body even names different implementer roles in adjacent instructions; the actual host contract must be resolved before porting. Its artifact precedence cannot override a user's newer decision or approval boundary.

**Disposition:** adapt its artifact contracts and staged reasoning for substantial cross-repository work. Do not impose the entire phase sequence on a small fix or assume its runtime comes with the Markdown.

Sources: [[artifacts/plugins/humanlayer-rpi]], [[sources/humanlayer--humanlayer]]. Direct bodies: `create-research`, `create-design-discussion`, `create-structure-outline`, `implement-outline`; catalogue distinguishes internal and Pi variants.

## Pstack makes investigation and verification concrete

Pstack includes investigative commands (`how`, `why`, `blast-radius`), design and competing approaches (`architect`, `arena`), review (`interrogate`), verification generators and maintainers, communication helpers, learning workflows and a set of engineering principles. The principles are distinct from the executable tooling and multi-agent workflows. Its Benny automation skills add issue triage, reproduction and bounded fixes; they are not ordinary read-only review helpers.

**how** builds an explanation of architecture and runtime flow. **why** seeks the evidence behind design choices. That split is valuable: code can establish what happens without proving why the team chose it.

**create-verification-skill** builds a project-specific way to start the app, drive a user-visible feature, capture evidence and clean up. It requires a real execution before treating the generated skill as delivered. **maintain-verification-skill** checks both source and live behavior, distinguishes documentation drift from a product regression, and limits edits to the verification package. This is a strong model for answering “can agents actually understand and verify this system?”—a feature map is maintained by use, rather than merely existing in docs.

However, **architect** proceeds into implementation by default unless a checkpoint is explicitly requested. That is unsuitable for a design-only request unless overridden. Model routing, Task APIs, Cursor rules, transcript locations, tool availability and project-local skill placement also need adaptation. **reflect** routes some findings to skill changes and others to a tracker; importing its exact workflow would import those write behaviors too. Its Accepted skill edits wait for approval, while Backlog tracker filing does not. Pstack's PR-opening playbook requires ready PRs rather than drafts, which conflicts with workflows that deliberately use drafts for review. Its multi-phase-plan playbook has an implementation checkpoint, unlike architect's default: a pack does not necessarily have one consistent approval policy.

**Disposition:** high-value investigation and verification candidates. Prefer using available skills with explicit scope; adapt host contracts when distributing them to other engineers. Keep expensive multi-model reviews and formal verification proportional to the task.

Sources: [[artifacts/plugins/pstack]], [[sources/cursor--plugins-pstack]]. Direct bodies: `how`, `architect`, `create-verification-skill`, `maintain-verification-skill`, `reflect`, `automate-me`. Review bodies as source evidence, not permission to execute their actions.

## Gstack is an integrated operating workflow, not just prompts

The inspected checkout contains product and planning reviews, design work, browser QA, debugging, security, shipping, deployment, post-deploy checks, retrospectives, documentation, context recovery, learning and tool setup. Its skill bodies contain substantial shared operational material. Browser commands, setup scripts, artifacts, configuration and learning infrastructure matter to how it behaves.

Separate **qa-only** from **qa**: reporting defects and fixing them are different actions. Similarly, shipping a PR and landing/deploying it are different workflows. Installing a large pack without making those differences clear would make it harder for nontechnical users to predict what a request will do.

A concrete mismatch appears in **retro**: it groups commits into sessions using a 45-minute gap, sums session durations as active coding time, calculates lines per hour and selects a “ship of the week” by highest lines changed. Those are activity heuristics, not measured labor time, business impact or engineer performance. Do not use them as the basis of management or cost allocation. Issue cycle time, review waiting time and blocked time can be useful if accurately labeled; actual effort and business benefit require their own evidence.

The local checkout is at `c7ae63201ab193a7dc7fb7e0d81238645111ffac`, while the research manifest pins `029356e`. The older wiki cannot establish the current checkout's complete behavior. The catalogue records the inspected checkout without silently rewriting the historical source record.

**Disposition:** investigate selected review/QA capabilities with their runtime intact. Do not transplant the entire operating style, deployment flow or retrospective metrics into the team by default.

Sources: [[artifacts/plugins/gstack]], [[sources/garrytan--gstack]]. Current-checkout evidence: `retro/SKILL.md` steps 4–9 and the current catalogue. The [detailed review](engineering-skills-gstack-pstack-review.md) covers all 59 nonfixture entries, distinguishing variants and shared preambles. The shared preamble can auto-select recommended options in spawned sessions, so interactive checkpoints are not invariant across delegation.

## Anthropic provides general capabilities and a skill evaluation loop

The source includes frontend design, web-app testing, MCP building, document coauthoring, internal communication, visual/document creation and skill authoring. These are capabilities to compose with an engineering workflow, rather than a replacement for project ownership and delivery policy.

**skill-creator** provides the strongest general evaluation pattern in this comparison: specify the desired behavior, create realistic test prompts, run with and without the skill, inspect artifacts and quantitative results, revise, and separately evaluate whether the description triggers appropriately. Source quality does not establish that a skill improves a particular harness; this loop tests that claim. The supplied trigger scripts are Claude-specific, and the optimizer selects its best iteration using test-set scores; retain an additional untouched final acceptance set rather than calling that reused selection set unbiased validation.

Do not treat the repository as uniformly licensed. Its README distinguishes open-source examples from source-available document skills. Check each selected skill's license and bundled resources before copying it into a shared marketplace. Existing installed capabilities may remove the need to copy anything.

**Disposition:** use existing general capabilities; use its evaluation approach when deciding whether a custom engineering skill earns its maintenance cost.

Sources: [[artifacts/plugins/anthropic-skills-marketplace]], [[sources/anthropic--skills]]; direct `skills/skill-creator/SKILL.md` and repository README.

## PM OS provides a separate product-management layer

The older citation points to a Claude package directory that was not found, but a subsequent targeted search located the Cowork 2.2.1 package at `sources/prodmgmt-world--pm-os-cowork/`. Its plugin has 235 skill files. This corrects the initial missing-source finding; the source variant matters.

Its PRD workflow turns transcripts, designs or research into requirements, use cases, stories, acceptance criteria and reviewed drafts. Strategy, opportunity mapping, assumptions, decisions, meetings and measurement are complementary workflows. Their knowledge library and workspace conventions are dependencies, not just optional decoration. The product-management perspective is useful for business outcomes, but it does not replace engineering verification. A simulated customer reviewer is not customer research.

This is a purchased package. The study analyzes its methods without copying the skill bodies into a team plugin or asserting redistribution rights. The separate package review records coverage and limitations. Its import workflow claims nothing leaves the machine yet includes a creator-webhook transmission; this is a source-level contradiction, not evidence any transmission occurred here. Do not carry that behavior into a team adaptation.

Sources: [[artifacts/plugins/pm-os]], [[sources/prodmgmt-world--pm-os]], [[sources/prodmgmt-world--pm-os-cowork]].

## Existing Flex skills already cover part of the proposed workflow

`flex-investigate-project` is a broad evidence-based onboarding and architecture investigation. `flex-finding-unknowns` addresses a specific ambiguous request and stops with a revised brief for confirmation; its reference-mapping mode is particularly relevant when porting a workflow. `flex-goals-spec` formats a defined objective for a Codex thread Goal—it is not a general GitHub epic or product-requirements workflow. Do not merge those meanings merely because each uses the word goal.

The engineering root AGENTS.md already covers choosing an implementation owner, shared versus child-repo documentation, draft versus approved scope, current GitHub status, preservation of local work and child-first submodule publication. New skills should perform repeatable tasks within those rules, not copy the same navigation policy into another place. This study does not change those existing instructions.

## One example shows how the methods can work together

For “let us build a profit calculator”:

1. **Investigate:** locate existing tools, data sources, owners and relevant decisions. Produce a current-state explanation with evidence. Reuse the how/why and factual-research methods.
2. **Clarify the outcome:** establish users, decisions the tool supports, required inputs and an observable success measure. Use a focused clarification method, not every interview skill.
3. **Record a draft:** write the proposed outcome, scope, assumptions and unresolved choices. Draft status is explicit; file creation is not approval.
4. **Choose an approach:** compare extending an existing application with a separate tool. Consult the real platform integration rules, not a generic “always microservices” preference.
5. **Break down approved work:** create linked, verifiable issues in dependency order. Keep the parent epic as the coordinating outcome.
6. **Implement and verify:** work in the owning repository, test the relevant boundaries and show the observable result. A merged PR does not prove deployment or business adoption.
7. **Communicate:** post the linked epic with issues/PRs and useful proof in the team's established channel format.
8. **Preserve learning:** update durable system knowledge when the system changes; keep one-off planning and execution records with the effort. Avoid copying volatile status into instructions.

This is a proposed composition of methods, not a new skill implemented by this study.

## A small evaluation should decide adoption

Compare the baseline harness, a selected upstream skill, and an adapted version using the same task evidence. Include repeated runs because a single impressive response is insufficient.

| Case | What a useful skill must do |
| --- | --- |
| New departmental tool with an existing similar app | Discover the existing capability before proposing a new repo |
| Draft epic with unresolved architecture | Preserve uncertainty; do not infer implementation approval |
| Calendar/PIM integration decision | Separate observed current behavior, future options and accepted decisions |
| Merged PR with deployment failure | Report both states correctly |
| Backend change without meaningful UI | Provide appropriate verification rather than a decorative screenshot |
| Closed cancelled issue | Do not treat closure as delivered value |
| Existing local changes and submodules | Preserve user work and publish child commits before parent pointers |
| Conflicting stale docs | Trace authoritative evidence and update the right owner, not add a competing copy |
| Weekly status request | Report commitments, progress and blockers without manufacturing hours worked |

Measure correct facts, missing dependencies, unnecessary questions, unauthorized actions, useful artifacts, tool failures, elapsed run time and model usage. Keep measured model cost separate from business value. Test trigger selection separately from output quality. Do not publish test messages to real team channels or mutate live issues just to run an evaluation; use fixtures and a controlled test target.

## Detailed source reviews

- [Matt Pocock and HumanLayer](engineering-skills-matt-humanlayer-review.md)
- [Compound Engineering and Anthropic](engineering-skills-compound-anthropic-review.md)
- [Gstack and Pstack](engineering-skills-gstack-pstack-review.md)
- [PM OS](engineering-skills-pm-os-review.md)

These reviews map individual skills and tightly related families to purpose, outputs, dependencies, side effects and a proposed disposition. They distinguish body-level semantic review from exhaustive dependency audits and runtime tests. Review scores refer to the earlier draft; corrections incorporated here do not retroactively turn those scores into a passed gate.

## Provisional adoption decision

- **Use existing capabilities:** code review, debugging, documentation, frontend and document tools where their tool contracts fit.
- **Adapt selected workflows:** clarification → draft epic → issues; current-state research → design decisions; project-specific verification; knowledge refresh.
- **Own team-specific integration:** channel publishing, meeting-decision reconciliation, cross-repository routing, approval-state interpretation and business-value/usage linkage.
- **Avoid blanket imports:** entire operating packs, automatic deployment behaviors, commit-derived hours and speculative infrastructure.

No new skill is approved solely by this report. These are candidate decisions pending selected dependency/host verification and representative evaluations. Preserve upstream attribution and notices for actual reuse; verify per-file terms at that point. A supported install and an attributed fork are different maintenance choices.

## Remaining work before adoption

The catalogue and detailed reviews make the source-review scope explicit. For selected candidates, finish dependency-level and host-contract verification, check reuse terms, and run behavioral comparisons. Body-level semantic review does not establish implementation reliability or improvement over the existing harness. The cross-family review gate from `analyses/_eval-rubric.md` has not run; this document remains draft and is not a release recommendation.
