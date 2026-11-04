# Authentication and rate limiting

Canonical URL: https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting
Retrieved: 2026-11-04
Capture URL: https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting.md
Capture: official Markdown (or text extraction if HTML); no diagram-dependent claims.

---

---
title: Auth and rate limiting
description: >-
  Learn how UCP traffic is classified into token, signed, and anonymous
  requests, and what each tier can do across Catalog MCP, Cart MCP, Checkout
  MCP, and Order MCP.
source_url:
  html: 'https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting'
  md: 'https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting.md'
---

# Auth and rate limiting

UCP traffic to Shopify's MCP servers is classified into three tiers based on how your agent identifies itself. Each tier has different capabilities and rate-limiting allowances.

***

## Traffic tiers

Each tier reflects how much Shopify knows about the agent making the request. Stronger identification means higher rate limits and access to more sensitive tools.

The following table summarizes what each tier can do. Subsequent sections describe how to qualify for each tier.

| Auth type | [Catalog tools](https://shopify.dev/docs/agents/catalog) | [Cart tools](https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp) | [Checkout tools](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp) | [`complete_checkout`](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp#complete_checkout) | [Order tools](https://shopify.dev/docs/agents/orders/order-mcp) |
| - | - | - | - | - | - |
| [Token](#token) | Yes, and provides personalized search results when presenting a [buyer-linked token](#buyer-linked-tokens) | Yes | Yes, and applies any automatic discounts when presenting a [buyer-linked token](#buyer-linked-tokens) | When the token is granted permission to complete purchases | Yes, with the `read_global_api_orders` scope |
| [Signed](#signed) | Yes | Yes | Yes | No | No |
| [Anonymous](#anonymous) | Yes | Yes | Yes | No | No |

Rate-limit guidance:

* **Rate limits scale with identification.** The Token tier gets the highest limits, Signed gets lower limits, and Anonymous gets the lowest.
* **Checkout MCP is rate-limited more strictly than Cart MCP at every tier.** Use [Cart MCP](https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp) to iterate on line items, refine context, and estimate totals, and reserve [Checkout MCP](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp) for buyers who are ready to purchase.
* **Order MCP is for on-demand reads.** Reserve [`get_order`](https://shopify.dev/docs/agents/orders/order-mcp#get_order) for buyer-initiated views and reconciling missed webhooks. For proactive lifecycle updates, subscribe to [Order webhooks](https://shopify.dev/docs/agents/orders/order-webhooks).

***

## Global Catalog rate limits

Authenticated requests to the [Global Catalog](https://shopify.dev/docs/agents/catalog/global-catalog) endpoint, `https://catalog.shopify.com/api/ucp/mcp`, are rate limited for each API client. The default limit is 5 requests each second for each API client.

The following Catalog tools share the same quota:

* [`search_catalog`](https://shopify.dev/docs/agents/catalog/global-catalog#search_catalog)
* [`get_product`](https://shopify.dev/docs/agents/catalog/global-catalog#get_product)
* [`lookup_catalog`](https://shopify.dev/docs/agents/catalog/global-catalog#lookup_catalog)

These limits apply only to the Global Catalog. [Storefront Catalog](https://shopify.dev/docs/agents/catalog/storefront-catalog) requests to a store's `/api/ucp/mcp` endpoint use the same tool names, but they're rate limited separately for each store.

Unauthenticated requests are rate limited for each IP address and also share a single limit with all other unauthenticated traffic, so their throughput isn't guaranteed. Don't use unauthenticated requests for production traffic.

If your integration needs a higher request rate, then contact your Shopify representative or partner contact. If you don't have a Shopify contact, then go to the [Shopify Help Center](https://help.shopify.com/en/partners/help-support/getting-support#contacting-shopify-support). Include your API client, expected traffic, and business reason.

***

## Token

Agents authenticating with a credential issued through [Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard), such as a global API token, customer accounts token, or shop access token.

* **How to authenticate:** JWT passed with Bearer token authentication. See [Authenticate your agent](https://shopify.dev/docs/agents/get-started/authentication) for a working example.
* **What you can do:** Access cart, checkout, and order tools at the highest rate limits. Call [`complete_checkout`](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp#complete_checkout) when your token has been granted the required permission to complete purchases on the shop's behalf. Call [`get_order`](https://shopify.dev/docs/agents/orders/order-mcp#get_order) when your token includes the `read_global_api_orders` scope. Order access is restricted to orders placed through your agent.
* **What you must send:** A [`Shopify-Buyer-IP` header](#buyer-ip-header) on every `tools/call` request to a merchant's UCP MCP endpoint.

### Buyer-linked tokens

Buyer-linked tokens carry a signed-in Shop customer's identity. Pass a buyer-linked token to make your calls buyer-aware. For example, use one to return [personalized search results](https://shopify.dev/docs/agents/catalog/global-catalog) from the Global Catalog, or to sign in the buyer to the merchant store.

If your agent already holds a [Shop](https://shop.app) access token for a signed-in customer, it can [exchange that token for a buyer-linked token](https://shopify.dev/docs/agents/profiles/buyer-linked-tokens) without a second browser redirect using the UCP delegated identity provider (IdP) flow with Shop as the IdP.

***

## Signed

Agents that haven't created an API key but have implemented HTTP signatures per the UCP specification.

* **How to authenticate:** HTTP Message Signatures per [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) using ECDSA P-256. Shopify verifies the signature against the public key published in your agent's [well-known UCP profile](https://ucp.dev/2026-08-25/specification/overview/). See the [UCP signatures specification](https://ucp.dev/2026-08-25/specification/signatures/) for how to construct signed requests.
* **What you can do:** Access cart and checkout tools at lower rate limits than the Token tier. `complete_checkout` and order tools aren't available at this tier.

***

## Anonymous

Agents that haven't identified themselves to Shopify.

* **How to authenticate:** No credentials or signatures provided. Send the request without an `Authorization` header or signature headers.
* **What you can do:** Access catalog, cart, and checkout build/edit tools at the lowest rate limits. `complete_checkout` and order tools aren't available at this tier.

***

## Buyer IP header

A Token-tier request acts for a specific buyer, so Shopify needs that buyer's IP address. Send it in the `Shopify-Buyer-IP` header on every `tools/call` request to a merchant's UCP MCP endpoint, `https://{shop-domain}/api/ucp/mcp`. That endpoint serves Storefront Catalog, Cart MCP, Checkout MCP, and Order MCP. Global Catalog requests don't need the header.

* **What to send:** The IPv4 or IPv6 address of the buyer your agent is acting for.
* **When it's required:** On every Token-tier `tools/call`, including read-only calls such as `get_cart` and `get_order`. Discovery requests such as `initialize` and `tools/list` don't need it, and neither do Signed or Anonymous requests.
* **When you don't have one:** There's no placeholder value, and Shopify doesn't fall back to the address your agent connects from. If your agent makes a Token-tier `tools/call` when no buyer is present, such as from a scheduled job, then the call fails.

If the header is missing or isn't a valid IP address, then Shopify rejects the request with HTTP `422`:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32000,
    "message": "AuthenticationFailed",
    "data": "Missing required buyer IP header."
  }
}
```

***

## Rate-limit responses

When your traffic exceeds the allowance for its tier, Shopify returns HTTP `429` with a `Retry-After` header. For merchant UCP MCP endpoints, the response body looks like this:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32000,
    "message": "Rate limit exceeded",
    "data": "Too many requests, please retry after 30 seconds"
  }
}
```

Wait the number of seconds in `Retry-After`, then retry with exponential backoff and jitter. When you retry a call that takes `meta["idempotency-key"]`, such as `complete_checkout`, reuse the key from the original request so the retry doesn't repeat the action.

On merchant UCP MCP endpoints, allowances differ by tier and by tool and can change, so read `Retry-After` from each `429` response instead of hard-coding a request budget.

***

## Next steps

[Authenticate your agent\
\
](https://shopify.dev/docs/agents/get-started/authentication)

[Generate API credentials and fetch bearer tokens at runtime.](https://shopify.dev/docs/agents/get-started/authentication)

[Define a profile\
\
](https://shopify.dev/docs/agents/get-started/profile)

[Host a UCP profile at a well-known URL for capability negotiation and signed-request verification.](https://shopify.dev/docs/agents/get-started/profile)

[Create a buyer-linked token\
\
](https://shopify.dev/docs/agents/profiles/buyer-linked-tokens)

[Turn a signed-in Shop session into a buyer-linked token using the UCP delegated IdP flow.](https://shopify.dev/docs/agents/profiles/buyer-linked-tokens)

***

