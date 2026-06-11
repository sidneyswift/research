---
domain: patterns
type: pattern
name: single-source-multi-surface-distribution
category: composition
status: confirmed
last-reviewed: 2026-06-02
example-count: 4
---

# single-source-multi-surface-distribution

> Author the capability **once** — a system prompt, a skill set, an engine — then make it run on several *surfaces* without hand-forking: a Cowork plugin, a Managed Agents API template, a CLI, an MCP server, **or a competing third-party agent harness** (Codex, Cursor, Gemini, …). The wrapper differs; the brains don't. Two mechanisms qualify: the surface **references** the one source (resolved at build/deploy), *or* a converter **transforms** the one source into each surface's format — either way there is a single source of truth and a drift guard.

## Longer definition

Agent artifacts can be consumed in more than one runtime: interactively inside Cowork/Claude Code, headlessly behind an API, as a standalone CLI, or as an MCP server other clients connect to. The naive approach is to rewrite the artifact per surface, which immediately drifts. This pattern keeps a **single source of truth** for the load-bearing content (the prompt, the skills) and adds a thin per-surface *wrapper* that points at that source. The wrappers differ (a `plugin.json` vs. an `agent.yaml` vs. a CLI entrypoint); the brains don't. A build/deploy step resolves the references into whatever each surface needs.

## Mechanism

Concretely, in `anthropics/financial-services` ([[sources/anthropic--financial-services#cookbooks-README]]):

1. The canonical content lives **once**: the agent's system prompt at `plugins/agent-plugins/<slug>/agents/<slug>.md`, and skills authored in `plugins/vertical-plugins/<vertical>/skills/`.
2. **Surface A — Cowork/Claude Code plugin**: `plugins/agent-plugins/<slug>/` bundles that prompt + (vendored copies of) the skills behind a `.claude-plugin/plugin.json`. Installs interactively.
3. **Surface B — Managed Agent**: `managed-agent-cookbooks/<slug>/agent.yaml` *references* the same files via conveniences the deploy script resolves — `system: {file: ../../plugins/agent-plugins/<slug>/agents/<slug>.md}` and `skills: [{from_plugin: ../../plugins/agent-plugins/<slug>}]` ([[sources/anthropic--financial-services#cookbook-agent-yaml]]). `scripts/deploy-managed-agent.sh` inlines the prompt, uploads the skills, and `POST`s the resolved config to `/v1/agents` ([[sources/anthropic--financial-services#scripts-deploy]]).
4. A **drift guard** keeps the surfaces honest: `scripts/check.py` fails if a bundled skill copy has diverged from its vertical source ([[sources/anthropic--financial-services#scripts-check]]); `sync-agent-skills.py` re-propagates the source ([[sources/anthropic--financial-services#scripts-sync]]).

gbrain reaches the same end differently — one engine, three install shapes (skillpack scaffold, standalone CLI, MCP server) generated from one codebase ([[sources/garrytan--gbrain#README]]). The unifying move is identical: **the capability is defined once; the surface is a packaging choice, not a rewrite.**

`openai/plugins` surfaces a **third mechanism — *no transform at all***. Where FSI *references* and CE *converts*, the Codex ecosystem sometimes needs neither: because the plugin/skill grammar has **converged across labs** ([[concepts/convergent-agent-plugin-spec]]), the *same files run natively* on more than one harness. `superpowers` is the proof — one skill set (`brainstorming`, `test-driven-development`, `systematic-debugging`, …) runs on **both Codex and Claude Code** with no per-surface wrapper or converter ([[sources/openai--plugins#superpowers]]). And `plugin-eval` is the within-ecosystem case: one Node codebase exposed as **both a CLI and a Codex plugin** from a single `src/` ("both a local Node.js CLI and a Codex plugin bundle"), so there is literally one source and *no second copy to drift* ([[sources/openai--plugins#plugin-eval]]). The drift guard degenerates to identity: you don't *check* the copies match because there are none. This is single-sourcing's limit case — reference → convert → **run-natively** as the spec standardizes.

`compound-engineering` extends the pattern along a third axis — **competing harnesses you don't own**, via *conversion* rather than *reference*. The skills/agents are authored once in Claude format; `src/parsers/claude.ts` reads them and `src/converters/claude-to-<target>.ts` + `src/targets/<target>.ts` emit the native layout for ~11 platforms (Codex, Cursor, Copilot, Droid, Qwen, OpenCode, Pi, Gemini, Kiro) ([[sources/every--compound-engineering-plugin#converter]], `#install-matrix`). The drift guard is `bun run release:validate`, which fails the build if the Claude/Cursor/Codex *marketplace manifests* fall out of parity ([[sources/every--compound-engineering-plugin#release-automation]]). The distinction worth noting: FSI/gbrain keep a live *reference* the deploy step resolves; CE produces *transformed copies* per target — so CE also needs **portability rules at authoring time** (no unguarded platform env vars; per-platform tool-equivalent names) so the one source survives conversion intact ([[sources/every--compound-engineering-plugin#cross-platform-authoring]]).

## When to use

- The same agent/skill has **both an interactive and a headless consumer** (an analyst in Cowork *and* a workflow engine calling the API) — the FSI case exactly.
- You ship to **multiple runtimes you don't control** (Claude Code, Cursor, Windsurf, an internal platform) and can't maintain N hand-written copies.
- The artifact's value is the **prompt/skill content**, and the runtime is incidental — so duplicating content per surface is pure liability.
- You want a single place to make a fix and have it land everywhere on the next deploy.

## When NOT to use

- **Only one surface will ever exist.** A skills-only demonstration repo consumed in one product (cf. [[artifacts/plugins/anthropic-skills-marketplace]]) gains nothing but indirection from a wrapper layer.
- **The surfaces need genuinely different content** (different prompts, tools, or safety posture per runtime). Forcing one source then overriding everything is worse than two honest definitions.
- **No build/deploy step is acceptable.** The pattern depends on a resolver (a deploy script, a sync script) to turn references into per-surface artifacts; if every file must be runnable as-authored with zero tooling, the indirection breaks.
- **Early exploration.** Premature single-sourcing locks in an abstraction before you know whether surface B will even materialize.

## Why it works

Drift is the tax on duplicated agent content, and it compounds silently — a prompt fix lands in the plugin but not the API deployment, and now two "identical" agents behave differently in production. Single-sourcing makes drift a *build failure* instead of a latent bug ([[sources/anthropic--financial-services#scripts-check]]). It also matches how these runtimes actually differ: the difference between a Cowork plugin and a Managed Agent is almost entirely *packaging and transport* (`plugin.json` vs. `POST /v1/agents` fields), not *behavior* — so the behavior belongs in one referenced place and the packaging in thin wrappers. The FSI repo states the goal outright: "Same agent, same skills — pick your surface… there is one source of truth" ([[sources/anthropic--financial-services#cookbooks-README]]).

## Detection recipe

A falsifiable test for spotting the pattern (`## Examples` are the positive fixtures; the single-surface cases are the negative test):

- **Look for**: one canonical definition (a prompt, skill set, or engine) consumed on **≥2 surfaces** (Cowork plugin + Managed-Agent API template + CLI + MCP + a foreign harness), where each surface is a thin wrapper that **references** the source *or* a **converter** that transforms it — not a hand-edited fork.
- **Confirm with**: a **drift guard** exists — a check/sync/validate step that fails the build when surfaces diverge — and the load-bearing content lives in exactly one place. Conversion-based variants also carry authoring-time portability rules (no unguarded platform env vars, tool-equivalent names).
- **Rule out**: only one surface will ever exist (the wrapper is dead weight); surfaces that genuinely need different content or safety posture (two honest definitions beat one-source-plus-overrides); or per-surface copies with *no* drift guard — that's just duplication waiting to drift, not single-sourcing.

## Examples in this wiki

- [[artifacts/plugins/anthropic-financial-services-marketplace]] — every named agent ships as a Cowork/Claude Code plugin **and** a Managed Agents API template; the `agent.yaml` references the plugin's system prompt + skills, resolved at deploy. — citation: [[sources/anthropic--financial-services#cookbooks-README]], [[sources/anthropic--financial-services#cookbook-agent-yaml]], [[sources/anthropic--financial-services#scripts-deploy]]
- [[artifacts/plugins/gbrain]] — one memory engine packaged as three install shapes (skillpack scaffold / standalone CLI / MCP server) from a single codebase. — citation: [[sources/garrytan--gbrain#README]]
- [[artifacts/plugins/compound-engineering]] — one Claude-format skill pack **converted** to ~11 competing agent harnesses by a Bun/TS CLI, with manifest-parity drift caught by `release:validate`. The new axis (competing third-party tools) and the new mechanism (conversion + authoring-time portability rules, not live reference). — citation: [[sources/every--compound-engineering-plugin#converter]], [[sources/every--compound-engineering-plugin#release-automation]], [[sources/every--compound-engineering-plugin#cross-platform-authoring]]
- [[artifacts/plugins/pm-os]] — **the *paid product line* variant, fifth creator.** One content set (235 skills, knowledge dirs, templates) packaged as three sale-able zips — claude-code (`.claude-plugin/`), cursor (`.cursor-plugin/` + `.cursor/` configs), cowork (`workspace/` layout) — versioned together as 2.2.1. The new axis: multi-surface as *commercial* distribution (one product, three SKUs), not open-source reach. Mechanism is closest to CE's convert (per-surface packaging of shared content), without a public converter. — citation: [[sources/prodmgmt-world--pm-os#root]], [[sources/prodmgmt-world--pm-os#cursor-variant]], [[sources/prodmgmt-world--pm-os#cowork-variant]]
- [[artifacts/plugins/openai-codex-plugins-marketplace]] — **the *run-natively* (no-transform) variant**, third creator/ecosystem. `plugin-eval` is one Node `src/` exposed as **CLI + Codex plugin** (single source, no copy to drift); `superpowers` runs **one skill set on two harnesses** (Codex + Claude Code) with no wrapper or converter — possible only because the plugin grammar converged ([[concepts/convergent-agent-plugin-spec]]). Reference (FSI) → convert (CE) → run-natively (here). — citation: [[sources/openai--plugins#plugin-eval]], [[sources/openai--plugins#superpowers]]

## Counter-examples or anti-pattern

- [[artifacts/plugins/anthropic-skills-marketplace]] — ships a **single surface**: skills consumed inside Claude's products. It *could* have wrapped them as a CLI or API template but didn't — correctly, because there's one consumer and the wrapper layer would be dead weight. The lesson: multi-surface is a response to multiple *real* consumers, not a default.
- The repo's own `claude-for-msft-365-install` is deliberately **Claude-Code-only** ([[sources/anthropic--financial-services#msft-365-install]]) — admin tooling with exactly one runtime. Even inside a repo built around the pattern, the authors opt out where a second surface makes no sense.

## Related patterns

- [[patterns/structural/marketplace-as-multi-plugin]] — composes-with: multi-surface is about *runtimes*; marketplace-as-multi-plugin is about *packaging units within one runtime*. The FSI repo does both at once.
- [[concepts/convergent-agent-plugin-spec]] — *enables the run-natively variant:* when two harnesses share the plugin/skill grammar, "one source, many surfaces" needs neither reference nor conversion — the same files run on both (superpowers). The concept is the precondition for the cheapest form of this pattern.
- *(proposed)* single-source-of-truth skill vendoring with drift detection — a sub-mechanism that makes this pattern safe; tracked on [[artifacts/plugins/anthropic-financial-services-marketplace]] pending a 2nd example.

## Open questions

- When the surfaces' *tool models* differ (a Cowork plugin's `tools:` frontmatter vs. a Managed Agent's typed `agent_toolset` + `mcp_toolset` blocks), how much really stays single-sourced vs. silently re-specified in the wrapper? The `gl-reconciler` prompt declares `tools:` in frontmatter *and* the `agent.yaml` re-declares toolsets — worth auditing whether those can disagree.
- Does the drift guard cover the *prompt* as rigorously as it covers skills? `check.py` resolves `system.file` references but the skill-drift check is the explicit one.
