---
domain: projects
type: design
last-reviewed: 2026-11-02
---

# Conversation Learning — proposed data contract

Owned by [[projects/conversation-learning/README]]. Initial design revision: 1. Local capture, annotation and validation prototypes cover a subset of this design; no production store or training exporter implements the full contract. [The synthetic example](example.synthetic.json) illustrates the relationships. Review using [[projects/conversation-learning/review-protocol]].

## Common envelope

Every record has `schema_version`, stable `id`, `record_type`, `revision`, `created_at`, `created_by`, `origin` (observed / human-authored / model-inferred / synthetic), and `evidence_refs`. Review adds `review_status` (unreviewed / confirmed / disputed / excluded), reviewer ID, timestamp and rationale. Unknown is explicit; missing fields never imply permission or success.

Access metadata: `owner_id`, `project_id`, `access_class`, `allowed_uses`, `rights_basis_ref`, `retention_policy_ref`. Allowed uses are explicit sets, e.g. private_analysis, internal_eval, internal_skill, provider_training, public_release. Default unset/empty means excluded from exports, not prohibited from private source review by an authorized reviewer. Export permissions are the intersection of all dependencies' allowed uses.

Evidence references use `record_id`, immutable `revision`, and optional event/text span or artifact blob hash. Text spans use Unicode code-point offsets into a named normalized-text revision, with the selected-text hash; source bytes have a separate checksum. Annotate append-only revisions with `supersedes`; never overwrite old labels. Deletion/tombstone records override ordinary append-only retention and invalidate derived releases.

## Record families

| Record | Required content beyond envelope |
| --- | --- |
| `capture` | Provider, source chat ID/link, capture method/time, source blob hash/URI, completeness by modality, truncation/omission notes, available model/harness/tool metadata |
| `task` | User objective, success criteria with origins, owner/project scope, conversation/capture IDs, episode IDs, artifact IDs, task-family/duplicate-group ID |
| `event` | Capture/task ID, provider event ID if available, sequence and parent/branch IDs, timestamp if known, actor/role, content blocks or blob refs, tool call/result IDs, visibility; model/harness/config refs or explicit unknowns |
| `artifact_revision` | Task ID, artifact ID, revision/hash, media type, blob URI, parent revision, provenance, relation to event/action |
| `intervention` | Episode ID, context cutoff and branch, offending event/action refs, feedback refs, repair refs or null, labels and evidence, active constraint refs, feedback meaning, impact, competing explanations |
| `episode` | Task/capture IDs, ordered event ranges, initial/changed goals, constraint timeline, phases/turning points, intervention IDs, outcome dimensions, effort observations, unresolved issues |
| `lesson` | Episode/intervention refs, observed pattern, scope and exceptions, proposed mechanism with confidence/rationale, alternative causes, proposed fix and responsible layer, counterfactual target provenance, evaluation refs and measured status |
| `evaluation` | Frozen input/context refs and cutoff, withheld expected criteria, evidence-backed oracle/checks, permitted tools/environment, baseline/candidate revisions and results, dataset split |
| `release_manifest` | Version/hash, selected record revisions, source capture hashes, transform code/config revision, filters, allowed use, split assignments, reviewer approvals, redaction version, exclusions and invalidations |

A raw capture URI is an authorized store pointer, not a promise the text is visible to all dataset consumers. Keep reversible identity/redaction maps separately restricted; use stable pseudonyms in derived records. Redaction can destroy useful context, so record semantic loss rather than calling a redacted task equivalent to its source.

## Annotation details

For every intervention, distinguish:

- `feedback_kind`: correction, preference, clarification, changed_goal, approval, rejection, other.
- `failure_labels`: zero or more rubric labels; optional for a preference or evolving goal.
- `constraint_available_at_cutoff`: yes / no / uncertain with event evidence.
- `attribution`: model / harness / context / tool / environment / task_change / mixed / unknown; a hypothesis with rationale, not proof.
- `acceptance`: accepted / rejected / unknown with evidence.
- `correctness`: supported / contradicted / not_checked / disputed with check evidence.
- `external_outcome`: verified_success / verified_failure / not_observed / not_applicable.
- `severity`: proposed contextual scale (minor revision / substantial rework / material consequence / unknown); do not infer harm from tone.
- `target_origin`: observed_repair / human_authored / model_generated / absent, with review independent of origin.

Include an author's local rationale, reviewer disagreement and confidence in each label. Do not turn an overall confidence number into a substitute for evidence. A user's sentence can mix a preference, factual correction and new information; annotate spans or multiple claims rather than forcing a single verdict.

## Context and hindsight

Keep two views: **decision-time input** (only information available at that branch/cutoff) and **review-time evidence** (including later outcome and feedback). Link both; never leak the second into an evaluation input. If no complete decision-time input exists, mark the record unsuitable for faithful replay.

Visible assistant explanations are observable content, not guaranteed internal reasoning. Do not fabricate hidden chain-of-thought. Model-written summaries and ideal responses remain derived hypotheses until reviewed.

## Split and export rules

Group by the whole real-world task, related chats, artifact revisions and near-duplicate task family before assigning train/development/test. All records derived from a task inherit its group. A held-out evaluation must also be protected from rule/skill authoring based on its contents; consider a later-time holdout for transfer.

For each export:

1. Resolve exact source/annotation revisions and allowed-use intersection.
2. Reject missing evidence, unresolved rights, unreviewed targets or incompatible redaction.
3. Confirm task-group separation and no context after cutoff.
4. Apply the view-specific gate from [[projects/conversation-learning/README]]. Do not emit a preference pair merely because two drafts are adjacent.
5. Record adapter/config versions, IDs and hashes in a release manifest. Map every row back to its source dependencies.
6. Honor deletion/permission changes by invalidating dependent exports; account for delivered copies explicitly. Do not promise to retract model learning or a downloaded copy automatically.

## Storage layout (proposed restricted store)

```text
captures/<capture-id>/original-export + attachments
blobs/sha256/<hash>                   # exact artifacts and payloads
records/{captures,tasks,events,artifacts}.jsonl
annotations/{interventions,episodes,lessons,reviews}.jsonl
evaluations/<evaluation-id>/
releases/<release-id>/manifest.json + derived rows
```

Use storage-native encryption, access control and backup appropriate to the owner. JSONL is a portable starting format, not an access-control system. Do not create this private corpus inside the public Research Git tree.

## Pilot-derived refinements — 2026-11-02

Grounding: [[projects/conversation-learning/pilots/commercial-redline-001/README]], [[sources/codex--commercial-redline-pilot#artifact-state]], [[sources/codex--commercial-redline-pilot#commitment-evolution]], and [[sources/codex--commercial-redline-pilot#execution-status]].

- `capture_kind` distinguishes native export, tool-response projection and sanitized evidence projection. Record retained item types, selected-command scope, page cursors, hashes and `hasMore`; never imply a partial projection is complete.
- Evidence may point to a capture revision plus stable `turn_id`/`command_id` when a full normalized event stream is unavailable. This is a bounded locator, not a substitute for decision-time context.
- `observation_form` and `repair_verification` distinguish paraphrased visible evidence, agent-reported checks, observed command output and independent reviewer verification.
- Interventions can represent clarification, changed goals or tool-process defects without explicit user feedback. A record is not necessarily a model failure. Preserve earlier approvals and constraints available at the time.
- An episode should record related artifact-state divergence and known failed substeps separately from overall tool exit status. Unknown causal origins stay unknown.
- Any source task already used to author a lesson is development evidence. Synthetic rephrasings are development probes too; their expected results are authored criteria, not measured performance.
- Each export still computes allowed-use intersection over dependencies. The pilot records permit local analysis; fixture declarations alone do not authorize training or publication of their source data.

Run `python3 scripts/check-conversation-learning.py projects/conversation-learning/pilots/commercial-redline-001` for structural/lineage checks. This is not an export gate or label-quality evaluator.

## Corpus-derived transport and review boundaries

[[sources/codex--conversation-corpus-20261102#C0018]] and [[projects/conversation-learning/runs/all-chats-20261102/README]] motivate explicit `transport_role` versus `authorship_kind` (human, assistant, tool, automation, injected/quoted, unknown). A user-role scheduling envelope is not a human correction, and an imported assistant-role tool dump is not assistant prose.

Review records distinguish full raw visible-projection reading from `full-dialogue-with-tool-inventory`. The latter requires exact dialogue IDs, complete inventoried tool IDs, inspected evidence IDs and explicit payload-review limits. Tool inventory is not independent verification of returned values. Exact deduplicated instruction blocks retain SHA-256 occurrence maps; only previously read identical bodies can be referenced instead of reread.

The evaluation-system episode adds further constraints. [[sources/codex--conversation-corpus-20261102#C0221]]

- A `review` record type does not establish human authorship. Preserve the actual annotator and evidence of human adjudication; model-generated labels cannot become human gold through a later summary.
- Link template definition, executed prompt, bindings, question revision and original output. A placeholder in the definition does not invalidate a concretely instantiated attempt. A corrected import or grade supersedes the interpretation without rewriting the original evidence.
- Keep safe behavior, task completion, grading-policy revision, answer-key maturity and attempt validity independent. An honest abstention can satisfy safety while leaving the requested task unmet.
- Review coverage, task outcomes and cost coverage advance independently. Cost metadata must name the measured scope and attribution method; reservations, authorized caps and account-wide bills cannot be substituted for exact per-attempt charges.
- A later report can contradict earlier observed evidence. Record the contradiction and unresolved interpretation; chronology alone does not make the later statement correct.

The design-program episode motivates a recurrence relation between interventions: a later repetition can show that an announced repair did not transfer. Preserve that relation, the failed samples and relevant environment state instead of retaining only the last passing rerun. [[sources/codex--conversation-corpus-20261102#C0136]]
