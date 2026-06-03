---
domain: creators
type: org
name: Anthropic
handle: anthropics
url: https://anthropic.com
last-reviewed: 2026-06-01
---

# Anthropic

> The company that makes Claude. Ships Claude Code, the Agent Skills format, the Claude API, and a reference repo of demonstration skills. Sets the spec the rest of the ecosystem reacts to.

## Attributes

- **What they ship**: Claude (model family), Claude Code (CLI/desktop/web), Claude.ai Skills format, Agent Skills specification, MCP (Model Context Protocol — co-created), Cowork plugin marketplace, the [Managed Agents API](https://docs.claude.com/en/api/managed-agents) (`/v1/agents`), vertical reference marketplaces (e.g. financial services), and **dynamic workflows** (model-generated JS harnesses for multi-agent orchestration, 2026-06-02).
- **Distribution channels**: github.com/anthropics, claude.ai, anthropic.com docs and support, Claude Code marketplace, Cowork.
- **Position in ecosystem**: Standard-setter. Their format choices propagate; their docs are authoritative.
- **Notable docs**: ["What are skills?"](https://support.claude.com/en/articles/12512176-what-are-skills), ["Creating custom skills"](https://support.claude.com/en/articles/12512198-creating-custom-skills), engineering post ["Equipping Agents for the Real World with Agent Skills"](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

## Artifacts produced

### Skills (in [[sources/anthropic--skills]])
*(speedrun: deep-dives pending — see candidate list in [[artifacts/skills/_index]])*

- algorithmic-art, brand-guidelines, canvas-design, claude-api, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx

### Plugins
- [[artifacts/plugins/anthropic-skills-marketplace]] — the repo itself, registered as a Claude Code plugin marketplace
- [[artifacts/plugins/anthropic-financial-services-marketplace]] — the FSI reference marketplace; 20 plugins, dual-runtime (Cowork plugin + Managed Agents API), trust-tiered subagents, single-source skill vendoring

### Spec
- Agent Skills specification at `sources/anthropic--skills/spec/agent-skills-spec.md` ([[sources/anthropic--skills#spec]])

## Design philosophy (discernible from artifacts)

- **Minimal SKILL.md frontmatter**: Anthropic's own skills use only `name:` + `description:`. Reading the [[sources/anthropic--skills#skill-creator]] meta-skill, the philosophy is that *description* is the primary discoverability mechanism — write it so triggering is reliable, and the rest of the SKILL.md teaches Claude *how*. Frontmatter is for routing, not configuration.
- **Skill bodies are written in conversational prose**, not specifications. `skill-creator`'s SKILL.md ends with "Cool? Cool." — voice is informal and instructional.
- **Progressive disclosure via `references/` and `scripts/`** — heavy material doesn't go in SKILL.md; SKILL.md is the index. (TODO: cite specific examples once deep-dived.)
- **Apache 2.0 default**, with select source-available carve-outs (docx, pdf, pptx, xlsx — production document skills).
- **Security and deployment-surface as first-class design** (newer FSI work): the financial-services marketplace ships every agent to two runtimes from one source, and isolates untrusted-document handling inside trust-tiered subagents (only the reader touches outsider docs; exactly one leaf holds Write). See [[artifacts/plugins/anthropic-financial-services-marketplace]]. A visibly more production-minded posture than the demonstration-grade skills repo — and the FSI plugins are authored by a distinct internal team (`Anthropic FSI`, owner Matt Piccolella).

## Source citations

- [[sources/anthropic--skills#README]] — repo description and intent
- [[sources/anthropic--skills#skill-creator]] — frontmatter conventions and skill-writing philosophy
- [[sources/anthropic--skills#marketplace.json]] — Cowork-installable plugin format
- [[sources/anthropic--plugins-reference]] — Claude Code plugin system spec: `plugin.json`, `${CLAUDE_PLUGIN_ROOT}` file resolution, and plugin caching behavior
- [[sources/anthropic--financial-services]] — FSI reference marketplace: dual-runtime distribution, managed-agent cookbooks (`agent.yaml` + subagents), trust-tiered subagent security, single-source skill vendoring with drift detection
- [[sources/anthropic--dynamic-workflows]] — "A harness for every task: dynamic workflows in Claude Code" (Thariq Shihipar + Sid Bidasaria, 2026-06-02): the first official Anthropic deep-dive on how the Claude Code harness works internally — model-generated JS workflows, 6 composable orchestration patterns, 3 named failure modes (agentic laziness, self-preferential bias, goal drift)
