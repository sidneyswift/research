---
domain: artifacts
type: index
subdomain: projects
last-reviewed: 2026-10-23
---

# Projects

Frontier projects, systems, and products that are runnable artifacts but aren't a single skill, plugin, or MCP server — e.g. an agent framework, a full application, a research system, or a multi-component toolkit. Each page uses [../../_schemas/project.md](../../_schemas/project.md), including evidence classes and guarantee boundaries.

Use this directory when the unit of study is bigger than one artifact type but is still a concrete thing you could clone and run. If the thing is purely an *idea*, it belongs in [concepts/](../../concepts/) instead.

## Cataloged projects

- [[artifacts/projects/humanlayer]] — collaborative coding-agent control plane: durable tasks, host execution, contextual feedback, incremental review, and scoped recovery. Full product/runtime ledger plus [[artifacts/plugins/humanlayer-rpi]]; source-inspected at `2f66a45`, not live-verified.

- [[artifacts/projects/codex-goals]] — OpenAI Codex CLI's **Goals** feature: persistent, thread-scoped, evidence-gated objectives via the `/goal` command surface (Codex ≥ 0.128.0). Embodies [[concepts/completion-contract]]; grounds [[patterns/behavioral/evidence-gated-completion]] and supplied the non-Garry 2nd example that promoted [[patterns/behavioral/skill-as-method-call]]. Source: [[sources/openai--using-goals-in-codex]].
- [[artifacts/projects/eve]] — Vercel's **eve** framework: a filesystem-first, durable agent framework — agent-as-directory authoring, a framework-owned **harness** + built-in toolbelt, durable session/turn/step execution, channels (one agent → many surfaces), sandboxes, subagents/remote-agents, schedules, connections, dynamic capabilities, and first-class evals. The wiki's **first ingested harness** — the long-missing middle of [[patterns/structural/thin-harness-fat-skills]] (which it grounds *and* complicates: a production harness is a full framework, not "~200 lines"). Embodies [[concepts/filesystem-first-agent-framework]] + [[concepts/durable-agent-execution]]. Source: [[sources/vercel--eve]].
- [[artifacts/projects/skill-diffs]] — SHL0MS's **skill-diffs**: a pipeline that mines the commit history of `SKILL.md` files across 4 agent platforms into a published `(before, after, intent)` dataset, plus a defect-derived rule-based linter and a skill-patch eval harness. The wiki's **first dataset-and-tooling-pipeline** artifact — a research-infrastructure axis distinct from skills/plugins/MCP/frameworks. Embodies [[concepts/commit-history-as-training-data]] + [[concepts/imitation-vs-correctness-eval]]; founding example of [[patterns/quality-bar/defect-derived-validation]]. Source: [[sources/SHL0MS--skill-diffs]].

## Candidate list (not yet deep-dived)

Add candidates here as one-line entries before promoting to a full page. Keep a `source:` URL on each.

- **Codex CLI** (OpenAI) — the broader agentic-coding tool; only its Goals feature is studied so far (see [[artifacts/projects/codex-goals]]). A full ingest would enable a Codex-vs-Claude-Code comparison. Source: `https://developers.openai.com/codex`.
- **Hermes Agent** (Nous Research) — the named downstream consumer of `skill-diffs`'s trained curator model; its **Curator** feature is a background maintenance pass tracking skill usage (active→stale→archived) directly relevant to this wiki's own LINT operation (see [[meta/self-improvements]] Pass 13). Not yet ingested — referenced only via its public docs page. Source: `https://hermes-agent.nousresearch.com/docs/user-guide/features/curator`.
