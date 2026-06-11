---
domain: creators
type: org # solo-operator product business (publishes as prodmgmt.world)
name: prodmgmt.world
handle: gnurio
url: https://prodmgmt.world
country: unknown
last-reviewed: 2026-06-10
---

# prodmgmt.world

> **One-line:** the publisher of PM OS — a paid, versioned, multi-surface PM skill bundle; our first *commercial* (non-open-source) creator, selling agent content as a product rather than sharing it as a repo.

*Page shape: compiled truth on top, append-only `## Timeline` below. Done when it passes the [page checklist](_definition-of-done.md).*

## Attributes

- **What they ship**: one flagship product — PM OS, a plugin bundle (235 skills, 12 sub-agents, 2 hooks, 6 MCP configs) for Claude Code, Cursor, and Cowork.
- **Distribution channel**: direct sales via prodmgmt.world (zip downloads per surface). Manifest references a GitHub repo (`gnurio/pm-os`) that is private/unverified.
- **Position in ecosystem**: independent commercial publisher productizing the skill-pack format for a non-engineering vertical (product management). Notable as evidence that the plugin/skill format has a *paid* market beyond open-source sharing.
- **Notable quotes / framings**: "Product Manager's AI Operating System — one plugin, one namespace"; "Skills, not commands — per Anthropic's plugin guidance" ([[sources/prodmgmt-world--pm-os#plugin-manifest]]).

## Artifacts produced

### Plugins
- [[artifacts/plugins/pm-os]]

## Design philosophy (if discernible)

Productization over openness: versioned releases with CHANGELOG and an in-product `upgrade` migration skill, onboarding (`pm-os-start`) and feedback/testimonial skills baked into the bundle itself. Strong taxonomy discipline (three-tier skill hierarchy; canonical short names; machine-readable `registry/` JSON). Judgment work goes to read-only sub-agents with uniform output contracts; deterministic work goes to shell scripts and state files that the LLM never writes directly. Follows Anthropic guidance closely (skills-only, no commands) while packaging the same content for rival surfaces (Cursor) — pragmatically cross-lab, not ecosystem-loyal.

## Timeline (append-only)

- 2026-06-10 — PM OS 2.2.1 purchased and ingested; first paid proprietary artifact in the wiki ([[sources/prodmgmt-world--pm-os#root]])
