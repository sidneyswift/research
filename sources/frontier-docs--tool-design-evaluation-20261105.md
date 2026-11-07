---
domain: sources
type: docs-page
url: https://intel.github.io/dokimi/methodology/
retrieved: 2026-11-05
snapshot-location: sources/frontier-docs--tool-design-evaluation-20261105/
last-reviewed: 2026-11-05
---

# Agent documentation: tool design and comparative evaluation

## Snapshot details

Four primary textual captures: two Intel Dokimi living documentation pages and two Anthropic engineering/research articles. Named immutable captures and `captures.json` preserve bytes, SHA-256, URLs, final URLs and representation. HTML main/article was converted to Markdown; diagrams are referenced but not downloaded or visually audited. No source code, evaluator, Docker task, agent API, tool server or example was executed. No independent performance replication.

| Capture | Canonical URL | SHA-256 |
| --- | --- | --- |
| [dokimi-methodology.md](frontier-docs--tool-design-evaluation-20261105/dokimi-methodology.md) | https://intel.github.io/dokimi/methodology/ | `cb34014853649aa90458cfdfef5eca5674c2662377bd02d69f874c95c458a80f` |
| [dokimi-measurement.md](frontier-docs--tool-design-evaluation-20261105/dokimi-measurement.md) | https://intel.github.io/dokimi/what-it-measures/ | `5ef9387d6a7c1695788b37b234c26c03d7b7e18badcd8a10841ea0cd0d1afd02` |
| [anthropic-writing-tools.md](frontier-docs--tool-design-evaluation-20261105/anthropic-writing-tools.md) | https://www.anthropic.com/research/writing-tools-for-agents | `93e53847d533cfbf750a859717c88f2995f6ba99c5ca5be256de6cae5e9303cc` |
| [anthropic-advanced-tools.md](frontier-docs--tool-design-evaluation-20261105/anthropic-advanced-tools.md) | https://www.anthropic.com/engineering/advanced-tool-use | `00d40f7d73649200eea029e8aaaaa159b433fc060689c969143dcf25fe40290b` |

## Anchor map

- `#root` — collection, reviewed scope and evidence limits.
- `#dokimi-methodology` — dokimi-methodology.md: comparative conditions, model roles, question provenance, answer generation, grounded judging, trust gates and executable tasks reviewed. Long legacy question-schema normalization detail captured as context, not exhaustively implementation-audited.
- `#dokimi-measurement` — dokimi-measurement.md: context arms, selected versus forced skill exposure, novelty classifications, repository static/reach/budget and executable task modes reviewed.
- `#anthropic-writing-tools` — anthropic-writing-tools.md: 2025-09-11 article; evaluation tasks, held-out tests, namespaces, meaningful outputs, response size/errors and tool-description principles reviewed. Chart pixels were not measured; quantitative causal claims not independently replicated.
- `#anthropic-advanced-tools` — anthropic-advanced-tools.md: 2025-11-24 article; deferred search, programmatic calling, input examples, adoption tradeoffs and internal test figures reviewed. Examples are article-specific, not freshly verified API compatibility instructions.

## Why we cite this

Documentation is also names, descriptions, examples, errors and dynamically delivered runtime context. These sources distinguish discovery, orchestration, input guidance and controlled evaluation. Dokimi's documented evaluator design is useful methodology; publishing a framework does not prove any product's documentation improves task completion. Anthropic reports internal results without a complete public experimental dataset in these captured articles.

## Popularity signals

First-party provenance: Intel's published Dokimi documentation and Anthropic's own tool-design engineering reports. No adoption ranking, universal effect size or current model recommendation inferred.

## Related sources

- [[sources/mintlify--docs-url-discovery-bench]] — narrower URL-discovery endpoint measure.
- [[sources/frontier-docs--empirical-20261105]] — independent research with study-specific tasks and confounds.
- [[sources/frontier-docs--platforms-20261105]] — shipped retrieval and answer-generation contracts.
