# submit-full

URL: https://docs.gusto.com/embedded-payroll/reference/put-v1-companies-company_id-payrolls-payroll_id-submit
Retrieved: 2026-11-04
Capture: full body rendered text; includes navigation. Layout/images omitted.

---

For AI agents: the docs index is at https://docs.gusto.com/embedded-payroll/llms.txt. The index for every project on this site is at https://docs.gusto.com/llms.txt. Append .md to any documentation page URL to get its markdown version.
Jump to Content
Guides
API Reference
Changelog
API Status
API Policy
Gusto Security
v2024-04-01
v2025-06-15
v2025-11-15
v2026-02-01
v2026-06-15
API Reference
Submit payroll
Copy Page
Submit payroll
put
https://api.gusto-demo.com
/v1/companies/
{company_id}
/payrolls/
{payroll_id}
/submit
Submits an unprocessed payroll to be calculated and run. This submission is asynchronous and a successful request responds with a 202 HTTP status. Upon success, transitions the payroll to the
processed
state.
You should poll to ensure that payroll is processed successfully, as async errors only occur after async processing is complete.
If the company is blocked from running payroll due to issues like incomplete setup, missing information or other compliance issues, the response will be 422 Unprocessable Entity with a categorization of the blockers as described in the error responses.
scope:
payrolls:run
Path Params
company_id
string
required
The UUID of the company
payroll_id
string
required
The UUID of the payroll
Body Params
submission_blockers
array of objects
An array of submission_blockers, each with a selected unblock option.
submission_blockers
ADD
object
Headers
X-Gusto-API-Version
string
enum
Defaults to 2026-06-15
Determines the date-based API version associated with your API call. If none is provided, your application's
minimum API version
is used.
2026-06-15
Allowed:
2026-06-15
Responses
202
Accepted
404
Not Found
422
Unprocessable Entity
This may happen when the body of your request contains errors such as
invalid_attribute_value
, or the request fails due to an
invalid_operation
. See the
Errors Categories
guide for more details.
Updated
5 months ago
Did this page help you?
Yes
No
Language
Shell
Node
Ruby
PHP
Python
Credentials
Bearer
Bearer
Loading
Loading…
Response
Click
Try It!
to start a request and see the response here!
Or choose an example:
application/json
404
-
not found
422
-
unmodifiable payroll type
422
-
payroll blocker missing bank info
422
-
payroll blocker missing employee setup
422
-
payroll blocker missing federal tax setup
422
-
payroll blocker missing bank verification
422
-
payroll blocker suspended
422
-
submission blocker missing selection
422
-
submission blocker invalid option
Updated
5 months ago
Did this page help you?
Yes
No
