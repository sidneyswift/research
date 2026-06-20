---
domain: sources
type: docs-page
url: https://agentskills.io/specification
retrieved: 2026-06-04
snapshot-location: sources/agentskills--specification/
upstream-commit: n/a (living page; spec carries no version stamp)
last-reviewed: 2026-06-04
governance: Agentic AI Foundation (AAIF, Linux Foundation-backed); spec repo github.com/agentskills/agentskills
---

# Agent Skills — the open specification (agentskills.io)

> The **formal open standard** for agent skills: a skill = a directory with `SKILL.md` (required `name` + `description` YAML frontmatter) plus optional `scripts/`/`references/`/`assets/`, loaded by **progressive disclosure** (~100-token metadata → full SKILL.md on activation → resources on demand). Originally developed by Anthropic, released as an open standard **2025-12-18** and donated to the Linux Foundation-backed **Agentic AI Foundation** — the same governance playbook as MCP. We cite it as the *standard body* that turns the cross-lab plugin/skill convergence from coincidence into adoption.

## Snapshot details

- **Retrieved**: 2026-06-04 (fetched from the site's own markdown endpoint `agentskills.io/specification.md`)
- **Where it lives in this wiki**: `sources/agentskills--specification/snapshot.md`
- **Upstream URL**: https://agentskills.io/specification
- **Upstream identifier**: n/a — living page, no version stamp. Spec governance repo: `github.com/agentskills/agentskills` (created 2025-12-16; ~19.9K★ as-of 2026-06-04 per research-agent retrieval).
- **Provenance of standardization facts**: release date + AAIF donation reported by SiliconANGLE (2025-12-18) and Anthropic's engineering post "Equipping agents for the real world with Agent Skills"; the spec page itself documents only the format.

## Anchor map

- `#root` — the spec as a whole
- `#directory-structure` — skill = dir with required `SKILL.md` + optional `scripts/` `references/` `assets/`
- `#frontmatter` — the field table: required `name` (≤64 chars, kebab, must match dir name) + `description` (≤1024); optional `license`, `compatibility` (≤500), `metadata` (arbitrary map), `allowed-tools` (experimental)
- `#description-guidance` — "what it does and when to use it," keyword-loaded; good-vs-poor example
- `#progressive-disclosure` — the 3-level loading model: metadata ~100 tokens at startup → SKILL.md (<5,000 tokens recommended) on activation → resources on demand; "keep SKILL.md under 500 lines"
- `#file-references` — relative paths from skill root, one level deep, no nested chains
- `#validation` — `skills-ref validate ./my-skill` reference validator
- `#governance` — open-standard facts (release 2025-12-18, AAIF/Linux Foundation, github.com/agentskills/agentskills) — *from secondary reporting, not the spec page*

## Why we cite this

- The existence of a **formal joint spec** — supersedes this wiki's earlier framing that the Anthropic/OpenAI plugin-format overlap was "convergence, not a shared standard body" ([[concepts/convergent-agent-plugin-spec]]). There *is* a standard body now.
- The canonical definitions: frontmatter contract, naming rules, progressive disclosure budget figures (~100 tokens / <5,000 tokens / 500 lines) — the numbers every adopter (Codex, Claude Code, Cursor, Copilot) inherits.
- The `compatibility` and `metadata` extension points — how lab-specific extras stay spec-legal.

## Popularity signals

- **Signal type**: adopters — agentskills.io's client list shows **40+ clients** including OpenAI Codex, Claude/Claude Code, Cursor, GitHub Copilot, VS Code, Gemini CLI, OpenCode, OpenHands, Goose, JetBrains Junie (as-of 2026-06-04, research-agent retrieval of agentskills.io/home).
- **Signal type**: github-stars (spec repo `agentskills/agentskills`) — **~19,938** as-of 2026-06-04.
- **Signal type**: named adoption — OpenAI's Codex skills doc links this spec directly: "Skills build on the open agent skills standard" ([[sources/openai--codex-skills-doc#open-standard]]).

## Related sources

- [[sources/openai--codex-skills-doc]] — OpenAI's implementation of this spec in Codex (+ its `agents/openai.yaml` extension).
- [[sources/anthropic--skills]] — Anthropic's skills repo, which carries the spec's ancestor (`spec/agent-skills-spec.md`).
- [[sources/openai--plugins]] — the Codex marketplace whose 479 SKILL.md files follow this anatomy.
- [[sources/openai--chatgpt-skills-help]] — ChatGPT's consumer-side adoption ("OpenAI skills follow the Agent Skills open standard").
