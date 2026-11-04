# SAP Asynchronous Processing — rendered documentation excerpt

Canonical URL: https://help.sap.com/docs/SAP_S4HANA_CLOUD/03c04db2a7434731b7fe21dca77440da/02b40f57315d495ebcf278e673a0fd90.html
Retrieved: 2026-11-04
Visible version: APIs for Sales, 2608 Latest, English.
Capture: main article prose read through browser rendering. Navigation and four collapsed example panels omitted; no exact sample response status is inferred from those panels.

---

Asynchronous Processing

Learn whether synchronous or asynchronous processing works best for you when setting up the Sales Order (A2X, OData V4) API.

When you set up an integration scenario, you should make a conscious decision about the processing of your API calls: Should they be executed synchronously or asynchronously?

Synchronous calls are the right choice if you need an immediate response to your API request. For more information about the different response options, see Create Requests and Update Requests.

Asynchronous calls are the right choice if you don't need a response right away.

Recommendation

When dealing with high data volumes and when no synchronous API response is required, we generally recommend asynchronous processing to improve the performance of your integration scenario.

To send requests asynchronously, you can provide the HTTP header parameter prefer with the value respond-async. In this case, you don't receive a response payload. Instead, the response header contains the parameter location with a URL that you can use to retrieve the API response asynchronously.
