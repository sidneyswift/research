---
domain: projects
type: protocol
last-reviewed: 2026-11-02
---

# Conversation Learning — review protocol

For [[projects/conversation-learning/README]], using [[projects/conversation-learning/data-contract]]. Proposed manual pilot procedure, not a deployed collector or a new global wiki operation.

## 1. Establish the task and evidence boundary

Record the user's real objective and source-access scope. Inventory chats, branches, files and revisions. Preserve the native export and checksum it before normalization. Report missing/truncated messages, tools or instructions explicitly. A retrieved summary can suggest candidates; it cannot stand in for an exact quote or complete trajectory.

## 2. Read the whole trajectory before selecting failures

Build a compact timeline with phases, constraint changes, candidate interventions and successful stretches. Capture artifact diffs and abandoned approaches where available. Do not diagnose a three-hour exchange solely from its last frustrated message. Separate observed elapsed duration from active user effort.

## 3. Extract evidence-linked interventions

For each candidate, answer: what should have happened given information available then; what happened; what did the human say or change; did a repair happen; what evidence supports the diagnosis? Mark new requirements, changing taste, preference, and missing context distinctly. Keep disagreement and unresolved outcomes rather than forcing a clean training pair.

## 4. Explain the episode

Review goal tracking, consistency across artifacts, repeated corrections, stopping behavior and recovery. Trace each claim to events/revisions. A chain of individually reasonable replies can still lose the task's objective. Record competing explanations before assigning root cause. Include successful counterexamples when stating a general failure mechanism.

## 5. Propose remedies at the appropriate layer

Use a scoped preference for taste; a skill for a repeatable domain procedure; a deterministic check for an observable invariant; context retrieval for missing facts; a workflow/harness change for coordination; and model-training candidates for reviewed behavior not adequately handled elsewhere. These are hypotheses to compare, not conclusions from the taxonomy alone.

Write a lesson with supporting IDs, applicability, exceptions, expected benefit, possible regression, and a measurable evaluation. Keep model-generated ideal responses visibly synthetic until a human validates them. Do not silently add a global instruction based on a single incident.

## 6. Review and test

Sidney reviews intent and preferences; domain correctness may require another qualified reviewer or external check. Review does not mean every claim is correct. Preserve who checked what and disputed labels. Freeze task-group holdouts before using cases to develop training, skills or rules.

Compare baseline and proposed remedy on eligible, reconstructible inputs plus held-out tasks. Measure task success, repeated corrections, unnecessary questions/actions and regressions; mark unverifiable outcomes unknown. Record model/harness/tool versions and environment limitations. Do not infer that an offline replay reproduces a real negotiation's outcome.

## Completion gate

- Exact evidence references resolve; missing context and uncertainty are explicit.
- Interventions and episode observations are distinct from proposed causal explanations.
- Acceptance, correctness and outside-world results remain separate.
- Lessons have scope, exceptions and test criteria; no unsupported generalized rule.
- Public wiki contains only allowed sanitized material; exports pass their use-specific gates.
- If a gate fails, retain an analysis candidate with the reason; do not manufacture a training-ready row.

## Lessons from the first pilot

[[projects/conversation-learning/pilots/commercial-redline-001/README]] exposed refinements grounded in [[sources/codex--commercial-redline-pilot#commitment-evolution]], [[sources/codex--commercial-redline-pilot#artifact-state]], and [[sources/codex--commercial-redline-pilot#execution-status]]:

- Read earlier authorization before calling a later reversal a violation. Classify goal clarification and reconsideration separately.
- Mark each repair as reported, tool-observed or independently rechecked; do not use an agent's apology as sole proof of a broader causal diagnosis.
- Review artifact pairs and execution outputs as well as user corrections. A failed substep can be hidden by a later successful command.
- Preserve successes and counterexamples alongside failure candidates, including appropriate disagreement and evidence checks.
- Record exact coverage and explicitly stop claims at that boundary. Never call a four-page review the entire lifetime chat.
- Mark studied cases and derived synthetic probes development-only before calling anything a holdout.

## Corpus review tooling

For [[projects/conversation-learning/runs/all-chats-20261102/README]], the canonical annotation ledger is `reviews.jsonl`; generated intervention, lesson and catalog views must be rebuilt from it. Counts in a triage review are not annotations and do not become learning records.

1. `scripts/capture-conversation-learning.py` preserves a frozen local projection outside Research using read-only database access. Connector captures and fallback history retain their own envelopes and hashes. Capture is not review.
2. `scripts/read-conversation-review.py` displays exact slices with original locators and conservative credential masking. Imported transport roles do not establish human authorship. Tool inventories and exact repeated-instruction factoring require explicit review limits.
3. `scripts/record-conversation-reviews.py` records full visible-projection reviews only after reading. `scripts/merge-conversation-review-shards.py` validates disjoint shard coverage and imports later corrections. A question carried in a tool wrapper still requires reading its payload.
4. `python3 scripts/build-conversation-learning-views.py --run projects/conversation-learning/runs/all-chats-20261102` renders `interventions.jsonl`, `lessons.jsonl` and `review-catalog.md`. It preserves source restrictions and missing context cutoffs; it creates no desired answers or training pairs.
5. `scripts/check-conversation-corpus.py --private-corpus <restricted-capture-path> --run projects/conversation-learning/runs/all-chats-20261102 --require-complete` checks hashes, message coverage, annotation lineage and private-analysis gates. A passing result establishes structural integrity and dispositions, not semantic correctness or complete hidden/tool evidence.

Regression fixtures live in `scripts/tests/test_conversation_review.py`. Source evidence remains private; the generated catalog is a local sanitized research surface, not authorization to publish it.

## Proposed second-pass intent classification

Before assigning new corpus labels, use [[projects/conversation-learning/classification-discovery]] for the evidence-backed blindspot pass, core/conditional axes, calibration cases and revised work order. The first-pass ledger remains the completed extraction; second-pass labels are additive, separately versioned and not retroactive proof of model failure. Proposed taxonomy choices are not human-adjudicated labels.

The authorized second pass is recorded at [[projects/conversation-learning/runs/intent-pass-20261102/README]]. `scripts/check-intent-classification.py` checks decision-window provenance and temporal gates; `scripts/build-intent-classification-views.py` renders annotation views. Evaluate the original action separately from the repair: judging only the reply after a correction can conceal the original failure. Calibration refinement and adjudication do not silently rewrite first-pass observations.
