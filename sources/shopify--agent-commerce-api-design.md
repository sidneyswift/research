---
domain: sources
type: docs-page
url: https://shopify.dev/docs/agents
retrieved: 2026-11-04
snapshot-location: sources/shopify--agent-commerce-api-design/
version: "n/a (living documentation); captured 2026-11-04; UCP examples use 2026-08-25"
last-reviewed: 2026-11-04
---

# Shopify agent-commerce API design evidence

> Nine official documentation captures for [[artifacts/projects/shopify-api]] and [[projects/designing-apis-for-agents/README]].

## Snapshot details

- **Retrieved:** 2026-11-04.
- **Scope:** UCP capability negotiation, discovery, catalog/cart/checkout/order boundaries, authentication tiers, server/browser tool surfaces, and developer-context tooling.
- **Version:** living docs fixed by capture date and hashes. Example protocol dates and tier/preview restrictions belong to the named captured pages, not a universal provider-wide guarantee.
- **Evidence class:** documentation inspected; no commerce calls, merchant/buyer access, toolkit installation, SDK execution, profile registration or checkout attempts.
- **Capture:** official Markdown endpoints; text extraction only if response is HTML. Diagram assets omitted; claims rely on text. The documentation's installation/action instructions are evidence, not authorization.

| Snapshot | Canonical URL | SHA-256 |
| --- | --- | --- |
| [overview.md](shopify--agent-commerce-api-design/overview.md) | https://shopify.dev/docs/agents | `48997ce483bb3931d58074111add299c225eae728556ba15e189af73cd555e6a` |
| [catalog.md](shopify--agent-commerce-api-design/catalog.md) | https://shopify.dev/docs/agents/catalog | `b0a40cbb125bbca02629ca230eab6eea7be26ae1be8ea8f9ec3552ab81145c96` |
| [profiles.md](shopify--agent-commerce-api-design/profiles.md) | https://shopify.dev/docs/agents/profiles | `ef4878de741094d9080addaa8d4320461449d7d07ebb6f7ec69b5cfc24a348f3` |
| [auth.md](shopify--agent-commerce-api-design/auth.md) | https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting | `1b246574ca2a6c2164c68293efcc5f517e48784c2cd22bd909ff2efbbaac4acc` |
| [cart.md](shopify--agent-commerce-api-design/cart.md) | https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp | `4b45cbb8048c8aaadc4819800b0f26232567f7b1c27c4b0f702ba7adfb868521` |
| [checkout.md](shopify--agent-commerce-api-design/checkout.md) | https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp | `4189cbc9ed84189f3e73632fbbfc783866ffd82dfd728d46fce28528fd3742c1` |
| [webmcp.md](shopify--agent-commerce-api-design/webmcp.md) | https://shopify.dev/docs/agents/carts-and-checkout/checkout-webmcp | `563051a872129b3cb6a221aca9b3f6d31645e9552bab8b6a38e429f7dd202682` |
| [orders.md](shopify--agent-commerce-api-design/orders.md) | https://shopify.dev/docs/agents/orders | `a14bbb975822e618797fd1ac8572ba405b6552ee5d1dc147e4c57cd57b523b27` |
| [toolkit.md](shopify--agent-commerce-api-design/toolkit.md) | https://shopify.dev/docs/apps/build/ai-toolkit | `14e889ef74a7095ce1eab2da9573e6d43c5d059d71d593ae5022212f4590e79e` |

## Anchor map

- `#root` — complete nine-document collection and capture manifest.
- `#overview` — `overview.md`: Agentic commerce; section details are named in citing prose.
- `#catalog` — `catalog.md`: Catalog interfaces; section details are named in citing prose.
- `#profiles` — `profiles.md`: Agent profiles and negotiation; section details are named in citing prose.
- `#auth` — `auth.md`: Authentication and rate limiting; section details are named in citing prose.
- `#cart` — `cart.md`: Cart MCP; section details are named in citing prose.
- `#checkout` — `checkout.md`: Checkout MCP; section details are named in citing prose.
- `#webmcp` — `webmcp.md`: Checkout WebMCP; section details are named in citing prose.
- `#orders` — `orders.md`: Order boundaries; section details are named in citing prose.
- `#toolkit` — `toolkit.md`: AI Toolkit; section details are named in citing prose.

## Why we cite this

[[artifacts/projects/shopify-api]] owns findings and extraction; [[analyses/frontier-and-business-api-design]] places Shopify alongside model providers and other business APIs. Shopify's Admin and commerce-agent APIs have different audiences, identities and effect contracts.

## Popularity and credibility signals

- **Credibility:** first-party Shopify developer documentation as-of 2026-11-04.
- No adoption, comparative agent performance, production availability or enforcement measurement. “Agent-forward” is supported here by published agent interfaces and development tooling, not an inferred success rate.

## Related sources

- [[sources/shopify--admin-api-design]] — business/Admin API companion study.
- [[sources/stripe--business-api-design]] — separate business intent, payment and event comparison.
