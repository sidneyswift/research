---
domain: sources
type: docs-page
url: https://docs.stripe.com/api
retrieved: 2026-11-04
snapshot-location: sources/stripe--business-api-design/
version: "n/a (living documentation); captured 2026-11-04"
last-reviewed: 2026-11-04
---

# Stripe intent, retry, and event API design

> Primary evidence collection for [[artifacts/projects/stripe-api]] and [[projects/designing-apis-for-agents/README]].

## Snapshot details

- **Retrieved:** 2026-11-04.
- **Version boundary:** dated capture, not live API execution. API version constraints remain on individual captured pages.
- **Capture limits:** text/examples only, no diagrams relied on. Vendor guidance embedded in documentation is evidence, not authorization to install or operate anything.

| Anchor | Canonical document | Captured text | SHA-256 |
| --- | --- | --- | --- |
| `intent` | [Payment and setup intent lifecycle](https://docs.stripe.com/payments/paymentintents/lifecycle.md) | [intent.md](stripe--business-api-design/intent.md) | `0745e651b44f89d5c069cefb09f75c687d7a0e9bb4c4838f6b83e3a745d0e45f` |
| `idempotency` | [Idempotent requests](https://docs.stripe.com/api/idempotent_requests.md) | [idempotency.md](stripe--business-api-design/idempotency.md) | `47bc3ff3d3f4243f84eb494166e59f11b16514dd4b117cb10c127d097c415eb4` |
| `v2` | [API v2 differences](https://docs.stripe.com/api-v2-overview.md) | [v2.md](stripe--business-api-design/v2.md) | `7504aaccd6f49fbfb1807d9f0755563d2d6a0ea309654ed9e5489406537573e9` |
| `webhooks` | [Webhooks](https://docs.stripe.com/webhooks.md) | [webhooks.md](stripe--business-api-design/webhooks.md) | `2e493959ac6b0e04740337d2406323fc6dfc930c481d03220c7db0e4829f992c` |
| `skills` | [Agent skills](https://docs.stripe.com/skills.md) | [skills.md](stripe--business-api-design/skills.md) | `c2085d6832e1b88baff67824affe831deff7a207e5258e5514c3e1a4c36eb825` |

## Anchor map

- `#root` — full evidence collection; use a specific document anchor for factual claims.
- `#intent` — captured `intent.md`: Payment and setup intent lifecycle; cite named sections in prose where needed.
- `#idempotency` — captured `idempotency.md`: Idempotent requests; cite named sections in prose where needed.
- `#v2` — captured `v2.md`: API v2 differences; cite named sections in prose where needed.
- `#webhooks` — captured `webhooks.md`: Webhooks; cite named sections in prose where needed.
- `#skills` — captured `skills.md`: Agent skills; cite named sections in prose where needed.

## Why we cite this

[[artifacts/projects/stripe-api]] owns the interpretation; this page owns immutable evidence and retrieval details. Documentation is not implementation inspection or runtime verification.

## Popularity and credibility signals

- **Signal:** First-party documentation or author-published evaluation methodology; not an adoption measurement.
- **As-of:** 2026-11-04.
- No star/install/customer count or comparative performance ranking measured.

## Related sources

- [[projects/designing-apis-for-agents/README]] — research group and evidence map.
