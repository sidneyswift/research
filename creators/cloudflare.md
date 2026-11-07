---
domain: creators
type: org
name: Cloudflare
url: https://developers.cloudflare.com/
last-reviewed: 2026-11-06
---

# Cloudflare

## Attributes

Publishes documented agent access surfaces and developer task examples. [[sources/cloudflare--docs-for-agents#root]]

## Artifacts produced

Documentation/research studied in [[concepts/developer-documentation-design]]. [[sources/cloudflare--docs-for-agents#root]]

- [[artifacts/skills/security-audit]] — security-review guidance plus a coverage-led full audit, independent candidate/record verification and two executable record validators. Source inspected; 65 bundled validator tests passed, not an end-to-end audit result. [[sources/cloudflare--security-audit-skill#root]] [[sources/cloudflare--security-audit-skill#test-execution]]

## Design philosophy

See the observed practices and limits in [[concepts/developer-documentation-design]] rather than inferring a broader philosophy from a small sample.

## Relationships

- [[projects/writing-amazing-developer-docs/README]] — documentation research collection.
- [[sources/cloudflare--docs-for-agents#root]] — primary evidence and review scope.

## Timeline

- 2026-11-05 — Added during the documentation research pass.

## Security-audit evidence — 2026-11-06

The released skill separates source-grounded claims from deployment unknowns and preserves evidence ownership across reviewers. It prescribes host sandboxing and safe artifact promotion rather than shipping those runtime mechanisms. These are observed choices in this artifact, not evidence that every Cloudflare system follows the same design. [[sources/cloudflare--security-audit-skill#execution-boundary]] [[sources/cloudflare--security-audit-skill#coverage-contract]]

- 2026-11-06 — Cataloged the skill at `c1c8a8c`; full source saved locally and validator tests executed. [[sources/cloudflare--security-audit-skill#root]] [[sources/cloudflare--security-audit-skill#test-execution]]
