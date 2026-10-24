---
domain: sources
type: other # zip release — paid product distributed as a ZIP, not a public repo; see Snapshot details
url: https://www.prodmgmt.world/ai-pm-os
retrieved: 2026-06-11
snapshot-location: sources/prodmgmt-world--pm-os-cowork/
upstream-commit: n/a (release artifact; version 2.2.1)
last-reviewed: 2026-06-11
---

# PM OS for Claude Cowork — v2.2.1 (beta) release ZIP

> The complete Cowork distribution of **PM OS**, prodmgmt.world's paid ($99 one-time) "Product
> Manager AI Operating System": a 235-skill / 12-agent / 2-hook Claude plugin **plus** a paired
> workspace folder (Context + Knowledge + Templates + Examples) governed by a 364-line AGENTS.md
> harness. Our first *paid, ZIP-distributed* source and first PM-vertical (non-engineering) pack.

*Done when it passes the [page checklist](_definition-of-done.md).*

## Snapshot details

- **Retrieved**: 2026-06-11 (user-uploaded `pm-os-cowork-2.2.1.zip`; Sid holds the license)
- **Where it lives in this wiki**: `sources/prodmgmt-world--pm-os-cowork/` — the original ZIP plus its
  extracted tree: `README.md` (install guide), `plugin/` (the `pm-os.zip` plugin contents: 235 skills,
  12 agents, 2 hooks, `.mcp.json`), `workspace/` (CLAUDE.md harness + 📂 Context / 🧠 Knowledge /
  📄 Templates / 💎 Examples).
- **Upstream URL**: https://www.prodmgmt.world/ai-pm-os (product page). Development repo `gnurio/pm-os`
  is referenced in hook comments (issues #8, PR #10) but is **not public** — this ZIP is the only
  evidence we can hold, which is why the extracted tree is committed (not reconstructable, unlike repo
  clones).
- **Upstream identifier**: version `2.2.1` (from `.claude-plugin/plugin.json`); inner files dated
  2026-06-08.
- **Snapshot storage note**: this source fits neither manifest row exactly — it's repo-shaped material
  with no clonable upstream. Treated like an article snapshot: committed, immutable, never edited.

## Anchor map

- `#root` — the source as a whole
- `#readme` — top-level `README.md`: 2-step Cowork install, upgrade path, known limitations vs Claude Code, "Cowork org marketplaces intentionally NOT used (paid product; licensing model)"
- `#plugin.json` — `plugin/.claude-plugin/plugin.json`: name/version/description ("237 PM skills (13 system + 10 workflows + 214 reusable), 10 sub-agents, 2 SessionStart hooks")
- `#mcp.json` — `plugin/.mcp.json`: 6 bundled MCP servers (lenny-podcast, notion, linear, atlassian, github, perplexity)
- `#hooks.json` — `plugin/hooks/hooks.json`: SessionStart matcher `startup|resume` → 2 shell hooks
- `#tidy-reminder` — `plugin/hooks/tidy-reminder.sh`: drift detection + the `[SESSION-START DIRECTIVE]` imperative payload; comment documents that passive phrasing "was being silently absorbed by the LLM" (issue #8)
- `#drip-reminder` — `plugin/hooks/drip-reminder.sh`: tapering-cadence nudge; defers to tidy ("only one nudge directive per session"); "the hook never mutates state"
- `#agents-md` — `workspace/CLAUDE.md` (titled "AGENTS.md"): the 364-line harness; rule engine diagram, 5 Non-Negotiable Rules
- `#pre-flight` — workspace/CLAUDE.md "MANDATORY PRE-FLIGHT": ✓/✗ attestation block required at the start of every substantive response
- `#context-guard` — workspace/CLAUDE.md "Context Guard": placeholder check blocks all work until `/start` fills Context; `/dev` escape hatch
- `#project-awareness` — workspace/CLAUDE.md "Project Awareness": `.current` multi-active project slugs, nested slugs, save destinations, prior-work scan, memory preflight via `bin/memory/*.sh`
- `#knowledge-routing` — workspace/CLAUDE.md "Knowledge Routing": topic → workflow → skill file → Knowledge files table
- `#slash-skills` — workspace/CLAUDE.md "Slash Skills": commands→skills migration story; per-distribution prefix table (Claude Code / Cowork / Cursor)
- `#plugin-architecture` — workspace/CLAUDE.md "Plugin Architecture": registry update rule, breadboard regeneration gate, changelog guard, 8 pre-release validation scripts
- `#mcp-servers-doc` — workspace/CLAUDE.md "MCP Servers": per-server auth/transport table; "Slack is intentionally not bundled" rationale
- `#scope-rule` — workspace/CLAUDE.md "Scope": declines non-professional requests with a fixed sentence
- `#journalist-spy` — workspace/CLAUDE.md "PM Thinking Partner": Rule 4, "ask the question that makes them see it themselves"; deliverable gate (Rule 3)
- `#pm-workflows-agent` — `plugin/agents/pm-workflows.md`: I/O contract (Inputs / Allowed reads / Writes / Output format / Failure behavior)
- `#reviewer-agents` — the 9 read-only reviewer agents (`devils-advocate-reviewer.md` etc.): `readonly: true`, shared STATUS/SCOPE/FINDINGS output format
- `#prd-workflow` — `plugin/skills/prd/SKILL.md`: 9-step PRD construction; subagent execution contract with inline-persona fallback
- `#pm-os-start` — `plugin/skills/pm-os-start/SKILL.md`: onboarding; per-platform structured-question tool table (Cursor `AskQuestion` vs Claude Code `AskUserQuestion`)
- `#strategy-workflow` — `plugin/skills/strategy/SKILL.md`: 4-step skill-chained workflow; lenny-podcast MCP optional enrichment
- `#knowledge-index` — `workspace/🧠 Knowledge/INDEX.md`: 118 frameworks / 50 prioritization / 100 interview questions / 41 north-star examples / 25 drills / 260 Lenny articles
- `#templates-examples` — `workspace/📄 Templates/` (7 PRD formats) + `workspace/💎 Examples/` (2 example PRDs, "calibrate evidence quality, not format")

## Why we cite this

- Claims about how a **paid, vertical (PM), non-engineering** skill pack is structured, gated, and distributed.
- The **imperative session-start directive** hook technique (and its documented passive-phrasing failure).
- The **mandatory pre-flight attestation block** and **Context Guard** harness-enforcement techniques.
- Multi-surface packaging (Claude Code / Cowork / Cursor) and its naming-prefix workarounds.
- Release-gate machinery referenced in `#plugin-architecture` (registry/breadboard/changelog validators) — *referenced but not shipped in this ZIP* (`bin/` lives in the private dev repo), so cite as the harness's stated rules, not as verified scripts.

## Popularity signals

- **Signal type**: price + positioning — **$99 one-time** paid product; prodmgmt.world's own plugin roundup notes it's the only paid one of the ten listed. **As-of**: 2026-06-11. Source: [prodmgmt.world/ai-pm-os](https://www.prodmgmt.world/ai-pm-os), [plugin roundup](https://www.prodmgmt.world/resources/claude-code/plugins).
- **Signal type**: release velocity — public version series 1.4 (2026-03) → 1.7 (2026-04) → 2.0 "The Memory Loop" (2026-05) → 2.2.1 (2026-06), each with a Substack writeup ([nurijanian.substack.com](https://nurijanian.substack.com/p/pm-os-v2-the-memory-loop)). **As-of**: 2026-06-11.
- **Signal type**: creator reach — George Nurijanian (@nurijanian) promotes via X + Substack; no public install counts (private repo, ZIP distribution), so adoption is **unverifiable** — flag, don't claim. **As-of**: 2026-06-11.

## Related sources

- [[sources/garrytan--gstack]] — the closest structural sibling: opinionated solo-auteur pack, but free, public, engineering-vertical.
- [[sources/every--compound-engineering-plugin]] — the other multi-surface, registry-gated pack; PM OS cites the same commands→skills migration pressure.
- [[sources/anthropic--plugins-reference]] — the plugin mechanism (hooks.json, `${CLAUDE_PLUGIN_ROOT}`, `.mcp.json`) PM OS rides on.
- [[sources/agentskills--specification]] — PM OS's SKILL.md frontmatter (`name` + "Use when…" description) conforms to the standard.
