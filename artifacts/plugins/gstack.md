---
domain: artifacts
type: plugin
name: gstack
creator: "[[creators/garry-tan]]"
source: "[[sources/garrytan--gstack]]"
ecosystem: claude-code
discovered-via: user-curated (Sidney named explicitly)
marketplace-listing: https://www.producthunt.com/products/gstack
status: active
last-reviewed: 2026-05-21
ingestion-mode: speedrun
components:
  skills: 23+ workflow skills (plus 8 power tools, by author's framing)
  commands: 36 slash commands documented in install one-liner
  agents: directory exists (./agents/), not yet inventoried
  hooks: TODO check .claude-plugin/ or setup script
  mcp-servers: none ships in-repo; integrates with gbrain MCP
popularity-signals:
  - signal: hacker-news-front-page
    value: thread at item id 47418576
    as-of: 2026-05-21
    source: "[[sources/garrytan--gstack#README]]"
  - signal: product-hunt-launch
    value: shipped
    as-of: 2026 (date TBD)
    source: "[[sources/garrytan--gstack#README]]"
  - signal: press-coverage
    value: 6+ third-party writeups (Sitepoint, MindStudio, Augment Code, BuildThisNow, AwesomeAgents, ExplainX)
    as-of: 2026-05-21
  - signal: author-distribution
    value: Garry Tan, CEO of Y Combinator — built-in reach
    as-of: 2026-05-21
---

# gstack

> **One-line:** Garry Tan's opinionated Claude Code skill pack that turns Claude Code into a virtual engineering team with persona-shaped skills (CEO, Designer, Eng Manager, QA Lead, CSO, Release Engineer).

## Attributes (speedrun bullets)

- **Target user**: founders, first-time Claude Code users, tech leads. Per [[sources/garrytan--gstack#README]], "Founders and CEOs — especially technical ones who still want to ship."
- **Install footprint**: `~/.claude/skills/gstack/` (41 MB cloned). Requires Bun v1.0+, Node.js (Windows only), Git. Setup script does the wiring. Team mode adds repo-level `.claude/` to share with collaborators.
- **Plugin layout**: 60+ top-level directories, each a sub-skill or infrastructure dir. `bin/` has ~62 scripts (gstack CLI helpers). Root docs are massive: README (42 KB), SKILL.md (47 KB), CLAUDE.md (49 KB), ARCHITECTURE.md (32 KB), BROWSER.md (60 KB), CHANGELOG.md (690 KB!).
- **Component naming = personas, not tasks**:
  - CEO-class: `/office-hours`, `/plan-ceo-review` ([[sources/garrytan--gstack#plan-ceo-review]])
  - Eng Manager: `/plan-eng-review`, `/review`, `/investigate`
  - Designer: `/design-consultation`, `/design-shotgun`, `/design-html`, `/design-review`
  - QA Lead: `/qa`, `/qa-only`
  - CSO (Chief Security Officer): `/cso` (OWASP + STRIDE)
  - Release Engineer: `/ship`, `/land-and-deploy`, `/canary`, `/freeze`, `/guard`, `/unfreeze`
  - Doc Engineer: `/document-release`, `/document-generate`
  - DevEx: `/plan-devex-review`, `/devex-review`
  - Auxiliary: `/autoplan`, `/pair-agent`, `/careful`, `/codex`, `/learn`, `/retro`, `/skillify`, `/browse`, `/connect-chrome`, `/setup-browser-cookies`, `/setup-deploy`, `/setup-gbrain`, `/sync-gbrain`, `/gstack-upgrade`
- **License**: MIT ([[sources/garrytan--gstack#root]] LICENSE file).

## Relationships

- **Creator**: [[creators/garry-tan]]
- **Source**: [[sources/garrytan--gstack#root]]
- **Composes with**: [[artifacts/plugins/gbrain]] via `/setup-gbrain` + `/sync-gbrain` ([[sources/garrytan--gstack#using-gbrain-with-gstack]])
- **Extends**: Anthropic SKILL.md format with custom frontmatter ([[sources/anthropic--skills#spec]])

## Composition strategy

- **Massive shared preamble** in root SKILL.md ([[sources/garrytan--gstack#SKILL.md]]). Every skill invocation runs `bin/gstack-update-check`, telemetry config check, project slug detection, per-project `learnings.jsonl` loading, timeline logging, and a "Skill routing" CLAUDE.md check. This is *infrastructure-as-preamble*.
- **ETHOS injection**: [[sources/garrytan--gstack#ETHOS.md]] is auto-injected into every workflow skill's preamble. Carries opinions like "Boil the Lake" (do the complete thing because completeness is cheap with AI) into every skill call.
- **`/browse` as shared substrate**: every skill that needs web access calls `/browse`, not `mcp__claude-in-chrome__*`. README's install instruction explicitly tells Claude to update CLAUDE.md to enforce this. ([[sources/garrytan--gstack#README]])
- **Multi-tier skills**: `/qa` ships Quick / Standard / Exhaustive tiers ([[sources/garrytan--gstack#qa]]). User picks the depth.
- **`benefits-from:` frontmatter** declares related skills — e.g., `plan-ceo-review` declares `benefits-from: [office-hours]`. ([[sources/garrytan--gstack#plan-ceo-review]])
- **Per-skill `gbrain:` block** for skills that pull context from gbrain — `retro` declares `context_queries: [{id: prior-retros, kind: filesystem}]`. ([[sources/garrytan--gstack#retro]])
- **Telemetry, learnings, timeline**: optional but built in. Every skill run logs to `~/.gstack/analytics/skill-usage.jsonl` if telemetry is on. Per-project learnings file at `~/.gstack/projects/{SLUG}/learnings.jsonl` is auto-loaded and grep-searched on every run.

## Patterns demonstrated (proposed, pending pattern-page creation)

- **Persona-shaped command naming** — proposed pattern. Skills named for roles (CEO/Designer/QA Lead) instead of task categories (planning/design/testing). Need 2nd example to confirm.
- **Philosophy injection via preamble** — ETHOS.md inserted into every workflow skill. Cultural priming, not technical. Need 2nd example to confirm.
- **Frontmatter extensions beyond official spec** — `preamble-tier`, `version`, `triggers`, `benefits-from`, `gbrain:` block, voice triggers in description. Need cross-reference with gbrain to confirm pattern.
- **Voice-trigger aliases in description** — e.g., `qa` declares "quality check", "test the app", "run QA" in the description text as STT aliases. ([[sources/garrytan--gstack#qa]])
- **Heavy bash preamble as "skill OS"** — root SKILL.md does telemetry, learnings, timeline, config — turning the preamble into a runtime. Likely anti-pattern in most contexts but worth studying.
- **Branding suffix in description** — gstack skills end their description with `(gstack)`. Probably to disambiguate when multiple skill packs are installed.

## Source citations

- [[sources/garrytan--gstack#README]] — pitch, install steps, 23-skill enumeration, persona framing, productivity claims
- [[sources/garrytan--gstack#SKILL.md]] — root preamble bash, frontmatter shape (preamble-tier, version, allowed-tools, triggers)
- [[sources/garrytan--gstack#ETHOS.md]] — "Boil the Lake", "Completeness is cheap"
- [[sources/garrytan--gstack#plan-ceo-review]] — interactive flag, benefits-from, multi-mode skill
- [[sources/garrytan--gstack#retro]] — gbrain: block in frontmatter
- [[sources/garrytan--gstack#qa]] — multi-tier skill (Quick/Standard/Exhaustive), voice triggers

## What we'd steal

- **Persona naming for skills** when the audience is non-engineers — "CEO review" lands harder than "scope expansion review."
- **`benefits-from:` declarations** to encode skill DAGs in metadata, not docs.
- **`gbrain:` context-query block** as a model for skills that need external memory.
- **Multi-tier skills** when depth/cost varies widely (Quick / Standard / Exhaustive).
- **Voice triggers as a first-class field** for skill discovery via speech-to-text.
- **Per-project `learnings.jsonl`** as a lightweight memory not requiring a vector DB.
- **Skill description suffix as pack-branding** to disambiguate which pack a skill came from.

## Weird/surprising thing (mandatory in speedrun mode)

The root SKILL.md preamble is a ~50-line bash script that runs *before any skill logic*, doing telemetry/learnings/timeline/config/proactive-mode/routing-detection. This crosses a line — preambles are usually "load context"; here it's "run a small CLI app." It implies gstack thinks of itself as a runtime, not a skill pack. The downside: every skill invocation pays the latency.

## Open questions / what's unclear

- How does gstack handle skill conflicts when other packs are also installed? Branding suffix `(gstack)` suggests they've thought about it.
- Is the ETHOS philosophy injection a *feature* (consistent voice) or a *constraint* (forces the user into Garry's worldview)?
- Does the persona framing actually improve outcomes vs. task-category framing, or is it primarily marketing?
- What does the `agents/` dir contain — full subagent definitions, or thin shims to skills?
- The 690 KB CHANGELOG is unusual — what's the release cadence? (TODO: skim CHANGELOG for cadence stats.)
