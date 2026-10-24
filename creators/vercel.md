---
domain: creators
type: org
name: Vercel
handle: vercel
url: https://vercel.com
last-reviewed: 2026-06-20
---

# Vercel

> The frontend-cloud company behind **Next.js**, the **AI SDK**, and the **Workflow SDK** — and, in this wiki, the maker of **eve**, an open-source filesystem-first framework for durable backend AI agents (Apache-2.0, public preview 2026-06-17). eve is the wiki's **first agent framework / harness** studied as a runnable artifact — the long-missing "thin harness" middle layer — and Vercel is its **first non-lab platform creator** (a tooling/infra company, not a frontier model lab).

**Scope note:** this page is grounded in the **one** Vercel source ingested so far — [[sources/vercel--eve]] (the framework + its 37 bundled docs). Vercel's broader catalog (Next.js, the AI SDK, AI Gateway, Vercel Sandbox, Vercel Workflow / the open-source Workflow SDK, Vercel Connect) is **context** that eve composes on top of — referenced where eve depends on it, but **not separately studied**. Claims below stay close to what the eve source supports.

## Attributes

- **What they ship (studied here)**: **eve** — "the framework for building agents" ([[sources/vercel--eve#README]]). An agent is authored as a directory under `agent/` (markdown instructions + TypeScript tools/channels/connections/subagents/schedules), and eve compiles it into a durable, HTTP-served, multi-channel agent. Distributed as the npm package `eve` with the CLI `eve` (`npx eve@latest init`), Apache-2.0, on GitHub at `vercel/eve` ([[sources/vercel--eve#root]]).
- **What eve is built on (Vercel primitives, context not separately studied)**: the open-source **Workflow SDK** (durable, resumable, crash-safe sessions — workflow-sdk.dev), **Vercel Sandbox** (per-session microVM isolation for the agent's `/workspace`), **Vercel AI Gateway** (model routing + provider fallback), and **Vercel Connect** (managed OAuth/MCP credential brokering) ([[sources/vercel--eve#docs-execution-model]], [[sources/vercel--eve#docs-sandbox]], [[sources/vercel--eve#docs-agent-config]], [[sources/vercel--eve#docs-connections]]). "All critical agent infrastructure works out of the box, no gluing point solutions together" is the explicit pitch; at preview, "eve runs only on Vercel" with other platforms "coming."
- **What they ship (context, unstudied)**: **Next.js** (the framework eve is positioned against as "Next.js for agents"), the **AI SDK** (`ai` package — eve's model layer), the **Workflow SDK**, **Vercel Sandbox**, **AI Gateway**, **Vercel Connect**, and the Vercel deployment platform.
- **Distribution channels**: npm (`eve`), GitHub (`github.com/vercel/eve`, incl. GitHub Discussions for community), the docs site (`eve.dev/docs`, with `llms.txt` / `sitemap.md` / `agents.md` machine surfaces), and `vercel.com/eve`.
- **Position in ecosystem**: a **platform/infra company entering the agent-framework layer** — distinct from the wiki's model labs (Anthropic, OpenAI) and individual skill authors (Garry Tan, Matt Pocock). eve competes at the *harness/runtime* tier (Claude Code, Codex CLI, OpenClaw) rather than the *skill/plugin* tier — which is exactly why it's valuable here: it's the first artifact that lets us inspect a real harness instead of taking the "~200-line thin loop" claim on faith ([[patterns/structural/thin-harness-fat-skills]]).
- **House style (discernible from one source)**: **convention over configuration, taken from the web framework into the agent domain** ("the files are the interface"; identity from path; no registry — [[sources/vercel--eve#docs-introduction]]); **durability as a default, not a feature**; **safety defaults that fail closed** for auth but stay *permissive* for tools/egress unless configured (a deployer-responsibility posture — [[sources/vercel--eve#docs-responsible-use]]); and an unusually **rigorous, agent-readable docs+dev discipline** (37 docs bundled into the package; `docs:check` validates the code snippets *inside* the docs; `AGENTS.md` codes the team's own "nothing is done until tests pass" rule — [[sources/vercel--eve#AGENTS.md]], [[sources/vercel--eve#docs-check]]).

## Artifacts produced

### Projects
- [[artifacts/projects/eve]] — the eve framework: filesystem-first authoring, a durable runtime, a default harness with a built-in toolbelt, channels for many surfaces, sandboxes, subagents/remote-agents, schedules, connections, hooks, dynamic capabilities, and first-class evals. The wiki's first ingested **agent framework / harness**. ([[sources/vercel--eve#root]])

### Concepts originated / popularized
- [[concepts/filesystem-first-agent-framework]] — *grounds (primary):* "an agent is a directory; a file's location says what it does, and its path usually gives it a name… there is no separate registry to keep in sync" ([[sources/vercel--eve#docs-introduction]], [[sources/vercel--eve#docs-project-layout]]). Convention-over-configuration (the Next.js/Rails idea) ported to agents; eve is the purest in-wiki instance.
- [[concepts/durable-agent-execution]] — *grounds (primary):* "an eve session is a durable conversation… it can run for days and survives process restarts and redeploys without any work on your part," via session/turn/step checkpointing on the Workflow SDK and durable **parked work** ([[sources/vercel--eve#docs-execution-model]]). Durability as the substrate of the agent loop, not an add-on.

## Design philosophy (discernible from artifacts)

- **The directory is the interface.** Capability is declared by *where a file lives*; eve discovers the tree and derives every identity from the path, so "the result stays readable before it runs" ([[sources/vercel--eve#docs-introduction]], [[sources/vercel--eve#docs-project-layout]]). The same convention-over-configuration bet that made Next.js's `pages/` legible, aimed at agents.
- **Durable by default.** The runtime — not the author — owns the loop, the checkpoints, and the resume. "You don't write workflow code directly"; tools/channels/hooks never touch the workflow primitives ([[sources/vercel--eve#docs-execution-model]]). Long-running, human-gated, crash-surviving agents are the baseline, not an advanced mode.
- **A framework-owned harness with a swappable everything-else.** eve ships the loop + a built-in toolbelt (`bash`/file/`web_*`/`todo`/`ask_question`/`agent`/`load_skill`/`connection_search`) and lets you override, disable, or extend each tool by filename — keeping capability in fat markdown skills + thin typed tools while the harness stays generic ([[sources/vercel--eve#docs-default-harness]]).
- **Secrets stay on the trusted side.** A hard app-runtime/sandbox boundary: the model drives work through tool calls and results, "never by holding a credential or reaching the runtime directly"; credentials are brokered at the firewall, channel signatures verified in constant time, auth fails closed ([[sources/vercel--eve#docs-security-model]]).
- **Docs are the product surface for agents.** The full doc set ships *inside the package* so a coding agent reads the version-matched docs locally; the repo even ships a pointer `SKILL.md`. One source of truth, many surfaces ([[sources/vercel--eve#README]], [[sources/vercel--eve#SKILL.md]], [[patterns/composition/single-source-multi-surface-distribution]]).

## Source citations

- [[sources/vercel--eve#root]] — the eve framework + repo (Apache-2.0, public preview 2026-06-17, 1,671★ as-of 2026-06-20).
- [[sources/vercel--eve#docs-introduction]] — "the files are the interface"; filesystem-first; durable by default.
- [[sources/vercel--eve#docs-execution-model]] — session/turn/step durability on the Workflow SDK; parked work.
- [[sources/vercel--eve#docs-default-harness]] — the default harness + built-in toolbelt + override/disable.
- [[sources/vercel--eve#docs-security-model]] — the app-runtime/sandbox trust boundary; credential brokering; fail-closed auth.
- [[sources/vercel--eve#AGENTS.md]] — the eve team's own coding/test discipline (the "what we'd steal" dev posture).

## Open questions / what to study next

- **The Vercel primitive stack underneath eve.** The **Workflow SDK** (durability), **Vercel Sandbox** (microVM isolation), **AI Gateway** (model routing), and **Vercel Connect** (OAuth brokering) are each a substantial system eve leans on but that we've only seen through eve's lens. The Workflow SDK in particular (open-source, workflow-sdk.dev) is the engine behind [[concepts/durable-agent-execution]] and a strong standalone ingest candidate.
- **eve's actual harness loop vs the "~200-line thin harness" claim.** eve *is* an ingested harness, but it's a full framework (durability, compaction, sandbox proxying, channels), not a 200-line loop. Reading `packages/eve/src/harness/` would let us measure the real shape of a production harness against [[patterns/structural/thin-harness-fat-skills]]'s thinness claim — the open question that pattern has carried since creation.
- **Is "Next.js for agents" a durable analogy or marketing?** Convention-over-configuration is the shared bet; whether eve's directory conventions reach the same "obvious in hindsight" status as Next.js routing is the thing to watch as adoption (and the star count) moves.
- **Lock-in vs portability.** "eve runs only on Vercel" at preview, yet the Workflow SDK is open-source and "not inherently tied to Vercel," with a future "supported way to provide a different Workflow world" ([[sources/vercel--eve#docs-execution-model]]). How portable the runtime really becomes is the key strategic question for anyone adopting it.
- **eve vs Codex / Claude Code head-to-head.** With eve ingested, the wiki finally has a harness to compare against the skill/plugin layers it already studies. A QUERY comparing eve's harness + evals + durability against Codex Goals ([[artifacts/projects/codex-goals]]) and the Claude Code plugin runtime would be high-value.
