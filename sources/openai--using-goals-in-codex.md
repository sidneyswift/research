---
domain: sources
type: docs-page
url: https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
retrieved: 2026-06-02
snapshot-location: sources/openai--using-goals-in-codex/snapshot.md
upstream-commit: 9b4e6279edd4dceb6b4b7da582482a7c882f7544 # openai/openai-cookbook, examples/codex/using_goals_in_codex.ipynb
last-reviewed: 2026-06-02
---

# "Using Goals in Codex: Persistent Objectives for Long-Running Work" (OpenAI Cookbook, docs-page)

> An OpenAI Cookbook guide (authors **Raj Pathak** and **Stefano Fabbri**, published 2026-05-09) introducing **Goals** in the Codex CLI: persistent, *thread-scoped* objectives that keep an agent working toward a defined outcome across turns, with a built-in **completion condition** ("what should be true, how success should be checked, and what constraints must stay intact"). Our primary source for the [[concepts/completion-contract]] idea, the [[patterns/behavioral/evidence-gated-completion]] pattern, the first **non-Garry** documented parameter signature that promotes [[patterns/behavioral/skill-as-method-call]], and the first **OpenAI** artifact in the wiki ([[artifacts/projects/codex-goals]]).

## Snapshot details

- **Retrieved**: 2026-06-02 — captured from the canonical notebook source, not the JS-rendered docs page.
- **Where it lives in this wiki**: [`sources/openai--using-goals-in-codex/snapshot.md`](openai--using-goals-in-codex/snapshot.md) — verbatim prose, immutable. The page is published HTML at `developers.openai.com`, but the **source of truth is a Jupyter notebook** in the public `openai/openai-cookbook` repo (`examples/codex/using_goals_in_codex.ipynb`, all 44 cells markdown). We extracted the markdown cell sources verbatim; this is a faithful capture, not a model summary.
- **Upstream URL**: https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
- **Upstream identifier (version stamp)**: notebook committed at `9b4e6279edd4dceb6b4b7da582482a7c882f7544` (openai/openai-cookbook, "[codex] add goals in codex cookbook (#2684)", 2026-05-13) — *added in that PR and unchanged since, so the commit ≈ the published page*. **Publish date on the page: 2026-05-09.** Classed `docs-page` (a living page that can change upstream) but pinned to a commit, so claims are anchored even though the working page may advance.
- **Figures**: the notebook embeds **7 diagrams** (`p0.png`–`p6.png`) as base64 cell attachments (~8 MB total). Per the wiki's lean-snapshot ethos ("large and reconstructable → don't commit"), the binaries are **not** committed; their `![pN.png](attachment:…)` references + the author's "*Figure N.*" captions are preserved verbatim in the snapshot, and the originals are reconstructable from the pinned commit above. No textual evidence is lost — every figure is described by its caption in-line.

## Anchor map

Every claim citing this source uses a `#anchor` from this list. Anchors are thematic pointers into the article's own sections (the section headers make stable anchors). Line numbers are into `snapshot.md`. **Do not invent new anchors** — extend this list if a future citation needs one.

- `#root` — the guide as a whole.
- `#completion-condition` — the one-sentence definition: "A Goal gives Codex a completion condition: what should be true, how success should be checked, and what constraints must stay intact" (L3).
- `#scoped-not-autonomy` — the guardrail framing: "A Goal is not background autonomy without boundaries. It is a scoped, user-controlled completion contract. You define the outcome, Codex works against the evidence in the thread, and the Goal can be paused, resumed, cleared, completed, or stopped by budget" (L9).
- `#prompt-vs-goal-loop` — the load-bearing mental model: "Prompt: ask -> work -> result -> wait" vs "Goal: work -> check -> continue or complete" (L107-111).
- `#goals-vs-prompts` — the section (L90-111): a prompt "says: do this next thing"; a Goal "says: keep working until this outcome is true"; the durable target is "attached to the thread," so after a turn Codex "can inspect the current evidence and decide whether the objective is satisfied."
- `#six-elements` — the strongest Goals define six things: **Outcome / Verification surface / Constraints / Boundaries / Iteration policy / Blocked stop condition** (L117-123).
- `#goal-template` — the explicit, documented **parameter signature**: `/goal <desired end state> verified by <specific evidence> while preserving <constraints>. Use <allowed inputs, tools, or boundaries>. Between iterations, <how Codex should choose the next best action>. If blocked or no valid paths remain, <what Codex should report and what would unlock progress>.` (L125-129). The promotion gate for [[patterns/behavioral/skill-as-method-call]].
- `#weak-vs-strong-perf` — the worked weak→strong example: `/goal Improve performance` → the full p95-latency contract (L131-141, L204-216, L218-224). "Strong Goals name the end state, verification surface, and constraints."
- `#research-evidence-standard` — "Define the evidence standard before the work begins, especially when exact proof may not be available," + the research-Goal template (L143-149).
- `#self-authoring-goal` — "When the task is clear but the Goal is not, Codex can help write the Goal itself" — a two-step describe→tighten workflow (L151-159). (Meta-prompting: the agent drafts its own spec.)
- `#lifecycle-commands` — the command surface: `/goal` (view), `/goal pause`, `/goal resume`, `/goal clear`; available "starting in Codex **0.128.0**"; npm/brew install (L18, L39-76).
- `#stopping-conditions` — the stopping condition "may be success, pause, clear, interruption, budget limit, or a blocker that requires user input" (L76); and the "Keep going / Try the next likely fix / Run the benchmark again…" intent a Goal makes explicit (L78-88).
- `#three-changes` — what changes when a Goal is active: (1) the objective stays visible, (2) continuation becomes possible from an idle thread, (3) completion must be evidence-based (L161-170).
- `#evidence-based-completion` — **the key claim**: "A Goal should not be marked complete because the model believes it is probably done. It should be complete only after the objective is checked against the relevant files, tests, logs, benchmark output, generated artifacts, or other concrete evidence" + "the evidence decides whether it is done" (L168-170, L196). Definitional anchor for [[patterns/behavioral/evidence-gated-completion]].
- `#thread-scoped-state` — "Goals are implemented as persisted thread state, not as global memory and not as project-level instructions… the objective belongs to the thread where the relevant context lives" (L172-182).
- `#event-driven-continuation` — continuation is "event-driven rather than a simple loop… only at safe boundaries: after a turn has finished, when no other work is pending, when no user input is queued, and when the thread is idle"; the dispatcher is "deliberately conservative" — plan-only work doesn't trigger continuation, interruptions pause, and "if a continuation turn makes no tool call, the next automatic continuation is suppressed so Codex does not spin" (L186-188).
- `#budget-accounting` — "Budget handling is explicit. When the budget is reached, Codex should stop substantive work, summarize progress and blockers, and identify the next useful step. Reaching a budget limit is not the same as completing the objective" (L198).
- `#bounded-tool-authority` — "The model can start a Goal and can mark an existing Goal complete only when the evidence supports completion. Pausing, resuming, clearing, and budget-limited transitions remain controlled by the user or the system" (L200).
- `#completion-contract-architecture` — the architecture summary: "a Goal is a **thread-scoped completion contract**. It combines durable objective state, lifecycle controls, continuation policy, budget accounting, and evidence-based completion. The point is not to make Codex loop forever; it is to let the objective persist until the evidence says the work is done" (L202).
- `#narrow-enough-to-audit` — "A Goal should be narrow enough to audit but broad enough to let Codex choose the next action," with the fix-the-test (too narrow) / improve-the-system (too broad) / make-the-suite-pass-without-changing-public-API (just right) trichotomy (L226-228).
- `#deep-hedging-casestudy` — the research case study: reproducing Buehler, Gonon, Teichmann & Wood's *Deep Hedging*; the Goal "was not to 'reproduce the paper' in the abstract" but to attempt headline numbers and "separate exact mechanics from approximate trained replacements" and be explicit about what "cannot be exactly replayed" (L250-309).
- `#blocked-claims` — what stayed blocked: "The paper does not provide the exact random seeds, generated training paths, TensorFlow graph, optimizer state, checkpoints, or full original simulation state… the strongest honest result is a partial and approximate reproduction, not an exact neural replay" (L288-290).
- `#epistemic-levels` — "preserve those different levels of support instead of flattening them into a single success claim" — confirmed / approximate / blocked / uncertain (L290-298).
- `#claim-ledger-format` — the literal ledger-entry format: **Claim / Route / Evidence surface / Status / Remaining uncertainty** (L301-307).
- `#dont-hide-uncertainty` — "Do not use a Goal to hide uncertainty. If the data may be unavailable, say so in the Goal… If proxy evidence is allowed, define how it should be labeled" (L321).
- `#when-not-to-use` — the section (L313-323): not for one-line edits, simple explanations, short reviews, or vague finish lines ("Make this better gives Codex no reliable completion condition").
- `#three-properties` — "Goals are strongest when the task has three properties: a durable objective, an evidence-based finish line, and a path that may require several turns of investigation" (L323).
- `#good-candidates` — the fit list: "performance optimization, flaky test investigation, dependency migrations, bug hunts that require reproduction, multi-step refactors, benchmark-driven tuning, and research tasks that require a final artifact" (L42).
- `#conclusion` — "They turn a thread from a sequence of isolated prompts into a stateful work loop around a defined outcome… For complex research, that is the difference between generating an answer and producing an audit. A good Goal does not merely ask Codex to finish. It tells Codex what finished means" (L325-332).

## Why we cite this

- **The crispest external statement of a "completion contract."** The article repeatedly frames a Goal as "a scoped, user-controlled completion contract" ([[#scoped-not-autonomy]]) and architecturally as "a thread-scoped completion contract" ([[#completion-contract-architecture]]). This is the grounding for the new [[concepts/completion-contract]] page — and the first articulation of the idea in the wiki from outside Garry Tan's corpus.
- **An explicit, documented parameter signature for a command-as-method.** [[#goal-template]] gives `/goal` a literal six-slot template (`<end state> verified by <evidence> while preserving <constraints>. Use <boundaries>. Between iterations <policy>. If blocked <stop condition>.`). This is exactly the artifact the [[patterns/behavioral/skill-as-method-call]] page named as its **promotion gate** ("a skill that ships an explicit, documented parameter signature… ideally from a non-Garry pack") — and it's from OpenAI, breaking the single-creator caveat.
- **"Evidence decides, not model confidence."** [[#evidence-based-completion]] states the rule directly: completion "only after the objective is checked against the relevant files, tests, logs, benchmark output, generated artifacts." This grounds the new [[patterns/behavioral/evidence-gated-completion]] pattern and corroborates [[patterns/behavioral/latent-vs-deterministic-split]] (the verification surface is the deterministic/assertable side) from a non-Garry source.
- **A budget ≠ completion boundary.** [[#budget-accounting]] — reaching a budget limit means "summarize progress and blockers," not "done." A clean, citable design distinction for any agent that runs long.
- **A conservative continuation dispatcher.** [[#event-driven-continuation]] — continuation only at safe boundaries; spin-suppression when a turn makes no tool call. Concrete machinery for "autonomy with a leash."
- **An anti-overclaiming research discipline.** [[#deep-hedging-casestudy]] + [[#epistemic-levels]] + [[#claim-ledger-format]] — separate confirmed / approximate / blocked / uncertain in the final artifact, with a literal ledger format. Directly relevant to how *this wiki* marks unverified claims (see [[meta/self-improvements]]).
- **A clean "when NOT to" boundary.** [[#when-not-to-use]] + [[#three-properties]] — Goals are for durable-objective + evidence-finish-line + multi-turn-path work; a one-off edit is still a plain prompt. Rare and valuable: a source that scopes its own technique.

## Popularity signals (if this source provides them)

Not a metrics-bearing source (no stars/likes). Its weight is **provenance + credibility**, captured at retrieval:

- **Publisher**: OpenAI, on its official developer site (`developers.openai.com/cookbook`) — first-party documentation for the Codex product, not third-party commentary.
- **Authors**: Raj Pathak, Stefano Fabbri (the latter the committing author of PR #2684).
- **Backed by a public repo**: `openai/openai-cookbook` (the widely-referenced OpenAI Cookbook), file `examples/codex/using_goals_in_codex.ipynb`, commit `9b4e627` (2026-05-13).
- **Product version stamp**: Goals ship "starting in Codex **0.128.0**" ([[#lifecycle-commands]]) — a dated capability marker for the Codex CLI.
- **As-of**: 2026-06-02.

## Related sources

- [[sources/garrytan--meta-meta-prompting]] — **strong conceptual echo.** The [[#self-authoring-goal]] "Codex can help write the Goal itself" workflow is meta-prompting (the agent drafts/tightens its own spec), the same move Garry's essay #6 describes; and the [[#prompt-vs-goal-loop]] "work → check → continue" loop is the autonomy that essay's "skills that build skills" assumes.
- [[sources/garrytan--complexity-ratchet]] — **same "evidence decides" thesis, different creator.** [[#evidence-based-completion]] ("the evidence decides whether it is done") is the per-task analogue of the ratchet's "everything harnessable is testable" ([[sources/garrytan--complexity-ratchet#everything-harnessable-testable]]); both insist a system's "done" be checked against an external assertable surface.
- [[sources/garrytan--thin-harness-fat-skills]] — the [[#goal-template]] parameter signature is the "skill as a method call" idea ([[sources/garrytan--thin-harness-fat-skills#skill-as-method-call]]) realized in a shipping non-Garry command.
- [[sources/garrytan--foxconn-factories]] — **tension to watch.** A Goal grants long-running autonomy under a contract; essay #8 warns against over-scaffolding a capable model. Reconciliation: the Goal's leash (budget, evidence gate, conservative dispatcher) is the *informed-autonomy* middle ground, not a "Foxconn factory." Noted for a future analysis.
- [[creators/openai]] — the publisher (this page seeds OpenAI's first creator entry).
