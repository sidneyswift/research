# API fundamentals

URL: https://docs.gusto.com/embedded-payroll/docs/api-fundamentals
Retrieved: 2026-11-04
Version: n/a (living page). Rendered-text capture; images/layout not preserved.

---

The Gusto Embedded API behavior is built on core fundamentals that apply to every endpoint.
These determine how information is displayed, how we handle identical requests, the number of requests you can make per minute, and the actions your application can take.
Pagination
To enhance API performance, several collection endpoints support pagination. To use this feature, add a page and optionally a per parameter to the URL query string.
For example
https://api.gusto.com/v1/companies/abc123/employees?page=2&per=5
returns the second page of five employees for the company identified by UUID
abc123
. If the per parameter is not included, the API returns 25 records per page, unless otherwise specified.
Each endpoint that supports pagination will be mentioned in its respective documentation.
Paginated responses
When pagination parameters are included, metadata will be returned in the response headers, as in this example:
X-Page: 3
X-Total-Count: 542
X-Total-Pages: 22
X-Per-Page: 20
Header
Description
Example
X-Page
The current page being returned
3
X-Total-Count
Total number of records in the full collection
542
X-Total-Pages
Total number of pages for this collection
22
X-Per-Page
Number of records returned per page
20
Cursor-based pagination
Some APIs support cursor-based pagination for more consistent results, particularly with real-time data models. Instead of
page
and
per
, cursor-based pagination uses
starting_after_uuid
and
limit
. For example:
https://api.gusto.com/v1/events?starting_after_uuid=10ac74e7-d6f0-46c0-9697-8ec77ab475ba&limit=5
Cursor-paginated APIs include the
X-Has-Next-Page
header, which will have a value either of true or false. For example,
X-Has-Next-Page: true
. If
X-Has-Next-Page
is
true
, more results will be available. Use the UUID of the last record from the current response as the next
starting_after_uuid
value.
Sorting
Many list endpoints support sorting via the
sort_by
query parameter. Each endpoint declares its own allowlist of sortable fields—check the parameter description on the endpoint's API reference page to see what's supported.
Sort format
The
sort_by
value follows the form
field
or
field:direction
, where direction is
asc
(ascending) or
desc
(descending).
When you omit the direction, the Gusto API sorts ascending by default.
For example, to list employees by name in descending order:
GET /v1/companies/{company_id}/employees?sort_by=name:desc
Sorting by multiple fields
To sort by more than one field, join the clauses with commas. Earlier fields take precedence, and each clause can specify its own direction.
For example, to sort employees by last name ascending, then first name ascending:
GET /v1/companies/{company_id}/employees?sort_by=last_name:asc,first_name:asc
Invalid sort fields
If you pass a field that isn't on an endpoint's allowlist—or a direction other than
asc
or
desc
—the API returns a
422 Unprocessable Content
error. Reference the
sort_by
parameter on an endpoint to confirm which fields are sortable.
Reliability
We use two main strategies to achieve operationally safe behavior: idempotency and optimistic version control. Both improve reliability—idempotency deals with retries, while version control deals with concurrency and versioning.
Use case
Strategy
HTTP method
Purpose
Creating resources
Idempotency key
POST
Retry safety: Ensures multiple
identical requests
have the same effect, preventing duplicate creations when retrying the same request. e.g. when timeouts happen during the create call.
Updating resources
Optimistic version control
PUT
Consistency safety: Prevents
concurrent conflicting updates
to the same resource. Ensures updates only apply if the data hasn't changed since the last time it was fetched.
Updating resources
Delta payloads
PUT
Data safety: Only the fields you send are updated. Omitted fields are left unchanged, so partial updates don't overwrite data you didn't intend to touch.
Idempotency
In API design,
idempotency
ensures that performing the same logical operation multiple times produces the same final result.
It protects your integration from network retries, client crashes, and concurrent updates that could otherwise cause duplicates or data inconsistencies.
The goal is to make each operation safe to retry.
In HTTP semantics, idempotency means that making the same request multiple times produces the same end state.
DELETE
is inherently idempotent: repeating the call will either delete the resource, or cause a "not found" error. You can't delete more than once.
PUT
and
POST
are not naturally idempotent, and need special mechanisms to ensure operational safety.
GET
is read-only and always surfaces the latest state of a resource; it never changes the server’s data and therefore doesn’t require idempotency handling.
Best practices
Always generate a new idempotency key for every unique create action.
Reuse the same idempotency key or version only when retrying the same request payload.
Log and store idempotency keys in your system to trace retry behavior.
Avoid sharing the same keys across different endpoints.
Optimistic version control
At Gusto we have object-based versions—essentially snapshots of a given resource—to process concurrent updates correctly, ensuring data integrity in a multi-user environment. It is a form of optimistic concurrency control, where the system 'assumes' that conflicts are rare and only checks for them at the time of an update.
For example
: Let’s say you give Frank (ID 7) a $200 bonus, but another app has already given Frank a $150 bonus. Your request to update the payroll sets the bonus to 200.00, overwriting the previous bonus. Frank is now set to receive a $200 bonus instead of the combined $350.
To prevent this, all updateable objects returned by the Gusto API include a
version
field. This
version
is calculated based on all updatable attributes of this object and its child objects.
To successfully update a record you’ve retrieved, you
must
include this same
version
number in your PUT request. If another process has already updated the record and changed the
version
number, your request will be rejected with a
409 Conflict
error.
This ensures that:
The object that you are trying to update did not change underneath.
Your updates will only overwrite the targeted data, instead of allowing overwriting other changes that may have occurred in the system since you last fetched the object.
You’re prevented from accidentally operating on a stale object version.
📘
The version only changes when an updatable attribute changes. It is not intended for general change detection and should only be used to prevent race conditions and the overwriting of data.
Update semantics (partial updates)
Gusto's
PUT
endpoints accept a
delta
, not the full resource. Send only the fields you want to change—any field you omit is left unchanged on the server.
This differs from the strict
RFC 7231
definition of
PUT
, where the request body replaces the entire resource and unsupplied fields are cleared. If you're integrating against Gusto for the first time and expecting standard
PUT
semantics, this is the most important behavioral difference to internalize—assuming full-replacement semantics can cause partners to unintentionally wipe data by re-sending a partial payload.
What to send
To update a single field, send only that field alongside the resource's current
version
. For example, to update an employee's email without touching their name, address, or any other attribute, call
PUT /v1/employees/{employee\_id}
with just:
JSON
{
  "version": "fe75bee7ff0d419d8f970ed941aef3a5",
  "email": "
[email protected]
"
}
The employee's
first_name
,
last_name
,
home_address
, and every other field remain exactly as they were.
Interaction with optimistic version control
The
version
field described in the previous section is still required on every
PUT
request, even a single-field delta. The delta applies on top of the resource at the version you supplied—if the resource has changed on the server since you fetched it, Gusto returns a
409 Conflict
and your update is rejected.
Rate limits
Rate limits are scoped per application-user pair. Each application can make
200 requests per minute per user
. If you exceed this rate, Gusto will return a
429 Too Many Requests
error.
Limits are enforced in a rolling 60-second window. The window starts when your first API call is made and resets 60 seconds later. A new window begins with your next API request.
API response headers
The following headers are now available to use when handling rate limiting programmatically:
Header
Description
Retry-After
The number of seconds until the rate limit window resets
X-RateLimit-Limit
The total number of requests allowed in the rate limit window
X-RateLimit-Remaining
The number of requests remaining in the rate limit window
X-RateLimit-Reset'
The datetime when the rate limit window will reset
Scopes
API scopes control what data your app can access. Each scope is named by resource and action, such as
employees:read
.
We currently support two types of actions:
read
: Read data from a resource
write
: Create, edit, or delete a resource
📘
Scopes in demo
By default, scopes are not enforced in the demo environment (
api.gusto-demo.com
), so you can build integrations before production scopes are finalized. Requests outside assigned scopes succeed in demo but return
403 Forbidden
in production. Use
GET /v1/token_info
to see which scopes a token holds, and confirm your integration only relies on those before going live.
Requesting and viewing scopes
You can view your application’s current scopes in the
Developer Portal
.
Before going to production, your application will be granted scopes based on your Embedded Payroll use case. Requests outside your assigned scopes will return a
403 Forbidden
error.
To request scope changes, contact your Technical Solutions representative. We recommend requesting
only
the scopes you need to build confidence and trust with your users.
String content
Free-text string values
in API responses—error messages, notification text, and label-style fields like tax agency names—are considered content, not contract. They are intended for display to end users and may change at any time, in any API version. Pass them through as-is rather than parsing or string-matching on their values.
Enum string values
are different. They come from a fixed, documented set and are part of the API contract: renaming or removing an existing enum value is a breaking change, while new enum values may be added in any version—so you should handle unknown values defensively.
See
What is a breaking change?
for the full versioning policy.
Updated
23 days ago
Did this page help you?
Yes
No
Copy Page
