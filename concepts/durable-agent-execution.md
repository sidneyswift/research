---
domain: concepts
type: concept
name: durable-agent-execution
creators: ["[[creators/vercel]]"]
sources: ["[[sources/vercel--eve]]"]
status: emerging
last-reviewed: 2026-06-20
popularity-signals:
  - signal: adoption
    value: "eve makes durable sessions the default, built on the open-source Workflow SDK; Codex Goals independently persist thread-scoped objective state"
    as-of: 2026-06-20
    source: "[[sources/vercel--eve#docs-execution-model]]"
---

# durable-agent-execution

> **One-line:** Run an agent conversation as a **durable workflow** — nest work as session → turn → step, **checkpoint at every step**, replay completed steps after a crash/redeploy instead of redoing them, and **park** (suspend holding no compute) whenever the agent waits on a human, an OAuth flow, or a child — then resume exactly where it left off, even days later.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): compiled truth on top + an append-only `## Timeline`.*

## What it is

A model of agent execution where **durability is the substrate, not a feature you add**. An eve session "is a durable conversation. It can run for days and survives process restarts and redeploys without any work on your part" ([[sources/vercel--eve#docs-execution-model]]). Work nests in three levels — **session** (the whole long-lived conversation/task), **turn** (one user message and all the work it triggers), **step** (a durable checkpoint: one model call + its tool calls). Every turn runs as a durable workflow (eve builds on the open-source **Workflow SDK**); eve "checkpoints progress and serializes durable state at each step boundary," so "your code runs inside a managed step… [and] tools, the sandbox, and subagents feel synchronous even though the session underneath them is durable." Two consequences define the model:

1. **Crash-resume by replay.** "Completed steps never re-run; eve replays the recorded result. A step interrupted mid-execution re-runs" — so a crash/timeout/redeploy mid-turn picks up from the last completed step rather than replaying the whole turn ([[sources/vercel--eve#docs-execution-model]]).
2. **Parked work.** When the agent must wait (a human approval, an interactive OAuth sign-in, a long-running subagent), "the turn parks durably. The workflow suspends and holds no compute until the input it's waiting on arrives… even if that's much later" ([[sources/vercel--eve#docs-execution-model]], [[sources/vercel--eve#docs-hitl]]).

## Where it came from

Durable execution is a known backend idea (workflow engines — Temporal, AWS Step Functions, and Vercel's own Workflow SDK). The contribution captured here is making it the **default execution model for an AI agent loop**, so that human-in-the-loop pauses, crash recovery, and day-long sessions are the floor rather than bespoke plumbing. [[creators/vercel]]'s **eve** is the grounding source: durability is owned by the runtime, and "you don't write workflow code directly… [workflow primitives] are an implementation detail of eve's runtime layer; channels, tools, and hooks never touch them" ([[sources/vercel--eve#docs-execution-model]]). There is independent, partial convergence: OpenAI's **Codex Goals** persist objective state as "thread state" that survives across turns and resumes ([[artifacts/projects/codex-goals]], [[sources/openai--using-goals-in-codex#thread-scoped-state]]) — the same instinct (persist the agent's work so it can stop and continue) at the *objective* grain rather than the *session* grain.

## Why it matters

Most agent failure modes at the edges are durability failures: a long task dies on a redeploy and loses everything; a "wait for the user to approve" pause means holding a process (and tokens, and a socket) open for hours; a crash mid-charge either double-charges or silently drops. Making execution durable converts those from application problems into framework guarantees — and it *changes what agents can be*: an agent that can park for days enables genuine human-in-the-loop (approve this refund tomorrow), genuine long-running autonomy (a migration that spans deploys), and genuine async delegation (fire a remote subagent, suspend, resume on its callback). It also forces a discipline the docs state plainly: because an interrupted step re-runs, **side effects must be idempotent or gated** — "make non-idempotent side effects like charges or emails idempotent, or gate them with approval" ([[sources/vercel--eve#docs-execution-model]]). That one rule is the price of replay-based durability, and naming it is half the value.

## Evidence & claims

- *"An eve session is a durable conversation… survives process restarts and redeploys without any work on your part."* — asserted as a default guarantee — [[sources/vercel--eve#docs-execution-model]]
- *"Completed steps never re-run; eve replays the recorded result. A step interrupted mid-execution re-runs."* — the replay contract (demonstrated as the runtime model) — [[sources/vercel--eve#docs-execution-model]]
- *Parked work "holds no compute until the input it's waiting on arrives, even if that's much later."* — the suspend/resume model behind HITL, OAuth, and remote subagents — [[sources/vercel--eve#docs-execution-model]], [[sources/vercel--eve#docs-hitl]], [[sources/vercel--eve#docs-remote-agents]]
- *Durable per-session state* (`defineState`) survives step boundaries — demonstrated — [[sources/vercel--eve#docs-state]]
- *Honest caveat:* eve does **not** maintain a durable FIFO queue of user messages; concurrent sends to one session are best-effort, "so don't rely on concurrent sends… behaving like a typical ordered chat queue" — a stated limit of the durability guarantee — [[sources/vercel--eve#docs-execution-model]]
- The streaming side is durable too: "every event is recorded before a step completes, so the whole stream is replayable" (reconnect via `startIndex`) — [[sources/vercel--eve#docs-sessions-streaming]]

## Patterns demonstrated

- [[patterns/behavioral/evidence-gated-completion]] — durable parking is what makes "stop and wait for the evidence / the human" cheap; the completion decision can suspend indefinitely without burning compute. Citation: [[sources/vercel--eve#docs-hitl]].
- [[patterns/behavioral/latent-vs-deterministic-split]] — the replay model *forces* the split onto side effects: non-idempotent (deterministic, must-not-double-fire) work must be made idempotent or gated, separating it from the freely-replayable latent loop. Citation: [[sources/vercel--eve#docs-execution-model]].
- *Candidate pattern (tracked here):* **idempotency-or-approval gate for replayable steps** — a concrete authoring rule that any checkpoint/replay runtime needs. eve states it; Codex Goals' conservative continuation is a cousin. Promote when a 2nd runtime states the same rule.

## Tensions & counter-arguments

- **Durability ≠ ordering.** eve foregrounds that it is *not* a message queue — concurrent sends to one session are best-effort, and deterministic behavior requires "send one user turn at a time and wait for `session.waiting`" ([[sources/vercel--eve#docs-execution-model]]). Durable-but-unordered is a subtle contract that's easy to over-trust.
- **Replay leaks into your code.** "Durable by default, nothing to configure" is true *until* a non-idempotent side effect re-fires on an interrupted-step replay. The guarantee shifts a burden onto the author (idempotency/approval) rather than removing it.
- **Engine lock-in.** Durability is provided by the Workflow SDK + (on Vercel) Vercel Workflow; eve "owns Workflow world selection" today, with pluggable worlds only promised ([[sources/vercel--eve#docs-execution-model]]). The guarantee is real but currently tied to one platform.
- **n=1 as a *default*.** Workflow engines are mature, but "durable execution as the default agent loop" is, in this wiki, grounded in one framework. Codex Goals shows the instinct converging at a different grain, but the *session-level* default is eve's.

## Timeline (append-only)

- 2026-06-17 — eve ships with durable sessions as the default, built on the open-source Workflow SDK ([[sources/vercel--eve#docs-execution-model]]).
- 2026-06-20 — Ingested as the grounding source; noted Codex Goals' thread-scoped persistence as an independent, objective-grain cousin ([[artifacts/projects/codex-goals]]).

## Related

- [[concepts/agent-control-plane]] / [[artifacts/projects/humanlayer]] — comparison at a different durability boundary: persistent task/session identities, an append-only event log, and continuation plumbing support work surviving individual sessions. The inspected HumanLayer orchestration does not establish Eve-style completed-step checkpoint replay or exactly-once effects, and some provider execution lives in external SDKs. — [[sources/humanlayer--humanlayer#HP01-task-policy]], [[sources/humanlayer--humanlayer#HP02-session-identity]], [[sources/humanlayer--humanlayer#event-log]], [[sources/humanlayer--humanlayer#runtime-boundary]].
- [[concepts/filesystem-first-agent-framework]] — the authoring half of eve's design; this is the runtime half.
- [[concepts/completion-contract]] / [[artifacts/projects/codex-goals]] — Codex Goals persist *objective* state across turns; durable-agent-execution persists *session/turn/step* state. Same instinct, different grain.
- [[patterns/behavioral/evidence-gated-completion]] — durable parking makes evidence-gated stops cheap.
- [[artifacts/projects/eve]] — the embodying artifact.

## What we'd steal

**Exhaustive ledger** (★ = highest-value, clearly portable):

- ★ **Session → turn → step as the durability grain.** Checkpoint at the *step* (one model call + its tools); replay completed steps; re-run only the interrupted one. A clean, copyable nesting for any agent runtime. ([[sources/vercel--eve#docs-execution-model]])
- ★ **Park-and-resume holding zero compute.** Model every wait (approval, OAuth, child) as a durable suspension, not a held process. This is what makes day-long human-in-the-loop affordable. ([[sources/vercel--eve#docs-execution-model]], [[sources/vercel--eve#docs-hitl]])
- ★ **"Interrupted steps re-run → make side effects idempotent or gate them."** The single rule that makes replay-based durability safe. State it explicitly wherever you checkpoint. ([[sources/vercel--eve#docs-execution-model]])
- ★ **Durability owned by the runtime, invisible to authored code.** "You don't write workflow code directly" — tools/channels/hooks never touch workflow primitives. Keep the hard part in the framework. ([[sources/vercel--eve#docs-execution-model]])
- **A replayable event stream** (every event recorded before the step completes; reconnect by index). Durability for the *observation* side, not just execution. ([[sources/vercel--eve#docs-sessions-streaming]])
- **Durable per-session state with a tiny API** (`defineState(name, initial)` → `get()`/`update()`, survives step boundaries, never shared with subagents). Short-term agent memory without standing up a store. ([[sources/vercel--eve#docs-state]])
- **State the limits.** "This is durable but *not* an ordered message queue" — being explicit about what durability does *not* give you prevents the worst over-trust bugs. ([[sources/vercel--eve#docs-execution-model]])

## Open questions

- **What does the Workflow SDK actually guarantee?** eve is the lens; the engine (open-source, workflow-sdk.dev) is the real subject — its consistency model, "worlds" abstraction, and storage are unstudied and a strong standalone ingest.
- **Does a second agent runtime make durability the default?** That's the gate from `emerging` to confirmed. Codex Goals persist objective state but aren't a full durable-session runtime; LangGraph/Temporal-backed agents would be the comparison.
- **How is "budget"/idle measured, and how does parking interact with model context?** A turn that parks for days then resumes — does it re-establish context, recompact, re-read files? eve says compaction resets read-before-write tracking ([[sources/vercel--eve#docs-default-harness]]); the full resume-after-long-park behavior is worth tracing.
- **Idempotency in practice.** The rule is stated; how often do real eve agents get it wrong, and is there tooling (beyond approval gating) to detect non-idempotent steps before they double-fire?

## Recovery boundary comparison — 2026-11-02

[[artifacts/projects/dsh-superagent-prototype]] persists domain changes/effect intent and resumes interrupted Assignments; this is distinct from replaying arbitrary external mutations exactly once. [[artifacts/projects/kody]] separates keyed execute observation/replay from workflow retry that re-executes package code. Both make [[patterns/behavioral/context-is-not-authority]] relevant to recovery: what resumes must retain a legitimate basis. [[sources/deepseek-ai--dsh-superagent-prototype#effects]], [[sources/deepseek-ai--dsh-superagent-prototype#execution]], [[sources/kody-hq--kody#execute-replay]], [[sources/kody-hq--kody#workflow-implementation]]

## API design connection — 2026-11-04

[[concepts/business-platform-api-design]] — A durable-operation API exposes accepted work and results; request idempotency alone does not make worker/provider effects exactly once.

## Cross-system API research — 2026-11-04

[[analyses/frontier-and-business-api-design]] compares nine documented systems and preserves the distinction between capability intent, presentation, execution and business outcome. [[concepts/agent-api-learning-and-evolution]] separates training familiarity from current interface context and observable task performance. The synthesis remains draft; no runtime or agent-success guarantee is added to this page.

## MCP research connection — 2026-11-04

[[concepts/mcp-extension-architecture]] distinguishes durable Tasks status/input/result retrieval from internal step checkpoint/replay. Creation must be durable before returning a handle, but cancellation is cooperative and domain-effect idempotency remains separate. [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#tasks]], [[sources/modelcontextprotocol--mcp-core-and-extensions-docs#task-errors-security]]

## Simulation replay is a different guarantee — 2026-11-03

[[artifacts/projects/tibo-dog]] reports recomputing a deterministic game run from inputs to validate a high score. This is **simulation replay for verification**, not evidence of crash-safe agent execution or exactly-once external effects. Reusing the idea for an agent evaluation needs captured nondeterministic responses and controlled side effects; replaying a payment or publication is not equivalent to replaying game state. That adaptation is our boundary analysis, not an implementation claim about the game. [[sources/poteto--tibo-engineering#deterministic-replay]]

## A long-running thread is not recovery evidence — 2026-11-04

Matt Pocock proposes a persistent local domain thread coordinating a factory of sandboxed workers; the reusable coordination principle lives in [[concepts/agent-control-plane#principle-persistent-domain-orchestration-with-sandboxed-execution]]. The screenshot specifies no checkpoint, replay, restart or effect-deduplication mechanism. It is a useful architecture proposal, not a new demonstrated example of this page's execution-durability guarantees. [[sources/mattpocock--domain-orchestrator-factory#domain-orchestrator]] [[sources/mattpocock--domain-orchestrator-factory#provenance-limits]]

## Conversation recovery versus effect recovery — 2026-11-04

[[artifacts/projects/codex]] persists canonical history separately from query metadata and reconstructs history against valid compaction boundaries. A remote executor reconnect is limited by destination retention; this does not establish the step-replay/exactly-once properties described for other runtimes. Compare the recovery unit and already-issued external effects explicitly. [[sources/openai--codex#storage]] [[sources/openai--codex#replay]] [[sources/openai--codex#executor]]

## Open Inspect: Checkpoint, retirement and uncertain execution

[[artifacts/projects/background-agents]] distinguishes recoverable workspace capture from confirmed retirement of the source execution. Generation/operation fences reject stale results; interrupted prompts are failed and continuation paused rather than automatically replayed. Ordinary non-destructive checkpoints have a narrower settlement path than shutdown. This complements Eve’s durable-step model: preserving a filesystem cannot undo an external effect or establish its safe replay. [[sources/open-inspect--background-agents#generation-fence]] [[sources/open-inspect--background-agents#checkpoint]] [[sources/open-inspect--background-agents#continuation]] [[sources/open-inspect--background-agents#shutdown-design]]

## SuperPlane — 2026-11-04

[[artifacts/projects/superplane]] persists event/queue/execution state before notification and recovers through pending-state scans. Runner completion hashes make identical terminal reports idempotent, not arbitrary remote effects. Finalization waits for tracked work to drain. Critically, copied node configuration coexists with live graph routing: specify the snapshot unit before claiming deterministic replay. [[sources/superplanehq--superplane#event-routing]] [[sources/superplanehq--superplane#runner-completion]] [[sources/superplanehq--superplane#finalization]] [[sources/superplanehq--superplane#execution-state]]

## Wider documentation application — 2026-11-05

[[concepts/developer-documentation-design]] now studies architecture/operational records, migration states, executable examples and delivery/evaluation boundaries. [[projects/writing-amazing-developer-docs/platform-documentation-system]] is the proposed application; no new vendor runtime guarantee or confirmed implementation example is claimed.

## Agent Habitat comparison — 2026-11-06

[[concepts/agent-habitat-architecture]] adds a proposed **security-state recovery** contract: restore attenuations, spent budgets, consumed approvals and action history with work progress. Journaled model replay is not universal exactly-once external effect; reconcile unknown outcomes. [[sources/replit--agent-habitat-architecture#durability]]

## Vercel Schedules — 2026-11-06

[[artifacts/projects/vercel-schedules]] separates timer occurrences, queue delivery and workflow recovery. Stable execution IDs do not make external effects exactly once; scheduler occurrence expiry and queue retention are separate windows. The newer experimental eve docs distinguish callback dispatch from agent completion. [[sources/vercel--schedules-docs#timing]] [[sources/vercel--schedules-docs#queue-contract]] [[sources/vercel--schedules-docs#eve-occurrence]]

## Memory consolidation — 2026-11-07

[[concepts/agent-memory-consolidation]] adds distinct recovery contracts: store creation versus successful dreaming, canceled versus residual in-flight usage, local write acknowledgment versus committed sync, and nightly retry versus complete input coverage. [[sources/anthropic--agent-memory-support#dream-lifecycle]] [[sources/anthropic--agent-memory-support#dream-cancellation]] [[sources/anthropic--agent-memory-support#self-hosted-conflicts]] [[sources/anthropic--agent-memory-support#dynamic-nightly]]

## T3 Code — 2026-11-07

[[artifacts/projects/t3code]] adds a pinned source case: Separate atomic accepted intent, process-bound versus replay-safe effects, retained receipt versus pruned replay history, and new restart-continuation intent. Provider/file rollback remains sequential. [[sources/pingdotgg--t3code#rt-replay-classification]] [[sources/pingdotgg--t3code#rt-dedup-lifetime]] Source/test inspection only; no hosted/provider outcome or new model score claimed.

## Proactive discernment — 2026-11-08

[[concepts/proactive-agent-discernment]]: heartbeat availability and scheduled follow-up are design triggers, not evidence of durable wakeups, deduplicated effects or completed user work. No retry, cancelation or overlap behavior is specified in the source. [[sources/rubriclabs--always-on-agents#wake]] [[sources/rubriclabs--always-on-agents#communication]]
