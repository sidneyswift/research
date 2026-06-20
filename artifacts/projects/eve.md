---
domain: artifacts
subdomain: projects
type: project
name: eve
creator: "[[creators/vercel]]"
source: "[[sources/vercel--eve]]"
ecosystem: eve # Vercel's own runtime (not Claude Code / Codex); deploys on Vercel
discovered-via: official-docs # eve.dev/docs, then the vercel/eve repo
status: active # public preview / beta, Apache-2.0, releases through eve@0.11.7
last-reviewed: 2026-06-20
popularity-signals:
  - signal: github-stars
    value: "1,671★ / 106 forks (Apache-2.0); repo created 2026-06-16, public preview 2026-06-17"
    as-of: 2026-06-20
    source: "[[sources/vercel--eve#github-stars]]"
---

# eve

> **One-line:** Vercel's open-source, **filesystem-first** framework for **durable** backend AI agents — you author an agent as a *directory* (markdown instructions + typed TypeScript tools/channels/connections/subagents/schedules), and eve discovers it, runs a framework-owned model loop (the "harness") with a built-in toolbelt, and serves it as a durable, crash-resumable, multi-channel agent on Vercel's Workflow SDK + Sandbox + AI Gateway + Connect. "Like Next.js for web apps, but for agents."

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): eve as it reads across its 37 bundled docs + repo, written as distilled judgment — not a transcription of the docs. Shape: compiled truth on top.*

**Scope note:** grounded in [[sources/vercel--eve]] (the `vercel/eve` repo + its bundled `docs/`, commit `bfc7191`, public preview). eve is in **beta** under the Vercel beta terms; APIs may change before GA. The Vercel primitives eve composes (Workflow SDK, Sandbox, AI Gateway, Connect) are referenced but **not separately ingested**.

## Attributes

- **What it is**: an **agent framework + runtime** — the wiki's first artifact at the *harness/runtime* tier rather than the *skill/plugin* tier. You write capabilities under `agent/`; eve "runs the model loop, persists every session, and serves the agent over HTTP and platform channels" ([[sources/vercel--eve#docs-getting-started]]). Published as npm `eve` + the `eve` CLI; Apache-2.0; deploys on Vercel ([[sources/vercel--eve#root]]).
- **Target user**: developers building **backend/production agents** who want durability, sandboxing, multi-channel delivery, auth, and evals "out of the box, no gluing point solutions together" — explicitly framed as **"Next.js for agents"** ([[sources/vercel--eve#README]]).
- **The authoring surface (the `agent/` directory)** — each concern has a fixed home ([[sources/vercel--eve#docs-project-layout]]):
  - `instructions.md` / `.ts` — the always-on system prompt (required on the root). ([[sources/vercel--eve#docs-instructions]])
  - `agent.ts` — `defineAgent` runtime config (model, compaction, experimental). Optional; default model `anthropic/claude-sonnet-4.6`. ([[sources/vercel--eve#docs-agent-config]])
  - `tools/<name>.ts` — typed actions (`defineTool`, Zod schema), run in the trusted **app runtime**. ([[sources/vercel--eve#docs-tools]])
  - `skills/<name>.md` (or packaged `SKILL.md`) — load-on-demand procedures, **Agent Skills-standard** markdown. ([[sources/vercel--eve#docs-skills]])
  - `connections/<name>.ts` — external MCP / OpenAPI servers (`defineMcpClientConnection` / `defineOpenAPIConnection`). ([[sources/vercel--eve#docs-connections]])
  - `channels/<name>.ts` — edge adapters (HTTP default, Slack, Discord, Teams, Telegram, Twilio, GitHub, Linear, custom). ([[sources/vercel--eve#docs-channels-overview]])
  - `sandbox/` — the per-agent isolated `/workspace` (backends, network policy, seeded files). ([[sources/vercel--eve#docs-sandbox]])
  - `subagents/<id>/` — declared specialist child agents (own dir, own tools/skills/sandbox). ([[sources/vercel--eve#docs-subagents]])
  - `schedules/<name>.ts` — cron jobs (root-only). ([[sources/vercel--eve#docs-schedules]])
  - `hooks/`, `lib/`, `instrumentation.ts` — event subscribers, shared code, telemetry. ([[sources/vercel--eve#docs-hooks]], [[sources/vercel--eve#docs-typescript-api]])
  - `evals/*.eval.ts` (app root, sibling of `agent/`) — scored checks (`defineEval`). ([[sources/vercel--eve#docs-evals-overview]])
- **The path-derived naming rule**: "Identity comes from the path. You never write a `name` or `id` field on a `define*` call." `agent/tools/get_weather.ts` → tool `get_weather`; `agent/connections/linear.ts` → connection `linear`. "There is no separate registry to keep in sync." ([[sources/vercel--eve#docs-project-layout]], [[sources/vercel--eve#docs-introduction]])
- **The default harness** (ships with every agent, no imports): the framework-owned agent loop + built-in tools — `bash`, `read_file`, `write_file`, `glob`, `grep` (proxy into the sandbox), `web_fetch`, `web_search`, `todo`, `ask_question`, `agent`, `load_skill`, `connection_search` — plus automatic **compaction** at `thresholdPercent` (0.9 default). Override a built-in by authoring its slug (+ spread `eve/tools/defaults`), disable it with a `disableTool()` sentinel, or add new tools. ([[sources/vercel--eve#docs-default-harness]])
- **Install footprint**: `npx eve@latest init my-agent` (scaffolds, installs deps, inits Git, opens the dev TUI) or `eve init .` into an existing app; manual is `npm install eve ai zod`. Node ≥24. The package **bundles its full docs** at `node_modules/eve/docs`. ([[sources/vercel--eve#docs-getting-started]], [[sources/vercel--eve#README]])
- **License / status**: Apache-2.0; public preview (beta) since 2026-06-17; releases through `eve@0.11.7` at clone; runs on Vercel today (other platforms "coming"). ([[sources/vercel--eve#root]])

## Relationships

- **Creator**: [[creators/vercel]] — the wiki's first platform/infra creator (vs. model labs and individual skill authors).
- **Source**: [[sources/vercel--eve#root]]
- **Embodies**: [[concepts/filesystem-first-agent-framework]] (the agent-as-directory / convention-over-configuration headline) and [[concepts/durable-agent-execution]] (session/turn/step checkpointing + parked work).
- **First ingested harness for**: [[patterns/structural/thin-harness-fat-skills]] — eve is the *middle layer* that pattern describes but had never ingested. Its `packages/eve/src/harness/` + the "The Harness" doc are a real, inspectable loop ([[sources/vercel--eve#docs-default-harness]], [[sources/vercel--eve#packages-src]]). It both **grounds** the pattern (framework-owned generic loop + fat markdown skills + thin typed tools) and **complicates** it (a production harness is a full framework, not "~200 lines").
- **Demonstrates**: [[patterns/composition/single-source-multi-surface-distribution]] (channels: one agent → many surfaces; docs-as-single-source), [[patterns/behavioral/latent-vs-deterministic-split]] (latent model loop vs deterministic typed tools across the trust boundary), [[patterns/composition/resolver-routing-table]] (skill `description` as routing hint + `defineDynamic` per-principal resolution), [[patterns/behavioral/skill-as-method-call]] (the `define*` helper family), [[patterns/behavioral/evidence-gated-completion]] (the team's "nothing is done until tests pass" + e2e `eve eval` gate), [[patterns/quality-bar/version-as-update-gate]] (changesets own the bump), [[patterns/quality-bar/complexity-ratchet]] (`guard:invariants` baselines-may-only-shrink; `docs:check` validates doc snippets).
- **Runs**: [[sources/agentskills--specification|Agent Skills]]-standard skills "as-is" — eve is a **harness** for the open skill standard, the runtime counterpart to the spec ([[sources/vercel--eve#docs-skills]]). Distinct from [[concepts/convergent-agent-plugin-spec]]'s *plugin/marketplace* layer: eve has channels/sandbox/durability, not a marketplace.
- **Sibling-in-spirit**: [[artifacts/projects/codex-goals]] (OpenAI) — both are runtime/behavioral surfaces of an agent tool; eve is the whole harness, Codex Goals one feature of one. eve's dev discipline ([[sources/vercel--eve#AGENTS.md]]) and Codex Goals' evidence-gated completion are cousins.
- **Built on (context, unstudied)**: Vercel **Workflow SDK** (durability), **Sandbox** (isolation), **AI Gateway** (models), **Connect** (OAuth/MCP brokering).

## What problem it solves

The "glue tax" of building a production agent. A naive agent is a model-call loop, but a *real* one needs durability (survive crashes/redeploys mid-task), human-in-the-loop pauses that can wait days, isolated code execution, secret handling, multi-channel delivery, auth, and a way to test the whole thing — and assembling those from point solutions is most of the work. eve's bet is that all of that is **framework infrastructure**, not application code: "all critical agent infrastructure works out of the box, no gluing point solutions together" ([[sources/vercel--eve#README]]). It also solves a *legibility* problem the same way Next.js did for web apps — "the directory tells you what the agent can do" before it runs, because every capability is a file in a known slot with a path-derived name and no registry to drift ([[sources/vercel--eve#docs-introduction]], [[sources/vercel--eve#docs-project-layout]]).

## How it works (the mechanism the source describes)

- **Discovery → compile → run.** eve walks `agent/`, derives identities from paths, and compiles the authored surface into a manifest (`.eve/`), which the runtime loads. `eve info` prints what was discovered + diagnostics; `packages/eve/src/` has real `discover/`, `compiler/`, `runtime/`, and `harness/` modules ([[sources/vercel--eve#docs-project-layout]], [[sources/vercel--eve#docs-cli]], [[sources/vercel--eve#packages-src]]).
- **The durable loop.** Work nests as **session → turn → step**; every turn runs as a durable workflow on the Workflow SDK and checkpoints at each step. "Completed steps never re-run; eve replays the recorded result. A step interrupted mid-execution re-runs, so make non-idempotent side effects idempotent, or gate them with approval." Work that must wait (approval, OAuth, a subagent) **parks** durably — the workflow suspends holding *no compute* until the input arrives, "even days later" ([[sources/vercel--eve#docs-execution-model]]).
- **The harness drives the model.** The framework-owned loop shows the model its instructions + advertised skills + tools + history, runs tool/subagent calls, compacts when the window fills, and decides continue/wait/finish — the author "never writes that loop" ([[sources/vercel--eve#docs-default-harness]], [[sources/vercel--eve#docs-readme-index]]).
- **Two contexts, one boundary.** Authored tools run in the **trusted app runtime** with `process.env`; the model's shell/file work runs in an **isolated sandbox** (`/workspace`, no secrets). Even `bash`/`write_file` live in the app runtime and *proxy* into the sandbox. The model "drives the work through tool calls and their results, never by holding a credential" ([[sources/vercel--eve#docs-security-model]], [[sources/vercel--eve#docs-sandbox]]).
- **Channels make it portable.** A channel normalizes platform input into a message, owns the `continuationToken`, and decides delivery — so "your weather tool does not need to know whether the question came from a browser or from Slack." The default eve HTTP channel exposes a stable session API (`POST /eve/v1/session`, a reconnectable NDJSON stream, follow-ups by continuation token) ([[sources/vercel--eve#docs-channels-overview]], [[sources/vercel--eve#docs-sessions-streaming]]).
- **Context control levers.** `instructions` (always-on) · `skills/` (on-demand via `load_skill`, progressive disclosure) · workspace/sandbox (inspected via tools, not pasted into the prompt) · subagents (delegated context) · `defineDynamic` (resolve tools/skills/instructions per caller from `ctx.session.auth`) ([[sources/vercel--eve#docs-context-control]], [[sources/vercel--eve#docs-dynamic-capabilities]]).
- **Delegation.** The built-in `agent` tool spins a copy of itself (shared sandbox, fresh history); declared subagents are isolated specialists lowered to a `{ message, outputSchema? }` tool; remote agents call another deployment via durable callback; the experimental `Workflow` tool lets the model orchestrate its own subagents from JS in a QuickJS allowlist sandbox ([[sources/vercel--eve#docs-subagents]], [[sources/vercel--eve#docs-remote-agents]], [[sources/vercel--eve#docs-dynamic-workflows]]).
- **Evals are first-class.** `defineEval` files in `evals/` drive the *same HTTP surface users hit* and grade with three surfaces — run-level methods, deterministic `t.check` builders, and an LLM `t.judge` — with gate-vs-soft severity, run by `eve eval --strict` in CI ([[sources/vercel--eve#docs-evals-overview]]).

## Patterns demonstrated

- [[patterns/structural/thin-harness-fat-skills]] — **eve is the first *ingested harness*.** It realizes the three-layer split as a framework: a generic framework-owned loop + built-in toolbelt (the harness middle), fat **Agent Skills-standard markdown** on top (`load_skill`, progressive disclosure), and thin deterministic **typed tools** at the bottom (`defineTool`, app runtime). It both grounds the pattern *and* tests its "~200-line thin" claim — eve's harness is a full framework. Citation: [[sources/vercel--eve#docs-default-harness]], [[sources/vercel--eve#docs-skills]], [[sources/vercel--eve#packages-src]].
- [[patterns/composition/single-source-multi-surface-distribution]] — **two ways at once.** (1) **Channels**: one agent codebase, "the same flow whether a message comes from a web app, the terminal, or Slack" → web/Slack/Discord/Teams/Telegram/Twilio/GitHub/Linear/CLI/cron. (2) **Docs-as-source**: the canonical `docs/` is the single source, *bundled into the npm package* (`node_modules/eve/docs`) + a pointer `SKILL.md` + the docs site + `llms.txt`/`sitemap.md`/`agents.md`, with `docs:check` guarding drift. Citation: [[sources/vercel--eve#docs-introduction]], [[sources/vercel--eve#docs-channels-overview]], [[sources/vercel--eve#SKILL.md]], [[sources/vercel--eve#docs-check]].
- [[patterns/behavioral/latent-vs-deterministic-split]] — the **trust boundary *is* the latent/deterministic line**: the latent model loop drives via tool calls; deterministic typed tools run in the trusted app runtime; exact/secret work never happens "in the model's head." Evals echo it (deterministic `t.check` vs `t.judge`). Citation: [[sources/vercel--eve#docs-security-model]], [[sources/vercel--eve#docs-tools]].
- [[patterns/composition/resolver-routing-table]] — the skill **`description` is the resolver** ("a routing hint, not a label… write it as the task that should trigger activation"), and `defineDynamic` is *per-principal* routing (resolve which tools/skills/instructions a caller can even see). No routing *eval* ships, like most non-Garry examples. Citation: [[sources/vercel--eve#docs-skills]], [[sources/vercel--eve#docs-dynamic-capabilities]].
- [[patterns/behavioral/skill-as-method-call]] — the entire `define*` family (`defineTool`/`defineSkill`/`defineAgent`/`defineSchedule`/…) is "same template, different arguments → different capability," and subagents/remote-agents share one lowered `{ message, outputSchema? }` signature so they compose as pipeline steps. Citation: [[sources/vercel--eve#docs-typescript-api]], [[sources/vercel--eve#docs-subagents]].
- [[patterns/behavioral/evidence-gated-completion]] — the eve team's own `AGENTS.md`: "Nothing is done until typecheck, lint, fmt, build, and the tests all pass," e2e = real `eve eval` against real models, and "if you cannot run a relevant suite… say so explicitly rather than claiming verification passed." Evals as a shipped framework primitive make this enforceable for *users'* agents too. Citation: [[sources/vercel--eve#AGENTS.md]], [[sources/vercel--eve#docs-evals-overview]].
- [[patterns/quality-bar/version-as-update-gate]] — changesets own the version; every PR touching the published package needs one; pre-1.0 `patch` for fixes+features, `minor` only for public-API breaks; `changeset publish` ships. Citation: [[sources/vercel--eve#changesets]].
- [[patterns/quality-bar/complexity-ratchet]] — `guard:invariants` enforces machine-checkable code invariants where "baselines may only shrink" (a forward-only floor), and `docs:check` validates the *code snippets inside the docs* so examples can't rot. Citation: [[sources/vercel--eve#guard-invariants]], [[sources/vercel--eve#docs-check]].

## Source citations

- Filesystem-first / agent-as-directory / no registry — [[sources/vercel--eve#docs-introduction]], [[sources/vercel--eve#docs-project-layout]]
- Durable session/turn/step + parked work — [[sources/vercel--eve#docs-execution-model]]
- The default harness + built-in toolbelt + override/disable + compaction — [[sources/vercel--eve#docs-default-harness]]
- App-runtime/sandbox trust boundary + credential brokering + fail-closed auth + markdown-as-data — [[sources/vercel--eve#docs-security-model]]
- Channels: normalize / own continuationToken / decide delivery — [[sources/vercel--eve#docs-channels-overview]]
- Skills = Agent Skills-standard, `load_skill`, description-as-routing-hint — [[sources/vercel--eve#docs-skills]]
- Sandbox backends + network policy + lifecycle — [[sources/vercel--eve#docs-sandbox]]
- Subagents (built-in copy vs declared) + lowered tool shape — [[sources/vercel--eve#docs-subagents]]
- Connections (MCP/OpenAPI), tokens the model never sees — [[sources/vercel--eve#docs-connections]]
- Dynamic capabilities (`defineDynamic`) — [[sources/vercel--eve#docs-dynamic-capabilities]]
- Evals as a first-class primitive (three assertion surfaces, gate/soft) — [[sources/vercel--eve#docs-evals-overview]]
- The CLI + recommended loop + `.eve/` artifacts — [[sources/vercel--eve#docs-cli]]
- The team's own dev discipline (the "what we'd steal" posture) — [[sources/vercel--eve#AGENTS.md]]
- Ships its own docs as the source of truth — [[sources/vercel--eve#README]], [[sources/vercel--eve#SKILL.md]]

## What makes it great

- **It moves the harness from "claim" to "artifact."** Until eve, this wiki studied fat skills and thin tools but had to take the *harness* on faith — every example (gstack, CE, Codex skills) rode someone else's loop. eve is a real, readable harness ([[sources/vercel--eve#docs-default-harness]], [[sources/vercel--eve#packages-src]]), which is precisely the missing middle [[patterns/structural/thin-harness-fat-skills]] has flagged since creation.
- **Durability is the substrate, not a feature.** "Survives process restarts and redeploys without any work on your part," and parked work holds zero compute while it waits days for a human — with one honest caveat the docs foreground (interrupted steps re-run, so make side effects idempotent or gate them) ([[sources/vercel--eve#docs-execution-model]]). Most agent tooling bolts durability on; eve makes it the floor.
- **Convention over configuration, done with taste.** The slot table is small and total; identity is path-derived; "no registry to keep in sync"; a flat layout for tiny agents grows into the nested one. It reads like Next.js's `pages/` aimed at agents ([[sources/vercel--eve#docs-project-layout]]).
- **A coherent security model stated plainly.** The app-runtime/sandbox boundary, the `charge_card` trace, credential brokering at the firewall, constant-time channel verification, fail-closed auth, and "authored markdown is data" (no `eval` of frontmatter) are a complete, legible threat model — rare for a framework this young ([[sources/vercel--eve#docs-security-model]]).
- **Docs engineered for agents.** 37 docs bundled into the package so a coding agent reads version-matched docs locally; a `<CopyPrompt>` to hand a coding agent; `docs:check` that validates the snippets *in* the docs. The framework treats "an agent will read these" as a first-class requirement ([[sources/vercel--eve#README]], [[sources/vercel--eve#docs-getting-started]], [[sources/vercel--eve#docs-check]]).
- **Evals as a built-in, not an afterthought.** `defineEval` against the real HTTP surface, three assertion tiers, gate/soft severity, CI exit codes — "a passing eval means the agent booted, accepted a request, and produced the result you asserted" ([[sources/vercel--eve#docs-evals-overview]]).

## What we'd steal

**Exhaustive ledger** (★ = highest-value, clearly portable). Many *idea*-level steals live on [[concepts/filesystem-first-agent-framework#what-we-d-steal]] and [[concepts/durable-agent-execution#what-we-d-steal]]; these are the **framework/implementation-level** lessons specific to eve:

- ★ **Path-derived identity, no registry.** Let a file's *location* declare what it is and its *path* name it — "move or rename it and its identity moves with it." Kills the registry-drift class of bug. (We already apply this to ourselves — `index.md` is the registry; eve is the sharper, registry-*less* version.) ([[sources/vercel--eve#docs-project-layout]])
- ★ **A small, total slot table.** A finite set of named directories, each with a one-line "add it when you need…" trigger, and a `flat` shorthand that grows into the `nested` form. Legible-before-it-runs. ([[sources/vercel--eve#docs-project-layout]], [[sources/vercel--eve#docs-introduction]])
- ★ **Override-by-filename / disable-by-sentinel for built-ins.** Author the slug + spread the default to wrap it; export `disableTool()` to remove it; an unknown slug *fails the build* rather than silently no-op'ing. A clean extensibility model for any harness with a default toolbelt. ([[sources/vercel--eve#docs-default-harness]])
- ★ **Durable park-and-resume for HITL.** A human approval or OAuth that suspends the run holding *no compute* for as long as it takes, then resumes exactly where it left off — the right shape for any long-running agent loop. ([[sources/vercel--eve#docs-execution-model]], [[sources/vercel--eve#docs-hitl]])
- ★ **The replay caveat as a first-class rule.** "Completed steps never re-run; an interrupted step re-runs — so make non-idempotent side effects idempotent, or gate them with approval." A crisp, copyable rule for any checkpointed loop. ([[sources/vercel--eve#docs-execution-model]])
- ★ **`toModelOutput` — separate what the model sees from what the channel renders.** Return rich data for the UI, project a terse summary to the model. A clean lever against context bloat that most tool APIs lack. ([[sources/vercel--eve#docs-tools]])
- ★ **Ship the docs *inside the package* + a pointer skill.** `node_modules/eve/docs` (version-matched) + a `SKILL.md` whose whole job is "read the bundled docs, don't trust me." Single-source distribution aimed at coding agents. ([[sources/vercel--eve#README]], [[sources/vercel--eve#SKILL.md]])
- ★ **`docs:check` that validates the code snippets in the docs.** Examples can't rot because CI runs them. The doc-level analogue of our own `wiki-doctor`. ([[sources/vercel--eve#docs-check]])
- ★ **`guard:invariants` with "baselines may only shrink."** A forward-only floor for code invariants — fix the violation, never edit the baseline up. A mechanical complexity-ratchet. ([[sources/vercel--eve#guard-invariants]])
- **Description-as-routing-hint, stated as a rule.** "The description is a routing hint, not a label — write it as the task that should trigger activation." The single most reusable line for authoring model-invoked skills/tools. ([[sources/vercel--eve#docs-skills]])
- **Per-principal capability resolution (`defineDynamic`).** Resolve *which* tools/skills/instructions a caller can even see from their auth/tenant/flags, before the prompt is assembled — "no one else sees them." Multi-tenant context control. ([[sources/vercel--eve#docs-dynamic-capabilities]])
- **The two-handle split.** One handle to *resume* a conversation (`continuationToken`, channel-owned), a different one to *stream/inspect* (`sessionId`, runtime-owned) — "mixing them up is the most common mistake." Clean separation for any session protocol. ([[sources/vercel--eve#docs-sessions-streaming]])
- **A reconnectable, replayable event stream** (NDJSON, every event recorded before a step completes, reconnect via `startIndex`). The right default for streaming agent UIs. ([[sources/vercel--eve#docs-sessions-streaming]])
- **Allowlist-not-denylist sandboxing for model-authored code.** The `Workflow` tool runs model JS in a QuickJS realm that "cannot read files… because those are not present, not because each one is blocked." Capability-by-absence beats capability-by-blocklist. ([[sources/vercel--eve#docs-dynamic-workflows]])
- **Credential brokering at the firewall.** Inject auth headers for matching domains at the sandbox network edge so "the secret stays in the app runtime; the sandbox process only ever sees the response." A pattern for giving an agent authenticated egress without handing it the secret. ([[sources/vercel--eve#docs-security-model]], [[sources/vercel--eve#docs-sandbox]])
- **Constant-time channel verification + "don't trust body-supplied identity."** Two one-line rules that prevent forged-signature and cross-user-impersonation bugs in any webhook front door. ([[sources/vercel--eve#docs-security-model]])
- **"Authored markdown is data."** Disable code-executing frontmatter engines so a skill/schedule file can't `eval` on parse. A concrete supply-chain guard for any system that loads user/model markdown. ([[sources/vercel--eve#docs-security-model]])
- **Auth fails closed + a `placeholderAuth()` that stays closed in production.** A scaffold that's safe-by-default until you replace the placeholder. ([[sources/vercel--eve#docs-security-model]])
- **Evals that hit the real HTTP surface, with gate-vs-soft severity.** "A passing eval means the agent booted, accepted a request, and produced the result you asserted." Plus `--strict` to fail soft-threshold misses in CI. ([[sources/vercel--eve#docs-evals-overview]])
- **A `<CopyPrompt>` for coding agents in the getting-started doc.** Ship the exact prompt that tells Claude Code/Cursor how to set your thing up. Meta-but-effective onboarding. ([[sources/vercel--eve#docs-getting-started]])
- **Wrap third-party deps; keep runtime deps near-zero.** The team rule "aim to keep `nitro` as the only runtime dependency… prefer vendoring over adding runtime `dependencies`" — a supply-chain-surface discipline worth copying. ([[sources/vercel--eve#AGENTS.md]])
- **"Pre-1.0: prefer breaking changes, no legacy fallback."** A stated stance that keeps a young codebase clean — correctness/simplicity over back-compat until it earns users. ([[sources/vercel--eve#AGENTS.md]])

## Open questions / what's unclear

- **Is the harness actually "thin"?** eve is a real harness but a *fat* one (durability, compaction, sandbox proxying, channels, discovery/compile). It resolves [[patterns/structural/thin-harness-fat-skills]]'s "we've never ingested a harness" gap — and immediately complicates the "~200 lines, read-only by default" claim. Reading `packages/eve/src/harness/` to measure the real loop is the highest-value follow-up.
- **The Vercel-primitive dependency.** Durability (Workflow SDK), isolation (Sandbox), models (AI Gateway), OAuth (Connect) are each a system seen only through eve. The **Workflow SDK** is open-source and a strong standalone ingest — it's the actual engine of [[concepts/durable-agent-execution]].
- **Lock-in vs portability.** "Runs only on Vercel" at preview, but the runtime is "not inherently tied to Vercel" with a future pluggable Workflow world ([[sources/vercel--eve#docs-execution-model]]). How real that portability becomes is the key adoption question.
- **Permissive-by-default safety.** Tools execute without approval unless gated; sandbox egress is `allow-all` by default ([[sources/vercel--eve#docs-responsible-use]]). The docs are explicit that this is the deployer's responsibility — but the *default* posture (convenience over safety) is a deliberate, debatable choice worth flagging for anyone shipping on it.
- **Does eve's evals primitive become the field's "skill pack has tests"?** [[patterns/quality-bar/skill-pack-bundle]] is about per-skill bundles; eve makes *eval-the-whole-agent* a framework default. Whether that's a competing or complementary unit of testing is an open comparison.
- **Adoption trajectory.** 1,671★ four days in is a fast start on Vercel's brand; whether eve reaches "Next.js for agents" status (vs. the crowded harness field — Claude Code, Codex, OpenClaw, Mastra, LangGraph) is the thing to watch. Re-check the signal.
