---
domain: concepts
type: concept
name: model-context-protocol
creators: ["[[creators/model-context-protocol]]"]
sources: ["[[sources/modelcontextprotocol--mcp-core-and-extensions-docs]]"]
status: active
last-reviewed: 2026-11-04
---

# Model Context Protocol

> MCP standardizes how an AI host discovers and uses external context and capabilities; the host and backing services still own orchestration, permissions and business correctness.

## What it is

MCP is a JSON-RPC protocol with three architectural roles: the **host** owns the AI experience and context, a **client** connects that host to one server, and a **server** exposes focused capabilities. A host can manage many clients. The server need not receive the whole conversation or see other servers; the host controls those information flows. This is the specified architecture, not proof that every connected product enforces it. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#architecture]]

At the captured current revision, `2026-07-28`, requests are self-contained: version and client capabilities travel in each request's `_meta`. Servers must implement `server/discover`; clients may call it to discover versions, identity and capabilities, or send a request and handle a version error. Modern MCP does not require an `initialize` handshake. Legacy `2025-11-25` and earlier do. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#current-version]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#compatibility]]

## Where it came from

This page distills the MCP project's current specification and companion extension documents captured on 2026-11-04. It studies a protocol contract, rather than attributing every subsequent extension to the protocol's original creator. [[creators/model-context-protocol]] represents the project/maintainer community; [[creators/anthropic]] and [[creators/openai]] have separately studied contributions. No historical origin date or ecosystem-wide adoption total was independently investigated in this pass. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#root]]

## Why it matters

One service contract can expose the same capabilities to different AI hosts, while the host handles model integration and human interaction. This creates an integration boundary; it does not make models, clients, workflows or authorization policies interchangeable. A correct build must select a common protocol revision, implement optional features explicitly and test its intended host. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#architecture]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-negotiation]]

## Evidence & claims

### The primitive vocabulary

| Contract/feature | Purpose | Interaction roles | Important boundary |
| --- | --- | --- | --- |
| Tools | Executable operations, input/output JSON schemas, content and structured results | Model through the host | Annotations are advisory; server must validate inputs and authorization |
| Resources | Addressable context/data, resource templates and reads | Application/host | A URI is not a permission grant or a filesystem path available to the model |
| Prompts | Reusable message/workflow templates with arguments | User through the host | Instructions do not implement business effects |
| Elicitation | Additional user input via form or URL interaction | Server requests; host presents; user reviews/accepts/declines | Sensitive credentials require URL-mode handling; execution checks remain necessary |

These are interaction models rather than a mandatory UI design. Tools, Resources and Prompts are distinct server primitives, not synonyms for three sorts of tool descriptions. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#primitives]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#elicitation]]

### Transport and lifecycle changed materially

| Dimension | Current `2026-07-28` | Legacy compatibility concern |
| --- | --- | --- |
| Negotiation | Per-request version/capabilities; optional client `server/discover` | `initialize`/initialized handshake |
| HTTP state | No protocol session IDs; explicit server-issued handles for cross-call state | Earlier Streamable HTTP could use `Mcp-Session-Id` |
| Server needs input | `input_required` result; retry original operation with `inputResponses` and opaque `requestState` | Earlier server-initiated JSON-RPC requests |
| Change notifications | Opted-in `subscriptions/listen` POST response stream | Earlier GET stream and resource subscription methods |
| Broken SSE response | Reissue as a new request with a new ID | Earlier resumable stream/message redelivery support |
| Async work | Optional Tasks extension | Experimental tasks previously lived in core |

The current standard transports are newline-delimited stdio for a local subprocess and Streamable HTTP for a remote endpoint. HTTP POST can return JSON or SSE; **using SSE does not make it the deprecated HTTP+SSE transport**. HTTP requires metadata headers including protocol version and applicable method/name headers, plus Origin validation. Merely serving JSON-RPC at a URL is insufficient conformance. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#transports]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#http-recovery]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#current-version]]

### Requests, business state and recovery

MCP being stateless does not require a stateless business. A server can issue a cart, workflow or other opaque handle, then require it as an ordinary tool argument on later calls. For authenticated servers, a handle is a name rather than a capability: validate caller authorization on every use. The non-normative guidance separately permits unauthenticated handles to act as bearer tokens, with sufficient entropy and bounded lifetime. Likewise, a JSON-RPC request ID correlates messages; this study found no general exactly-once business execution guarantee. Reissuing after a lost response therefore needs the underlying operation's idempotency/reconciliation design. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#tools-state-errors]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#http-recovery]]

MRTR returns `resultType: "input_required"`; the host fulfills permitted input requests and retries the operation with a different JSON-RPC ID. A server must treat client-carried `requestState` as attacker-controlled and integrity-protect it when it influences authorization, resource access or business logic. The spec recommends binding principal, expiry and originating request to limit replay; one-time redemption invariants require server-side enforcement. Opaque does not mean confidential. This is a continuation contract, not proof that a user approved the final business action. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#mrtr]]

Results distinguish protocol errors from tool execution errors (`isError: true`). The former describe inability to process the request; the latter can be an ordinary tool result explaining a business failure. A received result is not evidence that a payment, publication or other downstream effect succeeded. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#tools-state-errors]]

### Caching, identity and deprecated features

Cacheable results carry freshness and sharing hints (`ttlMs`, `cacheScope`); TTL is not immutability. Private cache reuse is restricted to the same authorization context. Method/parameter identity matters; Results of MRTR retries carrying `inputResponses` or `requestState` must not be cached. A change notification can invalidate a still-fresh entry. Self-reported serverInfo is for display/debugging, not a trust root. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#caching]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#discovery]]

Roots, Sampling, Logging and Dynamic Client Registration are deprecated in this revision, with documented migration paths and earliest removal rules. They are **still specified**, not already removed. Roots describe relevant filesystem scope; they do not create an OS sandbox. Existing implementations may depend on these features, so migration must be version-qualified. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#deprecated]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#base]]

## Patterns demonstrated

- [[patterns/behavioral/context-is-not-authority]] — tool descriptions, server identity strings, resource URIs and state handles are information; enforce access at the host/server/provider boundary. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#discovery]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#tools-state-errors]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — model chooses or composes capabilities; code validates schemas, transport metadata, state and credentials. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#base]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#transports]]
- [[patterns/composition/negotiated-capability-intersection]] — adjacent documented compatibility mechanism. MCP selects versions and checks peer support; it does not establish Shopify's exact dependency-pruning algorithm. This comparison does not promote the proposed pattern. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#compatibility]]
- [[patterns/quality-bar/revision-bound-review]] — a protocol generation is part of the evidence identity; modern and legacy examples cannot be merged into one contract. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#current-version]]

## Tensions & counter-arguments

The specification concentrates responsibilities in the host: context isolation, user consent and tool policy require real implementation. Remote service authentication also does not grant the MCP server unrestricted downstream API authority; its backend needs its own scoped credentials and checks. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#architecture]], [[concepts/mcp-enterprise-managed-authorization]]

Protocol standardization does not remove large-catalog discovery, context cost or tool semantics problems. [[concepts/code-mode-capability-interface]] addresses one complementary interface technique; [[concepts/skills-over-mcp]] supplies workflow context. Neither makes invalid API contracts valid. Declared extension support is a compatibility assertion, not a measured end-to-end result. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-negotiation]]

## Timeline

- 2026-11-04 — Captured current `2026-07-28` requirements and modern/legacy differences; added linked Apps, auth, vendor extensions and Skills studies. Documentation/code inspection only. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#root]]

## Related

- [[concepts/mcp-extension-architecture]] — optional extension contracts, maturity and fallback.
- [[artifacts/projects/mcp-apps]] — interactive UI protocol and SDK boundaries.
- [[artifacts/projects/openai-mcp-extensions]] — ChatGPT-specific product and SDK layer.
- [[concepts/mcp-enterprise-managed-authorization]] — human and workload identity contracts.
- [[concepts/skills-over-mcp]] — discoverable instructions and integrity checks.
- [[concepts/durable-agent-execution]] — step replay is stronger than task-status retrieval.
- [[artifacts/projects/kody]] — a concrete capability facade delivered through MCP.
- [[analyses/mcp-and-extensions]] — full comparison and proposed build sequence.

## What we'd steal

- ★ Keep host orchestration and service contracts separate; expose focused capabilities to many clients. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#architecture]]
- ★ Pin the protocol generation and feature matrix before choosing SDK examples. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#compatibility]]
- ★ Pass explicit server-issued business handles; validate ownership on each use. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#tools-state-errors]]
- ★ Design mutation idempotency and outcome readback below the transport retry layer. This is an adaptation inferred from lost-response reissue semantics, not an MCP-provided guarantee. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#http-recovery]]
- Preserve tools/resources/prompts as separate contracts rather than overloading tool descriptions with every context and workflow. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#primitives]]
- Use protected opaque continuation state for input rounds; enforce one-time use when the business demands it. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#mrtr]]
- Make cache scope an explicit authorization concern and use notifications as invalidation signals. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#caching]]
- Preserve protocol failures versus actionable domain/tool errors in logs and UI. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#tools-state-errors]]
- Treat discovery identity as display metadata; establish trust independently. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#discovery]]
- Keep local Origin/localhost protections and HTTP header/body consistency checks in code. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#transports]]
- Plan deprecation migration without claiming removal already happened. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#deprecated]]

## Open questions

- Which precise SDK/host releases implement the modern core and each extension together? This pass captures documentation, not a certified interoperability matrix.
- Which mutation APIs expose an idempotency key, durable operation ID and authoritative readback after a dropped stream?
- What are the measured discovery/context/latency tradeoffs for a direct tool catalog versus Code Mode on our actual workloads?

## Mintlify documentation application — 2026-11-05

[[artifacts/projects/mintlify]] examines documented index, skill, retrieval and editing surfaces with distinct authority and lifecycle boundaries. Its cited external discovery/protocol schema versions are not independently conformance-verified here. Source inspection is limited to the public URL benchmark; no hosted runtime guarantee or confirmed platform-implementation example is added.

## WebMCP and agent documentation follow-up — 2026-11-05

[[artifacts/projects/webmcp]] records current CG draft/browser/testing contracts separately: `document.modelContext` in the captured draft/Chrome guidance, older `navigator.modelContext` vocabulary in other current documentation, and declarative forms outside the current CG specification. This qualifies earlier evidence without editing its immutable snapshots. It is a documentation disagreement, not a reproduced interoperability failure. [[sources/frontier-docs--webmcp-20261105#documentation-drift]] [[sources/frontier-docs--webmcp-20261105#declarative-proposal]]

[[concepts/agent-documentation-interfaces]] compares page-local tools with documentation retrieval, generated answers, backend execution and administration.
