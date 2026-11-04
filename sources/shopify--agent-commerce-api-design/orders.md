# Order boundaries

Canonical URL: https://shopify.dev/docs/agents/orders
Retrieved: 2026-11-04
Capture URL: https://shopify.dev/docs/agents/orders.md
Capture: official Markdown (or text extraction if HTML); no diagram-dependent claims.

---

---
title: About orders
description: >-
  Monitor order lifecycle changes after checkout completion using UCP-shaped
  order webhooks and the get_order MCP tool.
source_url:
  html: 'https://shopify.dev/docs/agents/orders'
  md: 'https://shopify.dev/docs/agents/orders.md'
---

# About orders

After checkout completes, your agent can monitor the order's lifecycle: fulfillment events, returns, refunds, exchanges, and order edits.

Shopify's order capability (`dev.ucp.shopping.order`) implements the [UCP order specification](https://ucp.dev/2026-08-25/specification/shopping/order/) and exposes two surfaces:

* **[Order MCP](#order-mcp)**: The `get_order` tool fetches the current state of an order on demand. Use it for buyer-initiated views, reconciling dropped webhook deliveries, or any case where you need fresh state right now.
* **[Order webhooks](#order-webhooks)**: Shopify pushes the full current order state to your endpoint whenever a committed change occurs. Use webhooks as the primary signal for proactive notifications and timeline UIs.

**Caution:**

Tool use is subject to access and rate limiting that scale with how your agent identifies itself. See [Auth and rate limiting](https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting) for traffic tiers and what each can do.

***

## How it works

Your agent originates a checkout using [Checkout MCP](https://shopify.dev/docs/agents/carts-and-checkout/checkout-mcp) or [Embedded Checkout Protocol](https://shopify.dev/docs/agents/carts-and-checkout/ecp). After the checkout is complete, your agent can:

* Receive order webhooks at your registered endpoint as the order moves through fulfillment and post-purchase changes.
* Call `get_order` at any time to fetch the current state of an order by ID.

### Payload

Order MCP and order webhooks serialize the same fields in the same shape. The response from `get_order` matches the payload Shopify pushes to your webhook URL.

For the field-level reference and an example payload, see the [Order data model](https://shopify.dev/docs/agents/orders/order-mcp#order-data-model) on the Order MCP page.

If your agent negotiates the [declared fields extension](https://shopify.dev/docs/agents/carts-and-checkout/declared-fields), then orders also include a read-only `declared_fields` array with the values captured at checkout. For details, see [Order behavior](https://shopify.dev/docs/agents/carts-and-checkout/declared-fields#order-behavior).

### Capability negotiation

The order capability is automatically advertised on every shop's `/.well-known/ucp` document at UCP `2026-04-08` or later. There's no shop-level flag or gating to enable it.

If your agent's profile declares `dev.ucp.shopping.order` at a supported version, the capability is negotiated automatically.

### Order access

Your agent can fetch only orders that were facilitated through it. Orders placed through other channels or experiences are not accessible using this capability.

### UCP versions

The order capability requires UCP `2026-04-08` or later. It isn't offered on `2026-01-23`: agents negotiating that version don't see `get_order` in `tools/list`.

If your agent still negotiates `2026-01-23`, move to `2026-04-08` or later to use orders.

### When to use which surface

Pick the surface that matches how the update is triggered. Use webhooks when Shopify pushes a change to react to, and `get_order` when your agent needs to read the current state on demand.

| Use case | Recommended approach |
| - | - |
| Proactive buyer notifications (shipping updates, refund confirmations) | Webhooks |
| Buyer-initiated "Where's my order?" views | `get_order` |
| Reconciling missed webhook deliveries | `get_order` |
| Building a timeline of post-purchase changes | Webhooks |

**Info:**

Webhooks are the primary update channel. Use `get_order` for reconciliation and on-demand reads. Don't reconstruct order state by replaying webhook history. Each delivery contains the full current state of the order.

***

## Order MCP

[Order MCP](https://shopify.dev/docs/agents/orders/order-mcp) implements the UCP order capability over JSON-RPC. The capability exposes a single tool for retrieving an order on demand. Requests require a Global API JWT with the `read_global_api_orders` scope.

| Tool | Description |
| - | - |
| [`get_order`](https://shopify.dev/docs/agents/orders/order-mcp#get_order) | Fetch the current state of an order by ID. |

***

## Order webhooks

[Order webhooks](https://shopify.dev/docs/agents/orders/order-webhooks) deliver the full current order state to your registered endpoint whenever a committed change occurs. Every delivery has the same UCP-shaped payload, so route all order webhooks through the same handler and inspect the data to determine what changed. Don't branch on the topic name.

For reference, deliveries fire on three underlying topics:

| Topic | When it fires |
| - | - |
| `orders/create` | A new order is placed through your agent. |
| `orders/updated` | The order changes (payment captured, fulfillment progresses, an adjustment commits, or other internal updates). |
| `orders/delete` | An order is deleted. The payload still contains the order's last-known state. |

**Info:**

Delivery URL and topic are configured by Shopify. To subscribe or update an existing subscription, contact your Shopify partner manager.

***

## Next steps

[Try the UCP CLI quickstart\
\
](https://shopify.dev/docs/agents/get-started/quickstart)

[Run the full agentic commerce flow, including order tracking, with the UCP CLI.](https://shopify.dev/docs/agents/get-started/quickstart)

[Order MCP\
\
](https://shopify.dev/docs/agents/orders/order-mcp)

[Fetch the current state of an order on demand using the `get_order` tool.](https://shopify.dev/docs/agents/orders/order-mcp)

[Order webhooks\
\
](https://shopify.dev/docs/agents/orders/order-webhooks)

[Subscribe to order lifecycle events delivered to your endpoint as the full current order state.](https://shopify.dev/docs/agents/orders/order-webhooks)

[UCP order specification\
\
](https://ucp.dev/2026-08-25/specification/shopping/order/)

[Read the canonical UCP order capability specification.](https://ucp.dev/2026-08-25/specification/shopping/order/)

***

