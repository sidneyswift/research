---
domain: projects
type: extraction-run
status: complete-with-documented-gaps
last-reviewed: 2026-11-02
---

# All accessible chats — frozen review run

User requested the [[projects/conversation-learning/README]] process across every accessible chat, continuing until complete. The frozen accessible-chat review is **complete with documented gaps**: **506 discovered, 498 reviewed, eight unavailable or empty, zero pending**. This covers the accessible surfaces below, not every conversation in every account.

## Scope and access

The sidebar tools expose 50 recent unpinned chats plus pinned chats and paginated archives. To avoid mistaking that cap for completeness, this run also reads the local Codex metadata and visible-history projection databases in read-only transactions. The frozen metadata inventory contains **494 user-facing Codex roots**; **2,080 subagent and 4,459 guardian records** are inventoried as internal supporting/system sessions rather than independent human conversations. Ten recent and two archived ChatGPT conversations were additionally discovered through the available tools. ChatGPT discovery beyond that listing remains a stated tool limit, not a claim that the entire account was enumerated.

Initial local capture: **7,603 turns**, **68,194 visible user/assistant messages**, **18 empty projections**, zero JSON decoding failures. Empty projections require source/fallback checks before disposition. Capturing messages is not semantic review. Original source files and databases remain untouched.

## Storage and review discipline

Private projections, original tool captures, hashes and the title/ID mapping are outside Research in an owner-only local staging directory. This is not a configured backed-up corpus. Public repo records use aliases and sanitized descriptions; no private conversation dump, contract clauses, financial balances, credentials or personal contacts are published here.

Each chat remains pending until its visible text has been reviewed and a source-linked disposition is recorded. Large chats can remain partially reviewed with explicit offsets. Corrections, preferences, new requirements, failed tools, successes and unverifiable outcomes remain distinct. No-error-found is a legitimate disposition; no synthetic failure quota is imposed.

The run's own chat is bounded by the initial snapshot to avoid a self-extending loop. Active chats may advance after capture. Studied cases are development material, not untouched evaluation holdouts. Local analysis authorization does not imply model-training upload or public release authorization.

## Deliverables

- A per-chat coverage/disposition ledger, separating capture from semantic review.
- Sanitized evidence-linked intervention and episode/lesson candidates where supported.
- Cross-chat lesson consolidation by mechanism, without inventing prevalence from unreviewed chats.
- Synthetic development evaluation probes where an observable criterion is supported.
- Validation of IDs, evidence pointers, coverage and lineage; model behavior and domain correctness require separate checks.

## Completed output

| Output | Count | Meaning |
| --- | --- | --- |
| Discovered chats | 506 | 494 Codex roots and 12 ChatGPT chats |
| Reviewed chats | 498 | 421 visible-projection reviews; 77 dialogue reviews with explicit tool inventory and payload limits |
| Missing sources | 5 | C0125, C0126, C0127, C0149, C0205 |
| Inspected empty sources | 3 | C0100, C0338, C0461 |
| Pending | 0 | Every discovered chat has a review or documented evidence gap |
| Intervention annotations | 786 | Includes human feedback and separately identified observed agent/tool corrections; not 786 confirmed failures |
| Lesson candidates | 640 | Scoped model interpretations, not adjudicated training targets |
| Curated cross-chat findings | 18 | Mechanism-based consolidation, not prevalence estimates |
| Episode candidates | 8 | Longer trajectories with turning points and uncertain outcomes |
| Provisional task families | 11 | Related chats grouped without claiming complete identity resolution |
| Synthetic development probes | 14 | Proposed checks; not executed or held-out |

Start with [[projects/conversation-learning/runs/all-chats-20261102/learnings]] for the synthesis and [review-catalog.md](review-catalog.md) for per-chat observations. [coverage.jsonl](coverage.jsonl) records every disposition. [reviews.jsonl](reviews.jsonl) is the canonical annotation ledger; reviewer shards were archived privately after validated consolidation. [interventions.jsonl](interventions.jsonl), [lessons.jsonl](lessons.jsonl) and the catalog are deterministic views of that ledger. [findings.jsonl](findings.jsonl), [episodes.jsonl](episodes.jsonl), [task-families.jsonl](task-families.jsonl) and [development-probes.jsonl](development-probes.jsonl) retain curated cross-chat interpretations and their evidence.

All candidates remain human-unreviewed, development-only and training-ineligible. Private analysis is the only recorded allowed use. Human adjudication, exact target construction, future-use permissions and behavior evaluation are subsequent gates, not claimed results of this review.

## Verification

Capture hashes, exact message-ID multisets, annotation lineage, source locators, restrictions and completion dispositions pass `scripts/check-conversation-corpus.py --require-complete`. Nine synthetic regression tests pass, including duplicate coverage rejection, required user-facing tool payload inspection, corrected-review propagation, restriction preservation and rejection of silently unsupported recorder fields and unknown annotation locators. These checks establish structural consistency, not independent truth of every source-agent claim. The earlier pilot's 27 records also pass their structural validator.

The review preserves failed attempts, later retractions, changing goals and unfinished work. It does not verify historical deployments, provider behavior, legal conclusions or every attachment. No model-training or provider upload was performed.

## Evidence

[[sources/codex--conversation-corpus-20261102#capture]] binds the frozen private captures to sanitized aliases. Per-chat anchors on that source support annotation provenance.

## Typed imported-history refinement

Imported histories can store full tool call/result dumps in records labeled `agentMessage`, and scheduled/platform envelopes can arrive as `userMessage`. Transport role is not authorship. The review separates ordinary dialogue from exact imported tool wrappers; all ordinary dialogue is read, every tool occurrence is inventoried, and payload sections are inspected where needed to substantiate a finding. Huge catalog/schema outputs can remain uninspected, with explicit limits. Such reviews use `full-dialogue-with-tool-inventory`, never claim every raw payload byte was semantically read, and retain original private evidence for follow-up.

Exact repeated `<instructions>` bodies may also be factored by hash: the first unique body is read in full, repeated occurrences preserve pointers and timestamps, and all nonidentical surrounding text remains. This is deterministic factoring, not summarization or keyword-based completion.
