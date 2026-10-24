---
domain: artifacts
type: plugin
name: humanlayer-rpi
creator: "[[creators/humanlayer]]"
source: "[[sources/humanlayer--humanlayer]]"
ecosystem: cross-lab
discovered-via: user-curated
marketplace-listing: "Source README: humanlayer/riptide-rpi; current public installation not independently verified"
status: source-investigated
last-reviewed: 2026-10-23
ingestion-mode: full
license: Apache-2.0
components:
  skills: 22
  companion-hl-skills: 3
  commands: 0
  agents: 0
  hooks: 0
  mcp-servers: 0
  host-provided-rpi-agents: 7
popularity-signals: []
---

# HumanLayer RPI

> **One-line:** A coding-workflow plugin that turns uncertain work into factual research, explicit human decisions, testable implementation slices, and reviewable code, with durable artifacts connecting otherwise separate agent sessions.

This page covers the `rpi` plugin, its companion `hl` skills, and the HumanLayer runtime mechanisms that make their handoffs useful. They are separate layers: installing Markdown skills alone does not reproduce the task UI, synchronization, registered agents, or automatic session transitions. Evidence is pinned to the source revision; **prompt policy**, **implemented mechanism**, **documented practice**, and **our interpretation** are distinguished below. Tests were inspected, not executed. [[sources/humanlayer--humanlayer#WF33]] [[sources/humanlayer--humanlayer#WF34]]

## Attributes

- **What it does:** Creates a chain of reviewable decisions before code becomes expensive to change. The current RPI route is questions → research → design discussion → structure outline → implementation → PR; PRD-Oriented separates product and technical design. Oneshot and Freeform avoid unnecessary phases. [[sources/humanlayer--humanlayer#WF01]] [[sources/humanlayer--humanlayer#WF02]]
- **Target user:** Engineers and product collaborators using coding agents on work whose facts, desired behavior, or architecture need clarification. The central bottleneck is human review attention, not typing speed. [[sources/humanlayer--humanlayer#WF01]]
- **Identity and license:** The source manifest names the plugin `rpi`, base version `0.50.0`, Apache-2.0; the companion is `hl`, base version `0.2.0`. These are source manifest values, not verified currently installed release versions. [[sources/humanlayer--humanlayer#WF33]]
- **Component inventory:** 22 RPI skills, grouped below. There are no separate plugin-local agent, hook, command or MCP-server definitions in this bundle; host-provided runtime integrations are distinct. The documented seven RPI agent roles are locator, analyzer, pattern finder, web researcher, implementer, outline implementer, and implementation reviewer. [[sources/humanlayer--humanlayer#WF27]] [[sources/humanlayer--humanlayer#WF34]]

| Skill family | Source skill names | Job |
| --- | --- | --- |
| Research | `create-research-questions`, `iterate-research-questions`, `create-research`, `iterate-research` | Define the factual query, then build and revise the current-state map |
| Design | `create-design-discussion`, `iterate-design-discussion` | Present alternatives and record user-resolved decisions |
| Product and technical design | `create-prd`, `iterate-prd`, `create-tdd`, `iterate-tdd` | Separate WHAT/WHY from system and program HOW |
| Planning | `create-structure-outline`, `iterate-structure-outline`, `create-plan`, `iterate-plan` | Produce slices, optionally expand to detailed instructions |
| Implementation | `implement-outline`, `implement-plan`, `iterate-implementation` | Execute bounded phases and revise existing work |
| Workspace | `configure-workspaces`, `setup-worktree` | Configure and create isolated working directories |
| Review and publishing | `review-artifact-comments`, `ci-commit`, `describe-pr` | Process feedback, commit, and create/update a PR |

The companion's three skills are `orchestrate` (CLI task/session operations), `show-me` (focused visual explanations), and `teleport` (new session on another host from a handoff artifact and pushed branch). Source skill names are shown here. The reference docs call `create-outline` the current command and `create-structure-outline` an older UI name, while inspected runtime bundling still uses the latter. This is documented naming drift; current UI behavior was not verified. [[sources/humanlayer--humanlayer#WF31]] [[sources/humanlayer--humanlayer#WF34]]

- **Install footprint:** Markdown, reference templates and a small helper script are embedded into the daemon using Bun file imports. Full integration additionally needs HumanLayer's authenticated task/session runtime, a coding-agent runtime and provider access. Git/`gh` support worktree/PR operations; comment tools are task-scoped. The source README supplies a marketplace command, but standalone installation compatibility and installed disk size were not measured. [[sources/humanlayer--humanlayer#WF15]] [[sources/humanlayer--humanlayer#WF28]] [[sources/humanlayer--humanlayer#WF33]] [[sources/humanlayer--humanlayer#WF34]]
- **Layout:** `apps/riptide-rpi-claude-plugin/` holds the manifest, 22 skill directories and their references; `apps/riptide-humanlayer-claude-plugin/` holds three companion skills; `apps/riptide-daemon/` contains agents, bundling, routing and artifact hooks; `apps/riptide-api/` and `packages/ai/` supply transition and inference mechanisms. The source bundle and runtime should not be conflated. [[sources/humanlayer--humanlayer#WF18]] [[sources/humanlayer--humanlayer#WF20]] [[sources/humanlayer--humanlayer#WF34]]

## Relationships

- **Creator:** [[creators/humanlayer]].
- **Parent system:** [[artifacts/projects/humanlayer]]; workflow policy rides on the broader [[concepts/agent-control-plane]].
- **Source:** [[sources/humanlayer--humanlayer#WF33]], with mechanism anchors below.
- **Concepts sharpened:** [[concepts/review-cost-aware-workflows]] and [[concepts/artifact-centered-agent-context]].
- **Existing ideas extended:** [[concepts/completion-contract]], [[concepts/durable-agent-execution]], [[patterns/behavioral/evidence-gated-completion]], and [[patterns/behavioral/latent-vs-deterministic-split]].
- **Composes:** The 22 skills listed above. Individual skill pages are not created here; their shared artifact protocol is the useful unit of this deep dive.
- **Comparison candidates:** [[artifacts/plugins/compound-engineering]] and [[artifacts/plugins/gstack]] for composed coding workflows; [[artifacts/plugins/gbrain]] for durable knowledge. These are navigation links, not an asserted feature-equivalence ranking.

## What problem it solves

Fast code generation moves the expensive failure earlier: an agent confidently implements the wrong system. HumanLayer makes the facts, decisions and code shape separately visible before committing much implementation effort. Its distinctive move is not “always plan.” It is **choose the smallest representation and workflow that let a human correct the expensive misunderstanding**. [[sources/humanlayer--humanlayer#WF01]] [[sources/humanlayer--humanlayer#WF02]]

A second problem is context continuity. Research, design and implementation can happen in separate sessions, models or workstations, while a task's shared artifacts retain current decisions and progress. The artifact is a handoff contract; the chat is not the only memory. This connects review design to context engineering. [[sources/humanlayer--humanlayer#WF14]]

## Composition strategy

### Select phases by uncertainty, not ceremony

| Main uncertainty | Route | Review subject |
| --- | --- | --- |
| Small, clear result | Oneshot | Implemented behavior and PR |
| Facts and combined design | RPI | Research, choices, thin slices |
| Product and technical design differ | PRD-Oriented | Product outcome, system design, program design |
| No useful fixed sequence | Freeform | User-defined work |

The detailed code-level plan remains a supported older path, not the current default. The companion launch guide even permits going directly to implementation after research when an existing document adequately covers the task. This flexibility is part of the design. [[sources/humanlayer--humanlayer#WF02]]

### Artifacts own different kinds of truth

Research answers what currently exists; design records desired behavior and resolved choices; the outline names independently verifiable phases. The workflow’s role-specific precedence usually gives later design artifacts priority over earlier intended-state descriptions; it does not validate approval or make chronological recency sufficient authority. Live source remains authoritative for actual current behavior. Create skills write numbered artifacts; iterate skills revise an existing artifact rather than making a new competing specification. [[sources/humanlayer--humanlayer#WF04]] [[sources/humanlayer--humanlayer#WF14]]

```text
ticket → factual query plan → evidence-backed research
                            ↓
                  choices / PRD + TDD
                            ↓
                 testable vertical slices
                            ↓
               phase executor → verification
                            ↓
                    reviewable PR + CI
```

### The runtime adds state to otherwise reusable skills

The daemon embeds skill files and shared references, while code determines workflow-specific routing. A routing hook can send an outline directly to implementation when the session already runs in a worktree, regardless of an older “create later” setting. This is implemented prompt injection, not a hard execution gate. [[sources/humanlayer--humanlayer#WF18]] [[sources/humanlayer--humanlayer#WF34]]

An LLM extracts structured next-step hints from assistant text; the API then checks transition flags, labels, artifact types or extraction results, and newer sibling sessions before launching another session. Design-to-outline and outline-to-implementation are absent from the auto-advance transition table. This is a concrete latent/deterministic split, but its completion signals are weaker than test or approval evidence. [[sources/humanlayer--humanlayer#WF19]] [[sources/humanlayer--humanlayer#WF20]] [[sources/humanlayer--humanlayer#WF22]]

## Source citations

- **Workflow rationale and phase selection:** [[sources/humanlayer--humanlayer#WF01]]–[[sources/humanlayer--humanlayer#WF02]].
- **Factual research and evidence contracts:** [[sources/humanlayer--humanlayer#WF03]], [[sources/humanlayer--humanlayer#WF04]], [[sources/humanlayer--humanlayer#WF05]], [[sources/humanlayer--humanlayer#WF06]].
- **Human design, visual review and slices:** [[sources/humanlayer--humanlayer#WF07]], [[sources/humanlayer--humanlayer#WF08]], [[sources/humanlayer--humanlayer#WF09]], [[sources/humanlayer--humanlayer#WF10]], [[sources/humanlayer--humanlayer#WF11]], [[sources/humanlayer--humanlayer#WF12]], [[sources/humanlayer--humanlayer#WF13]].
- **Artifacts and runtime handoffs:** [[sources/humanlayer--humanlayer#WF14]], [[sources/humanlayer--humanlayer#WF15]], [[sources/humanlayer--humanlayer#WF16]], [[sources/humanlayer--humanlayer#WF17]], [[sources/humanlayer--humanlayer#WF18]], [[sources/humanlayer--humanlayer#WF19]], [[sources/humanlayer--humanlayer#WF20]], [[sources/humanlayer--humanlayer#WF21]], [[sources/humanlayer--humanlayer#WF22]], [[sources/humanlayer--humanlayer#WF23]].
- **Learning, completion and packaging:** [[sources/humanlayer--humanlayer#WF24]], [[sources/humanlayer--humanlayer#WF25]], [[sources/humanlayer--humanlayer#WF26]], [[sources/humanlayer--humanlayer#WF27]], [[sources/humanlayer--humanlayer#WF28]], [[sources/humanlayer--humanlayer#WF29]], [[sources/humanlayer--humanlayer#WF30]], [[sources/humanlayer--humanlayer#WF31]], [[sources/humanlayer--humanlayer#WF32]], [[sources/humanlayer--humanlayer#WF33]], [[sources/humanlayer--humanlayer#WF34]].

## What makes it great

The bundle is coherent because each representation has a job: neutral research, an open decision, a product outcome, a technical contract, a runnable slice, or a verified change. Its fresh-context strategy preserves the result of thought rather than trying to retain every token of thought. The newer outline-first route also shows restraint: review signatures and responsibilities, then let a capable implementer supply mechanical detail. [[sources/humanlayer--humanlayer#WF04]] [[sources/humanlayer--humanlayer#WF12]] [[sources/humanlayer--humanlayer#WF13]] [[sources/humanlayer--humanlayer#WF14]]

The executable layer improves the prompts without pretending prompts are enforcement. State-aware routing, owner-aware settings, rewind-aware deduplication and governed context loading are useful engineering mechanisms. Their limitations are equally instructive: an extracted “next step” is not proof of completion, and a Markdown approval instruction is not access control. [[sources/humanlayer--humanlayer#WF18]] [[sources/humanlayer--humanlayer#WF19]] [[sources/humanlayer--humanlayer#WF21]] [[sources/humanlayer--humanlayer#WF22]] [[sources/humanlayer--humanlayer#WF25]]

## What we'd steal

This is the complete 46-item portable ledger from the workflow investigation. ★ marks particularly valuable transfers; it does not discard the smaller mechanisms. **P** = prompt policy, **I** = implemented source, **D** = documentation. Benefits and reuse suggestions are our interpretation.

### Review economics and factual research

1. ★ **Optimize review attention, not generated volume (D).** Short correctable designs can prevent much larger incorrect diffs. Budget unchecked work and measure review/revision cost, not just code production. This is a rationale, not a benchmark proving planning always wins. [[sources/humanlayer--humanlayer#WF01]]
2. ★ **Scale process to risk (D/P).** Pick Oneshot, combined design, separate product/technical design, or Freeform according to uncertainty. Skip a detailed plan when the outline is enough. The portable lesson includes the escape hatches; imposing every phase defeats it. [[sources/humanlayer--humanlayer#WF02]]
3. **Write a query plan for another mind (P).** Preserve exact source pointers and ask what must be learned without embedding the proposed answer. This makes delegation reproducible and avoids losing high-signal links in paraphrase. Question-count guidance is a heuristic, not a coverage cap. [[sources/humanlayer--humanlayer#WF03]]
4. ★ **Separate observation from recommendation (P).** HumanLayer's researcher avoids the desired implementation and describes existing behavior. Reuse this as distinct evidence and design passes to reduce confirmation bias; do not hide product context when it is necessary to interpret the system. [[sources/humanlayer--humanlayer#WF04]]
5. **Specialize workers by output contract (P/I definitions).** Locator returns where, analyzer returns how, pattern finder returns examples. Group related questions by source area rather than launching one worker per question. Role names do not enforce read-only execution: these researchers retain Bash. [[sources/humanlayer--humanlayer#WF04]] [[sources/humanlayer--humanlayer#WF06]]
6. ★ **Bind claims to source revision and evidence class (P).** Record SHA, date, branch, code ranges, tests and unresolved questions. Future agents can assess drift instead of trusting timeless prose. Source proves a revision's implementation, not live deployment or successful execution. [[sources/humanlayer--humanlayer#WF05]]
7. **Bound the uncertainty loop (P).** Draft first, then use a targeted follow-up pass on remaining gaps. Keep unresolved questions explicit rather than searching indefinitely. Adapt the stopping rule to consequence; an arbitrary one-pass limit must not block essential verification. [[sources/humanlayer--humanlayer#WF04]]
8. **Explain causes and flows, not just locations (P).** Concept-first narrative, takeaway headers and adjacent diagrams transfer a usable mental model. Keep a source index separately. Assertive headings still need to expose uncertainty, and a beautiful diagram cannot replace traceable evidence. [[sources/humanlayer--humanlayer#WF05]]

### Human-owned design

9. ★ **Recommendations are not decisions (P).** Keep choices open until the user clearly settles them; record rationale and rejected alternatives. Use this for material scope or architecture choices, not every obvious local implementation detail. The state is textual policy, not a formal approval ledger. [[sources/humanlayer--humanlayer#WF07]]
10. **Separate product outcomes from technical means (P).** PRD owns WHAT/WHY; TDD owns HOW. Call out technical decisions that change user behavior. Thin inputs should produce honest questions, not invented requirements. For small work, keep one combined document instead. [[sources/humanlayer--humanlayer#WF08]] [[sources/humanlayer--humanlayer#WF09]]
11. **Choose a success signal before a solution (P).** Agree how the change will help: adoption, latency, errors, benchmark or qualitative confirmation. Treat the signal as part of completion. Preserve the source's allowance for tiny changes with no sensible metric; avoid metric theater. [[sources/humanlayer--humanlayer#WF08]]
12. **Ask the decision that unlocks the next one (P).** Offer concrete alternatives and a recommendation; distinguish a clarifying question from agreement. Patch only when the decision settles. One-question interviews reduce cognitive load but can frustrate experts who can resolve independent questions together. [[sources/humanlayer--humanlayer#WF08]] [[sources/humanlayer--humanlayer#WF09]]
13. ★ **Maintain a coherent specification, not a transcript (P).** Rewrite affected sections and visuals after resolved decisions. Future implementers should read current intent without reconstructing the chat. Preserve version history or a separate decision log when rewriting would otherwise erase important rationale. [[sources/humanlayer--humanlayer#WF08]] [[sources/humanlayer--humanlayer#WF09]]
14. **Review the whole after approving the parts (P).** Incrementally reasonable choices can form an incoherent solution. Ask for an integrated review after the interview, with separate system/program design checkpoints. This is an explicit cognitive check, not proof of runtime authorization. [[sources/humanlayer--humanlayer#WF09]]
15. **Design contracts before internal code shape (P).** Review component interactions, messages, schemas and failure paths, then responsibilities, call trees, injection seams and signatures. Reopen earlier decisions if implementation constraints contradict them; a phase boundary should not freeze a mistaken architecture. [[sources/humanlayer--humanlayer#WF10]]

### Concrete review and implementation

16. ★ **Use the smallest revealing representation (P).** Choose a call tree, component tree, contract, pseudocode, diff, sequence diagram or focused HTML by the disputed question. Show a complete target shape when a diff hides ownership. Decorative diagrams consume the same scarce review attention. [[sources/humanlayer--humanlayer#WF11]]
17. **Use the actual product's design language in mockups (P).** Research colors, type, spacing, components and real labels before presenting UX alternatives. Update the winning mockup with the spec. A convincing HTML artifact is still not a tested production feature or accessibility result. [[sources/humanlayer--humanlayer#WF11]]
18. **Specify intent and interfaces without pre-writing every function (P).** The outline is closer to a header file than finished code. Review contracts, ownership and checks while leaving routine detail to the executor. Exact protocol rules or sensitive algorithms may still require detailed agreement. [[sources/humanlayer--humanlayer#WF12]] [[sources/humanlayer--humanlayer#WF13]]
19. ★ **Slice vertically so every phase yields evidence (P).** Build one smallest end-to-end behavior rather than all schemas, then APIs, then UI. Require an independently runnable result before the next phase. Some migrations need atomic changes; do not manufacture slices that cannot actually be verified. [[sources/humanlayer--humanlayer#WF12]]
20. **Separate automated evidence from human judgment (P).** Machines check repeatable facts; humans judge meaning, taste and usability. Do not invent manual steps for symmetry. Checkboxes are claims, so consequential validation should retain receipts and rerun when the relevant environment or code changes. [[sources/humanlayer--humanlayer#WF12]] [[sources/humanlayer--humanlayer#WF13]]
21. ★ **Keep orchestration and execution in separate contexts (P).** A parent preserves intent and review state; a phase worker spends context on code. Send short prompts with artifact paths and boundaries, even for multiple authorized phases. Another agent is not automatically an independent verifier. [[sources/humanlayer--humanlayer#WF13]]
22. **Persist progress before changing sessions (P/D).** Write settled decisions, validation and phase markers into the controlling artifact; continue while context is useful, then resume from durable state. Revalidate stale checkmarks when code or assumptions drift rather than replaying the entire history uncritically. [[sources/humanlayer--humanlayer#WF13]] [[sources/humanlayer--humanlayer#WF14]]

### Artifacts as the context protocol

23. ★ **A task must outlive one session (D).** Keep task identity, files, comments and history distinct from a conversation's model, working directory and run state. This enables specialization and handoffs. Task membership still does not prove current filesystem state or access rights. [[sources/humanlayer--humanlayer#WF14]]
24. **Give artifacts narrow ownership and precedence (D/P).** Facts, decisions, phases and review summaries answer different questions. Later intended-state artifacts supersede earlier ones; current source answers actual behavior. Add approval/version status when recency alone would let a new draft override an accepted decision. [[sources/humanlayer--humanlayer#WF14]]
25. **Expose local files and cloud review as the same artifact (D/I helpers).** Let agents use ordinary paths while people review versioned documents. Normalize tool operations and scope them to the task. Do not mistake intercepted file-tool synchronization for general repository backup. [[sources/humanlayer--humanlayer#WF14]] [[sources/humanlayer--humanlayer#WF16]]
26. **Review comments have their own lifecycle (P).** Editing a document, investigating a concern, replying, resolving and deleting are different actions. Keep reversible comment state separate from prose. Applying feedback does not necessarily mean its author has accepted the result or authorized a reply. [[sources/humanlayer--humanlayer#WF15]]
27. **Completion state should not interrupt conversational intent (I).** Zero open questions can enable a next action without forcing another completion announcement. Hooks suppress repeated templates during revisions or discussion. Reuse this distinction in UI; injected guidance alone cannot guarantee model compliance. [[sources/humanlayer--humanlayer#WF17]]

### Guarded transitions

28. ★ **Put state-dependent routing in code (I).** Central rules combine workflow type, skill and actual worktree state; tests enumerate mode/timing combinations. Keep reusable prose focused on work. The current hook supplies context with `continue: true`, so it routes advice rather than enforcing permission. [[sources/humanlayer--humanlayer#WF18]]
29. **Turn conversational handoffs into structured actions carefully (I).** Extract prompt, label, type, task and explicitly stated destination; distinguish a task-file path from a working directory. Await extraction before its consumer. For stronger assurance, prefer typed emitted actions over probabilistic prose interpretation. [[sources/humanlayer--humanlayer#WF19]]
30. ★ **Automate individual transitions, not an undefined autonomy mode (I).** Use explicit flags, labels and completion conditions while leaving material design handoffs manual. Artifact existence or a next-step suggestion is only a completion proxy; neither establishes correctness, approval or passed tests. [[sources/humanlayer--humanlayer#WF20]]
31. **Resolve collaborative settings according to ownership (I).** Owner task choices must not be shadowed by seeded per-user defaults; collaborator overrides may differ. Match UI and backend semantics and test stale/missing rows. A preference to advance is still distinct from authority for external side effects. [[sources/humanlayer--humanlayer#WF21]]
32. **Consume one-time transition consent (I).** Turn the flag off after advancement so a later rewind does not silently reuse it. Keep recurring policy separate from “advance once.” HumanLayer's reset is best-effort after launch, so it is not an atomic exactly-once guarantee. [[sources/humanlayer--humanlayer#WF21]]
33. **Deduplicate attempts without forbidding rewinds (I).** An old target-phase session should not block a newer source attempt; a newer active target should. Reuse explicit attempt/generation IDs. The inspected sibling check precedes the transaction, so concurrent duplicate prevention is not proven by the ordinary-path tests. [[sources/humanlayer--humanlayer#WF22]]
34. **Carry an execution envelope across handoffs (I).** Preserve owner, actor, host, agent, model, effort, permissions and destination, not just the prompt. Verify changed directories before use. This source path accepts an LLM-extracted directory; its presence alone does not establish safe workspace ownership. [[sources/humanlayer--humanlayer#WF23]]

### Governed context learning

35. ★ **Distill repeated steering rather than session summaries (I prompt).** Generate small standing-instruction candidates from reusable corrections; exclude episodic task details. Review their scope before reuse because repetition can reflect a narrow situation or conflicting users. The implementation explicitly labels candidate generation a prototype. [[sources/humanlayer--humanlayer#WF24]]
36. **Every learned rule needs evidence and rationale (I).** Store source user/session/message references and a bounded relevant excerpt; reject invented IDs. Immutable evidence supports later review. A real citation proves existence, not that the cited passage semantically supports the rule. [[sources/humanlayer--humanlayer#WF24]] [[sources/humanlayer--humanlayer#WF26]]
37. **Remember rejected lessons semantically (I prompt/eval).** Released and dismissed rules both exclude equivalent future proposals, reducing repeated review spam. Include noise and reworded exclusions in evaluations. Allow deliberate reconsideration when context changes; negative memory should not make obsolete rejection permanent. [[sources/humanlayer--humanlayer#WF24]] [[sources/humanlayer--humanlayer#WF26]]
38. ★ **Separate inference, organizational release and personal enablement (I).** A generated candidate is not adopted policy. Authenticated tenant/user filters only release enabled, non-dismissed shards to the daemon. Preserve these distinct states when building agent memory; a fixed item cap is not a token or conflict budget. [[sources/humanlayer--humanlayer#WF25]]
39. **Snapshot learned context at fresh launch (I).** Stable ordering and ID-only success logs help reproducibility and privacy; resume/fork does not unexpectedly refresh rules. Optional lookup failure need not stop work. Fail-open preference loading is inappropriate for mandatory security or compliance policy. [[sources/humanlayer--humanlayer#WF25]]
40. **Model and reasoning effort are separate budgets (D/I definitions).** A child can inherit a model while using different effort; research and outline implementation have different resource needs. Verify actual runtime behavior instead of assuming parent settings propagate. This investigation did not test every documented model mapping. [[sources/humanlayer--humanlayer#WF27]]

### Operational completion and packaging

41. **Transfer the PR's shape and provenance (P).** Explain why, structural change and surprising constraints rather than a file changelog; attach a real machine-readable session link. Never invent attribution. Concision must not erase required migration, compatibility or validation information. [[sources/humanlayer--humanlayer#WF28]]
42. ★ **Opening a PR is not completing the reviewable result (P).** Follow CI, fix attributable failures, retry unrelated/flaky failures once, and cap repeated repair attempts. Report what remains unresolved. The source's particular waits and approval rules are environment-specific, not universal implementation requirements. [[sources/humanlayer--humanlayer#WF28]]
43. ★ **Apply backpressure to recurring agents (D).** One unreviewed PR, concurrency groups, reviewed memory and explicit iteration triggers prevent an output flood. Update the existing branch from feedback. Scope the queue appropriately; independent owners need not share one artificial global bottleneck. [[sources/humanlayer--humanlayer#WF30]]
44. **Separate durable visibility from ephemeral execution (D).** Disposable automation daemons can report into persistent task/session history and return meaningful IDs/status to the job. The documented automation bypasses prompts, so actual authority comes from job credentials and isolation, not its temporary lifetime. [[sources/humanlayer--humanlayer#WF30]]
45. **Use a thin dispatch index and load details on demand (P/I bundle).** Map each orchestration job to a reference, consult actual CLI help, and spool large output. Shared visual guidance is bundled into consuming skills; manifest-derived versions reduce duplicated release metadata. References can still drift. [[sources/humanlayer--humanlayer#WF31]] [[sources/humanlayer--humanlayer#WF34]]
46. ★ **Parallel tasks need physical work isolation (P/D).** Give each mutable task a checkout and explicit branch; distinguish pushed code from artifact sync during host moves. Worktrees do not isolate databases, ports, caches or credentials, and pushed branches do not transport ignored files. [[sources/humanlayer--humanlayer#WF32]]

## Open questions / what's unclear

- **Prompt gates versus enforcement:** Research neutrality, design approval and completion markers are largely instructions. Researchers retain Bash; a hook that adds context is not authorization. What runtime controls enforce these boundaries, if any, is not established by the inspected workflow files. [[sources/humanlayer--humanlayer#WF06]] [[sources/humanlayer--humanlayer#WF18]]
- **Completion proxy strength:** Research advancement checks a matching task artifact, not a verified completed artifact from that exact attempt. Later phases use extracted next-step presence; the update path retains a previous positive extraction when a later pass finds none. Stronger revision-bound completion would require additional design. [[sources/humanlayer--humanlayer#WF19]] [[sources/humanlayer--humanlayer#WF20]]
- **Exactly-once behavior is unproven:** Dedup checks are before the transaction and flag reset follows creation. Tests cover ordinary and rewind behavior, not a demonstrated concurrent-call guarantee. [[sources/humanlayer--humanlayer#WF21]] [[sources/humanlayer--humanlayer#WF22]]
- **Concrete documentation drift:** The hand-written reference promises a large-PR HTML walkthrough; the current `describe-pr` skill expressly prohibits walkthrough artifacts and instead continues through CI. Prefer the owning current skill for its prompt policy. Bundled leftover walkthrough resources do not mean that policy still requests them. [[sources/humanlayer--humanlayer#WF29]] [[sources/humanlayer--humanlayer#WF34]]
- **Source naming inconsistencies:** The outline orchestrator's introduction mentions both outline and generic implementers; its operative launch step selects the outline agent. Read operative instructions and runtime definitions rather than copying every example literally. [[sources/humanlayer--humanlayer#WF13]]
- **Learning quality:** Shard schemas check source IDs and structure, not semantic entailment. The live evaluation is opt-in outside CI and was not run. No deployment status, model quality rate or production outcome is asserted here. [[sources/humanlayer--humanlayer#WF24]] [[sources/humanlayer--humanlayer#WF26]]
- **Research is not adversarial review:** The analyzer explicitly suppresses correctness/security critique. This is useful for unbiased mapping but must not replace a separate audit. Excessive interview gates and rigid vertical slicing also have costs; Oneshot and other escape hatches are essential counterexamples. [[sources/humanlayer--humanlayer#WF02]] [[sources/humanlayer--humanlayer#WF06]]
- **Installation and usage:** The source inventory and bundle mapping are verified. Standalone marketplace installation, current installed versions, usage/popularity, and deployed cross-runtime behavior were not tested. [[sources/humanlayer--humanlayer#WF33]] [[sources/humanlayer--humanlayer#WF34]]

## Patterns demonstrated

- [[patterns/structural/thin-harness-fat-skills]] — a small orchestration resolver points to job-specific references; substantial workflow knowledge stays in skills. [[sources/humanlayer--humanlayer#WF31]]
- [[patterns/composition/resolver-routing-table]] — source-owned routing combines skill, workflow and worktree state, with tests for the decision matrix. [[sources/humanlayer--humanlayer#WF18]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — models infer next actions and learned preferences; code handles schemas, identity, release filtering and transition selection. The boundary's remaining weak completion signals are explicit. [[sources/humanlayer--humanlayer#WF19]] [[sources/humanlayer--humanlayer#WF20]] [[sources/humanlayer--humanlayer#WF25]]
- [[patterns/behavioral/evidence-gated-completion]] — phase verification precedes completion markers and CI follows PR creation, while auto-advance supplies an instructive weaker-proxy counterexample. [[sources/humanlayer--humanlayer#WF13]] [[sources/humanlayer--humanlayer#WF20]] [[sources/humanlayer--humanlayer#WF28]]
- [[patterns/behavioral/diarization]] — canonical research/design artifacts preserve distilled current understanding rather than conversation transcripts; learned shards compress reusable steering with evidence. [[sources/humanlayer--humanlayer#WF05]] [[sources/humanlayer--humanlayer#WF09]] [[sources/humanlayer--humanlayer#WF24]]
- [[patterns/quality-bar/revision-bound-review]] — research captures source SHA and exact code references; this practice should extend to approval/completion instead of treating a mutable artifact's existence as sufficient. [[sources/humanlayer--humanlayer#WF05]] [[sources/humanlayer--humanlayer#WF20]]
- [[patterns/composition/single-source-multi-surface-distribution]] — source skill/reference files are embedded into the daemon and shared visual references are mapped into consuming skills. [[sources/humanlayer--humanlayer#WF34]]
- [[patterns/quality-bar/version-as-update-gate]] — the bundle reads the embedded manifest version, and its source explains release-derived version stamping for content changes; release scripts were not independently traced in this workflow investigation. [[sources/humanlayer--humanlayer#WF34]]

## Pstack comparison — 2026-10-24

[[artifacts/plugins/pstack]] complements artifact-owned RPI context with explicit engineering principles, playbook orchestration, and maintained verification models. See [[artifacts/skills/poteto-mode]] and [[concepts/verification-model-fidelity]]; neither source inspection demonstrates superior outcomes. [[sources/cursor--plugins-pstack#PP03]]
