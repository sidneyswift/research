---
domain: artifacts
type: index
subdomain: projects
last-reviewed: 2026-06-01
---

# Projects

Frontier projects, systems, and products that are runnable artifacts but aren't a single skill, plugin, or MCP server — e.g. an agent framework, a full application, a research system, or a multi-component toolkit. Each page uses the closest-fitting `_schemas/` template (often [../../\_schemas/plugin.md](../../_schemas/plugin.md) as a starting point); adapt sections as needed.

Use this directory when the unit of study is bigger than one artifact type but is still a concrete thing you could clone and run. If the thing is purely an *idea*, it belongs in [concepts/](../../concepts/) instead.

## Cataloged projects

- [[artifacts/projects/codex-goals]] — OpenAI Codex CLI's **Goals** feature: persistent, thread-scoped, evidence-gated objectives via the `/goal` command surface (Codex ≥ 0.128.0). Embodies [[concepts/completion-contract]]; grounds [[patterns/behavioral/evidence-gated-completion]] and supplied the non-Garry 2nd example that promoted [[patterns/behavioral/skill-as-method-call]]. Source: [[sources/openai--using-goals-in-codex]].

## Candidate list (not yet deep-dived)

Add candidates here as one-line entries before promoting to a full page. Keep a `source:` URL on each.

- **Codex CLI** (OpenAI) — the broader agentic-coding tool; only its Goals feature is studied so far (see [[artifacts/projects/codex-goals]]). A full ingest would enable a Codex-vs-Claude-Code comparison. Source: `https://developers.openai.com/codex`.
