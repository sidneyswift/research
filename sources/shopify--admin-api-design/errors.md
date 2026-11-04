---
title: Shopify API response status and error codes
description: >-
  Learn what each HTTP status code from Shopify's APIs means and what to do
  about it, and how the GraphQL APIs report errors.
source_url:
  html: 'https://shopify.dev/docs/api/usage/response-codes'
  md: 'https://shopify.dev/docs/api/usage/response-codes.md'
---

# Shopify API response status and error codes

When Shopify receives a request to an API endpoint, it returns an HTTP status code with the response headers. On the GraphQL APIs, it also reports failures in the response body, in an `errors` array.

This page covers both: what each status code means and what to do about it, and how [the GraphQL APIs report errors](#graphql-error-handling) instead.

***

## Graph​QL error handling

On a GraphQL API, the status code describes the HTTP request, not the operation you asked for. Every GraphQL operation is a `POST` to a single endpoint, so when Shopify receives that request and answers it, the status is `200 OK` — even if the operation inside it failed. The failure is reported in the response body instead, in an `errors` array:

```json
{
  "errors": [
    {
      "message": "Throttled",
      "extensions": {
        "code": "THROTTLED"
      }
    }
  ]
}
```

So a `200` from a GraphQL API means Shopify answered, not that the operation worked. Check for an `errors` array before treating the response as a success, and read `errors[n].extensions.code` instead of branching on the status code.

### Where to find each API's error codes

Each GraphQL API documents its own error codes, because the codes and the conditions that produce them differ by API.

| API | Error codes |
| - | - |
| GraphQL Admin API | [Error handling](https://shopify.dev/docs/api/admin-graphql#error-handling) |
| Storefront API | [Error handling](https://shopify.dev/docs/api/storefront#error-handling) |
| Customer Account API | [Error handling](https://shopify.dev/docs/api/customer#error-handling) |
| Payments Apps API | [Error handling](https://shopify.dev/docs/api/payments-apps#error-handling) |
| Partner API | [Error handling](https://shopify.dev/docs/api/partner#error-handling) |

The Partner API uses numeric strings for its `errors[n].extensions.code` values, such as `"429"` and `"500"`, which match the HTTP status codes on this page. The other GraphQL APIs use symbolic names, such as `THROTTLED` and `INTERNAL_SERVER_ERROR`.

The REST Admin API doesn't return an `errors[n].extensions.code` value. It reports errors through the status codes on this page, with details in the response body's `errors` or `error` parameter.

***

## Common status codes

The following codes have Shopify-specific causes or remedies. If the code you're looking for isn't here, then see [Standard HTTP status codes](#standard-http-status-codes).

### `400 Bad Request`

The request wasn't understood by the server, generally due to bad syntax or because the `Content-Type` header wasn't correctly set to `application/json`.

This status is also returned when a [token exchange](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens#token-exchange-grant) request includes an expired or otherwise invalid ID token, and when a request provides an invalid `code` parameter during the [authorization code grant](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens#authorization-code-grant).

### `401 Unauthorized`

The necessary [authentication credentials](https://shopify.dev/docs/apps/build/authentication-authorization) aren't present in the request or are incorrect.

An expired access token also returns this status, so re-authenticate to obtain a new one. For how long each token lasts, see [token lifetimes](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens#token-lifetimes).

A refresh token that can no longer be used returns this status with the error code `invalid_request` and the description `This request requires an active refresh_token`. Treat it as final rather than retrying. See [refreshing an expiring offline access token](https://shopify.dev/docs/apps/build/authentication-authorization/implement-token-exchange#refresh-an-expiring-offline-token).

### `402 Payment Required`

The requested shop is currently frozen. The shop owner needs to log in to the shop's admin and pay the outstanding balance to unfreeze the shop.

### `403 Forbidden`

The server is refusing to respond to the request. On the [REST Admin API](https://shopify.dev/docs/api/admin-rest), this status is generally returned if you haven't [requested the appropriate scope](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes) for this action.

The GraphQL Admin, Storefront, and Payments Apps APIs report a missing scope differently: the request returns `200 OK` with `ACCESS_DENIED` in `errors[n].extensions.code`, so don't branch on a `403` to detect one. On the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql), a `403` means the store has been marked as fraudulent.

Starting April 1, 2027, a request to the GraphQL Admin API or the REST Admin API that presents a public app's non-expiring offline access token also returns this status. The response's `errors` value contains `Non-expiring access tokens are no longer accepted for the Admin API`, so you can tell it apart from a missing-scope `403`. To stop hitting it, see [Migrate to expiring offline access tokens](https://shopify.dev/docs/apps/build/authentication-authorization/migrate-to-expiring-offline-access-tokens).

### `404 Not Found`

The requested resource wasn't found, but might be available again in the future.

### `422 Unprocessable Entity`

The request body was well-formed but contains semantic errors. On the REST Admin API, a `422` can be returned from a variety of scenarios, including, but not limited to:

* Incorrectly formatted input
* Checking out products that are out of stock
* Canceling an order that has fulfillments
* Creating an order with tax lines on both line items and the order
* Creating a customer without an email or name
* Creating a product without a title

The response body provides details in the `errors` or `error` parameters.

### `423 Locked`

The requested shop is currently locked. Shops are locked if they repeatedly exceed their API request limit, or if there's an issue with the account, such as a detected compromise or fraud risk.

[Contact support](https://help.shopify.com/en/questions#/contact) if your shop is locked.

### `429 Too Many Requests`

The request wasn't accepted because the app has exceeded the rate limit. Learn more about [Shopify's API rate limits](https://shopify.dev/docs/api/usage/limits#rate-limits).

The GraphQL Admin, Storefront, Customer Account, and Payments Apps APIs don't use this status code for rate limiting. They return `200 OK` and report it in the response body as a `THROTTLED` error instead. The Partner API does return `429`, with `"429"` as its `errors[n].extensions.code` value. See [where to find each API's error codes](#where-to-find-each-apis-error-codes).

### `430 Shopify Security Rejection`

The request wasn't accepted because it might be malicious, and Shopify rejected it to protect the app from any possible attacks.

On the Storefront API, check that server-side requests include the correct [Buyer IP header](https://shopify.dev/docs/api/storefront#make-server-side-requests-with-a-private-access-token).

***

## Server error codes

Shopify returns a `5xx` code when it can't complete an otherwise valid request. Most are transient, so retry the request, and check the [Shopify status page](https://www.shopifystatus.com/) if the failure persists.

| Status code | Description |
| - | - |
| `500 Internal Server Error` | An internal error occurred in Shopify. Simplify or retry your request. If a large query fails repeatedly, then reduce the number of objects per page or split it into smaller requests instead of retrying it unchanged. If the issue persists, then record any error codes and timestamps and [contact Partner Support](https://help.shopify.com/en/questions/partners) so that Shopify staff can investigate. The GraphQL Admin, Storefront, Customer Account, and Payments Apps APIs report this in the response body as an `INTERNAL_SERVER_ERROR` error instead; the Partner API reports it as `"500"`. See [where to find each API's error codes](#where-to-find-each-apis-error-codes). |
| `501 Not Implemented` | The requested endpoint isn't available on that particular shop, for example requesting access to a Shopify Plus-only API on a non-Plus shop. This response might also indicate that the endpoint is reserved for future use. |
| `502 Bad Gateway` | Shopify's gateway received an invalid response from an upstream server. Retry the request, and check the [Shopify status page](https://www.shopifystatus.com/) if it persists. |
| `503 Service Unavailable` | The server is currently unavailable. Check the [Shopify status page](https://www.shopifystatus.com/) for reported service outages. |
| `504 Gateway Timeout` | The request couldn't complete in time. Shopify waits up to 10 seconds for a response. Try breaking it down into multiple smaller requests. |
| `530 Origin DNS Error` | Cloudflare can't resolve the requested DNS record. Check the [Shopify status page](https://www.shopifystatus.com/) for reported service outages. |
| `540 Temporarily Disabled` | The requested endpoint isn't currently available. It's been temporarily disabled, and will be back online shortly. |

***

## Standard HTTP status codes

Shopify returns the following codes with their standard HTTP meanings.

| Status code | Description |
| - | - |
| `200 OK` | The request was successfully processed by Shopify. On a GraphQL API, check the response body for an `errors` array before treating a `200` as a success. |
| `201 Created` | The request has been fulfilled and a new resource has been created. |
| `202 Accepted` | The request has been accepted, but not yet processed. |
| `204 No Content` | The request succeeded, and the response has no body. |
| `205 Reset Content` | The request succeeded, and the client should reset the document view that sent the request. |
| `303 See Other` | The response to the request can be found under a different URL in the `Location` header, and can be retrieved using a `GET` request to that resource. |
| `405 Method Not Allowed` | The server recognizes the request but rejects the specific HTTP method. |
| `406 Not Acceptable` | The request's `Accept` header doesn't specify any content formats that the server is able to fulfill. |
| `409 Conflict` | The requested resource couldn't be processed because of a conflict in the request. For example, the requested resource might not be in an expected state, or processing the request would create a conflict within the resource. |
| `414 URI Too Long` | The server is refusing to accept the request because the Uniform Resource Identifier (URI) provided was too long. |
| `415 Unsupported Media Type` | The request's `Content-Type` header specifies a payload format that the server doesn't support. |

***
