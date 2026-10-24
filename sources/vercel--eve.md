---
domain: sources
type: repo
url: https://github.com/vercel/eve
retrieved: 2026-06-20
snapshot-location: sources/vercel--eve/
upstream-commit: bfc71912547779375777525d5a0f8b130e061fc7
last-reviewed: 2026-06-20
---

# vercel/eve — "The Framework for Building Agents"

> Vercel's open-source, **filesystem-first** framework for **durable** backend AI agents (Apache-2.0, public preview 2026-06-17, npm `eve`, CLI `eve`). An agent is a *directory*: instructions in markdown, tools/channels/connections/subagents/schedules as TypeScript files, identity derived from path — and eve compiles it into a durable, HTTP-served, multi-channel agent built on Vercel's Workflow SDK + Sandbox + AI Gateway + Connect. The wiki's **first ingested agent framework / harness** (the long-missing "thin harness" middle layer), and **first Vercel source**.

*Done when it passes the [page checklist](_definition-of-done.md).*

## Snapshot details

- **Retrieved**: 2026-06-20
- **Where it lives in this wiki**: `sources/vercel--eve/` (live local clone, `.git/` intact, git-ignored, listed in `repos.manifest.tsv` — rebuildable via `sources/clone-all.sh`).
- **Upstream URL**: https://github.com/vercel/eve (docs site: https://eve.dev/docs)
- **Upstream identifier**: commit `bfc71912547779375777525d5a0f8b130e061fc7` (HEAD of 2026-06-19 10:33 -0400). Apache-2.0. Monorepo (pnpm + turbo), Node ≥24. Releases tagged through `eve@0.11.7` at clone time.
- **Repo shape**: monorepo — `packages/eve` (the framework + `eve` CLI, the published package; `src/` carries `harness/`, `discover/`, `compiler/`, `runtime/`, `execution/`, `sandbox/`, `channel/`, `evals/`, `context/`, `client/`, `react|vue|svelte/`, `public/`) · `packages/eve-catalog` (internal) · `apps/{docs,fixtures,frameworks,templates}` · `docs/` (37 published `.md`/`.mdx` files, ~55.7K words — the canonical doc set, also bundled into the npm package at `node_modules/eve/docs`) · `e2e/` (fixture-owned `eve eval` suites) · `scripts/` (guard-invariants, check-docs, check-doc-snippets, …) · root `SKILL.md` + `AGENTS.md` + `CONTRIBUTING.md` + `.changeset/`.
- **Extraction method**: full `git clone`; docs read from the clone's `docs/` tree (verbatim source markdown). Cross-checked against the live docs site's `sitemap.md` and `agents.md`.

## Anchor map

Every claim that cites this source uses a `#anchor` suffix registered here. Anchors point at files inside the clone (the `docs/` tree, repo-root files, or `packages/`).

- `#root` — the repo / framework as a whole
- `#README` — repo-root `README.md` — the pitch ("filesystem-first framework for durable AI agents"), the `agent/` tree, `npx eve@latest init`, minimal example, and the note "the `eve` package includes its full documentation… `node_modules/eve/docs`"
- `#SKILL.md` — repo-root `SKILL.md` — eve ships *as an Agent Skill* whose body is a **pointer**: "always read the bundled docs… `node_modules/eve/docs/`… Do not rely on this skill for guidance" (single-source-of-truth distribution)
- `#AGENTS.md` — repo-root `AGENTS.md` — the eve team's own dev discipline: 8 coding principles (public APIs need docs+tests; small modules; wrap third-party deps / keep `nitro` the only runtime dep; pre-1.0 prefer breaking changes; derive names from paths; name definitions for the protocol; all runtime in the `eve` package; comment why-not-what), 4 test tiers (unit/integration/scenario/e2e), `guard:invariants` ("baselines may only shrink"), `docs:check`, changeset rules, and "Nothing is done until typecheck, lint, fmt, build, and the tests all pass" + "If you cannot run a relevant suite… say so explicitly rather than claiming verification passed"
- `#docs-readme-index` — `docs/README.md` — the public mental model, the 20-step recommended reading order, "the runtime shape" (channels normalize input + own `continuationToken`; the harness does one unit of AI work and decides continue/wait/finish; runtime persists state + streams + owns workflow orchestration), and the two identifiers (`continuationToken` vs `sessionId`)
- `#docs-introduction` — `docs/introduction.mdx` — "an agent is laid out as files," "the files are the interface," "no separate registry to keep in sync," the same flow for web/terminal/Slack, "durable by default" (Workflow SDK)
- `#docs-project-layout` — `docs/reference/project-layout.md` — "identity comes from the path. You never write a `name` or `id` field," the slot table (`tools/`/`skills/`/`connections/`/`channels/`/`hooks/`/`schedules/`/`subagents/`/`sandbox/`/`lib/`/`instructions`), "only two sources reach the workspace" (`skills/` + `sandbox/workspace/**`), `eve info` discovery diagnostics
- `#docs-typescript-api` — `docs/reference/typescript-api.md` — the `define*` helper table (defineAgent/Tool/Dynamic/Mcp.../Channel/Skill/Instructions/Hook/Schedule/State/Sandbox/Instrumentation/RemoteAgent/Eval), the `ctx` members, and the per-import map
- `#docs-execution-model` — `docs/concepts/execution-model-and-durability.md` — session/turn/step nesting; "every turn runs as a durable workflow" on the Workflow SDK; checkpoint at step boundaries; resume-from-last-completed-step after crash/redeploy; "completed steps never re-run… a step interrupted mid-execution re-runs, so make non-idempotent side effects idempotent, or gate them with approval"; **parked work** (HITL/OAuth/subagent suspends with no compute held); message delivery/queueing caveat; append-only history
- `#docs-default-harness` — `docs/concepts/default-harness.md` — "the default harness is what every eve agent ships with… the framework-owned agent loop plus built-in tools"; compaction (`thresholdPercent` 0.9 default); the 11 built-in tools table + "Where it runs" column; override (same slug + spread `eve/tools/defaults`) / disable (`disableTool()` sentinel) / author-new; the opt-in `ExperimentalWorkflow`
- `#docs-context-control` — `docs/concepts/context-control.md` — the levers: `instructions.md` (always-on), `skills/` (on-demand, `load_skill`), workspace/sandbox (via tools, not the prompt), subagents (delegated context), `defineDynamic` (per-session); "eve does not inline the entire authored surface into the prompt… a shallow workspace hint and runtime tools to inspect deeper"
- `#docs-security-model` — `docs/concepts/security-model.md` — the **app-runtime vs sandbox trust boundary** table (secrets/Node only app-side; sandbox isolated `/workspace`, no `process.env`); the `charge_card` trace ("the model sees only `{ ok: true }`"); credential brokering at the firewall; connection tokens cached per-step, never serialized; channel verification ("verify signatures in constant time," "don't trust body-supplied identity"); "authored markdown is data" (`---js` engines disabled, no `eval`); "auth fails closed" (`placeholderAuth`/401); the pre-production checklist
- `#docs-sessions-streaming` — `docs/concepts/sessions-runs-and-streaming.md` — the two handles (`continuationToken` resume vs `sessionId`/`runId` stream); the NDJSON event vocabulary (session/turn/step/action/input.requested/subagent/compaction/authorization/...); reconnect via `startIndex`; `GET /eve/v1/info`; the 4-step dispatch order (channel handler → metadata projection → hooks → dynamic resolvers)
- `#docs-tools` — `docs/tools/overview.mdx` — "a tool is a typed action… runs in your app runtime with full `process.env`, not in the sandbox"; filename = tool name; Zod `inputSchema`; `needsApproval`; `toModelOutput` (project the model's view down while channels keep the full output); "do not return secrets… from tools"
- `#docs-hitl` — `docs/tools/human-in-the-loop.md` — approvals (`always()`/`once()`/`never()`/predicate) + questions (`ask_question`), both riding the same durable `session.waiting` pause/resume; "gating a side effect on approval is also how you make non-idempotent work safe across replays"
- `#docs-skills` — `docs/skills.mdx` — "a skill is a model-loadable procedure that follows the `SKILL.md` convention… progressive disclosure, the same model the broader **Agent Skills standard** uses, so a skill authored against that standard ports over as-is"; `load_skill`; "the description is a routing hint, not a label"; flat markdown vs packaged vs `defineSkill`; skills are per-agent scoped; `ctx.getSkill`
- `#docs-subagents` — `docs/subagents.mdx` — the built-in `agent` tool (copy of itself, shared sandbox) vs declared subagents (own dir, **isolation boundary**: inherits nothing, `description` required for delegation routing); every subagent lowered to a `{ message, outputSchema? }` tool; "do not rely on subagent delegation by itself as an approval boundary"
- `#docs-sandbox` — `docs/sandbox.mdx` — "the agent's isolated bash environment… every eve agent has exactly one"; `ctx.getSandbox()` handle (`run`/`spawn`/read/write/`resolvePath`/`setNetworkPolicy`); seeding `/workspace`; the four backends (`vercel`/`docker`/`microsandbox`/`justbash`) + `defaultBackend()` priority; `bootstrap` (template-scoped) vs `onSession` (session-scoped) lifecycle; network policy (`allow-all` default → `deny-all`/allow-list); credential brokering via per-domain `transform`
- `#docs-schedules` — `docs/schedules.mdx` — cron file per `schedules/<name>`; markdown "task mode" (fire-and-forget, can't park) vs handler `run` form (`receive`/`waitUntil`/`appAuth`, can park); root-only; Vercel Cron Jobs / Nitro scheduled tasks; the dev dispatch route
- `#docs-instructions` — `docs/instructions.mdx` — "the always-on system prompt, the agent's permanent identity"; markdown vs `instructions.ts` (build-time, captured into the manifest); instructions-vs-skills table (always-on vs on-demand); "instructions never run code"; the AI-disclosure deployer note
- `#docs-agent-config` — `docs/agent-config.md` — `defineAgent` fields (model via AI Gateway id or provider `LanguageModel`; default `anthropic/claude-sonnet-4.6`; `compaction`; `modelOptions`; `experimental.codeMode`; `outputSchema`; `build.externalDependencies`)
- `#docs-connections` — `docs/connections.mdx` — `defineMcpClientConnection` / `defineOpenAPIConnection`; "the model never sees a connection's URL or credentials"; `connection__search` + `connection__<connection>__<tool>` qualified names; static-token vs no-auth vs headers vs interactive OAuth (Vercel Connect `connect()` / self-hosted `defineInteractiveAuthorization`); tool filters; per-connection approval; `ctx.requireAuth()` on mid-call 401
- `#docs-dynamic-capabilities` — `docs/guides/dynamic-capabilities.md` — `defineDynamic` resolves tools/skills/instructions at runtime keyed on `ctx.session.auth`/channel metadata; resolver events (`session.started`/`turn.started`/`step.started`); "`execute` must be an inline function" (survives step boundaries); per-principal capability sets
- `#docs-dynamic-workflows` — `docs/guides/dynamic-workflows.md` — the experimental `Workflow` tool: the model authors JavaScript that orchestrates its *own* subagents as one durable step, in a QuickJS sandbox that's an **allowlist not a denylist** ("the sandbox cannot read files… because those are not present, not because each one is blocked")
- `#docs-hooks` — `docs/guides/hooks.md` — `defineHook` event subscribers (observe-only, after the event is durably recorded); `toolResultFrom` typed narrowing; the emit→hooks→dynamic-resolvers execution order; a thrown hook surfaces as `turn.failed`
- `#docs-state` — `docs/guides/state.md` — `defineState(name, initial)` durable per-session memory (`get()`/`update()`), survives step boundaries; never shared with subagents; state-vs-connection-storage boundary
- `#docs-session-context` — `docs/guides/session-context.md` — `ctx.session` (auth.current/initiator, id, turn, parent lineage), `ctx.getSandbox()`, `ctx.getSkill()`, `defineState`; "safe places" vs "unsafe places" (throws at module top level); the per-step context-container lifecycle
- `#docs-remote-agents` — `docs/guides/remote-agents.md` — `defineRemoteAgent` calls a separately-deployed eve agent as a subagent; same lowered `{ message, outputSchema? }` shape; outbound auth (`vercelOidc`/`bearer`/`basic`); async dispatch + durable callback (parent parks until the remote posts a terminal callback)
- `#docs-channels-overview` — `docs/channels/overview.mdx` — "a channel is the edge adapter… normalizes platform input, owns the `continuationToken`, decides delivery"; the default eve HTTP channel; `defineChannel` custom channels; the platform table (Slack/Discord/Teams/Telegram/Twilio/GitHub/Linear/web/CLI/cron/custom); "uses the Chat SDK's card-builder components… does not use the Chat SDK's runtime"
- `#docs-evals-overview` — `docs/evals/overview.mdx` — `defineEval` in `evals/*.eval.ts` (file path = identity); "evals exercise the same HTTP surface your users hit"; the `t` driver/assert context; the three assertion surfaces (run-level methods / `t.check` deterministic builders / `t.judge.autoevals.*` LLM-judge); gate vs soft severity; `eve eval [--strict]`
- `#docs-getting-started` — `docs/getting-started.mdx` — `npx eve@latest init`; minimal 2-file agent; the curl session/stream/follow-up walkthrough; the `<CopyPrompt>` "set up an eve agent for the user" coding-agent prompt
- `#docs-cli` — `docs/reference/cli.md` — `eve init/info/build/start/dev/link/deploy/eval/channels`; the `.eve/` build artifacts; the recommended loop (edit → `eve info` → `eve dev` → `eve build` → `eve start`)
- `#docs-responsible-use` — `docs/responsible-use.md` — "as the deployer, it is your responsibility…"; permissive defaults (tool execution without approval where omitted; sandbox egress not deny-all); "do not rely on model behavior alone to prevent sensitive or irreversible actions"
- `#packages-src` — `packages/eve/src/` — the framework module layout (`harness/`, `discover/`, `compiler/`, `runtime/`, `execution/`, `sandbox/`, `channel/`, `evals/`, `context/`, `protocol/`, `public/`, `react|vue|svelte/`) — evidence that "the harness" and "discovery" are real first-class modules, not just doc framing
- `#monorepo` — `package.json` + `pnpm-workspace.yaml` + `turbo.json` — the monorepo build (turbo `build`/`test:{unit,integration,scenario,e2e}`/`typecheck`/`docs:check`/`guard:invariants`), Node ≥24, pnpm
- `#changesets` — `.changeset/` + the `AGENTS.md` "Changesets" section + git tags (`eve@0.9.8`…`eve@0.11.7`) — every PR touching the published package needs a changeset; pre-1.0 `patch` for fixes+features, `minor` only for public-API breaks; release automation owns the bump (`changeset version` / `changeset publish`)
- `#guard-invariants` — `scripts/guard-invariants.mjs` + `scripts/guard-invariants-baseline.json` + the `AGENTS.md` rule "fix the violation rather than editing the baseline — baselines may only shrink" (a forward-only floor)
- `#docs-check` — `scripts/check-docs.mjs` + `check-doc-snippets.mjs` + `check-doc-mdx.mjs` (the `docs:check` gate that validates doc frontmatter/nav and *the code snippets inside the docs*)
- `#github-stars` — popularity signal captured at retrieval (see below)

## Why we cite this

Claims about: a **filesystem-first / convention-over-configuration** agent framework (an agent *is* a directory; identity from path; no registry — [[concepts/filesystem-first-agent-framework]]); **durable agent execution** (session/turn/step, checkpoint, crash-resume, parked work on the Workflow SDK — [[concepts/durable-agent-execution]]); the **default harness** as a concrete, ingestable artifact (the agent loop + built-in toolbelt + compaction + override/disable) — the long-missing "thin harness" middle of [[patterns/structural/thin-harness-fat-skills]]; **single-source multi-surface** distribution via channels (one agent codebase → web/Slack/Discord/Teams/Telegram/Twilio/GitHub/Linear/CLI/cron) and via shipping its own docs as the source of truth (README + bundled `node_modules/eve/docs` + a pointer `SKILL.md` + the docs site); the **latent/deterministic split** as an architectural boundary (latent model loop vs deterministic typed tools in the trusted app runtime); **Agent Skills standard** compatibility (progressive disclosure, `load_skill`, "ports over as-is"); per-principal **dynamic capability resolution** (`defineDynamic`); **evidence-gated completion** (the team's own "nothing is done until tests pass" + e2e `eve eval` gate; evals as a first-class framework primitive); **version-as-update-gate** (changesets own the bump); the **complexity ratchet** (`guard:invariants` baselines-may-only-shrink, `docs:check` validating snippets); and a strong agent **security model** (app-runtime/sandbox trust boundary, credential brokering, constant-time channel verification, fail-closed auth, markdown-as-data).

## Popularity signals

- **Signal type**: github-stars / forks (via `gh api repos/vercel/eve`)
- **Value at snapshot**: **1,671 ★**, **106 forks**, 59 open issues. Apache-2.0, TypeScript. Repo created **2026-06-16**; last push 2026-06-20. ~10 contributors at launch (Vercel core: ijjk, AndrewBarba, JohnPhamous, timolins, …).
- **As-of**: 2026-06-20 (≈4 days after public preview — a *fast-rising* signal; expect rapid change, re-check before relying on the number)
- **Launch reach (secondary)**: covered at launch as "Next.js for agents" (The New Stack, 2026-06-17; Vercel's own `vercel.com/eve`). Vercel's framework pedigree (Next.js) is the credibility backdrop for the velocity. Public preview under the Vercel beta terms; "for now, eve runs only on Vercel" with other platforms "coming."

## Related sources

- [[sources/agentskills--specification]] — the **Agent Skills open standard** eve's `skills/` conform to ("a skill authored against that standard ports over as-is" — [[sources/vercel--eve#docs-skills]]); eve is a *harness* that runs standard skills, the runtime counterpart to the spec.
- [[sources/anthropic--plugins-reference]] / [[sources/openai--plugins]] — the **plugin/marketplace** packaging layer of the convergent spec ([[concepts/convergent-agent-plugin-spec]]); eve is the *framework/runtime* layer beneath skills, a different axis (it has channels/sandbox/durability, not a marketplace).
- [[sources/openai--using-goals-in-codex]] — Codex Goals' evidence-gated completion is the behavioral cousin of eve's "nothing is done until tests pass" dev discipline ([[sources/vercel--eve#AGENTS.md]]) and its evals-as-primitive ([[sources/vercel--eve#docs-evals-overview]]).
- [[sources/garrytan--thin-harness-fat-skills]] — names the **thin harness / fat skills** architecture; eve is the wiki's first *ingested* harness, letting us finally inspect the middle layer that essay only describes.
- [[sources/garrytan--gbrain]] / [[sources/every--compound-engineering-plugin]] — fellow examples of single-source multi-surface distribution and the complexity ratchet, on the skill/plugin axis rather than the framework axis.

## Related wiki pages

- [[creators/vercel]] — author of the framework
- [[artifacts/projects/eve]] — the artifact page (the framework as a runnable thing)
- [[concepts/filesystem-first-agent-framework]] — the headline idea this source grounds
- [[concepts/durable-agent-execution]] — the durability model this source grounds
- [[patterns/structural/thin-harness-fat-skills]] — eve is the first ingested **harness**
- [[patterns/composition/single-source-multi-surface-distribution]] — channels + docs-as-source

## Related investigations

- [[artifacts/projects/humanlayer]] / [[concepts/agent-control-plane]] — related investigation of task/session orchestration and event persistence; [[sources/humanlayer--humanlayer#event-log]] and [[sources/humanlayer--humanlayer#runtime-boundary]] provide a comparison boundary to Eve’s [[concepts/durable-agent-execution]], without asserting equivalent step-replay guarantees.
