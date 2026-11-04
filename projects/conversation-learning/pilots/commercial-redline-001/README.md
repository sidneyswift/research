---
domain: projects
type: pilot
status: extracted-awaiting-human-review
last-reviewed: 2026-11-02
---

# Pilot 001 — commercial redline collaboration

A real extraction run for [[projects/conversation-learning/README]]: **10 intervention records, two episode records, eight lesson candidates, and four synthetic development-evaluation fixtures**. The evidence is a bounded review of the chat **Seeker SOW**; private contractual detail is excluded from this repo. [[sources/codex--commercial-redline-pilot#communication]]

**Read this as a reviewed source extraction with model-authored annotations awaiting Sidney's review.** No annotations are human-confirmed, no original conversation is training-ready, no remedy has demonstrated better model behavior, and nothing was sent to the counterparty or uploaded for training.

## What was actually reviewed

Four paginated chat reads: all 32 returned November 2 turns, 13:32–17:08 America/New_York, plus eight immediately preceding October 21 turns. The November wall-clock span is approximately 3h37m, not active user work. The source is not the whole lifetime chat: older turns remain, audio is only represented by handoff text, and full environment/instruction and artifact history is missing. The committed [[sources/codex--commercial-redline-pilot]] points to a sanitized immutable projection; private message projections and five selected command records are outside Research in local staging with checksums and owner-only filesystem modes. That staging is not a backed-up or shared corpus.

## Episode A — document quality improved faster than task alignment

The task was to review a received commercial draft, create genuine tracked changes, and explain changes simply enough to close the engagement. Initial review identified material risks and the agent produced inspectable document checks. Across later revisions, however, the user repeatedly supplied the decision policy: protect meaningful interests, avoid unnecessary negotiation, preserve the working relationship, and make continued work easy to agree. The observed sequence suggests local paragraph/document repair outpaced carrying that policy across the whole deliverable pair. This is a reviewer hypothesis, not proof of an internal model mechanism. [[sources/codex--commercial-redline-pilot#communication]] [[sources/codex--commercial-redline-pilot#changes-only]]

| Phase | Observation | Interpretation boundary |
| --- | --- | --- |
| Review and proposed edits | Agent identifies risk and explicitly discloses a substantive scope change | Broad initial review was requested; number of edits alone does not establish overreach |
| Redline and email | Native tracked changes and source-restoration checks are reported | File mechanics do not establish commercial alignment or legal correctness |
| Explain tool permissions | Multiple rewrites preserve batch approval until the user explicitly rejects it | The exact no-upfront-approval constraint becomes explicit later; earlier wording allowed another reading |
| Simplify negotiation | User questions extra numerical terms and added restrictions; agent removes them | Numerical target came from earlier user instructions; it was not hallucinated |
| Reconcile deliverables | Agent observes old email descriptions diverging from the redline | Divergence is observed; the source of the stale state is unknown |
| Revisit delivery promise | Clearer explanation leads user to restore original commitments | This includes reconsideration of an earlier authorized substantive change, not a proven unilateral breach |
| Remove unnecessary explanation | User twice questions why a restored provision remains in the email | Once a change is undone, its explanation needs reevaluation across the whole email |

Sources: [[sources/codex--commercial-redline-pilot#operational-intent]], [[sources/codex--commercial-redline-pilot#evaluation-provenance]], [[sources/codex--commercial-redline-pilot#artifact-state]], [[sources/codex--commercial-redline-pilot#commitment-evolution]].

**Holistic lesson:** maintain a small decision ledger shared by the edited artifact and its explanation: preserve, change, rationale, approval, and actual current revision. Reassess the whole pair when a decision changes. This proposed remedy targets decision continuity and artifact consistency; it is not a global instruction to minimize every legal protection. The original task is development evidence now and cannot serve as an untouched holdout.

## Episode B — evaluation status was mistaken for evidence

In the earlier episode, the user questions whether a saved result had the needed context. The agent correctly refuses to assert an unproven environment-specific pass. But when asked to remove unsupported results, it then treats approval/status notes as the factual evidence boundary, excludes supported candidates, and acknowledges the error after challenge. It later reports comparing historical answers against historical source snapshots and issuing an audit. This pilot verifies those observable statements and corrections; it does not revalidate the reported count. [[sources/codex--commercial-redline-pilot#historical-evidence]]

**Holistic lesson:** provenance, context availability, formal approval, factual support and freshness need separate fields. A conservative label filter can still produce a false claim. Preserve excluded/uncertain candidates and reasons rather than irreversibly collapsing the dataset into a single pass flag.

## Eight lesson candidates

| ID | Lesson | Proposed fix location | Evidence |
| --- | --- | --- | --- |
| L01 | Plain wording requires cause and consequence, not merely fewer paragraphs | Communication skill scoped to the requested audience | [[sources/codex--commercial-redline-pilot#communication]] |
| L02 | Test the operational result of a rewrite against the user's clarified intent | Task constraint check; preserve legitimate spending/data boundaries | [[sources/codex--commercial-redline-pilot#operational-intent]] |
| L03 | Explain the actual current diff; distinguish inherited ideas, existing terms and new changes | Revision-bound change ledger and paired document/email review | [[sources/codex--commercial-redline-pilot#evaluation-provenance]] [[sources/codex--commercial-redline-pilot#changes-only]] |
| L04 | Clarify substantive tradeoffs before committing to them; allow later user reconsideration | Decision workflow; record what was authorized and when | [[sources/codex--commercial-redline-pilot#commitment-evolution]] |
| L05 | Bind related outputs to a canonical revision and detect stale working copies | Artifact tooling/workflow | [[sources/codex--commercial-redline-pilot#artifact-state]] |
| L06 | Separate answer evidence, environment, review approval and historical/current validity | Dataset schema and factual verification procedure | [[sources/codex--commercial-redline-pilot#historical-evidence]] |
| L07 | A later successful command must not hide an earlier mutation failure | Fail-fast execution, validate-all-before-write and staged paired updates | [[sources/codex--commercial-redline-pilot#execution-status]] |
| L08 | Name the actual temporal trigger, particularly for work already underway | Explicit dates/events in explanations and constraints | [[sources/codex--commercial-redline-pilot#evaluation-provenance]] |

The structured [records](records.jsonl) preserve evidence IDs, decision cutoffs, observed feedback, uncertainty, alternative explanations and proposed fixes. They contain sanitized paraphrases, not preference-training pairs.

## Successes and limits

- The agent disclosed a substantive scope change before the later reconsideration. Do not relabel this as covert scope weakening. [[sources/codex--commercial-redline-pilot#commitment-evolution]]
- It challenged a consequential premise rather than merely agreeing. This is observable disagreement; legal correctness is not established here. [[sources/codex--commercial-redline-pilot#successful-controls]]
- It inspected document parts/metadata and checked reversibility rather than relying entirely on assurance. Those are observed tool actions, with checks reported by the source agent. [[sources/codex--commercial-redline-pilot#successful-controls]]
- No send action appears in the bounded episode. This is not an independent mailbox audit.

## What this run adds to the dataset design

Applied in [[projects/conversation-learning/data-contract]] and [[projects/conversation-learning/review-protocol]]:

1. A bounded tool projection must say what it omits; a sanitized source snapshot is not an original export.
2. Separate an observed statement from independent artifact verification, including claims about successful repair.
3. Classify evolving intent and prior user approvals before scoring a correction as failure.
4. Track regressions between paired artifacts, not only conversation messages.
5. Include process/tool failures with no explicit user correction.
6. Once a task informs rules or lessons, mark it development evidence; paraphrases of it are development probes, not independent holdouts.

These improve research machinery now. The proposed communication and execution remedies are not silently installed into the user's other projects.

## Evaluation candidates

[Four synthetic fixtures](evaluations.jsonl) cover change explanations, routine-tool permissions, evidence/status separation and shell failure propagation. They are authored probes derived from this case, not exact chat replays or held-out tests. Each includes expected checks and a regression case. Structure/lineage validation is implemented; model behavior and the risky shell sequence have not been executed.

For a meaningful improvement claim, run baseline and candidate configurations, review outcomes, and reserve a different task family or later-time task before developing the remedy. Original-chat replay also requires reconstructing missing instructions/tools and a trustworthy artifact baseline.

## Patterns demonstrated

Applications and evidence candidates, not new confirmed artifact examples:

- [[patterns/quality-bar/revision-bound-review]] — actual observed artifact-state mismatch motivates revision binding.
- [[patterns/quality-bar/defect-derived-validation]] — derive evaluation probes from observed corrections.
- [[patterns/behavioral/latent-vs-deterministic-split]] — automate lineage and structural checks; retain human review for intent and tradeoffs.
- [[patterns/behavioral/evidence-gated-completion]] — distinguish zero exit status, valid document structure, aligned content and completed task.

## What we'd steal

- ★ Evidence-linked local corrections **plus** an episode narrative showing repeated friction.
- ★ Counterexamples that prevent exaggerated failure labels and hindsight blame.
- ★ A decision/diff ledger shared by edited artifacts and explanatory text.
- ★ Independent dimensions for review state, provenance, factual support and freshness.
- Track stale artifacts and partial command failures as first-class incidents.
- Capture successful recovery without treating the agent's report as independent verification.
- Preserve scope, permissions and data-split lineage in sanitized derivatives.

## Open questions

- Does Sidney agree with these diagnoses, particularly the intent-evolution classification?
- Which permitted private storage should replace local evidence staging?
- Which separate task should become the untouched evaluation holdout?
- Can artifact versions and full decision-time context be reconstructed for faithful replay?
