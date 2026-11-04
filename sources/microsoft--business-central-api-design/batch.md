# Transactional batches

Canonical URL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/use-odata-batch
Retrieved: 2026-11-04
Capture: vendor Markdown or rendered HTML text; scripts/navigation removed where identifiable.

---

---
layout: Conceptual
title: Using OData transactional $batch requests - Business Central | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/use-odata-batch
feedback_system: Standard
feedback_product_url: https://experience.dynamics.com/ideas/categories/?forum=e288ef32-82ed-e611-8101-5065f38b21f1&forumName=Dynamics%20365%20Business%20Central
ms.author: jswymer
ms.reviewer: jswymer
uhfHeaderId: MSDocsHeader-Dynamics365-BusinessCentral
search.app:
- businesscentral
- businesscentral-docs
search.audienceType: admin, developer
breadcrumb_path: /dynamics365/business-central/dev-itpro/breadcrumb/toc.json
ms.service: dynamics-365-business-central
recommendations: true
author: jswymer
description: How to specify that all inner requests in a certain OData $batch request are processed in a transactional way in Business Central.
ms.custom: bap-template
ms.date: 2023-04-25T00:00:00.0000000Z
ms.topic: concept-article
locale: en-us
document_id: aca1566a-1dc8-e031-1777-002babf06034
document_version_independent_id: aca1566a-1dc8-e031-1777-002babf06034
updated_at: 2025-05-07T13:00:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/dynamics365smb-devitpro/blob/live/dev-itpro/webservices/use-odata-batch.md
gitcommit: https://github.com/MicrosoftDocs/dynamics365smb-devitpro/blob/8a22a8201f4fef800cc9234e5b56c8355c7223b0/dev-itpro/webservices/use-odata-batch.md
git_commit_id: 8a22a8201f4fef800cc9234e5b56c8355c7223b0
site_name: Docs
depot_name: NAV.dev-itpro
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/NAV.dev-itpro/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
word_count: 445
asset_id: webservices/use-odata-batch
moniker_range_name: 
monikers: []
item_type: Content
source_path: dev-itpro/webservices/use-odata-batch.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/86a4b315-a9f1-4577-b985-6fb0e0e67420
- https://authoring-docs-microsoft.poolparty.biz/devrel/0160afd6-d1cc-4233-b94c-d06c3230d644
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/96ac410d-d052-4707-8007-df31dd0fe041
- https://authoring-docs-microsoft.poolparty.biz/devrel/92494c58-7e81-4229-ae85-bb895913ffe3
platformId: 089f2631-5d24-4170-6769-7cf7e5ac4dcb
---

# Using OData transactional $batch requests - Business Central | Microsoft Learn

> 
> **APPLIES TO:** Business Central 2020 release wave 2 (version 17.1) and later

It's possible to specify that all inner requests in a certain OData $batch request are processed in a transactional way. Unless it's invoked commit, if an inner request fails after another request(s) has committed changes, all changes within a batch will be reverted as if the batch request never happened. Transactional $batch requests are useful in scenarios where a single business operation spans multiple requests, because they prevent adverse effects if parts of the operation fail. Also, they can improve performance by reducing the number of requests the client needs to do when errors occur.

## Enable OData transactional batch behavior

To enable transactional batch behavior, include the `Isolation: snapshot` header with the $batch request. The `Isolation: snapshot` header makes the entire batch to run within the same session. If the AL code doesn't invoke COMMIT, then the entire batch runs in the same transaction. Otherwise, for each commit, the transaction is committed, and a new one is started.

The [CommitBehavior attribute](../developer/attributes/devenv-commitbehavior-attribute) can be used to override the COMMIT behavior of the invoked method.

## Example

```
POST businesscentralPrefix/api/v2.0/$batch HTTP/1.1
```

## Request headers

| Header | Value |
| --- | --- |
| Authorization | Bearer {token}. Required. |
| Content-Type | application/json. Required for JSON Batch content. |
| Accept | application/json |
| Isolation | snapshot |

## Request body

The following request body contains three inner requests. The first two requests should execute successfully. The last request includes content that triggers a validation failure, so the request fails.

```json
{
       "requests": [
              {
                     "method": "PATCH",
                     "url": "items(7ce0af2e-0963-460f-9b1f-0014aea3e117)",
                     "headers": {
                           "Company": "CRONUS International Ltd.",
                           "Content-Type": "application/json",
                           "If-Match": "*"
                     },
                     "body": {
                           "displayName": "Touring Bicycle v2"
                     }
              },
              {
                     "method": "PATCH",
                     "url": "items(7ce0af2e-0963-460f-9b1f-0014aea3e117)/picture(7ce0af2e-0963-460f-9b1f-0014aea3e117)/contentValue",
                     "headers": {
                           "Company": "CRONUS International Ltd.",
                           "Content-Type": "application/json",
                           "If-Match": "*"
                     },
                     "body": {
                           "value": "Picture Blob"
                     }
              },      
              {
                     "method": "PATCH",
                     "url": "items(7ce0af2e-0963-460f-9b1f-0014aea3e117)",
                     "headers": {
                           "Company": "CRONUS International Ltd.",
                           "Content-Type": "application/json",
                           "If-Match": "*"
                     },
                     "body": {
                           "type": "Invalid Type"
                     }
              }
       ]
}
```

## Response

The following response includes successful responses for the first two inner requests, and an error for the last inner request. Because the `Isolation: snapshot` header was present in the batch request, none of the changes made by either of the successful inner requests are applied after completion of the batch request.

```json
{
       "responses": [
              {
                     "id": null,
                     "status": 200,
                     "headers": {
                           "content-type": "application/json; odata.metadata=minimal",
                           "odata-version": "4.0"
                     },
                     "body": {
                           "displayName": "Touring Bicycle v2",
                           // ...
                     }
              },
              {
                     "id": null,
                     "status": 204,
                     "headers": {}
              },
              {
                     "id": null,
                     "status": 400,
                     "headers": {
                           "content-type": "application/json; odata.metadata=minimal",
                           "odata-version": "4.0"
                     },
                     "body": {
                           "error": {
                                  "code": "Unknown",
                                  "message": "'Invalid Type' is not an option. The existing options are: Inventory,Service,Non-Inventory  CorrelationId:  x."
                           }
                     }
              }
       ]
}
```

## Related information

[OData Web Services](odata-web-services)[Using OData to Return-Obtain a JSON Document](return-obtain-json-document)
