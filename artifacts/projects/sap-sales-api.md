---
domain: artifacts
subdomain: projects
type: project
name: sap-sales-api
creator: "[[creators/sap]]"
source: "[[sources/sap--business-api-design]]"
ecosystem: SAP S/4HANA Cloud Public Edition
status: documentation-investigated
last-reviewed: 2026-11-04
---

# SAP sales APIs

## Attributes

- **Unit:** sampled Sales Order A2X OData V4 update/async contracts and OData V2 simulation contract, not all SAP APIs.
- **Version:** official APIs for Sales documentation, 2608 Latest, captured 2026-11-04.
- **Evidence:** browser-rendered excerpts; static retrieval returned a JavaScript shell. Collapsed examples were not relied on. No authenticated API execution, implementation inspection, or installations. [[sources/sap--business-api-design#root]]
- **Credibility:** first-party product documentation; popularity and agent success were not measured.

## Relationships

- [[creators/sap]] — publisher.
- [[projects/designing-apis-for-agents/README]] — research group.
- [[concepts/business-platform-api-design]] — foundation.
- [[analyses/frontier-and-business-api-design]] — comparative study.

## Mechanism and themes

### Execution duration is distinct from business intent

The V4 Sales Order API supports asynchronous requests using `prefer: respond-async`, with a location header pointing to the deferred API response. This is an established ERP counterexample to equating asynchronous execution with a frontier-only API design. This excerpt supports the negotiation and retrieval mechanism, not an uninspected universal job schema or a claim that every SAP service offers it. [[sources/sap--business-api-design#async]]

### Update contracts encode domain state and concurrency

PATCH requires entity keys and, except for the named pricing-element exceptions, an If-Match ETag of the sales order. Initial-valued properties can clear fields. Clients can request full or minimal representations. A business adapter must preserve these distinctions rather than blindly send the model's full object back. [[sources/sap--business-api-design#update]]

### Simulation is a separate business capability

The V2 simulation service computes pricing, availability and credit information without saving the simulated order. Which checks run depends on included associations; an empty association can be meaningful. Service metadata is exposed through `$metadata`. Simulation requires communication-scenario setup and excludes some order types, multi-order changesets, and particular save-time extension behavior. Therefore a successful simulation is not proof a later save will pass every check. [[sources/sap--business-api-design#simulation]]

## Patterns demonstrated

- Candidate **effect and execution axes**: simulation, version-checked update, minimal output, and deferred execution are independent choices in the documented interfaces. No confirmed pattern or implementation guarantee is promoted from these excerpts alone. [[sources/sap--business-api-design#root]]

## What we'd steal

- ★ Separate unsaved simulation from committing the business object. [[sources/sap--business-api-design#simulation]]
- ★ Preserve concurrency versions and domain-specific update exceptions. [[sources/sap--business-api-design#update]]
- ★ Negotiate response size independently of execution timing. [[sources/sap--business-api-design#update]], [[sources/sap--business-api-design#async]]
- Let long-running calls return a stable response retrieval location. [[sources/sap--business-api-design#async]]
- Publish machine-readable metadata alongside explanations. [[sources/sap--business-api-design#simulation]]
- Document which omitted, empty or initial-valued inputs mean skip, run, or clear. [[sources/sap--business-api-design#simulation]], [[sources/sap--business-api-design#update]]
- Describe simulation coverage and save-time checks it does not execute. [[sources/sap--business-api-design#simulation]]
- Expose warning truncation explicitly; absence from a returned list need not mean absence of a warning. [[sources/sap--business-api-design#simulation]]
- Carry communication-scenario requirements in capability discovery/setup. [[sources/sap--business-api-design#simulation]]

## Tensions and anti-patterns

- A broad provider comparison can accidentally combine different API versions into one imaginary interface. V4 update/async and V2 simulation remain explicitly separate here. [[sources/sap--business-api-design#root]]
- Simulation improves visibility but is not a transactional reservation or complete save-time validation. [[sources/sap--business-api-design#simulation]]
- GET/POST, OData, and schema familiarity do not establish correct business authority or user intent; this study did not measure agent behavior.

## Open questions and verification record

- Exact sample HTTP status codes, async result expiry and failure/cancellation semantics need a deeper ingest of the collapsed examples and linked lifecycle pages.
- How do custom extensions and tenant configuration affect simulation and mutation contracts? Not runtime-tested.
- Source text was read in a rendered browser; structured link/anchor checks run with the batch integration.
