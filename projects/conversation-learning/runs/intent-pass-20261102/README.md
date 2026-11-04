---
domain: projects
type: classification-run
status: calibration-awaiting-human-intent-review
last-reviewed: 2026-11-02
---

# Intent and collaboration — second annotation pass

Additive follow-up to [[projects/conversation-learning/runs/all-chats-20261102/README]], implementing [[projects/conversation-learning/classification-discovery]]. **The first 24 decision windows are annotated; full-corpus phase reclassification is not complete.** These are model judgments awaiting adjudication, not a new failure-rate measurement.

## Completed calibration

- 24 deliberately selected windows across nine corpus chats and the separate SOW pilot; initial windows were expanded when needed to include earlier approval or constraint evidence.
- Six core axes: phase purpose, clarity by dimension, human contribution, decision provenance, information available at the action cutoff, and response/result.
- Explicit separation of prior action, feedback and repair. Revision 1 initially focused on some repaired responses; revision 2 preserves and evaluates prior actions separately. Earlier annotation/rubric revisions are privately preserved with hashes.
- Eight candidates flagged for human intent adjudication; two focused questions sent about original routine-tool approval intent and the development of the creative-quality standard. No answers or human approvals have been recorded yet.
- First-pass ledger and derived files preserved byte-for-byte, with a [baseline manifest](first-pass-manifest.json) and immutable private copies.

Read the [calibration catalog](calibration-catalog.md), [structured annotations](calibration-annotations.jsonl), [[projects/conversation-learning/runs/intent-pass-20261102/rubric]], [summary](calibration-summary.json) and [human-review queue](human-review-queue.jsonl). The catalog and summary are generated from annotations; their overlapping label counts are not independent examples or population shares.

## What the sample establishes

The selected windows demonstrate why one “correction” label is insufficient. Examples include explicit prototype approval, a newly requested recurrence interaction, tactful writing refined toward a more direct style while new context is supplied, user reconsideration after a clear tradeoff explanation, appropriate authorization boundaries and source-reported evaluation defects. The SOW numerical target originated in an earlier user request, but applying that target to the new contract remained a separate decision. A direct rejection of a previous answer does not automatically establish violation of an earlier explicit instruction.

Seven windows do not establish a prior violation; twelve concern non-violation activities such as approvals, discovery or newly established requirements; five remain uncertain because earlier context, artifact truth or source-reported diagnoses need reconciliation. **These categories are judgments about the selected windows, not a finding that the source chats were error-free.** The new layer retains negative feedback and reported incidents alongside the more limited violation claim.

## Remaining work and coverage

[coverage.jsonl](coverage.jsonl) lists all 506 original source dispositions. Nine chats have selected calibration windows only; 489 reviewable chats remain pending full phase review; eight retain their original source gaps. No chat is marked fully phase-classified on the strength of a few selected windows. The separate bounded SOW pilot supplies six calibration windows and is not silently treated as a new independent corpus chat.

After resolving the calibration boundary cases, retain uncertain judgments and apply the stable rubric across reviewable source phases. Classify productive and quiet stretches as well as existing interventions; retain cross-chat families and modality limits. Report task, phase and intervention units separately. No reliable whole-corpus exploration-versus-execution percentage exists yet.

## Verification and limits

`python3 scripts/check-intent-classification.py --run projects/conversation-learning/runs/intent-pass-20261102 --private-corpus <restricted-corpus>` validates frozen baseline hashes, source/window identity, rubric revisions, exact locators, action ordering and private-analysis gates. Seven synthetic regression tests reject later requirements used as earlier obligations, unknown context promoted to a violation, invented evidence, rubric/window drift, false human approval and substitution of a repair for its prior action. Passing checks establish structural consistency, not label correctness.

Raw messages and earlier context remain outside Research. The annotations contain sanitized interpretations and locators. Full artifacts, unseen model inputs, hidden reasoning, physical-device outcomes, provider behavior and domain correctness are not established by this review. Every annotation remains human-unreviewed, development-only, private-analysis-only and training-ineligible; no desired targets or training exports are created.

## Related

- [[projects/conversation-learning/README]]
- [[projects/conversation-learning/data-contract]]
- [[projects/conversation-learning/review-protocol]]
- [[projects/conversation-learning/classification-discovery]]
