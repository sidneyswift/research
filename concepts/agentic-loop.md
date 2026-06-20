---
domain: concepts
type: concept
name: agentic-loop
creators: [[creators/forward-future]]
sources: [[sources/forward-future--loop-library]]
status: emerging
last-reviewed: 2026-06-20
popularity-signals:
  - signal: adoption
    value: 31 curated loops from ~14 named builders in one week; installable via skills.sh + Codex
    as-of: 2026-06-20
    source: [[sources/forward-future--loop-library#github-stars]]
---

# agentic-loop

> **One-line:** a **loop** is a bounded, self-correcting agent prompt — task + an observable verification check + a named stopping condition — that lets the agent *learn from the last result and take the next useful step*, as opposed to a one-shot prompt that asks the agent to do something once and trust its own confidence.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): compiled truth on top + an append-only `## Timeline`. Done when it passes the [page checklist](_definition-of-done.md).*

## What it is

Most prompts ask for one pass and accept whatever comes back. A loop adds the feedback that makes work repeatable: "Find the slowest page, make one focused improvement, and measure it again. Keep the change only if it helps. Repeat until every page meets the target or another pass stops producing a meaningful improvement" ([[sources/forward-future--loop-library#README-what-is-a-loop]]). Forward Future frames a good loop as answering four questions — *what is the agent trying to accomplish? how will it know the latest attempt worked? what should it do with what it learned? when should it finish or ask for help?* The skill expands this into a six-step cycle (**Observe → Choose → Act → Verify → Record → Repeat-or-stop**) governed by one non-negotiable: the stop decision must rest on an observable surface, never on the model's sense of being finished ([[sources/forward-future--loop-library#skill-feedback-cycle]]).

The crucial, under-appreciated half is the *boundary*: "Loops are not permission for an agent to run forever. The best ones are deliberately bounded. They include a real check, a clear stopping point, and a moment to hand control back to a person when judgment or approval is needed" ([[sources/forward-future--loop-library#README-why-bounded]]). A loop is therefore as much about *terminal states* (success / clean no-op / blocked / approval-required / exhausted / stagnated) as about iteration.

## Where it came from

The "agent loop" idea is old (control theory's feedback loop, Boyd's OODA, the RL agent-environment loop, the ReAct "reason+act" cycle). What [[creators/forward-future]] contributes (2026-06) is packaging it as a **prompt-design unit for everyday agent users**: a named, copy-ready artifact with a verification gate and a stop rule, collected into a browsable, submission-driven catalog ([[sources/forward-future--loop-library#README-what-is-a-loop]]). The vocabulary (trigger / success gate / terminal state / guardrail / persistent state) is deliberately hidden from beginners and inferred on their behalf ([[sources/forward-future--loop-library#skill-interview]]). The concept sits one layer above OpenAI's [[concepts/completion-contract]]: a completion contract specifies *one objective and its evidence*; a loop wraps that contract in a *repeating* observe-act-verify cycle with explicit continue-or-stop logic.

## Why it matters

It relocates the most dangerous decision — *am I done?* — from the model's confidence to an observable artifact. "An open-ended instruction like 'keep improving this' leaves too much room for guessing. A loop gives the work a clear finish line and a consistent way to judge progress… The agent can compare results instead of relying on confidence, keep improvements instead of merely making changes, and stop when it succeeds or stops making progress" ([[sources/forward-future--loop-library#README-why-bounded]]). For builders this is the difference between an agent you can leave running and one you have to babysit: a well-formed loop is *reusable* (another person/agent runs it without rebuilding the workflow) and *trustworthy* (its output is gated, not asserted).

## Evidence & claims

- *A loop = task + feedback + stop, vs a one-shot prompt* — demonstrated via the "make this faster" example. ([[sources/forward-future--loop-library#README-what-is-a-loop]])
- *Bounded by design; hands control back to a human for judgment/approval* — asserted as the definition of a "best" loop. ([[sources/forward-future--loop-library#README-why-bounded]])
- *The stop must be observable; "Replace 'until happy' with a rubric, threshold, benchmark, reviewer decision, or finite scenario set"* — prescribed rule. ([[sources/forward-future--loop-library#skill-feedback-cycle]])
- *Never report an error or exhausted budget as success* — prescribed terminal-state rule. ([[sources/forward-future--loop-library#skill-terminal-states]])
- *Recommend a one-shot when no new feedback can change the next action* — i.e. don't manufacture a loop where iteration is pointless. ([[sources/forward-future--loop-library#skill-feedback-cycle]])
- *Demonstrated across 31 instances* spanning engineering, evaluation, operations, content, and design. ([[sources/forward-future--loop-library#loop-data]])

## Patterns demonstrated

- [[patterns/behavioral/evidence-gated-completion]] — a loop's verify step + "exhausted ≠ success" *is* evidence-gated completion, applied per-iteration; the Loop Library is the pattern's confirming 2nd artifact.
- [[patterns/behavioral/latent-vs-deterministic-split]] — the loop forces the termination decision onto the deterministic/observable side; converting "until happy" to a rubric is this split made into a design rule.
- [[patterns/behavioral/skill-as-method-call]] — published loops are parameterized templates (`[N]`, `[budget]`, `[margin]`) invoked with arguments via the Adapt path.
- *Candidate pattern — generator–verifier separation:* several loops require a different actor to verify than to build ([[sources/forward-future--loop-library#loop-019-clodex]], [[sources/forward-future--loop-library#loop-027-autonomy]]); tracked on [[artifacts/skills/loop-library]] pending a 2nd wiki artifact.

## Tensions & counter-arguments

- **Prescription ≠ behavior.** A loop is still a *prompt*; nothing forces a given agent to honor "exhausted ≠ done." Without a real harness the gate can be theater — and one catalog loop (100% coverage) gates on a proxy its own note admits is gameable ([[sources/forward-future--loop-library#loop-005-test-coverage]]). The concept's value depends on the gate being non-gameable, which the concept itself can't guarantee.
- **Loops can launder runaway autonomy.** The framing repeatedly warns that a loop is "not permission to run forever," which is itself evidence that the natural failure mode is exactly that — an agent that keeps "improving" against a soft gate. Garry Tan's stance ([[concepts/compound-engineering]] / [[patterns/quality-bar/complexity-ratchet]]) would add: the loop only compounds value if each pass *also* ratchets the harness (tests/evals), not just the artifact.
- **When not to loop.** The skill itself concedes the anti-case: if no new feedback can change the next action, a one-shot is correct and a loop is ceremony.

## Timeline (append-only)

- 2026-06-12 — Forward Future publishes the Loop Library (repo created) ([[sources/forward-future--loop-library#github-stars]]).
- 2026-06-19 — 31 loops cataloged across 5 categories from ~14 named builders ([[sources/forward-future--loop-library#loop-data]]).
- 2026-06-20 — paged here; positioned as the repeating-cycle layer above [[concepts/completion-contract]] and the conceptual home of [[patterns/behavioral/evidence-gated-completion]]'s 2nd artifact.

## Related

- [[concepts/completion-contract]] — **builds-on.** A completion contract specifies one objective + its verification surface + a blocked stop; a loop wraps that in a repeating observe-act-verify-continue cycle.
- [[patterns/behavioral/evidence-gated-completion]] — **specializes-into.** The loop's verify+stop rule is this pattern.
- [[artifacts/skills/loop-library]] — the runnable skill that finds/adapts/designs loops.
- [[artifacts/projects/codex-goals]] — a productized single-objective completion contract; loop #028 wraps it.
- [[artifacts/skills/grilling]] — the loop *design interview* is a grilling/align-before-execute session.

## What we'd steal

**Exhaustive ledger** (★ = highest-value):

- ★ **The four-question test for a well-formed loop** (accomplish / how it knows it worked / what to do with the result / when to finish-or-ask) — a fast checklist for auditing any recurring agent instruction, including our own operations in `CLAUDE.md`.
- ★ **"Loops are not permission to run forever"** as a first-class design value — bound every autonomous instruction with a real check + a stop + a human-handoff moment.
- ★ **The six terminal states** (success / clean no-op / blocked / approval-required / exhausted / stagnated) as the vocabulary for "how this ends."
- **Hide the jargon, infer the structure** — let users describe outcomes in plain words; the system supplies the loop scaffolding.
- **One-shot-vs-loop as an explicit fork** — decide whether feedback can even change the next action before wrapping work in a loop.
- **Catalog the loop, don't re-derive it** — a reusable loop is run by others without rebuilding the workflow (the same compounding logic as skillify).

## Open questions

- Is "loop" meaningfully distinct from "completion contract," or is it the contract + a `while(progress)`? (Working answer: the repetition + the no-progress/stagnation terminal states are the delta.)
- Does the concept survive contact with non-gameable surfaces? How many of the 31 gates would hold against an agent optimizing to pass them?
- Where's the line between a loop and a full harness? At what point should a frequently-run loop be promoted into deterministic tooling (the latent→deterministic migration)?
