---
domain: artifacts
subdomain: projects
type: project
name: anthropic-agent-api
creator: "[[creators/anthropic]]"
source: "[[sources/anthropic--agent-api-design]]"
ecosystem: Claude API
status: documentation-investigated
last-reviewed: 2026-11-04
---

# Anthropic agent API

> One provider exposes three different work contracts: stateless model Messages with a tool protocol, asynchronous Message Batches, and a separate stateful Managed Agents harness.

## Attributes

- **Unit studied:** Claude first-party API design as documented on 2026-11-04, not all Anthropic products. Thirteen official documentation pages were captured with hashes. [[sources/anthropic--agent-api-design#root]]
- **Version:** Living docs; Messages reference displayed API version `2026-10-21`. Managed Agents carries the beta header `managed-agents-2026-04-01`. [[sources/anthropic--agent-api-design#versions]], [[sources/anthropic--agent-api-design#managed-runtime]]
- **Interfaces inspected:** Messages, user-defined tool schemas/results, strict inputs, SSE, asynchronous batches, errors/versions, and Managed Agents session/permission concepts. [[sources/anthropic--agent-api-design#overview]]
- **Evidence class:** Documentation and examples inspected. No API requests, runtime tests, or agent task evaluations executed. Product claims about secure execution, performance, or reliable schema generation remain documented claims.
- **Credibility signal:** Official reference and lifecycle examples, as-of 2026-11-04; no adoption count measured. [[sources/anthropic--agent-api-design#root]]

## Relationships

- [[creators/anthropic]] — publisher/provider.
- [[projects/designing-apis-for-agents/README]] — ongoing comparison group.
- [[concepts/business-platform-api-design]] — business intent versus transport duration.
- [[concepts/agent-control-plane]], [[concepts/durable-agent-execution]] — separate durable work state from model invocations and viewing connections.
- [[concepts/code-mode-capability-interface]] — naming/discovery/composition are a distinct interface concern.

## Mechanism and themes

### The lifecycle level is explicit

| Surface | Documented operation shape | Who owns the loop/state? | Completion boundary |
| --- | --- | --- | --- |
| Messages | `POST /v1/messages` with message history, optional tools and streaming | Application supplies stateless multi-turn inputs and executes client tools | A model turn/stop reason; not automatically business-task completion |
| Message Batches | `POST /v1/messages/batches`, then retrieve/poll/results/cancel | Provider schedules independent message requests | Batch ended plus per-request outcome; not a transactional business workflow |
| Managed Agents (beta) | Separate agent, environment, session, and events resources | Managed harness executes tools and persists session events/state | Session status and workflow outcome are different; `idle` can coexist with an open workflow run |

This table is a synthesis of documented contracts, not runtime validation. In particular, “frontier API” does not mean every request is a durable autonomous job. [[sources/anthropic--agent-api-design#messages]], [[sources/anthropic--agent-api-design#batches]], [[sources/anthropic--agent-api-design#managed-runtime]], [[sources/anthropic--agent-api-design#managed-session-operations]]

### Tool use is a typed handoff, with a separate effect boundary

User-defined client tools have a name, a strongly recommended description, and an `input_schema`. A model response can contain `tool_use` blocks with an ID, name, and input. The application runs the corresponding tool and sends `tool_result` with the matching `tool_use_id`, then continues the conversation. Server tools have provider-managed execution behavior. The schema identifies the call; it does not grant access to a business system. [[sources/anthropic--agent-api-design#messages]], [[sources/anthropic--agent-api-design#tool-lifecycle]]

The result protocol specifies ordering, `is_error`, and supported content. The docs explicitly treat externally sourced tool results as untrusted content and say to keep them inside result blocks. This is more than route naming: provenance is part of the interaction contract. [[sources/anthropic--agent-api-design#tool-lifecycle]]

`strict: true` is documented as constraining sampling to schema-valid tool arguments. **Our boundary:** type conformance does not establish a valid supplier, sufficient account balance, current approval, permission to act, or successful provider effect. Those still need business/runtime enforcement. [[sources/anthropic--agent-api-design#strict-tools]], [[sources/anthropic--agent-api-design#managed-permissions]]

### Tool discoverability can favor a different granularity than domain endpoints

Anthropic's tool-definition guidance recommends detailed behavioral descriptions, service-prefixed names, high-signal outputs, and consolidating related actions into fewer tools with an `action` parameter. Its example groups creating, reviewing, and merging pull requests. That is a concrete counterexample to a universal “one tool per action” rule. [[sources/anthropic--agent-api-design#tool-definitions]]

**Our interpretation:** a tool-selection surface may group several domain operations without merging their permissions, invariants, or implementation. A consolidated tool must still make its action/effects explicit. This guidance should not be generalized into a single untyped executor for every business operation; the captured doc does not establish an optimum tool count for a large ERP. [[sources/anthropic--agent-api-design#tool-definitions]], [[sources/anthropic--agent-api-design#managed-permissions]]

### Batches give inspectable asynchronous results, not universal exactly-once work

Batches process requests independently. The docs distinguish `succeeded`, `errored`, `canceled`, and `expired` outcomes; results can arrive in any order and must be matched by `custom_id`. Processing expiry is 24 hours; downloadable results are retained for 29 days after creation. These are dated service contracts, not a recommended universal retention duration. [[sources/anthropic--agent-api-design#batches]]

Cancellation races with already-running requests. The batch lifecycle and result envelope prevent an agent from treating “request accepted” or “batch ended” as “all items succeeded.” They do not establish that downstream business effects were applied once, were rolled back, or can be retried safely. [[sources/anthropic--agent-api-design#batches]], [[sources/aws--idempotent-apis#retries]]

### Streaming has its own error and evolution contract

SSE has message/content-block start, delta, stop, and error events. Tool-input deltas can be partial JSON; consumers accumulate them before parsing the final object or use SDK helpers. A `200` HTTP response can precede a stream error. New event types may appear, so clients must handle unknown variants gracefully. A live stream is an observation channel, not a durable external-effect ledger. [[sources/anthropic--agent-api-design#streaming]], [[sources/anthropic--agent-api-design#errors]]

The version header preserves existing input/output parameters within a version while permitting optional additions, output enum variants, and error-condition changes. Thus pinned version does not mean closed-world output parsing. The version history also lists explicit breaking changes in a newer date-version. [[sources/anthropic--agent-api-design#versions]]

### Managed execution separates definition, instance, context, and authority

Managed Agents distinguishes reusable agent configuration, environment, running session, and events. A session can be created idle and started with an event, or created with `initial_events`; the latter is documented as validating and persisting all events before returning, with all-or-nothing rejection if any initial event is invalid. A pinned agent version separates rollout from session creation; session overrides do not mutate the reusable agent. [[sources/anthropic--agent-api-design#managed-runtime]], [[sources/anthropic--agent-api-design#managed-session-create]]

The docs make an unusually useful completion distinction: a completed turn goes `idle`, and a workflow run can remain open while the session is idle. `terminated` is not the normal successful-task signal. Session deletion also leaves independent agents, environments, vaults, skills, memory stores, and separately uploaded files alone, while session-produced files are scoped to the deleted session. [[sources/anthropic--agent-api-design#managed-session-operations]]

Permission policies govern server-executed agent/MCP tools, while application-executed custom tools remain the application's responsibility. Policies include automatic allow, ask, and per-call server evaluation. The docs explicitly say `auto` is not a human checkpoint, distinguish user-message intent from tool-result content, and warn that forwarding untrusted end-user content as `user.message` can authorize more than intended. Evaluation metadata records allow/ask/deny. These are documented policy boundaries, not an independently verified security guarantee. [[sources/anthropic--agent-api-design#managed-permissions]]

## Patterns demonstrated

- [[patterns/behavioral/context-is-not-authority]] — the tool-result/user-intent distinction and application-owned custom-tool checks make provenance and effect authorization separate responsibilities. Documentation example; no additional implementation example count claimed. [[sources/anthropic--agent-api-design#tool-lifecycle]], [[sources/anthropic--agent-api-design#managed-permissions]]
- [[patterns/behavioral/evidence-gated-completion]] — the session-state/run-outcome distinction motivates checking the specific completion contract instead of an idle runtime indicator. The API documents the distinction; we did not execute an outcome checker. [[sources/anthropic--agent-api-design#managed-session-operations]]
- Candidate: **agent interaction protocol layered over stable capability contracts** — schemas, correlated tool results, result provenance, and continuation sit above ordinary effects. This single provider study does not establish a new confirmed cross-artifact pattern.

## What we'd steal

- ★ Name the lifecycle level: model turn, independent batch, persistent session, workflow run, and business completion are distinct. [[sources/anthropic--agent-api-design#messages]], [[sources/anthropic--agent-api-design#batches]], [[sources/anthropic--agent-api-design#managed-session-operations]]
- ★ Separate reusable definitions, execution instances, environments, and events; pin definition versions for reproducibility and rollout. [[sources/anthropic--agent-api-design#managed-runtime]], [[sources/anthropic--agent-api-design#managed-session-create]]
- ★ Make create-with-initial-work atomic at the documented input-persistence boundary; do not equate it with atomic external business effects. [[sources/anthropic--agent-api-design#managed-session-create]]
- ★ Keep tool provenance and execution authority explicit; custom-tool checks stay with the application. [[sources/anthropic--agent-api-design#managed-permissions]]
- Give tools meaningful service-prefixed names and descriptions covering when to use them, parameters, exclusions, and results. [[sources/anthropic--agent-api-design#tool-definitions]]
- Consider grouping related actions in an agent-facing tool, while preserving each action's authorization and invariants underneath. Evaluate the grouping rather than adopting it as a blanket rule. [[sources/anthropic--agent-api-design#tool-definitions]]
- Offer schema-constrained arguments, but still enforce semantic preconditions and permissions. [[sources/anthropic--agent-api-design#strict-tools]]
- Correlate every tool result to its exact call ID; encode execution errors distinctly from a successful content string. [[sources/anthropic--agent-api-design#tool-lifecycle]]
- Preserve untrusted outputs as typed result content. [[sources/anthropic--agent-api-design#tool-lifecycle]]
- Return stable useful identifiers and only the fields needed for the agent's next decision. [[sources/anthropic--agent-api-design#tool-definitions]]
- Design asynchronous result sets for correlation independent of order, mixed outcomes, expiry, and retention. [[sources/anthropic--agent-api-design#batches]]
- Treat cancellation as an in-progress request with partial results, not proof of rollback. [[sources/anthropic--agent-api-design#batches]]
- Expose request IDs in headers and errors, and surface them through SDKs. [[sources/anthropic--agent-api-design#errors]]
- Treat HTTP response establishment and streamed operation success as different stages. [[sources/anthropic--agent-api-design#streaming]]
- Require additive event/enum tolerance, even with version pinning. [[sources/anthropic--agent-api-design#versions]]
- Document dependent versus independent resource deletion and output retention. [[sources/anthropic--agent-api-design#managed-session-operations]]
- Separate automatic policy evaluation from required human approval; expose evaluation outcomes for audit. [[sources/anthropic--agent-api-design#managed-permissions]]

## Tensions and anti-patterns

- **Typed is not correct:** strict arguments do not prove the desired business operation, current permissions, or correct real-world outcome. [[sources/anthropic--agent-api-design#strict-tools]], [[sources/anthropic--agent-api-design#managed-permissions]]
- **Guidance is contextual:** consolidated action tools can reduce selection ambiguity but concentrate complexity and must retain action-specific controls. No comparative task benchmark was inspected. [[sources/anthropic--agent-api-design#tool-definitions]]
- **Model versus runtime:** stateless Messages and managed sessions support different ownership/control choices; their guarantees should not be silently interchanged. [[sources/anthropic--agent-api-design#managed-runtime]]
- **State costs:** Managed Agents is documented as stateful and not ZDR/HIPAA eligible in this capture. Suitability and eligibility can change; confirm current docs before adoption. [[sources/anthropic--agent-api-design#managed-runtime]]
- **Evolving surface:** beta-managed execution and additive event variants demand compatibility handling beyond a fixed schema. [[sources/anthropic--agent-api-design#versions]], [[sources/anthropic--agent-api-design#managed-runtime]]

## Open questions and verification record

- No failure-injection tests or business tasks were run. Does the documented lifecycle remain intelligible during connection loss, permission updates, and external provider timeouts?
- What idempotency/reconciliation guarantees exist for session-start retries and custom-tool side effects? This bounded documentation set does not settle them.
- When does a consolidated action tool improve agent selection versus separate named tools on the target business task corpus?
- What is the precise interaction between runtime permission policies, provider credentials, and tenant-level business authorization in a deployed integration?
- Source hashes and all registered anchors were validated locally; whole-wiki registration and index propagation are handled by the coordinating ingest. No confirmed new pattern was promoted.
