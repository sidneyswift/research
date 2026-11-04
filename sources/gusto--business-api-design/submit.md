# Submit payroll

URL: https://docs.gusto.com/embedded-payroll/reference/put-v1-companies-company_id-payrolls-payroll_id-submit
Retrieved: 2026-11-04
Version: n/a (living page). Rendered-text capture; images/layout not preserved.

---

company_id
string
required
The UUID of the company
payroll_id
string
required
The UUID of the payroll
submission_blockers
array of objects
An array of submission_blockers, each with a selected unblock option.
submission_blockers
ADD
object
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
