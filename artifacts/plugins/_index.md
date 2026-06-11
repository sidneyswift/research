---
domain: artifacts
type: index
subdomain: plugins
last-reviewed: 2026-05-21
---

# Plugins

Agent plugins cataloged — **Claude Code *and* Codex** as of 2026-06-02. Each page uses [../../\_schemas/plugin.md](../../_schemas/plugin.md). The two labs' plugin formats are near-identical (see [[concepts/convergent-agent-plugin-spec]]).

## By creator

### Anthropic official
- [[artifacts/plugins/anthropic-skills-marketplace]] — Anthropic's demonstration marketplace; 3 child plugins, 17 skills. The reference for "what a skill looks like."
- [[artifacts/plugins/anthropic-financial-services-marketplace]] — Anthropic's FSI reference marketplace; 20 plugins (7 vertical + 10 agent + 2 partner + 1 installer), dual-runtime (Cowork plugin + Managed Agents API), trust-tiered subagents. The most architecturally ambitious artifact in the wiki.

### Cowork marketplace
*(none yet)*

### Community / individual
- [[artifacts/plugins/gstack]] — Garry Tan's opinionated 23-skill engineering-team pack
- [[artifacts/plugins/gbrain]] — Garry Tan's three-shape (CLI + MCP + skillpack) memory system

### Every (Kieran Klaassen)
- [[artifacts/plugins/compound-engineering]] — the official Compound Engineering plugin; 38 skills + 43 sub-agents, authored once in Claude format and **converted to ~11 agent platforms**; dogfoods its own loop. The wiki's first **non-Garry tested skill pack**. (Marketplace also ships `coding-tutor` by Nityesh Agarwal — candidate below.)

### prodmgmt.world (commercial)
- [[artifacts/plugins/pm-os]] — paid, proprietary PM bundle (v2.2.1): 235 skills in a three-tier hierarchy (system/workflow/reusable), 12 read-only reviewer/router sub-agents, 2 nudge-only hooks, 6 MCP configs; one content set shipped as claude-code + cursor + cowork zips. The wiki's first **purchased** artifact — evidence the skill-pack format has a paid market.

### OpenAI (Codex — *not* Claude Code)
- [[artifacts/plugins/openai-codex-plugins-marketplace]] — OpenAI's official **Codex** marketplace; **167 plugins** (mostly hosted-connector `.app.json` wrappers + a skills layer; 479 skills total), `.codex-plugin/` manifest with a productized storefront (categories, install/auth policy, `codex://` deeplinks), `plugin-creator` meta-skill. The wiki's first non-Claude-Code marketplace; the example that makes [[patterns/structural/marketplace-as-multi-plugin]] cross-lab. ~140 of 167 are partner-authored.

## By target user

### Engineering
- [[artifacts/plugins/gstack]]
- [[artifacts/plugins/compound-engineering]] — agent-coding workflow loop (brainstorm → plan → work → review → compound)

### Vertical (domain-specific workflows)
- [[artifacts/plugins/gbrain]] — agent memory
- [[artifacts/plugins/anthropic-financial-services-marketplace]] — financial services (IB, equity research, PE, wealth, fund admin, ops)

### Reference / demonstration
- [[artifacts/plugins/anthropic-skills-marketplace]]
- [[artifacts/plugins/anthropic-financial-services-marketplace]] — also a reference set (tunable templates, not turnkey production)
- [[artifacts/plugins/openai-codex-plugins-marketplace]] — "a curated collection of Codex plugin examples"; the reference for *what a Codex plugin looks like*

## Candidate list

Promote candidates to full pages above when deep-dived. Otherwise leave as one-liners.

**`claude-for-financial-services` children** (all inside [[sources/anthropic--financial-services]]; the marketplace is paged, the children are not yet). Highest-value deep-dives first:

- `gl-reconciler` (agent) — `plugins/agent-plugins/gl-reconciler/` + cookbook `managed-agent-cookbooks/gl-reconciler/`. Already used as the worked example on the marketplace page; best single illustration of trust-tiered subagents. **Deep-dive first.**
- `financial-analysis` (vertical, core) — `plugins/vertical-plugins/financial-analysis/`. 13 skills + 7 commands + all 12 connectors; the dependency every agent assumes.
- `kyc-screener` (agent) — untrusted-document handling for onboarding packets; another trust-tier exemplar.
- `pitch-agent` / `model-builder` / `earnings-reviewer` / `market-researcher` / `meeting-prep-agent` / `valuation-reviewer` / `month-end-closer` / `statement-auditor` (agents) — the other 8 named agents; each = system prompt + bundled skills + 3-worker cookbook.
- `investment-banking` / `equity-research` / `private-equity` / `wealth-management` / `fund-admin` / `operations` (verticals) — domain skill+command bundles.
- `lseg` / `sp-global` (partner-built) — partner-authored; LSEG wraps its own MCP into command↔skill pairs, S&P ships per-skill licensing + audience-segmented `tear-sheet`.
- `claude-for-msft-365-install` — Claude-Code-only admin installer; the deliberate single-surface counter-example.

**`compound-engineering-plugin` children/siblings** (inside [[sources/every--compound-engineering-plugin]]; the plugin is paged, these are not yet):

- `coding-tutor` (plugin, by **Nityesh Agarwal**) — the 2nd plugin in Every's marketplace; 3 commands (`teach-me` / `quiz-me` / `sync-tutorials`) + 1 skill; spaced-repetition coding tutorials. A non-Kieran, non-workflow plugin in the same repo — useful contrast.
- High-value CE skills to deep-dive: `ce-compound` (the compounding mechanism; worked example on the marketplace page), `ce-code-review` (parallel persona lenses → JSON → dedup → confidence gate), `ce-plan`, `ce-work`, `ce-strategy` (the `STRATEGY.md` anchor).

**`openai/plugins` children** (inside [[sources/openai--plugins]]; the marketplace is paged, these are not yet). Highest-value deep-dives first:

- `figma` (`#figma`) — **the richest plugin**; exercises every primitive (7+ skills, real agent `.md`, commands, the repo's only `hooks.json` parity check, `.app.json`, a `ui/` workbench). **Deep-dive first** for the full Codex plugin shape.
- `plugin-eval` (`#plugin-eval`) — **meta-plugin that scores other plugins** (token budgets, baselines, benchmark harness, result schema; CLI + plugin). Mine its `references/` for our own eval gate (see [[meta/self-improvements]]).
- `superpowers` (`#superpowers`) — Jesse Vincent's (obra's) framework ported to Codex; the **same skills run in Claude Code** — the in-wiki proof of cross-runtime portability ([[concepts/convergent-agent-plugin-spec]]).
- `build-ios-apps` / `cloudflare` (`#mcp-json`) — the **2 plugins using raw `.mcp.json`** (local stdio `xcodebuildmcp` vs remote HTTP `mcp.cloudflare.com`); the connector-taxonomy edge cases.
- `twilio-developer-kit` (55 skills) / `zoom` (53) / `life-science-research` (50) / `vercel` (47) — the **skill-library** end of the spectrum (`#build-kits`), vs thin connector wrappers like `linear`.

- `garrytan/openclaw` — agent platform that gbrain primarily targets (referenced in gbrain manifest)
- `garrytan/hermes` — sibling agent deployment to OpenClaw
- `peter-steinberger/openclaw` — confusion: there's another `openclaw` with 247K stars per gstack README; need to verify which is which
- *Adjacencies to add after gstack deep-dive*: TBD (per hybrid mode)
- *Adjacencies to add after gbrain deep-dive*: TBD
