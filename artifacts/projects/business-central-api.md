---
domain: artifacts
subdomain: projects
type: project
name: business-central-api
creator: "[[creators/microsoft]]"
source: "[[sources/microsoft--business-central-api-design]]"
ecosystem: ERP / Microsoft Dynamics 365
status: documentation-investigated
last-reviewed: 2026-11-04
---

# Business Central API

## Attributes

- **Unit:** externally callable business API system; sampled contracts, not the full product.
- **Evidence:** official documentation captured 2026-11-04; specific pages and hashes on [[sources/microsoft--business-central-api-design#root]].
- **Verification:** documentation read, no implementation inspection or API execution; no credentials, production access, writes, or installations.
- **Credibility:** first-party docs, not popularity or measured agent usability.

## Relationships

- **Publisher:** [[creators/microsoft]].
- **Research group:** [[projects/designing-apis-for-agents/README]].
- **Foundation:** [[concepts/business-platform-api-design]].
- **Comparison:** [[analyses/frontier-and-business-api-design]].

## Mechanism and themes

Business Central's API v2 combines company-scoped business resources, editable representations, and bound business actions. Sales invoices have GET/POST/PATCH/DELETE methods and a separate posting action under `salesInvoices({id})/Microsoft.NAV.post`; updating a record and posting its accounting document are distinct intents. [[sources/microsoft--business-central-api-design#invoice]]

### Contract inventory

| Area | Observed documented contract | Design consequence |
| --- | --- | --- |
| Identity and scope | `companies({id})/salesInvoices({id})`, immutable non-editable GUID and business number | Tenant/environment/company/resource context must survive agent handoffs. |
| Query versus command | Resource methods coexist with `Microsoft.NAV.post` bound action | CRUD does not cover all business state transitions. |
| Optimistic concurrency | Invoice PATCH requires `If-Match`; unmatched eTag blocks update; omitted properties remain or recalculate | Preserve version preconditions; do not rewrite full stale objects. |
| Composition | `$batch` with `Isolation: snapshot`; AL COMMIT can split transactions | One HTTP request is not unconditionally one transaction. |
| Events | Register/renew handshake, three-day subscription expiry, delayed/coalesced changes, collection notifications | Event maintenance and resynchronization belong in infrastructure. |
| Authority | OAuth app identity plus permission assignment in Business Central; SUPER cannot be assigned | Authentication scope alone is not the domain permission grant. |

The rows derive respectively from [[sources/microsoft--business-central-api-design#invoice]], [[sources/microsoft--business-central-api-design#update]], [[sources/microsoft--business-central-api-design#batch]], [[sources/microsoft--business-central-api-design#webhooks]], [[sources/microsoft--business-central-api-design#authorization]].

### Failure and evidence boundaries

The batch example returns successful-looking inner responses for operations whose changes are ultimately rolled back. A caller must interpret the whole transaction outcome, not count individual 200 responses. `Isolation: snapshot` requires the documented COMMIT caveat. [[sources/microsoft--business-central-api-design#batch]]

The webhook documentation describes change notifications rather than an immutable ordered ledger: a delay can coalesce changes and produce a collection filter. It also documents a delegated-admin change caveat, retry behavior, and deletion of subscriptions for some receiver errors. An agent should not infer complete business history from webhook count. [[sources/microsoft--business-central-api-design#webhooks]]

The invoice reference prints action names such as CANCEL and SEND in places where one might expect an HTTP method. This review relies on the explicit POST posting example and action names; it does not invent nonstandard HTTP methods or certify every sample. [[sources/microsoft--business-central-api-design#invoice]]

## Patterns demonstrated

- Candidate **explicit business intent plus execution lifecycle**: retained resources, action semantics and/or result state appear in the contracts above. No confirmed pattern added from documentation comparison alone; runnable implementation evidence remains a separate bar. [[sources/microsoft--business-central-api-design#root]]

## What we'd steal

- ★ Preserve distinct create/update/post business intents rather than a generic record writer. [[sources/microsoft--business-central-api-design#invoice]]
- ★ Carry environment, company, GUID, and business reference separately. [[sources/microsoft--business-central-api-design#invoice]]
- ★ Enforce exact eTag preconditions; wildcard If-Match examples do not detect a stale read. [[sources/microsoft--business-central-api-design#update]]
- Review the whole batch and its COMMIT boundary before promising atomicity. [[sources/microsoft--business-central-api-design#batch]]
- Keep subscription validation, renewal, coalescing, retry, and resync out of the model loop. [[sources/microsoft--business-central-api-design#webhooks]]
- Assign domain permissions separately from OAuth token acquisition. [[sources/microsoft--business-central-api-design#authorization]]
- Use partial updates and return updated representations where useful. [[sources/microsoft--business-central-api-design#update]]
- Expose action-specific errors and confirm authoritative business state after actions when needed. [[sources/microsoft--business-central-api-design#invoice]]

## Tensions and anti-patterns

- Documented conventions and samples can hide exceptions, configuration differences, or incomplete examples; they require current contract review before implementation. [[sources/microsoft--business-central-api-design#root]]
- Familiar HTTP syntax does not establish correct tenant, permission, business milestone, or recovery behavior. Our inference from the scoped contracts above, not a measured model-performance claim.
- This evidence does not establish that agents were trained on this API or perform well on it.

## Open questions and verification record

- How do these contracts behave under real concurrent edits, duplicate delivery, worker failures, or permission changes? Not runtime-tested in this pass.
- Which smaller capabilities deserve agent-facing wrappers for the target business domain? Requires task/permission evidence.
- Source anchors and links are mechanically checked during batch integration; live provider behavior remains unverified.
