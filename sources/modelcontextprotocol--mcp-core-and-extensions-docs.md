---
domain: sources
type: docs-page
url: https://modelcontextprotocol.io/extensions/overview
retrieved: 2026-11-04
snapshot-location: sources/modelcontextprotocol--mcp-core-and-extensions-docs/
version: "2026-07-28 core; living extension catalog; pinned Tasks/Skills/Server Cards documents"
publish-date: "n/a (living pages)"
last-reviewed: 2026-11-04
---

# MCP core and extension architecture — official documentation collection

> Current protocol requirements, extension governance, Tasks, Skills, and discovery, captured separately from SDK execution and host adoption.

## Snapshot details

- **Retrieved:** 2026-11-04; official Markdown endpoints and selected immutable GitHub documentation files. The upstream documentation index was used to find versioned pages.
- **Evidence:** named captures in `sources/modelcontextprotocol--mcp-core-and-extensions-docs/`; `capture-map.json` records each URL, SHA-256, size and retrieval date. Captures are immutable; corrections belong on this citation page or the wiki.
- **Core revision:** `2026-07-28`, identified as current by `versioning.md`; earlier `2025-11-25` behavior is retained only where the captured compatibility page describes it.
- **Pinned supplements:** ext-tasks `b3d28aceaa6d49f5f92258e3d06b61ad6f111e84` (2026-10-20); ext-skills `649f7aee87d631ac4d1fdd3b12eef0c6264fdb3a` (2026-10-30); ext-server-card `526201bbc80231daa40ffcdecfc9da4e54e5dc93` (2026-08-12). These are selected documentation captures, not reconstructed source repositories or executed packages.
- **Scope:** documentation/specification inspection. No MCP server, client, conformance suite, SDK package, browser app, OAuth flow or business operation was run.

## Anchor map

- `#root` — entire collection and `capture-map.json`.
- `#architecture` — `architecture.md`, Host/Clients/Servers and Design Principles: host owns context, consent and cross-server boundaries.
- `#current-version` — `versioning.md`, Revisions and Negotiation; `changelog.md`, Major changes.
- `#base` — `base.md`, Messages, Statelessness, Auth, JSON Schema Usage and General fields.
- `#compatibility` — `compatibility.md`, modern/legacy terminology, version errors, extension negotiation and dual-era behavior; `stdio.md`, Backward Compatibility.
- `#discovery` — `discovery.md`, mandatory server RPC, optional client probe, caching, and unverified self-reported serverInfo.
- `#transports` — `stdio.md` and `http.md`, framing, POST/JSON/SSE, request headers, Origin checks, cancellation and backward compatibility.
- `#http-recovery` — `http.md`, Receiving Messages and Backward Compatibility; `changelog.md`, Major changes 1–9: no session header or resumable SSE; reissue broken in-flight requests.
- `#mrtr` — `multi-round-trip.md`, InputRequests/InputResponses/InputRequiredResult and client/server requirements, including conditional integrity requirements and replay guidance for opaque requestState.
- `#primitives` — `tools.md`, `resources.md`, `prompts.md`, User Interaction Model, Protocol Messages and Data Types.
- `#tools-state-errors` — `tools.md` lines 675–795, Stateful Tools, Error Handling and Security Considerations: explicit handles; protocol versus tool-execution error.
- `#elicitation` — `elicitation.md`, form/URL modes and security requirements; not every additional input should be sent as model context.
- `#deprecated` — `deprecated.md`, registry and migration paths: Roots, Sampling, Logging, DCR and older HTTP+SSE.
- `#caching` — `caching.md`, cache keys, freshness hints, public/private authorization contexts and pagination; MRTR-retried results are not cacheable.
- `#subscriptions` — `subscriptions.md`, opted-in notification types and acknowledgment; `http.md`, request-scoped versus listen-stream notifications.
- `#extension-lifecycle` — `snapshot.md` lines 19–150, Experimental/Beta/Stable, official repositories, reference implementations, conformance, opt-in and revision evolution.
- `#extension-negotiation` — `snapshot.md` lines 151–285, per-request modern capabilities, legacy initialize, graceful degradation and mandatory-auth rejection.
- `#extension-catalog` — `snapshot.md` lines 33–93, listed extensions, stages and destinations. Compare explicit caveats below.
- `#support-matrix` — `extensions-matrix.md`, community-maintained support list; most cells are blank in the Markdown capture and cannot establish support or absence.
- `#tasks` — `tasks.md` and pinned `tasks-spec.md` lines 19–410: capability, tools/call support, durable creation, polling, input, terminal states and cooperative cancellation.
- `#task-errors-security` — `tasks-spec.md` lines 782–911: protocol failure versus completed tool result with isError; per-request task authorization; unguessable IDs.
- `#task-version-drift` — `tasks-readme.md`, generation-agnostic requester/legacy receiver SDK description and released schema labels; `snapshot.md` lifecycle stage is separately Beta-to-Core.
- `#skills` — `skills.md` and `skills-spec.mdx` lines 25–475: Agent Skills transport binding, capability, skills/list/get, manifests, direct URI loading and resource reads.
- `#skill-integrity` — `skills-spec.mdx` lines 476–513 and 921–966; `skills.md`, Integrity and Verification/Security: retained manifests, per-file digest/size/frontmatter checks, origin, approval and dynamic-content limits.
- `#skill-support` — `skills-readme.md` and `skills-implementations.md`: Beta released revision, community implementation statuses including partial/plugin-submission-time import. Not deployment verification.
- `#server-cards` — `server-card-readme.md`, static remote connectivity metadata, recommended `<mcp-url>/server-card`, omission of primitive catalogs and install packages, experimental warning and graduation plan.
- `#documentation-conflicts` — the following evidence reconciliation notes, whose underlying captured sections are named above.

## Why we cite this

For protocol requirements and design intent, this is primary evidence. It does not prove any host/SDK implements those requirements, that the protocol solves authorization by itself, or that a tool's declared output is a successful business outcome. [[concepts/model-context-protocol]], [[concepts/mcp-extension-architecture]], [[concepts/skills-over-mcp]] and [[analyses/mcp-and-extensions]] own the distillation.

## Evidence reconciliation notes

- **Current versus legacy:** the current core overview still says extensions are negotiated “during initialization”; the dedicated versioning, changelog and extensions negotiation pages explicitly remove initialization for `2026-07-28`. Use their detailed version-qualified contract rather than the unqualified summary.
- **Server Cards:** the living extension catalog lists Beta, while the latest retrieved ext-server-card README calls itself Experimental and “not an accepted or official MCP extension.” Preserve this as unresolved upstream documentation disagreement. The README's linked discovery/schema Markdown paths were not found at its root; no missing document was fabricated.
- **Tasks:** the catalog says Beta-to-Core. A repository schema labeled Stable does not establish Stable extension lifecycle status. Its SDK README separately describes legacy receiver support; a published spec does not prove modern receiver implementation.
- **Skills:** the catalog and repository say Beta. The overview links some specification URLs under `specification/stable/`, while the pinned repository places the source of truth under `specification/beta/`. The captured Beta spec controls the detailed transport/integrity claims here. Final SEP status is not Stable extension status.
- **Support matrix:** blank cells in a rendered-text extraction are ambiguous. Use explicit implementation entries and verify the target host rather than interpreting every blank as unsupported.

## Popularity signals (if this source provides them)

- **Credibility:** normative material published by the MCP project, plus pinned extension-maintainer documentation; as-of 2026-11-04. No numerical adoption claim is inferred from the specification.
- **Attention:** no MCP-wide install/user total captured. The separate OpenAI repository source records its own stars; that is attention to one implementation, not MCP market share.

## Related sources

- [[sources/modelcontextprotocol--mcp-apps-docs]] — stable UI wire spec, SDK migration and draft additions.
- [[sources/modelcontextprotocol--mcp-authorization-docs]] — core OAuth and authorization extension specifications.
- [[sources/openai--mcp-extensions]] — concrete ChatGPT-specific extension spec, SDK and examples.
- [[sources/agentskills--specification]] — skill file format; distinct from MCP transport.
