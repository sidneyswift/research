# Endpoint | Developer Hub

URL: https://developer.ftrack.com/api/endpoint/index.html
Retrieved: 2026-11-04
Version: n/a (living page). Rendered-text capture; images/layout not preserved.

---

On this page
The API is available over HTTP with JSON used as the data transmission format.
For efficiency, the API operates in batch mode and is accessible via a single endpoint
https://FTRACK-WORKSPACE-URL/api
.
A client should POST to that endpoint a JSON payload that describes
a series of operations to perform
.
Each request should also include the following headers:
- Content-Type: application/json
- Accept: application/json
As each request is considered a list of operations, the response is equally a JSON encoded list of results that correspond to the indices of the operations.
Authentication
​
To use the API you will need a valid username and API key. The username should match the username of an ftrack account holder that you wish to perform actions on behalf of, via the API. See the main article
Authentication
.
API Authentication is then done using custom headers in the initial request:
- ftrack-user: USERNAME
- ftrack-api-key: API_KEY_TO_USE
The details are then stored for the rest of the session, and only a standard session cookie is required.
If the details are invalid, the request will return an HTTP error status code, with details on why the authentication failed in the response body.
Payloads
​
As mentioned above, request and response payloads must be encoded as JSON.
In addition, there are some special rules for handling certain data types.
Date and time
​
Should be a naive value, in the servers timezone, formatted as an ISO 8601 string.
Entities
​
An entity should only be fully encoded once. All duplicate entity references should be represented by an entity reference of the form:
{
"__entity_type__"
:
"EntityType"
,
""
:
""
}
In addition, for most operations only top level entities need to be fully encoded. For example, a Create operation would not recursively create all nested entities - instead each entity in a tree to be created should be handled by a separate create operation.
When decoding responses, be aware that it is possible for a fully encoded entity to be at any nested depth with all other references to that entity represented by an entity reference. As such you will need to recursively process a response and expand the entity references so that they all refer to the same full entity object.
tip
See also: Python API Session.merge implementation.
Errors
​
For authentication or exceptional errors a standard HTTP error code will be returned with details in the body and also in an
FTRACK_ERROR
header.
In the case of an operational error occurring the response payload will take the form of a dictionary that can be inspected to retrieve error details:
{
"exception"
:
"ExceptionName"
,
"content"
:
"Exception details"
}
When multiple operations are sent in one request, they are treated as related and will be processed within the same transaction server side. As a result, if any operation fails, then all operations in the batch will be rolled back.
Example
​
The following shows an example ‘empty’ request and corresponding response.
Example request:
POST /api HTTP/1.1
Host: example.ftrackapp.com
Content-Type: application/json
Accept: application/json
ftrack-user: john
ftrack-api-key: cdd5dcbc-d0bd-435c-8f9d-6ed6902cdd9a
[]
Example response:
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 2
Content-Type: text/html; charset=utf-8
Date: Tue, 17 Nov 2015 14:06:33 GMT
Pragma: no-cache
Server: nginx/1.6.1
[]
You can perform such a call using an HTTP client like cURL:
Replace the header credentials with your own.
curl
https://ftrack-test.ftrackapp.com/api
\
-X
POST
\
-H
"Content-Type: application/json"
\
-H
"ftrack-user: john"
\
-H
"ftrack-api-key: cdd5dcbc-d0bd-435c-8f9d-6ed6902cdd9a"
\
--data
'[]'
Output:
[]
