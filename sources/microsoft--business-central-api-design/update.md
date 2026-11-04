# Invoice update and If-Match

Canonical URL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoice_update
Retrieved: 2026-11-04
Capture: vendor Markdown or rendered HTML text; scripts/navigation removed where identifiable.

---

---
layout: Conceptual
title: Update salesInvoices - Business Central | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoice_update
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
description: Updates a sales invoice object in Dynamics 365 Business Central.
author: SusanneWindfeldPedersen
ms.topic: reference
ms.devlang: al
ms.date: 2026-08-21T00:00:00.0000000Z
locale: en-us
document_id: 8aa58a9b-a29d-0517-8e1b-4ad052720a49
document_version_independent_id: 169e1ff4-3fe0-7c37-85e9-f50a0ec6a56a
updated_at: 2026-08-24T13:04:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/dynamics365smb-devitpro/blob/live/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoice_update.md
gitcommit: https://github.com/MicrosoftDocs/dynamics365smb-devitpro/blob/b17c2215165d2e2a935aa3bcd2e7e2709a8b3d91/dev-itpro/api-reference/v2.0/api/dynamics_salesinvoice_update.md
git_commit_id: b17c2215165d2e2a935aa3bcd2e7e2709a8b3d91
site_name: Docs
depot_name: NAV.dev-itpro
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/NAV.dev-itpro/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
word_count: 313
asset_id: api-reference/v2.0/api/dynamics_salesinvoice_update
moniker_range_name: 
monikers: []
item_type: Content
source_path: dev-itpro/api-reference/v2.0/api/dynamics_salesinvoice_update.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0160afd6-d1cc-4233-b94c-d06c3230d644
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/92494c58-7e81-4229-ae85-bb895913ffe3
platformId: 54d733d1-bd4a-a201-41dd-d7863b2f2ce7
---

# Update salesInvoices - Business Central | Microsoft Learn

Update the properties of a sales invoice object for Business Central.

## HTTP request

Replace the URL prefix for Business Central depending on environment following the [guideline](../endpoints-apis-for-dynamics).

```
PATCH businesscentralPrefix/companies({id})/salesInvoices({id})
```

## Request headers

| Header | Value |
| --- | --- |
| Authorization | Bearer {token}. Required. |
| Content-Type | application/json |
| If-Match | Required. When this request header is included and the eTag provided doesn't match the current tag on the **salesInvoices**, the **salesInvoices** won't be updated. |

## Request body

In the request body, supply the values for relevant fields that should be updated. Existing properties that aren't included in the request body will maintain their previous values or be recalculated based on changes to other property values. For best performance you shouldn't include existing values that haven't changed.

## Response

If successful, this method returns a `200 OK` response code and an updated **salesInvoices** object in the response body.

## Example

**Request**

Here's an example of the request.

```json
PATCH https://{businesscentralPrefix}/api/v2.0/companies({id})/salesInvoices({id})
Content-type: application/json

{
  "paymentTermsId": "3bb5b4b6-ea4c-43ca-ba1c-3b69e29a6668"
}
```

**Response**

Here's an example of the response.

Note

The response object shown here may be truncated for brevity. All of the properties will be returned from an actual call.

```json
HTTP/1.1 200 OK
Content-type: application/json

{
    "id": "9e0f5c9c-44e3-ea11-bb43-000d3a2feca1",
    "number": "PS-INV103001",
    "externalDocumentNumber": "",
    "invoiceDate": "2019-01-15",
    "postingDate": "2019-01-15",
    "dueDate": "2019-01-15",
    "customerPurchaseOrderReference": "",
    "customerId": "f3a5738a-44e3-ea11-bb43-000d3a2feca1",
    "customerNumber": "20000",
    "customerName": "Trey Research",
    "billToName": "Trey Research",
    "billToCustomerId": "f3a5738a-44e3-ea11-bb43-000d3a2feca1",
    "billToCustomerNumber": "20000",
    "shipToName": "Trey Research",
    "shipToContact": "Helen Ray",
    "sellToAddressLine1": "153 Thomas Drive",
    "sellToAddressLine2": "",
    "sellToCity": "Chicago",
    "sellToCountry": "US",
    "sellToState": "IL",
    "sellToPostCode": "61236",
    "billToAddressLine1": "153 Thomas Drive",
    "billToAddressLine2": "",
    "billToCity": "Chicago",
    "billToCountry": "US",
    "billToState": "IL",
    "billToPostCode": "61236",
    "shipToAddressLine1": "153 Thomas Drive",
    "shipToAddressLine2": "",
    "shipToCity": "Chicago",
    "shipToCountry": "US",
    "shipToState": "IL",
    "shipToPostCode": "61236",
    "currencyId": "00000000-0000-0000-0000-000000000000",
    "currencyCode": "USD",
    "orderId": "00000000-0000-0000-0000-000000000000",
    "orderNumber": "",
    "paymentTermsId": "3bb5b4b6-ea4c-43ca-ba1c-3b69e29a6668",
    "shipmentMethodId": "00000000-0000-0000-0000-000000000000",
    "salesperson": "PS",
    "pricesIncludeTax": false,
    "remainingAmount": 0,
    "discountAmount": 0,
    "discountAppliedBeforeTax": true,
    "totalAmountExcludingTax": 164.7,
    "totalTaxAmount": 8.24,
    "totalAmountIncludingTax": 172.94,
    "status": "Paid",
    "lastModifiedDateTime": "2020-08-21T00:25:58.337Z",
    "phoneNumber": "",
    "email": "helen.ray@contoso.com"
}
```

## Related information

[Tips for working with the APIs](../../../developer/devenv-connect-apps-tips)[salesinvoice](../resources/dynamics_salesinvoice)[Get salesinvoice](dynamics_salesinvoice_get)[Delete salesinvoice](dynamics_salesinvoice_delete)[Create salesinvoice](dynamics_salesinvoice_create)
