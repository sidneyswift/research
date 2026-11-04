---
domain: projects
type: internal-project
status: design
owner: Sidney Swift
last-reviewed: 2026-11-02
---

# Conversation Learning

Turn everyday human–AI collaboration into an evidence-backed record of what failed, what helped, and what should change. Preserve enough context to learn from one response, a three-hour task, or recurring behavior across months.

**Status:** project charter, data contract, a bounded extraction pilot at [[projects/conversation-learning/pilots/commercial-redline-001/README]], and a completed frozen accessible-chat review (498 reviewed, eight documented gaps) at [[projects/conversation-learning/runs/all-chats-20261102/README]]. Local capture, review-ledger validation and deterministic annotation views now exist. Annotations remain model-reviewed candidates; no production backed-up corpus, training export, training run or demonstrated model improvement exists.

## Origin and scope

Sidney wants both local correction data and holistic lessons, reusable for training, post-training, harness engineering, skills, and future methods. [[sources/sidney-swift--conversation-learning-brief#requirements]]

This is an internal build project, distinct from the wiki's external artifact catalog. The architecture below is tested through bounded extraction work, while its training and evaluation uses remain proposals. Existing research supplies two useful constraints: accepted revisions need not be correct, and observed defects can produce practical validators. [[sources/SHL0MS--skill-diffs#gold-caveat]] [[sources/SHL0MS--skill-diffs#skill_linter]]

## The central design

Keep an immutable evidence archive, versioned annotations, and reproducible exports. Do not make a single provider's fine-tuning format the master record. This applies [[patterns/composition/single-source-multi-surface-distribution]] to data: one evidence base, multiple derived surfaces.

| Level | Preserve | Question it answers |
| --- | --- | --- |
| Events | Messages, visible tool calls/results, attachments and exact artifact revisions, available instructions/configuration | What did the agent actually have and do? |
| Interventions | Trigger, failed response/action, user's correction, repair, and evidence for each label | What needed correction at this moment? |
| Episodes | Task goal, phases, decisions, constraint changes, failed approaches, recovery and final outcome across one or several chats | Why did the overall collaboration succeed, drag on, or break down? |
| Lessons | Evidence from episodes, scope, competing explanations, exceptions, proposed remedy and a test | What could improve future behavior, and where should the fix live? |

A fifth record, the **task**, groups all chats, episodes and document revisions for the same real-world objective. A topic switch can begin a new episode inside one chat; a resumed task can span chats. Conversation boundaries are not task boundaries. See [[projects/conversation-learning/data-contract]] for record fields and relationships.

## Capture the narrow signal

An intervention links the precise pre-correction context to an observable response/action, feedback, and any repair. Include the user's own edits to documents, not just chat corrections. Keep a context cutoff: information learned later can explain the incident but must not be silently inserted into what the model knew at the time.

Label the feedback's meaning: factual correction, preference, instruction violation, missing context, goal change, tool/environment problem, clarification, or unresolved disagreement. These are proposed review labels, not a claim that every correction fits one category. Allow multiple labels and revisions.

Keep acceptance, preference, verified correctness, and external outcome as separate fields. Silence is not approval. A later draft is not automatically a better answer to the earlier prompt. This extends the existing [[concepts/imitation-vs-correctness-eval]] distinction to conversational feedback.

## Capture the holistic signal

An episode is a structured case study with a referenced timeline, not just an AI-written summary. Record:

- Original goal and success criteria; what changed, when, and who changed it.
- Constraints active in each phase; which were explicit, inferred, or unavailable.
- Turning points and repeated corrections, linked to event IDs and document versions.
- Local repairs that caused downstream regressions, abandoned branches, and successful recoveries.
- Outcome dimensions separately: artifact accepted, task completed, externally verified, or unresolved.
- Observed user effort: correction count and explicit rework; elapsed time is not assumed active work.
- Alternative explanations: model capability, harness/instruction conflict, context loss, missing tool, environment failure, evolving intent, or reviewer error.

For the suggested SOW pilot, examine whether contract edits, commercial intent, and the accompanying email stayed consistent through revisions. That is a review question, not an assertion that inconsistency occurred. A task can contain many good individual answers yet require excessive steering; conversely, an early error can be followed by excellent recovery.

## Many uses from the same evidence

These are proposed export views, each with its own eligibility gate. No claim that the pilot is large or clean enough to train a model.

| Use | Derived unit | Gate |
| --- | --- | --- |
| Harness/skill improvement | Scoped lesson → instruction, tool check, or workflow change | Evidence, exceptions, replay test and regression check; keep personal taste scoped |
| Evaluation | Pre-intervention context + withheld rubric + observable checks | Freeze before remedy development; reserve whole task families from training |
| Supervised fine-tuning | Context → human-reviewed desired response/action | Demonstrated or separately authored target; label synthetic targets and hindsight |
| Preference learning, including DPO | Same context → preferred and dispreferred alternatives | Actual comparison on the same information and task; no automatic adjacent-turn pairing |
| Process/reward supervision | Observed step/action → reviewed label/rationale, plus terminal result | Label only visible steps; preserve unknowns and reviewer disagreements |
| Trajectory learning | Multi-step context/action/outcome sequence | Tool and environment fidelity, explicit recovery/outcome labels, reproducible access |
| Continued pretraining | Authorized curated text corpus | Separate decision about objective, rights, data mixture and scale; no default export of raw errors |
| Future methods | New views over original evidence and annotation history | Preserve provenance and capability gaps instead of promising universal compatibility |

Preference optimization and step-level feedback are useful further reading: [DPO](https://arxiv.org/abs/2305.18290) and [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050). They have not been ingested or fully reviewed here. They do not establish that contract-collaboration feedback will yield the same gains as their experiments.

## Storage and access

**Research Git stores design, schemas, sanitized lessons, and clearly synthetic examples.** Private source chats, contracts, identifying details and outputs belong in a separate restricted corpus. This repository is described as public in its existing `.gitignore`; do not put the pilot transcript here. An ignored local directory alone would not provide access control or backup.

Start with JSONL metadata/annotations and content-addressed files for exact source exports and attachments in that restricted store. Use a small SQLite index only when queries justify it; add Parquet export for larger analysis later. These are implementation choices, not installed infrastructure.

Preserve provider-native exports as well as normalized events; explicit missingness is better than invented completeness. A summary-only chat API may be adequate for triage and inadequate for exact training examples. Do not claim hidden reasoning, truncated tool results, system instructions or unsaved document revisions were captured.

Keep owner, project/tenant, access class, and allowed uses on records. Private review, internal skill extraction, provider training upload, and public release are separate permissions. Derived lessons can still reveal sensitive facts. Deletion must be able to find dependent exports and annotations; immutable capture means never silently rewrite evidence, not retain it against a deletion requirement.

## Pilot and definition of done

1. Capture one bounded task with original export, available artifact revisions, permissions and a completeness report. Suggested candidate: Seeker SOW, with exact evidence access still to be established.
2. Review the complete task; extract supported corrections, successes and unresolved cases. Include quiet successful stretches to avoid a failure-only sample. Use [[projects/conversation-learning/review-protocol]].
3. Build one evidence-linked episode and at least one lesson candidate. Do not fill a quota by inventing failures.
4. Have Sidney review inferred intent, preferences, high-impact claims and disputed labels. Keep unreviewed candidates out of training exports.
5. Produce one replayable evaluation from an eligible case and one proposed harness/skill change. If the evidence supports neither, record why.
6. Compare baseline and changed behavior on held-out cases: task success, repeated corrections, regressions and review effort. Record model, harness and environment revisions. A single successful replay is limited evidence.
7. Export only eligible records, with manifest, lineage and split checks. Confirm no private corpus content was added to the public wiki.

**Done for this design phase:** linked project charter, data contract, review protocol, synthetic worked record and explicit pilot boundaries. **Done for the pilot:** inspectable evidence, reviewed annotations and a reproducible evaluation; not a training claim.

## Patterns demonstrated

Design applications, not new confirming artifact examples:

- [[patterns/composition/single-source-multi-surface-distribution]] — canonical evidence with versioned export adapters.
- [[patterns/quality-bar/defect-derived-validation]] — derive checks from observed corrections instead of adding generic rules.
- [[patterns/behavioral/latent-vs-deterministic-split]] — automate hashes, IDs and export gates; review intent and causality with human judgment.
- [[patterns/quality-bar/revision-bound-review]] — bind annotations to exact conversation/artifact revisions.

## What we'd steal

- ★ Preserve the full task trajectory alongside individual correction records.
- ★ Separate observed behavior, reviewer interpretation, hypothetical remedy and measured improvement.
- ★ Reserve evaluations before training or writing rules from the same cases.
- ★ Keep provider formats as exports and exact evidence as the durable center.
- Capture successes, recovery and unresolved disagreement, not only failures.
- Track information availability so later insight does not become a false earlier capability.
- Route fixes to the responsible layer: tool, context delivery, workflow, scoped preference, skill, or model.
- Preserve permitted uses and deletion lineage through every derivative.

## Open questions

- Can a complete Seeker SOW export, branches, tool traces and document revisions be obtained beyond the bounded pilot?
- Where should the restricted corpus live, who owns it, and what uses are allowed?
- What review burden is sustainable during daily work versus retrospective task reviews?
- Which recurring errors merit global rules, and which are specific to a person, domain or task?
- Does a remedy transfer to held-out tasks without creating new failure modes?

## Related

- [[projects/conversation-learning/classification-discovery]] — finding-unknowns pass and revised second-pass classification brief.

- [[projects/conversation-learning/data-contract]] — canonical record contract.
- [[projects/conversation-learning/review-protocol]] — annotation and review procedure.
- [Synthetic example](example.synthetic.json) — illustrative linkage; not a real incident or approved training record.
- [[concepts/commit-history-as-training-data]] — correction histories as evidence.
- [[concepts/imitation-vs-correctness-eval]] — accepted behavior versus independent checks.

## Pilot runs

- [[projects/conversation-learning/pilots/commercial-redline-001/README]] — first real extraction: two episodes, ten intervention annotations, eight lesson candidates and four synthetic development probes. See the pilot for missing evidence and interpretation limits.

## Corpus expansion

- [[projects/conversation-learning/runs/all-chats-20261102/README]] — user-requested exhaustive accessible-chat review, with separate capture/review status and explicit discovery limits.

## Intent reclassification

- [[projects/conversation-learning/runs/intent-pass-20261102/README]] — additive second pass: 24 decision-window calibration annotations, exact evidence boundaries, candidate labels and human-intent review queue. Full phase classification remains pending; the completed first-pass extraction is preserved.
