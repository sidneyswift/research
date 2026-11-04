---
domain: artifacts
subdomain: projects
type: project
name: ftrack-api
creator: "[[creators/ftrack]]"
source: "[[sources/ftrack--business-api-design]]"
ecosystem: production-tracking
status: documentation-investigated
last-reviewed: 2026-11-04
---

# ftrack API

> A production-tracking API with a single batched HTTP endpoint, a query language, a client unit of work, event subscriptions, and user-visible jobs. Its semantic boundaries live in operations and session behavior rather than one REST route per capability.

## Attributes

- **Unit studied:** ftrack HTTP endpoint/authentication/query contracts plus Python sessions, entities, events and Job examples. Seven official documentation pages captured 2026-11-04; server and SDK release revisions were not pinned. [[sources/ftrack--business-api-design#root]]
- **Evidence class:** documentation inspected; no credentials, SDK installation, provider execution, or fault injection.
- **Credibility:** official Developer Hub; no adoption count measured. [[sources/ftrack--business-api-design#root]]

## Relationships

- [[creators/ftrack]] — publisher.
- [[projects/designing-apis-for-agents/README]] — research group.
- [[concepts/business-platform-api-design]] — counterexample to categorizing responsibilities by route count or HTTP verb alone.
- [[concepts/code-mode-capability-interface]] — a comparison point for programmatic composition and schema discovery, not evidence they share an implementation.

## Mechanism and themes

### One transport endpoint, several semantic responsibilities

The API accepts a JSON list of operations at `POST https://FTRACK-WORKSPACE-URL/api`; results correspond to input indices. Operational errors use an `exception`/`content` object, while authentication or exceptional errors use HTTP error status and an `FTRACK_ERROR` header. The documentation states that operations in one request share a server transaction and all roll back if one fails. That scope is the server-side batch; it does not establish rollback of files, external applications, or event-triggered side effects. [[sources/ftrack--business-api-design#endpoint]]

This is a useful counterexample to a simplistic “GET means query, POST means workflow” catalog. An adapter needs the payload's operation kind, entity type and desired effects to classify a call. That is our implication of the documented transport model. [[sources/ftrack--business-api-design#endpoint]]

### Explicit query shape controls data volume

The query DSL selects one target entity type, supports projected fields and related-entity attributes, and includes filtering, ordering, offset and limit. A query can retrieve related data in one request without returning unrelated top-level entity types. For an agent, a projection is an explicit data budget and can reduce accidental repeated field fetches; this performance implication follows the docs but was not benchmarked here. [[sources/ftrack--business-api-design#query]]

### A local mutation is not a committed business change

The Python session records operations locally until `Session.commit()`. Commit can compress a create followed by local updates while preserving logical ordering. Queries are issued on demand against server state: a not-yet-committed local create need not appear in a query. Returned entities can merge into the session cache while preserving local modifications. Thus a queried entity object is not necessarily an untouched fresh server snapshot. [[sources/ftrack--business-api-design#sessions]]

Accessing an unloaded attribute may issue another query automatically; later accesses use the cache. Sessions download server schema and construct entity classes because different servers can expose different entity configurations. Entity keys are discoverable through typed dict-like objects. The agent-facing implication is to distinguish unloaded, cached, locally modified and committed values rather than flattening them into “the data.” [[sources/ftrack--business-api-design#sessions]], [[sources/ftrack--business-api-design#entities]]

### Events provide integration signals, not a workflow durability guarantee

Each session can subscribe to filtered event topics, publish events, receive replies, and target registered subscriber information. Events are received and queued in a background thread, while a dedicated processor can call `event_hub.wait()`. Importantly, `publish(..., synchronous=True)` invokes only local handlers and collects their results. It does not synchronously run remote subscribers. The captured guide does not establish durable replay, exactly-once delivery, or recovery after a processor crash. [[sources/ftrack--business-api-design#events]]

The context→authority→enforcement→recovery distinction is concrete: an event delivers context and routes a handler; the handler's API connection supplies authority; keys/roles/project access govern provider operations; durable effect recovery remains a separate integration responsibility unless another inspected contract supplies it. The first three elements follow the event/auth docs; the missing recovery guarantee is an evidence boundary, not a claim that ftrack has no such feature. [[sources/ftrack--business-api-design#events]], [[sources/ftrack--business-api-design#authentication]]

### A Job is a status/result surface

The Job example creates a user-associated job with `status: running`, later sets `status: done` and commits. Job components attach files whose download URLs can be retrieved. The guide presents this as feedback for long-running API tasks; it does not show the Job resource itself scheduling, checkpointing, or restarting execution. A status record and a durable worker are different capabilities. The guide also notes limited web UI support for multiple attachments. [[sources/ftrack--business-api-design#jobs]]

### Identity and scope are explicit but vendor-specific

Personal keys inherit the named user's permissions. Global keys still include a username, but permissions come from the key's assigned role; global keys need explicit access to private projects. A global-key username therefore must not be assumed to be the complete permission boundary. [[sources/ftrack--business-api-design#authentication]]

## Patterns demonstrated

- [[patterns/behavioral/context-is-not-authority]] — event source/target information routes context; actual resource access is governed by key/user/role/project rules. Documentation-level correspondence only. [[sources/ftrack--business-api-design#events]], [[sources/ftrack--business-api-design#authentication]]
- Candidate: staged local unit of work plus explicit commit. Captured as a mechanism here; no new confirmed pattern or independent implementation count asserted. [[sources/ftrack--business-api-design#sessions]]

## What we'd steal

- ★ **Separate transport from semantic capability.** Classify batched operations by effect and domain, not simply `POST /api`; useful for policy, audit and agent selection. Limit: the inspected docs do not define an agent adapter. [[sources/ftrack--business-api-design#endpoint]]
- ★ **Expose a previewable unit of work and explicit commit boundary.** Let a caller inspect staged operations before publication; adapt for bulk business edits. Limit: a local staging layer is not human approval or external-effect rollback. [[sources/ftrack--business-api-design#sessions]]
- ★ **Make selected fields and relationships explicit.** Use projections to control result size and avoid repeated hidden fetches; verify actual latency separately. [[sources/ftrack--business-api-design#query]], [[sources/ftrack--business-api-design#sessions]]
- **Discover tenant/server schema rather than hard-code every field.** Useful for customizable operations systems. Schema discovery does not establish permission to use every field. [[sources/ftrack--business-api-design#sessions]], [[sources/ftrack--business-api-design#entities]]
- **Preserve cache and mutation provenance.** Label values as unloaded/cached/local/committed in any agent adapter that would otherwise hide those distinctions. This is our adaptation of the documented session behavior. [[sources/ftrack--business-api-design#sessions]]
- **Keep transactional scope narrow and explicit.** Batch transaction rollback is valuable, but separately account for storage/provider effects outside it. [[sources/ftrack--business-api-design#endpoint]]
- **Use namespaced event topics, filtered subscriptions and explicit targets.** Useful for routing integration work, with separate persistence and authorization. [[sources/ftrack--business-api-design#events]]
- **Distinguish local synchronous dispatch from remote event processing.** Avoid promising remote completion from a synchronous local publish call. [[sources/ftrack--business-api-design#events]]
- **Attach outputs to a durable job identity.** Keep status and downloadable results discoverable independently of the process; supply separate execution recovery where needed. [[sources/ftrack--business-api-design#jobs]]
- **Preserve credential-role and project-access distinctions.** Audit key identity and user attribution together. [[sources/ftrack--business-api-design#authentication]]

## Tensions and anti-patterns

- A single generic endpoint is composable but needs semantic metadata for permission policy and agent discovery. HTTP routing alone does not explain its effects. [[sources/ftrack--business-api-design#endpoint]]
- Automatic population and cache merging simplify scripts while making network cost and freshness less obvious. [[sources/ftrack--business-api-design#sessions]]
- `Job.status = done` is an assertion by a client, not independent verification of the task's external outcome. The docs show the update, not a verifier. [[sources/ftrack--business-api-design#jobs]]
- Endpoint docs specify naive server-time-zone datetime values. An agent adapter should handle the timezone contract explicitly instead of importing a universal UTC assumption. [[sources/ftrack--business-api-design#endpoint]]

## Open questions and verification record

- No runtime calls or source implementation inspected. Seven snapshots and source anchors are available; links/hashes were checked by the research pass.
- Unverified: request-id/idempotency support, event durability/replay/order, Job cancellation/retry ownership, and server-version compatibility guarantees outside the captured guides.
- Which operations need business-specific approval beyond generic entity mutation? Which read projections minimize round trips for real production tasks?
