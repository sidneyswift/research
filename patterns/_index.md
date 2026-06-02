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

*(First two confirmed 2026-06-01 via `anthropic-financial-services`; three more confirmed 2026-06-01 from Garry Tan's "AI Explainer" series — gstack + gbrain. **2026-06-02 — `compound-engineering` (Every / Kieran Klaassen), the wiki's first non-Garry tested skill pack — promoted `complexity-ratchet` to confirmed, confirmed the new `version-as-update-gate`, broadened `single-source-multi-surface-distribution` (a new "competing harnesses" axis), and retired the same-creator caveat on `skill-pack-bundle` + `latent-vs-deterministic-split`.**)*

- **composition/** [[patterns/composition/single-source-multi-surface-distribution]] — author the capability once, make it run on multiple surfaces (reference *or* convert; never hand-fork). Examples: [[artifacts/plugins/anthropic-financial-services-marketplace]] (Cowork plugin + Managed Agents API), [[artifacts/plugins/gbrain]] (CLI + MCP + skillpack), [[artifacts/plugins/compound-engineering]] (one Claude format → **converted to ~11 competing harnesses** via a CLI). **3rd example + new axis 2026-06-02**: competing third-party tools, by conversion not live-reference.
- **structural/** [[patterns/structural/marketplace-as-multi-plugin]] — one repo's `marketplace.json` registers N à-la-carte plugins. Examples: [[artifacts/plugins/anthropic-financial-services-marketplace]] (20), [[artifacts/plugins/anthropic-skills-marketplace]] (3). Counter: gstack/gbrain (one plugin, many internal skills).
- **quality-bar/** [[patterns/quality-bar/skill-pack-bundle]] — a skill ships as a *tested bundle* (markdown skill + thin code + unit/LLM/integration/resolver tests; the 10-step "skillify" checklist). Examples: [[artifacts/plugins/gstack]] (7 parts as files) + [[artifacts/plugins/gbrain]] (`gbrain doctor` enforces 10 steps) + [[artifacts/plugins/compound-engineering]] (~1,094 tests incl. behavioral *contract* tests). **Same-creator caveat retired 2026-06-02** (CE is non-Garry, two ecosystems). Residue: the *resolver eval* sub-part stays Garry-best (CE leans on the built-in description-resolver).
- **composition/** [[patterns/composition/resolver-routing-table]] — a routing table mapping intent/content-type→which skill or doc to load; tested with trigger evals, audited with `check-resolvable`, fractal across layers (skill / filing / context-inside-a-skill). Examples: [[artifacts/plugins/gbrain]] (`skills/RESOLVER.md` + 14+ `routing-eval.jsonl` + `check-resolvable.ts`) + [[artifacts/plugins/gstack]] (`scripts/resolvers/` + resolver evals). **Supersedes** the old proposed "skill-router file `RESOLVER.md`" bullet. ⚠ same-creator.
- **behavioral/** [[patterns/behavioral/latent-vs-deterministic-split]] — every step is latent (model judgment) or deterministic (same-in/same-out); put each on the correct side. Examples: [[artifacts/plugins/gstack]] (deterministic `browse/` + `bin/` vs latent skills) + [[artifacts/plugins/gbrain]] ("zero-LLM" graph vs latent synthesis) + [[artifacts/plugins/compound-engineering]] (states the rule outright: "skills are guardrails… calibrate prescription to the failure mode"). **Same-creator caveat retired 2026-06-02** (CE is non-Garry and names the rule). Residue: the *word* "latent" is still essay vocabulary, not the field's.
- **quality-bar/** [[patterns/quality-bar/complexity-ratchet]] — every session adds tests/docs/evals that reload into the next session's context, so the quality floor only rises (forward-only). Examples: [[artifacts/plugins/gstack]] (TTY review-floor tests) + [[artifacts/plugins/gbrain]] (extraction ratchet) + [[artifacts/plugins/compound-engineering]] (`docs/solutions/` knowledge ratchet + branch-protection floor). **Promoted proposed→confirmed 2026-06-02** — CE is the independent non-Garry example its promotion bar named, and [[concepts/compound-engineering]] names the same forward-only principle independently.
- **quality-bar/** [[patterns/quality-bar/version-as-update-gate]] — `version` is the update-delivery trigger (installs are cached by version), so make it release-automation-owned, forbid hand-bumps, and let one automated bump per release gate the batch. Examples: [[artifacts/plugins/anthropic-financial-services-marketplace]] (pre-commit hook + CI Action) + [[artifacts/plugins/compound-engineering]] (release-please + `linked-versions` + `release:validate` across 3 manifests). **New + confirmed 2026-06-02.**
- **behavioral/** [[patterns/behavioral/skill-as-method-call]] — a skill/command file is a parameterized procedure; same file, different arguments → different capability. Examples: [[artifacts/plugins/gstack]] (`/qa` depth tiers, `/investigate`) + [[artifacts/projects/codex-goals]] (the `/goal` six-slot signature — explicit documented parameters, **non-Garry**, on the Codex CLI). **Promoted proposed→confirmed 2026-06-02** — Codex Goals cleared the page's named gate (a documented parameter signature from a non-Garry pack); the pattern now spans two creators *and* two harnesses.

## Proposed patterns

Hypotheses with one grounded example so far — tracked on the relevant artifact page until a 2nd example promotes them. Each gets a 1-line rationale.

*(With a dedicated page. Each grounded in 1 artifact's full shape; promotion needs the missing half. `complexity-ratchet` was **promoted out to confirmed 2026-06-02**.)*

- **structural/** [[patterns/structural/thin-harness-fat-skills]] — push intelligence up into markdown skills (~90% of value), execution down into deterministic code, keep the harness thin. **Fat-skills half now cross-confirmed across two creators** ([[artifacts/plugins/gstack]]/[[artifacts/plugins/gbrain]] + [[artifacts/plugins/compound-engineering]], which states the philosophy and rides interchangeable harnesses) — but still `proposed` because the thin-*harness* middle (OpenClaw / Claude Code / Codex) isn't ingested in *any* example; promotion needs an actual harness ingested. A possible missing "harnesses" axis.
- **behavioral/** [[patterns/behavioral/evidence-gated-completion]] — an agent may not self-declare *done*; completion is gated on an external verification surface (tests / benchmark / build / artifact), and budget-exhaustion ≠ done. Grounded in [[artifacts/projects/codex-goals]] (Codex Goals: "evidence decides, not model belief"); promotion candidates already in-wiki ([[patterns/quality-bar/complexity-ratchet]]'s "evidence decides"; gstack's plan-review finding-floor tests). **New (proposed) 2026-06-02.**
- **behavioral/** [[patterns/behavioral/diarization]] — read everything about a subject, write one structured page of distilled judgment (the "says vs actually building" gap, who-holds-the-belief). Grounded in [[artifacts/plugins/gbrain]] (`enrich/`, brain-page schema, entity propagation).

*(Other proposed — one example so far, tracked on artifact pages:)*

- **trust-tiered subagent privilege separation** — prompt-injection containment by role (only the reader touches untrusted docs; exactly one leaf holds Write; a critic re-verifies). 1 example ([[artifacts/plugins/anthropic-financial-services-marketplace]]); *the standout idea to find again*.
- **structured-output-as-injection-defense** — bound a worker's only output channel to a length/character-class-restricted schema so injected text can't survive. 1 example (FSI `reader` `output_schema`). *Relative:* CE's `ce-code-review` sub-agents return JSON the orchestrator merges/dedups — structured sub-agent output, defense-adjacent.
- **single-source-of-truth skill vendoring + drift check** — author once, vendor copies into bundles, fail the build on drift. 1 example (FSI `sync-agent-skills.py` + `check.py`).
- **provenance-first data-source hierarchy** — skills hard-prefer audited MCP connectors over web search, and say why. 1 example (FSI `comps-analysis`).
- **audience-segmented skill output** — one skill, N audiences, N reference files, "if unspecified, ask." 1 example (FSI/S&P `tear-sheet`).
- **skill-self-containment for portability** *(new — CE)* — a `SKILL.md` references only its own directory; duplicate shared files, never cross-link. 1 example ([[artifacts/plugins/compound-engineering]]; converter + versioned-cache driven).
- **cross-platform-portable skill authoring** *(new — CE)* — no unguarded platform env vars; name per-platform tool equivalents (`AskUserQuestion`/`request_user_input`/`ask_user`; `Agent`/`spawn_agent`/`subagent`). 1 example (CE).
- **dedup-before-create** *(new — CE)* — score overlap across dimensions; *update* the existing doc rather than create a near-duplicate. 1 example (CE `ce-compound`); already imported into this wiki's INGEST (see [[meta/self-improvements]]).
- **legacy-artifact cleanup registry** *(new — CE)* — register a removed skill/agent so stale flat-install copies are swept on upgrade. 1 example (CE `STALE_*` lists).
- **auto-invoke trigger phrases** *(new — CE)* — a skill self-fires on natural-language cues ("that worked", "it's fixed"). 1 example (CE `ce-compound`); relative of gstack's voice-trigger aliases.
- *(carried from earlier ingests, tracked on plugin pages, still need a 2nd example):* **persona/lens-shaped naming + multi-agent review panel** (gstack QA personas + **CE `ce-code-review` lenses + named-expert agents** — *likely confirmable*), philosophy-injection preamble (gstack ETHOS), frontmatter-extensions-beyond-spec (gstack + gbrain — likely confirmable), ~~skill-router file `RESOLVER.md` (gbrain)~~ → **promoted** to [[patterns/composition/resolver-routing-table]], **agent-first canonical docs `AGENTS.md`** (gbrain `AGENTS.md`-separate-from-`CLAUDE.md` + **CE `CLAUDE.md`=`@AGENTS.md` shim** — *likely confirmable*), `llms.txt`+`llms-full.txt` dual files (gbrain).

## Suspected anti-patterns

Things we've seen creators do that we think *don't* work. These need the same rigor as patterns — ≥2 examples and a clear "why this fails."

- *(none yet)*
