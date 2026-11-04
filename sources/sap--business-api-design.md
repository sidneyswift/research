---
domain: sources
type: docs-page
url: https://help.sap.com/docs/SAP_S4HANA_CLOUD/03c04db2a7434731b7fe21dca77440da/3bac8c01d7024ae1b15cf848ce12544e.html
retrieved: 2026-11-04
snapshot-location: sources/sap--business-api-design/
version: "APIs for Sales, SAP S/4HANA Cloud Public Edition 2608 Latest"
last-reviewed: 2026-11-04
---

# SAP S/4HANA sales API design evidence

## Snapshot details

- **Retrieved:** 2026-11-04, SAP Help Portal, English, visible version 2608 Latest.
- **Capture:** browser-rendered article excerpts; static HTTP/browser search fetches returned empty JavaScript shells. The excerpts explicitly mark omitted material; no collapsed example or uninspected implementation claim is supported.
- **Files:** [update](sap--business-api-design/update.md), [async](sap--business-api-design/async.md), [simulation](sap--business-api-design/simulation.md). Canonical URLs are retained in each immutable file.
- **Scope:** Update and async pages concern Sales Order A2X OData V4; simulation page concerns A2X OData V2. These are not interchangeable versions of one exact endpoint.

## Anchor map

- `#root` — full three-page evidence collection.
- `#update` — `update.md`, PATCH keys, ETag preconditions, initial values and response projection.
- `#async` — `async.md`, `prefer: respond-async` and location-based response retrieval.
- `#simulation` — `simulation.md`, unsaved simulation, requested checks, metadata and limitations.

## Why we cite this

[[artifacts/projects/sap-sales-api]] distinguishes preview, mutation, response projection and deferred execution in an established ERP API. [[analyses/frontier-and-business-api-design]] compares those contracts with agent APIs.

## Popularity and credibility signals

- **Signal:** first-party SAP Help Portal product documentation, not measured adoption or model familiarity.
- **As-of:** 2026-11-04.
- No runtime requests or configuration changes performed.

## Related sources

- [[sources/microsoft--business-central-api-design]] — another ERP's action and transactional boundaries.
- [[projects/designing-apis-for-agents/README]] — research group.
