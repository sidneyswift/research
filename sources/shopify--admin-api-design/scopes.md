---
title: Shopify API access scopes
description: >-
  Access scopes control which store data your app can read and write. This guide
  lists available access scopes, grouped by scope type.
source_url:
  html: 'https://shopify.dev/docs/api/usage/access-scopes'
  md: 'https://shopify.dev/docs/api/usage/access-scopes.md'
---

# Shopify API access scopes

Access scopes control which store data your app can read and write. This guide lists available access scopes, grouped by scope type.

The [REST Admin API](https://shopify.dev/docs/api/admin-rest) uses authenticated access scopes too, listed in [access scopes for the REST Admin API](https://shopify.dev/docs/api/admin-rest/usage/access-scopes).

***

## How it works

Shopify grants access scopes only to [public or custom apps](https://shopify.dev/docs/apps/launch/distribution). Legacy app types, such as private or unpublished apps, don't get new access scopes.

Request only the data your app needs to function. Any scope that writes a resource also grants read access to it, so request the write scope only when your app needs both. Shopify restricts access to scopes for apps that don't have a legitimate use for the associated data.

| Scope type | Description | Example use cases |
| - | - | - |
| [Authenticated](#authenticated-access-scopes) | Controls access to resources in the [GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql), [Web Pixel API](https://shopify.dev/docs/api/web-pixels-api), and [Payments Apps API](https://shopify.dev/docs/api/payments-apps). Use authenticated access scopes to interact with a store on behalf of a user. | * Creating products
* Managing discount codes |
| [Unauthenticated](#unauthenticated-access-scopes) | Controls an app's access to [Storefront API](https://shopify.dev/docs/api/storefront) objects. Use unauthenticated access scopes to interact with a store on behalf of a customer. | - Viewing products
- Initiating a checkout |
| [Customer](#customer-access-scopes) | Controls an app's access to [Customer Account API](https://shopify.dev/docs/api/customer) objects. Use customer access scopes to interact with data that belongs to a customer. | * Viewing orders
* Updating customer details |

You declare all three types in the same `scopes` field, in the [`[access_scopes]` section](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration#access_scopes) of your app's configuration file. To see which scopes an installation has actually been granted, refer to [checking granted access scopes](#checking-granted-access-scopes).

**Tip:**

For more information on how to configure your access scopes, refer to [app configuration](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration) and [manage access scopes](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes).

If a call is failing with an access scope error, refer to [troubleshoot scope problems](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes#troubleshoot-scope-problems).

***

## Authenticated access scopes

Authenticated access scopes provide apps with read and write access to store data. Use authenticated access scopes to interact with a store on behalf of a user.

Some scopes and types in this table carry a label:

* Shopify approval required Shopify has to approve your app for the scope before you can declare it. Refer to [Shopify approval scopes](#shopify-approval-scopes) for how to request one.
* B2B only The type is only available to stores with [B2B](https://shopify.dev/docs/apps/build/b2b) enabled.
* Shopify Plus The type is only available to finance embedded apps, or to apps installed on a Shopify Plus or Advanced store. [Contact Shopify Support](https://partners.shopify.com/current/support/) to enable it for your app.

**Info:**

For a new app, [declare the scopes it needs](https://shopify.dev/docs/apps/build/authentication-authorization/cli-app-authentication#customize-your-access-scopes) and deploy your app. Merchants approve the scopes when they install it. To assign scopes to an existing admin-created custom app, refer to [change API scopes](https://shopify.dev/docs/apps/build/authentication-authorization/legacy/admin-custom-apps#change-api-scopes).

| Scope | Access |
| - | - |
| `read_all_orders`[Approval requirements](#orders-permissions) | All relevant [orders](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) rather than the default window of orders created within the last 60 days.Doesn't grant access on its own. Declare it alongside `read_orders` or `write_orders` to extend that scope to older orders. Despite its `read_` prefix, it also extends `write_orders` to older orders, but it doesn't grant write access by itself. Refer to [orders permissions](#orders-permissions). |
| `read_analytics_annotations``write_analytics_annotations` | `AnalyticsAnnotation`Available as of API version `2026-10`. |
| `write_app_proxy` | [App proxy](https://shopify.dev/docs/apps/build/online-store/display-dynamic-data) configuration |
| `read_apps`Shopify approval required | The `heldByApp` field on `FulfillmentHold`, which identifies the app that created the fulfillment hold. |
| `read_assigned_fulfillment_orders``write_assigned_fulfillment_orders``read_merchant_managed_fulfillment_orders``write_merchant_managed_fulfillment_orders``read_third_party_fulfillment_orders``write_third_party_fulfillment_orders``read_marketplace_fulfillment_orders` Shopify approval required | `FulfillmentOrder`As of API version 2024-10, `write_third_party_fulfillment_orders` will no longer allow [order management apps](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps) to create fulfillments for fulfillment orders that have been assigned to a different fulfillment service app. |
| `read_cart_transforms``write_cart_transforms` | `CartTransform` |
| `read_cash_tracking``write_cash_tracking` | The `CashDrawer`, `CashTrackingSession`, and `PointOfSaleDevicePaymentSession` objects, and the cash drawer and reason code mutations, such as `cashDrawerCreate` and `cashManagementReasonCodeCreate`. These scopes are checked against POS access, so with an [online access token](https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens#online-access-tokens) they resolve only for a staff member who has it, which requires the Point of Sale channel on the store. |
| `read_checkout_and_accounts_configurations``write_checkout_and_accounts_configurations` | `CheckoutAndAccountsConfiguration` |
| `read_checkout_branding_settings``write_checkout_branding_settings` | `CheckoutBranding` |
| `read_checkout_settings``write_checkout_settings`Shopify approval required | The `CheckoutAndAccountsConfiguration` object and the `checkoutAndAccountsConfigurationUpdate` mutation. Accepted as an alternative to `read_checkout_and_accounts_configurations` and `write_checkout_and_accounts_configurations`.The object and the mutation are available as of API version 2026-04. The mutation also requires the `manage_checkout_settings` user permission, and a store with access to the checkout and accounts editor and to the contextualized checkouts and customer accounts feature. Modifying configuration overrides additionally requires the `view_markets` and `create_and_edit_markets` user permissions. |
| `read_companies``write_companies` | The company objects, including `Company`, `CompanyLocation`, `CompanyContact`, and `CompanyAddress`, and the company mutations, such as `companyCreate` and `companyLocationUpdate`. B2B onlyAccepted as an alternative to `read_customers` and `write_customers`. |
| `read_content``write_content``read_online_store_pages` | `Article``Blog``Comment``Page` |
| `read_customer_data_erasure``write_customer_data_erasure` | The `customerRequestDataErasure` and `customerCancelDataErasure` mutations. The read scope covers the `CustomerRequestDataErasureUserError` and `CustomerCancelDataErasureUserError` types that those mutations return. |
| `read_customer_merge``write_customer_merge` | `CustomerMergePreview``CustomerMergeRequest` |
| `read_customer_payment_methods`Shopify approval required | `CustomerPaymentMethod` |
| `read_customers``write_customers` | `Customer``Company` B2B only`CompanyLocation` B2B only`Segment` |
| `read_delivery_customizations``write_delivery_customizations` | `DeliveryCustomization` |
| `read_delivery_promises``write_delivery_promises`Shopify approval required | `DeliveryPromiseParticipant` and `DeliveryPromiseProvider` objects, the `deliveryPromiseParticipants` and `deliveryPromiseProvider` queries, and the `deliveryPromiseParticipantsUpdate` and `deliveryPromiseProviderUpsert` mutations. |
| `read_discounts``write_discounts` | `DiscountAutomaticNode` and `DiscountCodeNode` objects and the discount types they wrap, the `discountNodes`, `automaticDiscountNodes`, and `codeDiscountNodes` queries, and the discount mutations, such as `discountCodeBasicCreate` and `discountAutomaticBasicCreate`.To build discount functions, refer to [discounts](https://shopify.dev/docs/apps/build/discounts). |
| `read_draft_orders``write_draft_orders` | `DraftOrder` |
| `read_files``write_files` | The `File` interface and the objects that implement it, including `GenericFile`, `MediaImage`, `Video`, and `Model3d`, the `files` query, and the file mutations, such as `fileCreate` and `fileUpdate`. |
| `read_financial_kyc_information`Shopify approval required | `FinanceKycInformation` and `FinancialKycShopOwner` objects.Accepted as an alternative to `read_shopify_payments`, `read_shopify_payments_legal_entities`, or `read_capital` on some Shopify Payments objects, and as an alternative to `read_users` on `FinanceAppAccessPolicy`. |
| `read_fulfillment_constraint_rules``write_fulfillment_constraint_rules` | The `FulfillmentConstraintRule` object and `fulfillmentConstraintRules` query, and the `fulfillmentConstraintRuleCreate`, `fulfillmentConstraintRuleUpdate`, and `fulfillmentConstraintRuleDelete` mutations |
| `read_fulfillments``write_fulfillments` | `FulfillmentService` |
| `read_gift_card_transactions``write_gift_card_transactions` | The `GiftCardTransaction` interface and the objects that implement it, including `GiftCardCreditTransaction`, `GiftCardDebitTransaction`, and `GiftCardCashOutTransaction`, and the `giftCardCredit` and `giftCardDebit` mutations. The read scope covers the `GiftCardTransactionUserError` type that those mutations return. |
| `read_gift_cards``write_gift_cards` | `GiftCard` |
| `read_inventory``write_inventory` | `InventoryItem``InventoryLevel` |
| `read_inventory_shipments``write_inventory_shipments` | `InventoryShipment``InventoryShipmentLineItem``InventoryShipmentTracking` |
| `read_inventory_shipments_received_items``write_inventory_shipments_received_items` | Received items on an `InventoryShipment`. `write_inventory_shipments_received_items` authorizes the [`inventoryShipmentReceive`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/inventoryShipmentReceive) mutation. Received quantities are returned on `InventoryShipment` and `InventoryShipmentLineItem`, which `read_inventory_shipments` grants access to. |
| `read_inventory_transfers``write_inventory_transfers` | `InventoryTransfer``InventoryTransferLineItem` |
| `read_legal_policies``write_legal_policies` | `ShopPolicy` object and the `shopPolicyUpdate` mutation |
| `read_locales``write_locales` | `ShopLocale` |
| `read_locations``write_locations` | `Location` |
| `read_marketing_events``write_marketing_events` | `MarketingEvent``MarketingActivity` |
| `read_marketplace_orders``write_marketplace_orders`Shopify approval required | The `Order` object and the objects it wraps, such as `LineItem`, `Fulfillment`, and `Refund`, and the `orderCancel`, `orderCapture`, and `orderUpdate` mutations.Accepted as an alternative to `read_orders` and `write_orders`, but not equivalent to them: these scopes return only the orders attributed to your app, not every order on the store. |
| `read_marketplace_returns``write_marketplace_returns`Shopify approval required | The `Return`, `ReturnLineItem`, `ReverseDelivery`, and `ReverseFulfillmentOrder` objects, and the return mutations, such as `returnCreate` and `returnRefund`. Accepted as an alternative to `read_returns` and `write_returns`. |
| `read_markets``write_markets` | `Market` |
| `read_merchant_approval_signals`Shopify approval required | `MerchantApprovalSignals` |
| `read_metaobject_definitions``write_metaobject_definitions` | `MetaobjectDefinition` |
| `read_metaobjects``write_metaobjects` | `Metaobject` |
| `read_mobile_platform_applications``write_mobile_platform_applications`Shopify approval required | `AndroidApplication` and `AppleApplication` objects, which make up the `MobilePlatformApplication` union, and the `mobilePlatformApplicationCreate`, `mobilePlatformApplicationUpdate`, and `mobilePlatformApplicationDelete` mutations.Contact Shopify Support to enable these access scopes for your app. |
| `read_online_store_navigation``write_online_store_navigation` | `UrlRedirect` |
| `write_online_store_pages` | Article, blog, comment, and page mutations, such as `pageCreate` and `articleUpdate`. Accepted as an alternative to `write_content`. |
| `read_order_edits``write_order_edits` | `CalculatedOrder` |
| `read_orders``write_orders` | `AbandonedCheckout`, `Fulfillment`, `Order`, `OrderTransaction`, `DeliveryCarrierService``read_orders` provides read access and `write_orders` provides read and write access. Both cover orders created within the last 60 days. For older orders, add `read_all_orders` and follow the [approval requirements for your app](#orders-permissions). |
| `read_own_subscription_contracts``write_own_subscription_contracts`Shopify approval required | GraphQL Admin API `SubscriptionContract`Customer Account API `SubscriptionContract` |
| `read_payment_customizations``write_payment_customizations` | `PaymentCustomization` |
| `read_payment_gateways``write_payment_gateways`Shopify approval required | Payments Apps API `PaymentsAppConfiguration` |
| `read_payment_mandate``write_payment_mandate`Shopify approval required | `PaymentMandate` |
| `read_payment_sessions``write_payment_sessions`Shopify approval required | Payments Apps API `PaymentSession`, `CaptureSession`, `RefundSession`, `VerificationSession`, `VoidSession` |
| `read_payment_terms``write_payment_terms` | `PaymentTerms``PaymentSchedule` |
| `read_pixels``write_pixels``read_customer_events` | `WebPixel` and `ServerPixel` objects, and the `webPixelCreate`, `webPixelUpdate`, `webPixelDelete`, `serverPixelCreate`, and `serverPixelDelete` mutations.Creating or updating a pixel needs `write_pixels` and `read_customer_events` together. Server pixels also need the `read_server_pixels` and `write_server_pixels` scopes, which Shopify grants on approval. Refer to the [Web Pixels API](https://shopify.dev/docs/api/web-pixels-api). |
| `read_price_rules``write_price_rules` | `PriceRule` |
| `read_privacy_settings``write_privacy_settings` | `PrivacySettings``CookieBanner` |
| `read_product_listings` | `ProductFeed` object, the `publishedOnCurrentChannel` field on `Product`, `ProductVariant`, and `Collection`, and full sync mutations such as `productFullSync`. Accepted as an alternative to `read_products` on some fields. |
| `read_products``write_products` | `Product`, `ProductVariant`, `Collection`, `ResourceFeedback``SellingPlan` (also requires `read_purchase_options` or `read_own_subscription_contracts` for queries, and `write_purchase_options` or `write_own_subscription_contracts` for mutations) |
| `read_publications``write_publications` | Publication fields on `Product`, `Collection`, and `ProductVariant`, such as `publications` and `resourcePublications`, and publishing mutations such as `productPublish` and `publicationCreate`. Also accepted as `read_channels` and `write_channels`. |
| `read_reports``write_reports` | `shopifyqlQuery`, `AnalyticsTarget``AnalyticsTarget` is available as of API version `2026-10`. |
| `read_resource_feedbacks``write_resource_feedbacks` | `ProductResourceFeedback` and `DiscountResourceFeedback` objects. `DiscountResourceFeedback` is available only in the `unstable` API version. The app must be configured as a sales channel or to use the Storefront API. |
| `read_returns``write_returns` | The `Return` object, the reverse logistics objects, such as `ReverseDelivery` and `ReverseFulfillmentOrder`, and the return mutations, such as `returnCreate` and `returnRefund`. |
| `read_rollouts` | The `Rollout` and `RolloutTreatment` objects and the rollout change types, such as `RolloutChange`, through the `rollout` and `rollouts` queries and the `rollouts` field on discounts. To read the resource that a change affects, the app also needs that resource's access scope, such as `read_discounts`. Otherwise, the resource field returns `null`.Available as of API version `2026-10`. |
| `read_script_tags``write_script_tags` | `ScriptTag` |
| `read_shipping``write_shipping` | `DeliveryCarrierService` |
| `read_shopify_payments`Shopify approval required | `ShopifyPaymentsAccount` and `ShopifyPaymentsPayoutSchedule` objects, and charge statement descriptors such as `ShopifyPaymentsDefaultChargeStatementDescriptor` and `ShopifyPaymentsJpChargeStatementDescriptor`.`read_shopify_payments_accounts` and `read_shopify_payments_payouts` are accepted as alternatives for some of these objects. |
| `read_shopify_payments_accounts` | `ShopifyPaymentsAccount` and `ShopifyPaymentsPayoutSchedule` objects. Accepted as an alternative to `read_shopify_payments`. |
| `read_shopify_payments_accounts_sensitive`Shopify approval required | The `accountOpenerName` field on `ShopifyPaymentsAccount`. |
| `read_shopify_payments_bank_accounts` | `ShopifyPaymentsBankAccount` |
| `read_shopify_payments_dispute_evidences``write_shopify_payments_dispute_evidences`Shopify approval required | `ShopifyPaymentsDisputeEvidence`, `ShopifyPaymentsDisputeFileUpload`Request access [from Shopify](#shopify-payments-dispute-evidence-permissions). |
| `read_shopify_payments_dispute_file_uploads``write_shopify_payments_dispute_file_uploads`Shopify approval required | Dispute file upload endpoints of the REST Admin API.Request access [from Shopify](#shopify-payments-dispute-evidence-permissions). |
| `read_shopify_payments_disputes` | `ShopifyPaymentsDispute` |
| `read_shopify_payments_payouts` | `ShopifyPaymentsPayout``ShopifyPaymentsBalanceTransaction` |
| `read_store_credit_account_transactions``write_store_credit_account_transactions` | `StoreCreditAccountCreditTransaction``StoreCreditAccountDebitTransaction` |
| `read_store_credit_accounts` | `StoreCreditAccount` |
| `read_taxes`Shopify approval required | `TaxAppConfiguration` and `TaxSettings` objects.Reading `TaxAppConfiguration` also requires the user to have permission to manage taxes. `read_customers` is accepted as an alternative for `TaxSettings`. |
| `write_taxes`Shopify approval required | `taxAppConfigure` and `taxSummaryCreate` mutations. Limited to tax calculation apps. |
| `read_themes``write_themes` | `OnlineStoreTheme` |
| `read_translations``write_translations` | `Translation``TranslatableResource` |
| `read_users`Shopify approval required | `StaffMember` Shopify PlusThis type is available to finance embedded apps, and to apps installed on a store on the Shopify Plus or Advanced plan. Contact Shopify Support to enable this access scope for your app. |
| `read_validations``write_validations` | `Validation` |

***

## Unauthenticated access scopes

Unauthenticated access scopes provide apps with read and write access to the [Storefront API](https://shopify.dev/docs/api/storefront). Use unauthenticated access scopes to interact with a store on behalf of a customer.

**Info:**

For the Headless channel, permissions are managed in your Shopify admin. Refer to [request storefront permissions](https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/manage-headless-channels#request-storefront-permissions).

| Scope | Access |
| - | - |
| `unauthenticated_read_checkouts``unauthenticated_write_checkouts` | `Cart` |
| `unauthenticated_read_content` | Storefront content, such as `Article`, `Blog`, and `Comment` |
| `unauthenticated_read_customer_tags` | `tags` field on `Customer` |
| `unauthenticated_read_customers``unauthenticated_write_customers` | `Customer` |
| `unauthenticated_read_metaobjects` | `Metaobject``MetaobjectField``MetaobjectSEO` |
| `unauthenticated_read_product_inventory` | `quantityAvailable` field on `ProductVariant` and `totalAvailable` field on `Product` |
| `unauthenticated_read_product_listings` | `Product``Collection` |
| `unauthenticated_read_product_pickup_locations` | `Location``StoreAvailability` |
| `unauthenticated_read_product_tags` | `tags` field on `Product` |
| `unauthenticated_read_selling_plans` | Selling plan content on `Product` |
| `unauthenticated_read_shop_pay_installments_pricing` | `shopPayInstallmentsPricing` field on `Shop` and `ProductVariant` |

***

## Customer access scopes

Customer access scopes provide apps with read and write access to the [Customer Account API](https://shopify.dev/docs/api/customer). Use customer access scopes to interact with data that belongs to a customer.

Some fields in the Customer Account API reference list a required access scope that records an authentication state rather than a scope you request, such as `customer_read_pre_authenticated`. Those aren't listed here — refer to [Order status page authentication states](https://shopify.dev/docs/apps/build/customer-accounts/order-status-page#authentication-states).

**Info:**

To request these scopes for the Headless or Hydrogen channel, refer to [managing permissions](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/getting-started#step-2-configure-customer-account-api-access).

| Scope | Access |
| - | - |
| `customer_read_companies``customer_write_companies` | `Company` |
| `customer_read_customers``customer_write_customers` | `Customer` |
| `customer_read_draft_orders` | `DraftOrder` |
| `customer_read_locations``customer_write_locations` | `CompanyLocation` |
| `customer_read_markets` | `Market` |
| `customer_read_metaobjects` | `Metaobject` |
| `customer_read_orders``customer_write_orders` | `Order` |
| `customer_read_own_subscription_contracts``customer_write_own_subscription_contracts` | `SubscriptionContract` for records that belong to your app |
| `customer_read_store_credit_account_transactions` | `StoreCreditAccountTransaction` interface and the types that implement it, such as `StoreCreditAccountCreditTransaction` and `StoreCreditAccountDebitTransaction` |
| `customer_read_store_credit_accounts` | `StoreCreditAccount` |
| `customer_write_subscription_contracts` | `SubscriptionContract` for all records. Only available for Hydrogen and Headless storefronts |

***

## Requesting specific permissions

Some access scopes need Shopify's approval before you can declare them. Most are requested in the Partner Dashboard, but some require contacting Shopify Support.

### Shopify approval scopes

Shopify grants some access scopes to individual apps rather than to every app that declares them. You can't add one to your app configuration until Shopify approves your app for it. If you declare one before approval, then creating an app version fails with an `app_access` validation error on `scopes`.

Scopes labeled Shopify approval required in the tables above require approval. Some scopes have a specific request path or an automatic approval exception:

* `read_all_orders`: [approval requirements for historical orders](#orders-permissions).
* `read_customer_payment_methods`, `read_own_subscription_contracts`, and `write_own_subscription_contracts`: [request access for the Subscription APIs](#subscription-apis-permissions)
* `read_shopify_payments_dispute_evidences`, `write_shopify_payments_dispute_evidences`, `read_shopify_payments_dispute_file_uploads`, and `write_shopify_payments_dispute_file_uploads`: [request access for dispute evidence](#shopify-payments-dispute-evidence-permissions)
* `write_payment_gateways` and `write_payment_sessions`: granted automatically through your payments extension. Omit them from your `shopify.app.toml` file on initial deployment, then add them in a later deployment to request them from the merchant. Refer to [payments app configuration](https://shopify.dev/docs/apps/build/payments/configuration).

For every other labeled scope, [contact Shopify Support](https://partners.shopify.com/current/support/) and describe your app and why it needs the scope.

Protected customer data is reviewed separately, and that review isn't scope approval. You can declare the scopes that access protected customer data before your app is approved to use it. Refer to [protected customer data](#protected-customer-data-permissions) for what the API returns until then.

### Orders permissions

By default, `read_orders` provides read access and `write_orders` provides read and write access to orders created within the last 60 days. `read_all_orders` doesn't grant access on its own. Declare it alongside `read_orders` or `write_orders` to extend that scope's access to older orders:

| Scopes | Access |
| - | - |
| `read_orders` | Read orders created within the last 60 days |
| `write_orders` | Read and write orders created within the last 60 days |
| `read_orders` and `read_all_orders` | Read all orders, including older orders |
| `write_orders` and `read_all_orders` | Read and write all orders, including older orders |

Despite its `read_` prefix, `read_all_orders` extends whichever order scope your app has. With `write_orders`, your app can update older orders as well as read them. Write access always comes from `write_orders`: `read_all_orders` doesn't grant it.

**Note:**

Apps created in the Dev Dashboard under a merchant organization for use on stores in that organization don't need to request Shopify approval for `read_all_orders`. Add the scope to your app's [configuration](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes#where-you-configure-scopes) and release a new app version, or deploy the change with Shopify CLI. Then [check the granted scopes](#checking-granted-access-scopes) for your app installation.

For apps created under a Partner organization, request Shopify approval before declaring the scope:

1. From the Partner Dashboard, go to [**Apps**](https://partners.shopify.com/current/apps).
2. Click the name of your app.
3. Click **API access requests**.
4. In the **Access requests** section, on the **Read all orders scope** card, click **Request access**.
5. On the **Orders** page that opens, describe your app and why you're applying for access.
6. Click **Request access**.

After Shopify approves your request, [declare the scope and deploy the change](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes#modify-declared-scopes).

### Subscription APIs permissions

Subscription apps let users sell subscription products that generate multiple orders on a specific billing frequency.

With subscription products, the app user isn't required to get customer approval for each subsequent order after the initial subscription purchase. As a result, your app needs to request the required protected access scopes to use Subscription APIs from the app user:

1. From the Partner Dashboard, go to [**Apps**](https://partners.shopify.com/current/apps).
2. Click the name of your app.
3. Click **API access requests**.
4. In the **Access requests** section, on the **Access Subscriptions APIs** card, click **Request access**.
5. On the **Subscriptions** page that opens, describe why you're applying for access.
6. Click **Request access**.

After Shopify approves your request, declare the scopes your app requires. Subscription apps require `read_customer_payment_methods`, `read_own_subscription_contracts`, and `write_own_subscription_contracts`. For the full list of scopes by use case, refer to [purchase options](https://shopify.dev/docs/apps/build/purchase-options).

If your app uses the Customer Account API, then it also requires `customer_read_own_subscription_contracts` or `customer_write_own_subscription_contracts`.

### Shopify Payments dispute evidence permissions

The `read_shopify_payments_dispute_evidences`, `write_shopify_payments_dispute_evidences`, `read_shopify_payments_dispute_file_uploads`, and `write_shopify_payments_dispute_file_uploads` scopes are restricted. Shopify grants these scopes to individual apps. To be eligible:

* Your app must use [public distribution](https://shopify.dev/docs/apps/launch/distribution/select-distribution-method)
* Dispute or chargeback management must be a core part of what your app does. Apps outside the dispute space aren't granted these scopes

You can't add these scopes to your app configuration until Shopify approves your app for them. If you declare one before approval, then creating an app version fails with an `app_access` validation error on `scopes`.

To request access, [contact Shopify Support](https://partners.shopify.com/current/support/) and describe your app and why it needs to read or submit dispute evidence.

### Theme permissions

Most apps that integrate with a theme should use [theme app extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions). If your app uses [public distribution](https://shopify.dev/docs/apps/launch/distribution/select-distribution-method) and needs to modify a theme or theme files, then it needs an exemption in addition to the `write_themes` scope.

An exemption covers the specific use case that you describe in your request. We occasionally review usage of these scopes, and we might revoke an exemption as a result.

To request an exemption, [submit the exemption request form](https://docs.google.com/forms/d/e/1FAIpQLSfZTB1vxFC5d1-GPdqYunWRGUoDcOheHQzfK2RoEFEHrknt5g/viewform) and describe your app and why it needs to modify a theme or theme files.

### Protected customer data permissions

By default, apps don't have access to any protected customer data. To access protected customer data, you must meet our [protected customer data requirements](https://shopify.dev/docs/apps/launch/protected-customer-data#requirements). You can add the relevant scopes to your app, but the API won't return data from non-development stores until your app is configured and approved for protected customer data use.

***

## Checking granted access scopes

Declaring a scope isn't the same as having it. A scope takes effect only after it's approved on the store, and [optional scopes](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes#optional_scopes) are granted separately, after installation, so an app's granted scopes can differ from the ones in its configuration.

To see what an installation actually has, query [`currentAppInstallation`](https://shopify.dev/docs/api/admin-graphql/latest/queries/currentAppInstallation) in the GraphQL Admin API. Its `accessScopes` field returns each granted scope's `handle`, such as `read_orders`, with a `description` of what that scope allows.

For a request and response example, and for the App Bridge and React Router helpers that wrap this query, refer to [query currently granted scopes](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes#query-currently-granted-scopes).

***

## Next steps

* Learn how [API authentication](https://shopify.dev/docs/api/usage/authentication) works, and which token and header each Shopify API uses.
* Learn how to declare, modify, and revoke your app's scopes in [manage access scopes](https://shopify.dev/docs/apps/build/authentication-authorization/manage-access-scopes).

***
