---
domain: artifacts
subdomain: projects
type: project
name: ReadMe
creator: "[[creators/readme]]"
source: "[[sources/frontier-docs--platforms-20261105]]"
ecosystem: documentation-and-agent-tools
status: source-investigated
last-reviewed: 2026-11-05
---

# ReadMe

## Attributes

The unit studied is ReadMe's reader-facing agent documentation infrastructure, not its separate docs-authoring MCP. Four first-party pages were captured on 2026-11-05. Living pages report updates on 2026-10-29; the changelog capture lacks a publish-date field. Study evidence is published documentation, without installs, MCP/browser-tool calls, credentials or outcome tests. No adoption metric was collected. [[sources/frontier-docs--platforms-20261105#root]]

## Relationships

Creator: [[creators/readme]]. Compare [[artifacts/projects/mintlify]], [[artifacts/projects/fern]] and [[artifacts/projects/context7]] through [[concepts/developer-documentation-design]]. The useful distinction is which surfaces merely deliver evidence and which can perform business operations. [[sources/frontier-docs--platforms-20261105#readme-ai-ready]]

## Mechanism and themes

Project MCP includes endpoint/schema discovery, documentation retrieval and live `execute-request`. API credentials are forwarded separately from private-documentation credentials. All OpenAPI endpoints are documented as exposed by default, with route toggles; selecting a server index restricts execution targets. Branch/version selection is supported, but documentation-search tools are unavailable on branches. Custom tools contain title, description and instructions. These are materially different capabilities behind one MCP endpoint. [[sources/frontier-docs--platforms-20261105#readme-mcp]]

Agent discoverability includes negotiated Markdown, hierarchical indexes, graph links, API catalog, skill index and server card. ReadMe documents four WebMCP tools through `navigator.modelContext`, including trying an API endpoint. Training/search/prompt-context signals are advisory. The readiness grade samples pages and rewards enabled settings; this is not an execution benchmark. OAuth discovery explanation currently lists only a `None` setting, so the capture does not establish another functioning mode. [[sources/frontier-docs--platforms-20261105#readme-discoverability]]

ReadMe explicitly says publishing these surfaces cannot change model training or force a provider to fetch them. MCP content is shared across connected users; per-user business data scope comes from API authentication. This bounds inference-time evidence access separately from training-based familiarity. [[sources/frontier-docs--platforms-20261105#readme-ai-ready]]

The changelog describes recovery paths: nested/sidebar-shaped indexes, summarized roots, Markdown errors pointing back to indexes and redirects for guessed category URLs. Authentication/getting-started Markdown includes visible OpenAPI server/security context. Execution responses preserve statuses even for errors and empty successes. [[sources/frontier-docs--platforms-20261105#readme-llms-upgrade]]

## Patterns demonstrated

- [[patterns/behavioral/context-is-not-authority]] — documentation authentication and API execution credentials have different roles. [[sources/frontier-docs--platforms-20261105#readme-mcp]]
- [[patterns/composition/single-source-multi-surface-distribution]] — documentation produces indexes, Markdown and tool-facing reference. [[sources/frontier-docs--platforms-20261105#readme-discoverability]]
- [[patterns/composition/resolver-routing-table]] — scoped indexes and recovery links help route uncertain readers back into the documentation graph. [[sources/frontier-docs--platforms-20261105#readme-llms-upgrade]]

## What we'd steal

- ★ Distinguish schema inspection from API execution in tool inventories, auth documentation and user interfaces. Review effect-bearing route exposure before enabling a business API. [[sources/frontier-docs--platforms-20261105#readme-mcp]]
- Separate private-docs credentials, API data credentials, server restrictions and version selection. Each solves a different scope problem; branch search limitations must be explicit. [[sources/frontier-docs--platforms-20261105#readme-mcp]]
- Preserve child/sibling/curated-next links and hierarchical indexes in machine representations; let readers recover from guessed routes. [[sources/frontier-docs--platforms-20261105#readme-discoverability]] [[sources/frontier-docs--platforms-20261105#readme-llms-upgrade]]
- Keep custom-index ownership visible: replacing generation with repository content stops automatic updates. Enterprise defaults and project overrides need traceable scope. [[sources/frontier-docs--platforms-20261105#readme-discoverability]]
- Include server/security context in entry pages and retain HTTP status in execution results, including empty bodies. Test endpoint effects separately from response shape. [[sources/frontier-docs--platforms-20261105#readme-llms-upgrade]]
- ★ State what live docs cannot do: force retrieval, change training or independently provide per-user business-data authorization. Use these boundaries when planning agent adoption. [[sources/frontier-docs--platforms-20261105#readme-ai-ready]]
- Treat readiness settings, advisory content signals and actual successful tasks as distinct measurements. WebMCP's endpoint trial tool also needs effect-aware review. [[sources/frontier-docs--platforms-20261105#readme-discoverability]]

## Tensions and anti-patterns

A “documentation MCP” may execute real writes. Documentation tokens in URLs are secrets; the source explicitly warns about sharing them. Per-viewer personalization beyond project/password scoping is described as roadmap, not delivered protection. Vendor client setup examples are not independent proof of current host support. [[sources/frontier-docs--platforms-20261105#readme-mcp]]

## Open questions and verification record

What do runtime tool schemas declare about effects, retries and confirmations? Do route restrictions cover all execution paths? How does WebMCP preserve caller/session authority? These need further specification or controlled tests. Four immutable captures passed byte/hash validation. No task-success, safe-execution or browser-compatibility claim was independently exercised. [[sources/frontier-docs--platforms-20261105#root]]

## Agent documentation research connection

[[concepts/agent-documentation-interfaces]] owns the cross-system delivery, authority and evaluation comparison; this page owns the source-specific mechanisms.
