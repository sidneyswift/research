---
domain: creators
type: org
name: model-context-protocol
last-reviewed: 2026-11-04
---

# Model Context Protocol project

> The protocol project and extension-maintainer community behind the MCP specification and official extension contracts.

## Attributes

- **Unit:** the MCP project/maintainers, rather than attributing all work to one company. Official extension repositories use the MCP organization and `ext-` prefix; extension maintainers and working/interest groups own their specifications. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-lifecycle]]
- **Evidence studied:** current core docs, extension governance and catalogs, Apps, authorization, Skills, Tasks and Server Cards. No ecosystem-wide usage or product acceptance measurement. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#root]]

## Artifacts produced

- [[artifacts/projects/mcp-apps]] — shared interactive UI protocol and SDK.
- [[concepts/model-context-protocol]] — protocol roles, primitives, transport and modern/legacy behavior.
- [[concepts/mcp-extension-architecture]] — governance, optional compatibility and discovery.
- [[concepts/mcp-enterprise-managed-authorization]] — official auth profiles and their enforcement limits.
- [[concepts/skills-over-mcp]] — service-delivered Agent Skills transport and integrity.

## Design philosophy (if discernible)

Keep servers focused and composable, with host-owned context and consent. Add optional capabilities without making every SDK implement every extension. Stabilization requires independent interoperability evidence and a conformance scenario. These are specified design/governance commitments, not assertions that every deployment realizes them. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#architecture]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#extension-lifecycle]]

## Timeline (append-only)

- 2026-11-04 — Ingested versioned core and extension evidence; kept current requirements, older compatibility paths, vendor additions and documentation conflicts separate. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#root]]

## Source citations

- [[sources/modelcontextprotocol--mcp-core-and-extensions-docs]], [[sources/modelcontextprotocol--mcp-apps-docs]], [[sources/modelcontextprotocol--mcp-authorization-docs]].
- [[creators/openai]] — vendor extensions at [[artifacts/projects/openai-mcp-extensions]], distinct from the official catalog.
- [[creators/anthropic]] — separately cataloged skills, plugins and model/runtime APIs; this page does not rewrite historical attribution.
