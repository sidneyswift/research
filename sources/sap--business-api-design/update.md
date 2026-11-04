# SAP Update Requests — rendered documentation excerpt

Canonical URL: https://help.sap.com/docs/SAP_S4HANA_CLOUD/03c04db2a7434731b7fe21dca77440da/97d39eea3dec42589b58cf48d2b04482.html
Retrieved: 2026-11-04
Visible version: APIs for Sales, 2608 Latest, English.
Capture: main article text excerpt read through browser rendering. Static HTML was a JavaScript shell. Navigation, collapsed examples, and later variant-configuration examples omitted. The following text is source evidence, not wiki analysis.

---

Update Requests

Check sample requests to learn how to use Update requests with the Sales Order (A2X, OData V4) API.

To update any entity of an existing sales order, you can use the PATCH HTTP method. You must always provide all keys in the URL.

For every PATCH operation (with the exception of PATCH operations using the SalesOrderPricingElement or the SalesOrderItemPricingElement entity), you must set the If-Match header with the ETag of the sales order. The value for the sales order ETag can be retrieved from any request, either from the response Header parameter etag or from the response payload property @odata.etag.

Note

If you provide properties with initial values, these are interpreted as a request to clear the respective properties.

Response

For Update requests, you can choose from the following synchronous options by providing the HTTP header parameter prefer:

return=representation: This option gives back a full response containing all entities and their properties.

return=minimal: This option gives back a minimal response containing only the key of the created entity.

Recommendation

By default, the service response is a full response. For Update requests for single entities, the respective entities are returned. For deep insert requests, every entity that was provided is returned. To improve performance, we recommend that you choose the minimal response if you don't need comprehensive information.
