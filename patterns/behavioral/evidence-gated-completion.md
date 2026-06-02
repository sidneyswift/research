---
domain: patterns
type: pattern
name: evidence-gated-completion
category: behavioral
status: proposed
last-reviewed: 2026-06-02
example-count: 1
---

# evidence-gated-completion

> An agent may not declare a task **done** on self-assessment ("I think I'm finished"). Completion is *gated* on checking the objective against an external, assertable **verification surface** — a passing test, a benchmark threshold, a clean build, a generated artifact. Corollary: running out of budget/time is **not** completion; it's a blocked-and-summarize event.

## Longer definition

This is a discipline about *who decides the task is over*. The naive agent loop lets the model end on its own judgment of doneness — which is exactly the place a fluent model is most dangerous, because "plausibly complete" and "actually complete" are indistinguishable from the model's own vantage. Evidence-gated completion moves the stop decision off the model's confidence and onto an artifact the model (or a human) can *observe and assert on*. OpenAI's Codex Goals state the rule directly: "A Goal should not be marked complete because the model believes it is probably done. It should be complete only after the objective is checked against the relevant files, tests, logs, benchmark output, generated artifacts, or other concrete evidence" ([[sources/openai--using-goals-in-codex#evidence-based-completion]]). The pattern has two halves that travel together: a **positive gate** (define the verification surface *before* the work, so "done" is checkable) and a **negative gate** (a blocked/stop condition, and the rule that budget-exhaustion ≠ done — [[sources/openai--using-goals-in-codex#budget-accounting]]).

## Mechanism

1. **Name the verification surface up front.** Before the agent works, the objective is paired with the concrete evidence that proves it: a named test suite, a benchmark + threshold, a build command, a produced file. In Codex Goals this is the second of the six contract elements ("Verification surface") and shows up in the template as `… verified by <specific evidence> …` ([[sources/openai--using-goals-in-codex#six-elements]], [[sources/openai--using-goals-in-codex#goal-template]]).
2. **Check after each turn, against that surface — not against intuition.** The loop is "work → check → continue or complete" ([[sources/openai--using-goals-in-codex#prompt-vs-goal-loop]]). If the benchmark improves but misses the threshold, the agent keeps going; if it passes but a constraint regressed, it is *not* done ([[sources/openai--using-goals-in-codex#weak-vs-strong-perf]]).
3. **Distinguish "blocked" from "done."** If the evidence can't be produced (a tool won't run, source data is missing), the agent stops and reports "the attempted paths, the evidence gathered, the blocker, and the next input needed" — it does not paper over the gap ([[sources/openai--using-goals-in-codex#goal-template]], [[sources/openai--using-goals-in-codex#blocked-claims]]).
4. **Budget-exhaustion is its own exit, separate from completion.** "When the budget is reached, Codex should stop substantive work, summarize progress and blockers, and identify the next useful step. Reaching a budget limit is not the same as completing the objective" ([[sources/openai--using-goals-in-codex#budget-accounting]]).
5. **Preserve epistemic levels in the output.** When exact proof isn't available, the result separates confirmed / approximate / blocked / uncertain rather than flattening to a single success claim — with a literal ledger (Claim / Route / Evidence surface / Status / Remaining uncertainty) ([[sources/openai--using-goals-in-codex#claim-ledger-format]], [[sources/openai--using-goals-in-codex#epistemic-levels]]).

## When to use

- **Any long-running or autonomous loop** where the agent decides when to stop. The longer the leash, the more the stop decision must be externalized.
- **Anything a user will trust as fact** — a fix, a migration, a reproduction, a number. If "done" matters, gate it on evidence.
- **Tasks with a real finish line but an uncertain path** — performance work (benchmark), flaky tests (a reproduction + a green suite), refactors (tests + unchanged public API) ([[sources/openai--using-goals-in-codex#good-candidates]]).
- **Research/audit work**, where the *honest* output is a graded ledger, not a yes/no.

## When NOT to use

- **One-shot, low-stakes, or self-evident tasks.** A one-line edit, a definition, a short explanation — there's no multi-turn loop to gate, and inventing a "verification surface" is pure ceremony ([[sources/openai--using-goals-in-codex#when-not-to-use]]).
- **When no honest surface exists.** If you can't name evidence that would prove the outcome ("make this better"), don't fake one — the gate becomes a rubber stamp. Either find a real surface or admit the task is judgment-terminal (a human decides).
- **When the cheap surface is gameable and you can't fix it.** A gate on a proxy the agent can satisfy without achieving intent (overfit the benchmark, delete the failing test) is worse than no gate — it *launders* incompleteness as done. Only gate on surfaces you'd trust an adversary to optimize against.
- **Genuinely latent end-states.** Some outcomes ("is this essay persuasive?") have no assertable surface; forcing one mis-applies the pattern (the inverse of [[patterns/behavioral/latent-vs-deterministic-split]]'s wrong-side error).

## Why it works

A fluent model's failure mode on "am I done?" is *confident fabrication of completeness* — undetectable from the answer alone. An external verification surface has a *loud* failure mode (a red test, a missed threshold, a failed build), so routing the stop decision there converts a silent error into a catchable one. This is the same logic as [[patterns/behavioral/latent-vs-deterministic-split]] applied specifically to the *termination* step: the done-decision is exact and must-not-hallucinate, so it belongs on the deterministic/assertable side, never in latent space. It also defends against the structural pressure of autonomy: an agent rewarded for "finishing" will find the cheapest path to declaring victory unless the victory condition is externally defined and checked ([[sources/openai--using-goals-in-codex#evidence-based-completion]]). Separating budget-exhaustion from completion closes the most common laundering route — "I ran out of room, so I'll call it done."

## Detection recipe

- **Look for**: an explicit "verification surface" / "how success is checked" element in the task spec; language like "verified by <evidence>", "checked against tests/benchmark/build"; a *separate* blocked/stop path; an explicit rule that budget/time limits trigger a summary rather than a completion; graded output (confirmed/approximate/blocked) instead of binary done.
- **Confirm with**: the stop decision actually consults the surface — i.e., the agent *keeps going* when evidence falls short and *refuses to claim done* when it can't produce evidence. (The presence of tests isn't enough; the question is whether tests *gate the stop*.)
- **Rule out**: ordinary "the code has tests" (that's [[patterns/quality-bar/skill-pack-bundle]] / [[patterns/quality-bar/complexity-ratchet]] — about *coverage accruing*, not about *who ends the task*). The distinguishing question: *if the model felt confident but the evidence was absent, would the system still let it stop as "done"?* If no → evidence-gated completion. If the tests are just sitting there and the model self-declares → not this pattern.

## Examples in this wiki

- [[artifacts/projects/codex-goals]] — **the grounding example.** A Goal "should not be marked complete because the model believes it is probably done… only after the objective is checked against the relevant files, tests, logs, benchmark output, generated artifacts." Budget-exhaustion is explicitly *not* completion; a blocked path is a summarize-and-report event, not a fake done. The six-element contract names the verification surface and the blocked stop condition as first-class. — citation: [[sources/openai--using-goals-in-codex#evidence-based-completion]], [[sources/openai--using-goals-in-codex#budget-accounting]], [[sources/openai--using-goals-in-codex#goal-template]]

> **Why still `proposed` (1 example):** only one ingested artifact grounds this so far (Codex Goals, OpenAI). Two strong **promotion candidates already in the wiki** — verify their citations on a dedicated pass before listing them as confirmed examples:
> - [[patterns/quality-bar/complexity-ratchet]] / [[sources/garrytan--complexity-ratchet#everything-harnessable-testable]] — "the evidence decides whether it is done"; "if you can harness it… assert on it… you can ratchet it." This is evidence-gated *quality* across sessions; confirm whether it also frames a single task's *completion* as evidence-gated.
> - [[artifacts/plugins/gstack]] — the plan-review **finding-floor tests** fail if the agent declares a review done without firing the interactive question ([[sources/garrytan--complexity-ratchet#tty-interactive-review-test]]). That's a completion gated on an external assertion; confirm it reads as *this* pattern and not merely a behavioral contract test.
>
> A clean 2nd example promotes this to `confirmed` — ideally one already in-wiki (above), keeping the two-creator spread (OpenAI + Garry Tan) the wiki prizes.

## Counter-examples or anti-pattern

- **Self-declared completion (the inverse).** The default agent loop — model works, then ends on its own judgment of doneness — is exactly what this pattern forbids. Its failure mode is the silent overclaim: a plausible artifact accepted as a finished one. The Codex guide names the specific abuse: "Do not use a Goal to hide uncertainty" ([[sources/openai--using-goals-in-codex#dont-hide-uncertainty]]).
- **Budget-exhaustion masquerading as completion.** An agent that hits its limit and emits a confident "done" rather than "here's how far I got and what's blocking" has inverted the pattern. The explicit rule "budget limit ≠ completion" exists precisely to block this ([[sources/openai--using-goals-in-codex#budget-accounting]]).
- **Gate-on-a-gameable-proxy (the corruption).** Gating on a surface the agent can satisfy without the intent (overfit the one benchmark, weaken the assertion) launders incompleteness — worse than an honest "not done." The surface must be one you'd trust against an optimizer.

## Related patterns

- [[patterns/behavioral/latent-vs-deterministic-split]] — **specializes.** This is that split applied to the *termination* step: the done-decision is exact/assertable, so it must live on the deterministic side. The verification surface *is* the deterministic side.
- [[patterns/quality-bar/complexity-ratchet]] — **sibling / cousin.** The ratchet is evidence-gated *quality accumulating across sessions*; evidence-gated-completion is the *per-objective* version (does this one task get to stop?). Same "evidence decides," different timescale. A leading promotion candidate.
- [[patterns/behavioral/skill-as-method-call]] — **composes-with.** The completion contract that carries the verification surface is itself a parameterized invocation (the six-slot `/goal` template); evidence-gated-completion is *what the contract enforces*.
- [[patterns/quality-bar/skill-pack-bundle]] — **composes-with.** A bundle's tests are *candidate verification surfaces*; this pattern is the rule that those tests must *gate the stop*, not merely exist.

## Open questions

- **Is it confirmable now?** The two in-wiki candidates (complexity-ratchet, gstack floor tests) plausibly already demonstrate it; a focused re-read of those sources could promote this in one pass.
- **How do you pick a non-gameable surface?** The pattern's whole value collapses if the surface is gameable, yet the sources give no method for choosing one. Is there a heuristic beyond "would you trust an adversary to optimize against it"?
- **Who sets the gate — author or agent?** Codex lets the agent help *draft* the contract ([[sources/openai--using-goals-in-codex#self-authoring-goal]]); if the agent also proposes its own verification surface, is the gate still independent, or has it marked its own homework?
- **Does it generalize past code?** Tests/benchmarks/builds are crisp surfaces; the research case study ([[sources/openai--using-goals-in-codex#deep-hedging-casestudy]]) shows a *graded* surface (confirmed/approximate/blocked) for fuzzier work. How far down the fuzziness gradient does the pattern still hold?
