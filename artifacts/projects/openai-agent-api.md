---
domain: artifacts
subdomain: projects
type: project
name: openai-agent-api
creator: "[[creators/openai]]"
source: "[[sources/openai--agent-api-design]]"
ecosystem: openai
status: documentation-investigated
last-reviewed: 2026-11-04
---

# OpenAI agent and model APIs

> Separate the model/tool protocol, durable conversation, managed session, and execution environment. “Agent API” is not one undifferentiated endpoint.

## Attributes

- **Unit studied:** ten official documentation pages captured 2026-11-04, including Responses/function calling, background execution, Webhooks, Conversations, Batch, Structured Outputs, general compatibility, and managed Agents API configuration/review. [[sources/openai--agent-api-design#root]]
- **Evidence class:** documentation and documented request/response examples. No API calls, SDK execution, application installation, model evaluation, account permission check, or provider fault-injection test.
- **Distribution:** hosted API with official SDK examples. Protocol, SDK, and model behavior have different compatibility promises. [[sources/openai--agent-api-design#compatibility]]
- **Credibility:** official provider documentation, as of capture date. No popularity/adoption signal was measured.

## Relationships

- [[creators/openai]] — publisher/provider.
- [[projects/designing-apis-for-agents/README]] — research group and follow-on questions.
- [[concepts/business-platform-api-design]] — shared query/command/operation vocabulary.
- [[concepts/agent-control-plane]] and [[concepts/durable-agent-execution]] — separate durable state and execution lifecycles.
- [[concepts/code-mode-capability-interface]] — tool discovery, namespaces and composition.

## Mechanism and themes

### Three surfaces deliberately assign different responsibilities

| Surface | Documented orchestration/state ownership | Important limit |
| --- | --- | --- |
| Responses | Direct model interactions; manual history, response chaining or Conversations; hosted tools and application-executed tools | A custom function call is a request for application execution, not evidence that the business action occurred |
| Agents SDK | Runner in the application; application chooses deployment, storage, approvals and runtime integration | An SDK session is not the same resource as a managed API session |
| Agents API | OpenAI-managed Codex harness; saved session configuration, turns and items; service tools, application handlers and optional sandbox | A managed session, a saved agent, a Responses conversation and an execution sandbox remain distinct |

This is the provider's documented surface comparison, not an assertion that every behavior was implemented or tested in this research. Integration-effort labels in the source are provider claims, not measured outcomes here. [[sources/openai--agent-api-design#agent-surfaces]]

### A typed request to act is distinct from acting

In the Responses custom-function flow, the application sends tool definitions; the model emits zero, one or several calls; the application executes its code and submits outputs linked by `call_id`; the model continues. Output items can therefore be calls or messages rather than one fixed text body. Responses may use provider-hosted tools too, so “all tools execute in the caller” would also be wrong. [[sources/openai--agent-api-design#function-loop]]

Function definitions use purpose/parameter descriptions and JSON Schema. Strict mode constrains arguments, requires closed objects and all properties marked required, and represents optionality with nullable types. Captured docs explicitly distinguish Responses' attempt to normalize omitted strictness (with possible fallback) from Chat Completions' non-strict default. Model/version/path support matters; do not convert one endpoint's defaults into a platform-wide guarantee. [[sources/openai--agent-api-design#strict-schema]]

Structured Outputs separates valid shape from true content: the source warns that schema-conforming answers can still contain mistakes, and clients must account for refusal and incomplete output. Business validation and authorization remain additional application responsibilities—our inference from those limits, not a promise that a schema authorizes a payment. [[sources/openai--agent-api-design#structured-output-limits]]

### Naming and catalog design work at a different layer from HTTP paths

OpenAI's HTTP surface names provider resources such as responses, conversations and batches. Inside a model request, domain tools instead have purpose-bearing names, argument schemas, descriptions and namespaces. The function guide recommends concise namespace guidance for finding tool groups, detailed tool guidance for actual use, and deferred tool loading for larger catalogs. The reusable principle is a stable capability model plus a discoverable model-facing catalog—not replacing all REST resources with agent prompts. [[sources/openai--agent-api-design#tool-design]]

The source recommends not asking a model for already-known arguments, combining functions always used in a mandatory sequence, and evaluating the initial tool count (fewer than 20 is a soft suggestion). These are documented design recommendations, not a measured universal threshold. They create a real tension with speculative fine-grained endpoints: sometimes a cohesive business operation is a better callable unit. [[sources/openai--agent-api-design#tool-design]]

### Background generation reuses a resource rather than inventing a worker endpoint

The documented example creates a response through `POST /v1/responses` with `background: true`, retrieves it with `GET /v1/responses/{id}`, polls while queued/in progress, and cancels with `POST /v1/responses/{id}/cancel`. Background execution and resource intent are separate dimensions. A caller need not know which worker runs generation. [[sources/openai--agent-api-design#background]]

Streaming is another delivery option: a background response created with streaming enabled can resume after a stored-event sequence cursor. This is recovery of response delivery, not evidence of exactly-once execution of external business effects. The source also states temporary storage/retention conditions; background execution is not equivalent to “store nothing.” [[sources/openai--agent-api-design#background]]

Webhooks carry an event type and resource identifier, and the example retrieves the response to inspect its output. Receivers should verify signatures, acknowledge promptly, offload substantive processing, and deduplicate. Captured docs state exponential retry for up to 72 hours and possible duplicate delivery. Successful receipt, completed response generation, and completed business action are three different outcomes. [[sources/openai--agent-api-design#webhooks]]

### State has several identities and retention policies

A Conversation is a durable identified container for messages, calls and outputs that can be reused across sessions/devices/jobs. A Response is a generation resource; the conversation guide documents default response retention and a distinct TTL policy for conversation items. Chaining by prior response ID does not remove prior-input token charges. Those are specific source policies, not advice to retain business data indefinitely. [[sources/openai--agent-api-design#conversation]]

For managed Agents API, reusable saved configuration is copied into a session. Later saved-agent changes affect new sessions, not existing ones. Existing-session updates apply to later turns and have field-specific merging/replacement rules; some settings require a new session. The API even distinguishes an idle-state precondition (`409 Conflict`) for changing automatic review. This is a concrete example of lifecycle-aware updates rather than an unrestricted generic PATCH. [[sources/openai--agent-api-design#session-configuration]]

### Context delivery, authority and enforcement

| Boundary | What the captured documentation establishes |
| --- | --- |
| Context | Instructions, schemas, conversation items and saved configuration influence model work |
| API identity | Bearer credentials, optional organization/project selection, and separate administration credentials identify API access |
| Custom functions | Application executes model-requested functions; the call does not itself establish business authority |
| Managed action review | A reviewer model can approve/deny supported action requests according to context/risk; `review: none` is not a manual-approval mode |
| Environment enforcement | Review does not override outbound network restrictions; setting review alone does not configure self-hosted sandboxing |

The first two rows describe model context and API credential contracts. The last three show why a prompt, tool schema, approval decision and sandbox cannot be treated as interchangeable controls. Actual tenant ACLs for a business system and its final action authorization were not inspected. [[sources/openai--agent-api-design#function-loop]], [[sources/openai--agent-api-design#compatibility]], [[sources/openai--agent-api-design#review-boundary]]

### Batch is an explicit operation with item-level outcomes

Batch uploads a request file, starts a batch, exposes status, and places results in output/error files. Requests carry a unique `custom_id`; results may be reordered. Cancelled or expired jobs can still yield completed results, and unfinished items have explicit failures. An outer job's terminal state is therefore insufficient to decide every item's business outcome. [[sources/openai--agent-api-design#batch]]

### Compatibility includes behavioral drift

The general reference distinguishes REST major-version stability, semantically versioned SDKs and changeable model prompting behavior. It lists new JSON fields, opaque-ID format changes and new streaming event types as compatible additions, while recommending pinned model versions and application evaluations for behavior. This matters for agents: a stable HTTP schema alone does not ensure a stable decision policy. [[sources/openai--agent-api-design#compatibility]]

Request IDs and rate-limit headers provide operational contracts. `X-Client-Request-Id` is documented for tracing requests that lose their response. These pages do not establish it as a deduplication/idempotency key; do not silently assign it that meaning. [[sources/openai--agent-api-design#compatibility]]

## Patterns demonstrated

- [[patterns/behavioral/context-is-not-authority]] — schemas and context influence action proposals; application execution, review and environment controls have distinct boundaries. Documentation-level supporting comparison; no runtime guarantee was tested. [[sources/openai--agent-api-design#function-loop]], [[sources/openai--agent-api-design#review-boundary]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — model selects/proposes calls while the application executes, links outputs, checks schema and inspects statuses. [[sources/openai--agent-api-design#function-loop]], [[sources/openai--agent-api-design#strict-schema]]
- [[patterns/composition/resolver-routing-table]] — a tool namespace and deferred catalog provide selection metadata separately from loaded tool-use detail. This is a documented analogy, not evidence that the provider internally uses this wiki's routing pattern. [[sources/openai--agent-api-design#tool-design]]
- Candidate technique: explicit state-resource separation across response/conversation/session/environment. Do not promote on multiple modules of this one vendor alone. [[sources/openai--agent-api-design#agent-surfaces]]

## What we'd steal

- ★ **Name each lifecycle separately:** business task/run, model response, conversation, reusable configuration and execution environment. Adapt to business workflows without equating a generated answer to completed work. [[sources/openai--agent-api-design#agent-surfaces]]
- ★ **Make orchestration ownership an explicit product choice:** direct model protocol, app runner or managed agent; document who stores state and executes each tool type. [[sources/openai--agent-api-design#agent-surfaces]]
- ★ **Treat function calls as typed requests:** correlate outputs by call identity, support multiple calls, and validate business permission at execution. Schema matching alone is insufficient. [[sources/openai--agent-api-design#function-loop]], [[sources/openai--agent-api-design#structured-output-limits]]
- ★ **Separate background mode from intent:** reuse a named resource with initiation/retrieval/cancellation rather than exposing worker implementation. [[sources/openai--agent-api-design#background]]
- **Use domain names plus descriptions and schemas:** explain purpose, argument format, output meaning, and when not to call. [[sources/openai--agent-api-design#tool-design]]
- **Give catalog routing and actual use different detail levels:** concise namespace metadata, richer deferred tool definitions. [[sources/openai--agent-api-design#tool-design]]
- **Avoid asking the model to regenerate known IDs/context:** bind trusted known values in application code where appropriate. Do not hide information needed to authorize or audit an action. [[sources/openai--agent-api-design#tool-design]]
- **Combine mandatory sequences into coherent capabilities:** useful when every caller must take all steps; retain separate useful business operations when independent use is real. [[sources/openai--agent-api-design#tool-design]]
- **Evaluate the exposed tool count:** defer large/rare catalogs; do not legislate the guide's soft 20-tool suggestion as a universal limit. [[sources/openai--agent-api-design#tool-design]]
- **Represent impossible states structurally:** enums, closed objects, nullable optional fields and explicit strictness; test endpoint-specific defaults and unsupported schema handling. [[sources/openai--agent-api-design#strict-schema]]
- **Distinguish schema validity, refusal, incomplete output and semantic truth:** wire distinct handling paths. [[sources/openai--agent-api-design#structured-output-limits]]
- **Support reconnection with explicit cursors:** keep response delivery recovery separate from tool-effect recovery. [[sources/openai--agent-api-design#background]]
- **Publish webhook delivery semantics:** signature verification, acknowledgement deadline, retry window, duplicate key and fetchable canonical resource. [[sources/openai--agent-api-design#webhooks]]
- **Declare state retention by object:** do not let conversation lifetime silently inherit response TTL or background-storage assumptions. [[sources/openai--agent-api-design#conversation]], [[sources/openai--agent-api-design#background]]
- **Snapshot reusable settings into active work:** later definition edits should not silently mutate in-flight sessions. State exactly which changes affect future turns or require replacement. [[sources/openai--agent-api-design#session-configuration]]
- **Document merge versus replace versus clear semantics per field:** generic partial update language can conceal materially different behavior. [[sources/openai--agent-api-design#session-configuration]]
- **Separate review from containment and business permissions:** review modes and network/sandbox restrictions solve different problems; review disabled is not manual approval. [[sources/openai--agent-api-design#review-boundary]]
- **Use item IDs and per-item outcomes in bulk work:** ordering and an outer terminal state are insufficient; expose retained partial results. [[sources/openai--agent-api-design#batch]]
- **Separate protocol and model-behavior compatibility:** tolerate documented additive events/fields, pin models when needed, and maintain task evaluations. [[sources/openai--agent-api-design#compatibility]]
- **Provide tracing independent of returned response IDs:** preserve caller trace IDs and server request IDs; do not mislabel tracing as idempotency. [[sources/openai--agent-api-design#compatibility]]

## Tensions and anti-patterns

- **Convenience versus lifecycle complexity:** saved sessions and conversations reduce caller state handling but introduce distinct retention, update and cleanup contracts. [[sources/openai--agent-api-design#conversation]], [[sources/openai--agent-api-design#session-configuration]]
- **Composition versus semantic opacity:** a large generic tool surface can increase selection burden; combining every operation into one generic tool can hide business effects. The guide advocates small evaluated initial tool sets and cohesive mandatory sequences, not one endpoint for everything. [[sources/openai--agent-api-design#tool-design]]
- **Strict schema versus correct business decision:** a valid enum can still encode a wrong or unauthorized action. The source itself warns of content mistakes. [[sources/openai--agent-api-design#structured-output-limits]]
- **Managed autonomy versus authority:** model-based review does not replace the environment's restrictions or an application's real business controls. [[sources/openai--agent-api-design#review-boundary]]
- **AI-native does not imply an entirely new protocol:** resource IDs, HTTP verbs, async status, credentials, webhooks, request tracing and item correlation remain ordinary API mechanisms; the novel emphasis is model-selected work, state and runtime ownership. This is our interpretation of the documented contracts, not a historical priority claim. [[sources/openai--agent-api-design#root]]

## Open questions and verification record

- No behavior, permissions, background recovery or webhook delivery was executed. Provider documentation is the evidence class throughout.
- No comparison task corpus or model experiment establishes that these names/surfaces outperform other designs.
- The captured pages do not settle request idempotency across response creation, business-provider side effects, or unknown-outcome reconciliation for a target application.
- API docs do not establish which legacy/vendor APIs a model saw during training, how often, or the effect of future training. The function guide confirms training on a function-definition syntax, which is a narrower claim. [[sources/openai--agent-api-design#tool-design]]
- The research captures documentation as of 2026-11-04; feature support and availability require a fresh check before implementation.
- Source anchors and immutable snapshot hashes were checked locally; full wiki integration and broader doctor run are parent-coordinated.
