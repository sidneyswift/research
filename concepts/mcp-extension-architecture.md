---
domain: concepts
type: concept
name: mcp-extension-architecture
creators: ["[[creators/model-context-protocol]]"]
sources: ["[[sources/modelcontextprotocol--mcp-core-and-extensions-docs]]"]
status: active
last-reviewed: 2026-11-04
---

# MCP extension architecture

> A small common protocol can grow through explicitly negotiated feature contracts, while wire stability, implementation availability and product access remain separate questions.

## What it is

An MCP extension adds optional behavior beyond the core protocol. Its identifier is namespaced and its capability entry carries extension-defined settings. Core conformance does not require an SDK to implement every extension. Even Stable extensions require developer opt-in; unsupported optional UI should degrade to useful core output, while mandatory authorization can reject a client that lacks the required mechanism. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-lifecycle]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-negotiation]]

Extensions are not the same object as installable agent plugins, browser extensions or MCP servers. A server can implement several extensions; a plugin can package a server and instructions; a host can support only selected extension features. OpenAI's vendor-specific [[artifacts/projects/openai-mcp-extensions]] is also distinct from the MCP project's official `ext-*` catalog. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-catalog]], [[sources/openai--mcp-extensions#root]]

## Where it came from

The captured extension governance defines Experimental → Beta → Stable, with the option to promote a Beta or Stable feature into core through a Standards Track SEP. Official extension repositories live in the MCP GitHub organization. A Final SEP, a Stable schema snapshot, an npm version and a Stable extension lifecycle stage are different statuses. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-lifecycle]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#documentation-conflicts]]

## Why it matters

Teams can adopt one feature without implementing every experiment, and independent clients can state exactly which behavior they understand. The cost is a compatibility matrix: core version × extension wire revision/settings × SDK implementation × host surface/build × authorization policy. Treating a package install as proof of that entire matrix is the principal mistake this research would avoid. This matrix is our architectural inference from the separated contracts. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-negotiation]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#support-matrix]]

## Evidence & claims

### Catalog at retrieval

| Extension | Identifier | Catalog stage on 2026-11-04 | What it adds / evidence boundary |
| --- | --- | --- | --- |
| MCP Apps | `io.modelcontextprotocol/ui` | Stable | Interactive HTML views; [[artifacts/projects/mcp-apps]] owns wire/SDK/host distinctions |
| OAuth Client Credentials | `io.modelcontextprotocol/oauth-client-credentials` | Stable | Workload identity; [[concepts/mcp-enterprise-managed-authorization]] compares auth modes |
| Enterprise-Managed Authorization | `io.modelcontextprotocol/enterprise-managed-authorization` | Stable | Enterprise user identity brokering; does not itself audit every business action |
| Tasks | `io.modelcontextprotocol/tasks` | Beta, intended for Core | Durable handles, polling and input; schema-release stability is separate |
| Skills over MCP | `io.modelcontextprotocol/skills` | Beta, destination unstated | Discover/read skills; [[concepts/skills-over-mcp]] owns integrity/activation rules |
| Server Cards | No capability identifier established in this study | Catalog says Beta; repo says Experimental | Static remote connection metadata; stage conflict remains unresolved |

Stages come from the living catalog; the Server Cards disagreement is preserved rather than silently resolved. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-catalog]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#server-cards]]

### Negotiation and evolution

In modern core, clients advertise extensions in per-request clientCapabilities; servers advertise theirs through `server/discover`. Earlier implementations used `capabilities.extensions` in `initialize`, even though those older published schemas did not formalize that field. Version support must be checked before copying examples. Extension settings can further restrict MIME types or other behavior; recognizing a name alone is insufficient. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-negotiation]]

Experimental behavior can change freely and should be pinned. Beta prefers additive changes but can break compatibility, with a revision setting used to expose mismatches when appropriate. Stable behavior is published against a core protocol revision and immutable within that revision; draft changes accumulate for a later revision. Promotion to core makes the behavior core for the new revision, while older revisions may still need the extension advertised. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-lifecycle]]

Beta admission requires an official SDK reference implementation before review. Stable promotion requires an additional SEP, independent interoperating client/server implementations and a conformance scenario. These are governance requirements, not tests we executed or a promise that all SDKs/hosts support the feature. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-lifecycle]]

### Tasks: a lifecycle contract beyond one response stream

The captured `2026-07-28` Tasks spec augments `tools/call`: a supporting server can return `resultType: "task"` only if the client advertised the extension on that request. The task must already resolve durably before its handle is returned. `tasks/get` observes it, `tasks/update` supplies outstanding input, and `tasks/cancel` requests cancellation. `Mcp-Name` carries taskId for these HTTP methods. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#tasks]]

The distinctions are useful for [[concepts/durable-agent-execution]]: a durable task handle does not prove durable replay of every internal step or exactly-once external effects. Cancellation acknowledgment does not guarantee work stopped. A completed task can contain a tool result with `isError: true`; `failed` is reserved for JSON-RPC execution faults. Every task-related request still needs authorization; input requests receive the ordinary host trust checks. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#task-errors-security]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#tasks]]

### Three different kinds of discovery

1. A Server Card describes a remote server's identity and endpoints before connecting. It intentionally excludes tool/resource/prompt lists and local install metadata.
2. `server/discover` reports protocol versions and capabilities at runtime; its identity is self-reported.
3. Primitive catalogs (`tools/list`, etc.) describe operations/context, while `skills/list` describes workflow instructions.

These layers are complementary. None is proof of authorization or successful execution. Server Cards' captured README directs package/runtime/install metadata to the separate MCP Registry schema; a registry listing is not the same contract as a remotely hosted card. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#server-cards]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#discovery]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skills]]

## Patterns demonstrated

- [[patterns/composition/negotiated-capability-intersection]] — related compatibility contract; do not promote the more specific Shopify pattern merely because MCP has feature flags. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-negotiation]]
- [[patterns/quality-bar/revision-bound-review]] — extension stage and immutable protocol revision must accompany claims. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-lifecycle]]
- [[patterns/behavioral/context-is-not-authority]] — discovery and feature negotiation do not grant resource or task access. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#task-errors-security]]

## Tensions & counter-arguments

Optionality reduces mandatory implementation size while increasing the number of valid combinations a product must handle. Host support and SDK support can lag a specification. Community support tables help find evidence, but blank extraction cells and partial implementations make them unsuitable as a certification matrix. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#support-matrix]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#skill-support]]

The current ecosystem also contains documentation disagreements: Server Cards' lifecycle, outdated initialization summaries and Skills' obsolete stable-path links. These are concrete reasons to pin and reconcile evidence, not reasons to infer all extensions are unreliable. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#documentation-conflicts]]

## Timeline

- 2026-11-04 — Captured the six listed extension families, governance, modern/legacy negotiation and stage/documentation conflicts. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#root]]

## Related

- [[concepts/model-context-protocol]], [[artifacts/projects/mcp-apps]], [[artifacts/projects/openai-mcp-extensions]], [[concepts/mcp-enterprise-managed-authorization]], [[concepts/skills-over-mcp]], [[analyses/mcp-and-extensions]].
- [[concepts/convergent-agent-plugin-spec]] — file/package format convergence is a different layer.
- [[concepts/business-platform-api-design]] — domain operations still need their own consistency and effect contracts.

## What we'd steal

- ★ Separate normative core, extension wire, SDK and host versions in every implementation decision. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#documentation-conflicts]]
- ★ Keep one useful core response when optional UI is absent; fail closed when mandatory auth cannot be honored. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-negotiation]]
- ★ Treat task creation durability, cancellation intent and business success as separate observable states. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#tasks]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#task-errors-security]]
- Require real independent interoperability and a conformance scenario before calling our own extension stable. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-lifecycle]]
- Keep card discovery, capability discovery, operation catalogs and skill discovery distinct. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#server-cards]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#discovery]]
- Record conflicts as unresolved evidence with exact sources; don't merge all statuses into a single readiness badge. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#documentation-conflicts]]
- Attach authorization to each task operation; do not trust possession of a task name alone. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#task-errors-security]]

## Open questions

- Which source resolves the Server Cards catalog-versus-README stage disagreement?
- Which modern SDK receivers implement Tasks fully, beyond the legacy receiver support described by its README?
- Which exact host/build/settings combinations provide each extension, and which fallback paths have been exercised?
