---
domain: patterns
type: index
last-reviewed: 2026-06-01
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

*(First two confirmed 2026-06-01 via `anthropic-financial-services`; three more confirmed 2026-06-01 when Garry Tan's 8-essay "AI Explainer" series supplied a 2nd grounded artifact — gstack **and** gbrain — for each. Same-creator caveat tracked on each page.)*

- **composition/** [[patterns/composition/single-source-multi-surface-distribution]] — author the capability once, package it for multiple runtime surfaces that reference (not copy) the source. Examples: [[artifacts/plugins/anthropic-financial-services-marketplace]] (Cowork plugin + Managed Agents API), [[artifacts/plugins/gbrain]] (CLI + MCP + skillpack).
- **structural/** [[patterns/structural/marketplace-as-multi-plugin]] — one repo's `marketplace.json` registers N à-la-carte plugins. Examples: [[artifacts/plugins/anthropic-financial-services-marketplace]] (20), [[artifacts/plugins/anthropic-skills-marketplace]] (3). Counter: gstack/gbrain (one plugin, many internal skills).
- **quality-bar/** [[patterns/quality-bar/skill-pack-bundle]] — a skill ships as a *tested bundle* (markdown skill + thin code + unit/LLM/integration/resolver tests; the 10-step "skillify" checklist). Examples: [[artifacts/plugins/gstack]] (7 parts as real files) + [[artifacts/plugins/gbrain]] (`gbrain doctor` enforces all 10 steps). **Promoted from proposed** 2026-06-01. ⚠ both same-creator (Garry Tan).
- **composition/** [[patterns/composition/resolver-routing-table]] — a routing table mapping intent/content-type→which skill or doc to load; tested with trigger evals, audited with `check-resolvable`, fractal across layers (skill / filing / context-inside-a-skill). Examples: [[artifacts/plugins/gbrain]] (`skills/RESOLVER.md` + 14+ `routing-eval.jsonl` + `check-resolvable.ts`) + [[artifacts/plugins/gstack]] (`scripts/resolvers/` + resolver evals). **Supersedes** the old proposed "skill-router file `RESOLVER.md`" bullet. ⚠ same-creator.
- **behavioral/** [[patterns/behavioral/latent-vs-deterministic-split]] — every step is latent (model judgment) or deterministic (same-in/same-out); put each on the correct side. Examples: [[artifacts/plugins/gstack]] (deterministic `browse/` Playwright CLI + `bin/` vs latent markdown skills) + [[artifacts/plugins/gbrain]] ("zero-LLM" typed-link graph vs latent search/synthesis). ⚠ same-creator; "latent" is the essays' label, not repo vocabulary.

## Proposed patterns

Hypotheses with one grounded example so far — tracked on the relevant artifact page until a 2nd example promotes them. Each gets a 1-line rationale.

*(With a dedicated page — from the AI-Explainer series, 2026-06-01. Each is grounded in 1 in-wiki artifact so far; promotion needs a 2nd, ideally non-Garry.)*

- **structural/** [[patterns/structural/thin-harness-fat-skills]] — push intelligence up into markdown skills (~90% of value), execution down into deterministic code, keep the harness thin. Fat-skills side grounded in [[artifacts/plugins/gstack]]/[[artifacts/plugins/gbrain]]; the thin *harness* (OpenClaw/Hermes) isn't ingested — a possible missing "harnesses" axis.
- **behavioral/** [[patterns/behavioral/skill-as-method-call]] — a skill file is a parameterized procedure (TARGET/QUESTION/DATASET); same file, different invocation → different capability. Grounded in [[artifacts/plugins/gstack]] (`/qa` tiers, `/investigate`); needs a skill with an explicit documented parameter signature.
- **behavioral/** [[patterns/behavioral/diarization]] — read everything about a subject, write one structured page of distilled judgment (the "says vs actually building" gap, who-holds-the-belief). Grounded in [[artifacts/plugins/gbrain]] (`enrich/`, brain-page schema, entity propagation).
- **quality-bar/** [[patterns/quality-bar/complexity-ratchet]] — every session adds tests+docs+evals that reload into the next session's context, so the quality floor only rises (forward-only); 90% coverage as the threshold AI made affordable. Grounded in [[artifacts/plugins/gstack]] (TTY review-floor tests) + [[artifacts/plugins/gbrain]] (extraction ratchet); the system-level sibling of `skill-pack-bundle`.

*(Other proposed — one example so far, tracked on artifact pages:)*

- **trust-tiered subagent privilege separation** — prompt-injection containment by role (only the reader touches untrusted docs; exactly one leaf holds Write; a critic re-verifies). 1 example ([[artifacts/plugins/anthropic-financial-services-marketplace]]); *the standout idea to find again*.
- **structured-output-as-injection-defense** — bound a worker's only output channel to a length/character-class-restricted schema so injected text can't survive. 1 example (FSI `reader` `output_schema`).
- **single-source-of-truth skill vendoring + drift check** — author once, vendor copies into bundles, fail the build on drift. 1 example (FSI `sync-agent-skills.py` + `check.py`).
- **provenance-first data-source hierarchy** — skills hard-prefer audited MCP connectors over web search, and say why. 1 example (FSI `comps-analysis`).
- **version-as-update-gate** — patch-bump a changed plugin's `version` once per branch; `version` gates update delivery. 1 example (FSI pre-commit + Action).
- **audience-segmented skill output** — one skill, N audiences, N reference files, "if unspecified, ask." 1 example (FSI/S&P `tear-sheet`).
- *(carried from earlier ingests, tracked on plugin pages, still need a 2nd example):* persona-shaped command naming (gstack), philosophy-injection preamble (gstack ETHOS), frontmatter-extensions-beyond-spec (gstack + gbrain — likely confirmable on a dedicated pass), ~~skill-router file `RESOLVER.md` (gbrain)~~ → **promoted** to [[patterns/composition/resolver-routing-table]], agent-first install protocol `AGENTS.md` (gbrain), `llms.txt`+`llms-full.txt` dual files (gbrain).

## Suspected anti-patterns

Things we've seen creators do that we think *don't* work. These need the same rigor as patterns — ≥2 examples and a clear "why this fails."

- *(none yet)*
