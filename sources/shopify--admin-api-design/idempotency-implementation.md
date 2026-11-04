---
title: Implementing idempotency
description: >-
  Learn how to implement idempotency in applications that call the Shopify
  GraphQL Admin API.
source_url:
  html: >-
    https://shopify.dev/docs/apps/build/apis/graphql-admin/implementing-idempotency
  md: >-
    https://shopify.dev/docs/apps/build/apis/graphql-admin/implementing-idempotency.md
---

# Implementing idempotency

This page provides detailed guidance on implementing idempotency on the client-side when calling certain GraphQL Admin API mutations.

The information on this page, in particular, implementation-specific details such as error codes and the retention window, only applies to mutations that support the `@idempotent` directive, because idempotency was built into these mutations in a similar way. Learn more about [idempotency directive syntax](https://shopify.dev/docs/api/usage/idempotent-requests).

***

## Understanding idempotency

### Core principles

Understanding these two principles helps you implement idempotency correctly:

**Principle 1: Distinct requests need different idempotency keys**

Each distinct request should have its own unique idempotency key. We **strongly** recommend using UUIDs to ensure uniqueness.

**Principle 2: Duplicate requests must use the same idempotency key**

For the purposes of this documentation, a 'duplicate request' is one that has the same mutation variables and is **not intended to be a separate operation** from the original request. Duplicate requests must reuse the same idempotency key to enable deduplication and concurrency protection.

**What qualifies as a duplicate request:**

* Accidental double-clicks that send additional requests with identical parameters.
* Network retries with the exact same parameters after a timeout or connection failure.
* Job retries that resubmit the same operation after an initial failure.

**What doesn't qualify as a duplicate request:**

A request whose mutation variables are exactly identical to those of the first request isn't a duplicate request if it's *intended to result in a separate operation* being performed. Consider this scenario:

1. The client makes a first request to increment their inventory by +2 due to having received inventory from supplier A.
2. The client makes a second request with identical mutation variables to increment their inventory by +2, due to having received inventory from supplier B.
3. The intent for these two requests is different: they are meant to be performing *separate operations*. Here, the client isn't retrying the first inventory adjustment, they're trying to create a second, entirely new inventory adjustment.
4. The onus is on the client to decide when to use identical or different idempotency keys, because only the client is aware if they're intending to perform a separate operation or not.

**Common mistake:**

Avoid generating a new random UUID every time you call the mutation. This violates Principle 2 and prevents proper idempotency protection, because every request is treated as distinct.

### How idempotency protection is implemented on the server-side

Shopify tracks idempotency keys for **24 hours** from the original request. During this window, all duplicate requests with the same idempotency key are handled according to the original request's status:

**Concurrent requests**

When multiple duplicate requests arrive in quick succession while the first request is still processing, Shopify returns `IDEMPOTENCY_CONCURRENT_REQUEST` to subsequent requests instead of processing them. This protects against race conditions and duplicate operations.

**Successful request retries**

After the original request completes successfully, any duplicate requests with the same idempotency key receive the cached GraphQL response without reprocessing the operation. This ensures safe retries without duplication.

Note that on rare occasions, the cached GraphQL response may not be the same as the original one, as the cached response is constructed from database records, which may have changed since the original successful response. The below scenario illustrates this:

*Example scenario*:

1. Client A calls the [`locationActivate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/locationActivate) mutation with the idempotency key 'abc'. The location is successfully activated, so in the response, [`isActive`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/locationActivate#returns-location.fields.isActive) is `true`.
2. Client B calls the [`locationDeactivate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/locationDeactivate) mutation with the idempotency key 'def'. The same location is successfully deactivated, and the database records are updated accordingly.
3. Client A calls the [`locationActivate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/locationActivate) mutation with the idempotency key 'abc'. Since the idempotency key is the same, no activation logic will be triggered, and a cached response will be returned instead.
4. Since this cached response is constructed from the current database state, [`isActive`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/locationActivate#returns-location.fields.isActive) will be `false` in the cached response.

**Failed request retries**

When the original request fails to process, duplicate requests might receive either:

* `IDEMPOTENCY_CONCURRENT_REQUEST` if the original request is stalled or still marked as in-progress.
* An error with a suitable message for example, "The refund couldn't be processed."

**24-hour retention window**

After 24 hours, idempotency keys expire and are no longer recognized as duplicates. Thus, retries that occur beyond this window (such as long-delayed job retries), will not have idempotency protection, and will be treated as separate operations.

***

## Best practices for using idempotency keys

Following these best practices ensures reliable, safe retries in your application.

### Generating idempotency keys

**Use UUIDs (v4 or v7)**: Generate a random universally unique identifier for each unique operation.

```javascript
// Example: JavaScript with crypto.randomUUID()
const idempotencyKey = crypto.randomUUID();
// Result: "3f5b6ebf-143c-4da5-8d0f-fb8553bfd85d"
```

```ruby
# Example: Ruby with SecureRandom
idempotency_key = SecureRandom.uuid
# Result: "3f5b6ebf-143c-4da5-8d0f-fb8553bfd85d"
```

**For deterministic scenarios (background jobs, services)**: Suppose you have a collection of parameters (that is, mutation variables) and stable identifiers (for example, the unique id of a retrying job) which, taken together, uniquely identify distinct requests. In this case, you can use UUID v5 to generate deterministic keys from using those parameters/identifiers as inputs:

```javascript
// Example: Generate deterministic key for a job retry
import { v5 as uuidv5 } from 'uuid';


const namespace = '6ba7b810-9dad-11d1-80b4-00c04fd430c8'; // Your app namespace
const jobParams = `${jobId}-${JSON.stringify(mutationVariables)}`;
const idempotencyKey = uuidv5(jobParams, namespace);


// Same job + variables always produces the same key
```

This approach ensures duplicate job retries use the same idempotency key while different jobs or parameters produce unique keys.

### Storing idempotency keys

**Before sending the request**, you should generally persist the idempotency key along with the operation intent. You should come up with the best persistence strategy that aligns with your application's architecture.

**Why persist first**: If your application crashes after sending the request but before recording the key, you risk losing the ability to safely retry or verify the operation succeeded.

**Note:**

If you're generating the idempotency key deterministically, then you don't need to persist the idempotency key—you can just recreate it from the same parameters / stable identifiers if you want to reuse it.

**For web and mobile apps**: You can persist the key by attaching the idempotency key to the page or screen lifecycle:

```javascript
// Example: React component managing idempotency
function InventoryAdjustmentForm() {
  // Generate key on component mount, persists during page lifecycle
  const idempotencyKeyRef = useRef(crypto.randomUUID());


  const handleSubmit = async (formData) => {
    try {
      await adjustInventory(formData, idempotencyKeyRef.current);
      // Success - regenerate key for next submission
      idempotencyKeyRef.current = crypto.randomUUID();
    } catch (error) {
      // Error - keep same key for retry on this page
      handleError(error);
    }
  };


  return <form onSubmit={handleSubmit}>...</form>;
}
```

This pattern ensures that additional requests sent (due to say, double-clicking) before receiving a successful response all use the same idempotency key, allowing the server to deduplicate them. After a successful response, the key regenerates so the next submission is treated as a new operation.

### When to generate a new key

Generate a **new** idempotency key when:

* Starting a genuinely new operation (different intent).
* Modifying any request parameters from the original.

**Reuse** the same idempotency key when:

* Retrying after a backend processing failure, a network failure or a timeout.
* Retrying after receiving an `IDEMPOTENCY_CONCURRENT_REQUEST` error.
* Resubmitting an operation you're unsure has completed, in order to check on its status

**Tip:**

In practice, what the above guidelines usually translates to is this: "*If you receive a successful response from the backend, generate a new key (so you can use it in subsequent genuinely new operations). If you receive a failed response from the backend, reuse the same key (so you can safely retry)*".

If you are certain you want to retry the request as a **separate operation** following a failed response, and have verified that this won't result in unintended duplicate processing, you may regenerate a new key after a failed response.

***

## Using idempotency with bulk operations

You can use the `@idempotent` directive with [bulk mutation operations](https://shopify.dev/docs/apps/build/apis/graphql-admin/bulk-operations/imports). When you do, idempotency is applied per row in your JSONL input file, not per the entire bulk operation. Each row in the JSONL file represents a separate mutation call, and each one needs its own unique idempotency key. Don't use the same key for every row — reusing a single key across rows causes rows after the first to be treated as duplicates.

The same [best practices for idempotency keys](#best-practices-for-using-idempotency-keys) apply to bulk operations. If you retry the bulk operation, reuse the same keys for the same rows. If you use deterministic key generation (UUID v5), you can regenerate identical keys from the same input parameters without persisting them.

To pass the idempotency key, declare it as a variable in the mutation string and provide its value in each line of the JSONL file, alongside the other mutation arguments.

### Example: Bulk inventory adjustment with idempotency

#### Step 1: Define the mutation string with a variable for the key

When you pass the mutation to `bulkOperationRunMutation`, use a variable for the `@idempotent` directive's `key` argument:

## Mutation string

```graphql
mutation call($input: InventoryAdjustQuantitiesInput!, $idempotencyKey: String!) {
  inventoryAdjustQuantities(input: $input) @idempotent(key: $idempotencyKey) {
    inventoryAdjustmentGroup {
      id
    }
    userErrors {
      field
      message
      code
    }
  }
}
```

#### Step 2: Include the idempotency key in each JSONL row

Each line in the JSONL file provides the `idempotencyKey` variable alongside the `input` variable. Every row must have its own unique key:

## JSONL input file

```json
{ "input": { "reason": "correction", "name": "available", "changes": [{ "delta": 1, "inventoryItemId": "gid://shopify/InventoryItem/1", "locationId": "gid://shopify/Location/1" }] }, "idempotencyKey": "a1b2c3d4-e5f6-7890-abcd-ef1234567890" }
{ "input": { "reason": "correction", "name": "available", "changes": [{ "delta": 5, "inventoryItemId": "gid://shopify/InventoryItem/2", "locationId": "gid://shopify/Location/1" }] }, "idempotencyKey": "b2c3d4e5-f6a7-8901-bcde-f12345678901" }
{ "input": { "reason": "correction", "name": "available", "changes": [{ "delta": -3, "inventoryItemId": "gid://shopify/InventoryItem/3", "locationId": "gid://shopify/Location/2" }] }, "idempotencyKey": "c3d4e5f6-a7b8-9012-cdef-123456789012" }
```

#### Step 3: Run the bulk mutation

## POST https://{shop}.myshopify.com/admin/api/{api\_version}/graphql.json

```graphql
mutation {
  bulkOperationRunMutation(
    mutation: "mutation call($input: InventoryAdjustQuantitiesInput!, $idempotencyKey: String!) { inventoryAdjustQuantities(input: $input) @idempotent(key: $idempotencyKey) { inventoryAdjustmentGroup { id } userErrors { field message code } } }",
    stagedUploadPath: "tmp/21759409/bulk/89e620e1-0252-43b0-8f3b-3b7075ba4a23/bulk_op_vars"
  ) {
    bulkOperation {
      id
      status
    }
    userErrors {
      field
      message
    }
  }
}
```

***

## Understanding idempotency errors

When working with idempotent requests, you might encounter specific error codes that help you understand what went wrong and how to proceed. These errors are typically returned in the `userErrors` array with a `code` field that identifies the specific idempotency issue.

### IDEMPOTENCY\_​KEY\_​PARAMETER\_​MISMATCH

**What it means**: You're attempting to reuse an idempotency key with different request parameters than the original request.

**Error response**:

```json
{
  "userErrors": [
    {
      "field": null,
      "message": "The same idempotency key cannot be used with different operation parameters.",
      "code": "IDEMPOTENCY_KEY_PARAMETER_MISMATCH"
    }
  ]
}
```

**What causes this**: Shopify fingerprints each request's parameters. If you retry with the same idempotency key but different inputs (different quantities, different item IDs, and so on), this error occurs. This error indicates incorrect usage of idempotency on the client side- it might be caused by the client incorrectly implementing idempotency, so it's failing to regenerate a unique idempotency key after receiving a successful GraphQL response from the original request.

**How to handle**:

* If you intended for the second request with different parameters to be processed as a *separate operation*, you should generate a new idempotency key for the modified request.
* If you intended for the second request to be a retry of the original request, you should change the parameters back to exactly match what they were originally, and retry the original request with the same idempotency key.

**Note:**

By default, request parameters include all input fields. Usually, changing any value—even a single quantity or ID—requires a new idempotency key.

However, for some mutations, parameters like timestamps may be omitted from the fingerprint, so it's acceptable to reuse the idempotency key even if the timestamp changes. If there are parameters that do not form part of the fingerprinting, these should be mentioned in the mutation description.

Additionally, parameter order can affect fingerprinting. Ensure your client consistently orders input fields to avoid unexpected parameter mismatches.

### IDEMPOTENCY\_​CONCURRENT\_​REQUEST

**What it means**: Another request with the same idempotency key is currently being processed.

**Error response**:

```json
{
  "userErrors": [
    {
      "field": null,
      "message": "This request is currently in progress, please try again.",
      "code": "IDEMPOTENCY_CONCURRENT_REQUEST"
    }
  ]
}
```

**What causes this**: Your application made multiple simultaneous requests with the same idempotency key before the first request completed.

**How to handle**: Wait briefly (exponential backoff recommended) and retry with the same idempotency key. The original request completes, and subsequent retries receive the cached result.

### Miscellaneous 'NOT\_​FOUND' errors

Errors in this category are domain-specific 'Not Found' errors such as `LOCATION_NOT_FOUND`, `SHIPMENT_NOT_FOUND` or `PURCHASE_ORDER_NOT_FOUND`.

**What it means**: The business data that was associated with, or created by, your original request has been deleted from the database.

**Error response**:

```json
{
  "userErrors": [
    {
      "field": null,
      "message": "The location couldn't be found",
      "code": "LOCATION_NOT_FOUND"
    }
  ]
}
```

**What causes this**: Receiving this error indicates that the original request was successfully completed, but the backend business data associated with the original request was subsequently deleted by a separate process.

**How to handle**: The client is working with stale data, so they should verify the system state before proceeding. If they are absolutely sure that they want to recreate the deleted record, then they should call the mutation again with a different idempotency key.

**Example scenario**:

1. Shop owner A schedules an inventory adjustment of +50 units on his app using idempotency key `abc-123` because he thinks he'll be receiving new inventory next week.
2. The request completes successfully, creating a scheduled change database record, but Owner A doesn't receive a successful response on his app due to network problems.
3. Soon after, Shop Owner B sees that scheduled change in her app and manually cancels it because she knows the delivery next week is no longer happening due to a product shortage.
4. Then, Shop Owner A retries the request because he didn't get a successful response the first time.
5. Shop Owner A gets the 'Not Found' error.
6. Rather than retrying the request with a different idempotency key, he should investigate the system state—this would lead him to discover that the scheduled change was created, but then manually deleted by Owner B for a valid reason, so he wouldn't retry the request.

***

## List of mutations supporting the `@idempotent` directive

This list was last updated 2 February 2026. To check if a mutation supports the `@idempotent` directive on a given API version, check the mutation descriptions using the following links (or equivalent links, if the mutation you want to check is not in the list). If a mutation supports the directive, this is explicitly mentioned in the description.

1. [`inventoryActivate`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventoryActivate)
2. [`inventoryAdjustQuantities`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventoryAdjustQuantities)
3. [`inventoryMoveQuantities`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventoryMoveQuantities)
4. [`inventorySetOnHandQuantities`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventorySetOnHandQuantities)
5. [`inventorySetQuantities`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventorySetQuantities)
6. [`inventorySetScheduledChanges`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventorySetScheduledChanges)
7. [`inventoryShipmentAddItems`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventoryShipmentAddItems)
8. [`inventoryShipmentCreate`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventoryShipmentCreate)
9. [`inventoryShipmentCreateInTransit`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventoryShipmentCreateInTransit)
10. [`inventoryShipmentReceive`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventoryShipmentReceive)
11. [`inventoryTransferCreate`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventoryTransferCreate)
12. [`inventoryTransferCreateAsReadyToShip`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventoryTransferCreateAsReadyToShip)
13. [`inventoryTransferDuplicate`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventoryTransferDuplicate)
14. [`inventoryTransferSetItems`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/inventoryTransferSetItems)
15. [`locationActivate`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/locationActivate)
16. [`locationDeactivate`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/locationDeactivate)
17. [`refundCreate`](https://shopify.dev/docs/api/admin-graphql/2026-01/mutations/refundCreate)

***
