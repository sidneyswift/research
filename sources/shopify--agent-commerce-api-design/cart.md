# Cart MCP

Canonical URL: https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp
Retrieved: 2026-11-04
Capture URL: https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp.md
Capture: official Markdown (or text extraction if HTML); no diagram-dependent claims.

---

---
title: Cart MCP server
description: >-
  Use the Cart MCP server to build and iterate on carts before the buyer commits
  to purchase, then convert carts into checkouts with the Checkout MCP server.
source_url:
  html: 'https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp'
  md: 'https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp.md'
---

# Cart MCP

The Cart MCP server enables AI agents to build and iterate on a cart before the buyer commits to purchase. When the buyer is ready to buy, convert the cart into a checkout with [Checkout MCP](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp).

## How it works

Cart MCP implements the UCP cart capability (`dev.ucp.shopping.cart`, version `2026-08-25`). A cart is a pre-checkout container for line items, localization context, and optional buyer information. Cart tools accept unauthenticated requests, which lets you estimate totals and share a cart with the buyer before collecting credentials.

When the buyer is ready to purchase, pass the cart ID to [`create_checkout`](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp#create_checkout) on Checkout MCP to convert the cart into a checkout session.

For usage guidelines, see [About carts and checkout](https://shopify.dev/docs/agents/carts-and-checkout). For the full UCP specification, see the [Cart capability](https://ucp.dev/2026-08-25/specification/shopping/cart/) and [Cart MCP binding](https://ucp.dev/2026-08-25/specification/shopping/cart/mcp/).

### Cart vs.​checkout

Carts and checkouts are designed for different parts of the buyer journey:

* **Carts have a long TTL.** Use them for browsing sessions where the buyer is still exploring. Iterate on `line_items` and `context` across multiple turns, share the cart's `continue_url` with the buyer, and let the cart persist while they decide.
* **Checkouts are short-lived.** Create one only when the buyer is ready to purchase. Each checkout session represents an active transaction with stricter freshness, idempotency, and rate-limit guarantees.

***

## Use with the AI Toolkit

The [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) [installs](https://shopify.dev/docs/agents#get-started) the `ucp` skill, which lets agents in Cursor, Claude Code, and other compatible IDEs call each Cart MCP tool by name. Ask your assistant in natural language (`"add this variant to a new cart"`) and the skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command, or run `ucp cart` directly in a terminal.

Run `ucp cart <subcommand> --input-schema --business <url>` to fetch the merchant's live input schema before composing payloads.

##### Create cart

```bash
ucp cart create --business https://{shop}.example.com \
  --set /line_items/0/item/id='gid://shopify/ProductVariant/12345' \
  --set /line_items/0/quantity=1 \
  --set /context/address_country=US
```

##### Get cart

```bash
ucp cart get gid://shopify/Cart/cart_abc123 \
  --business https://{shop}.example.com
```

##### Update cart

```bash
ucp cart update gid://shopify/Cart/cart_abc123 \
  --business https://{shop}.example.com \
  --set /line_items/0/quantity=2
```

##### Cancel cart

```bash
ucp cart cancel gid://shopify/Cart/cart_abc123 \
  --business https://{shop}.example.com
```

### Rate limits

Cart MCP and Checkout MCP have separate rate limits, and Checkout MCP is throttled more strictly across every tier. Limits scale with how your agent identifies itself:

* **Token tier** (Bearer token): The highest limits.
* **Signed tier** (signed request): Lower limits.
* **Anonymous tier**: The lowest limits.

Keep exploratory and review-style interactions — adjusting `line_items`, refining `context`, refreshing totals — on Cart MCP, and only call Checkout MCP when the buyer is ready to buy. When the server rate-limits a request, retry after the delay specified by the HTTP `Retry-After` response header and apply exponential backoff with jitter.

For tier definitions, capability matrices, and the full guidance, see [Auth and rate limiting](https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting).

| Use case | Recommended tool |
| - | - |
| Browsing, exploration, total estimates across turns | Cart MCP |
| Sharing a cart link with the buyer | Cart MCP (`continue_url`) |
| Buyer is ready to purchase | Checkout MCP |
| Completing the order in your application | Checkout MCP (`complete_checkout`) |

***

## Make requests

All requests follow the JSON-RPC 2.0 protocol. Send `POST` requests to the merchant's UCP endpoint: `https://{shop-domain}/api/ucp/mcp`

Cart tools accept unauthenticated requests. You don't need a Bearer token to call `create_cart`, `get_cart`, `update_cart`, or `cancel_cart`.

If you send a Bearer token, then the request must also include a [`Shopify-Buyer-IP` header](https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting#buyer-ip-header) with the buyer's IP address.

Every request must include a `meta` object in `arguments`. Include `meta["ucp-agent"]` with a `profile` URI (your agent's [UCP profile at `/.well-known/ucp`](https://ucp.dev/2026-08-25/specification/overview/)) for [capability negotiation](https://ucp.dev/2026-08-25/specification/shopping/cart/mcp/#discovery). For `cancel_cart`, you must also include `meta["idempotency-key"]` with a unique UUID for retry safety.

The cart is returned in `result.structuredContent`. The `result.content` array may also be present with a text representation of the cart.

POST

## https://{shop-domain}/api/ucp/mcp

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "tool_name",
    "arguments": {
      "meta": {
        "ucp-agent": { 
          "profile": "https://example.com/.well-known/ucp" 
        }
      }
    }
  }
}
```

## {} Response

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "structuredContent": {
      "cart": {
        "ucp": {
          "version": "2026-08-25",
          "capabilities": {
            "dev.ucp.shopping.cart": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/cart/" }]
          }
        },
        "id": "gid://shopify/Cart/cart_abc123",
        "continue_url": "https://shop.example.com/cart/c/cart_abc123"
      }
    },
    "content": [
      { "type": "text", "text": "{\"cart\":{\"ucp\":{...},\"id\":\"gid://shopify/Cart/cart_abc123\",...}}" }
    ]
  }
}
```

***

## Cart tools

Cart tools let your agent build and iterate on a cart before the buyer commits to purchase. For requests that operate on an existing cart (`get_cart`, `update_cart`, `cancel_cart`), pass the cart ID as the top-level `id` in `arguments`.

* [`create_cart`](#create_cart): Create a new cart with line items and optional buyer context.
* [`get_cart`](#get_cart): Retrieve the current state of a cart.
* [`update_cart`](#update_cart): Replace the cart's contents.
* [`cancel_cart`](#cancel_cart): Cancel a cart.

When the buyer is ready to buy, pass the cart ID to [`create_checkout`](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp#create_checkout) on Checkout MCP to convert the cart into a checkout.

### `create_cart`

Create a new cart with line items and optional buyer context.

Use this tool when the buyer has selected products from the Catalog and you want to build a cart before starting checkout. The response includes a `cart` object with the merchant-assigned `id`, validated line items, estimated totals, and a `continue_url` that the buyer can use to pick up the cart on the merchant's storefront.

**Info:**

If you require sales channel attribution and plan to convert the cart into a checkout with [`create_checkout`](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp#create_checkout), set attribution on the cart before conversion.

When to use:

* Buyer has picked one or more products and you want to estimate totals.
* You want to iterate on cart contents over multiple turns before committing to a checkout.
* You want to share a cart with the buyer via `continue_url` without starting a checkout.

#### Parameters

***

meta•objectRequired (critical)

Request metadata. You're required to include `ucp-agent.profile`, the URI to your agent's UCP profile for capability negotiation.

***

cart•objectRequired (critical)

The cart object containing the cart data. Includes the following fields:

* `line_items` (required): Array of items to add to the cart. Each item must include `quantity` and an `item` object with the product variant `id`.
* `context`: Localization hints including `address_country`, `address_region`, and `postal_code`. Merchants may use these as a signal for pricing, availability, and currency estimates, but `context` is not authoritative for shipping — collect a shipping address through Checkout MCP when the buyer is ready to purchase. If omitted, the merchant falls back to geo-IP.
* `attribution`: Optional attribution metadata. Supported fields include `referring_domain`, `click_id_tag`, `click_id_value`, `activity_id_tag`, `activity_id_value`, `utm_campaign`, `utm_source`, `utm_medium`, `utm_content`, and `utm_term`.
* `buyer`: Optional buyer information for personalized estimates. When the [buyer consent](https://ucp.dev/2026-08-25/specification/shopping/extensions/buyer-consent/) capability (`dev.ucp.shopping.buyer_consent`) is negotiated, `buyer.consent` accepts the buyer's consent decisions.
* `signals`: Optional platform-provided environment data for authorization and abuse prevention.

***

#### Call from the Shopify AI Toolkit and UCP CLI

With the [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) [installed](https://shopify.dev/docs/agents#get-started), ask your assistant in natural language (`"create a cart at <shop> with..."`) and the `ucp` skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command. You can also run the command directly in a terminal:

## Create

```bash
ucp cart create --business https://{shop}.example.com \
  --set /line_items/0/item/id='gid://shopify/ProductVariant/12345' \
  --set /line_items/0/quantity=1 \
  --set /context/address_country=US \
  --set /attribution/utm_source=example_agent
```

#### Call the tool directly

POST

## https://{shop-domain}/api/ucp/mcp

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "create_cart",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-08-25/valid-with-capabilities.json"
        }
      },
      "cart": {
        "line_items": [
          {
            "quantity": 2,
            "item": {
              "id": "gid://shopify/ProductVariant/12345678901"
            }
          }
        ],
        "context": {
          "address_country": "US",
          "address_region": "CA",
          "postal_code": "94105"
        },
        "attribution": {
          "referring_domain": "example-agent.com",
          "click_id_tag": "gclid",
          "click_id_value": "abc123xyz",
          "activity_id_tag": "activity_id",
          "activity_id_value": "cart-start-001",
          "utm_campaign": "spring_sale",
          "utm_source": "example_agent",
          "utm_medium": "agentic_commerce",
          "utm_content": "sweater_recommendation",
          "utm_term": "organic cotton sweater"
        }
      }
    }
  }
}
```

## {} Response

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "structuredContent": {
      "cart": {
        "ucp": {
          "version": "2026-08-25",
          "capabilities": {
            "dev.ucp.shopping.cart": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/cart/" }]
          }
        },
        "id": "gid://shopify/Cart/cart_abc123",
        "currency": "USD",
        "line_items": [
          {
            "id": "gid://shopify/CartLine/li_1?cart=cart_abc123",
            "item": {
              "id": "gid://shopify/ProductVariant/12345678901",
              "title": "Organic Cotton Sweater",
              "price": 8900
            },
            "quantity": 2,
            "totals": [
              { "type": "subtotal", "amount": 17800, "display_text": "Subtotal" },
              { "type": "total", "amount": 17800, "display_text": "Total" }
            ]
          }
        ],
        "totals": [
          { "type": "subtotal", "amount": 17800, "display_text": "Subtotal" },
          { "type": "total", "amount": 17800, "display_text": "Total" }
        ],
        "attribution": {
          "referring_domain": "example-agent.com",
          "click_id_tag": "gclid",
          "click_id_value": "abc123xyz",
          "activity_id_tag": "activity_id",
          "activity_id_value": "cart-start-001",
          "utm_campaign": "spring_sale",
          "utm_source": "example_agent",
          "utm_medium": "agentic_commerce",
          "utm_content": "sweater_recommendation",
          "utm_term": "organic cotton sweater"
        },
        "messages": [],
        "continue_url": "https://shop.example.com/cart/c/cart_abc123",
        "expires_at": "2026-05-08T15:17:07Z"
      }
    },
    "content": [
      { "type": "text", "text": "{\"cart\":{\"ucp\":{...},\"id\":\"gid://shopify/Cart/cart_abc123\",...}}" }
    ]
  }
}
```

### `get_cart`

Retrieve the current state of an existing cart.

Use this tool to refresh estimated totals after a context change, or to confirm what a cart contains before calling `create_checkout`. If the cart does not exist or has expired, the response returns a successful JSON-RPC `result` whose `messages` array contains an `unrecoverable` error with code `not_found`.

When to use:

* You need to refresh estimated totals after updating the cart's localization context.
* You want to verify the cart exists before starting checkout.
* The buyer returned to the conversation and you want to show the current cart contents.

#### Parameters

***

meta•objectRequired (critical)

Request metadata. You're required to include `ucp-agent.profile`, the URI to your agent's UCP profile for capability negotiation.

***

id•stringRequired (critical)

The ID of the cart to retrieve.

***

#### Call from the Shopify AI Toolkit and UCP CLI

With the [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) [installed](https://shopify.dev/docs/agents#get-started), ask your assistant in natural language (`"refresh the cart at <shop>"`) and the `ucp` skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command. You can also run the command directly in a terminal:

## Get

```bash
ucp cart get gid://shopify/Cart/cart_abc123 \
  --business https://{shop}.example.com
```

#### Call the tool directly

POST

## https://{shop-domain}/api/ucp/mcp

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "get_cart",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-08-25/valid-with-capabilities.json"
        }
      },
      "id": "gid://shopify/Cart/cart_abc123"
    }
  }
}
```

## {} Not-found response

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "structuredContent": {
      "cart": {
        "ucp": {
          "version": "2026-08-25",
          "capabilities": {
            "dev.ucp.shopping.cart": [{ "version": "2026-08-25" }]
          }
        },
        "messages": [
          {
            "type": "error",
            "code": "not_found",
            "content": "Cart not found or has expired",
            "severity": "unrecoverable"
          }
        ],
        "continue_url": "https://shop.example.com/"
      }
    }
  }
}
```

### `update_cart`

Replace the contents of an existing cart.

**Caution:**

`update_cart` uses PUT semantics. Each request replaces the cart's full state with the payload you send. Omit a field (for example `line_items` or `context`) and it's removed from the cart. This differs from Storefront API and AJAX cart mutations, which patch individual fields. There is no server-side merge of partial updates.

When to use:

* The buyer changed quantities or removed items; send the full updated `line_items` array.
* The buyer shared a location or postal code; send updated localization `context` alongside the existing `line_items` to refresh estimates. `context` is a hint for pricing, availability, and currency — it is not used as the shipping address at checkout.
* You want to preserve or update attribution; resend `attribution` with the full desired cart state.
* You want to attach buyer information (for example, email) to an existing cart.

#### Parameters

***

meta•objectRequired (critical)

Request metadata. You're required to include `ucp-agent.profile`, the URI to your agent's UCP profile for capability negotiation.

***

id•stringRequired (critical)

The ID of the cart to update.

***

cart•objectRequired (critical)

The cart object containing the full desired cart state. Any field you omit is removed from the cart.

* `line_items` (required): Full replacement array of items.
* `context`: Localization signals.
* `attribution`: Attribution metadata. Because the cart object is replaced, resend attribution if you want to preserve it.
* `buyer`: Optional buyer information. When [buyer consent](https://ucp.dev/2026-08-25/specification/shopping/extensions/buyer-consent/) is negotiated, include `buyer.consent` to confirm the buyer's consent decisions. Omitting `consent` leaves the current consent unchanged.
* `signals`: Optional platform signals.

***

#### Call from the Shopify AI Toolkit and UCP CLI

With the [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) [installed](https://shopify.dev/docs/agents#get-started), ask your assistant in natural language (`"change the quantity of <variant> in the cart to 2"`) and the `ucp` skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command. You can also run the command directly in a terminal:

## Update

```bash
ucp cart update gid://shopify/Cart/cart_abc123 \
  --business https://{shop}.example.com \
  --set /line_items/0/item/id='gid://shopify/ProductVariant/12345' \
  --set /line_items/0/quantity=2
```

#### Call the tool directly

POST

## https://{shop-domain}/api/ucp/mcp

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 2,
  "params": {
    "name": "update_cart",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-08-25/valid-with-capabilities.json"
        }
      },
      "id": "gid://shopify/Cart/cart_abc123",
      "cart": {
        "line_items": [
          {
            "quantity": 3,
            "item": { "id": "gid://shopify/ProductVariant/12345678901" }
          },
          {
            "quantity": 1,
            "item": { "id": "gid://shopify/ProductVariant/22222222222" }
          }
        ],
        "context": {
          "address_country": "US",
          "address_region": "CA",
          "postal_code": "94105"
        },
        "attribution": {
          "utm_source": "example_agent",
          "utm_medium": "agentic_commerce",
          "utm_campaign": "spring_sale"
        }
      }
    }
  }
}
```

## {} Response

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "structuredContent": {
      "cart": {
        "ucp": {
          "version": "2026-08-25",
          "capabilities": {
            "dev.ucp.shopping.cart": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/cart/" }]
          }
        },
        "id": "gid://shopify/Cart/cart_abc123",
        "currency": "USD",
        "line_items": [
          {
            "id": "gid://shopify/CartLine/li_1?cart=cart_abc123",
            "item": { "id": "gid://shopify/ProductVariant/12345678901", "title": "Organic Cotton Sweater", "price": 8900 },
            "quantity": 3
          },
          {
            "id": "gid://shopify/CartLine/li_2?cart=cart_abc123",
            "item": { "id": "gid://shopify/ProductVariant/22222222222", "title": "Cotton Tote", "price": 2400 },
            "quantity": 1
          }
        ],
        "totals": [
          { "type": "subtotal", "amount": 29100, "display_text": "Subtotal" },
          { "type": "total", "amount": 29100, "display_text": "Total" }
        ],
        "messages": [],
        "continue_url": "https://shop.example.com/cart/c/cart_abc123",
        "expires_at": "2026-05-08T15:17:07Z"
      }
    }
  }
}
```

### `cancel_cart`

Cancel an active cart. Requires `meta["idempotency-key"]` (UUID) in addition to `meta["ucp-agent"]`.

Canceling a cart removes it from storage. Subsequent calls to [`get_cart`](#get_cart) with the same ID return a `not_found` business outcome. Cancel a cart when the buyer abandons the conversation or you want to clean up a stale cart before starting a new one.

When to use:

* The buyer indicated they no longer want to purchase.
* You want to remove a stale cart before starting a new one.

#### Parameters

***

meta•objectRequired (critical)

Request metadata. You're required to include `ucp-agent.profile` and `idempotency-key`.

***

id•stringRequired (critical)

The ID of the cart to cancel.

***

#### Call from the Shopify AI Toolkit and UCP CLI

With the [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) [installed](https://shopify.dev/docs/agents#get-started), ask your assistant in natural language (`"cancel my cart at <shop>"`) and the `ucp` skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command. You can also run the command directly in a terminal:

## Cancel

```bash
ucp cart cancel gid://shopify/Cart/cart_abc123 \
  --business https://{shop}.example.com
```

#### Call the tool directly

POST

## https://{shop-domain}/api/ucp/mcp

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 3,
  "params": {
    "name": "cancel_cart",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-08-25/valid-with-capabilities.json"
        },
        "idempotency-key": "660e8400-e29b-41d4-a716-446655440001"
      },
      "id": "gid://shopify/Cart/cart_abc123"
    }
  }
}
```

## {} Response

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "structuredContent": {
      "cart": {
        "ucp": {
          "version": "2026-08-25",
          "capabilities": {
            "dev.ucp.shopping.cart": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/cart/" }]
          }
        },
        "id": "gid://shopify/Cart/cart_abc123",
        "messages": [
          {
            "type": "info",
            "code": "cart_canceled",
            "content": "Cart canceled"
          }
        ],
        "continue_url": "https://shop.example.com/"
      }
    }
  }
}
```

***

## Error handling

UCP distinguishes between protocol errors and business outcomes.

* **Business outcomes:** Application-level results from successful request processing, returned as JSON-RPC `result` with the UCP envelope and a `messages` array.
* **Protocol errors:** Transport-level failures (authentication, rate limiting, unavailability) that prevent request processing. Returned as JSON-RPC `error` with code `-32000`, or `-32001` for discovery errors.

See the [Cart MCP binding](https://ucp.dev/2026-04-08/specification/cart-mcp/#error-handling), the [Checkout MCP binding](https://ucp.dev/2026-04-08/specification/checkout-mcp/#error-handling), and [Core Specification error handling](https://ucp.dev/2026-04-08/specification/overview/#error-handling) for the complete error code registry and examples.

### Protocol errors

Transport-level failures that prevent the request from being processed (for example authentication failure, rate limiting, or service unavailability) are returned as JSON-RPC `error` with code `-32000`, or `-32001` for discovery errors. These are not application outcomes: the server did not complete the operation.

When the server rate-limits your request, retry after the delay specified by the HTTP `Retry-After` response header. Clients should honor `Retry-After` and apply exponential backoff with jitter when the header is absent. Don't retry inside the same checkout or payment lifecycle without an [`idempotency-key`](https://ucp.dev/2026-04-08/specification/checkout-mcp/#request-metadata).

## Protocol error (JSON-RPC error)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32000,
    "message": "Unauthorized"
  }
}
```

### Business outcomes

Application-level results (including conditions like an expired cart, unavailable merchandise, or an adjusted quantity) are returned as a successful JSON-RPC `result` with `structuredContent.cart` and a `messages` array. The request was processed; the outcome is in the payload.

Inspect `result.structuredContent.cart` and its `messages` array. Use message `type`, `code`, and optional `path` to adjust your flow (for example, prompt the buyer to pick an alternative product or adjust quantity).

Checkout responses use a different envelope. See [Business outcomes on Checkout MCP](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp#business-outcomes) when working with checkout tools.

## Business outcome (result with messages)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "structuredContent": {
      "cart": {
        "ucp": { "version": "2026-08-25", "capabilities": { "dev.ucp.shopping.cart": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/cart/" }] } },
        "id": "gid://shopify/Cart/cart_abc123",
        "line_items": [
          { "id": "gid://shopify/CartLine/li_1?cart=cart_abc123", "quantity": 100, "available_quantity": 12 }
        ],
        "messages": [
          {
            "type": "warning",
            "code": "quantity_adjusted",
            "content": "Quantity adjusted; requested 100 units but only 12 available",
            "path": "$.line_items[0].quantity"
          }
        ],
        "continue_url": "https://shop.example.com/cart/c/cart_abc123"
      }
    }
  }
}
```

***

