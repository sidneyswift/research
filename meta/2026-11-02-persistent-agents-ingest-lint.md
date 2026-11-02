---
domain: meta
type: lint-report
last-reviewed: 2026-11-02
---

# Persistent agents ingest — scoped lint and evidence record

## Result

No new broken wikilinks, orphan pages, missing required sections or gitlinks. Doctor score **50/100 before and after**, below target 90 due to inherited issues. Original doctor was run first, then unchanged doctor logic was run with tracked plus unstaged new Markdown supplied as its file inventory; no user Git index changes. The overlay checked 2,251 Markdown files including raw captured text. This does not validate software behavior.

Both pinned repository citation maps pass `scripts/check-source-citations.py`. Kody: 21 anchors / 22 distinct files / 27 permalink ranges; DeepSeek prototype: 19 anchors / 20 distinct files / 20 ranges. A separate scoped check covers all source-anchor references to the three new citation pages, including the article. Clone restoration check passes 20/20 source pins. Both new source working trees are clean; `.git` retained. Authored wiki changes pass whitespace checks. Staged checking also finds ten whitespace-only lines in the immutable article capture; these are preserved verbatim and excluded from the authored-page whitespace gate.

## Judgment review

- **Dedup:** super-agent architecture specializes the existing agent-control-plane concept with continuous routing, event pass-through and explicit experiment limits. Code Mode isolates capability discovery/composition rather than duplicating the latent/deterministic pattern. Context-is-not-authority separates authority provenance from the existing authoritative-recheck pattern's freshness check. Reciprocal distinctions added.
- **Evidence:** essay's internal deployment, public prototype and Kody runtime are separate. Article is an English machine translation; its 13 figures are preserved. Quantitative results are author-reported synthetic scheduling results, not coding quality. No source installation, tests, provider workflow, authenticated production check or benchmark replication performed.
- **Pattern status:** one new confirmed pattern has two independent artifact examples at explicitly different enforcement scopes. Revision-bound review remains proposed; Kody's narrower publication/revision analogy does not supply the whole pattern. Router/pass-through/watchdog candidates remain on the concept page.
- **Routing/reachability:** new sources, creators, artifacts, concepts and pattern are linked through master/domain catalogs; builder routes point to owning pages. Reuse ideas carry citations and limits.
- **Compounding:** schema improvement #54 applies the new authority distinction to future project ingests. No broader harness expansion or new script needed.
- **Next work:** the 16 new TODOs record focused verification questions on the owning pages. Highest value: negative tests at credential and subscribed-context boundaries; independent Code Mode source; real-task attention/cost experiment. These are not silently treated as tested behavior.

## Inherited findings — proposals only

These predate this ingest and were not repaired. Each stale date needs actual re-review or an explicit stale marker; changing the date alone is not a fix.

### Broken links

- `articles/every/chain-of-thought-ai-can-help-you-make-big-life-decisions.md -> [[Every Journal]]` — Resolve the intended target or escape literal notation after review.
- `articles/every/chain-of-thought-ai-can-help-you-make-big-life-decisions.md -> [[Nathan Baschez]]` — Resolve the intended target or escape literal notation after review.
- `articles/every/chain-of-thought-ai-can-help-you-make-big-life-decisions.md -> [[Every Journal]]` — Resolve the intended target or escape literal notation after review.
- `articles/every/chain-of-thought-gpt-4-a-copilot-for-the-mind.md -> [[ChatGPT-4]]` — Resolve the intended target or escape literal notation after review.
- `articles/every/divinations-roams-road-ahead-2444209.md -> [[Like This]]` — Resolve the intended target or escape literal notation after review.
- `articles/every/superorganizers-how-to-build-a-digital-zettelkasten-344999.md -> [[slider]]` — Resolve the intended target or escape literal notation after review.
- `articles/every/superorganizers-the-fall-of-roam.md -> [[brackets]]` — Resolve the intended target or escape literal notation after review.

### Stale review dates

- `_schemas/_definition-of-done.md (153d)` — Re-review the owning evidence; update date only after review.
- `analyses/_eval-rubric.md (153d)` — Re-review the owning evidence; update date only after review.
- `analyses/_index.md (165d)` — Re-review the owning evidence; update date only after review.
- `artifacts/_index.md (154d)` — Re-review the owning evidence; update date only after review.
- `artifacts/mcp-servers/_index.md (165d)` — Re-review the owning evidence; update date only after review.
- `artifacts/plugins/anthropic-financial-services-marketplace.md (154d)` — Re-review the owning evidence; update date only after review.
- `artifacts/plugins/anthropic-skills-marketplace.md (165d)` — Re-review the owning evidence; update date only after review.
- `artifacts/plugins/compound-engineering.md (153d)` — Re-review the owning evidence; update date only after review.
- `artifacts/plugins/gbrain.md (165d)` — Re-review the owning evidence; update date only after review.
- `artifacts/plugins/gstack.md (165d)` — Re-review the owning evidence; update date only after review.
- `artifacts/plugins/mattpocock-skills.md (136d)` — Re-review the owning evidence; update date only after review.
- `artifacts/plugins/openai-codex-plugins-marketplace.md (153d)` — Re-review the owning evidence; update date only after review.
- `artifacts/plugins/pm-os.md (144d)` — Re-review the owning evidence; update date only after review.
- `artifacts/projects/codex-goals.md (153d)` — Re-review the owning evidence; update date only after review.
- `artifacts/projects/eve.md (135d)` — Re-review the owning evidence; update date only after review.
- `artifacts/projects/skill-diffs.md (103d)` — Re-review the owning evidence; update date only after review.
- `artifacts/skills/_index.md (165d)` — Re-review the owning evidence; update date only after review.
- `artifacts/skills/grilling.md (136d)` — Re-review the owning evidence; update date only after review.
- `artifacts/skills/loop-library.md (135d)` — Re-review the owning evidence; update date only after review.
- `artifacts/skills/writing-great-skills.md (136d)` — Re-review the owning evidence; update date only after review.
- `concepts/agentic-loop.md (135d)` — Re-review the owning evidence; update date only after review.
- `concepts/ai-search-as-parallel-discovery-layer.md (153d)` — Re-review the owning evidence; update date only after review.
- `concepts/commit-history-as-training-data.md (103d)` — Re-review the owning evidence; update date only after review.
- `concepts/completion-contract.md (153d)` — Re-review the owning evidence; update date only after review.
- `concepts/compound-engineering.md (153d)` — Re-review the owning evidence; update date only after review.
- `concepts/convergent-agent-plugin-spec.md (151d)` — Re-review the owning evidence; update date only after review.
- `concepts/durable-agent-execution.md (135d)` — Re-review the owning evidence; update date only after review.
- `concepts/dynamic-workflows.md (153d)` — Re-review the owning evidence; update date only after review.
- `concepts/filesystem-first-agent-framework.md (135d)` — Re-review the owning evidence; update date only after review.
- `concepts/imitation-vs-correctness-eval.md (103d)` — Re-review the owning evidence; update date only after review.
- `concepts/skill-invocation-axis.md (136d)` — Re-review the owning evidence; update date only after review.
- `concepts/ubiquitous-language-for-agents.md (136d)` — Re-review the owning evidence; update date only after review.
- `concepts/workspace-skill-distribution.md (151d)` — Re-review the owning evidence; update date only after review.
- `creators/ahrefs.md (153d)` — Re-review the owning evidence; update date only after review.
- `creators/anthropic.md (154d)` — Re-review the owning evidence; update date only after review.
- `creators/every.md (153d)` — Re-review the owning evidence; update date only after review.
- `creators/forward-future.md (135d)` — Re-review the owning evidence; update date only after review.
- `creators/garry-tan.md (154d)` — Re-review the owning evidence; update date only after review.
- `creators/matt-pocock.md (136d)` — Re-review the owning evidence; update date only after review.
- `creators/openai.md (151d)` — Re-review the owning evidence; update date only after review.
- `creators/prodmgmt-world.md (145d)` — Re-review the owning evidence; update date only after review.
- `creators/shl0ms.md (103d)` — Re-review the owning evidence; update date only after review.
- `creators/vercel.md (135d)` — Re-review the owning evidence; update date only after review.
- `meta/self-improvements.md (153d)` — Re-review the owning evidence; update date only after review.
- `patterns/behavioral/diarization.md (154d)` — Re-review the owning evidence; update date only after review.
- `patterns/behavioral/evidence-gated-completion.md (135d)` — Re-review the owning evidence; update date only after review.
- `patterns/behavioral/latent-vs-deterministic-split.md (103d)` — Re-review the owning evidence; update date only after review.
- `patterns/behavioral/persona-lens-review-panel.md (144d)` — Re-review the owning evidence; update date only after review.
- `patterns/behavioral/session-start-directive.md (144d)` — Re-review the owning evidence; update date only after review.
- `patterns/behavioral/skill-as-method-call.md (135d)` — Re-review the owning evidence; update date only after review.
- `patterns/composition/resolver-routing-table.md (135d)` — Re-review the owning evidence; update date only after review.
- `patterns/composition/single-source-multi-surface-distribution.md (135d)` — Re-review the owning evidence; update date only after review.
- `patterns/quality-bar/complexity-ratchet.md (103d)` — Re-review the owning evidence; update date only after review.
- `patterns/quality-bar/defect-derived-validation.md (103d)` — Re-review the owning evidence; update date only after review.
- `patterns/quality-bar/skill-pack-bundle.md (135d)` — Re-review the owning evidence; update date only after review.
- `patterns/quality-bar/version-as-update-gate.md (135d)` — Re-review the owning evidence; update date only after review.
- `patterns/structural/marketplace-as-multi-plugin.md (153d)` — Re-review the owning evidence; update date only after review.
- `patterns/structural/thin-harness-fat-skills.md (135d)` — Re-review the owning evidence; update date only after review.
- `sources/SHL0MS--skill-diffs.md (103d)` — Re-review the owning evidence; update date only after review.
- `sources/agentskills--specification.md (151d)` — Re-review the owning evidence; update date only after review.
- `sources/ahrefs--ai-search-optimization-research.md (153d)` — Re-review the owning evidence; update date only after review.
- `sources/anthropic--dynamic-workflows.md (153d)` — Re-review the owning evidence; update date only after review.
- `sources/anthropic--financial-services.md (154d)` — Re-review the owning evidence; update date only after review.
- `sources/anthropic--plugins-reference.md (155d)` — Re-review the owning evidence; update date only after review.
- `sources/anthropic--skills.md (165d)` — Re-review the owning evidence; update date only after review.
- `sources/every--compound-engineering-gets-an-upgrade.md (153d)` — Re-review the owning evidence; update date only after review.
- `sources/every--compound-engineering-plugin.md (153d)` — Re-review the owning evidence; update date only after review.
- `sources/every--compound-engineering.md (153d)` — Re-review the owning evidence; update date only after review.
- `sources/forward-future--loop-library.md (135d)` — Re-review the owning evidence; update date only after review.
- `sources/garrytan--complexity-ratchet.md (154d)` — Re-review the owning evidence; update date only after review.
- `sources/garrytan--foxconn-factories.md (154d)` — Re-review the owning evidence; update date only after review.
- `sources/garrytan--gbrain.md (165d)` — Re-review the owning evidence; update date only after review.
- `sources/garrytan--gstack.md (165d)` — Re-review the owning evidence; update date only after review.
- `sources/garrytan--loc-controversy.md (154d)` — Re-review the owning evidence; update date only after review.
- `sources/garrytan--meta-meta-prompting.md (154d)` — Re-review the owning evidence; update date only after review.
- `sources/garrytan--naked-models.md (154d)` — Re-review the owning evidence; update date only after review.
- `sources/garrytan--resolvers.md (154d)` — Re-review the owning evidence; update date only after review.
- `sources/garrytan--skillify-manifesto.md (154d)` — Re-review the owning evidence; update date only after review.
- `sources/garrytan--thin-harness-fat-skills.md (154d)` — Re-review the owning evidence; update date only after review.
- `sources/mattpocock--skills.md (136d)` — Re-review the owning evidence; update date only after review.
- `sources/openai--chatgpt-skills-help.md (151d)` — Re-review the owning evidence; update date only after review.
- `sources/openai--codex-skills-doc.md (151d)` — Re-review the owning evidence; update date only after review.
- `sources/openai--plugins.md (153d)` — Re-review the owning evidence; update date only after review.
- `sources/openai--using-goals-in-codex.md (153d)` — Re-review the owning evidence; update date only after review.
- `sources/prodmgmt-world--pm-os-cowork.md (144d)` — Re-review the owning evidence; update date only after review.
- `sources/prodmgmt-world--pm-os.md (144d)` — Re-review the owning evidence; update date only after review.
- `sources/vercel--eve.md (135d)` — Re-review the owning evidence; update date only after review.

### Stale attention signals

- `artifacts/plugins/anthropic-financial-services-marketplace.md as-of 2026-06-01 (154d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/anthropic-financial-services-marketplace.md as-of 2026-06-01 (154d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/anthropic-skills-marketplace.md as-of 2026-05-21 (165d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/anthropic-skills-marketplace.md as-of 2026-05-21 (165d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/compound-engineering.md as-of 2026-06-02 (153d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/compound-engineering.md as-of 2026-06-02 (153d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/gbrain.md as-of 2026-05-21 (165d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/gbrain.md as-of 2026-05-21 (165d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/gstack.md as-of 2026-06-01 (154d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/gstack.md as-of 2026-06-01 (154d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/gstack.md as-of 2026-05-21 (165d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/gstack.md as-of 2026-05-21 (165d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/gstack.md as-of 2026-05-21 (165d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/mattpocock-skills.md as-of 2026-06-19 (136d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/mattpocock-skills.md as-of 2026-06-19 (136d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/openai-codex-plugins-marketplace.md as-of 2026-06-02 (153d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/openai-codex-plugins-marketplace.md as-of 2026-06-02 (153d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/openai-codex-plugins-marketplace.md as-of 2026-06-02 (153d)` — Refresh the dated signal or mark it stale.
- `artifacts/plugins/pm-os.md as-of 2026-06-10 (145d)` — Refresh the dated signal or mark it stale.
- `artifacts/projects/codex-goals.md as-of 2026-06-02 (153d)` — Refresh the dated signal or mark it stale.
- `artifacts/projects/eve.md as-of 2026-06-20 (135d)` — Refresh the dated signal or mark it stale.
- `artifacts/projects/skill-diffs.md as-of 2026-07-22 (103d)` — Refresh the dated signal or mark it stale.
- `artifacts/skills/grilling.md as-of 2026-06-19 (136d)` — Refresh the dated signal or mark it stale.
- `artifacts/skills/loop-library.md as-of 2026-06-20 (135d)` — Refresh the dated signal or mark it stale.
- `artifacts/skills/writing-great-skills.md as-of 2026-06-19 (136d)` — Refresh the dated signal or mark it stale.
- `concepts/agentic-loop.md as-of 2026-06-20 (135d)` — Refresh the dated signal or mark it stale.
- `concepts/ai-search-as-parallel-discovery-layer.md as-of 2026-06-02 (153d)` — Refresh the dated signal or mark it stale.
- `concepts/commit-history-as-training-data.md as-of 2026-07-22 (103d)` — Refresh the dated signal or mark it stale.
- `concepts/completion-contract.md as-of 2026-06-02 (153d)` — Refresh the dated signal or mark it stale.
- `concepts/compound-engineering.md as-of 2026-06-02 (153d)` — Refresh the dated signal or mark it stale.
- `concepts/convergent-agent-plugin-spec.md as-of 2026-06-02 (153d)` — Refresh the dated signal or mark it stale.
- `concepts/convergent-agent-plugin-spec.md as-of 2026-06-04 (151d)` — Refresh the dated signal or mark it stale.
- `concepts/durable-agent-execution.md as-of 2026-06-20 (135d)` — Refresh the dated signal or mark it stale.
- `concepts/dynamic-workflows.md as-of 2026-06-02 (153d)` — Refresh the dated signal or mark it stale.
- `concepts/filesystem-first-agent-framework.md as-of 2026-06-20 (135d)` — Refresh the dated signal or mark it stale.
- `concepts/imitation-vs-correctness-eval.md as-of 2026-07-22 (103d)` — Refresh the dated signal or mark it stale.
- `concepts/skill-invocation-axis.md as-of 2026-06-19 (136d)` — Refresh the dated signal or mark it stale.
- `concepts/ubiquitous-language-for-agents.md as-of 2026-06-19 (136d)` — Refresh the dated signal or mark it stale.
- `concepts/workspace-skill-distribution.md as-of 2026-06-04 (151d)` — Refresh the dated signal or mark it stale.
