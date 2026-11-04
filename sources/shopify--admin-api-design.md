---
domain: sources
type: docs-page
url: https://shopify.dev/docs/api/admin-graphql/2026-10
retrieved: 2026-11-04
snapshot-location: sources/shopify--admin-api-design/
version: "GraphQL Admin reference displays 2026-10; other pages are living cross-version documentation captured 2026-11-04"
last-reviewed: 2026-11-04
---

# Shopify Admin API design — official documentation collection

> Seven primary documentation snapshots covering GraphQL's error layers, asynchronous bulk reads, scoped idempotency contracts, API evolution, and granted access.

## Snapshot details

- **Retrieved:** 2026-11-04.
- **Method:** official Markdown endpoints, captured byte-for-byte without source edits; capture URLs, byte counts and hashes in [capture-manifest.json](shopify--admin-api-design/capture-manifest.json).
- **Version:** `overview.md` frontmatter explicitly identifies `api_version: 2026-10`. The requested dated reference maps internally to `latest` in its `source_url`; the captured bytes and explicit version are the evidence, not an enduring assumption about the latest alias. Other pages contain cross-version guidance rather than one pinned API schema.
- **Boundary:** Documentation inspected, not API/SDK execution or implementation inspection. No app installation, token acquisition, shop access, mutations, webhooks or commerce transactions performed. Embedded setup instructions were treated as evidence, not authorization.
- **Capture limits:** Text/schema/examples preserved; diagrams and images are not used as evidence. This is a sampled Admin/API usage study, not an exhaustive Shopify platform audit.

| Snapshot | Canonical document requested | SHA-256 |
| --- | --- | --- |
| [overview.md](shopify--admin-api-design/overview.md) | https://shopify.dev/docs/api/admin-graphql/2026-10 | `cca75e775d45a31f7bbc0e1281e70c0e8e3a9cfcaf6a318d294d30cfa3dcc599` |
| [bulk.md](shopify--admin-api-design/bulk.md) | https://shopify.dev/docs/apps/build/apis/graphql-admin/bulk-operations/queries | `1d567deee10fbcfe9cd38325355a7e2e1532f7bdcd400f0d2273e97c30d5c71e` |
| [idempotency.md](shopify--admin-api-design/idempotency.md) | https://shopify.dev/docs/api/usage/idempotent-requests | `ab3fd92496a5cf03f749e6f10916c9b3a3fa7ce262c385d2abec4f3754df1e7b` |
| [idempotency-implementation.md](shopify--admin-api-design/idempotency-implementation.md) | https://shopify.dev/docs/apps/build/apis/graphql-admin/implementing-idempotency | `2fad8cda843af533b28f70576d16ee7c37afbfa07b22f59a89bc0a78138a403d` |
| [versioning.md](shopify--admin-api-design/versioning.md) | https://shopify.dev/docs/api/usage/versioning | `c02c3156f46b479c79c184979239a7853d6872ff3d005eebbe562b93186d85b9` |
| [errors.md](shopify--admin-api-design/errors.md) | https://shopify.dev/docs/api/usage/response-codes | `efc7fac683975aca956fe01543c668891772fa78e1636ce4b738c2925e106a44` |
| [scopes.md](shopify--admin-api-design/scopes.md) | https://shopify.dev/docs/api/usage/access-scopes | `07f0fdb877e9f9090cfcd24bc1ee1e31044a88fdcdd2929e988bca96daae9ad1` |

## Anchor map

- `#root` — the complete seven-document collection.
- `#overview` — [overview.md](shopify--admin-api-design/overview.md): Authentication; Endpoints and queries; Rate limits; Status and error codes; HTTP 200, top-level errors, and explicitly selected mutation `userErrors`.
- `#bulk` — [bulk.md](shopify--admin-api-design/bulk.md): Limitations; Bulk query workflow; Wait for operation; Download result data; Operation failures; Canceling an operation; Rate limits. Distinguishes initiation by mutation, asynchronous query, result/partial result, webhook finish, and per-version behavior.
- `#idempotency` — [idempotency.md](shopify--admin-api-design/idempotency.md): General key mechanics; mutation argument versus `@idempotent` directive; per-row protection for bulk mutations. The mutation description owns support; this is not blanket coverage of every call.
- `#idempotency-implementation` — [idempotency-implementation.md](shopify--admin-api-design/idempotency-implementation.md): Scope disclaimer; intent versus identical arguments; 24-hour retention; concurrent/mismatched requests; cached response caveat; persistence and bulk rows; listed supporting mutations.
- `#versioning` — [versioning.md](shopify--admin-api-design/versioning.md): Versioned versus unversioned APIs; quarterly releases; support overlap; fall-forward; actual-version header; release candidate/unstable and deprecation policy. Catalog is listed as unversioned; Admin's policy must not be projected onto every agent-facing surface.
- `#errors` — [errors.md](shopify--admin-api-design/errors.md): GraphQL body errors versus HTTP transport codes; API-specific error codes; throttling/access denied can be HTTP 200. Read together with mutation `userErrors` in `#overview`.
- `#scopes` — [scopes.md](shopify--admin-api-design/scopes.md): Scope types; per-resource permissions; order/protected-customer constraints; declared versus actually granted scopes and `currentAppInstallation.accessScopes`.

## Why we cite this

Evidence for [[artifacts/projects/shopify-api]], [[analyses/frontier-and-business-api-design]] and [[projects/designing-apis-for-agents/README]]. These contracts support comparisons between established business capabilities and agent-facing adapters; they do not establish that agents can use Shopify correctly or that a particular store/account grants access.

## Popularity and credibility signals

- **Signal:** official Shopify developer reference and guides, with typed examples, explicit errors/lifecycle and version statements.
- **As-of:** 2026-11-04.
- No install, adoption, usability, performance, or agent-success count measured.

## Related sources

- [[sources/shopify--agent-commerce-api-design]] — complementary agent/UCP documentation; keep its authentication/version/authority contracts separate.
- [[sources/ietf--http-semantics]] — normative HTTP concepts are distinct from GraphQL operation semantics and provider-specific implementation guarantees.
- [[sources/aws--idempotent-apis]] — comparison of caller intent and effect deduplication; Shopify's named scopes/windows remain provider-specific.

## Documentation tensions and extraction notes

- The bulk guide prints example endpoint URLs under `/api/{api_version}/graphql.json`, while the Admin overview uses `/admin/api/2026-10/graphql.json`. This collection preserves both; use the explicit Admin reference for implementation and verify the relevant surface rather than propagating the example shorthand blindly.
- The response-codes guide describes operation failures inside HTTP 200 but also documents genuine transport/account/server non-200 failures. Do not collapse this into a claim that every GraphQL request always returns 200.
- The general idempotency page describes common update/delete behavior, then names exceptions with additional non-idempotent effects. Support/error/window details must be read at the particular mutation and mechanism; never infer them from the HTTP verb or mutation name alone.
