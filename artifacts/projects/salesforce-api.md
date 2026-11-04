---
domain: artifacts
subdomain: projects
type: project
name: salesforce-api
creator: "[[creators/salesforce]]"
source: "[[sources/salesforce--business-api-design]]"
ecosystem: CRM / business operations
status: documentation-investigated
last-reviewed: 2026-11-04
---

# Salesforce REST and Bulk APIs

## Attributes

- **Unit:** externally callable business API system; sampled contracts, not the full product.
- **Evidence:** official documentation captured 2026-11-04; specific pages and hashes on [[sources/salesforce--business-api-design#root]].
- **Verification:** documentation read, no implementation inspection or API execution; no credentials, production access, writes, or installations.
- **Credibility:** first-party docs, not popularity or measured agent usability.

## Relationships

- **Publisher:** [[creators/salesforce]].
- **Research group:** [[projects/designing-apis-for-agents/README]].
- **Foundation:** [[concepts/business-platform-api-design]].
- **Comparison:** [[analyses/frontier-and-business-api-design]].

## Mechanism and themes

Salesforce provides both dependent REST request composition and durable asynchronous query jobs. This is an established-business counterexample to the idea that task resources, runtime polling, and client-side composition are inherently new agent-native designs. [[sources/salesforce--business-api-design#composite]], [[sources/salesforce--business-api-design#query-jobs]]

### Contract inventory

| Area | Observed documented contract | Design consequence |
| --- | --- | --- |
| Composition | POST `/services/data/vXX.X/composite`, reference IDs connect later subrequests to earlier outputs | Declarative composition can reduce round trips without one endpoint per workflow. |
| Authority | All composite subrequests execute as the same user | One envelope does not create new permission authority for a child operation. |
| Failure | Per-subrequest bodies and HTTP statuses; configurable rollback behavior | Envelope success is insufficient to infer every child succeeded. |
| Durable query | POST `/services/data/vXX.X/jobs/query`; GET job; GET results; PATCH abort; DELETE job | Read-only business intent can have an explicitly created runtime resource. |
| State | `UploadComplete`, `InProgress`, `Aborted`, `JobComplete`, `Failed` for query jobs | A returned job ID is not a returned dataset. |
| Result contract | CSV, opaque `Sforce-Locator`, `maxRecords`, same API version as creation | Pagination and version provenance are execution state. |

These are documented in [[sources/salesforce--business-api-design#composite]], [[sources/salesforce--business-api-design#create-job]], [[sources/salesforce--business-api-design#query-jobs]], [[sources/salesforce--business-api-design#results]].

### Limits that matter to agents

Composite supports at most 25 subrequests in the captured page, with up to five sObject Collection/query operations, and excludes binary resource types. Those are dated vendor limits, not general architecture constants. [[sources/salesforce--business-api-design#composite]]

Bulk SOQL has its own unsupported constructs; ORDER BY or LIMIT can disable PK chunking. This makes a single generic query tool potentially misleading if it hides which execution API it targets. The adapter should state the dialect and execution limits rather than make the model discover them by repeated failure. [[sources/salesforce--business-api-design#query-jobs]], [[sources/salesforce--business-api-design#create-job]]

Results require `JobComplete` on the captured results endpoint; the locator is opaque and must not be guessed. The API version used to retrieve results must match the creation version or the documented response is 409. [[sources/salesforce--business-api-design#results]]

## Patterns demonstrated

- Candidate **explicit business intent plus execution lifecycle**: retained resources, action semantics and/or result state appear in the contracts above. No confirmed pattern added from documentation comparison alone; runnable implementation evidence remains a separate bar. [[sources/salesforce--business-api-design#root]]

## What we'd steal

- ★ Offer deliberate bounded composition with named references and explicit rollback semantics. [[sources/salesforce--business-api-design#composite]]
- ★ Keep caller identity consistent across composed steps and inspect every child outcome. [[sources/salesforce--business-api-design#composite]]
- ★ Treat expensive queries as durable jobs rather than pretending every read is immediate. [[sources/salesforce--business-api-design#query-jobs]]
- Separate aborting execution from deleting its retained job data. [[sources/salesforce--business-api-design#query-jobs]]
- Preserve API version, query ID, result format and opaque continuation locator. [[sources/salesforce--business-api-design#results]]
- Bound output size with maxRecords and expose data through result references. [[sources/salesforce--business-api-design#results]]
- Document execution-specific query dialect restrictions and optimization pitfalls. [[sources/salesforce--business-api-design#create-job]]
- Do not hard-code captured vendor limits as universal interface principles. [[sources/salesforce--business-api-design#composite]]

## Tensions and anti-patterns

- Documented conventions and samples can hide exceptions, configuration differences, or incomplete examples; they require current contract review before implementation. [[sources/salesforce--business-api-design#root]]
- Familiar HTTP syntax does not establish correct tenant, permission, business milestone, or recovery behavior. Our inference from the scoped contracts above, not a measured model-performance claim.
- This evidence does not establish that agents were trained on this API or perform well on it.

## Open questions and verification record

- How do these contracts behave under real concurrent edits, duplicate delivery, worker failures, or permission changes? Not runtime-tested in this pass.
- Which smaller capabilities deserve agent-facing wrappers for the target business domain? Requires task/permission evidence.
- Source anchors and links are mechanically checked during batch integration; live provider behavior remains unverified.
