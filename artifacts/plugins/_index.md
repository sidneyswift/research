---
domain: artifacts
type: index
subdomain: plugins
last-reviewed: 2026-05-21
---

# Plugins

Claude Code plugins cataloged. Each page uses [../../\_schemas/plugin.md](../../_schemas/plugin.md).

## By creator

### Anthropic official
- [[artifacts/plugins/anthropic-skills-marketplace]] — Anthropic's demonstration marketplace; 3 child plugins, 17 skills. The reference for "what a skill looks like."
- [[artifacts/plugins/anthropic-financial-services-marketplace]] — Anthropic's FSI reference marketplace; 20 plugins (7 vertical + 10 agent + 2 partner + 1 installer), dual-runtime (Cowork plugin + Managed Agents API), trust-tiered subagents. The most architecturally ambitious artifact in the wiki.

### Cowork marketplace
*(none yet)*

### Community / individual
- [[artifacts/plugins/gstack]] — Garry Tan's opinionated 23-skill engineering-team pack
- [[artifacts/plugins/gbrain]] — Garry Tan's three-shape (CLI + MCP + skillpack) memory system

## By target user

### Engineering
- [[artifacts/plugins/gstack]]

### Vertical (domain-specific workflows)
- [[artifacts/plugins/gbrain]] — agent memory
- [[artifacts/plugins/anthropic-financial-services-marketplace]] — financial services (IB, equity research, PE, wealth, fund admin, ops)

### Reference / demonstration
- [[artifacts/plugins/anthropic-skills-marketplace]]
- [[artifacts/plugins/anthropic-financial-services-marketplace]] — also a reference set (tunable templates, not turnkey production)

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

- `garrytan/openclaw` — agent platform that gbrain primarily targets (referenced in gbrain manifest)
- `garrytan/hermes` — sibling agent deployment to OpenClaw
- `peter-steinberger/openclaw` — confusion: there's another `openclaw` with 247K stars per gstack README; need to verify which is which
- *Adjacencies to add after gstack deep-dive*: TBD (per hybrid mode)
- *Adjacencies to add after gbrain deep-dive*: TBD
