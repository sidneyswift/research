---
domain: artifacts
type: plugin
name: pm-os
creator: "[[creators/prodmgmt-world]]"
source: "[[sources/prodmgmt-world--pm-os]]"
ecosystem: cross-lab # ships claude-code + cursor + cowork variants of one content set
discovered-via: other # purchased (Sidney bought it for study, 2026-06-10)
marketplace-listing: https://prodmgmt.world
status: active
last-reviewed: 2026-06-10
components:
  skills: 235 # 13 system + 11 sequenced workflow + 211 reusable
  commands: 0 # deliberately zero — "Skills, not commands — per Anthropic's plugin guidance"
  agents: 12
  hooks: 2
  mcp-servers: 6
popularity-signals:
  - signal: commercial-product
    value: paid product, no public install counts
    as-of: 2026-06-10
    source: "[[sources/prodmgmt-world--pm-os#root]]"
---

# pm-os

> **One-line:** a paid, proprietary "operating system" for product managers — 235 PM skills, 12 reviewer/router sub-agents, and 2 nudge hooks, shipped as parallel Claude Code, Cursor, and Cowork packages from one content set.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): read everything about the plugin, then write distilled judgment — not a transcription of its README. Done when it passes the [page checklist](_definition-of-done.md).*

## Attributes

- **What it does**: turns a coding agent into a PM copilot — write PRDs/strategy docs through sequenced workflows, review any product doc through multi-persona sub-agents, maintain a PM "memory" folder convention with hook-driven tidy/drip rituals.
- **Target user**: working product managers at SaaS companies (stakeholder management, exec comms, roadmap politics are heavily represented), secondarily founders.
- **Component inventory** ([[sources/prodmgmt-world--pm-os#plugin-manifest]]):
  - **13 system skills** (`pm-os-*`): start, pm-help, pm-status, upgrade, tidy, project, capture-memory, daily-drip, import-ai-memory, framework, skill, feedback, testimonial — the "OS" layer: onboarding, maintenance, memory.
  - **11 sequenced workflow skills**: strategy, opportunity, assumptions, research, decisions, stakeholder, meeting, pm-review, coaching, measure, prd — multi-step rituals that chain the reusable skills.
  - **211 reusable skills**: one technique each (jtbd-forces, seven-powers, mom-test-guide, press-release, tradeoff-matrix, …) with canonical short names ([[sources/prodmgmt-world--pm-os#skills-dir]]).
  - **12 sub-agents** ([[sources/prodmgmt-world--pm-os#agents-dir]]): a `pm-workflows` router, `knowledge-librarian`, `context-manager`, 7 cross-functional review personas (engineering, design, legal-risk, executive, UX-research, customer-voice, devil's-advocate), 2 PRD-specific reviewers (flaws = harsh critic, strengths = optimist). All read-only with an explicit I/O contract (STATUS / SCOPE / FINDINGS / OPEN_QUESTIONS / RECOMMENDED_NEXT_ACTION).
  - **2 SessionStart hooks** ([[sources/prodmgmt-world--pm-os#hooks]]): `tidy-reminder.sh` and `drip-reminder.sh` — shell scripts that inspect state files under the user's `📂 Context/Work/` folder and emit a session-start directive nudging `/tidy` or `/daily-drip`. Hooks never mutate state; a separate `bin/` script is the only writer.
  - **6 MCP servers** ([[sources/prodmgmt-world--pm-os#mcp-config]]): lenny-podcast (custom HTTP server — searchable Lenny's Podcast transcript corpus), notion, linear, atlassian, github, perplexity (all standard hosted/stdio servers).
- **Install footprint**: content-only (markdown + 2 shell scripts + JSON configs); no npm deps. MCP servers require per-service auth. ~2.5 MB of skills.
- **Plugin layout**: `.claude-plugin/plugin.json`, `skills/` (235 dirs), `agents/` (12 md), `hooks/`, `.mcp.json`, `registry/` (machine-readable JSON index of all components + CAPABILITIES.md), plus content dirs (`🧠 Knowledge/` frameworks, `📄 Templates`, `💎 Examples`, `📂 Context` user-workspace convention).
- **License**: Proprietary (paid product).

## Relationships

- **Creator**: [[creators/prodmgmt-world]]
- **Source**: [[sources/prodmgmt-world--pm-os#root]]
- **Composes**: 235 bundled skills (none individually paged; candidates: the `prd` workflow + reviewer-agent system are the standouts)
- **Depends on**: 6 MCP servers (only lenny-podcast is first-party; rest are standard Notion/Linear/Atlassian/GitHub/Perplexity)
- **Marketplace neighbors**: [[artifacts/plugins/compound-engineering]] (the engineering-domain analog: big skill pack + sub-agents + multi-platform conversion), [[artifacts/plugins/gstack]] (opinionated single-domain pack)

## What problem it solves

"Every PM deliverable, on tap, with taste." The bundle earns coherence three ways: (1) the 11 workflow skills *sequence* the 211 reusable skills into rituals rather than leaving a grab-bag; (2) the 12 sub-agents give every document a standing multi-perspective review board; (3) the system skills + hooks maintain a persistent PM workspace (projects, memory, tidiness) across sessions. It is closer to a *product* than a skill dump — versioned (2.2.1, CHANGELOG, upgrade skill), onboarded (`pm-os-start`), and monetized.

## Composition strategy

- **Three-tier skill hierarchy** (system / workflow / reusable) with the workflow tier explicitly chaining reusable skills — the clearest example we've cataloged of skills composing skills by *reference* rather than duplication.
- **Router agent** (`pm-workflows`) classifies a request and dispatches to the right workflow — a resolver-routing-table implemented as a sub-agent ([[patterns/composition/resolver-routing-table]]).
- **Skills vs. agents split**: generation work = skills; *judgment* work (review, critique) = read-only sub-agents with output contracts. Commands eliminated entirely, citing Anthropic guidance ("Skills, not commands") ([[sources/prodmgmt-world--pm-os#plugin-manifest]]).
- **Hooks automate nudges, not work**: SessionStart hooks only *remind* (tidy/drip); mutation is reserved for explicit skill runs. Clean read/write separation — hook reads state, one `bin/` script writes it.
- **One content set, three surfaces**: claude-code, cursor, and cowork zips share the same skills/knowledge content with per-surface packaging (`.claude-plugin/` vs `.cursor-plugin/` vs `workspace/`) ([[sources/prodmgmt-world--pm-os#cursor-variant]]).
- **Machine-readable registry**: `registry/*.json` mirrors the component inventory so tooling (and the router agent) can enumerate capabilities without parsing markdown.

## Patterns demonstrated

- [[patterns/composition/single-source-multi-surface-distribution]] — one content set shipped as claude-code + cursor + cowork packages; same play as compound-engineering's ~11-platform conversion, but as a *paid product line*.
- [[patterns/composition/resolver-routing-table]] — `pm-workflows` router agent + `registry/` JSON index route requests to 235 skills.
- [[patterns/quality-bar/skill-pack-bundle]] — **as counter-pressure**: the largest single-domain pack we've cataloged (235 skills) ships with *no visible tests or evals* — a commercial data point against the tested-bundle discipline being universal (logged on the pattern page).
- [[patterns/quality-bar/version-as-update-gate]] — versioned releases (2.2.1), CHANGELOG, and a dedicated `pm-os-upgrade` skill that migrates user state between versions.
- [[patterns/behavioral/latent-vs-deterministic-split]] — deterministic shell hooks + state files + JSON registry vs. latent skill/agent judgment; hooks explicitly never mutate (single-writer `bin/` scripts).
- *(supports, not yet a pattern)* read-only reviewer sub-agents with explicit output contracts — same adversarial-verification idea as Anthropic's dynamic-workflows article and FSI's trust-tiered subagents; third sighting, strengthens the proposed adversarial-verification candidate noted in [[sources/anthropic--dynamic-workflows]]'s ingest.

## Source citations

- Component counts, "Skills, not commands," proprietary license, version: [[sources/prodmgmt-world--pm-os#plugin-manifest]]
- 235 skill inventory: [[sources/prodmgmt-world--pm-os#skills-dir]]
- 12 agent personas + read-only contracts: [[sources/prodmgmt-world--pm-os#agents-dir]]
- Hook behavior (nudge-only, single-writer state): [[sources/prodmgmt-world--pm-os#hooks]]
- MCP server list: [[sources/prodmgmt-world--pm-os#mcp-config]]
- Three-surface packaging: [[sources/prodmgmt-world--pm-os#cursor-variant]], [[sources/prodmgmt-world--pm-os#cowork-variant]]
- Registry index: [[sources/prodmgmt-world--pm-os#registry]]

## What makes it great

- The **three-tier hierarchy** keeps 235 skills navigable — system/workflow/reusable is a genuinely good taxonomy other packs lack (compound-engineering is flatter at 38).
- The **reviewer-agent board** is the crown jewel: 9 distinct, well-written personas with severity-tagged findings, tone calibration ("don't say X, say Y"), named anti-patterns ("just add a field" = 5 days), and a uniform output contract. Deliberate flaws/strengths *pairing* fights single-reviewer bias.
- It's **productized**: versioning, upgrade migration, onboarding, feedback/testimonial skills, paid distribution. Most packs are repos; this is a SKU.

## What we'd steal

**Exhaustive ledger, not a curated top-3.**

- ★ **Reviewer board as parallel read-only sub-agents with a uniform output contract** — already ported into Auto's `prd-review` OpenClaw skill (9 personas, fan-out + synthesis). The single most portable component.
- ★ **Three-tier skill taxonomy** (system / workflow / reusable) — adopt if our own skill count grows past ~20; workflows that *reference* atomic skills beat monolithic mega-skills.
- ★ **Flaws + strengths paired reviewers** — running a harsh critic *and* an optimist on the same doc and synthesizing beats either alone; cheap to apply to any review loop.
- ★ **One content set → many surfaces as a product line** — the multi-surface zip strategy is the distribution template if we ever sell a skill bundle (third sighting of this play; see compound-engineering, codex marketplace).
- **Machine-readable `registry/` JSON beside human markdown** — lets routers/tooling enumerate components deterministically.
- **Hooks that nudge but never mutate** (single-writer state scripts) — clean automation hygiene worth copying into any session-start hook design.
- **Named anti-pattern playbooks inside personas** ("make it real-time" → ask actual latency; "offline mode" → 8–12 weeks) — encoding effort heuristics into reviewer prompts is what makes findings concrete.
- **Tone-calibration blocks in agent prompts** ("don't say 'this will never work,' say…") — small, transferable trick for any critique agent.
- **An `upgrade` skill that migrates user state between pack versions** — versioned content packs need this; nobody else we've cataloged ships it.
- **Explicit "Skills, not commands" stance** — citing platform guidance as a design constraint keeps the surface area to one primitive.

## Open questions / what's unclear

- No public adoption signals (paid product, no marketplace counts) — can't gauge real-world usage.
- The `gnurio/pm-os` GitHub repo in the manifest is private/unverified — unclear if buyers get repo access or just zips.
- How much of the 211 reusable skills is genuinely distinct vs. near-duplicate prompt variations — a skill-level dedup audit would tell us, but is low priority.
- Cowork-variant behavior unverified (we studied the claude-code tree most closely).
