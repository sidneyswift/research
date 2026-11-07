---
domain: concepts
type: concept
name: business-platform-api-design
creators:
  - "[[creators/google]]"
  - "[[creators/microsoft]]"
  - "[[creators/aws]]"
  - "[[creators/ietf]]"
sources:
  - "[[sources/google--aip-121]]"
  - "[[sources/google--aip-136]]"
  - "[[sources/google--aip-151]]"
  - "[[sources/microsoft--async-request-reply]]"
  - "[[sources/microsoft--cqrs]]"
  - "[[sources/microsoft--domain-analysis]]"
  - "[[sources/microsoft--web-api-design]]"
  - "[[sources/aws--idempotent-apis]]"
  - "[[sources/ietf--http-semantics]]"
status: active
last-reviewed: 2026-11-04
---

# Business platform API design

> **One-line:** Model stable business capabilities, distinguish reading state from requesting effects, and make long-running work observable through a durable operation contract.

## What it is

An API is a promise about intent, effects, results, and failure. HTTP routes are one expression of that promise; queues and workers implement it. Distinguish **business resources**, **commands**, **workflow runs**, and **operation status**. Whether processing finishes inside the HTTP request is a separate axis from whether it changes business state. This is our synthesis of resource-oriented design, command/query separation, and asynchronous request-reply guidance. [[sources/google--aip-121#resources]], [[sources/microsoft--cqrs#separation]], [[sources/microsoft--async-request-reply#lifecycle]]

## Where it came from

These ideas predate this review. Google AIPs specify a resource-oriented API style with custom methods and long-running operations; Microsoft documents CQRS, business domain boundaries, and asynchronous request-reply; AWS explains retry-safe contracts; RFC 9110 defines HTTP semantics. This page combines their guidance without claiming that their conventions form a single universal standard. [[sources/google--aip-121#root]], [[sources/google--aip-136#root]], [[sources/google--aip-151#root]], [[sources/microsoft--domain-analysis#root]], [[sources/aws--idempotent-apis#root]], [[sources/ietf--http-semantics#root]]

## Why it matters

Business users, agents, scheduled jobs, integrations, and interfaces can reuse the same capabilities without inheriting a particular UI's sequence of steps. A caller can inspect a result without accidentally refreshing a provider, triggering a workflow, or taking a business action. Durable run IDs also make retries and handoffs intelligible. These are design benefits inferred from the source contracts, not measured performance claims for a particular platform. [[sources/microsoft--domain-analysis#boundaries]], [[sources/microsoft--async-request-reply#lifecycle]], [[sources/aws--idempotent-apis#retries]]

## Evidence & claims

### Two independent axes

| Intent | Short, bounded execution | Long-running or externally dependent execution |
| --- | --- | --- |
| Retrieve or compute information | `GET /invoices/{id}`; safe calculation/search where appropriate | Explicit export/report request, then status and result retrieval |
| Request a business effect | `POST /invoices/{id}:approve`, returning the updated representation | `POST /payment-runs`, returning a durable run/operation reference |

The routes are proposed examples. A computation need not change business records, yet creating a durable report or consuming substantial resources can deserve an explicit POST request. Conversely, a command may complete immediately. A read-only POST search is possible when query input exceeds URL limits. Method alone therefore cannot fully classify side effects. [[sources/google--aip-136#actions]], [[sources/google--aip-151#operations]]

HTTP GET is safe in the sense that the caller does not request a state change. Logging and cache management are compatible with that; approving an invoice, starting a provider sync, or initiating a payment are different contracts. Do not turn a cache miss into an undisclosed business workflow. [[sources/ietf--http-semantics#safe-methods]]

### Does this need two endpoints?

Usually separate **read current state** from **request new work**. Often long-running work needs three capabilities:

1. Initiate: `POST /supplier-syncs`.
2. Observe execution: `GET /operations/{operationId}`.
3. Read business results: `GET /suppliers/{supplierId}` or `GET /supplier-syncs/{syncId}/results`.

A named run resource can also be the status resource, so this is not a mandatory count of three routes. For a simple synchronous update, the command response can return its result directly. Returning data after a command is normal; command/query separation concerns responsibility, not a ban on response bodies. [[sources/google--aip-121#resources]], [[sources/google--aip-136#actions]], [[sources/microsoft--async-request-reply#lifecycle]]

An endpoint that reads inputs, executes a known business action, and returns its outcome is coherent. An endpoint called `GET /supplier` that sometimes starts onboarding is not. Proposed distinction: internal implementation may combine reads and writes; external intent must remain explicit. [[sources/ietf--http-semantics#safe-methods]], [[sources/microsoft--cqrs#separation]]

### Naming and categorization

Start with business language, ownership, and invariants. Group the catalog by domains such as procurement, inventory, billing, identity, and reporting, then tag operations as query, command, workflow, or event. Tag execution as immediate/long-running separately. This catalog taxonomy is our recommendation, grounded in business-capability boundaries rather than a requirement of HTTP. [[sources/microsoft--domain-analysis#boundaries]]

| Capability | Proposed name | What it promises |
| --- | --- | --- |
| Read a business resource | `GET /purchase-orders/{id}` | Return an order representation |
| List/filter | `GET /purchase-orders?status=approved` | Bounded, paginated results |
| Create a draft | `POST /purchase-orders` | Create a business record |
| Ordinary editable fields | `PATCH /purchase-orders/{id}` | Apply allowed field changes |
| Enforce an action | `POST /purchase-orders/{id}:approve` | Check approval rules and transition state |
| Durable business process | `POST /supplier-onboardings` | Create a trackable onboarding run |
| Observe runtime | `GET /operations/{id}` | Execution state and outcome references |
| Publish a fact | `purchase-order.approved` | A past event, not a request to approve |

Use plural nouns for collections, consistent identifiers and field conventions, and explicit domain verbs where CRUD obscures intent. Google's colon action syntax is one valid house style; an action subresource is another. Choose one consistently. Do not force `approve` into an unrestricted status PATCH just to avoid a verb. Do not name contracts after `worker`, `queue`, or `executeTask` unless managing runtime infrastructure is the actual product. [[sources/google--aip-121#resources]], [[sources/google--aip-136#actions]], [[sources/microsoft--web-api-design#contracts]]

### Long-running lifecycle: a proposed HTTP contract

```http
POST /supplier-syncs
Idempotency-Key: one-key-for-this-user-intent
Content-Type: application/json

{"supplierId":"sup_123","scope":"catalog"}
```

```http
HTTP/1.1 202 Accepted
Location: /operations/op_123
Retry-After: 3
Content-Type: application/json

{"id":"op_123","status":"queued","resourceUrl":"/supplier-syncs/sync_123"}
```

```http
GET /operations/op_123

HTTP/1.1 200 OK
Content-Type: application/json

{"id":"op_123","status":"succeeded","resultUrl":"/supplier-syncs/sync_123/results"}
```

These are illustrative schemas, following Microsoft's HTTP pattern. `202` means accepted, not completed. `201 Created` can instead be appropriate when the promised action is creation of a run resource; distinguish that creation from completion of its work. Google's Operation schema is a separate convention, not a requirement that all HTTP APIs return this exact status/body. [[sources/microsoft--async-request-reply#lifecycle]], [[sources/ietf--http-semantics#accepted]], [[sources/google--aip-151#operations]]

Keep operation status distinct from business status: `operation=succeeded` might mean a draft was produced, while the invoice remains `awaiting_approval`. Specify terminal states, progress semantics, result/error schema, retention/expiry, and whether cancellation is supported. Cancellation request acceptance is not proof that external effects were reversed. Partial completion needs per-item outcomes or a reconciliation path. [[sources/microsoft--async-request-reply#lifecycle]], [[sources/google--aip-151#operations]]

### Implementation underneath the contract

```text
API: authenticate → authorize → validate → record request + durable dispatch
                                                  ↓
                                       queue / workflow engine
                                                  ↓
                                     worker → domain capabilities
                                                  ↓
                                operation state + business results

Reads → authorized query service → business data / read projections
```

Our recommended implementation is a thin transport layer calling domain/application services. Share capabilities there; do not require a worker in the same application to loop through its own HTTP endpoints. Across real service boundaries, use the owning service's supported API or messages. API modularity, code modularity, and separate deployment are different decisions. Domain ownership should determine who may write business data. [[sources/microsoft--domain-analysis#boundaries]], [[sources/google--aip-121#resources]]

Avoid the acceptance gap: saving a run and publishing a queue message as unrelated writes can lose work. Use a transactional outbox, a database-backed durable queue, or an engine with a documented durable-start guarantee. A dispatcher may deliver more than once, so consumers still need idempotency. Microsoft's CQRS guidance explicitly discusses atomic outbox persistence and duplicate-safe consumption. [[sources/microsoft--cqrs#separation]]

For command retries, scope a caller's idempotency key to the tenant/caller and operation; atomically bind it to the request intent and its result/run. The same key with different parameters must fail rather than silently reuse another request. Return the existing run for duplicates; retain deduplication state for the documented replay window. Worker step retries and provider effects need their own idempotency/reconciliation: a deduplicated HTTP request alone does not prevent a duplicated external action after a worker crash. A provider timeout can mean an unknown outcome. [[sources/aws--idempotent-apis#retries]], [[sources/microsoft--async-request-reply#lifecycle]]

### Unknown future uses: preserve options at the right seams

**Our architectural judgment:** begin with cohesive domain modules and a modest set of capability contracts. A modular monolith plus durable workers is a reasonable starting implementation when independent scaling, ownership, or isolation has not yet justified separate services. The sources establish business boundaries and separation options, not a mandate for this deployment shape. [[sources/microsoft--domain-analysis#boundaries]], [[sources/microsoft--cqrs#separation]]

Expose an additional independently callable capability when at least one is real: it is independently useful to a consumer; has distinct permissions or business rules; has its own lifecycle/result; or requires independent scaling/ownership. Keep steps private when splitting them lets callers bypass invariants or leaves every consumer rebuilding the same mandatory sequence. Do not publish every helper function for hypothetical reuse. Do not duplicate rules in a workflow endpoint and a smaller endpoint; both call the owning capability. [[sources/microsoft--domain-analysis#boundaries]], [[sources/google--aip-121#resources]], [[sources/microsoft--cqrs#separation]]

Concrete proposed example: supplier onboarding can compose supplier creation, document collection, review, and activation. Invoice ingestion may reuse supplier lookup without triggering onboarding. Approval should be callable only if it is a coherent business action with authorization and state preconditions, not merely because it is a worker step. A single generic `POST /execute` with flags for all these actions sacrifices discoverability and permission clarity. [[sources/microsoft--domain-analysis#boundaries]], [[sources/microsoft--cqrs#separation]]

### Platform conventions and the easy-to-miss contracts

Adopt one API style guide, schema-based API specification such as OpenAPI, standard errors, bounded lists with stable ordering/pagination, filter conventions, compatibility rules, and a documented migration path. Contract review should cover authorization, business invariants, retries, concurrency, and failure before route implementation. An additive field is not automatically harmless if strict consumers reject unknown fields; widening enums can break exhaustive clients. [[sources/microsoft--web-api-design#contracts]]

Use HTTP conditional requests such as `If-Match` where appropriate to prevent overwriting newer state. A prior GET or validation pass does not reserve the world; enforce business preconditions again at the actual state transition. [[sources/ietf--http-semantics#concurrency]], [[sources/microsoft--cqrs#separation]]

For each operation, explicitly record these review questions (our checklist synthesized from the sources, not a universal standard):

- **Identity and access:** Who owns the resource? Who may read, run, approve, cancel, and retrieve results? Carry tenant context into workers and enforce it on status/result endpoints too.
- **Freshness:** Is this authoritative state, a projection, cached provider data, or a newly computed snapshot? How does a caller request refresh and know when it is visible?
- **Input timing:** Does a run use an immutable input revision or the latest data when it starts? What happens if approvals or permissions change while queued?
- **Failure:** Which errors are immediate versus asynchronous? Can a step partially succeed? What resolves an unknown external outcome?
- **Limits and cost:** What are batch sizes, timeouts, polling guidance, quotas, retention, and cancellation limits? Who may initiate expensive work?
- **Traceability:** Can support connect actor, request ID, operation ID, input version, worker attempts, provider effects, and result without exposing secrets?
- **Evolution:** Who consumes it, who owns it, what is stable, and what is the deprecation process?

The lifecycle/freshness concerns follow from asynchronous/CQRS contracts; request intent and traceability follow from AWS's retry model; preconditions follow from HTTP and command validation. Tenant propagation and permission rechecks also connect to the wiki's existing [[concepts/agent-control-plane]] and [[patterns/structural/authoritative-recheck-after-notification]] rather than being claims that a status URL by itself supplies security. [[sources/microsoft--async-request-reply#lifecycle]], [[sources/microsoft--cqrs#separation]], [[sources/aws--idempotent-apis#retries]], [[sources/ietf--http-semantics#concurrency]]

## Patterns demonstrated

- [[patterns/structural/authoritative-recheck-after-notification]] — queued execution can outlive the input state; source guidance on command validation and duplicate-safe processing complements the existing agent implementation. This does not add another inspected artifact or promote the pattern. [[sources/microsoft--cqrs#separation]]
- Candidate technique: explicit read/command/operation contracts, supported by several design documents here. No new confirmed pattern is created: documentation agreement is not inspection of two runnable artifacts.

## Tensions & counter-arguments

- **Separation costs:** CQRS with separate stores creates synchronization, consistency, and operational complexity. Its basic form can share a store; ordinary CRUD may be sufficient. Endpoint separation alone is not full CQRS. [[sources/microsoft--cqrs#separation]]
- **Resource purity versus business intent:** standard methods improve consistency, but custom actions are justified when standard methods do not fit. Google explicitly warns against contorting semantics. [[sources/google--aip-136#actions]]
- **Synchronous simplicity versus durable execution:** short predictable work need not become a job. Long-running work introduces polling, retention, and partial-failure contracts. [[sources/microsoft--async-request-reply#lifecycle]]
- **Composition versus invariant preservation:** reusable pieces help only when they retain coherent business rules. Domain boundary evaluation remains an evolving judgment, not a mechanical endpoint-size formula. [[sources/microsoft--domain-analysis#boundaries]]
- **Evidence boundary:** this review reads primary guidance. It does not benchmark an implementation, select a workflow engine, or establish any existing business platform's correctness.

## Timeline

- 2026-11-04 — Queried wiki for existing API-design coverage; captured nine primary sources and compiled this concept, distinguishing source conventions from proposed platform decisions.

## Related

- [[artifacts/projects/shopify-api]] — business GraphQL alongside negotiated agent tools, full-state updates, explicit escalation and operation-specific retry contracts.

- [[projects/designing-apis-for-agents/README]] — ongoing research group; questions, evidence map, and future investigations.

- [[concepts/agent-control-plane]] — durable business/task identity and runtime identity have separate lifecycles.
- [[concepts/durable-agent-execution]] — a worker needs stronger persistence than a response that merely says accepted.
- [[concepts/ubiquitous-language-for-agents]] — shared domain terms carry into route and command naming.
- [[concepts/code-mode-capability-interface]] — composable agent interfaces depend on explicit capability effects and results.

## What we'd steal

- ★ Separate intent/effects from execution duration in the API catalog.
- ★ Explicit initiation, durable operation status, and result retrieval for long-running work.
- ★ Domain capability ownership; orchestrate shared rules instead of duplicating them.
- ★ Keep coherent modules before multiplying network boundaries for imagined future reuse.
- Resource nouns and purposeful actions; consistent style without forcing every action into CRUD.
- A normal command may return the resulting business resource.
- Business run identity and runtime operation identity need not be the same object.
- Distinguish operation success from approval, settlement, publication, or other business completion.
- Declare freshness and input-version semantics.
- Validate early; enforce transactional preconditions at execution.
- Durable acceptance and outbox/queue recovery before claiming work is accepted.
- Caller-intent idempotency, payload mismatch handling, and a documented retention window.
- Separate request deduplication from worker/provider effect deduplication and reconciliation.
- Explicit cancellation limits and partial-result/error representation.
- Authorized status/results, per-domain permissions, quotas, and cost boundaries.
- Consistent schemas, errors, pagination, filtering, ordering, compatibility, and migration policy.
- Correlate requests, runs, attempts, provider actions, and outputs.
- Review contracts against concrete failure scenarios, not just a successful response example.

## Open questions

- Which business domains and cross-domain processes does the target platform actually own?
- Which operations have real latency, compensation, approval, or provider-reconciliation requirements?
- Which capabilities already have multiple consumers, and which are hypothetical reuse?
- Should each domain expose its own run resources, or is a shared operation envelope sufficient?
- Which tenant isolation, data residency, scale, and ownership constraints justify deployment boundaries?

## Cross-system API research — 2026-11-04

[[analyses/frontier-and-business-api-design]] compares nine documented systems and preserves the distinction between capability intent, presentation, execution and business outcome. [[concepts/agent-api-learning-and-evolution]] separates training familiarity from current interface context and observable task performance. The synthesis remains draft; no runtime or agent-success guarantee is added to this page.

## MCP research connection — 2026-11-04

[[concepts/model-context-protocol]] is a host/service facade over domain operations, not a replacement for their effect and consistency contracts. [[analyses/mcp-and-extensions]] applies that distinction to Apps, authorization and Tasks; transport retries need domain idempotency/readback. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#tools-state-errors]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#http-recovery]]

## Documentation application — 2026-11-05

[[concepts/developer-documentation-design]] applies this research to documentation authoring, distribution or review. See [[projects/writing-amazing-developer-docs/README]] for the evidence map. This cross-reference adds no inspected runtime example or benchmark result.

## Frontier documentation interfaces — 2026-11-05

[[concepts/agent-documentation-interfaces]] specializes the delivery/interaction boundary: source retrieval versus synthesized answers versus API execution; version fallback and retrieval-triggered indexing; browser-local tool lifecycle; novel/internal API task evaluation. [[sources/frontier-docs--platforms-20261105#root]] [[sources/frontier-docs--webmcp-20261105#root]] [[sources/frontier-docs--empirical-20261105#root]]

The owned findings preserve source-specific controls and uncertainty; no universal context budget or future training-data guarantee is inferred. See [[artifacts/projects/dokimi]] for the documented evaluator, and [[artifacts/projects/webmcp]] for the dated browser contract.

## Vercel Schedules — 2026-11-06

[[artifacts/projects/vercel-schedules]] is a schedule-resource API case study: name/ID/occurrence identity, OIDC environment scope, partial read projections, cursor-complete pagination and retry-after-write ambiguity. HTTP and SDK shapes differ; invoke is not generally retry-idempotent. [[sources/vercel--schedules-docs#api]] [[sources/vercel--schedules-docs#sdk]] [[sources/vercel--schedules-docs#retry-boundary]]

## T3 Code — 2026-11-07

[[artifacts/projects/t3code]] adds a pinned source case: Implement reusable domain capabilities before adapting user RPC/MCP/jobs. Decoded flags can make a retrieval-shaped method effectful and change its required authority; one route label is not an effect contract. [[sources/pingdotgg--t3code#service-reach]] [[sources/pingdotgg--t3code#auth-rpc-authorization]] Source/test inspection only; no hosted/provider outcome or new model score claimed.
