---
domain: artifacts
subdomain: projects
type: project
name: stripe-api
creator: "[[creators/stripe]]"
source: "[[sources/stripe--business-api-design]]"
ecosystem: Payments / business operations
status: documentation-investigated
last-reviewed: 2026-11-04
---

# Stripe API

## Attributes

- **Unit:** externally callable business API system; sampled contracts, not the full product.
- **Evidence:** official documentation captured 2026-11-04; specific pages and hashes on [[sources/stripe--business-api-design#root]].
- **Verification:** documentation read, no implementation inspection or API execution; no credentials, production access, writes, or installations.
- **Credibility:** first-party docs, not popularity or measured agent usability.

## Relationships

- [[artifacts/projects/shopify-api]] — complementary commerce intent, checkout authority and agent-facing protocol study.

- **Publisher:** [[creators/stripe]].
- **Research group:** [[projects/designing-apis-for-agents/README]].
- **Foundation:** [[concepts/business-platform-api-design]].
- **Comparison:** [[analyses/frontier-and-business-api-design]].

## Mechanism and themes

Stripe models business intent as lifecycle-bearing resources rather than a single success/failure RPC. PaymentIntent and SetupIntent have different effects, and confirmation, required action, processing, and success are distinct stages. The captured docs also expose materially different idempotency, pagination, and list-consistency rules in the v1 and v2 namespaces. [[sources/stripe--business-api-design#intent]], [[sources/stripe--business-api-design#v2]]

### Contract inventory

| Area | Observed documented contract | Design consequence |
| --- | --- | --- |
| Business effect | PaymentIntent collects a payment; SetupIntent prepares payment credentials without a charge | Similar schemas/names do not imply equivalent authority or effects. |
| Lifecycle | Requires method/confirmation/action; processing; succeeded/canceled | User interaction and external settlement timing are business state, not HTTP latency. |
| v1 retries | Saved first response after execution begins, including 500s; parameter mismatch rejected; at least 24-hour retention before pruning | Retrying a request is scoped to an explicit policy, not a timeless guarantee. |
| v2 retries | Successful work not repeated; failed or partially failed work can be retried toward completion | One provider can evolve the meaning of its retry contract across surfaces. |
| Events | Signature verification; duplicates and unordered delivery; thin versus snapshot formats | Event handlers need authentication, deduplication, state reconciliation and schema policy. |
| Discovery | Official docs publish agent skills, Markdown, CLI/plugin guidance | Established business vendors are already adapting their discovery layer for agents. |

Rows supported by [[sources/stripe--business-api-design#intent]], [[sources/stripe--business-api-design#idempotency]], [[sources/stripe--business-api-design#v2]], [[sources/stripe--business-api-design#webhooks]], [[sources/stripe--business-api-design#skills]].

### Evolution within a provider

The v2 overview documents JSON requests/responses, token/page-URL pagination, eventually consistent lists by default, and different expansion/include behavior. Most existing endpoints remain in v1 in the captured overview. Avoid extrapolating v2 semantics to PaymentIntents or every Stripe operation. [[sources/stripe--business-api-design#v2]]

PaymentIntent success describes the documented payment flow, not a guarantee against a future refund/dispute or proof that a new platform's entire order workflow is complete. Cancellation has payment-method and time-window restrictions. Our integration should map the exact business milestone rather than translate every success into a global done flag. [[sources/stripe--business-api-design#intent]], [[sources/stripe--business-api-design#webhooks]]

The docs contain installation/setup instructions aimed at coding agents. We captured them as evidence of distribution design; we did not install the CLI, create a sandbox, obtain keys, or invoke a payment API. [[sources/stripe--business-api-design#skills]]

## Patterns demonstrated

- Candidate **explicit business intent plus execution lifecycle**: retained resources, action semantics and/or result state appear in the contracts above. No confirmed pattern added from documentation comparison alone; runnable implementation evidence remains a separate bar. [[sources/stripe--business-api-design#root]]

## What we'd steal

- ★ Model meaningful business intent and required follow-up states explicitly. [[sources/stripe--business-api-design#intent]]
- ★ Separate storing credentials from taking the financial action. [[sources/stripe--business-api-design#intent]]
- ★ Bind retry keys to intent and parameters with documented retention and replay behavior. [[sources/stripe--business-api-design#idempotency]]
- Review retry semantics per namespace/version instead of assuming one provider-wide rule. [[sources/stripe--business-api-design#v2]]
- Distinguish immediate point reads from eventually consistent lists. [[sources/stripe--business-api-design#v2]]
- Use opaque continuation/page URLs instead of inferred offsets. [[sources/stripe--business-api-design#v2]]
- Verify webhook signatures, deduplicate events and reconcile current state without assuming delivery order. [[sources/stripe--business-api-design#webhooks]]
- Separate thin event references from versioned snapshot payloads. [[sources/stripe--business-api-design#webhooks]]
- Publish versioned machine-readable documentation and discovery affordances alongside the stable API. [[sources/stripe--business-api-design#skills]]
- Expose cancellation limits and actions required from a human or external system. [[sources/stripe--business-api-design#intent]]

## Tensions and anti-patterns

- Documented conventions and samples can hide exceptions, configuration differences, or incomplete examples; they require current contract review before implementation. [[sources/stripe--business-api-design#root]]
- Familiar HTTP syntax does not establish correct tenant, permission, business milestone, or recovery behavior. Our inference from the scoped contracts above, not a measured model-performance claim.
- This evidence does not establish that agents were trained on this API or perform well on it.

## Open questions and verification record

- How do these contracts behave under real concurrent edits, duplicate delivery, worker failures, or permission changes? Not runtime-tested in this pass.
- Which smaller capabilities deserve agent-facing wrappers for the target business domain? Requires task/permission evidence.
- Source anchors and links are mechanically checked during batch integration; live provider behavior remains unverified.

## Documentation application — 2026-11-05

[[concepts/developer-documentation-design]] applies this research to documentation authoring, distribution or review. See [[projects/writing-amazing-developer-docs/README]] for the evidence map. This cross-reference adds no inspected runtime example or benchmark result.
