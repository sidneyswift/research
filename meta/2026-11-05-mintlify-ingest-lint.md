---
domain: meta
type: lint-report
last-reviewed: 2026-11-05
---

# Mintlify documentation ingest checks

Scope: [[artifacts/projects/mintlify]], three source citation pages, creator context, indexes/backlinks, documentation research integration and a static benchmark inventory.

## Checks and result

- `check-document-captures.py` verifies39files across two receipts:20current product docs/index pages,13article/report/library surfaces and six figures. Two benchmark figures visually reviewed; no full visual site audit.
- `check-source-citations.py` verifies the pinned benchmark map: seven registered anchors, eight referenced source files and eleven immutable line ranges; zero structural errors. Semantic claim review remains separate.
- `./setup.sh --check --only mintlify--docs-url-discovery-bench`:1/1ready at5f055a8. Clone is ignored, clean and retains .git; manifest pin is fetchable. No source applications/dependencies executed.
- Own static JSON/Git-tree inventory records result-file hashes, valid/error row counts and missing proxy-log/snapshot paths. This is not a vendor benchmark rerun or full result reproduction. [[sources/mintlify--docs-url-discovery-bench#inventory]]
- Added wikilink targets and source anchors checked. Mutable Markdown whitespace checked separately from immutable captures. No source gitlink or new orphan introduced.
- Research contributor reviewed benchmark/report/lifecycle statements. Product mechanisms read against source docs; no authenticated runtime or business-outcome verification.
- Wiki doctor remains50/100: seven inherited imported-article broken-link occurrences, stale review/popularity dates; zero orphans and missing required sections. No unrelated automatic fixes.

## Important remaining evidence limits

- Historical source publication dates and current docs may differ; old Index is marked discontinued and current partner-feed availability is contact-gated.
- Benchmark proxy logs claimed as committed are absent at the pin; snapshots are explicitly not bundled. Aggregate rows are preserved, full replay/decomposition inputs are not.
- Product auth/visibility/API filtering, generated skills, WebMCP and discovery-schema claims were not conformance/runtime tested.
- Requests, readiness, URL-path selection, PR acceptance and heuristic saved cost are not verified implementation or business outcomes.
- Embedded source installation/feedback instructions were treated as evidence, never executed. Reading/search permission did not authorize configuration or external submissions.

## Reflect

[[meta/self-improvements]] records an applied reproducibility-input addition to [[_schemas/documentation-case-study]]. Existing validation machinery was sufficient for this ingest; no new confirmed pattern or generic checker introduced.
