---
domain: artifacts
type: plugin
name: anthropic-agent-skills
creator: "[[creators/anthropic]]"
source: "[[sources/anthropic--skills]]"
ecosystem: claude-code (also Claude.ai, also API)
discovered-via: official-docs (Anthropic's own demonstration set)
marketplace-listing: "/plugin marketplace add anthropics/skills"
status: active
last-reviewed: 2026-05-21
ingestion-mode: speedrun
components:
  skills: 17 across 3 child plugins
  commands: none — skills only
  agents: none
  hooks: none
  mcp-servers: none
popularity-signals:
  - signal: official-anthropic
    value: "yes — Anthropic's own demonstration repo, linked from anthropic.com docs"
    as-of: 2026-05-21
    source: "[[sources/anthropic--skills#README]]"
  - signal: marketplace-included
    value: registered as a plugin marketplace with 3 child plugins
    as-of: 2026-05-21
    source: "[[sources/anthropic--skills#marketplace.json]]"
---

# anthropic-agent-skills (the marketplace)

> **One-line:** Anthropic's official demonstration marketplace. One repo containing three Claude Code plugins (`document-skills`, `example-skills`, `claude-api`) totaling 17 skills. The reference shape for what a "well-formed" skill looks like.

## Attributes

- **Marketplace owner**: Keith Lazuka @ Anthropic ([[sources/anthropic--skills#marketplace.json]])
- **Three child plugins** ([[sources/anthropic--skills#marketplace.json]]):
  1. **document-skills** (4 skills, source-available): `xlsx`, `docx`, `pptx`, `pdf` — power Claude's document capabilities in production
  2. **example-skills** (12 skills, Apache 2.0): `algorithmic-art`, `brand-guidelines`, `canvas-design`, `doc-coauthoring`, `frontend-design`, `internal-comms`, `mcp-builder`, `skill-creator`, `slack-gif-creator`, `theme-factory`, `web-artifacts-builder`, `webapp-testing`
  3. **claude-api** (1 skill, Apache 2.0): Claude API / SDK documentation skill
- **Install**: `/plugin marketplace add anthropics/skills` then `/plugin install document-skills@anthropic-agent-skills` etc.
- **Plugin layout**: very flat. `skills/<name>/SKILL.md` for each skill. Each skill self-contained with its own `references/`, `scripts/`, `assets/` as needed.
- **Includes**: `spec/agent-skills-spec.md` — the actual Agent Skills specification (the *thing* the rest of the ecosystem extends).
- **Includes**: `template/SKILL.md` — starter template for new skills.
- **License**: Apache 2.0 for most; source-available for the 4 document skills (per [[sources/anthropic--skills#README]]).

## Relationships

- **Creator**: [[creators/anthropic]]
- **Source**: [[sources/anthropic--skills#root]]
- **Reference for**: every other skill pack in this wiki — Anthropic's format choices are the floor
- **Companion docs**: linked from anthropic.com/engineering and support.claude.com

## Composition strategy

- **The marketplace is the composition unit.** A single repo registers as a marketplace, then declares N installable plugins inside via `.claude-plugin/marketplace.json`. Each child plugin has its own name + description + skill list. This is a *light* composition pattern — no skill-to-skill dependencies, no shared resources between plugins. Just packaging.
- **Skills are self-contained.** No `shared_deps` analog. No cross-skill imports. Each skill stands alone.
- **No `commands/`, no `agents/`, no `hooks/`, no MCP servers.** This is pure skill demonstration — the simplest possible plugin shape.
- **Skills marketed as "demonstration and educational"** ([[sources/anthropic--skills#README]] disclaimer). Anthropic explicitly says: production Claude may behave differently. The point is showing the *pattern*, not shipping the runtime.

## Patterns demonstrated (proposed)

- **Marketplace-as-multi-plugin** — one repo declares ≥2 plugins via `marketplace.json`. Lets a creator group related work without forking. Need 2nd example.
- **Minimal frontmatter** — Anthropic skills use only `name:` + `description:`. The spec floor. ([[sources/anthropic--skills#skill-creator]])
- **License segmentation within one repo** — Apache 2.0 for most, source-available for production-grade ones. Lets a vendor open-source most while protecting business-critical work.
- **Demonstration-mode disclaimer** — explicitly frames the skills as "educational" so users don't expect production-equivalent behavior.

## Source citations

- [[sources/anthropic--skills#README]] — repo intent, license segmentation, install instructions, disclaimer
- [[sources/anthropic--skills#marketplace.json]] — three child plugins, skill mappings, owner
- [[sources/anthropic--skills#skill-creator]] — canonical SKILL.md frontmatter shape
- [[sources/anthropic--skills#spec]] — the Agent Skills specification itself

## What we'd steal

- **Marketplace manifest** as a way to ship multiple related plugins from one repo without forking.
- **License segmentation strategy** — open source most, protect the few production-load-bearing skills, segment cleanly within one repo.
- **Demonstration disclaimer** for any artifact that's reference-mode rather than production-mode. Sets expectations honestly.
- **`spec/` + `template/` directories alongside the skills.** Telling users *how to write more skills* alongside the skills themselves makes the repo a teaching artifact, not just a tool.
- **Minimal frontmatter** as a starting point — let descriptions do the work; add custom fields only when triggering becomes unreliable.

## Weird/surprising thing

The marketplace `name` is `anthropic-agent-skills` but the owner field is a specific employee (`Keith Lazuka <klazuka@anthropic.com>`). Personalizing ownership of an Anthropic-official artifact is unusual — most companies would put a team or distribution-list email. It's a small signal that skills are still emerging-product territory inside Anthropic, not a fully institutionalized line.

## Open questions / what's unclear

- Why 3 child plugins and not 1 or 17? Why is `claude-api` its own plugin instead of joining `example-skills`?
- The 4 source-available document skills are bundled as one plugin — is that because Claude's own product depends on the same files?
- No `commands/`, `agents/`, `hooks/`, or MCP servers in the entire marketplace. Is that deliberate (skills-as-foundation) or pre-feature (these primitives weren't ready)?
- How do the 17 skills here compare to the equivalent skills inside Garry Tan's gstack? (E.g., gstack has its own `skillify`, gbrain has its own `skill-creator`. We'll find out as we deep-dive.)
