---
domain: sources
type: docs-page
url: https://developers.openai.com/api/docs/guides/agents
retrieved: 2026-11-04
snapshot-location: sources/openai--agent-api-design/
version: "n/a (living documentation collection); retrieved 2026-11-04"
last-reviewed: 2026-11-04
---

# OpenAI agent and model API design — official documentation collection

> Ten official documentation snapshots covering model/tool contracts, state, asynchronous execution, managed agent sessions, and operational controls.

## Snapshot details

- **Retrieved:** 2026-11-04.
- **Version:** n/a (living pages). Claims are anchored to these captured bytes, not an unspecified future revision.
- **Capture:** official Markdown versions obtained by appending `.md` to the canonical URLs. Markdown snapshots are immutable evidence; no source code or API behavior was executed.
- **Scope:** Responses, function tools, Structured Outputs, background generation, webhooks, conversation state, Batch, general API compatibility, and the documented distinction between Agents API/SDK/Responses plus session configuration/review. Not an exhaustive platform review.
- **Limits:** text/schema/examples are preserved. Referenced diagram/image binaries were not downloaded; claims rely on text. Account availability, deployed behavior, provider internals, and agent success rates were not tested.

| Snapshot | Canonical URL | SHA-256 |
| --- | --- | --- |
| [function-calling.md](openai--agent-api-design/function-calling.md) | https://developers.openai.com/api/docs/guides/function-calling | `46d01db6895d007a8cd79806055ca44ea55ac88e3ffbfae80d14ec7dc8411f93` |
| [background.md](openai--agent-api-design/background.md) | https://developers.openai.com/api/docs/guides/background | `a2cbf609dd6dbd0cbc23369b06eed647fea8d8dd531fec736682ad65aed482e2` |
| [webhooks.md](openai--agent-api-design/webhooks.md) | https://developers.openai.com/api/docs/guides/webhooks | `f87cb4c61a8524418dbe5a28c84a8fec2a29baf7da08272dd6a867c1c5936d13` |
| [conversation-state.md](openai--agent-api-design/conversation-state.md) | https://developers.openai.com/api/docs/guides/conversation-state | `cbe2dd7fbc94538a5823ba4108e048789481cbca9628d832f347091d2c159702` |
| [batch.md](openai--agent-api-design/batch.md) | https://developers.openai.com/api/docs/guides/batch | `607bb7b751c050587de1bc8deac0d21de351145daaf19c1dfd8cbafc16b826af` |
| [overview.md](openai--agent-api-design/overview.md) | https://developers.openai.com/api/reference/overview | `a046d08b9f57f2d8e5e540c2a9ae201b93a6c64647679e81bea0eabe787f58b7` |
| [structured-outputs.md](openai--agent-api-design/structured-outputs.md) | https://developers.openai.com/api/docs/guides/structured-outputs | `dcd211d602a85c8573033559384424d6ebc86af73a844e752822ed868d82032b` |
| [agents.md](openai--agent-api-design/agents.md) | https://developers.openai.com/api/docs/guides/agents | `df4f61b609550619a3f9e445c66d28318b9f681affe1a819ef0098cde32bf43a` |
| [agents-configuration.md](openai--agent-api-design/agents-configuration.md) | https://developers.openai.com/api/docs/guides/agents-api/configuration | `3a283f0b0db9874a81250b3052b82e346d2c9dee9d1a290c0428fabcf8a2012e` |
| [automatic-review.md](openai--agent-api-design/automatic-review.md) | https://developers.openai.com/api/docs/guides/agents-api/sessions/approvals | `01e6c369740ca593c60aaf46ad9281b0e7242bc8fb16bcaa2aad62fba96c4eb7` |

## Anchor map

- `#root` — this complete captured documentation collection.
- `#function-loop` — [function-calling.md](openai--agent-api-design/function-calling.md), captured lines 18–107 and 598–676: Definitions, application-owned function execution, call IDs, and multi-call responses.
- `#tool-design` — [function-calling.md](openai--agent-api-design/function-calling.md), captured lines 478–596: Function descriptions, namespaces, deferred tool search, small initial tool sets, known arguments and cohesive sequences.
- `#strict-schema` — [function-calling.md](openai--agent-api-design/function-calling.md), captured lines 1082–1198: Parallel calls, strict-mode constraints, API-dependent defaults and supported-schema limits.
- `#background` — [background.md](openai--agent-api-design/background.md), captured lines 1–20, 140–164, 310–340, 402–425, 769–775: Same response creation with background flag; retrieve/poll/cancel, streaming resume cursor and retention limits.
- `#webhooks` — [webhooks.md](openai--agent-api-design/webhooks.md), captured lines 274–340: Event notifications, quick 2xx acknowledgement, 72-hour retry window, duplicates, signature verification.
- `#conversation` — [conversation-state.md](openai--agent-api-design/conversation-state.md), captured lines 434–452 and 723–741: Durable Conversation resource, distinct response retention, response chaining and token billing.
- `#batch` — [batch.md](openai--agent-api-design/batch.md), captured lines 25–43, 195–208, 393–408, 499–515, 684–696: Batch job lifecycle, custom request IDs, output files, unordered results, cancellation and expiration.
- `#compatibility` — [overview.md](openai--agent-api-design/overview.md), captured lines entire snapshot: Authentication, project context, request IDs, rate-limit headers, explicit client compatibility envelope and model-behavior caveat.
- `#structured-output-limits` — [structured-outputs.md](openai--agent-api-design/structured-outputs.md), captured lines 1–17, 296–347, 3619–3632, 4167, 4429–4451: Function-vs-output schemas, schema adherence versus content mistakes, refusal and incomplete output.
- `#agent-surfaces` — [agents.md](openai--agent-api-design/agents.md), captured lines entire snapshot: Managed Agents API versus application-owned SDK versus Responses; distinct session/conversation/sandbox resources.
- `#session-configuration` — [agents-configuration.md](openai--agent-api-design/agents-configuration.md), captured lines 164–202, 289–305, 451–509: Saved configuration copied into session, update/override semantics, immutable settings, environments, 409 review update precondition.
- `#review-boundary` — [automatic-review.md](openai--agent-api-design/automatic-review.md), captured lines 112–165: Reviewer model, review=none behavior, environment/sandbox prerequisites, network restrictions remain enforced.

## Why we cite this

Primary evidence for [[artifacts/projects/openai-agent-api]], [[concepts/business-platform-api-design]], and [[projects/designing-apis-for-agents/README]]. The documents specify several different ownership models; do not infer that all OpenAI APIs run a complete application workflow or enforce business authority.

## Popularity signals

- **Credibility signal:** official OpenAI developer documentation and API reference, captured 2026-11-04.
- **Popularity measurement:** none taken. No install count, benchmark, customer adoption, or demonstrated reliability claim is inferred from publication.

## Related sources

- [[sources/openai--plugins]] — separate plugin-distribution research; not interchangeable with API runtime contracts.
- [[sources/microsoft--async-request-reply]] — comparison point for explicit initiation/status/result contracts.
- [[sources/aws--idempotent-apis]] — comparison point for request-intent deduplication; an OpenAI client request ID is not documented here as an idempotency key.
