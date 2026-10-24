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
| [[sources/anthropic--dynamic-workflows]] | article | 2026-06-02 | n/a (article) |
| [[sources/ahrefs--ai-search-optimization-research]] | tweet | 2026-06-02 | n/a (social post) |
| [[sources/agentskills--specification]] | docs-page | 2026-06-04 | n/a (living page) |
| [[sources/openai--codex-skills-doc]] | docs-page | 2026-06-04 | n/a (living page) |
| [[sources/openai--chatgpt-skills-help]] | docs-page | 2026-06-04 | n/a (living page, ⚠ secondary-fidelity capture) |
| [[sources/prodmgmt-world--pm-os]] | other (purchased bundle) | 2026-06-10 | v2.2.1 (zips; local-only copy) |
| [[sources/prodmgmt-world--pm-os-cowork]] | zip release (other) | 2026-06-11 | v2.2.1 (paid product; private upstream) |
| [[sources/mattpocock--skills]] | repo | 2026-06-19 | `6eeb81b` (135,831★) |
| [[sources/forward-future--loop-library]] | repo | 2026-06-20 | `6ee3345` (92★) |
| [[sources/vercel--eve]] | repo | 2026-06-20 | `bfc7191` (1,671★) |
| [[sources/SHL0MS--skill-diffs]] | repo | 2026-07-22 | `2ded6c0` (0★; dataset v0.5) |
| [[sources/humanlayer--humanlayer]] | repo | 2026-10-23 | `2f66a45` (11,977★ at retrieval) |

The 8 `garrytan--*` essays form one **"AI Explainer" series** (#1–#8) — a longitudinal record of `gstack`/`gbrain`'s growth (stars climb 72K→75K→87K→93K→105K across the run). See also: [sources/_index.md](sources/_index.md) for citation conventions.

## Creators

| Creator | Type | Notes |
| --- | --- | --- |
| [[creators/anthropic]] | org | Sets the Agent Skills spec; ships demonstration skills + plugins + the Claude API |
| [[creators/garry-tan]] | individual | President & CEO of Y Combinator; ships `gstack` and `gbrain` |
| [[creators/every]] | org | Media+software company; origin/home of compound engineering. Kieran Klaassen (plugin author, GM of Cora) + Dan Shipper (CEO) |
| [[creators/openai]] | org | Frontier lab; ships GPT + the **Codex** CLI. Three studied layers: **Goals** ([[artifacts/projects/codex-goals]]), the **167-plugin marketplace** ([[artifacts/plugins/openai-codex-plugins-marketplace]]), and the **skills distribution/governance stack** ([[concepts/workspace-skill-distribution]]) |
| [[creators/ahrefs]] | org | Largest SEO tooling company; publishes large-scale AI search optimization research (Tim Soulo, CMO). Data/research contributor, not an agent builder |
| [[creators/prodmgmt-world]] | org | George Nurijanian; independent commercial publisher of **PM OS** ($99 PM-vertical bundle); **first commercial/closed creator** and first non-engineering vertical |
| [[creators/matt-pocock]] | individual | TypeScript educator (Total TypeScript / AI Hero); ships `mattpocock/skills` (**135K★**) — fundamentals-over-frameworks, small/composable/model-agnostic; defines `skill-invocation-axis` + `ubiquitous-language-for-agents` |
| [[creators/vercel]] | org | Frontend-cloud co. behind Next.js / AI SDK / Workflow SDK; ships **eve** ([[artifacts/projects/eve]]) — the wiki's **first agent framework / harness** and first platform/infra creator. Grounds `filesystem-first-agent-framework` + `durable-agent-execution` |
| [[creators/forward-future]] | org | Matthew Berman's AI media brand; ships the **Loop Library** — a curated, submission-driven catalog of repeatable agent loops + an installable find/adapt/design skill. First catalog-of-prompts creator |
| [[creators/shl0ms]] | individual | GitHub handle (real name undisclosed); ships **skill-diffs** ([[artifacts/projects/skill-diffs]]) — a commit-history mining pipeline + dataset + linter/eval tools for training a skill-curator model. First dataset-and-tooling-pipeline creator; lowest-traction source to date (0★) |
| [[creators/humanlayer]] | org | Collaborative coding-agent platform and RPI workflow; human review, task continuity, and host execution |

## Artifacts — Plugins

| Plugin | Creator | Status | One-line |
| --- | --- | --- | --- |
| [[artifacts/plugins/anthropic-skills-marketplace]] | Anthropic | speedrun | Demonstration marketplace; 3 child plugins, 17 skills; reference shape |
| [[artifacts/plugins/gstack]] | Garry Tan | speedrun | Virtual engineering team (CEO, Designer, QA Lead, etc.); 23 skills |
| [[artifacts/plugins/gbrain]] | Garry Tan | speedrun | Hybrid vector+graph memory; ships as CLI + MCP + skillpack |
| [[artifacts/plugins/anthropic-financial-services-marketplace]] | Anthropic (FSI) | full | FSI marketplace; 20 plugins, dual-runtime (Cowork + Managed Agents API), trust-tiered subagents |
| [[artifacts/plugins/compound-engineering]] | Every (Kieran Klaassen) | full | Compound-engineering loop; 38 skills + 43 agents, converted to ~11 harnesses; dogfoods its own loop; **first non-Garry tested pack** |
| [[artifacts/plugins/openai-codex-plugins-marketplace]] | OpenAI | full | **Codex** marketplace; 167 plugins, hosted-app (`.app.json`) connectors + 479 skills; productized storefront; **first non-Claude-Code marketplace** |
| [[artifacts/plugins/pm-os]] | prodmgmt.world | full | Paid PM-vertical "AI OS" (v2.2.1); 235 skills (3-tier hierarchy) + 12 reviewer/router sub-agents + nudge hooks + fat enforcement harness (pre-flight, Context Guard, deliverable gate); plugin/workspace split; **first purchased artifact + first non-engineering vertical** |
| [[artifacts/plugins/mattpocock-skills]] | Matt Pocock | full | "Skills For Real Engineers"; ~17 small composable **model-agnostic** skills fixing 4 agent failure modes with SWE fundamentals; pure skills, **no tests**; **135K★** (highest in corpus); the counter-bet to `skill-pack-bundle` |
| [[artifacts/plugins/humanlayer-rpi]] | HumanLayer | source-investigated | RPI workflow skills + companion helpers; 46 lessons on review gates, artifact ownership, specialist work, and bounded context |

Candidate queue (not yet ingested): see [artifacts/plugins/_index.md](artifacts/plugins/_index.md).

## Artifacts — Skills

| Skill | Creator | Status | One-line |
| --- | --- | --- | --- |
| [[artifacts/skills/grilling]] | Matt Pocock | active | Relentless one-question-at-a-time alignment interview; the reusable loop behind `grill-me`/`grill-with-docs`. The wiki's **first individual skill page** |
| [[artifacts/skills/writing-great-skills]] | Matt Pocock | active | Reference for *authoring* skills — predictability, the two loads, the info-hierarchy ladder, leading words, the five failure modes; the most self-applicable artifact in the wiki |
| [[artifacts/skills/loop-library]] | Forward Future | active | Find/adapt/design a **bounded agent loop** (task + observable verify + named stop); bundles a 31-loop catalog from ~14 builders. The **confirming 2nd artifact** for [[patterns/behavioral/evidence-gated-completion]] |

Candidate queue (dozens more from `mattpocock/skills`, `anthropic/skills`, gstack/gbrain, pm-os, FSI): see [artifacts/skills/_index.md](artifacts/skills/_index.md).

## Artifacts — MCP Servers

*(none ingested yet; 1 referenced inside gbrain's manifest — `gbrain serve`)*

Candidate queue: see [artifacts/mcp-servers/_index.md](artifacts/mcp-servers/_index.md).

## Artifacts — Projects

Frontier projects/systems/products that aren't reducible to a single skill, plugin, or MCP server.

| Project | Creator | Status | One-line |
| --- | --- | --- | --- |
| [[artifacts/projects/codex-goals]] | OpenAI | feature-deep-dive | Codex CLI's **Goals** feature — persistent, evidence-gated `/goal` objectives (≥ 0.128.0); embodies [[concepts/completion-contract]], grounds [[patterns/behavioral/evidence-gated-completion]] |
| [[artifacts/projects/eve]] | Vercel | active (beta) | **Filesystem-first, durable agent framework** ("Next.js for agents") — agent-as-directory, a framework-owned harness + toolbelt, durable sessions, channels, sandboxes, evals. The wiki's **first ingested harness**; embodies [[concepts/filesystem-first-agent-framework]] + [[concepts/durable-agent-execution]] |
| [[artifacts/projects/skill-diffs]] | SHL0MS | active | Commit-history mining pipeline → `(before, after, intent)` skill-edit dataset (4 platforms) + a **defect-derived linter** + skill-patch eval harness. The wiki's **first dataset-and-tooling-pipeline** artifact; embodies [[concepts/commit-history-as-training-data]] + [[concepts/imitation-vs-correctness-eval]] |
| [[artifacts/projects/humanlayer]] | HumanLayer | source-investigated | Collaborative agent platform: tasks, sessions, hosts, artifacts, review, and scoped recovery; pinned source investigation |

Candidate queue: see [artifacts/projects/_index.md](artifacts/projects/_index.md).

## Concepts

- [[concepts/review-cost-aware-workflows]] — Choose workflow depth and review surfaces around human decision cost; review facts and choices before expensive implementation.
- [[concepts/artifact-centered-agent-context]] — Give facts, decisions, design, and execution progress explicit artifact owners; pass bounded context into fresh sessions.
- [[concepts/agent-control-plane]] — Separate durable tasks, access, artifacts, and review from provider-specific sessions and execution hosts.

Ideas and techniques worth their own page — especially from essays, papers, and threads. A concept graduates to a [pattern](#patterns) once observed across ≥2 artifacts.

**Paged:**

- [[concepts/compound-engineering]] — Every's (Kieran Klaassen's) methodology: each unit of work makes the next easier; 80/20 planning + 50/50 features-vs-systems; "taste belongs in systems, not review." The independently-named twin of [[patterns/quality-bar/complexity-ratchet]]; embodied by [[artifacts/plugins/compound-engineering]].
- [[concepts/completion-contract]] — an agent objective as a persistent, evidence-verified *contract* ("done" decided by evidence, not confidence). OpenAI's term, productized as Codex Goals; embodied by [[artifacts/projects/codex-goals]].
- [[concepts/dynamic-workflows]] — Claude Code's model-generated JS harnesses for multi-agent orchestration. The model writes a custom harness per task, spawning subagents with isolated context windows to defeat agentic laziness, self-preferential bias, and goal drift. Six composable patterns. Workflows distributable via skills. `active`. Source: [[sources/anthropic--dynamic-workflows]].
- [[concepts/ai-search-as-parallel-discovery-layer]] — AI chatbots form a **parallel discovery layer** independent of Google organic search — different sources, citation patterns, and content format preferences. Backed by 1B data points across 14 Ahrefs studies. YouTube mentions = highest AI brand visibility correlation (0.737); 28.3% of most-cited pages have zero Google visibility. `emerging`. Source: [[sources/ahrefs--ai-search-optimization-research]].
- [[patterns/structural/thin-harness-fat-skills]] — portable workflow judgment can live in Markdown while runtime responsibilities remain in code. [[artifacts/projects/eve]] and [[artifacts/projects/humanlayer]] expose substantial lifecycle, recovery, and authorization infrastructure: separation is supported; literal “thinness” is not. Remains **proposed** pending a sharper invariant and evidence for it, rather than promotion by counting another runtime.
- [[concepts/workspace-skill-distribution]] — how an org distributes skills to every member without per-machine installs: four rails (repo-as-install via the `.agents/skills` scope ladder, ChatGPT admin push "install for other members," marketplace/workspace sharing, machine scope `/etc/codex/skills`) + the **restrictive/additive split** (enforcement config can only constrain, never distribute). `emerging`, OpenAI-grounded (n=1 ecosystem). Sources: [[sources/openai--codex-skills-doc]] + [[sources/openai--chatgpt-skills-help]] + [[sources/openai--plugins]].
- [[concepts/skill-invocation-axis]] — every skill splits on *who can invoke it*: **model-invoked** (has a `description`; model/user/other-skills can reach it; pays **context load**) vs **user-invoked** (`disable-model-invocation`; human-only; pays **cognitive load**; unreachable by other skills). A user-invoked skill may call model-invoked ones but never another user-invoked one; piled cognitive load is cured by a router skill. A deliberate context-budget lever. `emerging`; Matt Pocock. Source: [[sources/mattpocock--skills]].
- [[concepts/ubiquitous-language-for-agents]] — Evans's **ubiquitous language** ported to the human↔agent gap: a `CONTEXT.md` glossary *for the agent* (and nothing else — decisions → ADRs), built via `domain-modeling`/`grill-with-docs`, collapsing jargon to single terms (fewer tokens, consistent naming). Pocock's "single coolest technique." `emerging`. Source: [[sources/mattpocock--skills]].
- [[concepts/filesystem-first-agent-framework]] — **convention over configuration, ported to agents**: an agent *is* a directory, each capability is a file in a known slot, identity is path-derived, the framework *discovers* the tree (no registry, no big config object). The Rails/Next.js idea aimed at agents. `emerging` (n=1 whole-agent framework — eve). Source: [[sources/vercel--eve]].
- [[concepts/durable-agent-execution]] — **durability as substrate, not feature**: run a conversation as a durable workflow (session → turn → step), checkpoint each step, replay completed steps after a crash, and **park** with zero compute while waiting on a human/OAuth/child, resuming days later. Forces "interrupted steps re-run → make side effects idempotent or gate them." `emerging` (eve's default, on the Workflow SDK; Codex Goals a different-grain cousin). Source: [[sources/vercel--eve]].
- [[concepts/agentic-loop]] — a **loop** = a bounded, self-correcting agent prompt (task + observable verification + a named stopping condition), the opposite of a one-shot prompt; the repeating-cycle layer above [[concepts/completion-contract]]. "Loops are not permission for an agent to run forever." `emerging`; Forward Future. Source: [[sources/forward-future--loop-library]].
- [[concepts/commit-history-as-training-data]] — mine the **commit-by-commit revision history** of many public instances of an artifact into `(before, after, intent)` training triples, capturing evolution instead of collecting only finished snapshots. `emerging` (n=1 — SHL0MS's `skill-diffs`, on `SKILL.md` files across 4 platforms). Grounds [[patterns/quality-bar/defect-derived-validation]]. Source: [[sources/SHL0MS--skill-diffs]].
- [[concepts/imitation-vs-correctness-eval]] — when a training corpus's "gold" is just *whatever got merged*, split the eval into an **imitation** axis (lexical + LLM-judge match to the accepted-edit distribution) and a **correctness** axis (a gold-independent rule-based signal), because a bigger model can win one and lose the other. `emerging`. Source: [[sources/SHL0MS--skill-diffs]].

Candidate queue: see [concepts/_index.md](concepts/_index.md).

## Patterns

The actual research output. Confirmed patterns (≥2 artifact examples + counter-example) listed here. Proposed patterns are tracked on the relevant artifact pages and promoted when evidence accumulates.

**Confirmed (10 as of 2026-06-20; supporting sightings added 2026-07-22):**

- [[patterns/behavioral/evidence-gated-completion]] — an agent can't self-declare *done*; completion is gated on an external verification surface, and budget-exhaustion ≠ done. **Promoted proposed→confirmed 2026-06-20:** [[artifacts/projects/codex-goals]] (OpenAI) + [[artifacts/skills/loop-library]] (Forward Future) + **[[artifacts/projects/eve]] (Vercel — 3rd creator: the team's "nothing is done until tests pass" / "say so explicitly rather than claiming verification passed" dev-discipline gate + evals as a shipped primitive)**.

- [[patterns/behavioral/persona-lens-review-panel]] — review via parallel narrow persona/lens reviewers (read-only, partial by design, structured returns) merged by an orchestrator. pm-os (9-reviewer PRD panel) + compound-engineering (`/ce-code-review` JSON merge) + gstack (lens-as-slash-command). **New + confirmed at creation 2026-06-11** — three creators, three verticals.

- [[patterns/composition/single-source-multi-surface-distribution]] — one definition, many surfaces (reference *or* convert *or* run-natively; never hand-fork). financial-services (Cowork + Managed Agents API), gbrain (CLI + MCP + skillpack), compound-engineering (→ ~11 competing harnesses via a converter), openai-codex-plugins (plugin-eval = CLI+plugin; superpowers runs on Codex+Claude Code with **no transform** — **new mechanism 2026-06-02**), pm-os (**naming-adaptation variant** — per-surface prefix/namespace builds, 2026-06-11) + **eve (the framework-level "channels" variant — one agent → web/Slack/Discord/Teams/Telegram/Twilio/GitHub/Linear/CLI/cron; + docs-as-source bundled in the npm package; 2026-06-20 → 6 examples, 5 creators)**.
- [[patterns/structural/marketplace-as-multi-plugin]] — one repo's `marketplace.json` registers N à-la-carte plugins. financial-services (20), anthropic-skills-marketplace (3), **openai-codex-plugins (167 — first non-Claude-Code, makes the pattern cross-lab 2026-06-02)**.
- [[patterns/quality-bar/skill-pack-bundle]] — a skill ships as a *tested bundle*; "a skill pack has tests." gstack + gbrain + compound-engineering (~1,094 tests incl. behavioral *contract* tests). **Same-creator caveat retired 2026-06-02** (CE is non-Garry, two ecosystems); residue: the *resolver eval* sub-part stays Garry-best. **Counter-bet 2026-06-19:** [[artifacts/plugins/mattpocock-skills]] (135K★, *zero* tests) bets radical smallness + predictability-by-construction against the tested bundle.
- [[patterns/composition/resolver-routing-table]] — a *tested* routing table (intent→which skill/doc); trigger evals + `check-resolvable`, fractal across layers. gbrain + gstack + **pm-os (first non-Garry explicit table at 235-skill scale, 2026-06-11; adds the per-response routing declaration — but ships no routing eval, so the tested half stays ⚠ same-creator)** + **mattpocock `ask-matt` (2026-06-19 — 2nd non-Garry table, triggered by *invocation type* not scale; also no eval; 3 non-Garry build, none test)**.
- [[patterns/behavioral/latent-vs-deterministic-split]] — every step is model-judgment or same-in/same-out; put each on the right side. gstack + gbrain + compound-engineering (states the rule: "skills are guardrails… calibrate prescription to the failure mode") + pm-os (PM-vertical: deterministic hook detection + single-writer memory scripts, 2026-06-11). **Same-creator caveat retired 2026-06-02.** **Supporting sighting 2026-07-22:** skill-diffs (a dataset pipeline's own linter/quality-score vs. its LLM-classify/judge tooling — first sighting outside an agent harness).
- [[patterns/quality-bar/complexity-ratchet]] — every session adds tests/docs/evals that reload into context, so the quality floor only rises (forward-only). gstack + gbrain + compound-engineering (`docs/solutions/` knowledge ratchet + branch-protection floor). **Promoted proposed→confirmed 2026-06-02** — CE is the independent non-Garry example; [[concepts/compound-engineering]] names the principle independently. **Supporting sighting 2026-07-22:** skill-diffs (the ratchet applied to a dataset's versioned enrichment chain, not a codebase).
- [[patterns/quality-bar/version-as-update-gate]] — `version` is the update-delivery trigger (installs resolved by version), so release-automation owns it and hand-bumps are forbidden. financial-services (pre-commit hook) + compound-engineering (release-please + `linked-versions`) + **eve (changesets on the **npm registry** substrate — a *different* delivery substrate than the plugin file-cache, 2026-06-20 → 3 examples)**. **Confirmed 2026-06-02.**
- [[patterns/behavioral/skill-as-method-call]] — a skill/command file is a parameterized procedure; same file, different arguments → different capability. **Promoted 2026-06-02**: gstack (`/qa` tiers, `/investigate`) + [[artifacts/projects/codex-goals]] (the `/goal` six-slot signature — non-Garry, on the Codex CLI).

**Proposed, with a dedicated page:**

- [[patterns/structural/thin-harness-fat-skills]] — portable workflow judgment can live in Markdown while runtime responsibilities remain in code. [[artifacts/projects/eve]] and [[artifacts/projects/humanlayer]] expose substantial lifecycle, recovery, and authorization infrastructure: separation is supported; literal “thinness” is not. Remains **proposed** pending a sharper invariant and evidence for it, rather than promotion by counting another runtime.
- [[patterns/behavioral/diarization]] — read everything about a subject, write one structured page of distilled judgment (the "says vs actually building" gap). gbrain `enrich/` + brain-page schema.
- [[patterns/behavioral/session-start-directive]] — session-start hooks must emit *imperative, position-pinned, persistence-bounded* directives, not passive context (which the model silently absorbs); one directive per session. Grounded in pm-os's hooks, which carry their own before/after failure evidence (issue #8). **New (proposed) 2026-06-11.**
- [[patterns/quality-bar/defect-derived-validation]] — build a validation/lint rule set by mining what real maintainers actually fixed across a historical corpus, then validate the rule set itself by running it back over the corpus and reporting hit rates. Grounded in skill-diffs' `skill_linter.py` (rules derived from real merged-commit PR titles; 61% of ~665k skills trigger ≥1 finding). **New (proposed) 2026-07-22.**
- [[patterns/structural/authoritative-recheck-after-notification]] — For the inspected V2 launch path, replicated state wakes an actor that fetches authoritative readiness and acquires scoped ownership. HumanLayer only; proposed.
- [[patterns/quality-bar/revision-bound-review]] — Bind review state and comment targets to the content revision they concern; distinguish local review markers, shared feedback, and approval. HumanLayer only; proposed.

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
- *New from compound-engineering (1 example each; see [patterns/_index.md](patterns/_index.md)):* skill-self-containment for portability · cross-platform-portable skill authoring · dedup-before-create · legacy-artifact cleanup registry · auto-invoke trigger phrases · ~~persona/lens multi-agent review panel~~ → **promoted** to [[patterns/behavioral/persona-lens-review-panel]] (3rd example: pm-os, 2026-06-11)
- *New from pm-os (1 example each, tracked on [[artifacts/plugins/pm-os]]):* pre-flight attestation block · context-guard onboarding gate · deliverable gate / coach-not-doer enforcement · plugin/workspace split as upgrade architecture
- *New from mattpocock (tracked on [[artifacts/plugins/mattpocock-skills]]):* **align-before-execute** (grill before building) · invocation-type-triggered router (`ask-matt`) · the **skill-pack-bundle counter-bet** (135K★ pack, no tests) · 2 new concepts ([[concepts/skill-invocation-axis]], [[concepts/ubiquitous-language-for-agents]])
- Audience-segmented skill output (financial-services / S&P)

See [patterns/_index.md](patterns/_index.md) for the per-category breakdown.

## Analyses

*(none yet — see [analyses/_index.md](analyses/_index.md) for the rule of "no synthesis until ≥5 artifacts of relevant type")*

## Meta

- [[_schemas/project]] — project investigation template; distinguish code, test inspection/execution, prompt policy, documentation, and inference.

The wiki applied to itself — improvements to our own machinery, each traced to a pattern observed in the wiki (the [REFLECT](CLAUDE.md) operation).

- [[meta/self-improvements]] — self-improvement ledger; applied/embodied wiki machinery changes traced to observed patterns and concepts, including routing, doctor tooling, page definitions of done, consumer-agent guidance, portability, and release/versioning principles.
