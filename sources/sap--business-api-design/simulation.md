# SAP Sales Order Simulation — rendered documentation excerpts

Canonical URL: https://help.sap.com/docs/SAP_S4HANA_CLOUD/03c04db2a7434731b7fe21dca77440da/b64937ce2692427594ee794ad033b8b3.html
Retrieved: 2026-11-04
Visible version: APIs for Sales, 2608 Latest, English.
Capture: selected article prose, service metadata and constraints read through browser rendering. Entity table and navigation omitted. Excerpts separated with capture labels.

---

Sales Order - Simulate (A2X, OData V2)

The Sales Order - Simulate (A2X, OData V2) API allows you to simulate the creation of sales orders.

Technical name: API_SALES_ORDER_SIMULATION_SRV

With this synchronous inbound OData service, you can simulate the creation of a sales order. This gives you information about pricing, material availability, and the customer's credit limit. The response is provided synchronously. The simulated sales order is not saved.

Add the following associations to your request to retrieve specific information:

to_Pricing

To trigger the calculation of prices, add this association to the request. If you send the requestion without the association, you won't get any pricing pricing information.

to_ScheduleLine

To trigger the available-to-promise (ATP) check, add this association to the request on item level. Note that it is sufficient to add the association to a single item. The check is triggered for the other items automatically.

to_Credit

To trigger the credit limit check, add this association to the request on header level. You must add the empty association to enable the credit limit check.

[Capture excerpt: service metadata]

The service metadata file can be retrieved through /sap/opu/odata/SAP/API_SALES_ORDER_SIMULATION_SRV/$metadata

[Capture excerpt: limitations and required setup]

Note that for technical reasons, only 20 messages that don't lead to an abortion (that is, success messages, info messages, and warnings) can be transmitted. If there are more messages, the last of those 20 messages will let you know that additional messages exist.

Required Communication Scenario

To use this service, you have to configure the following communication scenario: SAP_COM_0109.

Constraints

With this service, it is not possible to:

Process sales orders with sales order processing type P (sales orders for project-based services (PBS))

Process sales orders with SD document category I (sales order without charge)

Create or process multiple sales orders in a single change set of a $batch OData request

For more information about $batch requests, see $batch Processing.

To execute the Check of Sales Documents Before Saving BAdI.

Note

The simulation result excludes changes to the header custom fields of the BAdI Modification of Sales Document in Finalize Phase before Save.
