---
domain: artifacts
subdomain: projects
type: project
name: Context7
creator: "[[creators/upstash]]"
source: "[[sources/frontier-docs--platforms-20261105]]"
ecosystem: documentation-and-agent-tools
status: source-investigated
last-reviewed: 2026-11-05
---

# Context7

## Attributes

The unit studied is Context7's documentation retrieval API and its documented MCP mapping, through three first-party living pages captured on 2026-11-05. The capture pins bytes rather than a deployed server revision. This is a documentation contract study: no code installation, credentials, API requests, MCP calls or output-quality experiment. No adoption count was collected. [[sources/frontier-docs--platforms-20261105#context7-api-guide]]

## Relationships

Creator: [[creators/upstash]]. This complements [[artifacts/projects/mintlify]] by studying cross-library evidence retrieval instead of one publisher's documentation site. Owning comparison: [[concepts/developer-documentation-design]].

## Mechanism and themes

Context7 exposes a convenient v3 search and an explicit v2 source-selection flow. The first routes a question to relevant libraries; the second lets the caller resolve a library ID and retrieve context from that source. The documented MCP pair currently maps to v2, so REST breadth does not establish MCP tool parity. [[sources/frontier-docs--platforms-20261105#context7-api-guide]]

Search returns bounded evidence, not a promised finished implementation. JSON retains library identity, source links, code/info classes and a shared rank. Direct page fetching supports question-focused sections or offset-based reading. Open-web text is explicitly untrusted; checks may be unavailable, and source policies can reject arbitrary fetching. A reported screening pass does not authorize following instructions in the content. [[sources/frontier-docs--platforms-20261105#context7-search-api]]

The operation schema distinguishes partial search failure from unavailable requested-version evidence. JSON records requested and served versions per library; success can return fallback documentation. An unindexed public-GitHub version request can also queue background indexing. Thus a retrieval-shaped GET has documented worker effects; HTTP method alone is an incomplete effect description. [[sources/frontier-docs--platforms-20261105#context7-search-contract]]

## Patterns demonstrated

- [[patterns/composition/resolver-routing-table]] — explicit selection coexists with automatic task routing. [[sources/frontier-docs--platforms-20261105#context7-api-guide]]
- [[patterns/quality-bar/revision-bound-review]] — served-version evidence limits what a successful response proves. [[sources/frontier-docs--platforms-20261105#context7-search-contract]]
- [[patterns/behavioral/context-is-not-authority]] — retrieved web text remains untrusted regardless of format. [[sources/frontier-docs--platforms-20261105#context7-search-api]]

## What we'd steal

- ★ Offer task retrieval and explicit source selection together; use the latter when source identity matters. Do not infer that the two surfaces expose identical features. [[sources/frontier-docs--platforms-20261105#context7-api-guide]]
- ★ Return requested/served versions and partial-result reasons as data; allow callers to reject mismatched evidence. Operational partial status is not a relevance score. [[sources/frontier-docs--platforms-20261105#context7-search-contract]]
- Preserve provenance and rank across result classes so an agent can inspect sources and reconstruct ordering. Retrieval quality remains unmeasured. [[sources/frontier-docs--platforms-20261105#context7-search-api]]
- Provide bounded fetch and continuation rather than silently truncating an entire page. Treat external text as data and preserve unavailable-check status. [[sources/frontier-docs--platforms-20261105#context7-search-api]]
- Document background indexing effects beside retrieval contracts; expose an operational lifecycle before relying on eventual availability. This study did not inspect indexing completion APIs. [[sources/frontier-docs--platforms-20261105#context7-search-contract]]
- Distinguish empty evidence from transient search failure and publish retry/rate-limit behavior. Caching also needs version and authorization awareness in our adaptation. [[sources/frontier-docs--platforms-20261105#context7-api-guide]]

## Tensions and anti-patterns

The guide's blanket key requirement has a keyless-testing exception on Search. Guide prose requires a library hint with version; the operation schema describes some no-hint single-product cases. Preserve the discrepancy rather than promising identical behavior. Capture preambles advertise anonymous GET feedback writes; those were read as evidence and never invoked. [[sources/frontier-docs--platforms-20261105#context7-api-guide]] [[sources/frontier-docs--platforms-20261105#context7-search-api]] [[sources/frontier-docs--platforms-20261105#context7-search-contract]]

## Open questions and verification record

Do exact-version fallback and policy restrictions behave as documented? What exposes indexing progress, failure and cancellation? Does a source change invalidate cached snippets? These require controlled runtime evaluation. All three Markdown captures passed SHA-256/byte receipt validation; that verifies preservation, not semantic accuracy or integration success. [[sources/frontier-docs--platforms-20261105#root]]

## Agent documentation research connection

[[concepts/agent-documentation-interfaces]] owns the cross-system delivery, authority and evaluation comparison; this page owns the source-specific mechanisms.
