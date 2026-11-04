# Payroll Processing Request

URL: https://docs.gusto.com/embedded-payroll/docs/payroll-processing-request
Retrieved: 2026-11-04
Version: n/a (living page). Rendered-text capture; images/layout not preserved.

---

The
processing_request
object is returned by our Get a Single Payroll API
endpoint
and Prepare API
endpoint
to provide better visibility into whether a payroll is currently being calculated or submitted.
While payroll is being calculated or submitted, it is important that no additional payroll API calls are made to modify the payroll (This includes the prepare, update, calculate, and submit APIs). The
processing_request
object is returned by our
GET companies/{company_id}/payrolls/{payroll_id}
endpoint
and the
PUT companies/{company_uuid}/payrolls/{payroll_uuid}/prepare
endpoint
. This object provides better visibility into the status of the calculation or submission process. It also returns relevant error information if there is a failure.
1. processing_request Attribute
The processing_request attribute is included in the response for the
GET companies/{company_id}/payrolls/{payroll_id}
endpoint
and the
PUT companies/{company_uuid}/payrolls/{payroll_uuid}/prepare
endpoint
:
JSON
"processing_request": {  
	"status": "calculate_success",  
	"errors": []
}
Status values can be:
calculating
calculate_success
submitting
submit_success
processing_failed
You will receive
"processing_request": null
if:
You have not attempted to calculate or submit the payroll
The
calculate
/
submit
process has not started yet. The
calculation
/
submission
is done asynchronously and generally starts within a couple seconds of a successful
calculate
/
submit
API request. This could take longer when many payrolls are being processed
The calculation has been cleared out by a request to the
PUT companies/{company_uuid}/payrolls/{payroll_uuid}/prepare
endpoint
.
2. Processing Failures
When processing fails we will return errors in the same format as our other API response errors.  Here are the most common error responses you will see when processing fails
Employee net pay less than zero
JSON
"processing_request": {  
        "status": "processing_failed",  
        "errors": [  
            {  
                "error_key": "employee_compensations",  
                "category": "nested_errors",  
                "metadata": {  
                    "employee_uuid": "4f8d4b3c-dab0-4ede-b52c-857c34404629"  
                },  
                "errors": [  
                    {  
                        "error_key": "net_pay",  
                        "category": "invalid_attribute_value",  
                        "message": "Net pay must be greater than or equal to 0. This is likely occurring due to deductions, tax withholding for benefits, or additional tax withholding exceeding employee pay. Can modify these, add pay, or exclude employee from this payroll."  
                    }  
                ]  
            }  
	]  
}
Debit date no longer valid
JSON
"processing_request": {  
        "status": "processing_failed",  
        "errors": [  
            {  
                "error_key": "base",  
                "category": "invalid_attribute_value",  
                "message": "Payroll was not processed before deadline. Please recalculate payroll to get updated dates."  
            }  
	]  
}
Fallback error - If we are unable to map the error correctly we will return this error.
JSON
"processing_request": {  
        "status": "processing_failed",  
        "errors": [  
            {  
                "error_key": "base",  
                "category": "internal_error",  
                "message": "Something went wrong. Please try reprocessing and contact support if the issue persists."  
            }  
	]  
}
Updated
11 months ago
Did this page help you?
Yes
No
Copy Page
