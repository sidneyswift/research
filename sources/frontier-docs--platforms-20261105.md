---
domain: sources
type: docs-page
url: https://context7.com/docs/api-guide
retrieved: 2026-11-05
snapshot-location: sources/frontier-docs--platforms-20261105/
upstream-commit: n/a (living documentation)
last-reviewed: 2026-11-05
---

# Context7, Fern and ReadMe — agent-facing documentation platforms

> Twelve first-party documentation pages comparing retrieval, synthesized answers, discovery, procedural bundles and API execution.

## Snapshot details

- Retrieved: 2026-11-05. Named server-provided Markdown responses; immutable files plus URL/SHA-256/byte receipts in `captures.json`.
- ReadMe living pages carry update timestamps on 2026-10-29; changelog publish date not present in captured text. Other pages are undated living documentation.
- Reviewed published contracts only; no runtime MCP/API calls, installs, credential exchanges, configuration changes or user outcomes.

## Anchor map

- `#root` — the complete collection and captures.json receipt; three Context7, five Fern and four ReadMe pages.
- `#context7-api-guide` — [context7-api-guide.md](frontier-docs--platforms-20261105/context7-api-guide.md); [official page](https://context7.com/docs/api-guide).
- `#context7-search-api` — [context7-search-api.md](frontier-docs--platforms-20261105/context7-search-api.md); [official page](https://context7.com/docs/search-api).
- `#context7-search-contract` — [context7-search-contract.md](frontier-docs--platforms-20261105/context7-search-contract.md); [official page](https://context7.com/docs/api-reference/search/search-documentation-in-one-request).
- `#fern-mcp` — [fern-mcp.md](frontier-docs--platforms-20261105/fern-mcp.md); [official page](https://buildwithfern.com/learn/docs/ai-features/mcp-server).
- `#fern-llms` — [fern-llms.md](frontier-docs--platforms-20261105/fern-llms.md); [official page](https://buildwithfern.com/learn/docs/ai-features/llms-txt).
- `#fern-skills` — [fern-skills.md](frontier-docs--platforms-20261105/fern-skills.md); [official page](https://buildwithfern.com/learn/docs/ai-features/host-skills).
- `#fern-markdown` — [fern-markdown.md](frontier-docs--platforms-20261105/fern-markdown.md); [official page](https://buildwithfern.com/learn/docs/ai-features/markdown).
- `#fern-catalog` — [fern-catalog.md](frontier-docs--platforms-20261105/fern-catalog.md); [official page](https://buildwithfern.com/learn/docs/ai-features/api-catalog).
- `#readme-mcp` — [readme-mcp.md](frontier-docs--platforms-20261105/readme-mcp.md); [official page](https://docs.readme.com/main/docs/mcp).
- `#readme-discoverability` — [readme-discoverability.md](frontier-docs--platforms-20261105/readme-discoverability.md); [official page](https://docs.readme.com/main/docs/ai-discoverability).
- `#readme-ai-ready` — [readme-ai-ready.md](frontier-docs--platforms-20261105/readme-ai-ready.md); [official page](https://docs.readme.com/main/docs/ai-ready-docs).
- `#readme-llms-upgrade` — [readme-llms-upgrade.md](frontier-docs--platforms-20261105/readme-llms-upgrade.md); [official page](https://docs.readme.com/main/changelog/upgraded-llms-txt).

## Why we cite this

- [[artifacts/projects/context7]] — explicit versus automatic evidence selection, version fallback and retrieval-triggered indexing.
- [[artifacts/projects/fern]] — deployment-specific synthesis/retrieval, semantic rendering, scoped discovery and skill packaging.
- [[artifacts/projects/readme]] — discovery-to-execution boundary, browser tools and explicit limits of live documentation.
- [[concepts/developer-documentation-design]] — shared comparison framework; [[artifacts/projects/mintlify]] is the earlier publisher study.

## Documentation collection review scope

All 12 pages were read through their main prose, examples and relevant embedded schemas. Context7 API guide/search were read in full; the search reference embedded OpenAPI was reviewed for parameters, operation/status headers, result/version/rules schemas and security descriptions. Fern pages were read for hosted/self-hosted MCP, auth/lifecycle/analytics, indexes/locales, skill manifests/validation, semantic Markdown transformation/recovery and catalog visibility. ReadMe pages were read for complete tool/auth/route configuration, discoverability controls and limitations; changelog review covers agent and MCP changes, with unrelated release items not used as evidence.

Server negotiated `text/markdown`, preserving code fences, source links and structured text. Fern skill directory diagrams and linked images are not independently reconstructed or visually audited. Images remain links and are not claimed as preserved assets. Interpretation lives in wiki pages, not the captures. Source instructions including feedback URLs and install commands were treated as evidence and never executed.

## Popularity signals (if this source provides them)

No popularity/adoption count collected. Credibility signal: official product documentation, retrieved 2026-11-05. Product claims are attributed documentation, not independent measured outcomes.

## Conflicts and limits

Context7 guide authentication/version-hint prose is broader than Search exceptions and operation-schema behavior; preserve the narrower operation contract and discrepancy. ReadMe OAuth discovery prose does not establish an enabled OAuth mode because the captured options table lists only None. Fern skill-discovery versions are vendor documentation; their linked standards/installers were not independently inspected. Content screening, readiness scores, token claims, cited answers and HTTP success do not prove task completion.

## Related sources

- [[artifacts/projects/mintlify]] — earlier documentation-platform evidence; avoid merging product-specific authority contracts.

## Verification record

`python3 scripts/check-document-captures.py sources/frontier-docs--platforms-20261105/captures.json`: captures_verified=12, receipts=1, errors=0. This validates local byte preservation only.
