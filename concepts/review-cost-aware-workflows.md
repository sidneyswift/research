---
domain: concepts
type: concept
name: review-cost-aware-workflows
creators: ["[[creators/humanlayer]]"]
sources: ["[[sources/humanlayer--humanlayer]]"]
status: emerging
last-reviewed: 2026-10-23
---

# review-cost-aware-workflows

> Organize agent work around the cost of checking and correcting it: review facts before designs, designs before large code changes, and runnable slices before accumulating more unchecked work.

## What it is

An agent can generate code faster than a person can understand it. HumanLayer treats that imbalance as a workflow-design problem: move consequential decisions into smaller artifacts that humans can inspect cheaply. Research establishes current facts; design establishes intended behavior; a structure outline defines independently checkable slices; implementation applies those choices. The number of stages should match the risk, rather than being compulsory ceremony. This is our descriptive name for the mechanism, not a term HumanLayer claims to have invented. [[sources/humanlayer--humanlayer#workflow-phases]]

## Where it came from

HumanLayer's workflow explanation explicitly identifies review as the bottleneck and recommends the shortest workflow that controls the main risk. The RPI plugin operationalizes that account as research, design, outline, implementation, and iteration procedures. This ingest studies the October 23, 2026 source snapshot; it does not establish historical priority for staged development. [[sources/humanlayer--humanlayer#workflow-phases]]

## Why it matters

The useful optimization target becomes **validated progress per unit of human attention**, not generated tokens or parallel sessions. That metric is a proposed application of the source's argument, not a measured HumanLayer result. Review a schema with its consuming query, or a function interface with its call path, while changing them is still cheap. Ship the first complete behavior early enough to discover a wrong assumption. [[sources/humanlayer--humanlayer#workflow-phases]]

## Evidence & claims

- **Documented rationale:** planning puts decisions before expensive implementation and gives each review a clear subject. No controlled productivity benchmark is provided here. [[sources/humanlayer--humanlayer#workflow-phases]]
- **Documented mechanism:** current-state research is distinct from future-state design; PRD and TDD may separate product and engineering decisions. [[sources/humanlayer--humanlayer#workflow-phases]]
- **Prompt policy:** implementation follows an approved artifact, works in phases, and normally pauses for manual verification. A prompt instruction is not an unbypassable authorization boundary. [[sources/humanlayer--humanlayer#implementation-gates]]
- **Implemented supporting mechanism:** local review markers preserve which content version was marked reviewed, allowing later work to be inspected as a delta. These localStorage records are not a shared approval ledger and do not prove the marked version was understood or approved. [[sources/humanlayer--humanlayer#review-watermarks]]

## Patterns demonstrated

- [[patterns/behavioral/evidence-gated-completion]] — a phase is paired with automated and human verification, rather than treating generated code as completion. [[sources/humanlayer--humanlayer#implementation-gates]]
- [[patterns/quality-bar/revision-bound-review]] — retain the version that was actually reviewed; do not transfer that judgment silently to a later version. [[sources/humanlayer--humanlayer#review-watermarks]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — choose workflow depth with judgment; represent review state and route allowed transitions in code. [[sources/humanlayer--humanlayer#auto-advance]]

## Tensions & counter-arguments

- **Ceremony can cost more than the mistake.** The source explicitly allows a short Oneshot path. A rename or already-understood fix should not acquire a PRD merely because the infrastructure supports one. [[sources/humanlayer--humanlayer#workflow-phases]]
- **Small artifacts can still be wrong.** A well-written plan does not prove its assumptions. Keeping research objective and validating slices are separate protections. [[sources/humanlayer--humanlayer#objective-research]]
- **A phase boundary is not always a permission boundary.** Users can authorize multiple phases, and supported auto-advance transitions can continue without another manual invocation. Preserve the user's actual authorization instead of mechanically asking again. [[sources/humanlayer--humanlayer#workflow-phases]], [[sources/humanlayer--humanlayer#auto-advance]]
- **Review still consumes attention.** Parallel generation can overwhelm the queue. The automation guide's one-open-agent-PR guard is a documented response, not proof of a hard global WIP limit. [[sources/humanlayer--humanlayer#automation]]

## Timeline

- 2026-10-23 — Extracted from HumanLayer's workflow explanation, RPI instructions, review state, and transition logic. [[sources/humanlayer--humanlayer#workflow-phases]]

## Related

- [[artifacts/projects/humanlayer]] — complete extraction and portable-idea ledger.
- [[artifacts/plugins/humanlayer-rpi]] — the installable workflow layer.
- [[concepts/completion-contract]] — defines what completion means; this concept determines when and at what granularity to inspect progress.
- [[concepts/artifact-centered-agent-context]] — supplies the stable artifacts that make staged review possible.

## What we'd steal

- ★ **Choose review stages by the cost of a wrong assumption.** Use a short path when the answer is obvious; add research or design review only where uncertainty warrants it. [[sources/humanlayer--humanlayer#workflow-phases]]
- ★ **Keep facts and proposals in different artifacts.** A reviewer should know whether they are correcting a statement about the current system or choosing its future. [[sources/humanlayer--humanlayer#objective-research]]
- ★ **Plan vertical slices with an observable result.** A route returning fixed data can be checked before the next slice adds persistence. [[sources/humanlayer--humanlayer#workflow-phases]]
- **Review queries with schemas and call paths with interfaces.** Make hidden performance and integration assumptions visible before implementation. [[sources/humanlayer--humanlayer#workflow-phases]]
- **Record reviewed versions and show the delta.** Do not make people re-review an entire evolving artifact. [[sources/humanlayer--humanlayer#review-watermarks]]
- **Bound unreviewed output.** For recurring agents, consider one outstanding proposed change per job before generating another. [[sources/humanlayer--humanlayer#automation]]
- **Treat approval and factual verification as different operations.** A user liking the plan does not prove the implementation passed its checks. [[sources/humanlayer--humanlayer#implementation-gates]]

## Open questions

- What is the measured effect on review minutes, escaped defects, and rework across task sizes?
- Which transitions benefit from human review, and which can be safely delegated under an existing authorization?
- Can reviewer workload and queue age provide a better auto-advance throttle than a fixed stage count?

## Pstack comparison — 2026-10-24

[[artifacts/plugins/pstack]] and [[concepts/evidence-calibrated-research]] expose decision queues, confidence tiers, and bounded review artifacts so a human can inspect the consequential choices. Prompt-prescribed attention savings remain unmeasured. [[sources/cursor--plugins-pstack#RE08]] [[sources/cursor--plugins-pstack#RE16]]
