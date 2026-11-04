---
domain: creators
type: org
name: NVIDIA
url: https://github.com/NVIDIA
last-reviewed: 2026-11-04
---

# NVIDIA

> In this wiki: the publisher of Auto-Ontology and its companion text-to-SQL evaluation harness. This is a source-scoped project study, not a company profile.

## Attributes

- **Work studied:** a maintained semantic-context service, review UI, curated MCP adapter, setup/query/management skills, and evaluation tooling. [[sources/nvidia--auto-ontology#architecture]] [[sources/nvidia--auto-ontology-eval#root]]
- **Distribution:** public GitHub repositories under NVIDIA; application declares Apache-2.0. [[sources/nvidia--auto-ontology#license]]
- **Evidence boundary:** implementation/docs inspection and structural checks; no inferred deployment/adoption or independent benchmark result.

## Artifacts produced

### Projects

- [[artifacts/projects/auto-ontology]] — business terms, source bindings, reusable measures, query validation and review/publication boundaries.

### Sources

- [[sources/nvidia--auto-ontology]] — application at `caced11e…`.
- [[sources/nvidia--auto-ontology-eval]] — evaluator at `ec41b2c…`; same-team companion, not independent validation.

## Design philosophy (if discernible)

The studied project moves meaning into inspectable, reusable artifacts and keeps the agent-facing tool surface small. Its management skill demands explicit measure/relationship contracts and exact publication readback. The evaluator separates run health from model scores and reports both fixed and broken questions. These are project-specific design choices, not claims about every NVIDIA product. [[sources/nvidia--auto-ontology#measure-contracts]] [[sources/nvidia--auto-ontology#curated-tools]] [[sources/nvidia--auto-ontology-eval#health-gate]] [[sources/nvidia--auto-ontology-eval#flips]]

## Timeline (append-only)

- 2026-11-04 — Auto-Ontology and its evaluation companion ingested with pinned source evidence, 26 portable principles and explicit implementation-versus-guidance limits. [[sources/nvidia--auto-ontology]] [[sources/nvidia--auto-ontology-eval]]

## Source citations

- [[sources/nvidia--auto-ontology#root]] — product intent.
- [[sources/nvidia--auto-ontology-eval#root]] — evaluation design.
