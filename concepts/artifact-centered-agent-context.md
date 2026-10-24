---
domain: concepts
type: concept
name: artifact-centered-agent-context
creators: ["[[creators/humanlayer]]"]
sources: ["[[sources/humanlayer--humanlayer]]"]
status: emerging
last-reviewed: 2026-10-23
---

# artifact-centered-agent-context

> Keep the task's current facts, decisions, progress, and feedback in explicit artifacts; let conversations and workers be replaceable consumers of that context.

## What it is

HumanLayer's workflow persists research, designs, outlines, and progress in task artifacts that multiple sessions can use. A fresh implementing agent reads the relevant artifact rather than inheriting every previous exploratory token. Create and iterate have different semantics; each document type owns a different question. Current code answers what exists, while approved design artifacts describe what should exist. This is our name for the observed architecture, not a HumanLayer claim of a new universal memory algorithm. [[sources/humanlayer--humanlayer#artifact-authority]], [[sources/humanlayer--humanlayer#context-handoff]]

The system also distinguishes **task context** from **standing guidance**. Its context-shard prototype proposes short reusable rules from recurring steering, retains message evidence, and filters what enters a fresh session through release, dismissal, and personal enablement state. A lesson is not automatically adopted just because a model generated it. [[sources/humanlayer--humanlayer#context-shards]]

## Where it came from

The evidence is the HumanLayer RPI skills, task-file synchronization, structured feedback, and context-shard generation/query/injection implementation at the pinned October 23, 2026 revision. This page is adjacent to the wiki's existing [[patterns/behavioral/diarization]] but does not equate a current-state task specification with a generalized knowledge dossier. [[sources/humanlayer--humanlayer#task-model]], [[sources/humanlayer--humanlayer#context-shards]]

## Why it matters

An indefinitely growing conversation couples useful decisions to irrelevant exploration. An artifact gives future workers a smaller, inspectable input with an explicit role. It also lets humans edit and comment on the same object the next worker will consume. The tradeoff is that compression can lose evidence or preserve a bad interpretation; explicit provenance, versioning, and unresolved questions are part of the design, not optional decoration. [[sources/humanlayer--humanlayer#context-handoff]], [[sources/humanlayer--humanlayer#feedback-targets]]

## Evidence & claims

- **Prompt policy:** in phased outline implementation, one fresh implementation worker per phase receives the phase and artifact path; progress and validation live in the outline. This is context separation, not proof of independent reasoning or worker correctness. [[sources/humanlayer--humanlayer#context-handoff]]
- **Documented + implemented:** ordinary local task files are synchronized into artifact surfaces. The inspected mirror SDK is hook/scan-driven, has a separate retrying outbox, and explicitly does not behave like a general filesystem watcher or deletion mirror. [[sources/humanlayer--humanlayer#file-artifacts]]
- **Implemented:** feedback serialization retains selected text, context, replies, authors, and captured comment IDs; accepted delivery and comment resolution are distinct outcomes. Not every typed review field is necessarily serialized by every exporter. [[sources/humanlayer--humanlayer#feedback-targets]], [[sources/humanlayer--humanlayer#feedback-delivery]]
- **Implemented prototype:** candidate standing rules must cite existing message IDs; released and dismissed rules are both exclusion inputs. Reference validation proves that a message exists, not that it entails the proposed lesson. [[sources/humanlayer--humanlayer#context-shards]]
- **Implemented:** enabled rules load at fresh launch, not resume/fork; lookup failure is nonfatal. This makes them optional context, not mandatory security policy. [[sources/humanlayer--humanlayer#context-shards]]

## Patterns demonstrated

- [[patterns/behavioral/diarization]] — related distillation instinct, with narrower task-state and standing-rule roles. [[sources/humanlayer--humanlayer#artifact-authority]], [[sources/humanlayer--humanlayer#context-shards]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — infer candidate lessons with a model; validate citation IDs, filter release/enablement, order results, and inject context in code. [[sources/humanlayer--humanlayer#context-shards]]
- [[patterns/quality-bar/revision-bound-review]] — retain the content and target a human comment actually concerned. [[sources/humanlayer--humanlayer#feedback-targets]]

## Tensions & counter-arguments

- **Compression can harden a mistake.** A coherent specification can be less truthful than a messy transcript if it loses disagreement or uncertainty. Preserve the supporting evidence and decisions that remain open. [[sources/humanlayer--humanlayer#objective-research]], [[sources/humanlayer--humanlayer#context-shards]]
- **Newer does not necessarily mean authoritative.** The workflow's simplified precedence requires adaptation when a later artifact is a draft or an unapproved revision. Do not silently replace an accepted decision with a newer suggestion. [[sources/humanlayer--humanlayer#artifact-authority]]
- **Negative memory can become stale.** Suppressing dismissed lessons reduces repetitive suggestions, but a rejected rule may become appropriate after circumstances change. Re-review is a proposed extension, not a verified feature here. [[sources/humanlayer--humanlayer#context-shards]]
- **Stable context delays updates.** Fresh-launch-only injection avoids mid-session drift but delays changed guidance. Optional fail-open retrieval must not be reused for policies that must always apply. [[sources/humanlayer--humanlayer#context-shards]]
- **Cross-host continuation has physical limits.** Shared artifacts do not move unpushed Git changes or every provider's local session history. [[sources/humanlayer--humanlayer#remote-hosts]], [[sources/humanlayer--humanlayer#context-handoff]]

## Timeline

- 2026-10-23 — Extracted the task-artifact and standing-guidance distinction from the HumanLayer source; no live memory-generation or quality evaluation was run. [[sources/humanlayer--humanlayer#context-shards]]

## Related

- [[artifacts/projects/humanlayer]] — runtime and product implementation.
- [[artifacts/plugins/humanlayer-rpi]] — complete workflow and context ledger.
- [[concepts/review-cost-aware-workflows]] — why these artifacts exist as review surfaces.
- [[concepts/agent-control-plane]] — where task identity and execution lifecycle are stored.
- [[concepts/durable-agent-execution]] — persistent context is distinct from replayable tool execution.

## What we'd steal

- ★ **Give every artifact one owning question.** Research owns facts; design owns choices; the outline owns slices and checks. [[sources/humanlayer--humanlayer#artifact-authority]]
- ★ **Pass paths and bounded work orders to fresh workers.** Preserve the orchestrator's decision context instead of filling it with implementation traces. [[sources/humanlayer--humanlayer#context-handoff]]
- ★ **Separate episodic task facts from reusable standing rules.** Do not turn a one-off request into a permanent preference. [[sources/humanlayer--humanlayer#context-shards]]
- ★ **Require provenance for candidate memory.** Store evidence IDs, excerpts, and rationale; inspect entailment separately from structural validity. [[sources/humanlayer--humanlayer#context-shards]]
- **Remember rejected candidates.** Reduce repeated proposals, while retaining a way to revisit them when circumstances change. [[sources/humanlayer--humanlayer#context-shards]]
- **Separate generation, release, and enablement.** Model inference, organizational endorsement, and personal applicability are different decisions. [[sources/humanlayer--humanlayer#context-shards]]
- **Compile feedback rather than asking people to reconstruct it.** Preserve comment identity and the surrounding content needed to act. [[sources/humanlayer--humanlayer#feedback-targets]]
- **Distinguish current truth from history.** Keep the current specification coherent; preserve prior reasoning through versions or separate records. [[sources/humanlayer--humanlayer#artifact-authority]]
- **Record context selection at launch.** Stable IDs and ordering make future investigations more reproducible, without copying sensitive message bodies into logs. [[sources/humanlayer--humanlayer#context-shards]]

## Open questions

- Do context shards measurably reduce repeated corrections without increasing cross-task overgeneralization?
- What should expire, conflict, or supersede a released rule?
- Which artifact content is sufficient for a new worker, and when must it reopen the underlying source?

## Pstack comparison — 2026-10-24

[[concepts/evidence-calibrated-research]] specializes what an evidence handoff preserves: source coverage, contradictory findings, and confidence language. [[concepts/verification-model-fidelity]] adds an authority contract between source, model, properties, and generated views. [[artifacts/plugins/pstack]] is the supporting source family. [[sources/cursor--plugins-pstack#RE03]] [[sources/cursor--plugins-pstack#RE08]]
