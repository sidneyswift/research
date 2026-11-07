---
domain: artifacts
subdomain: projects
type: project
name: Fern
creator: "[[creators/fern]]"
source: "[[sources/frontier-docs--platforms-20261105]]"
ecosystem: documentation-and-agent-tools
status: source-investigated
last-reviewed: 2026-11-05
---

# Fern

## Attributes

The unit studied is Fern Docs' agent-facing delivery surfaces: hosted/self-hosted site MCP, scoped indexes, Markdown rendering, hosted custom skills and API catalog. Five first-party pages were captured on 2026-11-05; custom skill hosting is labeled beta. This pins published text, not a runtime release. No installation, client connection, credential exchange or task-success experiment occurred. No adoption metric was collected. [[sources/frontier-docs--platforms-20261105#root]]

## Relationships

Creator: [[creators/fern]]. Compare [[artifacts/projects/mintlify]] and [[artifacts/projects/readme]] through [[concepts/developer-documentation-design]]. Fern's site retrieval server differs from its organization-management server and API-execution generator. [[sources/frontier-docs--platforms-20261105#fern-mcp]]

## Mechanism and themes

Hosted site MCP exposes one semantic RAG answer tool. Self-hosted containers instead expose keyword `searchDocs` plus Markdown `fetchPage`, enforcing browser-equivalent caller access. Protected access uses JWTs; expiry requires token exchange again, without transport-level automatic refresh. Test traffic may skip analytics storage while still being answered. Disabling the server also removes its discovery and connection buttons. [[sources/frontier-docs--platforms-20261105#fern-mcp]]

Indexes exist at navigation nodes and preserve locale-specific links. Fern does not generate a full-site concatenation, citing its context/serving tradeoffs. Individual-page index URLs redirect to Markdown. This is one publisher's design choice, not evidence that every full export is harmful. [[sources/frontier-docs--platforms-20261105#fern-llms]]

Endpoint Markdown is a semantic rendering: request/response/auth property lists omit internal schema names and reference chains. Changelog output bounds recent entries, then points to a complete index. Redirects and useful missing-page suggestions support recovery. Markdown can exist for routable pages absent from navigation, so discovery omission is not access control. [[sources/frontier-docs--platforms-20261105#fern-markdown]]

Skills are separately published instruction bundles with discovery manifests. Current and legacy discovery layouts coexist; the current layout uses typed single-file/archive artifacts and digests. The API catalog separately connects human references to OpenAPI using standard Linkset relations and filters entries by viewer visibility. [[sources/frontier-docs--platforms-20261105#fern-skills]] [[sources/frontier-docs--platforms-20261105#fern-catalog]]

## Patterns demonstrated

- [[patterns/composition/single-source-multi-surface-distribution]] — shared content produces indexes and specialized Markdown. [[sources/frontier-docs--platforms-20261105#fern-markdown]]
- [[patterns/behavioral/context-is-not-authority]] — reading a skill bundle and obtaining API-execution authority are separate acts. [[sources/frontier-docs--platforms-20261105#fern-skills]]
- [[patterns/quality-bar/revision-bound-review]] — discovery-layout versions and deployment modes qualify interoperability claims. [[sources/frontier-docs--platforms-20261105#fern-skills]] [[sources/frontier-docs--platforms-20261105#fern-mcp]]

## What we'd steal

- ★ Name answer synthesis versus source retrieval explicitly, including deployment differences; evaluate them against different task oracles. [[sources/frontier-docs--platforms-20261105#fern-mcp]]
- Carry caller access through tool retrieval and document token expiry/recovery; treat analytics suppression as separate from execution. [[sources/frontier-docs--platforms-20261105#fern-mcp]]
- ★ Use scoped indexes, page descriptions and locale-preserving links for progressive reading. Preserve a default-language fallback policy rather than mixing locales invisibly. [[sources/frontier-docs--platforms-20261105#fern-llms]]
- Render endpoint semantics, interactive examples and auth into readable text; disclose omitted schema internals and keep a complete specification reachable. [[sources/frontier-docs--platforms-20261105#fern-markdown]]
- Preserve redirect extensions, missing-page suggestions and bounded changelog continuation. Test these as interfaces, not decorative conveniences. [[sources/frontier-docs--platforms-20261105#fern-markdown]]
- Publish typed, digest-bound skill artifacts with supporting files and validation. Integrity identifies bytes; it does not establish instruction safety or installation permission. [[sources/frontier-docs--platforms-20261105#fern-skills]]
- Advertise a catalog linking human reference and machine schema while avoiding unauthenticated inventory leakage. Verify downstream spec protection separately. [[sources/frontier-docs--platforms-20261105#fern-catalog]]

## Tensions and anti-patterns

Do not conflate hosted synthesis with self-hosted keyword search or either with API execution. Do not treat omitted navigation entries as protected resources or Markdown availability as meaning preservation. Skill discovery claims here come from Fern; the underlying discovery standard and installer were not independently inspected. [[sources/frontier-docs--platforms-20261105#fern-mcp]] [[sources/frontier-docs--platforms-20261105#fern-markdown]] [[sources/frontier-docs--platforms-20261105#fern-skills]]

## Open questions and verification record

Evaluate schema-flattening fidelity, deployment-mode retrieval differences and revocation/cache behavior. All five captures passed receipt checks; linked images were not preserved or visually analyzed. No answer accuracy, citation correctness, token-reduction magnitude or business outcome was independently demonstrated. [[sources/frontier-docs--platforms-20261105#root]]

## Agent documentation research connection

[[concepts/agent-documentation-interfaces]] owns the cross-system delivery, authority and evaluation comparison; this page owns the source-specific mechanisms.
