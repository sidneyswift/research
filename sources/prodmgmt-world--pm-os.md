---
domain: sources
type: other # purchased proprietary plugin bundle (3 zips: claude-code, cursor, cowork)
url: https://prodmgmt.world
retrieved: 2026-06-10
snapshot-location: sources/prodmgmt-world--pm-os-bundle/ # LOCAL-ONLY, git-ignored (proprietary paid product — never committed/pushed; this repo is public)
upstream-commit: n/a # distributed as versioned zips; studied version 2.2.1
last-reviewed: 2026-06-10
---

# PM OS 2.2.1 (prodmgmt.world) — purchased plugin bundle

> **One-line:** the purchased "Product Manager's AI Operating System" bundle — 235 skills + 12 sub-agents + 2 hooks shipped as parallel Claude Code, Cursor, and Cowork packages — our first *paid, proprietary* artifact source.

*Done when it passes the [page checklist](_definition-of-done.md).*

## Snapshot details

- **Retrieved**: 2026-06-10 (purchased copy)
- **Where it lives in this wiki**: `sources/prodmgmt-world--pm-os-bundle/` — a **local-only, git-ignored** evidence copy (3 zips + extracted claude-code/cursor/cowork trees), same Option-B treatment as the cloned repos but with a stricter reason: PM OS is a proprietary paid product (`"license": "Proprietary"` in its manifest), so committing it to this public repo would republish paid material. It is **not** in `repos.manifest.tsv` (no public repo to re-clone from); rebuild by re-extracting the purchased zips. Claims below cite file paths inside that copy.
- **Upstream URL**: https://prodmgmt.world (product site); repo field in manifest: https://github.com/gnurio/pm-os (private/unverified)
- **Upstream identifier**: version `2.2.1` (from `.claude-plugin/plugin.json` and zip filenames)

## Anchor map

Paths are relative to `sources/prodmgmt-world--pm-os-bundle/claude-code/pm-os/plugins/pm-os/` unless noted.

- `#root` — the bundle as a whole (all three zips)
- `#plugin-manifest` — `.claude-plugin/plugin.json` (name, version 2.2.1, proprietary license, component description: 13 system + 11 workflow + 211 reusable skills, 12 sub-agents, 2 SessionStart hooks)
- `#skills-dir` — `skills/` (235 skill directories)
- `#agents-dir` — `agents/` (12 sub-agent persona files: pm-workflows router, knowledge-librarian, context-manager, 7 cross-functional reviewers, 2 PRD reviewers)
- `#hooks` — `hooks/hooks.json` + `tidy-reminder.sh` + `drip-reminder.sh` (2 SessionStart nudge hooks)
- `#mcp-config` — `.mcp.json` (6 servers: lenny-podcast HTTP, notion, linear, atlassian, github, perplexity)
- `#registry` — `registry/` (agents.json, commands.json, skills.json, workflows.json, CAPABILITIES.md — machine-readable component index)
- `#cursor-variant` — sibling cursor zip: `.cursor-plugin/marketplace.json`, `.cursor/hooks.json`, `.cursor/mcp.json`, emoji-named content dirs (📂 Context, 🧠 Knowledge, 📄 Templates, 💎 Examples)
- `#cowork-variant` — sibling cowork zip: `workspace/` layout for Anthropic Cowork
- `#knowledge-dir` — `🧠 Knowledge/` framework library shipped alongside skills (frameworks the reviewer agents cite)

## Why we cite this

- Claims about how a commercial PM skill bundle is structured, priced-tier packaged, and distributed across three agent surfaces from one content set.
- Component inventory and composition claims for [[artifacts/plugins/pm-os]].
- Evidence for [[patterns/composition/single-source-multi-surface-distribution]] (one content set → claude-code + cursor + cowork zips) and [[patterns/quality-bar/skill-pack-bundle]].

## Popularity signals (if this source provides them)

- **Signal type**: commercial product (paid); no public star/install counts available.
- **Value at snapshot**: n/a — sold via prodmgmt.world; marketing claims on site not independently verifiable.
- **As-of**: 2026-06-10

## Related sources

- [[sources/anthropic--plugins-reference]] — the plugin format PM OS targets
- [[sources/every--compound-engineering]] — the other large multi-surface skill pack we've studied (38 skills/43 agents, converted to ~11 platforms)
