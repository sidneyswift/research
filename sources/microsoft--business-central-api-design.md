---
domain: sources
type: docs-page
url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/
retrieved: 2026-11-04
snapshot-location: sources/microsoft--business-central-api-design/
version: "n/a (living documentation); captured 2026-11-04"
last-reviewed: 2026-11-04
---

# Business Central API design

> Primary evidence collection for [[artifacts/projects/business-central-api]] and [[projects/designing-apis-for-agents/README]].

## Snapshot details

- **Retrieved:** 2026-11-04.
- **Version boundary:** dated capture, not live API execution. API version constraints remain on individual captured pages.
- **Capture limits:** text/examples only, no diagrams relied on. Vendor guidance embedded in documentation is evidence, not authorization to install or operate anything.

| Anchor | Canonical document | Captured text | SHA-256 |
| --- | --- | --- | --- |
| `invoice` | [Sales invoice resource](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/resources/dynamics_salesinvoice) | [invoice.md](microsoft--business-central-api-design/invoice.md) | `5cf2f866fc00da6d90df96a48a8f113a7abce425b98de3715051dd3710fd23bf` |
| `update` | [Invoice update and If-Match](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoice_update) | [update.md](microsoft--business-central-api-design/update.md) | `af938a8bec26f8a69490406b33bd5df7fc20105379fc4598d5f6e0c061ff94dc` |
| `batch` | [Transactional batches](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/use-odata-batch) | [batch.md](microsoft--business-central-api-design/batch.md) | `1bd45206abe7e9feddbe0d7b78098489fb68e83554726ed13bb18c4b6db31080` |
| `webhooks` | [Webhook lifecycle](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/dynamics-subscriptions) | [webhooks.md](microsoft--business-central-api-design/webhooks.md) | `7455cd01ad5eba80e29b256cd8c4c8b764813f751bcab241cfd9169040e5c995` |
| `authorization` | [Service-to-service authentication](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/automation-apis-using-s2s-authentication) | [authorization.md](microsoft--business-central-api-design/authorization.md) | `b5a23a76145b0a65c66c313f363495d227a892bd4ccaa58c2d342d1ee5954a59` |

## Anchor map

- `#root` — full evidence collection; use a specific document anchor for factual claims.
- `#invoice` — captured `invoice.md`: Sales invoice resource; cite named sections in prose where needed.
- `#update` — captured `update.md`: Invoice update and If-Match; cite named sections in prose where needed.
- `#batch` — captured `batch.md`: Transactional batches; cite named sections in prose where needed.
- `#webhooks` — captured `webhooks.md`: Webhook lifecycle; cite named sections in prose where needed.
- `#authorization` — captured `authorization.md`: Service-to-service authentication; cite named sections in prose where needed.

## Why we cite this

[[artifacts/projects/business-central-api]] owns the interpretation; this page owns immutable evidence and retrieval details. Documentation is not implementation inspection or runtime verification.

## Popularity and credibility signals

- **Signal:** First-party documentation or author-published evaluation methodology; not an adoption measurement.
- **As-of:** 2026-11-04.
- No star/install/customer count or comparative performance ranking measured.

## Related sources

- [[projects/designing-apis-for-agents/README]] — research group and evidence map.
