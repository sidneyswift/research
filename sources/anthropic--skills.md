---
domain: sources
type: repo
url: https://github.com/anthropics/skills
retrieved: 2026-05-21
snapshot-location: sources/anthropic--skills/
upstream-commit: 690f15cac7f7b4c055c5ab109c79ed9259934081
upstream-commit-date: 2026-05-19
last-reviewed: 2026-05-21
license: Apache 2.0 (most) + source-available (docx/pdf/pptx/xlsx)
---

# Anthropic Skills (`anthropics/skills`)

> Anthropic's official skills repository. Demonstration skills + the Agent Skills specification + a starter template. The canonical reference everyone benchmarks against.

## Snapshot details

- **Retrieved**: 2026-05-21
- **Location**: `sources/anthropic--skills/` (11 MB, `.git/` stripped)
- **Upstream URL**: https://github.com/anthropics/skills
- **Upstream commit**: `690f15c` (2026-05-19)
- **Installable as Claude Code plugin marketplace** via `/plugin marketplace add anthropics/skills`. Two installable plugins inside: `document-skills@anthropic-agent-skills`, `example-skills@anthropic-agent-skills`.

## Anchor map

- `#root` — the repo as a whole
- `#README` — `README.md` at repo root
- `#marketplace.json` — `.claude-plugin/marketplace.json` (the marketplace manifest)
- `#spec` — `spec/agent-skills-spec.md` (the official spec)
- `#template` — `template/SKILL.md` (the starter template)
- `#skills-dir` — `skills/` directory listing (17 demonstration skills)
- `#skill-creator` — `skills/skill-creator/SKILL.md` (the meta-skill that creates other skills)
- `#mcp-builder` — `skills/mcp-builder/SKILL.md`
- `#frontend-design` — `skills/frontend-design/SKILL.md`
- `#docx`, `#pdf`, `#pptx`, `#xlsx` — the document-generation skills (source-available)
- `#brand-guidelines`, `#internal-comms` — enterprise skills
- `#algorithmic-art`, `#canvas-design`, `#slack-gif-creator`, `#theme-factory` — creative skills
- `#webapp-testing`, `#web-artifacts-builder`, `#doc-coauthoring`, `#claude-api` — technical/dev skills
- `#third-party-notices` — `THIRD_PARTY_NOTICES.md` (license inventory)

(Add anchors here as we cite specific files inside the snapshot. Anchors after `#` map to filesystem paths under `sources/anthropic--skills/`.)

## Why we cite this

The authoritative source for what a "skill" *is* (per Anthropic). Every other skill in the ecosystem is in conversation with this spec — extending it, simplifying it, or rejecting parts of it. We cite this for:
- The canonical SKILL.md frontmatter shape (`name:` + `description:`)
- The progressive-disclosure pattern as Anthropic demonstrates it
- Reference behaviors for tool-restricted skills (look at `allowed-tools` usage — or lack of it — across the 17 skills)
- The marketplace plugin format (`.claude-plugin/marketplace.json`)

## Popularity signals

- **Official Anthropic repository** — listed in Anthropic's docs and support articles
- **Linked from Anthropic engineering post** "Equipping Agents for the Real World with Agent Skills" (cited in README)
- **GitHub stars**: not captured at snapshot — TODO add via `gh api` next pass
- **Cross-references this repo from**: gstack, gbrain, third-party tutorials, agentskills.io

## Related sources

- [[sources/garrytan--gstack]] — opinionated extension/replacement built on top of skills format
- [[sources/garrytan--gbrain]] — uses skills format inside OpenClaw plugin runtime, extends manifest
