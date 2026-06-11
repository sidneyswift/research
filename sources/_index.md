---
domain: sources
type: index
last-reviewed: 2026-05-21
---

# Sources

Primary evidence backing every claim in the wiki. Snapshotted, not just linked. Each source page uses [../_schemas/source.md](../_schemas/source.md).

## Citation convention

Wikilinks to sources use **anchors that are defined on the source page itself**. Don't invent anchor names ad-hoc — register them in the source's "Anchor map" section first.

✅ `[[sources/anthropic--skills#SKILL.md-L1-L20]]`
✅ `[[sources/joe-dev--my-skill-pack#manifest]]`
❌ `[[sources/anthropic--skills#somewhere-near-the-top]]` — anchor not registered

## Cloned repos

Repos sit at `sources/<creator>--<repo>/` (the actual git clone, `.git/` stripped) and have a corresponding `sources/<creator>--<repo>.md` page that is the citation target.

- [[sources/anthropic--skills]] — `anthropics/skills` (11 MB, commit `690f15c` of 2026-05-19). The official Anthropic skills + spec + template.
- [[sources/garrytan--gstack]] — `garrytan/gstack` (41 MB, commit `029356e` of 2026-05-20). Garry Tan's 23-skill engineering-team pack.
- [[sources/garrytan--gbrain]] — `garrytan/gbrain` (71 MB, commit `1580c6d` of 2026-05-20, version 0.36.4.0). Garry Tan's memory system.
- [[sources/anthropic--financial-services]] — `anthropics/financial-services` (2.7 MB, commit `120a31d` of 2026-05-29, Apache 2.0). Anthropic's FSI reference marketplace — 20 plugins, dual-runtime (Cowork plugin + Managed Agents API), 10 managed-agent cookbooks with trust-tiered subagents.
- [[sources/every--compound-engineering-plugin]] — `everyinc/compound-engineering-plugin` (11 MB, commit `3e77a7b` of 2026-06-01, MIT). Every's official Compound Engineering plugin — 38 skills + 43 sub-agents authored once in Claude format and converted to ~11 agent platforms; dogfoods its own loop (27 brainstorms + 57 plans + 30 solutions). The wiki's first **non-Garry tested skill pack**.
- [[sources/openai--plugins]] — `openai/plugins` (57 MB, 4,580 files, commit `bebc3d6` of 2026-06-01, 1,334★). OpenAI's official **Codex** plugin marketplace — **167 plugins** (mostly hosted-connector `.app.json` wrappers + 479 skills), the `.codex-plugin/` manifest with a productized storefront, the `plugin-creator` meta-skill. The wiki's first **non-Claude-Code / non-Anthropic** marketplace; grounds [[concepts/convergent-agent-plugin-spec]].

## Articles, posts, threads

External writing we cite. Always include retrieval date and a snapshot path (PDF / screenshot / archive.org URL).

**Garry Tan's "AI Explainer" series (8 essays, @garrytan, ~April–May 2026).** Retrieved 2026-06-01; each held verbatim at `sources/garrytan--<slug>/snapshot.md`. A longitudinal record of building `gstack`/`gbrain` (gstack stars climb 72K→75K→87K→93K→105K across the run, gbrain 14K→20K) and the source for the series' patterns. ⚠ Canonical URLs + exact dates are TODO (estimated from internal evidence).

- [[sources/garrytan--thin-harness-fat-skills]] — **#1** *"Thin Harness, Fat Skills"* — the architecture overture: five primitives (skill files, thin harness, resolvers, latent-vs-deterministic, diarization) + the three-layer model. (~Apr 2026; cites the 2026-03-31 Claude Code npm leak.)
- [[sources/garrytan--resolvers]] — **#2** *"Resolvers: The Routing Table for Intelligence"* — the resolver as the governance layer (trigger evals, `check-resolvable`, fractal resolvers). (gstack 72K stars.)
- [[sources/garrytan--loc-controversy]] — **#3** *"On the LOC controversy"* — defends the 600K-LOC/60-day claim with deflation math + quality data (reverts, slop-scan, tests). (~2026-04-18, "day 108"; gstack 75K stars / 14,965 installs.)
- [[sources/garrytan--naked-models]] — **#4** *"Naked Models Are Stupider"* — rebuttal to Kyle Kingsbury (Jepsen): the model is the engine, the harness is the car. (cites the 512K-line Claude Code leak.)
- [[sources/garrytan--skillify-manifesto]] — **#5** *"How to really stop your agents from making the same mistakes"* — the 10-step skillify checklist; LangChain-vs-workflow critique; GBrain-vs-Hermes. The richest [[patterns/quality-bar/skill-pack-bundle]] articulation.
- [[sources/garrytan--meta-meta-prompting]] — **#6** *"Meta-Meta-Prompting"* — compounding skills + diarization at scale (book-mirror, 100K-page brain). Credits Karpathy's LLM Wiki (this wiki's own pattern) as GBrain's inspiration. (gstack 87K stars.)
- [[sources/garrytan--complexity-ratchet]] — **#7** *"The AI Agent Complexity Ratchet"* — 90% coverage as the AI-affordable threshold; everything-harnessable-is-testable. (2026-05-12; gstack 93K stars / 701K LOC.)
- [[sources/garrytan--foxconn-factories]] — **#8** *"Stop building Foxconn factories for your agents"* — the skill-pack primitive, "just-in-time software," "tokenmaxxing," the verified ~105K-star figure, and the OpenClaw=Steinberger correction.

**Every — compound engineering.** Kieran Klaassen (GM of Cora) + Dan Shipper (CEO); the methodology's origin and home. ⚠ Partial captures (`every.to` is a subscription publication) — confirmed metadata + verbatim fragments + outline; full-text paste is TODO.

**Anthropic — dynamic workflows.** The first official Anthropic technical deep-dive on how the Claude Code harness works, by Thariq Shihipar and Sid Bidasaria (Anthropic Claude Code team). Published 2026-06-02.

- [[sources/anthropic--dynamic-workflows]] — **article** (X article + Claude Blog mirror), Thariq Shihipar (@trq212) + Sid Bidasaria (@sidbid), 2026-06-02. "A harness for every task: dynamic workflows in Claude Code" — model writes JS harness on the fly, 6 composable orchestration patterns, 3 named failure modes. 3,340 likes / 7,574 bookmarks. Grounds [[concepts/dynamic-workflows]].

- [[sources/every--compound-engineering-gets-an-upgrade]] — **article**, Kieran Klaassen, 2026-05-29 (updated 2026-06-01). The 4-step → 8-step evolution; "AI is the stuff in the middle. Humans are the bread on either end."

## Marketplace listings

Marketplace pages capture install counts, ratings, descriptions — popularity signals decay so we capture values *at retrieval date*.

*(none yet)*

## Purchased / proprietary bundles

Paid products studied under license. Raw content is held **locally outside the wiki** (never committed — republishing paid material); the citation page anchors claims to file paths inside the licensed copy.

- [[sources/prodmgmt-world--pm-os]] — **purchased bundle** (PM OS 2.2.1, prodmgmt.world, retrieved 2026-06-10). 235 skills + 12 sub-agents + 2 hooks + 6 MCP configs, shipped as claude-code + cursor + cowork zips. Grounds [[artifacts/plugins/pm-os]]. The wiki's first paid proprietary source.

## Social

Tweets, Reddit threads, HN comments. Capture full text + author + date.

- [[sources/ahrefs--ai-search-optimization-research]] — **tweet** (+ LinkedIn cross-post), Tim Soulo (@timsoulo, CMO of Ahrefs), 2026-06-02. Synthesis of 14 Ahrefs studies analyzing 1 billion data points on AI search optimization — how ChatGPT, AI Overviews, and AI Mode cite web content. 2,576 likes / 5,348 bookmarks. Grounds [[concepts/ai-search-as-parallel-discovery-layer]].

## Docs

Official Anthropic / Cowork / vendor docs we cite as authoritative. Living pages — pin claims to the retrieval date.

- [[sources/anthropic--plugins-reference]] — Claude Code "Plugins reference" (`code.claude.com/docs`, retrieved 2026-05-31). The mechanism layer: `plugin.json` schema, `${CLAUDE_PLUGIN_ROOT}` file resolution, and the `~/.claude/plugins/cache` caching behavior. Partial verbatim snapshot.
- [[sources/every--compound-engineering]] — Every's living "Compound Engineering" guide (`every.to/guides`, retrieved 2026-06-02; **partial capture**). The loop, the 80/20 + 50/50 rules, the eight beliefs to "unlearn," "taste belongs in systems, not review," the 5-stage adoption ladder.
- [[sources/openai--using-goals-in-codex]] — OpenAI Cookbook guide *"Using Goals in Codex"* (`developers.openai.com/cookbook`, retrieved 2026-06-02; captured verbatim from the notebook source). Pinned to `openai/openai-cookbook` commit `9b4e627` (2026-05-13; page published 2026-05-09, authors Raj Pathak & Stefano Fabbri). Documents Codex **Goals** — persistent, evidence-gated objectives via `/goal`. The wiki's first **OpenAI** source.
