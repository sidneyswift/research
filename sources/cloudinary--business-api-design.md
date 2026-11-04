---
domain: sources
type: docs-page
url: https://cloudinary.com/documentation/
retrieved: 2026-11-04
snapshot-location: sources/cloudinary--business-api-design/
version: "n/a (living documentation); captured 2026-11-04"
last-reviewed: 2026-11-04
---

# Cloudinary media/DAM API design

> Official documentation collection for [[artifacts/projects/cloudinary-api]] and [[projects/designing-apis-for-agents/README]].

## Snapshot details

- **Retrieved:** 2026-11-04.
- **Version:** n/a (living documentation); capture date fixes the evidence studied. Documentation-specific version defaults are reported in the artifact where relevant, not asserted as universal API versions.
- **Capture method:** HTML rendered-text extraction, with navigation removed where structurally identifiable. Code token spacing may change; diagrams, interactive panels and layout are not reproduced. Some Cloudinary captures retain navigation, so the anchor map names the substantive section.
- **Evidence class:** documentation only. No authenticated provider API calls, SDK execution, production transactions, or behavioral evaluations.
- **Preservation:** immutable captured files; hashes below. Existing captures were not rewritten when extraction limitations were discovered.

| Snapshot | Canonical URL | SHA-256 |
| --- | --- | --- |
| [admin.md](cloudinary--business-api-design/admin.md) | https://cloudinary.com/documentation/admin_api | `35efe1f96c8840ba56a6543844f8b55a3eae8f9a47022850bfc7d96fc0a135cb` |
| [search.md](cloudinary--business-api-design/search.md) | https://cloudinary.com/documentation/search_method | `c3e04295e8d2386f5d12b0add055b6d6c52c927df2a043070de8ac74058dcd04` |
| [processing.md](cloudinary--business-api-design/processing.md) | https://cloudinary.com/documentation/upload_parameters_processing | `609da0394f82c020ac0136616c07d74cb6fabfc21ceb5306cb69dd4c3e26ea6e` |
| [notifications.md](cloudinary--business-api-design/notifications.md) | https://cloudinary.com/documentation/notifications | `dbada60aeb02a2db1c1f9ffaa7e084df75ed370a4551d12936f6aa40d878080d` |
| [identity.md](cloudinary--business-api-design/identity.md) | https://cloudinary.com/documentation/ts_asset_id_vs_public_id | `14b898186aa83d8a347628c089b9aa24c587ab23b4100734c226e10cb159cde3` |

## Anchor map

- `#root` — the complete documentation collection.
- `#admin` — [admin.md](cloudinary--business-api-design/admin.md), **Admin API reference / Overview / Error handling / Usage limits**: Asset administration, authentication, errors, usage limits, pagination and response compatibility.
- `#search` — [search.md](cloudinary--business-api-design/search.md), **Search API method / Search method / Search examples**: Query expressions, projections, sorting and cursor-based result retrieval.
- `#processing` — [processing.md](cloudinary--business-api-design/processing.md), **Post-upload processing / Requesting asynchronous uploads / Eager asynchronous transformations**: Upload versus post-upload processing; async and eager_async completion boundaries.
- `#notifications` — [notifications.md](cloudinary--business-api-design/notifications.md), **Webhook notifications / Verifying notification signatures / Retry policy**: Notification delivery, signatures, retries and payload evolution.
- `#identity` — [identity.md](cloudinary--business-api-design/identity.md), **Asset ID vs public ID / How the two identifiers differ / When to use each identifier**: Mutable delivery public ID versus immutable asset ID and display label.

## Why we cite this

For concrete API structure and contract choices: query/data surfaces, business commands, asynchronous lifecycle, authority, and recovery/compatibility boundaries. A documented contract is not proof that a current tenant or integration enforces it correctly.

## Popularity signals

- **Credibility signal:** official vendor developer documentation at retrieval, 2026-11-04.
- No install, usage, popularity, or agent-performance count measured.

## Related sources

- [[sources/ietf--http-semantics]] — HTTP baseline; vendor-specific use of PUT, POST and error conventions may differ from normative semantics.
- [[sources/microsoft--async-request-reply]] — comparative long-running-operation model.
