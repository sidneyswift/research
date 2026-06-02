---
domain: patterns
type: index
last-reviewed: 2026-05-21
---

# Patterns

**The actual research output.** Recurring techniques observed across multiple artifacts. A pattern is only `confirmed` once ≥2 artifacts in this wiki demonstrate it with citations.

Each pattern uses [../_schemas/pattern.md](../_schemas/pattern.md). Sub-directories will be created as patterns accumulate — don't pre-stub them.

## Categories

- **structural/** — how artifacts are organized on disk (file layout, bundling, progressive disclosure, asset packaging)
- **behavioral/** — how artifacts steer the model (trigger phrasing, decision tables, refusal patterns, citation rituals)
- **composition/** — how artifacts call other artifacts (skill→skill, command→skill, agent→skill, MCP→skill)
- **quality-bar/** — what separates great from mediocre (testing artifacts, dogfood evidence, naming, versioning, deprecation hygiene)

## Confirmed patterns

*(First two confirmed 2026-06-01, when `anthropic-financial-services` supplied the 2nd grounded example for each.)*

- **composition/** [[patterns/composition/single-source-multi-surface-distribution]] — author the capability once, package it for multiple runtime surfaces that reference (not copy) the source. Examples: [[artifacts/plugins/anthropic-financial-services-marketplace]] (Cowork plugin + Managed Agents API), [[artifacts/plugins/gbrain]] (CLI + MCP + skillpack).
- **structural/** [[patterns/structural/marketplace-as-multi-plugin]] — one repo's `marketplace.json` registers N à-la-carte plugins. Examples: [[artifacts/plugins/anthropic-financial-services-marketplace]] (20), [[artifacts/plugins/anthropic-skills-marketplace]] (3). Counter: gstack/gbrain (one plugin, many internal skills).

## Proposed patterns

Hypotheses with one grounded example so far — tracked on the relevant artifact page until a 2nd example promotes them. Each gets a 1-line rationale.

- **trust-tiered subagent privilege separation** — prompt-injection containment by role (only the reader touches untrusted docs; exactly one leaf holds Write; a critic re-verifies). 1 example ([[artifacts/plugins/anthropic-financial-services-marketplace]]); *the standout idea to find again*.
- **structured-output-as-injection-defense** — bound a worker's only output channel to a length/character-class-restricted schema so injected text can't survive. 1 example (FSI `reader` `output_schema`).
- **single-source-of-truth skill vendoring + drift check** — author once, vendor copies into bundles, fail the build on drift. 1 example (FSI `sync-agent-skills.py` + `check.py`).
- **provenance-first data-source hierarchy** — skills hard-prefer audited MCP connectors over web search, and say why. 1 example (FSI `comps-analysis`).
- **version-as-update-gate** — patch-bump a changed plugin's `version` once per branch; `version` gates update delivery. 1 example (FSI pre-commit + Action).
- **audience-segmented skill output** — one skill, N audiences, N reference files, "if unspecified, ask." 1 example (FSI/S&P `tear-sheet`).
- *(carried from earlier ingests, tracked on plugin pages, still need a 2nd example):* persona-shaped command naming (gstack), philosophy-injection preamble (gstack ETHOS), frontmatter-extensions-beyond-spec (gstack + gbrain — likely confirmable on a dedicated pass), skill-router file `RESOLVER.md` (gbrain), agent-first install protocol `AGENTS.md` (gbrain), `llms.txt`+`llms-full.txt` dual files (gbrain).

## Suspected anti-patterns

Things we've seen creators do that we think *don't* work. These need the same rigor as patterns — ≥2 examples and a clear "why this fails."

- *(none yet)*
