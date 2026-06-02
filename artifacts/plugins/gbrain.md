---
domain: artifacts
type: plugin
name: gbrain
creator: "[[creators/garry-tan]]"
source: "[[sources/garrytan--gbrain]]"
ecosystem: claude-code (via MCP), OpenClaw (native), Cursor/Windsurf/etc (via MCP)
discovered-via: user-curated (Sidney named explicitly)
status: active
last-reviewed: 2026-05-21
ingestion-mode: speedrun
version-at-snapshot: 0.36.4.0
components:
  skills: 43 in skillpack scaffold (+ shared deps + excluded-from-install)
  commands: gbrain CLI (~30+ subcommands inferred from README excerpts)
  agents: none documented at top level
  hooks: none documented
  mcp-servers: 1 (gbrain serve — stdio + http variants)
popularity-signals:
  - signal: github-stars
    value: ~14,000
    as-of: 2026-05 (per Vectorize.io article)
    source: "[[sources/garrytan--gbrain#README]] (TODO: snapshot live count via gh api)"
  - signal: release-momentum
    value: ~5,000 stars in first 24 hours (April 5, 2026 launch)
    as-of: 2026-05-21
    source: "[[sources/garrytan--gbrain#README]]"
  - signal: press-coverage
    value: Vectorize.io review, Little Might explainer, Saeloun blog
    as-of: 2026-05-21
---

# gbrain

> **One-line:** Garry Tan's hybrid vector + auto-extracting-graph memory system for AI agents. Ships as CLI + MCP server + skillpack scaffold for OpenClaw/Hermes/etc. The production memory layer behind Garry's own agents.

## Attributes (speedrun bullets)

- **Target user**: agent operators who hit the "smart but forgetful" wall. Originally engineered for Garry's OpenClaw + Hermes; now generalized.
- **Three install shapes** ([[sources/garrytan--gbrain#README]]):
  1. Skillpack scaffold for OpenClaw/Hermes — `gbrain skillpack scaffold --all`
  2. CLI standalone — `bun install -g github:garrytan/gbrain` + `gbrain init --pglite`
  3. MCP server — `gbrain serve` (stdio) or `gbrain serve --http` (with OAuth 2.1 + admin dashboard)
- **Database options**: PGLite (zero-config, ~2 sec init), Postgres + pgvector (Supabase), thin-client mode.
- **Default embedding** (v0.36.2.0): ZeroEntropy `zembed-1` @ 1280d via Matryoshka. Reranker: `zerank-2`. Claims 2.2× faster + 2.6× cheaper than OpenAI. Configurable via `gbrain config set embedding_model <provider:model>`.
- **Production scale claim** ([[sources/garrytan--gbrain#README]]): 17,888 pages, 4,383 people, 723 companies, 21 cron jobs running autonomously — Garry's own brain.
- **License**: MIT ([[sources/garrytan--gbrain#root]] LICENSE).

## Relationships

- **Creator**: [[creators/garry-tan]]
- **Source**: [[sources/garrytan--gbrain#root]]
- **Composes with**: [[artifacts/plugins/gstack]] via `/setup-gbrain` and `/sync-gbrain` skills
- **Target platforms**: `garrytan/openclaw`, `garrytan/hermes` (not yet cataloged), any MCP client
- **Extends**: SKILL.md format with custom manifest fields (`shared_deps`, `excluded_from_install`, `contracts.contextEngines`) — see [[sources/garrytan--gbrain#openclaw-plugin-json]]

## Composition strategy

- **Three-shape product**: same engine, three packaging surfaces (skillpack / CLI / MCP). Each surface targets a different consumer. This is a *distribution-shape* pattern, not a code pattern.
- **`RESOLVER.md` as skill router**: `skills/RESOLVER.md` is read once per request; the agent picks one skill, executes. Replaces Claude's auto-trigger heuristic with explicit routing. ([[sources/garrytan--gbrain#skills-resolver]])
- **Underscore-prefixed convention files**: `_AGENT_README.md`, `_brain-filing-rules.md` (+`.json`), `_output-rules.md`, `_friction-protocol.md` — universal rules that prefix every skill. ([[sources/garrytan--gbrain#skills-AGENT_README]])
- **Manifest extensions beyond Anthropic spec** ([[sources/garrytan--gbrain#openclaw-plugin-json]]):
  - `shared_deps`: skills listed here are dependencies shared across all installed skills
  - `excluded_from_install`: bootstrap/migration skills hidden from end-user install
  - `contracts.contextEngines: ["gbrain-context"]`: declares the plugin *provides* a named context engine that other plugins can consume
- **`AGENTS.md` as agent-first install protocol**: separate from `CLAUDE.md`, with a 9-step flow. Agent must read this before installing. Claude Code reads `CLAUDE.md` automatically. ([[sources/garrytan--gbrain#AGENTS.md]])
- **`[AGENT]`-marked cost-matrix banner**: on install, gbrain prints a 9-cell matrix (search mode × downstream model). The agent is *required* to relay it to the operator and confirm before continuing. Silent acceptance is explicitly prohibited because "cost spread between corners is 25×." ([[sources/garrytan--gbrain#AGENTS.md]])
- **`llms.txt` + `llms-full.txt`**: dual discoverability files at root — concise map + same map with core docs inlined. Designed for LLM ingestion. ([[sources/garrytan--gbrain#llms-txt]] [[sources/garrytan--gbrain#llms-full-txt]])
- **Built-in eval framework**: `evals/` dir + sibling `garrytan/gbrain-evals` repo with BrainBench scorecards. Self-claim: P@5 49.1%, R@5 97.9% on a 240-page corpus. ([[sources/garrytan--gbrain#README]])
- **Autopilot loop**: `gbrain doctor --remediate --yes --target-score 90 --max-usd 5` — agent drives the brain to a quality score by itself, refuses to spend past a cap. Cron-driveable.

## Patterns demonstrated (proposed)

- **Three-shape distribution** — same engine packaged as skillpack + CLI + MCP. Lets one product reach three consumer surfaces. Need 2nd example.
- **Skill-router file (RESOLVER.md)** — explicit routing replaces description-based auto-triggering. Need 2nd example. (Note: this is a *very different* skill-selection philosophy than Anthropic's.)
- **Underscore-prefixed universal rules** — `_AGENT_README`, `_brain-filing-rules`, `_output-rules` apply to every skill in the pack. Need 2nd example.
- **Agent-first install protocol** — `AGENTS.md` separate from `CLAUDE.md`, treats LLM as the primary install reader. Need 2nd example.
- **`[AGENT]`-marked operator-decision banner** — forces human-in-the-loop on cost-impacting choices. Pattern: encode H.I.T.L. as a protocol the agent must follow, not as a UI prompt.
- **Quantitative skill evals shipped with the pack** — BrainBench-style scorecards as part of the artifact, not a side project.

## Source citations

- [[sources/garrytan--gbrain#README]] — three install shapes, production scale, BrainBench numbers, ZeroEntropy defaults, autopilot loop
- [[sources/garrytan--gbrain#AGENTS.md]] — install protocol for agents, 9-cell cost matrix requirement
- [[sources/garrytan--gbrain#openclaw-plugin-json]] — manifest extensions (shared_deps, excluded_from_install, contracts.contextEngines)
- [[sources/garrytan--gbrain#llms-txt]] [[sources/garrytan--gbrain#llms-full-txt]] — LLM discoverability files

## What we'd steal

- **`llms.txt` + `llms-full.txt` dual files** at root of any artifact that wants LLM consumers. Trivially cheap, makes the artifact discoverable to crawling agents.
- **`AGENTS.md` separate from `CLAUDE.md`** for any artifact that needs an agent-driven install. Recognizes LLMs as a real persona.
- **`[AGENT]`-marked banners requiring operator confirmation** before cost-bearing choices. This is the cleanest H.I.T.L. pattern I've seen — declarative, scoped, enforceable.
- **`shared_deps` in the manifest** so common rules don't get duplicated across skills.
- **`excluded_from_install`** to hide bootstrap skills from end users without splitting into multiple repos.
- **`contracts.contextEngines`** as a typed declaration of what the plugin *provides* to other plugins — a contract-based composition primitive.
- **`RESOLVER.md` skill router** as an alternative to description-auto-matching when you control all the skills in the pack (and want determinism).
- **Underscore-prefix universal rules files** so they sort to the top and are obviously special.
- **Quantitative evals shipped with the artifact** as proof of quality.

## Weird/surprising thing

The `[AGENT]`-marked cost-matrix banner is *required* — the agent **must** relay it to the operator before continuing. This is a protocol-level human-in-the-loop, encoded as an instruction the agent must obey rather than a config option the user can flip. It's also extremely on-brand for an artifact built by a YC CEO: respect for the operator's wallet is non-negotiable.

The second surprising thing: gbrain ships an OpenClaw plugin manifest (`openclaw.plugin.json`), not a Claude Code `.claude-plugin/plugin.json`. It's pointed at a *different runtime* (OpenClaw) as primary, with Claude Code as a secondary consumer via MCP. This reframes "what is a plugin" — it's a multi-runtime artifact now, not a Claude-Code-only one.

## Open questions / what's unclear

- How does `RESOLVER.md` route in practice — is the agent told "read RESOLVER.md, pick one, then load only that skill"? That's a major break from Claude's auto-trigger model.
- Do other plugins consume `contracts.contextEngines: ["gbrain-context"]`, or is this aspirational?
- Is the 9-step `AGENTS.md` install actually followed reliably by Claude/Codex/Cursor? (Empirical test needed.)
- What's the relationship to `garrytan/openclaw`? Is OpenClaw itself worth cataloging as a "runtime"?
- The `_brain-filing-rules.json` — what does it specify? Schema for where pages go, probably. Worth a separate look.
