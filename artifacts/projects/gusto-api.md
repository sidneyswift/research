---
domain: artifacts
subdomain: projects
type: project
name: gusto-api
creator: "[[creators/gusto]]"
source: "[[sources/gusto--business-api-design]]"
ecosystem: payroll
status: documentation-investigated
last-reviewed: 2026-11-04
---

# Gusto Embedded payroll API

> A business API whose payroll workflow separates retrieval, preparation, calculation preview and submission, while asynchronous status, version conflicts and scopes constrain what callers can safely infer or do.

## Attributes

- **Unit studied:** four distinct official documentation pages captured 2026-11-04, plus a supplementary full-body capture of the submit reference. The reference exposes a date-based API version header/default; this is evidence at retrieval, not a promise about all partner applications. [[sources/gusto--business-api-design#root]], [[sources/gusto--business-api-design#submit-full]]
- **Evidence class:** documentation inspected; no authentication, payroll calculations/submissions, employee data, payments, SDK installation or behavioral tests.
- **Credibility:** official Gusto Embedded documentation; no measured adoption or agent success claim. [[sources/gusto--business-api-design#root]]

## Relationships

- [[creators/gusto]] — publisher.
- [[projects/designing-apis-for-agents/README]] — research group.
- [[concepts/business-platform-api-design]] — business commands, concurrency and asynchronous completion.
- [[concepts/agent-control-plane]] — separate API access, workflow execution and business authority.

## Mechanism and themes

### The API follows business intent, not CRUD alone

The regular-payroll guide retrieves upcoming unprocessed payrolls, optionally prepares/updates employee compensation, calculates taxes/benefits/deductions, and submits. Calculation produces a preview of values for the payroll; it is asynchronous and returns `202`, after which the caller polls the payroll resource for `calculated_at` and details. This is explicit data retrieval plus stateful computation, not an immediate pure read. [[sources/gusto--business-api-design#workflow]]

Submission is a separately named `PUT /v1/companies/{company_id}/payrolls/{payroll_id}/submit` action. The reference says it calculates/runs an unprocessed payroll asynchronously, returns `202`, exposes blockers as `422`, and requires `payrolls:run`. Accepted submission is not proof of successful processing, and the inspected contract does not establish bank settlement or receipt by an employee. [[sources/gusto--business-api-design#submit-full]]

### Status is attached to the business resource

`processing_request` is returned through GET payroll and prepare. Its states distinguish `calculating`, `calculate_success`, `submitting`, `submit_success` and `processing_failed`, with structured errors. It may initially be null because work has not started, because it was never requested, or because prepare cleared the calculation. Therefore null is not sufficient evidence that no accepted work exists. The guide advises callers not to modify payroll through prepare/update/calculate/submit while calculation or submission is in progress. [[sources/gusto--business-api-design#processing]]

This supplies a concrete alternative to a universal `/operations/{id}` route: status can live on an identified business aggregate. The tradeoff is that callers must preserve which business phase was requested and distinguish resource state from execution state. That tradeoff is our interpretation of the documented structure. [[sources/gusto--business-api-design#processing]], [[sources/gusto--business-api-design#workflow]]

### Retries and concurrency have different mechanisms

Fundamentals distinguishes creation idempotency keys from object-version checks for updates. Updatable objects include a `version` based on their attributes and children; PUT with a stale version is rejected with `409 Conflict`. The same guide describes delta PUT updates: omitted fields are unchanged. Thus this API's PUT contract cannot be inferred from a generic HTTP tutorial that assumes full-resource replacement. An adapter must follow the actual provider contract while preserving its unusual semantics. [[sources/gusto--business-api-design#fundamentals]]

There is also a source tension: the fundamentals prose says PUT is not naturally idempotent, while RFC 9110 defines PUT among idempotent methods. We retain the useful operational version/retry rules but do not promote that generalization into a universal HTTP principle. Idempotency means repeated intended effect, not an identical response or immunity to concurrency. [[sources/gusto--business-api-design#fundamentals]], [[sources/ietf--http-semantics#safe-methods]]

### Permission contracts differ across environments and operations

The fundamentals guide documents resource/action scopes and states that demo scopes are not enforced by default; requests outside assigned scopes can succeed there but return `403` in production. The submit reference adds the concrete `payrolls:run` scope beyond the fundamentals' general read/write description. A successful demo is therefore weak evidence for production authorization, and an action's own reference is essential. [[sources/gusto--business-api-design#fundamentals]], [[sources/gusto--business-api-design#submit-full]]

Authority map: company/payroll IDs and input data identify the task; bearer token/scopes authorize API actions; the provider validates versions, blockers and workflow state; polling retrieves eventual processing outcome. User-facing approval, integration policy and bank settlement require their own evidence and cannot be inferred from token possession or `202`. [[sources/gusto--business-api-design#workflow]], [[sources/gusto--business-api-design#submit-full]], [[sources/gusto--business-api-design#processing]]

### Evolution policy belongs in the contract

The submit reference documents `X-Gusto-API-Version` and the application's minimum version when omitted. Fundamentals distinguishes free-text display content, which may change, from machine enum values, which require defensive handling of additions. It documents pagination headers, rate-limit metadata and `Retry-After`. These are machine-usable compatibility/recovery details, not model-training assumptions. [[sources/gusto--business-api-design#fundamentals]], [[sources/gusto--business-api-design#submit-full]]

## Patterns demonstrated

- [[patterns/behavioral/context-is-not-authority]] — payroll data, calculate-preview output and demo success do not supply production run authority. Scopes and workflow checks are separate. Documentation-level correspondence only. [[sources/gusto--business-api-design#fundamentals]], [[sources/gusto--business-api-design#submit-full]]
- Candidate: explicit preview/commit business phases plus observable asynchronous processing. No new confirmed pattern count asserted from documentation alone. [[sources/gusto--business-api-design#workflow]], [[sources/gusto--business-api-design#processing]]

## What we'd steal

- ★ **Expose high-consequence business phases by intent.** Prepare/calculate/submit are distinguishable so an agent can inspect a preview without being granted a run action. Calculation itself still updates processing state. [[sources/gusto--business-api-design#workflow]], [[sources/gusto--business-api-design#submit-full]]
- ★ **Treat acceptance, calculation, submission and settlement as separate facts.** Poll the documented processing state; seek additional settlement evidence when needed. The latter is our boundary, not a settlement contract in these docs. [[sources/gusto--business-api-design#processing]], [[sources/gusto--business-api-design#submit-full]]
- ★ **Use idempotency for request intent and versions for concurrent updates.** Keep keys stable only across retries of the same payload; reconcile a stale-version conflict before resubmission. [[sources/gusto--business-api-design#fundamentals]]
- **Publish terminal/nonterminal states with structured errors.** Include business phase in the status vocabulary and machine error fields. [[sources/gusto--business-api-design#processing]]
- **Document initial status ambiguity.** A null field can mean not yet started; retain accepted intent rather than automatically replaying a run. [[sources/gusto--business-api-design#processing]]
- **Make invalid concurrent transitions explicit.** Block or avoid modification during calculation/submission; a workflow adapter should account for these phases. [[sources/gusto--business-api-design#processing]]
- **Test production permission assumptions separately from demo success.** Inspect token scopes and the exact action reference. [[sources/gusto--business-api-design#fundamentals]], [[sources/gusto--business-api-design#submit-full]]
- **Separate display text from machine control.** Do not parse human error prose; tolerate unknown added enum values without silently treating them as success. [[sources/gusto--business-api-design#fundamentals]]
- **Preserve version defaults, pagination and rate metadata.** Pin intended API semantics and make traversal/backoff explicit in an agent adapter. [[sources/gusto--business-api-design#fundamentals]], [[sources/gusto--business-api-design#submit-full]]
- **Capture documentation contradictions instead of flattening them.** Provider-specific delta PUT and a general idempotency statement need distinct treatment against the HTTP standard. [[sources/gusto--business-api-design#fundamentals]], [[sources/ietf--http-semantics#safe-methods]]

## Tensions and anti-patterns

- The convenience name `prepare` obscures an important effect: preparing can clear prior calculation state. The workflow contract, not an intuitive verb alone, determines consequences. [[sources/gusto--business-api-design#processing]]
- Status attached to a payroll avoids a separate operation resource but can be ambiguous before asynchronous processing starts. [[sources/gusto--business-api-design#processing]]
- CRUD verbs and URL shape do not determine business effect: a PUT submit action can initiate high-consequence asynchronous work. [[sources/gusto--business-api-design#submit-full]]
- Demo permission permissiveness can conceal a production failure. A demo-only evaluation cannot establish tenant/permission correctness. [[sources/gusto--business-api-design#fundamentals]]

## Open questions and verification record

- Four documentation pages/five snapshots captured; first submit capture omitted introductory contract, so an immutable full-body supplement preserves it. Source links/anchors and hashes checked; no runtime calls.
- Unverified: payroll submission idempotency semantics specific to the submit endpoint, cancellation deadlines, funding/settlement lifecycle, webhook ordering and production enforcement in a real partner tenant.
- Which business approval/input revision should an agent bind to a calculated preview, and how should it react if any input changes before submission?
