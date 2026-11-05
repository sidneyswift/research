---
domain: meta
type: lint-report
last-reviewed: 2026-11-05
---

# Developer documentation ingest checks

Scope: [[projects/writing-amazing-developer-docs/README]], [[concepts/developer-documentation-design]], authoring blueprints and their nine source collections, indexes and backlinks.

## Checks performed

- `python3 scripts/wiki-doctor.py --json`: score **50/100**. Zero orphans, missing required sections or stray source gitlinks. Seven broken-link occurrences remain in previously imported Every articles; these are outside this ingest. Older reviewed dates and popularity signals remain stale. Do not interpret the repository-wide score as a review of factual correctness.
- `python3 scripts/check-document-captures.py` against nine receipts: **41 files verified, zero errors**. These comprise 37 documentation captures, two paper metadata captures and two original paper-reading notes. The full papers are not reproduced in Git; their notes record version-pinned restoration URLs and hashes.
- Scoped comparison validates newly added wikilinks and registered source anchors, excluding inherited schema/example placeholders. This is link structure, not semantic proof.
- A second contributor reviewed product-example claims and proposed wording. Incorporated explicit success rather than arbitrary terminal-state completion, more practical writing guidance and a direct citation to newly captured Stripe versioning. This is not a cross-family analysis evaluation or a runtime test.
- Mutable Markdown whitespace checked separately from immutable source bytes.

## Findings and limits

- `articles/every/...`: seven inherited broken wikilink occurrences. Proposed fix: review imported article conventions before deciding whether to escape examples or create pages; no auto-fix applied.
- Older wiki `last-reviewed` and popularity signals: re-ingest/verify the relevant sources before refreshing dates. This pass's added backlinks do not revalidate prior content.
- No new orphans or missing required sections. No new confirmed pattern; docs-only recurrence does not meet the inspected-artifact bar.
- Product documentation inspected as text. No fresh-account provisioning, request execution, visual UI inspection or human/agent task experiment. Proposed blueprints remain proposed.
- Broad style-guide captures and language variants exceed the reviewed sections; citation pages state the actual reading scope.

## Reflect outcome

[[meta/self-improvements]] records an applied addition to [[_schemas/source]] for reviewed coverage and extraction limits. This is a grounded application of [[patterns/quality-bar/revision-bound-review]]; source snapshots themselves were not amended.
