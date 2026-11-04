---
domain: creators
type: org
name: Microsoft
url: https://learn.microsoft.com/azure/architecture/
last-reviewed: 2026-11-04
---

# Microsoft

> Publisher of primary API/architecture guidance studied in [[concepts/business-platform-api-design]].

## Attributes

- **Material studied:** official documentation/standards, not inspected runnable artifacts.
- **Distribution:** https://learn.microsoft.com/azure/architecture/
- **Evidence boundary:** guidance establishes contracts and conventions, not correctness of a target implementation. [[sources/microsoft--async-request-reply#lifecycle]], [[sources/microsoft--cqrs#separation]], [[sources/microsoft--domain-analysis#boundaries]], [[sources/microsoft--web-api-design#contracts]]

## Artifacts produced

No new runnable artifact was cataloged in this pass. Documentation and its takeaways are linked through [[concepts/business-platform-api-design]].

## Design philosophy

Business-capability boundaries and explicit architectural tradeoffs, including shared-store CQRS and asynchronous request-reply. [[sources/microsoft--async-request-reply#lifecycle]], [[sources/microsoft--cqrs#separation]], [[sources/microsoft--domain-analysis#boundaries]], [[sources/microsoft--web-api-design#contracts]]

## Timeline

- 2026-11-04 — Captured API design evidence for [[concepts/business-platform-api-design]].

## Source citations

- [[sources/microsoft--async-request-reply#lifecycle]]
- [[sources/microsoft--cqrs#separation]]
- [[sources/microsoft--domain-analysis#boundaries]]
- [[sources/microsoft--web-api-design#contracts]]

## API design research — 2026-11-04

- [[artifacts/projects/business-central-api]] — ERP contract study from [[sources/microsoft--business-central-api-design#root]], grouped in [[projects/designing-apis-for-agents/README]]. Documentation-level evidence; no live API verification.
