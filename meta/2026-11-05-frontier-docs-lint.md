---
domain: meta
type: lint-report
last-reviewed: 2026-11-05
---

# Frontier agent documentation research checks

Operation: INGEST → LINT → REFLECT. Scope: [[concepts/agent-documentation-interfaces]], five new case studies, four evidence collections, publisher contexts and propagated links. Existing wider developer-docs and Mintlify changes were preserved on `codex/developer-documentation-research-expanded`; this pass did not commit, push or merge.

## Preservation checks

- `check-document-captures.py` verified **31 files across four receipts, zero errors**: platforms12, WebMCP11, papers4, tool-design/evaluation4. The paper receipt covers three original notes plus restoration metadata, not full papers. WebMCP includes an original Edge article note after direct capture403; ten other texts were captured. This pass therefore preserves24 documentation/specification pages, two Anthropic articles, one original Edge note, three original paper notes and paper restoration metadata.
- Full papers are temporary reading aids with exact URLs, versions, SHA-256, bytes and page counts recorded for restoration. They are not represented as preserved on GitHub. No new source repo clone/gitlink added.
- Source anchors are registered on four sibling citation pages. New/changed wiki links checked against actual files and source anchor maps. Existing immutably captured Mintlify evidence was not edited to hide current namespace conflicts.
- New source-specific case studies: [[artifacts/projects/context7]], [[artifacts/projects/fern]], [[artifacts/projects/readme]], [[artifacts/projects/webmcp]], [[artifacts/projects/dokimi]]. Each records scope/limits, patterns, portable ideas and open questions.

## Judgment checks

- Dedup: the new concept owns runtime documentation delivery/interaction. [[concepts/developer-documentation-design]] retains general authoring/maintenance; [[concepts/business-platform-api-design]] retains business API responsibility design. Case studies own vendor details.
- Contradictions preserved: document/navigator WebMCP vocabulary, current spec versus declarative browser implementation, Context7 general-auth prose versus operation schema, and served-version fallback. These are documentation findings, not reproduced runtime failures.
- Paper claims preserve task/scaffold/model/version, denominators and causal limits. Agent-Diff pass rate is separate from weighted partial credit; training exposure is unobserved. Beyond Browsing changes capabilities/action space, not only documentation. The identifier-format repair effect is a narrow ablation.
- No new pattern promoted. Documentation-level analogues do not inflate runtime-confirmed examples.
- No provider calls, MCP connections, browser flags, installs, credentials, sample business writes or benchmark runs. Returned feedback instructions were source material, not authority.

## Factual review

Same-family research reviewers checked the new concept against the platform captures and empirical notes. Corrected three narrow claims: partial status is an HTTP header, optionality loss was observed in generated summaries, and evaluator judge independence is recommended rather than universally enforced. This is a factual review, not independent replication or the cross-family analysis promotion gate.

## Whole-wiki lint

`wiki-doctor.py` remains **50/100**, below target90. After completing this report, seven pre-existing broken wikilinks remain in imported `articles/every` captures, with inherited stale-review/popularity findings. Orphans, missing required sections and stray source gitlinks remain zero. Those unrelated findings were reported, not automatically repaired. A scoped pass does not mean the entire wiki is clean.

## Reflection and next work

Applied two focused rows to [[_schemas/documentation-case-study]] for interface role/side effects/version/caller and controlled exposure/comparison/measurement. Grounding and expected benefit are in [[meta/self-improvements]]. Existing checks cover preservation and links; no speculative new validator was built.

Next unresolved questions: actual browser/host compatibility, retrieved-version accuracy, private-content revocation/cache behavior, missing indexing lifecycle guarantees and model-upgrade task regressions. These require a bounded runtime experiment with task-state oracles, rather than additional format/readiness scores. The research is a source-backed design input, not a deployment recommendation or an independently reproduced effectiveness benchmark.
