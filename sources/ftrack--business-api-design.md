---
domain: sources
type: docs-page
url: https://developer.ftrack.com/
retrieved: 2026-11-04
snapshot-location: sources/ftrack--business-api-design/
version: "n/a (living documentation); captured 2026-11-04"
last-reviewed: 2026-11-04
---

# ftrack API and Python client design

> Official documentation collection for [[artifacts/projects/ftrack-api]] and [[projects/designing-apis-for-agents/README]].

## Snapshot details

- **Retrieved:** 2026-11-04.
- **Version:** n/a (living documentation); capture date fixes the evidence studied. Documentation-specific version defaults are reported in the artifact where relevant, not asserted as universal API versions.
- **Capture method:** HTML rendered-text extraction, with navigation removed where structurally identifiable. Code token spacing may change; diagrams, interactive panels and layout are not reproduced. Some Cloudinary captures retain navigation, so the anchor map names the substantive section.
- **Evidence class:** documentation only. No authenticated provider API calls, SDK execution, production transactions, or behavioral evaluations.
- **Preservation:** immutable captured files; hashes below. Existing captures were not rewritten when extraction limitations were discovered.

| Snapshot | Canonical URL | SHA-256 |
| --- | --- | --- |
| [endpoint.md](ftrack--business-api-design/endpoint.md) | https://developer.ftrack.com/api/endpoint/index.html | `52af8b8898bf0d646a801b086291161132e8f3892f7751e940c8a47b9f469852` |
| [authentication.md](ftrack--business-api-design/authentication.md) | https://developer.ftrack.com/api/authentication/index.html | `b6243ab861bc480e091963a870ad125d4ae92ed97ceee6b51e4b0a52a1e62ca1` |
| [query.md](ftrack--business-api-design/query.md) | https://developer.ftrack.com/api/query-language/index.html | `9eb9238cff35eae1f06c34ce4a24501f8c83aee45525ff0967bb10328e3c025f` |
| [sessions.md](ftrack--business-api-design/sessions.md) | https://developer.ftrack.com/api-clients/python/understanding-sessions/index.html | `f9c26f51b7a33bda0ffd2d089f97e08988554c00565dd98284f3736fddb4e07a` |
| [entities.md](ftrack--business-api-design/entities.md) | https://developer.ftrack.com/api-clients/python/working-with-entities/index.html | `fc695a2006db912d5bd31334f1549046438f69d251a3feac5ab7fc1dfd7eb645` |
| [events.md](ftrack--business-api-design/events.md) | https://developer.ftrack.com/api-clients/python/handling-events/index.html | `f8b9c558ea6dec2df345ef61bf2c6341917cdbf7b9fc7a45f8ca1acf97fd19d9` |
| [jobs.md](ftrack--business-api-design/jobs.md) | https://developer.ftrack.com/api-clients/examples/job/index.html | `5d13e514f877764ceccaa1ad3d207688f00ef75110f3c846cbcc88883ff18fab` |

## Anchor map

- `#root` — the complete documentation collection.
- `#endpoint` — [endpoint.md](ftrack--business-api-design/endpoint.md), **Endpoint / Errors**: HTTP batch endpoint, payloads, per-batch server transaction and operational errors.
- `#authentication` — [authentication.md](ftrack--business-api-design/authentication.md), **Authentication / Personal API keys / Global API keys**: Personal versus global keys, roles and private-project access.
- `#query` — [query.md](ftrack--business-api-design/query.md), **Query language / Projections**: Entity query DSL, projections, relationships, filtering, ordering and limits.
- `#sessions` — [sessions.md](ftrack--business-api-design/sessions.md), **Understanding sessions / Unit of work / Auto-population / Entity types**: Unit of work, commit, on-demand queries, caching, auto-population and schema download.
- `#entities` — [entities.md](ftrack--business-api-design/entities.md), **Working with entities / Attributes**: Typed entities, attributes and local mutation semantics.
- `#events` — [events.md](ftrack--business-api-design/events.md), **Handling events / Subscribing to events / Publish synchronously**: Subscribe/publish, local synchronous handlers, replies and targets.
- `#jobs` — [jobs.md](ftrack--business-api-design/jobs.md), **Managing jobs / Attachments**: User-visible long-running Job status and attachments; no durable execution guarantee.

## Why we cite this

For concrete API structure and contract choices: query/data surfaces, business commands, asynchronous lifecycle, authority, and recovery/compatibility boundaries. A documented contract is not proof that a current tenant or integration enforces it correctly.

## Popularity signals

- **Credibility signal:** official vendor developer documentation at retrieval, 2026-11-04.
- No install, usage, popularity, or agent-performance count measured.

## Related sources

- [[sources/ietf--http-semantics]] — HTTP baseline; vendor-specific use of PUT, POST and error conventions may differ from normative semantics.
- [[sources/microsoft--async-request-reply]] — comparative long-running-operation model.
