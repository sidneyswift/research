---
domain: sources
type: docs-page
url: https://vercel.com/docs/schedules
retrieved: 2026-11-06
snapshot-location: sources/vercel--schedules-docs/
last-reviewed: 2026-11-06
---

# Vercel Schedules — bounded documentation collection

> Static/dynamic schedules, delivery and cancellation semantics, environment ownership, SDK/API controls, Queues and experimental eve integration.

## Snapshot details

- **Version:** public-beta documentation as retrieved 2026-11-06; no backend build or installed SDK version inspected. Several pages carry an implausible `last_updated: 2018-10-20` field; that is preserved metadata, not the launch date.
- **Evidence:** seventeen immutable readable captures; [SHA-256/byte receipt](vercel--schedules-docs/capture.json) records canonical/final URLs, timestamps, extraction type and read scope. [Coverage manifest](vercel--schedules-docs/coverage.json) lists announcement links, failed guessed routes, and unvisited integrations/navigation.
- **Reviewed:** full announcement separately; full schedules overview, configuration, handlers, management, SDK, HTTP API, limits, local development, migration, tenancy, eve dynamic schedules, linked skill, beta changelog, Queues overview and discovery index. Queues concepts read at the explicit delivery/recovery/versioning sections listed in the receipt.
- **Retrieval limits:** `llms.txt` inspected; full corpus fetch timed out, so this is a scoped collection, not an exhaustive Vercel-site read. Full spill files used for eve and Queues concepts, not truncated tool previews. Relative links, tables and code preserved as returned; link-base interpretation uses each canonical URL. No visual/rendered or interactive behavior asserted.
- **Execution limits:** no scheduling skill installed, no schedule created, no deployment or runtime test. The skill is captured source material—not instructions to operate the user's account.

## Capture inventory

| File | Primary source / reading role |
| --- | --- |
| [schedules](vercel--schedules-docs/schedules.md) | https://vercel.com/docs/schedules — Full captured text |
| [sdk](vercel--schedules-docs/sdk.md) | https://vercel.com/docs/schedules/sdk — Full captured text |
| [http-api](vercel--schedules-docs/http-api.md) | https://vercel.com/docs/schedules/http-api — Full captured text |
| [queues](vercel--schedules-docs/queues.md) | https://vercel.com/docs/queues — Full captured text |
| [eve-dynamic](vercel--schedules-docs/eve-dynamic.md) | https://eve.dev/docs/experimental/dynamic-schedules — Full captured text |
| [skill](vercel--schedules-docs/skill.md) | https://raw.githubusercontent.com/vercel/vercel-plugin/main/skills/vercel-schedules/SKILL.md — Full captured text |
| [llms](vercel--schedules-docs/llms.md) | https://vercel.com/llms.txt — Full captured text |
| [configuration](vercel--schedules-docs/configuration.md) | https://vercel.com/docs/schedules/configuration — Full captured text |
| [handle-runs](vercel--schedules-docs/handle-runs.md) | https://vercel.com/docs/schedules/handle-runs — Full captured text |
| [manage](vercel--schedules-docs/manage.md) | https://vercel.com/docs/schedules/manage — Full captured text |
| [local-development](vercel--schedules-docs/local-development.md) | https://vercel.com/docs/schedules/local-development — Full captured text |
| [concepts](vercel--schedules-docs/concepts.md) | https://vercel.com/docs/schedules/concepts — Full captured text |
| [limits](vercel--schedules-docs/limits.md) | https://vercel.com/docs/schedules/limits — Full captured text |
| [multi-tenant](vercel--schedules-docs/multi-tenant.md) | https://vercel.com/docs/schedules/multi-tenant — Full captured text |
| [migration](vercel--schedules-docs/migration.md) | https://vercel.com/docs/schedules/migrate-from-cron-jobs — Full captured text |
| [queue-concepts](vercel--schedules-docs/queue-concepts.md) | https://vercel.com/docs/queues/concepts — Selected sections: durability, at-least-once, visibility, lifecycle, residency/failover, deployments, delayed delivery, idempotency, retries, ordering |
| [beta](vercel--schedules-docs/beta.md) | https://vercel.com/changelog/vercel-schedules-is-now-in-public-beta — Full captured text |

## Anchor map

### root

Product boundary, static versus dynamic resource model and public-beta status. [Captured source](vercel--schedules-docs/schedules.md).

### configuration

Exactly one target; build-output function identifiers; trigger exclusivity; static/dynamic name collision behavior and single-time syntax. [Captured source](vercel--schedules-docs/configuration.md).

### deployment

Current deployment routing, rollback/static reconciliation, environment identity and state persistence. [Captured source](vercel--schedules-docs/concepts.md).

### timing

IANA timezone, jitter, overlap, late-occurrence expiry, catch-up bursts and one-time lifecycle. [Captured source](vercel--schedules-docs/concepts.md).

### targets

Private function, public path and queue targets; retries differ by target. [Captured source](vercel--schedules-docs/handle-runs.md).

### event-auth

Metadata parsing is not CRON_SECRET validation on public paths; private triggers have a different trust boundary. [Captured source](vercel--schedules-docs/handle-runs.md).

### dedupe

Occurrence executionId is stable across repeated delivery; handler side effects still need idempotence. [Captured source](vercel--schedules-docs/handle-runs.md).

### lifecycle

Temporary enablement, manual invocation, deletion cutoff, branch cleanup, one-time dispatch races and 90-day history. [Captured source](vercel--schedules-docs/manage.md).

### environments

SDK deployment-bound scope versus production-default CLI; dynamic schedules active in every environment; static Preview default inactive. [Captured source](vercel--schedules-docs/manage.md).

### observability

Metrics cover recorded outcomes only; missing outcomes are excluded, not counted as success. [Captured source](vercel--schedules-docs/manage.md).

### sdk

Client/import-time configuration, explicit fields, null-versus-omission semantics, fixed expression type, pagination and errors. [Captured source](vercel--schedules-docs/sdk.md).

### api

OIDC/access-token authority, HTTP-only optional name, payload omission from reads, strict object input and acceptance semantics. [Captured source](vercel--schedules-docs/http-api.md).

### retry-boundary

Writes may apply before 503; name-based create/delete reconciliation versus non-idempotent invoke, which starts a new run per request. [Captured source](vercel--schedules-docs/http-api.md).

### tenancy

Namespace mapping, shared consumer routing, cursor-complete cleanup and one-time deletion exception. [Captured source](vercel--schedules-docs/multi-tenant.md).

### limits

Plan-specific count/frequency/rate limits, destructive downgrade behavior, payload size and downstream resource usage. [Captured source](vercel--schedules-docs/limits.md).

### local

Session-local state, no production fallback for --local, unsupported service targets and local DST restrictions; quotas not fully simulated. [Captured source](vercel--schedules-docs/local-development.md).

### migration

GET-preserving transition, remove crons in same change, jitter differences, keep stable names and optional private target conversion. [Captured source](vercel--schedules-docs/migration.md).

### queue-contract

At-least-once/TTL, leases, retries/maxDeliveries, no FIFO and no built-in DLQ; examined contract sections only. [Captured source](vercel--schedules-docs/queue-concepts.md).

### queue-versioning

Default push queues bind to publishing deployment; promotion/rollback does not drain old consumers; polling differs. [Captured source](vercel--schedules-docs/queue-concepts.md).

### queue-dedupe

Publish dedupe window min(retention,24h), out-of-band filtering and independent at-least-once consumer semantics. [Captured source](vercel--schedules-docs/queue-concepts.md).

### queue-residency

Selected region may temporarily fail over to a neighboring region; strict residency not supported in captured docs. [Captured source](vercel--schedules-docs/queue-concepts.md).

### workflow-boundary

Queue transport is distinct from stateful workflow steps and agent-session recovery. [Captured source](vercel--schedules-docs/queues.md).

### eve-identity

Creator references, required current-access auth, principal scope, no app-identity fallback and invoke-as-creator. [Captured source](vercel--schedules-docs/eve-dynamic.md).

### eve-tools

Separate operations/schemas/approval rules; direct/deferred/code-only tools, client calls versus model approval, unattended sessions. [Captured source](vercel--schedules-docs/eve-dynamic.md).

### eve-payload

Preparation before approval and before write, changed-preparation rejection, payload replacement changing creator, destination authorization and prepared-data validation. [Captured source](vercel--schedules-docs/eve-dynamic.md).

### eve-occurrence

Callback dispatch versus agent completion, retries including event-handler failure, execution-keyed session dedupe and experimental local/provider limits. [Captured source](vercel--schedules-docs/eve-dynamic.md).

### skill

Captured authoring/routing guidance, path/import/bash/prompt selectors and exclusions; no install or efficacy test. [Captured source](vercel--schedules-docs/skill.md).

### beta

November 5 public-beta announcement; price statements and examples are time-bound published claims. [Captured source](vercel--schedules-docs/beta.md).

### documentation-conflicts

- **Payload:** skill says ≤8 KB; Schedules SDK, HTTP API and limits say 16 KB. Use the current service-specific reference for planning, and verify the deployed limit; do not silently rewrite the skill capture.
- **Static count:** skill generalizes “up to 100” to a project; limits scope 100 static declarations to Hobby deployments. Other plan capacities are separately documented.
- **Function path:** beta changelog uses `function: api/cleanup.ts`; configuration guide explicitly requires build-output ID without source extension, e.g. `api/cleanup`. The requested blog uses the latter. No build was run to settle implementation behavior.
- **Path preference:** skill says path is only for migration; handler docs also allow routes that must stay public. The skill is an opinionated default, not a platform restriction.
- **Queue publish dedupe:** overview says retention-period dedupe; detailed concepts cap it at 24 hours. Treat the narrower documented window as the design bound, not permanent exactly-once processing.
- **SDK versus HTTP:** SDK requires `name` and accepts `target: { topic }`; HTTP can generate a name and documents `{ type: queue, topic }`. Preserve surface-specific contracts.
- **eve versus platform:** eve documents a 64 KB prepared-write bound; Vercel Schedules documents 16 KB payloads. Different envelopes/provider layers—do not assume 64 KB can pass the hosted provider. eve's completed-state vocabulary is also not the platform's two-state lifecycle.
- **Version routing:** Schedules chooses current environment deployment; generic push Queues pins messages to their publishing deployment. These are different stages, not a universal “always latest code” guarantee. Exact promotion/dispatch races were not exercised.

## Why we cite this

Primary documentation for [[artifacts/projects/vercel-schedules]]; authored runtime contracts and integration guidance, not backend source verification. Reading an SDK reference or skill does not prove the platform honors every contract.

## Popularity signals

Public beta on all plans per November 5 changelog. No usage, reliability, latency or agent-success benchmark captured. Changelog advertises pricing starting at $5 per million runs and $10 per million creations for Pro/Enterprise; target compute/queue consumption is separate and this is not a live cost estimate.

## Related sources

- [[sources/vercel--introducing-schedules]] — requested announcement, captured separately.
- [[sources/vercel--eve]] — historical eve source study, not silently updated by this later experimental guide.
