# Sales invoice resource

Canonical URL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/resources/dynamics_salesinvoice
Retrieved: 2026-11-04
Capture: vendor Markdown or rendered HTML text; scripts/navigation removed where identifiable.

---

---
layout: Conceptual
title: salesInvoice resource type - Business Central | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/resources/dynamics_salesinvoice
feedback_system: Standard
feedback_product_url: https://experience.dynamics.com/ideas/categories/?forum=e288ef32-82ed-e611-8101-5065f38b21f1&forumName=Dynamics%20365%20Business%20Central
ms.author: solsen
ms.reviewer: solsen
uhfHeaderId: MSDocsHeader-Dynamics365-BusinessCentral
search.app:
- businesscentral
- businesscentral-docs
search.audienceType: admin, developer
breadcrumb_path: /dynamics365/business-central/dev-itpro/breadcrumb/toc.json
ms.service: dynamics-365-business-central
recommendations: true
description: A sales invoice object in Dynamics 365 Business Central.
author: SusanneWindfeldPedersen
ms.topic: reference
ms.devlang: al
ms.date: 2026-08-21T00:00:00.0000000Z
locale: en-us
document_id: e94f317d-c661-22fa-227b-61cf80b749f8
document_version_independent_id: 2301ee7b-b246-2ce4-3771-b50d529d0847
updated_at: 2026-08-24T13:04:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/dynamics365smb-devitpro/blob/live/dev-itpro/api-reference/v2.0/resources/dynamics_salesinvoice.md
gitcommit: https://github.com/MicrosoftDocs/dynamics365smb-devitpro/blob/b17c2215165d2e2a935aa3bcd2e7e2709a8b3d91/dev-itpro/api-reference/v2.0/resources/dynamics_salesinvoice.md
git_commit_id: b17c2215165d2e2a935aa3bcd2e7e2709a8b3d91
site_name: Docs
depot_name: NAV.dev-itpro
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/NAV.dev-itpro/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
word_count: 1011
asset_id: api-reference/v2.0/resources/dynamics_salesinvoice
moniker_range_name: 
monikers: []
item_type: Content
source_path: dev-itpro/api-reference/v2.0/resources/dynamics_salesinvoice.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0160afd6-d1cc-4233-b94c-d06c3230d644
- https://authoring-docs-microsoft.poolparty.biz/devrel/86a4b315-a9f1-4577-b985-6fb0e0e67420
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/92494c58-7e81-4229-ae85-bb895913ffe3
- https://authoring-docs-microsoft.poolparty.biz/devrel/96ac410d-d052-4707-8007-df31dd0fe041
platformId: 3cad58fb-9f04-5440-2dee-6440f178bb93
---

# salesInvoice resource type - Business Central | Microsoft Learn

Represents a sales invoice in Business Central.

Note

For information about enabling APIs for Business Central see [Enabling the APIs for Dynamics 365 Business Central](../enabling-apis-for-dynamics-nav).

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| [GET salesInvoice](../api/dynamics_salesinvoice_get) | salesInvoice | Gets a sales invoice object. |
| [DELETE salesInvoice](../api/dynamics_salesinvoice_delete) | none | Deletes a sales invoice object. |
| [POST salesInvoice](../api/dynamics_salesinvoice_create) | salesInvoice | Creates a sales invoice object. |
| [PATCH salesInvoice](../api/dynamics_salesinvoice_update) | salesInvoice | Updates a sales invoice object. |

## Bound actions

The salesInvoice resource type offers a bound action called `cancel`, which cancels the corresponding salesInvoice batch. This is illustrated in the following example: `CANCEL https://<server address>:<server API port>/<server instance name>/api/v2.0/companies({id})/salesInvoices({id})/Microsoft.NAV.cancel`

The response has no content; the response code is 204.

The salesInvoice resource type offers a bound action called `cancelAndSend`, which cancels and sends the corresponding salesInvoice batch. This is illustrated in the following example: `CANCELANDSEND https://<server address>:<server API port>/<server instance name>/api/v2.0/companies({id})/salesInvoices({id})/Microsoft.NAV.cancelAndSend`

The response has no content; the response code is 204.

The salesInvoice resource type offers a bound action called `makeCorrectiveCreditMemo`, which makes corrective credit memos to the corresponding salesInvoice batch. This is illustrated in the following example: `MAKECORRECTIVECREDITMEMO https://<server address>:<server API port>/<server instance name>/api/v2.0/companies({id})/salesInvoices({id})/Microsoft.NAV.makeCorrectiveCreditMemo`

The response has no content; the response code is 204.

The salesInvoice resource type offers a bound action called `post`, which posts the corresponding salesInvoice batch. This is illustrated in the following example: `POST https://<server address>:<server API port>/<server instance name>/api/v2.0/companies({id})/salesInvoices({id})/Microsoft.NAV.post`

The response has no content; the response code is 204.

The salesInvoice resource type offers a bound action called `postAndSend`, which posts and sends the corresponding salesInvoice batch. This is illustrated in the following example: `POSTANDSEND https://<server address>:<server API port>/<server instance name>/api/v2.0/companies({id})/salesInvoices({id})/Microsoft.NAV.postAndSend`

The response has no content; the response code is 204.

The salesInvoice resource type offers a bound action called `send` which sends the corresponding salesInvoice batch. This is illustrated in the following example: `SEND https://<server address>:<server API port>/<server instance name>/api/v2.0/companies({id})/salesInvoices({id})/Microsoft.NAV.send`

The response has no content; the response code is 204.

## Navigation

| Navigation | Return Type | Description |
| --- | --- | --- |
| [customer](dynamics_customer) | customer | Gets the customer of the salesInvoice. |
| [currency](dynamics_currency) | currency | Gets the currency of the salesInvoice. |
| [dimensionValue](dynamics_dimensionvalue) | dimensionValue | Gets the dimensionvalue of the salesInvoice. |
| [paymentTerm](dynamics_paymentterm) | paymentTerm | Gets the paymentterm of the salesInvoice. |
| [shipmentMethod](dynamics_shipmentmethod) | shipmentMethod | Gets the shipmentmethod of the salesInvoice. |
| [dimensionSetLines](dynamics_dimensionsetline) | dimensionSetLines | Gets the dimensionsetlines of the salesInvoice. |
| [salesInvoiceLines](dynamics_salesinvoiceline) | salesInvoiceLines | Gets the salesinvoicelines of the salesInvoice. |
| [pdfDocument](dynamics_pdfdocument) | pdfDocument | Gets the pdfdocument of the salesInvoice. |
| [attachments](dynamics_attachment) | attachments | Gets the attachments of the salesInvoice. |
| [documentAttachments](dynamics_documentattachment) | documentAttachments | Gets the documentattachments of the salesInvoice. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| id | GUID | The unique ID of the sales invoice. Non-editable. |
| number | string | Specifies the number of the sales invoice. |
| externalDocumentNumber | string | Specifies an external document number for the sales invoice. |
| invoiceDate | date | The invoice date . |
| postingDate | date | The date that the sales invoice is posted. |
| dueDate | date | T he date the sales invoice is due. |
| promisedPayDate | date |  |
| customerPurchaseOrderReference | string | The customer purchase order reference for the invoice. |
| customerId | GUID | The unique ID of customer. |
| customerNumber | string | The customer's number. |
| customerName | string | The customer's name. |
| billToName | string | Bill to name. |
| billToCustomerId | GUID | Bill to customer id. |
| billToCustomerNumber | string | Bill to customer number. |
| shipToName | string | Ship to name. |
| shipToContact | string | Ship to contact. |
| sellToAddressLine1 | string | Sell to address line 1. |
| sellToAddressLine2 | string | Sell to address line 2. |
| sellToCity | string | Sell to city. |
| sellToCountry | string | Sell to country. |
| sellToState | string | Sell to state. |
| sellToPostCode | string | Sell to post code. |
| billToAddressLine1 | string | Bill to address line 1. |
| billToAddressLine2 | string | Bill to address line 2. |
| billToCity | string | Bill to city. |
| billToCountry | string | Bill to country. |
| billToState | string | Bill to state. |
| billToPostCode | string | Bill to post code. |
| shipToAddressLine1 | string | Ship to address line 1. |
| shipToAddressLine2 | string | Ship to address line 2. |
| shipToCity | string | Ship to city. |
| shipToCountry | string | Ship to country. |
| shipToState | string | Ship to state. |
| shipToPostCode | string | Ship to post code. |
| currencyId | GUID | Specifies which currency the sales invoice uses. |
| shortcutDimension1Code | string |  |
| shortcutDimension2Code | string |  |
| currencyCode | string | The default currency code for the sales invoice. |
| orderId | GUID | The id of the order to which the sales invoice is associated to. Read-Only. |
| orderNumber | string | The number of the order to which the sales invoice is associated to. Read-Only. |
| paymentTermsId | GUID | Specifies which payment term the sales invoice uses. |
| shipmentMethodId | GUID | Specifies which shipment method the sales invoice uses. |
| salesperson | string | The salesperson code for the sales invoice. |
| disputeStatusId | GUID |  |
| disputeStatus | string |  |
| pricesIncludeTax | boolean | Specifies whether the prices include Tax or not. Read-Only. |
| remainingAmount | decimal | The amount including VAT. |
| discountAmount | decimal | The sales invoice discount amount. |
| discountAppliedBeforeTax | boolean | Specifies whether the discount is applied before tax. |
| totalAmountExcludingTax | decimal | The total amount excluding tax. Read-Only. |
| totalTaxAmount | decimal | The total tax amount for the sales invoice. Read-Only. |
| totalAmountIncludingTax | decimal | The total amount including tax. Read-Only. |
| status | NAV.invoiceEntityAggregateStatus | The status of the sales invoice. It can be " ", "Draft", "In Review", "Open", "Paid", "Canceled" or "Corrective". |
| lastModifiedDateTime | datetime | The last datetime the sales invoice was modified. Read-Only. |
| phoneNumber | string | Specifies the sales invoice's telephone number. |
| email | string | Specifies the sales invoice's email address. |

## JSON representation

Here's a JSON representation of the salesInvoice resource.

```json
{
    "id": "GUID",
    "number": "string",
    "externalDocumentNumber": "string",
    "invoiceDate": "date",
    "postingDate": "date",
    "dueDate": "date",
    "promisedPayDate": "date",
    "customerPurchaseOrderReference": "string",
    "customerId": "GUID",
    "customerNumber": "string",
    "customerName": "string",
    "billToName": "string",
    "billToCustomerId": "GUID",
    "billToCustomerNumber": "string",
    "shipToName": "string",
    "shipToContact": "string",
    "sellToAddressLine1": "string",
    "sellToAddressLine2": "string",
    "sellToCity": "string",
    "sellToCountry": "string",
    "sellToState": "string",
    "sellToPostCode": "string",
    "billToAddressLine1": "string",
    "billToAddressLine2": "string",
    "billToCity": "string",
    "billToCountry": "string",
    "billToState": "string",
    "billToPostCode": "string",
    "shipToAddressLine1": "string",
    "shipToAddressLine2": "string",
    "shipToCity": "string",
    "shipToCountry": "string",
    "shipToState": "string",
    "shipToPostCode": "string",
    "currencyId": "GUID",
    "shortcutDimension1Code": "string",
    "shortcutDimension2Code": "string",
    "currencyCode": "string",
    "orderId": "GUID",
    "orderNumber": "string",
    "paymentTermsId": "GUID",
    "shipmentMethodId": "GUID",
    "salesperson": "string",
    "disputeStatusId": "GUID",
    "disputeStatus": "string",
    "pricesIncludeTax": "boolean",
    "remainingAmount": "decimal",
    "discountAmount": "decimal",
    "discountAppliedBeforeTax": "boolean",
    "totalAmountExcludingTax": "decimal",
    "totalTaxAmount": "decimal",
    "totalAmountIncludingTax": "decimal",
    "status": "NAV.invoiceEntityAggregateStatus",
    "lastModifiedDateTime": "datetime",
    "phoneNumber": "string",
    "email": "string"
}
```

Note

The `id` property value in this API resource might be different than the `systemId` of the corresponding record because the `systemId` of the unposted invoices are carried to posted invoices in the API, but not to the record. Use the `https://{businesscentralPrefix}/microsoft/automate/v1.0/companies({id})/postedSalesInvoices({systemId})` route and extract the `apiId` property to map the `systemId` of a posted sales invoice record to the `salesInvoice` API resource.

## Related information

[GET salesInvoice](../api/dynamics_salesinvoice_get)[DELETE salesInvoice](../api/dynamics_salesinvoice_delete)[POST salesInvoice](../api/dynamics_salesinvoice_create)[PATCH salesInvoice](../api/dynamics_salesinvoice_update)
