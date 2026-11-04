# Composite dependent requests

Canonical URL: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-composite-composite-post.html
Retrieved: 2026-11-04
Capture: vendor Markdown or rendered HTML text; scripts/navigation removed where identifiable.

---

Send Multiple Requests Using Composite
Executes a series of REST API requests in a single call. You can use the output of one request as the input to a subsequent request. The response bodies and HTTP statuses of the requests are returned in a single response body. The entire series of requests counts as a single call toward your API limits.
The sObject Blob Get and sObject Rich Text Image Get APIs return binary data. These APIs aren’t supported in a Composite API request.
The requests in a composite call are called subrequests. All subrequests are executed in the context of the same user. In a subrequest’s body, you specify a reference ID that maps to the subrequest’s response. You can then refer to the ID in the
url
or
body
fields of later subrequests by using a JavaScript-like reference notation.
For example, the following composite request body includes two subrequests. The first creates an account and designates the output as
refAccount
. The second creates a contact parented under the new account by referencing
refAccount
in the subrequest body.
You can specify whether an error in a subrequest causes the whole composite request to roll back or just the subrequests that depend on it. You can also specify headers for each subrequest.
Composite is supported for the following resources.
All sObject resources (
/services/data/vXX.X/sobjects/
), including
sObject Rows by External ID
and excluding
sObject Blob Get
The Query resource (
/services/data/vXX.X/query/?q=soql
)
The QueryAll resource (
/services/data/vXX.X/queryAll/?q=soql
)
The sObject Collections resource (
/services/data/vXX.X/composite/sobjects
). Available in API version 43.0 and later.
You can have up to 25 subrequests in a single call. Up to 5 of these subrequests can be sObject Collections or query operations, including Query and QueryAll requests.
URI:
/services/data/vXX.X/composite
Formats:
JSON
HTTP method:
POST
Authentication:
Authorization: Bearer token
Parameters:
None required
Request body:
Composite Request Body
Response body:
Composite Response Body
For examples of using the Composite resource, see
Execute Dependent Requests in a Single API Call
and
Update an Account, Create a Contact, and Link Them with a Junction Object
.
Composite Subrequest Result
The composite subrequest result describes the result for a subrequest.
