---
domain: concepts
type: concept
name: completion-contract
creators:
  - "[[creators/openai]]"
sources:
  - "[[sources/openai--using-goals-in-codex]]"
status: emerging
last-reviewed: 2026-06-02
popularity-signals:
  - signal: adoption
    value: "Shipped as the `/goal` command surface in Codex CLI ≥ 0.128.0 (first-party OpenAI feature)"
    as-of: 2026-06-02
    source: "[[sources/openai--using-goals-in-codex#lifecycle-commands]]"
---

# completion-contract

> **One-line:** Specify an agent's objective as a persistent, evidence-verified *contract* — an outcome, how success is checked, and what must stay intact — so the agent runs a "work → check → continue or complete" loop instead of "prompt → work → wait," and "done" is decided by **evidence, not model confidence**.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): the idea as it reads across the source, written as distilled judgment — not a summary of the cookbook.*

## What it is

A completion contract is a way of *stating an objective* to an agent such that the agent can autonomously decide whether it is finished. OpenAI's Codex ships it as **Goals**: "a Goal gives Codex a completion condition: what should be true, how success should be checked, and what constraints must stay intact" ([[sources/openai--using-goals-in-codex#completion-condition]]). The contract is **persistent** (it survives across turns, attached to the thread, not re-stated each message), **scoped** (it names boundaries, a budget, and a stop condition), and **evidence-gated** (completion is checked against concrete artifacts — tests, benchmarks, logs, a built page — not asserted because the model "believes it is probably done" — [[sources/openai--using-goals-in-codex#evidence-based-completion]]). The shift it produces is from the prompt loop "ask → work → result → wait" to the goal loop "work → check → continue or complete" ([[sources/openai--using-goals-in-codex#prompt-vs-goal-loop]]). It is *not* unbounded background autonomy: "a Goal is not background autonomy without boundaries. It is a scoped, user-controlled completion contract" ([[sources/openai--using-goals-in-codex#scoped-not-autonomy]]).

## Where it came from

The crisp term **"completion contract"** and the productized form (`/goal`) are OpenAI's, in the Codex Cookbook guide "Using Goals in Codex" by Raj Pathak and Stefano Fabbri (published 2026-05-09; notebook commit `9b4e627`, 2026-05-13 — [[sources/openai--using-goals-in-codex#root]]). The underlying idea — goal-directed agents that persist an objective and verify completion — long predates this page (it is the basic shape of any agent control loop); the source's contribution is to (a) name it cleanly, (b) give it an auditable **six-element structure**, and (c) draw the boundary against "autonomy without a leash." Within this wiki it rhymes with Garry Tan's independently-arrived-at "the evidence decides whether it is done" ([[sources/garrytan--complexity-ratchet#everything-harnessable-testable]]) — two creators converging on evidence-gated completion.

## Why it matters

It changes *where the finish line lives*. In a plain prompt, "done" is implicit and the user re-supplies the target after every intermediate result ("keep going," "run the benchmark again" — [[sources/openai--using-goals-in-codex#stopping-conditions]]). A completion contract moves the finish line into durable, inspectable state, which (1) lets the agent take multi-turn paths where "the next step depends on what it learns along the way" without losing the target, (2) makes the agent's *self-assessment of doneness* auditable — it must point at evidence — and (3) bounds the autonomy with a budget and an explicit blocked stop condition so "persist until done" never becomes "loop forever." For anyone building agents, the practical upshot: **you specify the contract once; the agent runs the loop; the evidence — not the agent's confidence — closes it.** The same discipline is why a research agent can "produce an audit" rather than "generate an answer" ([[sources/openai--using-goals-in-codex#conclusion]]).

## The six elements (the auditable structure)

The source's reusable contribution — a strong contract names six things ([[sources/openai--using-goals-in-codex#six-elements]]):

1. **Outcome** — what is true when the work is done.
2. **Verification surface** — the test / benchmark / report / artifact / command output that *proves* it.
3. **Constraints** — what must not regress while the agent works.
4. **Boundaries** — which files, tools, data, or resources the agent may touch.
5. **Iteration policy** — how the agent decides what to try next after each attempt.
6. **Blocked stop condition** — when to stop and report that no defensible path remains (and what would unlock it).

These slot into a literal template — `/goal <end state> verified by <evidence> while preserving <constraints>. Use <boundaries>. Between iterations <policy>. If blocked <stop condition>.` ([[sources/openai--using-goals-in-codex#goal-template]]) — i.e. the contract *is* a documented parameter signature (see Patterns demonstrated).

## Evidence & claims

- *A Goal is a completion condition + constraints* — demonstrated (shipped feature): [[sources/openai--using-goals-in-codex#completion-condition]]
- *Completion must be evidence-based, not model-belief* — asserted as the design center: "the evidence decides whether it is done" ([[sources/openai--using-goals-in-codex#evidence-based-completion]])
- *State is thread-scoped, not global memory / project instructions* — asserted (architecture choice): [[sources/openai--using-goals-in-codex#thread-scoped-state]]
- *Continuation is event-driven and conservative* (only at idle/safe boundaries; spin-suppressed if a turn makes no tool call) — asserted: [[sources/openai--using-goals-in-codex#event-driven-continuation]]
- *Reaching a budget limit ≠ completion* — asserted: [[sources/openai--using-goals-in-codex#budget-accounting]]
- *Lifecycle authority is bounded* — the model may start a Goal and mark complete *only when evidence supports it*; pause/resume/clear/budget stay with the user/system — asserted: [[sources/openai--using-goals-in-codex#bounded-tool-authority]]
- *Works for research by preserving epistemic levels* (confirmed / approximate / blocked / uncertain) — demonstrated via the Deep Hedging reproduction case study: [[sources/openai--using-goals-in-codex#deep-hedging-casestudy]], [[sources/openai--using-goals-in-codex#claim-ledger-format]]

> **Asserted vs. demonstrated:** the *user-facing behavior* (the `/goal` surface, the research case study) is demonstrated; the *internal architecture* (thread-scoped state, the conservative dispatcher, budget accounting) is **asserted by the authors** — we have the design described, not the source code. Treat architecture claims as OpenAI's own account.

## Patterns demonstrated

- [[patterns/behavioral/evidence-gated-completion]] — **the core technique this concept rides on.** Completion is gated on an external, assertable verification surface; budget-exhaustion ≠ done. Citation: [[sources/openai--using-goals-in-codex#evidence-based-completion]], [[sources/openai--using-goals-in-codex#budget-accounting]].
- [[patterns/behavioral/skill-as-method-call]] — the six-element contract is a **documented parameter signature**: `/goal <end state> verified by <evidence>…` is one command re-aimed by its arguments. This source is the example that **promoted** that pattern to confirmed. Citation: [[sources/openai--using-goals-in-codex#goal-template]].
- [[patterns/behavioral/latent-vs-deterministic-split]] — the contract splits the loop: the **verification surface** (tests/benchmark/build) is the deterministic/assertable side; **iteration policy** ("choose the next best action") is the latent side. Putting the *done-decision* on the assertable side is the whole point. Citation: [[sources/openai--using-goals-in-codex#evidence-based-completion]].

## Tensions & counter-arguments

- **Autonomy vs. leash.** A completion contract authorizes an agent to keep working unattended, which sits against the wiki's "don't build runaway autonomy" instincts (cf. [[sources/garrytan--foxconn-factories]] on over-scaffolding capable models). The source's answer is the leash itself — budget accounting, a conservative event-driven dispatcher, spin-suppression, and bounded lifecycle authority ([[sources/openai--using-goals-in-codex#event-driven-continuation]], [[sources/openai--using-goals-in-codex#bounded-tool-authority]]) — i.e. *informed* autonomy, not background autonomy. Whether that leash holds in practice is unverified (we have the design, not a trace).
- **Over-specification.** A contract can be drawn so narrowly it stops being useful: "Fix the failing checkout test" may be *too narrow* if the real bug is upstream; "Improve the whole system" is too broad to audit. The source's own rule — "narrow enough to audit but broad enough to let Codex choose the next action" ([[sources/openai--using-goals-in-codex#narrow-enough-to-audit]]) — concedes the technique has a Goldilocks zone, not a free lunch.
- **Gaming the verification surface.** Evidence-gated completion is only as honest as the surface: an agent optimizing to "make the benchmark pass" can satisfy the letter while missing the intent (the classic proxy-metric failure). The source partially pre-empts this ("do not use a Goal to hide uncertainty"; label proxy evidence — [[sources/openai--using-goals-in-codex#dont-hide-uncertainty]]), but choosing a non-gameable surface is left to the author.
- **Not for everything.** The source scopes itself out of one-line edits, simple explanations, and vague-finish-line tasks ([[sources/openai--using-goals-in-codex#when-not-to-use]]) — a contract is overhead that only pays off on durable-objective, evidence-finish-line, multi-turn work.

## Related

- [[artifacts/projects/codex-goals]] — the runnable artifact that embodies this concept (`/goal` in the Codex CLI).
- [[patterns/behavioral/evidence-gated-completion]] — the pattern this concept is built on.
- [[patterns/behavioral/skill-as-method-call]] — the contract-as-parameter-signature view.
- [[sources/garrytan--complexity-ratchet]] — the system-level cousin: "the evidence decides" applied across sessions (the ratchet) rather than within one objective (the contract).

## What we'd steal

**Exhaustive ledger** (★ = highest-value, clearly portable):

- ★ **The six-element contract as a spec template** — Outcome / Verification surface / Constraints / Boundaries / Iteration policy / Blocked stop condition. A ready-made checklist for specifying *any* long-running agent task (including our own [[meta/self-improvements|wiki operations]]). Front-load it.
- ★ **"Evidence decides, not confidence."** Never let an agent mark itself done on self-assessment; require it to point at an external artifact (test pass, built page, resolved link). This is the single most portable rule on the page.
- ★ **Blocked stop condition as a first-class element.** Make "what to do when you *can't* finish honestly" part of the spec up front — "stop with the attempted paths, the evidence gathered, the blocker, and the next input needed" ([[sources/openai--using-goals-in-codex#goal-template]]). Prevents both silent failure and overclaiming.
- ★ **Budget limit ≠ completion.** When you run out of budget, *summarize progress + blockers*, don't emit a fake "done." A clean rule for any token/time-bounded agent ([[sources/openai--using-goals-in-codex#budget-accounting]]).
- **The "work → check → continue or complete" loop** as the mental model for any persistent objective (vs. "ask → work → wait").
- **Self-authoring the contract**: ask the agent to *draft* the goal from a plain-language description, then tighten the success condition / verification surface / stop condition before activating ([[sources/openai--using-goals-in-codex#self-authoring-goal]]). Lowers the cost of writing a good contract.
- **Thread-scoped (not global) objective state** — keep the objective where the relevant context lives, so it can be audited against the actual files/commands/diffs of that thread ([[sources/openai--using-goals-in-codex#thread-scoped-state]]).
- **Conservative continuation** — only continue at safe/idle boundaries; suppress the next auto-continuation if a turn made no tool call (anti-spin). A concrete safety rule for autonomous loops ([[sources/openai--using-goals-in-codex#event-driven-continuation]]).
- **Preserve epistemic levels in the output** — confirmed / approximate / blocked / uncertain, with a literal ledger format (Claim / Route / Evidence surface / Status / Remaining uncertainty). Directly applicable to how this wiki marks unverified claims ([[sources/openai--using-goals-in-codex#claim-ledger-format]], [[sources/openai--using-goals-in-codex#epistemic-levels]]).
- **"Narrow enough to audit, broad enough to choose the next action"** — the Goldilocks heuristic for scoping any agent task.
- **Scope the technique out loud** — the page tells you when *not* to use a Goal. Steal the habit of putting a "when NOT to use" boundary on every capability ([[sources/openai--using-goals-in-codex#when-not-to-use]]).

## Open questions

- **Does the leash actually hold?** We have OpenAI's *description* of budget accounting + the conservative dispatcher, not a trace or the source. Does the spin-suppression rule prevent runaway in practice, and how often do Goals hit budget vs. complete vs. block?
- **How gameable is the verification surface in the wild?** The proxy-metric risk is real; is there evidence of Goals "passing the benchmark" while missing intent?
- **Is "completion contract" the field's term or OpenAI's?** Anthropic/Cursor/others have agent-objective features; do any name this the same way, or is it convergent-but-unnamed (the same question the wiki tracks for [[patterns/behavioral/latent-vs-deterministic-split]])? A second creator naming it would graduate this concept toward a pattern.
- **Where's the line between a completion contract and a [[patterns/quality-bar/complexity-ratchet|ratchet]]?** Both are evidence-gated; one is per-objective (within a thread), the other per-session (across history). Are they the same idea at two timescales?
