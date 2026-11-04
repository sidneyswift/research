---
domain: sources
type: docs-page
url: https://platform.claude.com/docs/en/api/overview
retrieved: 2026-11-04
snapshot-location: sources/anthropic--agent-api-design/
version: "n/a (living documentation); captured 2026-11-04; API reference displayed 2026-10-21"
last-reviewed: 2026-11-04
---

# Anthropic agent API design documentation

> A bounded capture of thirteen official Claude API documentation pages, covering model prompting, tool protocols, asynchronous batches, and the separate beta Managed Agents runtime.

## Snapshot details

- **Retrieved:** 2026-11-04.
- **Location:** `sources/anthropic--agent-api-design/`; each named Markdown file is an immutable rendered-text snapshot of one official page. The two JSON capture manifests record canonical URLs, character counts, and SHA-256 hashes.
- **Upstream identifier:** n/a (living documentation), fixed by captured text and hashes. Messages reference displays API version `2026-10-21`; Managed Agents is labeled beta with `managed-agents-2026-04-01`.
- **Capture method:** Direct HTTPS fetch of official documentation HTML, text extraction using BeautifulSoup, removal of structurally identifiable navigation/script/style. Text and examples support the claims; images and visual layout were not captured. Rendered text splits syntax-highlighted examples across lines.
- **Evidence boundary:** Documentation inspected; no authenticated API request, account access test, SDK execution, latency measurement, or permission bypass experiment. Docs are vendor assertions, not proof that all runtime guarantees hold.

## Anchor map

- `#root` — all thirteen captured official pages and their manifests.
- `#overview` — [overview.md](anthropic--agent-api-design/overview.md), available API categories, authentication/workspace/version headers, SDK handling, and cloud-platform variation. Canonical: https://platform.claude.com/docs/en/api/overview
- `#messages` — [messages.md](anthropic--agent-api-design/messages.md), `POST /v1/messages`, stateless conversation inputs, tools, content blocks, stop reasons. Canonical: https://platform.claude.com/docs/en/api/messages/create
- `#tool-definitions` — [define-tools.md](anthropic--agent-api-design/define-tools.md), user-defined names/descriptions/input schema, especially lines 175–217 on descriptions, consolidated actions, namespacing, and high-signal outputs. Canonical: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools
- `#tool-lifecycle` — [handle-tools.md](anthropic--agent-api-design/handle-tools.md), client/server dispatch, tool IDs and matching results, ordering, `is_error`, untrusted results. Canonical: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls
- `#strict-tools` — [strict-tools.md](anthropic--agent-api-design/strict-tools.md), `strict: true`, grammar-constrained schema conformance and supported-schema caveats. Canonical: https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use
- `#batches` — [batches.md](anthropic--agent-api-design/batches.md), batch creation/poll/results/cancel, independent requests, expiry/retention, `custom_id`, unordered results, four per-request outcomes. Canonical: https://platform.claude.com/docs/en/build-with-claude/batch-processing
- `#streaming` — [streaming.md](anthropic--agent-api-design/streaming.md), SSE event lifecycle, JSON input deltas, midstream errors, unknown event types, recovery limits. Canonical: https://platform.claude.com/docs/en/build-with-claude/streaming
- `#errors` — [errors.md](anthropic--agent-api-design/errors.md), HTTP errors, retries, post-200 SSE failure, request ID header/error body, request limits. Canonical: https://platform.claude.com/docs/en/api/errors
- `#versions` — [versions.md](anthropic--agent-api-design/versions.md), version header, additive output/enum evolution, explicit breaking-change history. Canonical: https://platform.claude.com/docs/en/api/versioning
- `#managed-runtime` — [managed-overview.md](anthropic--agent-api-design/managed-overview.md), Messages versus managed harness, four resource concepts, persisted events, beta/retention limits. Canonical: https://platform.claude.com/docs/en/managed-agents/overview
- `#managed-session-create` — [managed-sessions.md](anthropic--agent-api-design/managed-sessions.md), separate create/start versus `initial_events`, all-or-nothing initial validation/persistence, agent version pinning, overrides, budget boundaries. Canonical: https://platform.claude.com/docs/en/managed-agents/sessions
- `#managed-session-operations` — [managed-operations.md](anthropic--agent-api-design/managed-operations.md), session statuses, session-local updates, archive/delete, independent resource lifecycle, and `idle` not implying workflow completion. Canonical: https://platform.claude.com/docs/en/managed-agents/session-operations
- `#managed-permissions` — [managed-permissions.md](anthropic--agent-api-design/managed-permissions.md), server-tool policy versus custom-tool responsibility, allow/ask/auto, event provenance and untrusted end-user intent, policy evaluation metadata. Canonical: https://platform.claude.com/docs/en/managed-agents/permission-policies

## Why we cite this

Evidence for [[artifacts/projects/anthropic-agent-api]] and [[projects/designing-apis-for-agents/README]]. The collection shows how one frontier provider already exposes multiple lifecycle levels; no single endpoint shape represents every agent-facing capability.

## Popularity signals

- **Credibility signal:** Official Anthropic Claude Platform documentation, with endpoint schemas, concrete request/response examples, and stated lifecycle/compatibility contracts.
- **As-of:** 2026-11-04.
- No independent adoption or API usability measurement was taken. Official status is an authority signal, not a popularity claim.

## Related sources

- [[sources/google--aip-151]] — independent long-running-operation design guidance.
- [[sources/aws--idempotent-apis]] — external-effect retry guarantees require more than a model/tool protocol.
- [[sources/microsoft--async-request-reply]] — comparison with conventional asynchronous business processing.
