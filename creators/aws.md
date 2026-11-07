---
domain: creators
type: org
name: Amazon Web Services
url: https://aws.amazon.com/builders-library/
last-reviewed: 2026-11-04
---

# Amazon Web Services

> Publisher of primary API/architecture guidance studied in [[concepts/business-platform-api-design]].

## Attributes

- **Material studied:** official documentation/standards, not inspected runnable artifacts.
- **Distribution:** https://aws.amazon.com/builders-library/
- **Evidence boundary:** guidance establishes contracts and conventions, not correctness of a target implementation. [[sources/aws--idempotent-apis#retries]]

## Artifacts produced

No new runnable artifact was cataloged in this pass. Documentation and its takeaways are linked through [[concepts/business-platform-api-design]].

## Design philosophy

Caller intent, retry-safe effects, atomic request recording, and auditable request identifiers. [[sources/aws--idempotent-apis#retries]]

## Timeline

- 2026-11-04 — Captured API design evidence for [[concepts/business-platform-api-design]].

## Source citations

- [[sources/aws--idempotent-apis#retries]]

## Wider documentation study — 2026-11-05

[[concepts/developer-documentation-design]] extends the previous study using [[sources/docs-research--architecture-20261105#aws-adr]]. Captured guidance/contract only; no runtime or adoption result.
