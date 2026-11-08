---
domain: sources
type: article
url: https://rubriclabs.com/blog/always-on-agents
retrieved: 2026-11-08
snapshot-location: sources/rubriclabs--always-on-agents/
last-reviewed: 2026-11-08
---

# Rubric Labs — Designing an Always-On Agent

## Snapshot details

- **Byline:** Dexter Storey. Published 2026-11-05; publication and modification metadata preserved in original HTML/extraction.
- **Preserved:** [full readable article](rubriclabs--always-on-agents/snapshot.md), [original HTML](rubriclabs--always-on-agents/page.html), [extracted metadata/figures/links](rubriclabs--always-on-agents/extracted-page.json); **12 hashed evidence files**. [Receipt](rubriclabs--always-on-agents/capture.json); [coverage](rubriclabs--always-on-agents/coverage.json).
- **Reviewed:** Complete prose; seven static figure/caption records and original figure HTML fragments. Banner retained. Modified 2026-11-05T21:47:23Z. Both substantive linked articles read.
- **Limits:** no interactive demonstrations or animations executed, no model calls, no benchmark replication, no implementation repository audited. Linked second-level references and navigation are listed but unreviewed. Capturing rendered initial states does not preserve a working offline interactive application.

## Anchor map

### root

Full article. Frames always-on agents as one continuous user-facing thread, proactivity and situational awareness. The claim that AGI disagreement may be about form factor is the author's hunch, not a result or a definition we adopt.

### continuity

Single-threaded: one conversational counterpart for multiple activities; heavy browser work can proceed while the main agent continues talking. Single-threaded describes user experience, not a prohibition on concurrent execution.

### context

Compaction: author reports externally imposed summaries can break momentum. Proposed tools foldContext replaces a range with an agent-written summary; dropContext removes a range from active context. Token usage visible every turn; prefer lulls/task boundaries and retain active work. No schemas, recovery behavior, controlled ablation or raw-log deletion contract supplied.

### dispatch

Dispatch: subagents take heavy work out of the main conversation and let the coordinator stay responsive. Sick-day example orders food and books a doctor in parallel. Illustrative sequence, not evidence of safe medical or purchasing authority or successful production transactions.

### wake

Heartbeat: inject a simple message into chat history; wake sleeping agent on fixed cadence or agent-requested timing. The proposal separates availability from synchronous request/response. No durable scheduling, cancellation, overlap, retry or missed-wakeup contract is given.

### communication

Messaging as a tool: only the message tool sends to the human; ordinary last-turn output remains an internal note. A wake can do work and choose silence. Austin travel example separates early preparation from delivery near arrival. This is Rubric's architecture, not this assistant's transport behavior.

### awareness

Broad access: email/browser/files and computer-use access can discover context, but access alone does not supply timely awareness. Full access is the author's suggested mechanism, not proof that least-privilege boundaries are unnecessary.

### notifications

Inbox receives adapted webhooks/polling notifications. An event such as a canceled flight should wake the agent sooner than periodic polling. Spam, irrelevant Slack and GitHub events make wake-on-every-event expensive and noisy.

### triage

Small-model filter (Jev example) separates wake-worthy events from low-priority items retained for later bulk reading. No classifier reliability, calibration, outage handling or lossless queue behavior demonstrated in this article.

### discernment

Discernment: agents may both over-act on others' messages and miss real opportunities. The Slack example pursues a message without mandate/access/context then produces an unwanted design document. No intervention precision/recall or task-benefit evaluation is provided.

### learning-lane

Designing for discernment: start conservative, explicit responsibilities, doing nothing allowed, ask when ownership is unclear, retain feedback on actions and consult it before repeating them. Thanks, corrections and silence are proposed signals, not established labels or grants of authority.

### training-hypothesis

The author attributes weaknesses to task-completion-oriented RL and proposes environments rewarding discernment/memory use. No training-data inspection, causal experiment or trained-policy result supports the universal claim about today's models.

### figures

Seven figure fragments and static labels: a day of activity, chatbot versus continuous thread, fold/drop context, sick-day workers, timed Austin message, notification filter and unsolicited Slack response. Full original HTML retained; animation timelines/scripts not replayed or bundled.

## Why we cite this

Architecture and author-reported examples for [[concepts/proactive-agent-discernment]]. Product-wide or performance generalizations remain attributed, not converted into tested guarantees.

## Popularity signals

Primary Rubric Labs field guide, retrieved November 8, 2026. No adoption, star count or popularity claim asserted.

## Related sources

- [[sources/rubriclabs--always-on-agents]] — always-on architecture and discernment.
- [[sources/rubriclabs--agent-harness]] — harness functional taxonomy.
- [[sources/rubriclabs--jev-use-cases]] — decision-model examples and qualified comparison.
