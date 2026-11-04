# Create a query job

Canonical URL: https://developer.salesforce.com/docs/platform/api-asynch/guide/query-create-job.html
Retrieved: 2026-11-04
Capture: vendor Markdown or rendered HTML text; scripts/navigation removed where identifiable.

---

Create a Query Job
Creates a query job.
URI:
/services/data/vXX.X/jobs/query
Available since release:
This resource is available in API version 47.0 and later.
Format:
application/json
HTTP method:
POST
Authentication:
Authorization:Bearer token
Headers:
Optionally, use the
Sforce-Call-Options
header to specify a
default namespace
.
Request body
The request body specifies the query to be performed.
Bulk API 2.0 doesn’t support SOQL queries that include any of these items:
GROUP BY, OFFSET, or TYPEOF clauses.
Aggregate Functions such as
COUNT()
.
Date functions in GROUP BY clauses. (Date functions in WHERE clauses are supported.)
Compound data, such as compound address fields, compound geolocation fields, and
FIELDS()
. (Instead, query the individual components of compound fields.)
Parent-to-child
relationship queries
. (Child-to-parent relationship queries are supported.)
You can also specify some optional parameters. For example:
Request parameters:
Parameter
Description
Required or Optional
operation
The type of query. Possible values are:
query
—Returns data that hasn’t been deleted or archived. For more information, see
query()
in
SOAP API Developer Guide
.
queryAll
—Returns records that have been deleted because of a merge or delete, and returns information about archived Task and Event records. For more information, see
queryAll()
in
SOAP API Developer Guide
.
Required
query
The query to be performed.
Required
contentType
The format to be used for the results. Currently the only supported value is
CSV
(comma-separated variables). Defaults to
CSV
. The actual separator can be a character other than a comma. The
columnDelimiter
parameter specifies what character to use.
Optional
columnDelimiter
The column delimiter used for CSV job data. The default value is
COMMA
. Possible values are:
BACKQUOTE
—back quote character (`)
CARET
—caret character (^)
COMMA
—comma character (,)
PIPE
—pipe character (|)
SEMICOLON
—semicolon character (;)
TAB
—tab character
Optional
lineEnding
The line ending used for CSV job data, marking the end of a data row. The default is
LF
. Possible values are:
LF
—linefeed character
CRLF
—carriage return character followed by a linefeed character
Optional
Response Body
Response Parameters:
Parameter
Description
id
The unique ID for this job.
operation
The type of query.
object
The object type being queried.
createdById
The ID of the user who created the job.
createdDate
The UTC date and time when the job was created.
systemModstamp
The UTC date and time when the API last updated the job information.
state
The current state of processing for the job. Possible values are:
UploadComplete
—The job is ready to be processed and Salesforce has put the job in the queue.
InProgress
—Salesforce is processing the job.
Aborted
—The job has been aborted. See
Abort a Query Job
.
JobComplete
—Salesforce has finished processing the job.
Failed
—The job failed.
concurrencyMode
Reserved for future use. How the request is processed. Currently only parallel mode is supported. (When other modes are added, the API chooses the mode automatically. The mode isn’t user configurable.)
contentType
The format to be used for the results. Currently the only supported value is
CSV
.
JunctionIdList
fields and embedded lists can’t be returned.
apiVersion
The API version that the job was created in.
lineEnding
The line ending used for CSV job data, marking the end of a data row.
columnDelimiter
The column delimiter used for CSV job data.
This example creates a job that queries Accounts.
The response is:
