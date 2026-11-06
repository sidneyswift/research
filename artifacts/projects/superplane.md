---
domain: artifacts
subdomain: projects
type: project
name: superplane
creator: "[[creators/superplane]]"
source: "[[sources/superplanehq--superplane]]"
ecosystem: multi-provider
status: source-investigated
last-reviewed: 2026-11-04
---

# SuperPlane — durable workflows around coding agents

> Put repeatable engineering work in an explicit process: keep the task durable, delegate judgment to agents, coordinate mutations, and make progress depend on observable state. A workflow that finishes is still not proof that its change is correct.

## Attributes

- **Unit of study:** the SuperPlane monorepo at `7d755d16b8ae836ecebf61639efc6266d74a4b0b`, retrieved 2026-11-04. Full local tracked source saved: **10,205 entries**, shallow Git history; source map, hashes and restoration recipe published separately. [[sources/superplanehq--superplane]]
- **Architecture:** Go modular monolith with independently scalable API/workers, PostgreSQL state, RabbitMQ notifications, protobuf/gRPC/REST contracts, React/TypeScript UI and integrated runner/fleet machinery. [[sources/superplanehq--superplane#architecture]] [[sources/superplanehq--superplane#runner-protocol]]
- **Product framing:** a factory for turning high-confidence backlog work into reviewed changes, using agents, external checks, feedback and human decisions. This is the README's positioning, not a demonstrated one-shot success rate. [[sources/superplanehq--superplane#root]]
- **Distribution/license:** Apache-2.0 outside `ee/`, separate Enterprise terms inside `ee/`. Runtime licensing and source licensing are different: billing is EE source but does not require a runtime license feature. [[sources/superplanehq--superplane#license]]
- **Attention at retrieval:** 8,785 stars / 690 forks. No measured adoption, speedup, autonomous completion rate or cost advantage claimed. [[sources/superplanehq--superplane]]
- **Evidence class:** selected implementation and bundled templates read; architecture/contributor docs and a clearly labeled draft PRD consulted; selected test assertions inspected, **not executed**. No installation, provider execution or deployment.

## Relationships

- **Creator/source:** [[creators/superplane]] · [[sources/superplanehq--superplane]].
- **Control/runtime:** [[concepts/agent-control-plane]], [[concepts/durable-agent-execution]], [[concepts/agentic-loop]], [[concepts/completion-contract]].
- **Review/evidence:** [[concepts/review-cost-aware-workflows]], [[concepts/verification-model-fidelity]], [[concepts/artifact-centered-agent-context]], [[concepts/trace-lake]].
- **Comparisons:** [[artifacts/projects/codex]], [[artifacts/projects/background-agents]], [[artifacts/projects/humanlayer]], [[artifacts/projects/eve]]. These operate at overlapping but different layers; no runtime comparison was performed.

## Mechanism and themes

### 1. Make the work record outlive any one execution

The factory PRD calls the Work Order the durable record spanning multiple automations, but is explicitly **Draft**. Its proposed lifecycle must not overwrite the implementation: the pinned model uses `draft`, `open`, `closed`, with a separate result and an allowed-transition table. Transitions require an execution owner when opening a draft, prevent return to draft during an active line dispatch, clear obsolete waiting notes, and record a status event in the same database transaction. Closing also drops queued line work and requests run cancellation. A mutable current-state projection plus event records is useful without claiming a universally immutable event store. [[sources/superplanehq--superplane#factory-draft]] [[sources/superplanehq--superplane#work-order]]

The implementation template separates agent work from orchestration. The agent is told to follow repository-owned instructions, implement and commit; deterministic steps commit leftovers, check that there are commits ahead of the base, push, and require title/description files. Later graph nodes find an open PR and create or update it, then attach the artifact to the task. The instruction not to create the PR is **prompt policy**, not evidence that the agent lacks credentials to do so. Similarly, “commits exist” is not a behavioral correctness check, and leftover auto-commit is a policy choice to scrutinize. [[sources/superplanehq--superplane#implementation-template]]

### 2. Durable state first, notifications for latency, polling for recovery

The event router consumes notifications and also scans pending events every minute. It locks an event and transactionally records downstream queue items plus routing state, then publishes notifications after commit. The queue worker similarly locks the node, records dispatch changes and publishes after its transaction. This grounds a **database-backed catch-up path**, not a cross-system exactly-once guarantee: RabbitMQ publication and PostgreSQL commits are not one atomic operation here, and arbitrary external effects need their own idempotency/reconciliation. [[sources/superplanehq--superplane#event-routing]] [[sources/superplanehq--superplane#queue]]

Node queues use resolved keys and capacity limits. Full queues retain FIFO ordering without blocking unrelated keys; the scan window is bounded, and self-managed merge/loop components own admission differently. A focused test puts another branch behind a full queue's deep backlog and asserts that it still dispatches. This is stronger evidence than a generic claim of “parallel agents,” but the test was inspected, not run. Runner scheduling separately allocates organization capacity with locks and FIFO pending tasks. These are distinct admission scopes. [[sources/superplanehq--superplane#queue]] [[sources/superplanehq--superplane#queue-test]] [[sources/superplanehq--superplane#runner-admission]]

### 3. Completion, business outcome and configuration identity are separate

Executions persist state, result, reason, root-event/run/previous-execution references and copied node configuration. Passing records output events and completion together; finished or cancelling executions do not emit another pass through that path. The run finalizer locks the run and refuses finalization while active executions, queue items or pending events remain. This establishes workflow quiescence at the tracked-work boundary, not that every desired external outcome happened. [[sources/superplanehq--superplane#execution-state]] [[sources/superplanehq--superplane#finalization]]

The component guide distinguishes an execution error from a legitimate negative business outcome and gives those outcomes explicit channels. An approval rejection is emitted as an outcome, not necessarily an infrastructure failure. Collapsing all these into one success boolean loses the reason for the next action. [[sources/superplanehq--superplane#operator-interface]] [[sources/superplanehq--superplane#approval]]

Canvas edits use per-user staging and an explicit commit. The commit path checks stale staging before and inside the transaction, creates a version and publishes it. **Important limit:** an execution's copied configuration does not freeze the entire run: the event router reads live edges when routing subsequent events. Record separately the versions of graph, node configuration, input, code and credentials; do not infer replay determinism from a versioned editor. [[sources/superplanehq--superplane#staging]] [[sources/superplanehq--superplane#execution-state]] [[sources/superplanehq--superplane#event-routing]]

### 4. Coordinate mutation and bound the repair loop

PR activities distinguish concurrent work from requests for exclusive mutation access. Exclusive requests wait in request order; the current owner can re-request without consuming a new reservation. Where a feedback handler has a maximum-attempt limit, acquiring exclusive access reserves the attempt. The limit pauses further fixing, and passing evaluations or explicit continuation establish reset boundaries. Inspected tests cover FIFO access, exhaustion and renewed budgets. This coordinates participating SuperPlane activities on a PR; it is not a repository-wide lock against independent humans or tools. [[sources/superplanehq--superplane#pr-coordination]] [[sources/superplanehq--superplane#repair-budget]] [[sources/superplanehq--superplane#coordination-test]]

Observed PR heads are recorded as revisions. A changed head invalidates cached mergeability; even a force-push back to a previously known SHA can become current. Older activities are not automatically cancelled merely because the head changed. The merge endpoint requires a caller-provided expected SHA, compares it to mergeability evidence, checks allowed merge method and feature availability, and locks work order/PR to recheck active automation before invoking the provider. A provider head-conflict test asserts refusal. These are revision/coordination gates, not proof of semantic correctness. [[sources/superplanehq--superplane#pr-revision]] [[sources/superplanehq--superplane#merge]] [[sources/superplanehq--superplane#merge-tests]]

The provider merge call occurs inside a local database transaction. **Inference:** local rollback cannot undo a successful remote merge if later bookkeeping fails. That cross-system failure window requires reconciliation; no live fault-injection result is claimed. [[sources/superplanehq--superplane#merge]]

### 5. Give judgments typed outputs without promoting them into proof

Merge-confidence prompts ask an agent to inspect the actual PR diff and original task, then report named checks. The server owns standard names, score direction and thresholds, validates integer scores 1–5 and bounded nonempty summaries, and rejects disabled checks based on the enabled list passed to it. This reduces interpretation drift. It does **not** validate whether the review was correct or whether a “security” score represents tested security. The prompt's read-only language is not an OS sandbox guarantee. [[sources/superplanehq--superplane#confidence]]

Approval is a separate mechanism: configured requirements can name users, roles, groups or any authenticated user; the component checks matching authority and prevents one person from satisfying multiple requirement slots. A rejection immediately emits the rejected channel. An empty requirement list immediately completes as approved. Thus the presence of an Approval node does not alone prove a nonempty human gate, and the separate merge API must not be assumed to require this specific component. [[sources/superplanehq--superplane#approval]]

### 6. Runner success is a protocol, not a log line

Runner documentation describes single-use registration tokens, host/Docker execution modes, bounded sequential log chunks, completion after retained chunks are acknowledged, and a server completion acknowledgement before ephemeral exit. It explicitly distinguishes creating registration credentials from starting a machine. Controlled shutdown is bounded: the first signal requests cancellation/flush/completion; a second signal or the timeout exits immediately. This is a documented protocol, not proof that all logs always survive every failure. [[sources/superplanehq--superplane#runner-protocol]]

The implementation checks task/runner ownership and state, uses a consistent runner-before-task lock order, and persists a completion hash. Identical terminal completions are idempotent; conflicting results fail. The API checks connection identity, commits the task result before triggering downstream request processing, and retains a scheduled fallback. Request processing can outlive the runner connection. Task success here means no cancellation, nonzero exit or reported error—not an independently evaluated change. [[sources/superplanehq--superplane#runner-completion]]

Completion clears the stored encrypted task payload. Log lifecycle separately advances through active, archivable, archiving and archived states; the design keeps high-frequency append metadata at the active store, not a PostgreSQL update per chunk. A hash and acknowledgement protect a local completion record, not exactly-once external commands or total historical-log completeness. [[sources/superplanehq--superplane#runner-completion]] [[sources/superplanehq--superplane#log-lifecycle]]

### 7. Keep proposed work, structured output and execution authority distinct

Scheduled intake reads a proposal file and validates an object with nonempty title/description, or explicit `{}` for no proposal, before creating a task. Missing/invalid input fails this template instead of being parsed from the final chat text. The generic runner result reader is weaker: invalid/missing JSON yields no result rather than automatically failing the task. **Validation strength belongs to the actual producer/consumer path.** Scheduled intake documentation also states no cross-run deduplication and fixed timezone offsets that do not track daylight-saving changes. [[sources/superplanehq--superplane#scheduled-intake]] [[sources/superplanehq--superplane#result-file]]

Runner rollout documentation separates admission disablement from existing-work cleanup: running tasks retain reconnect/log/cancel/complete access, while new work is blocked and queued capacity released. At the API layer, mapped authorization rules combine organization permission, token scope, additional required actions, feature gates and license features. The authorizer returns without a permission check for unmapped routes; correctness therefore depends on routing/authentication registration outside this function. This is not a claim of an exploitable route or a completed tenant-isolation audit. [[sources/superplanehq--superplane#runner-admission]] [[sources/superplanehq--superplane#authorization]]

### 8. Make operating the system cheaper than decoding it

Component guidance asks nodes to show distinguishing targets, not every setting; outcome channels exist when downstream action genuinely differs; details explain how a state was reached and link to external evidence. Typed configuration distinguishes missing conditional fields from zero values, backend setup validates required data, and semantic renderers own field-specific feedback. These are contributor design prescriptions, not a claim that every integration complies. [[sources/superplanehq--superplane#operator-interface]] [[sources/superplanehq--superplane#component-contract]]

Contributor rules also encode deployment-boundary and transaction lessons: API configuration is not worker configuration; tests with injected credentials do not verify deployed secrets; database handles must propagate through model calls. The repo tracks legacy transaction-access debt and prohibits growing it. This is useful maintenance guidance, not proof that all legacy paths are gone. [[sources/superplanehq--superplane#contributor-checks]]

## Patterns demonstrated

- [[patterns/behavioral/latent-vs-deterministic-split]] — agent implementation/review wrapped by explicit graph steps, result validation and server-owned thresholds. [[sources/superplanehq--superplane#implementation-template]] [[sources/superplanehq--superplane#confidence]]
- [[patterns/behavioral/evidence-gated-completion]] — no-open-work finalization, acknowledged task results and exact-head merge admission; each is a different contract. [[sources/superplanehq--superplane#finalization]] [[sources/superplanehq--superplane#runner-completion]] [[sources/superplanehq--superplane#merge]]
- [[patterns/behavioral/context-is-not-authority]] — workflow inputs and agent judgments differ from identity, token scope, actor eligibility and admission state. [[sources/superplanehq--superplane#authorization]] [[sources/superplanehq--superplane#approval]]
- [[patterns/structural/authoritative-recheck-after-notification]] — notifications accelerate DB-backed processing; merge rechecks active automation and expected head. [[sources/superplanehq--superplane#event-routing]] [[sources/superplanehq--superplane#merge]]
- [[patterns/quality-bar/revision-bound-review]] — **narrow analogue only:** PR-head and mergeability binding, not evidence of the full delta-view/feedback-anchor pattern. Keep that pattern proposed. [[sources/superplanehq--superplane#pr-revision]] [[sources/superplanehq--superplane#merge]]
- [[patterns/quality-bar/complexity-ratchet]] — explicit transaction propagation and a no-new-debt maintenance rule. [[sources/superplanehq--superplane#contributor-checks]]

## What we'd steal

Portable mechanisms from the inspected scope; ★ marks priorities, not evidence strength. Adapt these when a concrete workflow needs them, not as a mandate to deploy a factory.

1. **★ Durable work identity above runs.** Keep task intent, artifacts and status across multiple automations; do not use one agent transcript as the whole business record. [[sources/superplanehq--superplane#work-order]]
2. **Explicit transitions plus outcome.** Validate lifecycle moves and close reasons separately; state names in a draft spec are not runtime truth. [[sources/superplanehq--superplane#work-order]]
3. **Transition-local history.** Write state and its explanatory event in one transaction; this does not require pretending every stored object is append-only. [[sources/superplanehq--superplane#work-order]]
4. **Invalidate stale status notes.** Clear the explanation of an old wait whenever the work changes state; operational UI is part of correctness. [[sources/superplanehq--superplane#work-order]]
5. **★ Keep judgment inside an explicit process.** Use agent steps for implementation/review and deterministic steps for publication, attachment and output checks. Prompt instructions alone do not constrain credential use. [[sources/superplanehq--superplane#implementation-template]]
6. **Find before creating external artifacts.** Reuse an open PR for the task branch; combine with provider idempotency/reconciliation for the remaining race window. [[sources/superplanehq--superplane#implementation-template]]
7. **Record before notifying.** Persist routing/queue state transactionally, then notify. Never equate this with atomic delivery across DB and broker. [[sources/superplanehq--superplane#event-routing]]
8. **Recover through state scans.** Use notifications for fast response and pending-state polling for catch-up; avoid a correctness dependency on one notification. [[sources/superplanehq--superplane#event-routing]]
9. **★ Partition concurrency by contested resource.** Use keys such as branch or PR to serialize conflicts without globally serializing independent work. [[sources/superplanehq--superplane#queue]]
10. **Bound scans without starving other keys.** Full queues must not consume every dispatch window; the regression fixture should exceed the window. [[sources/superplanehq--superplane#queue-test]]
11. **Let coordinating components own admission.** Merge/loop nodes waiting for further inputs cannot blindly inherit ordinary execution-slot gating. [[sources/superplanehq--superplane#queue]]
12. **Separate permanent configuration failure from retryable errors.** Record the former as a failed execution requiring correction, instead of endlessly retrying it. [[sources/superplanehq--superplane#queue]]
13. **★ Finalize only after tracked work drains.** Check executions, queued work and pending events together; a terminal-looking leaf is insufficient. [[sources/superplanehq--superplane#finalization]]
14. **Preserve lifecycle, result and reason.** A rejected approval, an engine error and a cancelled run need different follow-up behavior. [[sources/superplanehq--superplane#execution-state]] [[sources/superplanehq--superplane#operator-interface]]
15. **Stage edits before publishing.** Make activation explicit and reject stale staging; editor autosave is not authority to change live behavior. [[sources/superplanehq--superplane#staging]]
16. **★ Name the exact snapshot unit.** Copied node config and live graph edges coexist here. Specify what freezes before claiming reproducibility. [[sources/superplanehq--superplane#execution-state]] [[sources/superplanehq--superplane#event-routing]]
17. **★ Separate inspection from mutation ownership.** Permit concurrent analysis but queue participating writers on the same PR; the lock does not control external writers. [[sources/superplanehq--superplane#pr-coordination]]
18. **Reserve repair budgets at mutation admission.** Waiting for access should not spend an attempt; repeated admission of the same owner should not double-spend. [[sources/superplanehq--superplane#repair-budget]]
19. **Make repair exhaustion inspectable and resumable.** Persist a limit-reached state and an explicit budget reset boundary, instead of retrying indefinitely. [[sources/superplanehq--superplane#repair-budget]]
20. **★ Bind merging to the expected revision.** Recheck head identity and active automation at the action boundary; a green old observation is not current permission. [[sources/superplanehq--superplane#merge]]
21. **Invalidate derived caches when evidence changes.** Clear mergeability on a new head; retain old revision history without treating it as the new verdict. [[sources/superplanehq--superplane#pr-revision]]
22. **Own score semantics in code.** Keep names, direction, bands and allowed checks outside generated review text; validation does not establish calibration. [[sources/superplanehq--superplane#confidence]]
23. **Keep review dimensions distinct.** Blast radius, specification drift, performance, security and reversibility answer different questions; do not market the aggregate as proof. [[sources/superplanehq--superplane#confidence]]
24. **Represent approval requirements and actors.** Prevent one actor filling every slot and retain decision provenance; explicitly decide whether empty requirements should pass. [[sources/superplanehq--superplane#approval]]
25. **Use scoped bootstrap credentials.** Hand runners registration credentials rather than installation administrator tokens; registration and machine provisioning are different operations. [[sources/superplanehq--superplane#runner-protocol]]
26. **★ Hash completion payloads for idempotent acknowledgement.** Accept an identical terminal report and reject a conflicting one; this protects recording, not arbitrary tool effects. [[sources/superplanehq--superplane#runner-completion]]
27. **Commit completion before triggering downstream work.** Let follow-on processing outlive the connection and retain a scheduled fallback. [[sources/superplanehq--superplane#runner-completion]]
28. **Separate result, logs and retention lifecycles.** Acknowledged retained chunks, archived logs and successful work are not synonyms. Clear transient payloads when finished. [[sources/superplanehq--superplane#runner-protocol]] [[sources/superplanehq--superplane#log-lifecycle]] [[sources/superplanehq--superplane#runner-completion]]
29. **Move hot log metadata off the primary DB write path.** Keep append-frequency counters with the active store and low-frequency archive coordination in the database. [[sources/superplanehq--superplane#log-lifecycle]]
30. **Make shutdown bounds explicit.** Graceful flush/cancel/ack has a timeout and second-signal escape; do not promise perfect capture after forced exit. [[sources/superplanehq--superplane#runner-protocol]]
31. **Disable admission without disabling cleanup.** Existing tasks still need reconnect, logs, cancellation and completion after fleet disablement. [[sources/superplanehq--superplane#runner-admission]]
32. **Separate organization capacity from per-resource contention.** FIFO capacity admission and PR mutation ownership solve different bottlenecks. [[sources/superplanehq--superplane#runner-admission]] [[sources/superplanehq--superplane#pr-coordination]]
33. **★ Validate machine-consumed artifacts, not final prose.** Scheduled intake requires a structured proposal; generic JSON parsing alone does not impose that contract. [[sources/superplanehq--superplane#scheduled-intake]] [[sources/superplanehq--superplane#result-file]]
34. **Make no-op a legitimate result.** An explicit empty proposal avoids forcing low-value tasks. Add deduplication only when repeated proposals justify it; it is absent here. [[sources/superplanehq--superplane#scheduled-intake]]
35. **Share preview and execution semantics.** Schedule previews use the actual scheduler; document fixed-offset/DST behavior rather than implying wall-clock timezone fidelity. [[sources/superplanehq--superplane#scheduled-intake]]
36. **Intersect permissions at the real action boundary.** Organization role, token scope, additional actions, feature and license checks serve distinct purposes; audit rule coverage before claiming global enforcement. [[sources/superplanehq--superplane#authorization]]
37. **Preserve absent versus explicitly empty configuration.** Conditional field pointers distinguish missing from zero values; network-policy env overrides distinguish unset from an empty override. Do not interpret every empty value as a safe default. [[sources/superplanehq--superplane#component-contract]] [[sources/superplanehq--superplane#network-policy]]
38. **Make operational displays explain decisions.** Show the distinguishing target, outcome and evidence/timeline, with readable errors and useful external links instead of raw payload dumps. [[sources/superplanehq--superplane#operator-interface]]
39. **Turn integration experience into contributor contracts.** Keep semantic field validation, typed outputs and outcome-channel conventions reusable; preserve native API shapes when flattening would mislead users. [[sources/superplanehq--superplane#component-contract]] [[sources/superplanehq--superplane#operator-interface]]
40. **★ Verify deployment scope, not just code paths.** Trace required configuration through API, workers, runners and charts; injected test credentials do not establish live readiness. [[sources/superplanehq--superplane#contributor-checks]]
41. **Ratchet away transaction escape hatches.** Pass the database handle through the call chain and forbid new legacy accesses; do not require a speculative all-at-once rewrite. [[sources/superplanehq--superplane#contributor-checks]]
42. **Distinguish source license from feature entitlement.** An open-source core, EE directory and runtime-enabled modules need separate reuse/deployment accounting. [[sources/superplanehq--superplane#license]]

## Tensions and anti-patterns

- **“One-shot” is product framing, not an observed benchmark.** The design explicitly includes multiple agent/check/repair passes. No task corpus or matched baseline was evaluated here. [[sources/superplanehq--superplane#root]] [[sources/superplanehq--superplane#repair-budget]]
- **Model review versus executable evidence:** the review-score machinery is useful for prioritizing attention, but does not settle the earlier preference for empirical/formal checks. Compare [[concepts/review-cost-aware-workflows]]; measure whether these reviews catch consequential defects at acceptable cost before expanding them. [[sources/superplanehq--superplane#confidence]]
- **Versioned authoring versus frozen execution:** staging/version records coexist with live-edge routing. Historical replay requires more than the editor's commit history. [[sources/superplanehq--superplane#staging]] [[sources/superplanehq--superplane#event-routing]]
- **Successful local transaction versus external effect:** broker publishing and provider mutation are separate systems; do not infer global exactly-once from row locks, completion hashes or a transaction around an HTTP call. [[sources/superplanehq--superplane#event-routing]] [[sources/superplanehq--superplane#merge]]
- **Approval component versus approval guarantee:** no requirements passes immediately; generic user/role hooks and exact-head merging are different boundaries. [[sources/superplanehq--superplane#approval]] [[sources/superplanehq--superplane#merge]]
- **Policy versus sandbox:** instructions not to modify a review checkout or not to create a PR are prompt policy. Host/Docker runner modes and integration credentials require separate deployment-level threat analysis. [[sources/superplanehq--superplane#confidence]] [[sources/superplanehq--superplane#implementation-template]] [[sources/superplanehq--superplane#runner-protocol]]
- **Scope limits:** the source mixes implementation, product drafts and contributor prescriptions; no evidence here establishes all integrations conform, all routes are protected, or Enterprise deployment is permitted under the core license. [[sources/superplanehq--superplane#factory-draft]] [[sources/superplanehq--superplane#authorization]] [[sources/superplanehq--superplane#license]]

## Open questions and verification record

- Fault-inject a remote merge that succeeds before local commit failure: which reconciliation path restores the Work Order without repeating unwanted effects?
- Edit graph edges during an in-flight run: characterize actual behavior and decide whether future runs should pin the graph or deliberately follow live policy.
- Compare task success, human review time, defect escape rate, repair attempts and cost with/without model-scored review on a representative corpus. Score validity is not calibration.
- Audit supported deployment modes for authentication-rule coverage, host/container isolation, network policy enforcement and credential revocation. This source pass does not certify them.
- **Preservation and validation:** complete pinned tracked tree local-only; immutable source links and hashes in [[sources/superplanehq--superplane]]. Source application tests not run. Research link/range/hash checks and wiki-doctor delta are the ingestion checks, not product runtime verification.

## Agent Habitat comparison — 2026-11-06

[[concepts/agent-habitat-architecture]] provides a proposed action-authorization comparison: approval should bind the actual operation, target and destination, and recovery must retain consumed approvals. This does not upgrade existing SuperPlane guarantees or claim Habitat compliance. [[sources/replit--agent-habitat-architecture#approval]] [[sources/replit--agent-habitat-architecture#durability]]
