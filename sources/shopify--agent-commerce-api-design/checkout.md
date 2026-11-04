# Checkout MCP

Canonical URL: https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp
Retrieved: 2026-11-04
Capture URL: https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp.md
Capture: official Markdown (or text extraction if HTML); no diagram-dependent claims.

---

---
title: Checkout MCP server
description: >-
  Use the Checkout MCP server to create and manage checkout sessions, convert
  carts into checkouts, and refer buyers to Shopify merchant storefronts to
  complete purchases.
source_url:
  html: 'https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp'
  md: 'https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp.md'
---

# Checkout MCP

The Checkout MCP server enables AI agents to create and manage checkout sessions, convert carts into checkouts, and refer buyers to the merchant storefront to complete purchases.

## How it works

Checkout MCP implements the UCP checkout capability (`dev.ucp.shopping.checkout`). Checkout tools manage a purchase session once the buyer is ready to buy. All requests require authentication or a signed request.

When the buyer is ready to purchase, set the optional `cart_id` field in the `checkout` object of [`create_checkout`](#create_checkout) to convert a cart built with [Cart MCP](https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp) into a checkout session. See [Convert a cart into a checkout](#convert-a-cart-into-a-checkout).

For usage guidelines, see [About carts and checkout](https://shopify.dev/docs/agents/carts-and-checkout). For the full UCP specification, see [Checkout capability](https://ucp.dev/2026-08-25/specification/shopping/checkout/) and the [Checkout MCP binding](https://ucp.dev/2026-08-25/specification/shopping/checkout/mcp/).

**Info:**

**Use Cart MCP for iteration.** Checkout MCP is rate-limited more strictly than [Cart MCP](https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp) across all tiers. Iterate on line items, localization, and estimated totals on a cart, then create a checkout when the buyer is ready to buy. See [Auth and rate limiting](https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting) for details.

***

## Use with the AI Toolkit

The [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) [installs](https://shopify.dev/docs/agents#get-started) the `ucp` skill, which lets agents in Cursor, Claude Code, and other compatible IDEs call each Checkout MCP tool by name, including how to handle the escalation flow when a merchant requires buyer review. Ask your assistant in natural language (`"complete this checkout with..."`) and the skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command, or run `ucp checkout` directly in a terminal.

Set `UCP_ON_ESCALATION` before completing a checkout to open the merchant's `continue_url` in the buyer's browser automatically.

##### Create from cart

```bash
ucp checkout create --business https://{shop}.example.com \
  --input '{"cart_id":"gid://shopify/Cart/cart_abc123","line_items":[]}'
```

##### Update

```bash
ucp checkout update gid://shopify/Checkout/abc123 \
  --business https://{shop}.example.com \
  --input-schema
ucp checkout update gid://shopify/Checkout/abc123 \
  --business https://{shop}.example.com \
  --input '{"buyer":{"email":"buyer@example.com"}}'
```

##### Complete

```bash
export UCP_ON_ESCALATION='jq -r .url | xargs open'
ucp checkout complete gid://shopify/Checkout/abc123 \
  --business https://{shop}.example.com
```

##### Cancel

```bash
ucp checkout cancel gid://shopify/Checkout/abc123 \
  --business https://{shop}.example.com
```

***

## Authenticate

Obtain your client credentials (client ID and secret) from [the **Catalog** section of Dev Dashboard](https://shopify.dev/docs/apps/build/dev-dashboard).

Then use those credentials to retrieve a token for subsequent requests. Send it in the `Authorization: Bearer {token}` header on each request.

The response contains:

* `access_token`: A JWT access token used to interact with the MCP server.
* `token_type`: The type of the access token. This is always `Bearer`.

JWT tokens created from Dev Dashboard credentials have a 60-minute TTL. You can use a decoder tool like [`jwt.io`](https://www.jwt.io/) to view more details related to how Shopify issues this token.

POST

## https://api.shopify.com/auth/access\_token

```bash
curl --request POST \
  --url https://api.shopify.com/auth/access_token \
  --header 'Content-Type: application/json' \
  --data '{
    "client_id": "{your_client_id}",
    "client_secret": "{your_client_secret}",
    "grant_type": "client_credentials"
  }'
```

## {} Response

```json
{
    "access_token": "f8563253df0bf277ec9ac6f649fc3f17",
    "token_type": "Bearer"
}
```

***

## Make requests

All requests follow the JSON-RPC 2.0 protocol. Send `POST` requests to the merchant's UCP endpoint: `https://{shop-domain}/api/ucp/mcp`

Token-tier requests must also include a [`Shopify-Buyer-IP` header](https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting#buyer-ip-header) with the buyer's IP address.

Every request must include a `meta` object in `arguments`. Include `meta["ucp-agent"]` with a `profile` URI (your agent's [UCP profile at `/.well-known/ucp`](https://ucp.dev/2026-08-25/specification/overview/)) for [capability negotiation](https://ucp.dev/2026-08-25/specification/shopping/checkout/mcp/#discovery). For `complete_checkout` and `cancel_checkout`, you must also include `meta["idempotency-key"]` with a unique UUID for retry safety.

The checkout is returned in `result.structuredContent`. The `result.content` array may also be present with a text representation of the checkout.

Platforms may use [HTTP Message Signatures](https://ucp.dev/2026-08-25/specification/signatures/) (for example, RFC 9421) for agent authentication in addition to or instead of Bearer tokens.

Learn more about [building agentic commerce experiences](https://shopify.dev/docs/agents/get-started/authentication).

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
      "ucp": {
        "version": "2026-08-25",
        "capabilities": {
          "dev.ucp.shopping.checkout": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/checkout/", "schema": "https://ucp.dev/2026-08-25/schemas/shopping/checkout.json" }],
          "dev.ucp.shopping.fulfillment": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/extensions/fulfillment/", "schema": "https://ucp.dev/2026-08-25/schemas/shopping/fulfillment.json", "extends": ["dev.ucp.shopping.checkout", "dev.ucp.shopping.cart"] }]
        }
      },
      "id": "checkout_abc123",
      "status": "incomplete",
      "continue_url": "https://shop.example.com/checkout/checkout_abc123"
    },
    "content": [
      { "type": "text", "text": "{\"ucp\":{...},\"id\":\"checkout_abc123\",...}" }
    ]
  }
}
```

***

## Checkout tools

Checkout tools manage a purchase session once the buyer is ready to buy. [`create_checkout`](#create_checkout) also accepts an optional `cart_id` field in the `checkout` object to convert a cart built with [Cart MCP](https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp) into a checkout session. See [Convert a cart into a checkout](#convert-a-cart-into-a-checkout).

**Caution:**

Tool use is subject to access and rate limiting that scale with how your agent identifies itself. See [Auth and rate limiting](https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting) for traffic tiers and what each can do.

Checkout MCP provides tools for managing the checkout lifecycle. For get, update, complete, and cancel operations, pass the checkout session ID as the top-level `id` in `arguments` rather than within the `checkout` object. The UCP spec treats resource identification and payload separately so the server can validate requests correctly.

* [`create_checkout`](#create_checkout): Create a new checkout session with line items and buyer information.
* [`get_checkout`](#get_checkout): Retrieve the current state of a checkout session.
* [`update_checkout`](#update_checkout): Update a checkout session with new information.
* [`complete_checkout`](#complete_checkout): Submit payment and place the order. When a checkout returns `requires_escalation`, direct the buyer to `continue_url` to complete the purchase on the merchant's checkout.
* [`cancel_checkout`](#cancel_checkout): Cancel an active checkout session.

### `create_checkout`

Create a new checkout session with line items, buyer information, and fulfillment preferences.

Use this tool when a buyer is ready to purchase items and you need to initiate the checkout process. The response includes a `continue_url` for handing off to a trusted UI.

When to use:

* Buyer says "I want to buy this item"
* Agent has collected enough information to start checkout
* Buyer confirms their cart and wants to proceed

#### Parameters

***

meta•objectRequired (critical)

Request metadata. You're required to include `ucp-agent.profile`, the URI to your agent's UCP profile for capability negotiation.

***

checkout•objectRequired (critical)

The checkout object containing all checkout data. Includes the following fields:

* `currency` (required): ISO 4217 currency code (for example, `USD`, `EUR`, `GBP`).
* `line_items` (required): Array of items to purchase. Each item must include `quantity` and an `item` object with the product variant `id`. When you set `cart_id`, pass an empty array (`[]`).
* `cart_id`: The optional ID of a cart built with [Cart MCP](https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp) to convert into this checkout. Only valid when both the cart and checkout capabilities are negotiated. When present, the server loads the referenced cart, uses its `line_items`, `context`, and `buyer`, and ignores overlapping fields in the `checkout` payload, so `currency` and `buyer` aren't needed. Invalid GIDs return `invalid_cart_id`; missing carts return `cart_not_found`. See [Convert a cart into a checkout](#convert-a-cart-into-a-checkout).
* `buyer` (required): Buyer information. Contact method `email` or `phone_number` must be provided, per-merchant configuration. When the [buyer consent](https://ucp.dev/2026-08-25/specification/shopping/extensions/buyer-consent/) capability (`dev.ucp.shopping.buyer_consent`) is negotiated, `buyer.consent` accepts the buyer's consent decisions.
* `context`: Provisional buyer signals for intent, localization, currency, and eligibility decisions. Supported fields include `address_country`, `address_region`, `postal_code`, `intent`, `language`, `currency`, and `eligibility`. A shipping address supersedes these context hints.
* `attribution`: Optional attribution metadata. Supported fields include `referring_domain`, `click_id_tag`, `click_id_value`, `activity_id_tag`, `activity_id_value`, `utm_campaign`, `utm_source`, `utm_medium`, `utm_content`, and `utm_term`.
* `fulfillment`: Fulfillment preferences including shipping `methods` and `destinations`.
* `payment`: Payment configuration including available `instruments` and `selected_instrument_id`.

***

#### Call from the Shopify AI Toolkit and UCP CLI

With the [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) [installed](https://shopify.dev/docs/agents#get-started), ask your assistant in natural language (`"start a checkout from this cart"`) and the `ucp` skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command. You can also run the command directly in a terminal:

## Create from cart

```bash
ucp checkout create --business https://{shop}.example.com \
  --input '{"cart_id":"gid://shopify/Cart/cart_abc123","line_items":[]}'
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
    "name": "create_checkout",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-08-25/valid-with-capabilities.json"
        }
      },
      "checkout": {
        "currency": "USD",
        "line_items": [
          {
            "quantity": 2,
            "item": {
              "id": "gid://shopify/ProductVariant/12345678901"
            }
          }
        ],
        "buyer": {
          "email": "buyer@example.com"
        },
        "context": {
          "intent": "Buyer wants two sweaters shipped to Brooklyn",
          "language": "en-US",
          "currency": "USD",
          "eligibility": [
            "com.example.loyalty_gold"
          ]
        },
        "attribution": {
          "referring_domain": "example-agent.com",
          "click_id_tag": "gclid",
          "click_id_value": "abc123xyz",
          "activity_id_tag": "activity_id",
          "activity_id_value": "checkout-start-001",
          "utm_campaign": "spring_sale",
          "utm_source": "example_agent",
          "utm_medium": "agentic_commerce",
          "utm_content": "sweater_recommendation",
          "utm_term": "organic cotton sweater"
        },
        "fulfillment": {
          "methods": [
            {
              "type": "shipping",
              "destinations": [
                {
                  "first_name": "Jane",
                  "last_name": "Smith",
                  "street_address": "123 Main Street",
                  "address_locality": "Brooklyn",
                  "address_region": "NY",
                  "postal_code": "11201",
                  "address_country": "US"
                }
              ]
            }
          ]
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
      "ucp": {
          "version": "2026-08-25",
          "capabilities": {
            "dev.ucp.shopping.checkout": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/checkout/", "schema": "https://ucp.dev/2026-08-25/schemas/shopping/checkout.json" }],
            "dev.ucp.shopping.fulfillment": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/extensions/fulfillment/", "schema": "https://ucp.dev/2026-08-25/schemas/shopping/fulfillment.json", "extends": ["dev.ucp.shopping.checkout", "dev.ucp.shopping.cart"] }]
          },
          "payment_handlers": {
            "com.google.pay": [{ "id": "gpay", "version": "2026-01-23", "config": {} }]
          }
        },
        "id": "gid://shopify/Checkout/abc123?key=xyz789",
        "status": "requires_escalation",
        "currency": "USD",
        "buyer": {
          "email": "buyer@example.com"
        },
        "line_items": [
          {
            "id": "gid://shopify/CartLine/li_1?cart=abc123",
            "item": {
              "id": "gid://shopify/ProductVariant/12345678901",
              "title": "Organic Cotton Sweater",
              "price": 8900,
              "image_url": "https://cdn.shopify.com/example/sweater.jpg"
            },
            "quantity": 2,
            "totals": [
              { "type": "subtotal", "amount": 17800, "display_text": "Subtotal" },
              { "type": "items_discount", "amount": 0, "display_text": "Discount" },
              { "type": "total", "amount": 17800, "display_text": "Total" }
            ]
          }
        ],
        "totals": [
          { "type": "subtotal", "amount": 17800, "display_text": "Subtotal" },
          { "type": "fulfillment", "amount": 500, "display_text": "Shipping" },
          { "type": "tax", "amount": 1466, "display_text": "Tax" },
          { "type": "total", "amount": 19766, "display_text": "Total" }
        ],
        "fulfillment": {},
        "expires_at": "2026-02-20T15:17:07Z",
        "links": [
          { "type": "privacy_policy", "url": "https://shop.example.com/policies/privacy" },
          { "type": "terms_of_service", "url": "https://shop.example.com/policies/terms" }
        ],
        "payment": {
          "instruments": []
        },
        "attribution": {
          "referring_domain": "example-agent.com",
          "click_id_tag": "gclid",
          "click_id_value": "abc123xyz",
          "activity_id_tag": "activity_id",
          "activity_id_value": "checkout-start-001",
          "utm_campaign": "spring_sale",
          "utm_source": "example_agent",
          "utm_medium": "agentic_commerce",
          "utm_content": "sweater_recommendation",
          "utm_term": "organic cotton sweater"
        },
        "messages": [],
        "continue_url": "https://shop.example.com/cart/c/abc123?key=xyz789"
    },
    "content": [
      { "type": "text", "text": "{\"ucp\":{...},\"id\":\"gid://shopify/Checkout/abc123?key=xyz789\",...}" }
    ]
  }
}
```

### `get_checkout`

Retrieve the current state of an existing checkout session.

Use this tool to check the status of a checkout, see updated totals after changes, or verify what information is still needed before completion.

When to use:

* Need to refresh checkout state after buyer returns
* Want to show current totals and line items
* Checking if checkout is ready for payment

#### Parameters

***

meta•objectRequired (critical)

Request metadata. You're required to include `ucp-agent.profile`, the URI to your agent's UCP profile for capability negotiation.

***

id•stringRequired (critical)

The ID of the checkout session to retrieve.

***

#### Call from the Shopify AI Toolkit and UCP CLI

With the [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) [installed](https://shopify.dev/docs/agents#get-started), ask your assistant in natural language (`"refresh my checkout"`) and the `ucp` skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command. You can also run the command directly in a terminal:

## Get

```bash
ucp checkout get gid://shopify/Checkout/abc123 \
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
    "name": "get_checkout",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-08-25/valid-with-capabilities.json"
        }
      },
      "id": "gid://shopify/Checkout/abc123?key=xyz789"
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
      "ucp": {
          "version": "2026-08-25",
          "capabilities": {
            "dev.ucp.shopping.checkout": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/checkout/", "schema": "https://ucp.dev/2026-08-25/schemas/shopping/checkout.json" }],
            "dev.ucp.shopping.fulfillment": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/extensions/fulfillment/", "schema": "https://ucp.dev/2026-08-25/schemas/shopping/fulfillment.json", "extends": ["dev.ucp.shopping.checkout", "dev.ucp.shopping.cart"] }]
          },
          "payment_handlers": {
            "com.google.pay": [{ "id": "gpay", "version": "2026-01-23", "config": {} }]
          }
        },
        "id": "gid://shopify/Checkout/abc123?key=xyz789",
        "status": "incomplete",
        "currency": "USD",
        "buyer": {
          "email": "buyer@example.com"
        },
        "line_items": [
          {
            "id": "gid://shopify/CartLine/li_1?cart=abc123",
            "item": {
              "id": "gid://shopify/ProductVariant/12345678901",
              "title": "Organic Cotton Sweater",
              "price": 8900,
              "image_url": "https://cdn.shopify.com/example/sweater.jpg"
            },
            "quantity": 2,
            "totals": [
              { "type": "subtotal", "amount": 17800, "display_text": "Subtotal" },
              { "type": "items_discount", "amount": 0, "display_text": "Discount" },
              { "type": "total", "amount": 17800, "display_text": "Total" }
            ]
          }
        ],
        "totals": [
          { "type": "subtotal", "amount": 17800, "display_text": "Subtotal" }
        ],
        "fulfillment": {},
        "expires_at": "2026-02-20T15:17:07Z",
        "links": [
          { "type": "privacy_policy", "url": "https://shop.example.com/policies/privacy" },
          { "type": "terms_of_service", "url": "https://shop.example.com/policies/terms" }
        ],
        "payment": {
          "instruments": []
        },
        "messages": [
          {
            "type": "warning",
            "code": "missing_shipping_address",
            "content": "Shipping address is required",
            "path": "$.fulfillment"
          }
        ],
        "continue_url": "https://shop.example.com/cart/c/abc123?key=xyz789"
    }
  }
}
```

### `update_checkout`

Update an existing checkout session with new information.

Use this tool to modify line items, update shipping address, change fulfillment method, or add buyer information before completing the checkout.

When to use:

* Buyer wants to change quantity or remove items
* Buyer provides or updates shipping address
* Need to update buyer email or contact info
* Changing a delivery option

**Caution:**

`update_checkout` uses PUT semantics. Each request replaces the full checkout state with the payload you send. Omit a field (for example `line_items` or `buyer`) and it is removed from the checkout. There is no server-side merge of partial updates.

Before sending an update, remove response-only fields from the payload. `checkout.buyer.country_code` isn't accepted as input. `checkout.payment.instruments[].display` is response-only. For fulfillment updates, `checkout.fulfillment.methods[].id` is optional, but `line_item_ids` is required.

#### Parameters

***

meta•objectRequired (critical)

Request metadata. You're required to include `ucp-agent.profile`, the URI to your agent's UCP profile for capability negotiation.

***

id•stringRequired (critical)

The ID of the checkout session to update.

***

checkout•objectRequired (critical)

The checkout object containing the complete updated checkout state. Includes the following fields:

* `line_items` (required): Updated array of items. Replaces existing line items.
* `buyer` (required): Updated buyer information. Contact method `email` or `phone_number` must be provided, per-merchant configuration. When [buyer consent](https://ucp.dev/2026-08-25/specification/shopping/extensions/buyer-consent/) is negotiated, include `buyer.consent` to confirm the buyer's consent decisions. Omitting `consent` leaves the current consent unchanged.
* `context`: Updated provisional buyer signals for intent, localization, currency, and eligibility decisions. Supported fields include `address_country`, `address_region`, `postal_code`, `intent`, `language`, `currency`, and `eligibility`. A shipping address supersedes these context hints.
* `attribution`: Attribution metadata. Because the checkout object is replaced, resend attribution if you want to preserve it.
* `fulfillment`: Updated fulfillment preferences. Each method must include `line_item_ids`.
* `payment`: Updated payment configuration. Don't send response-only `display` fields from `payment.instruments`.

***

#### Call from the Shopify AI Toolkit and UCP CLI

With the [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) [installed](https://shopify.dev/docs/agents#get-started), ask your assistant in natural language (`"add my email to this checkout"`) and the `ucp` skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command. You can also run the command directly in a terminal:

## Update

```bash
ucp checkout update gid://shopify/Checkout/abc123 \
  --business https://{shop}.example.com \
  --input-schema
ucp checkout update gid://shopify/Checkout/abc123 \
  --business https://{shop}.example.com \
  --input '{"buyer":{"email":"buyer@example.com"}}'
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
    "name": "update_checkout",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-08-25/valid-with-capabilities.json"
        }
      },
      "id": "gid://shopify/Checkout/abc123?key=xyz789",
      "checkout": {
        "line_items": [
          {
            "id": "gid://shopify/CartLine/a891d8e3-7dad-42fe-b795-d8ad77ce2af8?cart=hWNF4zCrAqgZcs3OYKm4Vgji",
            "quantity": 1,
            "item": {
              "id": "gid://shopify/ProductVariant/12345678901"
            }
          }
        ],
        "buyer": {
          "email": "buyer@example.com",
          "consent": {
            "dev.ucp.consent.analytics": { "granted": false, "source": "business" },
            "dev.ucp.consent.preferences": { "granted": false, "source": "business" },
            "dev.ucp.consent.sale_or_sharing": { "granted": false, "source": "business" },
            "dev.ucp.consent.marketing": {
              "granted": false,
              "source": "business",
              "segments": {
                "dev.ucp.consent.marketing.email": { "granted": true, "source": "platform" },
                "dev.ucp.consent.marketing.sms": { "granted": false, "source": "business" }
              }
            }
          }
        },
        "context": {
          "address_country": "US",
          "address_region": "NY",
          "postal_code": "10001",
          "intent": "Buyer updated the shipping destination",
          "language": "en-US",
          "currency": "USD"
        },
        "attribution": {
          "utm_source": "example_agent",
          "utm_medium": "agentic_commerce",
          "utm_campaign": "spring_sale"
        },
        "fulfillment": {
          "methods": [
            {
              "type": "shipping",
              "line_item_ids": [
                "gid://shopify/CartLine/a891d8e3-7dad-42fe-b795-d8ad77ce2af8?cart=hWNF4zCrAqgZcs3OYKm4Vgji"
              ],
              "destinations": [
                {
                  "first_name": "Jane",
                  "last_name": "Smith",
                  "street_address": "456 Oak Avenue",
                  "address_locality": "Manhattan",
                  "address_region": "NY",
                  "postal_code": "10001",
                  "address_country": "US"
                }
              ]
            }
          ]
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
      "ucp": {
          "version": "2026-08-25",
          "capabilities": {
            "dev.ucp.shopping.checkout": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/checkout/", "schema": "https://ucp.dev/2026-08-25/schemas/shopping/checkout.json" }],
            "dev.ucp.shopping.fulfillment": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/extensions/fulfillment/", "schema": "https://ucp.dev/2026-08-25/schemas/shopping/fulfillment.json", "extends": ["dev.ucp.shopping.checkout", "dev.ucp.shopping.cart"] }],
            "dev.ucp.shopping.buyer_consent": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/extensions/buyer-consent/", "schema": "https://ucp.dev/2026-08-25/schemas/shopping/buyer_consent.json", "extends": ["dev.ucp.shopping.cart", "dev.ucp.shopping.checkout"] }]
          },
          "payment_handlers": {
            "com.google.pay": [{ "id": "gpay", "version": "2026-01-23", "config": {} }]
          }
        },
        "id": "gid://shopify/Checkout/abc123?key=xyz789",
        "status": "requires_escalation",
        "currency": "USD",
        "buyer": {
          "email": "buyer@example.com",
          "consent": {
            "dev.ucp.consent.analytics": { "granted": false, "source": "business", "description": "Analytics and performance measurement" },
            "dev.ucp.consent.preferences": { "granted": false, "source": "business", "description": "Remember preferences and personalize your shopping experience" },
            "dev.ucp.consent.sale_or_sharing": { "granted": false, "source": "business", "description": "Sale or sharing of personal data with third parties" },
            "dev.ucp.consent.marketing": {
              "granted": false,
              "source": "business",
              "description": "Marketing communications",
              "segments": {
                "dev.ucp.consent.marketing.email": { "granted": true, "source": "platform", "description": "Promotional emails" },
                "dev.ucp.consent.marketing.sms": { "granted": false, "source": "business", "description": "Marketing text messages" }
              }
            }
          }
        },
        "line_items": [
          {
            "id": "gid://shopify/CartLine/li_1?cart=abc123",
            "item": {
              "id": "gid://shopify/ProductVariant/12345678901",
              "title": "Organic Cotton Sweater",
              "price": 8900,
              "image_url": "https://cdn.shopify.com/example/sweater.jpg"
            },
            "quantity": 1,
            "totals": [
              { "type": "subtotal", "amount": 8900, "display_text": "Subtotal" },
              { "type": "items_discount", "amount": 0, "display_text": "Discount" },
              { "type": "total", "amount": 8900, "display_text": "Total" }
            ]
          }
        ],
        "totals": [
          { "type": "subtotal", "amount": 8900, "display_text": "Subtotal" },
          { "type": "fulfillment", "amount": 500, "display_text": "Shipping" },
          { "type": "tax", "amount": 752, "display_text": "Tax" },
          { "type": "total", "amount": 10052, "display_text": "Total" }
        ],
        "fulfillment": {},
        "expires_at": "2026-02-20T15:17:07Z",
        "links": [
          { "type": "privacy_policy", "url": "https://shop.example.com/policies/privacy" },
          { "type": "terms_of_service", "url": "https://shop.example.com/policies/terms" }
        ],
        "payment": {
          "instruments": []
        },
        "attribution": {
          "utm_source": "example_agent",
          "utm_medium": "agentic_commerce",
          "utm_campaign": "spring_sale"
        },
        "messages": [],
        "continue_url": "https://shop.example.com/cart/c/abc123?key=xyz789"
    }
  }
}
```

### `complete_checkout`

Submit payment and place the order. Requires `meta["idempotency-key"]` (UUID) in addition to `meta["ucp-agent"]`. Use this tool when the checkout is ready and the buyer has authorized payment. This finalizes the transaction and creates an order.

When to use:

* Checkout status is `ready_for_complete`
* Buyer has reviewed and confirmed the order
* Payment credential has been collected

#### Parameters

***

meta•objectRequired (critical)

Request metadata. You're required to include `ucp-agent.profile`, the URI to your agent's UCP profile for capability negotiation, and an `idempotency-key`.

***

id•stringRequired (critical)

The ID of the checkout session to complete.

***

checkout•objectRequired (critical)

Checkout object containing payment credentials and finalization data. Include `checkout.payment` with the payment instrument and credential from the trusted UI. When [buyer consent](https://ucp.dev/2026-08-25/specification/shopping/extensions/buyer-consent/) is negotiated, you can also include `checkout.buyer.consent` to confirm the buyer's consent decisions.

***

#### Call from the Shopify AI Toolkit and UCP CLI

With the [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) [installed](https://shopify.dev/docs/agents#get-started), ask your assistant in natural language (`"complete the checkout"`) and the `ucp` skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command, including handing the buyer off when the merchant escalates. You can also run the command directly in a terminal:

## Complete

```bash
export UCP_ON_ESCALATION='jq -r .url | xargs open'
ucp checkout complete gid://shopify/Checkout/abc123 \
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
    "name": "complete_checkout",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-08-25/valid-with-capabilities.json"
        },
        "idempotency-key": "661e9500-f39c-52e5-b827-557766551111"
      },
      "id": "gid://shopify/Checkout/abc123?key=xyz789",
      "checkout": {
        "payment": {
          "instruments": [
            {
              "id": "pm_1234567890abc",
              "handler_id": "gpay_7k2m",
              "type": "card"
            }
          ]
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
      "ucp": {
          "version": "2026-08-25",
          "capabilities": {
            "dev.ucp.shopping.checkout": [{ "version": "2026-08-25" }],
            "dev.ucp.shopping.fulfillment": [{ "version": "2026-08-25" }]
          }
        },
        "id": "gid://shopify/Checkout/abc123?key=xyz789",
        "status": "completed",
        "currency": "USD",
        "buyer": {
          "email": "buyer@example.com"
        },
        "line_items": [
          {
            "id": "gid://shopify/CartLine/li_1?cart=abc123",
            "item": {
              "id": "gid://shopify/ProductVariant/12345678901",
              "title": "Organic Cotton Sweater",
              "price": 8900
            },
            "quantity": 2,
            "totals": [
              { "type": "subtotal", "amount": 17800 },
              { "type": "total", "amount": 17800 }
            ]
          }
        ],
        "totals": [
          { "type": "subtotal", "amount": 17800 },
          { "type": "fulfillment", "amount": 500 },
          { "type": "tax", "amount": 1466 },
          { "type": "total", "amount": 19766 }
        ],
        "order": {
          "id": "gid://shopify/Order/9876543210",
          "permalink_url": "https://shop.example.com/orders/9876543210"
        },
        "messages": []
    }
  }
}
```

### `cancel_checkout`

Cancel an active checkout session. Requires `meta["idempotency-key"]` (UUID) in addition to `meta["ucp-agent"]`. Use this tool when a buyer abandons the checkout or explicitly requests cancellation. Canceled checkouts can't be resumed. Cancellation expires the checkout immediately. The canceled checkout resource includes `expires_at`, which is set to the cancellation timestamp.

When to use:

* Buyer explicitly cancels the order
* Session has been abandoned
* Need to start fresh with a new checkout

#### Parameters

***

meta•objectRequired (critical)

Request metadata. You're required to include `ucp-agent.profile`, the URI to your agent's UCP profile for capability negotiation, and an `idempotency-key`.

***

id•stringRequired (critical)

The ID of the checkout session to cancel.

***

#### Call from the Shopify AI Toolkit and UCP CLI

With the [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) [installed](https://shopify.dev/docs/agents#get-started), ask your assistant in natural language (`"cancel this checkout"`) and the `ucp` skill picks the right [UCP CLI](https://github.com/Shopify/ucp-cli) command. You can also run the command directly in a terminal:

## Cancel

```bash
ucp checkout cancel gid://shopify/Checkout/abc123 \
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
    "name": "cancel_checkout",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-08-25/valid-with-capabilities.json"
        },
        "idempotency-key": "772f0611-f40d-63f6-c938-668877662222"
      },
      "id": "gid://shopify/Checkout/abc123?key=xyz789"
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
      "ucp": {
          "version": "2026-08-25",
          "capabilities": {
            "dev.ucp.shopping.checkout": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/checkout/", "schema": "https://ucp.dev/2026-08-25/schemas/shopping/checkout.json" }],
            "dev.ucp.shopping.fulfillment": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/extensions/fulfillment/", "schema": "https://ucp.dev/2026-08-25/schemas/shopping/fulfillment.json", "extends": ["dev.ucp.shopping.checkout", "dev.ucp.shopping.cart"] }]
          }
        },
        "id": "gid://shopify/Checkout/abc123?key=xyz789",
        "status": "canceled",
        "currency": "USD",
        "line_items": [],
        "totals": [],
        "fulfillment": {},
        "expires_at": "2026-02-20T15:17:07Z",
        "links": [],
        "payment": {
          "instruments": []
        },
        "messages": []
    }
  }
}
```

***

## Convert a cart into a checkout

When both the cart and checkout capabilities are negotiated, [`create_checkout`](#create_checkout) accepts an optional `cart_id` field in the `checkout` object. Passing a cart ID from [Cart MCP](https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp) converts the referenced cart into a checkout session.

The server applies the following rules:

* **Cart contents win.** The merchant uses the cart's `line_items`, `context`, and `buyer` when creating the checkout and ignores any overlapping fields in the `checkout` payload. Any `attribution` in the `checkout` payload is still applied to the checkout.
* **`checkout` and `line_items` are still required.** Send `cart_id` inside the `checkout` object, and pass `line_items` as an empty array (`"line_items": []`). The cart's line items are used instead.
* **Discount codes must be forwarded.** If the cart has applied discount codes, include those codes in `checkout.discounts.codes`. Don't assume Shopify re-applies cart discount codes automatically during conversion.
* **Idempotent conversion.** If an incomplete checkout already exists for the cart, the server returns that existing session rather than creating a new one. Safe to retry.
* **Linked lifecycle.** The cart remains linked to the checkout for the duration of the checkout. This supports back-to-storefront flows where the buyer returns to the cart on the merchant site.

The server returns business outcomes when `cart_id` can't be resolved:

* `invalid_cart_id`: The `cart_id` isn't a valid Shopify GID.
* `cart_not_found`: The cart doesn't exist or has expired.

**Note:**

`cart_id` is currently accepted as input but is **not returned** on checkout response objects. Store the cart ID on your side if you need to reference it after conversion.

POST

## https://{shop-domain}/api/ucp/mcp

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "id": 1,
  "params": {
    "name": "create_checkout",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://shopify.dev/ucp/agent-profiles/examples/2026-08-25/valid-with-capabilities.json"
        }
      },
      "checkout": {
        "cart_id": "gid://shopify/Cart/cart_abc123",
        "line_items": []
      }
    }
  }
}
```

***

## Checkout status

### General access

For most partners referring checkout sessions from Catalog, each response from [`create_checkout`](#create_checkout), [`get_checkout`](#get_checkout), and [`update_checkout`](#update_checkout) includes:

* `status`: `requires_escalation`
* `messages`: an array of message objects, each with `type` and `severity`. The message's `severity` is `requires_buyer_input` (merchant needs input not available via API), `requires_buyer_review` (the buyer hasn't opted in to the channel, or the checkout otherwise requires review not available via API), or `recoverable` depending on the condition.
* `continue_url` for handing off to the merchant storefront

When the session is ready for the buyer to finish on the storefront, present the `continue_url`. For general access, directing buyers to that URL is how checkout completes; you do not call [`complete_checkout`](#complete_checkout).

Append query parameters to `continue_url` for attribution, such as UTM tags:

```text
https://merchant.example/checkout/cn/...?utm_source=your_agent&utm_medium=agentic_commerce&utm_campaign=example
```

## General access terminal state (example)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "structuredContent": {
      "id": "gid://shopify/Checkout/...",
      "status": "requires_escalation",
      "messages": [
        {
          "type": "error",
          "severity": "requires_buyer_input"
        }
      ],
      "continue_url": "https://merchant.com/checkout/..."
    }
  }
}
```

### Lifecycle

Every tool response includes `status` and a `messages` array. Each message has a `severity` that reflects the resource state and recommended action.

Build for escalations regardless of how you authenticate. When `status` is `incomplete` or `requires_escalation`, use `severity` to decide the next step: call `update_checkout` to resolve `recoverable` messages, or direct the buyer to `continue_url` when messages include `severity: requires_buyer_input` or `severity: requires_buyer_review`. When `status` is `ready_for_complete`, you can call [`complete_checkout`](#complete_checkout) to place the order in your application; otherwise, the buyer finishes on the merchant's checkout via `continue_url`.

See the [checkout status lifecycle](https://ucp.dev/2026-08-25/specification/shopping/checkout/#checkout-status-lifecycle) in the UCP spec for the full reference.

| Status | Description |
| - | - |
| `incomplete` | Checkout is missing required information. Inspect `messages` (including each message's `severity`) and resolve via `update_checkout`. |
| `requires_escalation` | Checkout requires buyer input or review not available via API. Check `messages` for `severity: requires_buyer_input` or `severity: requires_buyer_review` and hand off to the buyer via `continue_url`. |
| `ready_for_complete` | All information is collected. Call [`complete_checkout`](#complete_checkout) or hand off via `continue_url`. |
| `complete_in_progress` | Merchant is processing the `complete_checkout` request. |
| `completed` | Order placed successfully. |
| `canceled` | Checkout session is invalid or expired. Start a new session if needed. |

### Interpret `get_checkout` responses

`get_checkout` returns the current checkout resource, but the payload can change as the checkout moves through its lifecycle. Use `status` as the source of truth for the checkout state, and inspect `messages` for missing information or required buyer action.

When `status` is `completed`, use `order` as the purchase confirmation signal. Other response fields can vary by status, merchant configuration, and negotiated capabilities.

| Status | What to do |
| - | - |
| `incomplete` | Use `messages` to determine what to send in the next `update_checkout` request. |
| `requires_escalation` | Hand off to the buyer with `continue_url` when it's present. |
| `ready_for_complete` | Call [`complete_checkout`](#complete_checkout) or hand off to the buyer. |
| `complete_in_progress` | Wait for the merchant to finish processing the `complete_checkout` request, then retrieve the checkout again. |
| `completed` | Read `order` instead of relying on nonterminal checkout fields. |
| `canceled` | Start a new checkout session. |

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

Application-level results (including conditions like an expired session, unavailable merchandise, an invalid address, or a declined payment) are returned as a successful JSON-RPC `result` with `structuredContent` and a `messages` array. The request was processed; the outcome is in the payload.

Inspect `result.structuredContent` and its `messages` array. Use message `type`, `code`, and optional `path` to adjust your flow (for example, prompt the buyer to fix an address or direct them to `continue_url`).

Cart responses use a different envelope. See [Business outcomes on Cart MCP](https://shopify.dev/docs/agents/carts-and-checkout/cart-mcp#business-outcomes) when working with cart tools.

## Business outcome (result with messages)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "structuredContent": {
      "ucp": { "version": "2026-08-25", "capabilities": { "dev.ucp.shopping.checkout": [{ "version": "2026-08-25", "spec": "https://ucp.dev/2026-08-25/specification/shopping/checkout/" }] } },
      "id": "gid://shopify/Checkout/abc123?key=xyz789",
      "status": "incomplete",
      "line_items": [
        { "id": "gid://shopify/CartLine/li_1?cart=abc123", "quantity": 1 }
      ],
      "messages": [
        {
          "type": "error",
          "code": "address_invalid",
          "content": "Shipping address is missing a postal code",
          "path": "$.fulfillment.methods[0].destinations[0].postal_code"
        }
      ],
      "continue_url": "https://shop.example.com/checkouts/c/abc123?key=xyz789"
    }
  }
}
```

***

