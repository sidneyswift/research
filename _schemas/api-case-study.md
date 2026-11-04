---
domain: _schemas
type: project-supplement
last-reviewed: 2026-11-04
---

# API case-study supplement

Use with [project.md](project.md) when studying an externally callable API system. Keep the project template's required sections and evidence boundaries. This supplement codifies the repeated nine-system comparison in [[analyses/frontier-and-business-api-design]], grounded in [[patterns/quality-bar/defect-derived-validation]] and [[patterns/composition/single-source-multi-surface-distribution]].

## Input and output

- **Input:** named API system, version/date, bounded primary documentation or implementation scope, research question.
- **Output:** one artifact page (or extension of an existing overlapping page), source citation collection, immutable evidence, indexes/backlinks, and logged verification. Shared synthesis links to the case study rather than maintaining a parallel vendor specification.
- **Evidence class:** distinguish documentation, implementation inspection, executed test, provider result, and inference. Docs alone do not prove execution durability, permission enforcement, or agent usability.

## Contract matrix

For each row, record the exact observed contract, a source anchor, its design implication, and unknowns. Say not studied when evidence is absent.

| Dimension | Inspect |
| --- | --- |
| Identity and scope | Tenant/company/project, immutable IDs, mutable names, request/run/result correlation |
| Intent and effects | Query, preview, mutation, approval, commit, external action; hidden effects in convenient names |
| Input semantics | Required/optional, omitted/null/empty/default, schema constraints and business validation |
| Execution ownership | Model output, app tool, SDK, provider job or managed runtime; who actually executes |
| Lifecycle | Acceptance, intermediate states, named terminal outcomes, results, partial failures, expiry/cancellation |
| Composition | Independent batch, dependent requests, workflow, transactional unit and commit exceptions |
| Authority | Authentication versus domain permissions, delegated actor, environment differences, custom-tool responsibility |
| Concurrency and retries | Version/eTag, request deduplication, unknown external outcome, worker/effect guarantees |
| Events | Verification, replay/order/duplicate behavior, subscription maintenance, resynchronization |
| Freshness and output | Cached/local/remote state, staged edits, projections, result size, paging and readiness |
| Evolution | API, SDK, model, resource and workflow versions; schema/event/enum compatibility |
| Agent discovery | Names, descriptions, grouping, loading/retrieval, examples; declared support versus negotiated set versus callable tools under current auth/page state; refresh/invalidation trigger; documented advice versus measured usability |

## Capture rules for documentation collections

Keep one sibling source citation page for the bounded collection, with a table of canonical URL → named immutable capture → version/retrieval → hash and a document/section anchor map. Capture each document separately; if extraction omitted important content, add a clearly labeled supplementary capture instead of editing the first. Record browser-rendered excerpts and omitted examples explicitly. Do not treat an HTML shell, search snippet, or navigation-only extraction as a complete article.

## Definition of done

- [ ] Dedup checked by subject, mechanism and role; project checklist satisfied.
- [ ] Contract matrix covers the investigated scope, with gaps marked.
- [ ] Every vendor claim resolves to a registered source anchor and supporting text.
- [ ] No inferred HTTP method, transaction, scheduler, authority, or business completion guarantee from a name, status object, or envelope 200 alone.
- [ ] Vendor documentation conflicts are recorded; standards and endpoint-specific behavior remain distinct.
- [ ] Immutable captures and hashes verified; supplements preserve earlier evidence.
- [ ] Exhaustive portable-idea ledger, counterexamples and open questions retained.
- [ ] Hub, domain/root indexes, creator and relevant existing entities updated; no new orphan.
- [ ] Scoped structural checks run and existing unrelated findings disclosed.
- [ ] Any cross-system analysis stays draft until [the synthesis review gate](../analyses/_eval-rubric.md) passes.

## Negotiation refinement — 2026-11-04

Grounded in [[artifacts/projects/shopify-api]] and [[patterns/composition/negotiated-capability-intersection]]: distinguish a caller’s declaration, server-selected compatible set, and actually callable operations under current authority/page state. Record refresh/invalidation behavior. A negotiation profile is not an action permission grant. [[sources/shopify--agent-commerce-api-design#profiles]], [[sources/shopify--agent-commerce-api-design#auth]], [[sources/shopify--agent-commerce-api-design#webmcp]]
