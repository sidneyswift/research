# Query results and locators

Canonical URL: https://developer.salesforce.com/docs/platform/api-asynch/guide/query-get-job-results.html
Retrieved: 2026-11-04
Capture: vendor Markdown or rendered HTML text; scripts/navigation removed where identifiable.

---

Get Results for a Query Job
Gets the results for a query job. The job must have the state
JobComplete
.
If encoding is enabled for Bulk API 2.0 Query job responses, there is a significant improvement in performance of query result downloads. This not the total query time, but a reduction in the time to download the results.
URI:
/services/data/vXX.X/jobs/query/queryJobId/results
or
Use the same API version to get query results that you used to create the query. Otherwise, the call returns a 409 error.
Available since release:
This resource is available in API version 47.0 and later.
Formats:
CSV
HTTP methods:
GET
Authentication:
Authorization: Bearer token
Request parameters:
Parameter
Description
Required or Optional
queryJobId
The ID of the query job.
Required
locator
A string that identifies a specific set of query results. Providing a value for this parameter returns only that set of results.
Omitting this parameter returns the first set of results.
You can find the locator string for the next set of results in the response of each request. See
Example
and
Rules and Guidelines
.
As long as the associated job exists, the locator string for a set of results does not change. You can use the locator to retrieve a set of results multiple times.
Optional
maxRecords
The maximum number of records to retrieve per set of results for the query. The request is still subject to the size limits.
If you are working with a very large number of query results, you may experience a timeout before receiving all the data from Salesforce. To prevent a timeout, specify the maximum number of records your client is expecting to receive in the
maxRecords
parameter. This splits the results into smaller sets with this value as the maximum size.
If you don’t provide a value for this parameter, the server uses a default value based on the service.
Optional
Response Body
If the request is successful, the status code is 200 (OK) and the request body contains the results of the job’s query. For example:
In API version 50.0 and later, the order of the columns returned by the query is the same as the order you requested them. In version 49.0 and earlier, the order of the columns is returned alphabetically.
Response Headers
Header
Description
Sforce-NumberOfRecords
The number of records in this set.
Sforce-Locator
The locator for the next set of results (if there are any). Use this value in other
GET
request to retrieve the next set of query results.
This value is a pseudo random string (for example,
MTAwMDA
). The length of this string varies depending on how many sets of results there are.
If there are no more sets of query results, this value is the string ‘null’.
See
Example
and
Rules and Guidelines
.
This example retrieves the results for the job with ID
750R0000000zxr8IAA
. It also shows how to use the
locator
and
maxRecords
query parameters. (In this example, we use them both, but they are independent. You don’t have to use them together.) For an example on how to download data in parallel, see
Get Parallel Results for a Query Job
.
We start by sending an initial request to retrieve the first set of query results. We don’t use the
locator
parameter because we want to get the first set of results.
The
Accept
header must match what was specified when the job was created. Currently, only
text/csv
is supported.
The response body is:
The response includes
MTAwMDA
as a value for the
Sforce-Locator
header. This value is not ‘null’, which means that there are more query results that we can retrieve.
To retrieve the next set of query results, we send another request, using the
locator
parameter and the locator string,
MTAwMDA
.
The response body is:
Notice that the locator value has changed. This means that there is another set of query results that we can retrieve. We use the new locator string,
MjAwMDAw
, in another request.
We repeat this process until the value of the
Sforce-Locator
header is ‘null’, which indicates that there are no more results to retrieve.
To retrieve your full set of query results, follow these rules and guidelines.
Use
/services/data/vXX.X/jobs/query/queryJobId/results
to get the first set of results for the job.
If there are no more results, the
Sforce-Locator
header’s value is the string ‘null’. Otherwise, set the
locator
query parameter to that value to get the next set of results.
For
locator
, use only the value from the
Sforce-Locator
header. Don’t try to guess what it is. How this parameter is evaluated is subject to change.
Repeat this process until the
Sforce-Locator
header’s value is the string ‘null’. That set is the last set of results.
See Also
Errors
