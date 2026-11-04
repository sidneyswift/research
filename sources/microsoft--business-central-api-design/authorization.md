# Service-to-service authentication

Canonical URL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/automation-apis-using-s2s-authentication
Retrieved: 2026-11-04
Capture: vendor Markdown or rendered HTML text; scripts/navigation removed where identifiable.

---

---
layout: Conceptual
title: Using Service to Service Authentication - Business Central | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/automation-apis-using-s2s-authentication
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
description: Service-to-service authentication enables external services to connect as an application, without impersonating normal users.
ms.date: 2025-06-20T00:00:00.0000000Z
ms.topic: how-to
locale: en-us
document_id: 1555e693-76e8-b1d9-267f-bf06f068c9f4
document_version_independent_id: 725078be-b4d2-ced1-1ce0-52fc379f6a4e
updated_at: 2025-11-10T19:00:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/dynamics365smb-devitpro/blob/live/dev-itpro/administration/automation-apis-using-s2s-authentication.md
gitcommit: https://github.com/MicrosoftDocs/dynamics365smb-devitpro/blob/c5fa68cccf3638a4e554532c7215f6fd20fc4e83/dev-itpro/administration/automation-apis-using-s2s-authentication.md
git_commit_id: c5fa68cccf3638a4e554532c7215f6fd20fc4e83
site_name: Docs
depot_name: NAV.dev-itpro
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/NAV.dev-itpro/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
word_count: 1629
asset_id: administration/automation-apis-using-s2s-authentication
moniker_range_name: 
monikers: []
item_type: Content
source_path: dev-itpro/administration/automation-apis-using-s2s-authentication.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0160afd6-d1cc-4233-b94c-d06c3230d644
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/43093068-2dda-408b-b3fe-dfd705c84f78
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/92494c58-7e81-4229-ae85-bb895913ffe3
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/e453d60d-ba7e-43bc-8028-ec38e6b62512
platformId: 33e9d32e-b434-81ab-7bce-206df309fc6f
---

# Using Service to Service Authentication - Business Central | Microsoft Learn

Service-to-Service (S2S) authentication is suited for scenarios where integrations are required to run without any user interaction. S2S authentication uses the [Client Credentials OAuth 2.0 Flow](/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow). This flow enables you to access resources by using the identity of an application.

Note

For more information about OAuth 2.0 flows, see [OAuth 2.0 and OpenID Connect protocols on the Microsoft identity platform](/en-us/azure/active-directory/develop/active-directory-v2-protocols) in the Microsoft Entra ID documentation.

In contrast, OAuth delegate flows, like [authorization code](/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow), [implicit grant flow](/en-us/azure/active-directory/develop/v2-oauth2-implicit-grant-flow) and [resource owner password credentials](/en-us/azure/active-directory/develop/v2-oauth-ropc) can be configured to require multifactor authentication (MFA). This configuration prevents unattended integrations because MFA is required to acquire the access token from Microsoft Entra ID.

## Feature availability

The following table describes in which versions S2S authentication was made available for online or on-premises environments.

| API | Online | On-premises |
| --- | --- | --- |
| Business Central automation APIs | version 17.0 | versions 18.11 and 19.5 |
| Business Central APIs v1.0 | version 18.3 | versions 18.11 and 19.5 |
| Business Central APIs v2.0 | version 18.3 | versions 18.11 and 19.5 |
| Business Central custom APIs | version 18.3 | versions 18.11 and 19.5 |
| Business Central web services | version 18.3 | versions 18.11 and 19.5 |

## Main usage scenarios

Two main scenarios are enabled with S2S authentication:

1. Company setup using automation API

    Automation APIs provide capability for automating company setup through APIs. The automation APIs are used to hydrate tenants, that is, to bring them to an initial state.

    The **D365 Automation** entitlements give access to APIs in the `/api/microsoft/automation` route by using the OAuth client credentials flow. An application token with the `Automation.ReadWrite.All` scope is needed for accessing Business Central Automation APIs.
2. External user and non-interactive user access to APIs and web services.

    S2S authentication enables both external user and non-interactive user access to Business Central online. Refer to [license guide](https://www.microsoft.com/licensing/product-licensing/dynamics365) for scenarios and usage. An application token with the `API.ReadWrite.All` scope is needed for accessing Business Central APIs and web services.

Note

When you use S2S authentication, you can now use the integration session to create scheduled tasks. This capability is supported on 21.2 and later versions of Business Central online.

## Business Central on-premises prerequisite

Business Central on-premises must be configured for Microsoft Entra authentication with OpenID Connect.

Important

The `ValidAudiences` parameter of the Business Central must include the endpoint `https://api.businesscentral.dynamics.com`. If it doesn't, you get the error `Authentication_InvalidCredentials` on API requests, or the error `securitytokeninvalidaudienceexception` in the application log when you try to download symbols from Visual Studio.

Learn more in [Configure Microsoft Entra authentication with OpenID Connect](authenticating-users-with-azure-ad-openid-connect).

## Set up service-to-service authentication

To set up service-to-service authentication, you have to do two things:

- Register an application in your Microsoft Entra tenant for authenticating API calls against Business Central.
- Grant access for that application in Business Central.

These tasks are described in the sections that follow.

## Task 1: Register a Microsoft Entra application for authentication to Business Central

Complete these steps to register an application in your Microsoft Entra tenant for service-to-service authentication.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Register an application for Business Central in Microsoft Entra tenant.

    Follow the general guidelines at [Register your application with your Microsoft Entra tenant](/en-us/entra/identity-platform/quickstart-register-app).

    When you add an application to a Microsoft Entra tenant, you must specify the following information:

    | Setting | Description |
    | --- | --- |
    | Name | Specify a unique name for your application. |
    | Supported account types | Select either **Accounts in this organizational directory only (Microsoft only - Single tenant)** or **Accounts in any organizational directory (Any Microsoft Entra ID directory - Multitenant)**. |
    | Redirect URI | (optional) This setting is only required if you want to use the Business Central web client to grant consent to the API (see task 2). Otherwise, you can grant consent using the Azure portal.To specify the redirect URL, set the first box to **Web** to specify a web application. Then, enter the URL for your Business Central on-premises browser client, followed by *OAuthLanding.htm*, for example: `https://MyServer/BCnnn/OAuthLanding.htm` or `https://cronus.onmicrosoft.com/BCnnn/OAuthLanding.htm`, where `BCnnn`is the web server instance name, like BC260. This file is used to manage the exchange of data between Business Central and other services through Microsoft Entra ID.**Important:** The URL must match the URL of Web client, as it appears in the browser address. For example, even though the actual URL might be `https://MyServer:443/BCNNN/OAuthLanding.htm`, the browser typically removes the port number `:443`. |

    When completed, an **Overview** displays in the portal for the new application.

    Note

    Copy the **Application (client) ID** of the registered application. You need this value later. You can get this value from the **Overview** page.
3. Create a client secret for the registered application as follows:

    1. Select **Certificates & secrets** &gt; **New client secret**.
    2. Add a description, select a duration, and select **Add**.

    Note

    Copy the secret's value for use in your client application code. This secret value is never displayed again after you leave this page.

    Learn more about in [Add a client secret](/en-us/entra/identity-platform/how-to-add-credentials?tabs=client-secret) in the Microsoft Entra documentation.
4. Grant the registered application **API.ReadWrite.All** and **Automation.ReadWrite.All** permission to the **Dynamics 365 Business Central** API as follows:

    1. Select **API permissions** &gt; **Add a permission** &gt; **Microsoft APIs**.
    2. Select **Dynamics 365 Business Central**.
    3. Select **Application permissions**, select **API.ReadWrite.All** and **Automation.ReadWrite.All**, then select **Add permissions**.

        The **API permissions** page includes one of the following entries:

        | API / Permission name | Type | Description |
        | --- | --- | --- |
        | Dynamics 365 Business Central / Automation.ReadWrite.All | Application | Full access to automation |
        | Dynamics 365 Business Central / API.ReadWrite.All | Application | Access to APIs and webservices |

        Learn more in [Add permissions to access your APIs](/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#add-permissions-to-access-your-web-api).
    4. (optional) Grant admin consent on each permission by selecting it in the list, then selecting **Grant admin consent for &lt;tenant name&gt;**.

        This step isn't required if you're granting consent from the Business Central web client in task 2.

## Task 2: Set up the Microsoft Entra application in Business Central

Complete these steps to set up the Microsoft Entra application for service-to-service authentication in Business Central.

1. In the Business Central client, search for **Microsoft Entra applications** and open the page.
2. Select **New**.

    The **Microsoft Entra application Card** opens.
3. In the **Client ID** field, enter the **Application (Client) ID** for the registered application in Microsoft Entra ID from task 1.
4. Fill in the **Description** field. If a partner set up this application, enter sufficient partner-identifying information, so all applications set up by this partner can be tracked in the future if necessary.
5. Set the **State** to **Enabled**.
6. Assign permissions to objects as needed.

    Learn more in [Assign Permissions to Users and Groups](/en-us/dynamics365/business-central/ui-define-granular-permissions).

    Important

    Applications can't be assigned the **SUPER** permission set. Make sure that applications follow least-privilege principle and only assign permissions required for the integration to work.

    Note

    The system permission sets and user groups called **D365 AUTOMATION** and **EXTEN. MGT. - ADMIN** provide access to most typical objects used with automation.

    The **EXTEN. MGT. - ADMIN** permission set was introduced in Business Central 2021 release wave 1 as a replacement for the **D365 EXTENSION MGT** permission set in earlier versions.
7. (optional) Select **Grant Consent** and follow the wizard.

    This step grants consent to the API. This step is only required if you didn't grant consent from the Azure portal in task 1. You can only complete this step if you configured a redirect URL in the registered Microsoft Entra app.

    Tip

    Pre-consent can be done by adding the Microsoft Entra application to the **Adminagents** group in the partner tenant. Learn more in [Pre-consent your app for all your customers](/en-us/graph/auth-cloudsolutionprovider#pre-consent-your-app-for-all-your-customers) in the Graph documentation.

## Calling API and web services OAuth2Flows

After the Microsoft Entra application is set up and access granted, you're ready to make API and web service calls to Business Central.

For most cases, use the `AcquireTokenByAuthorizationCode` method from the OAuth 2.0 module. Learn more in [Microsoft identity platform and OAuth 2.0 authorization code flow](/en-us/entra/identity-platform/v2-oauth2-auth-code-flow). Explore an example at [OAuth2Flows](https://github.com/microsoft/BCTech/blob/master/samples/OAuth2Flows/TestOAuth2Flows.Page.al).

Important

When getting access tokens, it's important to keep security in mind. For example, ensure that you don't expose the tokens. You can do that in two ways:

- Make the method you're using non-debuggable. Here's an example of how to use the non-debuggable property for protecting access tokens:

```
   [NonDebuggable]
   procedure GetAccessToken(var AccessToken: Text): Boolean
   begin
       ...
   end;

```

- Set the `showMyCode` property to false for the extension.

Tip

You can also see this sample in the [BCTech GitHub repo](https://github.com/microsoft/BCTech/tree/master/samples/VSCRestClientOAuthBCAccess).

The following sample uses the [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for Visual Studio Code using the Client Credentials OAuth 2.0 flow. Using the Rest Client makes it easy to see which HTTP calls are made both against Business Central and Microsoft Entra ID. Any HTTP client can be used to create the following requests. Or you can choose any library, like MSAL (short for Microsoft Authentication Library). Remember to specify the scope as `https://api.businesscentral.dynamics.com/.default` and the Token URL as `https://login.microsoftonline.com/<tenantId>/oauth2/v2.0/token`.

```http
@tenantId = <tenant id>
@clientId = <client id>
@clientSecret = <client secret>
@baseUri = https://api.businesscentral.dynamics.com
@scope = {{baseUri}}/.default
@bcEnvironmentName = production
@url = {{baseUri}}/v2.0/{{bcEnvironmentName}}/api/v2.0

### Define entity, like customers, items, or vendors
@entityName =customers 

# @name auth
POST https://login.microsoftonline.com/{{tenantId}}/oauth2/v2.0/token HTTP/1.1
Content-type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id={{clientId}}
&client_secret={{clientSecret}}
&scope={{scope}}

### Variable Response
@accessHeader = Bearer {{auth.response.body.$.access_token}}

# @name GetCompanies
GET {{url}}/companies HTTP/1.1
Authorization: {{accessHeader}}

### Variable Response
@companyId = {{GetCompanies.response.body.value.[0].id}}
@companyUrl = {{url}}/companies({{companyId}})
@displayName = MyItemDisplayName2

### Get entities

# @name GetEntities
GET {{companyUrl}}/{{entityName}} HTTP/1.1
Authorization: {{accessHeader}}

### Create entity

# @name CreateEntity
POST {{companyUrl}}/{{entityName}} HTTP/1.1
Content-Type:  application/json
Authorization: {{accessHeader}}

{
 "displayName" : "{{displayName}}"
}

### Get created entity

# @name GetCreatedEntity
GET {{companyUrl}}/{{entityName}}/?$filter=displayName eq '{{displayName}}' HTTP/1.1
Authorization: {{accessHeader}}

#### Variable Response
@entityId = {{GetCreatedEntity.response.body.value.[0].id}}

### Modify entity

# @name ModifyEntity
PATCH {{companyUrl}}/{{entityName}}({{entityId}})
Authorization: {{accessHeader}}
Content-Type:  application/json
If-Match: *

{
    "displayName" : "DeleteMe-{{displayName}}"
}

### Delete entity

# @name DeleteItem
Delete {{companyUrl}}/{{entityName}}({{entityId}})
Authorization: {{accessHeader}}
```

## Related information

[OAuth2 and Microsoft Entra ID](/en-us/azure/active-directory/develop/active-directory-v2-protocols)[Client Credentials flow/S2S using MSAL library](/en-us/azure/active-directory/develop/scenario-daemon-overview)[C# samples using Client Credentials flow](https://github.com/Azure-Samples/active-directory-dotnetcore-daemon-v2)[OAuth 2.0 client credentials flow on the Microsoft identity platform](/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow)[Samples and libraries for OAuth: Microsoft identity platform authentication libraries](/en-us/azure/active-directory/develop/reference-v2-libraries)[Business Central Repository on GitHub - PowerShell samples using MSAL](https://github.com/microsoft/BCTech/tree/master/samples/PSOAuthBCAccess)[Business Central API v2.0](/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/)
