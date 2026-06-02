# Research Wiki — Master Index

The single front door. Every page in the wiki should be reachable from this index in one or two clicks. If a page exists but isn't listed here, it's effectively invisible — `INGEST` step 7 is to add it here.

For an explanation of what this wiki is and how it operates, see [CLAUDE.md](CLAUDE.md). For a human-friendly summary, see [README.md](README.md). For the chronological record of what was added when, see [log.md](log.md). **If you're an agent pointed here from another project to mine this wiki while building something, start at [for-builders.md](for-builders.md)** — the consumer front door (routing table + extraction protocol).

## Quick navigation

| Section | Purpose |
| --- | --- |
| [Sources](#sources) | Cloned/snapshotted evidence — every claim cites here |
| [Creators](#creators) | People and orgs behind the artifacts |
| [Artifacts — Plugins](#artifacts--plugins) | Collections (skills + commands + agents + hooks + MCP) |
| [Artifacts — Skills](#artifacts--skills) | Individual skills |
| [Artifacts — MCP Servers](#artifacts--mcp-servers) | MCP server projects |
| [Artifacts — Projects](#artifacts--projects) | Frontier projects/systems not reducible to one skill/plugin/MCP |
| [Concepts](#concepts) | Ideas & techniques (often from essays & papers) |
| [Patterns](#patterns) | Recurring techniques across artifacts (the research output) |
| [Analyses](#analyses) | Synthesis writeups |
| [Meta](#meta) | The wiki applied to itself (REFLECT ledger) |

---

## Sources

Cloned repo snapshots and their citation pages. Repo files live at `sources/<creator>--<repo>/`; the `.md` page is the citation target.

| Source | Type | Snapshot date | Commit |
| --- | --- | --- | --- |
| [[sources/anthropic--skills]] | repo | 2026-05-21 | `690f15c` |
| [[sources/garrytan--gstack]] | repo | 2026-05-21 | `029356e` |
| [[sources/garrytan--gbrain]] | repo | 2026-05-21 | `1580c6d` |
| [[sources/anthropic--plugins-reference]] | docs-page | 2026-05-31 | n/a (living page) |
| [[sources/anthropic--financial-services]] | repo | 2026-06-01 | `120a31d` |
| [[sources/garrytan--foxconn-factories]] | article | 2026-06-01 | n/a (essay #8) |
| [[sources/garrytan--thin-harness-fat-skills]] | article | 2026-06-01 | n/a (essay #1) |
| [[sources/garrytan--resolvers]] | article | 2026-06-01 | n/a (essay #2) |
| [[sources/garrytan--loc-controversy]] | article | 2026-06-01 | n/a (essay #3) |
| [[sources/garrytan--naked-models]] | article | 2026-06-01 | n/a (essay #4) |
| [[sources/garrytan--skillify-manifesto]] | article | 2026-06-01 | n/a (essay #5) |
| [[sources/garrytan--meta-meta-prompting]] | article | 2026-06-01 | n/a (essay #6) |
| [[sources/garrytan--complexity-ratchet]] | article | 2026-06-01 | n/a (essay #7) |
| [[sources/every--compound-engineering-plugin]] | repo | 2026-06-02 | `3e77a7b` |
| [[sources/every--compound-engineering]] | docs-page | 2026-06-02 | n/a (living page) |
| [[sources/every--compound-engineering-gets-an-upgrade]] | article | 2026-06-02 | 2026-05-29 |
| [[sources/openai--using-goals-in-codex]] | docs-page | 2026-06-02 | `9b4e627` (pub 2026-05-09) |
| [[sources/openai--plugins]] | repo | 2026-06-02 | `bebc3d6` |

The 8 `garrytan--*` essays form one **"AI Explainer" series** (#1–#8) — a longitudinal record of `gstack`/`gbrain`'s growth (stars climb 72K→75K→87K→93K→105K across the run). See also: [sources/_index.md](sources/_index.md) for citation conventions.

## Creators

| Creator | Type | Notes |
| --- | --- | --- |
| [[creators/anthropic]] | org | Sets the Agent Skills spec; ships demonstration skills + plugins + the Claude API |
| [[creators/garry-tan]] | individual | President & CEO of Y Combinator; ships `gstack` and `gbrain` |
| [[creators/every]] | org | Media+software company; origin/home of compound engineering. Kieran Klaassen (plugin author, GM of Cora) + Dan Shipper (CEO) |
| [[creators/openai]] | org | Frontier lab; ships GPT + the **Codex** CLI. Two studied Codex layers: **Goals** ([[artifacts/projects/codex-goals]]) and the **167-plugin marketplace** ([[artifacts/plugins/openai-codex-plugins-marketplace]]) |

## Artifacts — Plugins

| Plugin | Creator | Status | One-line |
| --- | --- | --- | --- |
| [[artifacts/plugins/anthropic-skills-marketplace]] | Anthropic | speedrun | Demonstration marketplace; 3 child plugins, 17 skills; reference shape |
| [[artifacts/plugins/gstack]] | Garry Tan | speedrun | Virtual engineering team (CEO, Designer, QA Lead, etc.); 23 skills |
| [[artifacts/plugins/gbrain]] | Garry Tan | speedrun | Hybrid vector+graph memory; ships as CLI + MCP + skillpack |
| [[artifacts/plugins/anthropic-financial-services-marketplace]] | Anthropic (FSI) | full | FSI marketplace; 20 plugins, dual-runtime (Cowork + Managed Agents API), trust-tiered subagents |
| [[artifacts/plugins/compound-engineering]] | Every (Kieran Klaassen) | full | Compound-engineering loop; 38 skills + 43 agents, converted to ~11 harnesses; dogfoods its own loop; **first non-Garry tested pack** |
| [[artifacts/plugins/openai-codex-plugins-marketplace]] | OpenAI | full | **Codex** marketplace; 167 plugins, hosted-app (`.app.json`) connectors + 479 skills; productized storefront; **first non-Claude-Code marketplace** |

Candidate queue (not yet ingested): see [artifacts/plugins/_index.md](artifacts/plugins/_index.md).

## Artifacts — Skills

*(none ingested yet; 17+ candidates queued from `anthropic/skills`, dozens more inside gstack/gbrain)*

Candidate queue: see [artifacts/skills/_index.md](artifacts/skills/_index.md).

## Artifacts — MCP Servers

*(none ingested yet; 1 referenced inside gbrain's manifest — `gbrain serve`)*

Candidate queue: see [artifacts/mcp-servers/_index.md](artifacts/mcp-servers/_index.md).

## Artifacts — Projects

Frontier projects/systems/products that aren't reducible to a single skill, plugin, or MCP server.

| Project | Creator | Status | One-line |
| --- | --- | --- | --- |
| [[artifacts/projects/codex-goals]] | OpenAI | feature-deep-dive | Codex CLI's **Goals** feature — persistent, evidence-gated `/goal` objectives (≥ 0.128.0); embodies [[concepts/completion-contract]], grounds [[patterns/behavioral/evidence-gated-completion]] |

Candidate queue: see [artifacts/projects/_index.md](artifacts/projects/_index.md).

## Concepts

Ideas and techniques worth their own page — especially from essays, papers, and threads. A concept graduates to a [pattern](#patterns) once observed across ≥2 artifacts.

**Paged:**

- [[concepts/compound-engineering]] — Every's (Kieran Klaassen's) methodology: each unit of work makes the next easier; 80/20 planning + 50/50 features-vs-systems; "taste belongs in systems, not review." The independently-named twin of [[patterns/quality-bar/complexity-ratchet]]; embodied by [[artifacts/plugins/compound-engineering]].
- [[concepts/completion-contract]] — an agent objective as a persistent, evidence-verified *contract* ("done" decided by evidence, not confidence). OpenAI's term, productized as Codex Goals; embodied by [[artifacts/projects/codex-goals]].
- [[concepts/convergent-agent-plugin-spec]] — Anthropic's `.claude-plugin/` and OpenAI's `.codex-plugin/` are near-identical (same skills/hooks/MCP/marketplace grammar) — the agent plugin shape is consolidating into a **cross-lab standard**. `emerging`. Grounds the cross-ecosystem reach of [[patterns/structural/marketplace-as-multi-plugin]] + [[patterns/structural/thin-harness-fat-skills]]. Sources: [[sources/openai--plugins]] + [[sources/anthropic--plugins-reference]].

Candidate queue: see [concepts/_index.md](concepts/_index.md).

## Patterns

The actual research output. Confirmed patterns (≥2 artifact examples + counter-example) listed here. Proposed patterns are tracked on the relevant artifact pages and promoted when evidence accumulates.

**Confirmed (8 as of 2026-06-02):**

- [[patterns/composition/single-source-multi-surface-distribution]] — one definition, many surfaces (reference *or* convert *or* run-natively; never hand-fork). financial-services (Cowork + Managed Agents API), gbrain (CLI + MCP + skillpack), compound-engineering (→ ~11 competing harnesses via a converter), openai-codex-plugins (plugin-eval = CLI+plugin; superpowers runs on Codex+Claude Code with **no transform** — **new mechanism 2026-06-02**, →4 examples).
- [[patterns/structural/marketplace-as-multi-plugin]] — one repo's `marketplace.json` registers N à-la-carte plugins. financial-services (20), anthropic-skills-marketplace (3), **openai-codex-plugins (167 — first non-Claude-Code, makes the pattern cross-lab 2026-06-02)**.
- [[patterns/quality-bar/skill-pack-bundle]] — a skill ships as a *tested bundle*; "a skill pack has tests." gstack + gbrain + compound-engineering (~1,094 tests incl. behavioral *contract* tests). **Same-creator caveat retired 2026-06-02** (CE is non-Garry, two ecosystems); residue: the *resolver eval* sub-part stays Garry-best.
- [[patterns/composition/resolver-routing-table]] — a *tested* routing table (intent→which skill/doc); trigger evals + `check-resolvable`, fractal across layers. gbrain + gstack. ⚠ same-creator.
- [[patterns/behavioral/latent-vs-deterministic-split]] — every step is model-judgment or same-in/same-out; put each on the right side. gstack + gbrain + compound-engineering (states the rule: "skills are guardrails… calibrate prescription to the failure mode"). **Same-creator caveat retired 2026-06-02.**
- [[patterns/quality-bar/complexity-ratchet]] — every session adds tests/docs/evals that reload into context, so the quality floor only rises (forward-only). gstack + gbrain + compound-engineering (`docs/solutions/` knowledge ratchet + branch-protection floor). **Promoted proposed→confirmed 2026-06-02** — CE is the independent non-Garry example; [[concepts/compound-engineering]] names the principle independently.
- [[patterns/quality-bar/version-as-update-gate]] — `version` is the update-delivery trigger (installs cached by version), so release-automation owns it and hand-bumps are forbidden. financial-services (pre-commit hook) + compound-engineering (release-please + `linked-versions`). **New + confirmed 2026-06-02.**
- [[patterns/behavioral/skill-as-method-call]] — a skill/command file is a parameterized procedure; same file, different arguments → different capability. **Promoted 2026-06-02**: gstack (`/qa` tiers, `/investigate`) + [[artifacts/projects/codex-goals]] (the `/goal` six-slot signature — non-Garry, on the Codex CLI).

**Proposed, with a dedicated page:**

- [[patterns/structural/thin-harness-fat-skills]] — fat markdown skills (~90% of value) / thin deterministic code / thin harness. Fat-skills half now **cross-confirmed across three creators** (gstack/gbrain + compound-engineering + openai-codex-plugins/superpowers); still `proposed` — the thin *harness* middle (OpenClaw / Claude Code / Codex) is now *named* via a concrete artifact but its loop still isn't ingested in any example.
- [[patterns/behavioral/evidence-gated-completion]] — an agent can't self-declare *done*; completion is gated on an external verification surface, and budget-exhaustion ≠ done. Grounded in [[artifacts/projects/codex-goals]] (Codex Goals); in-wiki promotion candidates noted (`complexity-ratchet`, gstack floor tests). **New (proposed) 2026-06-02.**
- [[patterns/behavioral/diarization]] — read everything about a subject, write one structured page of distilled judgment (the "says vs actually building" gap). gbrain `enrich/` + brain-page schema.

Proposed patterns currently mentioned across the plugin pages (need 2nd example to confirm):

- Persona-shaped command naming (gstack)
- Philosophy injection via preamble (gstack ETHOS)
- Frontmatter extensions beyond official spec (gstack + gbrain both do this — likely confirmable now)
- Voice-trigger aliases in description (gstack)
- Heavy bash preamble as "skill OS" (gstack)
- Pack-branding suffix in skill descriptions (gstack)
- ~~Three-shape distribution: CLI + MCP + skillpack (gbrain)~~ → **promoted** to [[patterns/composition/single-source-multi-surface-distribution]]
- ~~Skill-router file (`RESOLVER.md`) (gbrain)~~ → **promoted** to [[patterns/composition/resolver-routing-table]]
- Underscore-prefixed universal rules (gbrain)
- Agent-first install protocol (`AGENTS.md` separate from `CLAUDE.md`) (gbrain)
- `[AGENT]`-marked operator-decision banner (gbrain)
- ~~Marketplace-as-multi-plugin (anthropic-skills-marketplace)~~ → **promoted** to [[patterns/structural/marketplace-as-multi-plugin]]
- `llms.txt` + `llms-full.txt` dual files (gbrain)
- Trust-tiered subagent privilege separation (financial-services) — *new; standout idea to find again*
- Structured-output-as-injection-defense (financial-services)
- Single-source-of-truth skill vendoring + drift check (financial-services)
- Provenance-first data-source hierarchy (financial-services)
- ~~Version-as-update-gate (financial-services)~~ → **promoted** to [[patterns/quality-bar/version-as-update-gate]] (2nd example: compound-engineering)
- *New from compound-engineering (1 example each; see [patterns/_index.md](patterns/_index.md)):* skill-self-containment for portability · cross-platform-portable skill authoring · dedup-before-create · legacy-artifact cleanup registry · auto-invoke trigger phrases
- Audience-segmented skill output (financial-services / S&P)

See [patterns/_index.md](patterns/_index.md) for the per-category breakdown.

## Analyses

*(none yet — see [analyses/_index.md](analyses/_index.md) for the rule of "no synthesis until ≥5 artifacts of relevant type")*

## Meta

The wiki applied to itself — improvements to our own machinery, each traced to a pattern observed in the wiki (the [REFLECT](CLAUDE.md) operation).

- [[meta/self-improvements]] — self-improvement ledger; applied/embodied wiki machinery changes traced to observed patterns and concepts, including routing, doctor tooling, page definitions of done, consumer-agent guidance, portability, and release/versioning principles.
