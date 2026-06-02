---
domain: artifacts
subdomain: projects
type: project
name: codex-goals
creator: "[[creators/openai]]"
source: "[[sources/openai--using-goals-in-codex]]"
ecosystem: codex-cli # OpenAI Codex CLI (not Claude Code)
discovered-via: official-docs
status: active # shipped in Codex CLI ≥ 0.128.0
last-reviewed: 2026-06-02
popularity-signals:
  - signal: adoption
    value: "First-party OpenAI feature, available starting Codex CLI 0.128.0"
    as-of: 2026-06-02
    source: "[[sources/openai--using-goals-in-codex#lifecycle-commands]]"
---

# codex-goals

> **One-line:** A Codex CLI feature that turns a thread into a persistent, evidence-verified objective: you set a `/goal`, and Codex keeps working ("work → check → continue or complete") until the evidence says it's done, it's blocked, or it hits a budget — under a user-controlled lifecycle.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): the Goals feature as it reads across the source, written as distilled judgment — not a transcription of the cookbook.*

**Scope note:** this page covers the **Goals feature** of OpenAI's Codex CLI, not all of Codex. We've ingested one first-party source about Goals; the rest of Codex (the broader agentic-coding tool) is **not yet studied** and is queued in [artifacts/projects/_index.md](_index.md). Claims here are grounded in [[sources/openai--using-goals-in-codex]] only.

## Attributes

- **What it does**: gives a Codex thread a *persistent objective with a completion condition*. Instead of a one-off prompt, you state an outcome + how success is verified + constraints, and Codex autonomously iterates toward it, checking evidence after each turn, until a stopping condition ([[sources/openai--using-goals-in-codex#completion-condition]], [[sources/openai--using-goals-in-codex#prompt-vs-goal-loop]]).
- **Target user**: developers using the Codex CLI for tasks "where the next step depends on what Codex learns along the way" — profiling, patching, benchmarking, reproducing flaky tests, dependency migrations, multi-step refactors, and research that yields an artifact ([[sources/openai--using-goals-in-codex#good-candidates]]).
- **Command surface** (`/goal` lifecycle — [[sources/openai--using-goals-in-codex#lifecycle-commands]]):
  - `/goal <outcome>` — activate a Goal.
  - `/goal` — view the current Goal.
  - `/goal pause` — pause autonomous work.
  - `/goal resume` — resume a paused Goal.
  - `/goal clear` — remove the current Goal.
- **Stopping conditions**: success, pause, clear, interruption, budget limit, or a blocker requiring user input ([[sources/openai--using-goals-in-codex#stopping-conditions]]).
- **Install footprint**: ships in the Codex CLI; "available starting in Codex **0.128.0**." Install/upgrade via `npm install -g @openai/codex@latest` or `brew upgrade --cask codex` ([[sources/openai--using-goals-in-codex#lifecycle-commands]]).
- **License**: the Codex CLI's own license (not stated in this source). The cookbook guide lives in `openai/openai-cookbook` (MIT).

## Relationships

- **Creator**: [[creators/openai]]
- **Source**: [[sources/openai--using-goals-in-codex#root]]
- **Embodies**: [[concepts/completion-contract]] — Goals *are* the productized completion contract.
- **Sibling Codex artifact**: [[artifacts/plugins/openai-codex-plugins-marketplace]] — the *other* studied layer of the same CLI. Goals is the **behavioral** surface (how Codex runs a long objective); the marketplace is the **packaging/distribution** surface (how Codex gets new capabilities). Same creator, same CLI, complementary layers.
- **Sibling-in-spirit**: [[artifacts/plugins/gstack]] / [[artifacts/plugins/gbrain]] (Garry Tan) — the closest in-wiki artifacts that lean on evidence-gated, parameterized agent procedures, though on Claude Code rather than Codex.

## What problem it solves

The "restate the target after every turn" tax. Without Goals, a multi-turn task means the user repeatedly typing "keep going / try the next fix / run the benchmark again / continue until this is actually done" ([[sources/openai--using-goals-in-codex#stopping-conditions]]). Those tasks "do not need a bigger prompt. They need a persistent objective" ([[sources/openai--using-goals-in-codex#root]]). Goals make that intent explicit and durable, so Codex holds the target across turns and decides for itself whether each intermediate result satisfies it — while staying inside a user-defined, budgeted, evidence-gated contract rather than running open-ended.

## How Goals work (the mechanism the source describes)

- **State**: a Goal is "persisted thread state, not global memory and not project-level instructions" — it records objective, lifecycle, budget, and progress, scoped to the thread where the relevant files/commands/diffs live ([[sources/openai--using-goals-in-codex#thread-scoped-state]]).
- **Lifecycle states**: active / paused / complete / budget-limited — these determine whether Codex may continue, must wait, or should summarize ([[sources/openai--using-goals-in-codex#completion-contract-architecture]]).
- **Continuation**: event-driven, not a loop — Codex continues "only when the thread is idle and the Goal is active and within budget," and only at safe boundaries (turn finished, nothing pending, no queued input). The dispatcher is "deliberately conservative": plan-only work doesn't trigger continuation, interruptions pause, and "if a continuation turn makes no tool call, the next automatic continuation is suppressed so Codex does not spin" ([[sources/openai--using-goals-in-codex#event-driven-continuation]]).
- **Completion**: evidence-based — "a Goal should not be marked complete because the model believes it is probably done… only after the objective is checked against the relevant files, tests, logs, benchmark output, generated artifacts" ([[sources/openai--using-goals-in-codex#evidence-based-completion]]).
- **Budget**: explicit — at the limit, Codex "should stop substantive work, summarize progress and blockers, and identify the next useful step. Reaching a budget limit is not the same as completing the objective" ([[sources/openai--using-goals-in-codex#budget-accounting]]).
- **Authority**: bounded — the model may *start* a Goal and *mark complete only when evidence supports it*; pause/resume/clear/budget transitions stay with the user or system ([[sources/openai--using-goals-in-codex#bounded-tool-authority]]).

## Patterns demonstrated

- [[patterns/behavioral/evidence-gated-completion]] — Goals are the **grounding example**: "done" is decided by checking the objective against an external verification surface, and budget-exhaustion ≠ done. Citation: [[sources/openai--using-goals-in-codex#evidence-based-completion]], [[sources/openai--using-goals-in-codex#budget-accounting]].
- [[patterns/behavioral/skill-as-method-call]] — `/goal` is a **parameterized command with a documented signature** (the six-slot template); same command, different arguments → different objective. This artifact is the **non-Garry 2nd example that promoted the pattern to confirmed**. Citation: [[sources/openai--using-goals-in-codex#goal-template]], [[sources/openai--using-goals-in-codex#six-elements]].
- [[patterns/behavioral/latent-vs-deterministic-split]] — the verification surface (tests/benchmark/build output) is the deterministic/assertable side; iteration policy ("choose the next best action") is the latent side; the completion *decision* is forced onto the assertable side. Citation: [[sources/openai--using-goals-in-codex#evidence-based-completion]].

## Source citations

- Definition + completion condition — [[sources/openai--using-goals-in-codex#completion-condition]]
- Scoped, not background autonomy — [[sources/openai--using-goals-in-codex#scoped-not-autonomy]]
- Prompt-loop vs goal-loop — [[sources/openai--using-goals-in-codex#prompt-vs-goal-loop]]
- Six-element contract + template — [[sources/openai--using-goals-in-codex#six-elements]], [[sources/openai--using-goals-in-codex#goal-template]]
- Lifecycle commands + version 0.128.0 + install — [[sources/openai--using-goals-in-codex#lifecycle-commands]]
- Evidence-based completion — [[sources/openai--using-goals-in-codex#evidence-based-completion]]
- Thread-scoped state — [[sources/openai--using-goals-in-codex#thread-scoped-state]]
- Conservative, event-driven continuation — [[sources/openai--using-goals-in-codex#event-driven-continuation]]
- Budget ≠ completion — [[sources/openai--using-goals-in-codex#budget-accounting]]
- Bounded lifecycle authority — [[sources/openai--using-goals-in-codex#bounded-tool-authority]]
- Research case study (Deep Hedging) + claim-ledger format — [[sources/openai--using-goals-in-codex#deep-hedging-casestudy]], [[sources/openai--using-goals-in-codex#claim-ledger-format]]
- When NOT to use — [[sources/openai--using-goals-in-codex#when-not-to-use]]

## What makes it great

- **It scopes its own autonomy.** The standout design choice is that "persist until done" is fenced on *four* sides at once — budget, a conservative event-driven dispatcher (with explicit anti-spin), evidence-gated completion, and user-held lifecycle authority. Most "agent keeps working" features advertise the autonomy; this one foregrounds the leash ([[sources/openai--using-goals-in-codex#completion-contract-architecture]]).
- **A documented parameter signature for a slash command.** The six-slot `/goal` template is the rare case of an agent command shipping an explicit, auditable argument structure rather than "type whatever you want" ([[sources/openai--using-goals-in-codex#goal-template]]).
- **Completion is defined as an audit, not a vibe.** For research it produces "an audit" that "separates confirmed claims, support-only evidence, blocked claims, and remaining uncertainty," with a literal ledger format — the feature *defines what finished means* rather than trusting the model's say-so ([[sources/openai--using-goals-in-codex#conclusion]], [[sources/openai--using-goals-in-codex#claim-ledger-format]]).

## What we'd steal

**Exhaustive ledger** (★ = highest-value, clearly portable). Most of the *idea*-level steals live on [[concepts/completion-contract#what-we-d-steal]]; these are the **implementation/feature-level** lessons specific to this artifact:

- ★ **A four-sided leash on long-running autonomy**: budget accounting + conservative event-driven continuation + evidence-gated completion + user-held lifecycle, all at once. If we build any "keep going" loop, copy all four, not one.
- ★ **Anti-spin rule**: if a continuation turn makes no tool call, suppress the next automatic continuation. A tiny, concrete guard against runaway loops ([[sources/openai--using-goals-in-codex#event-driven-continuation]]).
- ★ **`<verb> <object>` lifecycle on one command surface** (`/goal`, `/goal pause|resume|clear`) — a clean pattern for exposing stateful, pausable agent work through one slash command rather than many.
- **Continue only at safe/idle boundaries** (turn finished, nothing pending, no queued input) — don't interrupt in-flight work to "make progress."
- **"Budget reached" → summarize progress + blockers + next step**, never a fake completion. A drop-in rule for token/time-bounded runs.
- **Bounded tool authority**: let the model *start* and *complete-with-evidence*, but keep pause/resume/clear/budget with the user/system. A sensible default split of agent vs. human control.
- **Two-step self-authoring**: "Help me turn this into a strong `/goal`…" — let the agent draft its own contract, then tighten it. Reduces the friction of writing a good objective ([[sources/openai--using-goals-in-codex#self-authoring-goal]]).
- **A worked weak→strong example pair** as documentation (`/goal Improve performance` → the full p95 contract) — a teaching pattern worth copying when we document our own operations ([[sources/openai--using-goals-in-codex#weak-vs-strong-perf]]).

## Open questions / what's unclear

- **Implementation is described, not shown.** Thread-scoped state, the dispatcher, and budget accounting are the authors' account; we have no source or trace. How is "budget" measured (tokens? turns? time?), and how often do Goals complete vs. block vs. exhaust budget?
- **How does this compare to Claude Code's equivalents?** Plan mode, hooks, and long-running loops cover overlapping ground. A side-by-side (Codex Goals vs. Claude Code persistent-objective mechanisms) would be a strong QUERY once we've ingested a Claude Code analogue.
- **Is the verification surface gameable?** Evidence-gated completion is only as good as the surface chosen; the source warns but doesn't measure.
- **The rest of Codex.** This is one feature of a broader tool — capabilities, model, sandboxing, and approval model are all unstudied. The **distribution layer is now studied** ([[artifacts/plugins/openai-codex-plugins-marketplace]]); the *runtime* (harness loop, sandbox, approval) still isn't. Queue a full Codex CLI ingest.
