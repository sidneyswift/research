---
domain: artifacts
type: skill
name: loop-library
creator: [[creators/forward-future]]
source: [[sources/forward-future--loop-library]]
ecosystem: both
discovered-via: other
status: active
last-reviewed: 2026-06-20
popularity-signals:
  - signal: github-stars
    value: 92 ★ / 14 forks (repo one week old)
    as-of: 2026-06-20
    source: [[sources/forward-future--loop-library#github-stars]]
---

# loop-library

> **One-line:** an installable skill that helps an agent **find** a published loop, **adapt** the nearest one, or **design** a new one through a short plain-language interview — where a *loop* is a bounded prompt that pairs a task with a real verification check and a named stopping condition. Bundles a curated catalog of **31 loops** from across the builder community.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): read everything about the skill, then write distilled judgment — not a transcription of its README. Done when it passes the [page checklist](_definition-of-done.md).*

## Attributes

- **What it does**: routes a request to the smallest useful path — recommend ≤3 published loops, adapt a published loop's thresholds/tools/cadence without weakening its feedback cycle, or interview the user and emit a new bounded loop as a <80-word copy-ready prompt. Treats "a loop" as "a feedback system with terminal states, not… permission for endless autonomy" ([[sources/forward-future--loop-library#SKILL.md]]).
- **Trigger conditions** (verbatim `description:`): *"Find, compare, adapt, and design repeatable AI-agent loops with explicit triggers, actions, verification, stopping conditions, guardrails, and handoffs. Use when a user asks for a loop, recurring agent workflow, automation cadence, iterative improvement process, an existing Loop Library recommendation, or help turning an outcome into a bounded copy-ready loop through a short question-led design session."* ([[sources/forward-future--loop-library#skill-description]])
- **Bundled resources**: `references/catalog.md` (a dated, offline fallback copy of all 31 loops) + `agents/openai.yaml` (a Codex interface extension). The *live* `catalog.md`/`catalog.json` on the site is treated as source-of-truth over the bundled copy ([[sources/forward-future--loop-library#skill-find]]).
- **SKILL.md size**: ~166 lines / ~1.7k tokens — a behavioral spec, almost no boilerplate.
- **Progressive disclosure depth**: 2 levels — `SKILL.md` → (live catalog URL *or* bundled `references/catalog.md`). The catalog itself is generated from `scripts/loop-data.mjs`.
- **External dependencies**: none required; *optional* web access to read the live catalog. The skill explicitly does **not** start schedules, change production, or send messages — those keep normal approvals ([[sources/forward-future--loop-library#README-skill]]).
- **License**: MIT.

## Relationships

- **Creator**: [[creators/forward-future]] (Matthew Berman's brand; curated community submissions)
- **Source**: [[sources/forward-future--loop-library#root]]
- **Embodies / instantiates the concept**: [[concepts/agentic-loop]] — this skill is the runnable front end; the 31 loops are its instances.
- **Composes with**: [[artifacts/skills/grilling]] — the design interview *is* a grilling/align-before-execute session in plain language; [[artifacts/projects/codex-goals]] — loop #028 wraps Codex Goals (`$goal-planner-codex`) directly.
- **Same installer as**: [[artifacts/plugins/mattpocock-skills]] (skills.sh / `npx skills add`).

## What problem it solves

A one-shot prompt ("make this faster," "keep improving this") gives a fluent agent too much room to guess and no honest finish line. The Loop Library turns recurring agent work into reusable loops that "compare results instead of relying on confidence, keep improvements instead of merely making changes, and stop when [they] succeed or stop making progress" ([[sources/forward-future--loop-library#README-why-bounded]]). The skill lowers the authoring cost: a non-expert describes an outcome in plain words and gets back a bounded, copy-ready loop without having to know the vocabulary.

## How it works (mechanism)

1. **Route to the smallest path** — Find / Adapt / Design / Find-then-design; "Do not ask for information the user already supplied" ([[sources/forward-future--loop-library#skill-route]]).
2. **Find = search the live catalog**, ranked by outcome fit, available inputs/tools, verification fit, acceptable authority, and stopping condition; recommend ≤3 with exact title + link + the smallest adaptation; "Never invent a Loop Library title, number, contributor, or URL" ([[sources/forward-future--loop-library#skill-find]]).
3. **Stay grounded** — use only user-supplied facts or files in scope; "Do not invent a technology stack, tool, metric, test method… Never present a guess as a 'sensible default.'" ([[sources/forward-future--loop-library#skill-grounding]])
4. **Design via interview** — one short question at a time, jargon hidden: *get done? → when does it run? → what's in/out of scope? → how will you know it worked? → when should it stop or ask for help?* Infer the smallest repeatable action and the handoff rather than asking ([[sources/forward-future--loop-library#skill-interview]]).
5. **Build the feedback cycle** — every loop is **Observe → Choose → Act → Verify → Record → Repeat-or-stop**, with the load-bearing rules: make the success gate observable ("Replace 'until happy' with a rubric, threshold, benchmark, reviewer decision, or finite scenario set"); name terminal states (success / clean no-op / blocked / approval-required / exhausted / stagnated) and **never report an error or exhausted budget as success**; prefer a **no-progress stop** over an invented time/iteration/cost limit; **re-read current state** before consequential actions; preserve unrelated work and gate destructive/production/external actions behind approval; **separate the working signal from a fresh acceptance gate** when an artifact could overfit its own metric; use **independent verification** when the same actor shouldn't both create and approve; and recommend a one-shot workflow when no new feedback can change the next action ([[sources/forward-future--loop-library#skill-feedback-cycle]], [[sources/forward-future--loop-library#skill-terminal-states]]).
6. **Deliver compressed** — return only a one-sentence description + a `> Prompt:` paragraph under ~80 words; keep the six-step internal design private unless asked ([[sources/forward-future--loop-library#skill-deliver]]).

## The 31 loops (the catalog)

The canonical dataset is `scripts/loop-data.mjs` ([[sources/forward-future--loop-library#loop-data]]); every published surface (site, `catalog.json`, `catalog.md`, the bundled skill fallback, structured data, sitemap, feed) is generated from it behind a drift check ([[sources/forward-future--loop-library#AGENTS.md-canonical]]). All 31 share the same shape — a `prompt`, an observable `verify` gate, a `useWhen` trigger, 4 `steps`, a `why`, and a safety `note`. Mapped to the wiki patterns each one demonstrates:

| # | Loop | By | Category | Verify / stop condition | Wiki pattern(s) |
| --- | --- | --- | --- | --- | --- |
| 001 | The docs sweep | M. Berman | Eng | Docs match implementation; finish with a reviewable PR | evidence-gated-completion · complexity-ratchet |
| 002 | The architecture satisfaction loop | P. Steinberger | Eng | Architecture satisfactory + checks pass; live-test/autoreview/commit each step | evidence-gated-completion · latent-vs-deterministic-split |
| 003 | The sub-50 ms page-load loop | M. Berman | Eng | Every page <50 ms on the same benchmark, no regressions | evidence-gated-completion |
| 004 | The production error sweep | M. Berman | Eng | Actionable errors fixed + verified (PR), or **clean no-op** if logs clean | evidence-gated-completion |
| 005 | The 100% test coverage loop | M. Berman | Eng | Full suite passes at 100% per the coverage report | evidence-gated-completion *(⚠ gameable proxy — note warns "coverage ≠ good assertions")* |
| 006 | The SEO/GEO visibility loop | M. Berman | Content | Repeatable crawl + query benchmark finds no high-impact gap | evidence-gated-completion · rank-by-expected-impact |
| 007 | The logging coverage loop | M. Berman | Eng | Every important path emits useful, **tested** logs | evidence-gated-completion |
| 008 | The nightly changelog loop | M. Berman | Eng | Every user-relevant change accounted for, or no-change recorded | scheduled-cadence + clean-no-op terminal state |
| 009 | The quality streak loop | M. Berman | Eval | `[N]` realistic cases pass **in a row**; each failure → regression coverage | complexity-ratchet · evidence-gated-completion |
| 010 | The full product evaluation loop | M. Berman | Eval | Every scenario meets the bar on a final complete rerun | evidence-gated-completion |
| 011 | The test-suite speed loop | M. Berman | Eng | Faster suite, no coverage/behavior regression vs fixed baseline | evidence-gated-completion |
| 012 | The repository cleanup loop | M. Berman | Eng/Ops | Re-run inventory shows every item current/owned/safely removed | evidence-gated-completion · preserve-unrelated-work |
| 013 | The stale-safe batch release loop | M. Berman | Ops | Released revision = latest integrated main containing the full batch | evidence-gated-completion |
| 014 | The production data cleanup loop | M. Berman | Ops | Post-cleanup audit + classifier regression tests pass | evidence-gated-completion · complexity-ratchet (classifier) |
| 015 | The post-release baseline loop | M. Berman | Ops | Baseline tied to a verified release revision + recorded conditions | reproducible-baseline |
| 016 | The ticket-to-PR-ready loop | Hiten Shah | Eng | Reproduces before fix, not after; regression checks pass | evidence-gated-completion · skill-as-method-call |
| 017 | The customer AI deployment loop | AgentLed.ai | Ops | One priority reaches a proven terminal state (rollout/fixed/escalated) | evidence-gated-completion · approval-gates |
| 018 | The product update podcast loop | Pierson Marks | Content | Episode accurate to sources, or confirmed no-episode; ask before publishing | clean-no-op · approval-gate (MCP: Jellypod) |
| 019 | The Clodex adversarial-review loop | L. Kucinski | Eng | Codex approves or only accepted findings remain; **errored/exhausted ≠ approved** | generator–verifier separation · evidence-gated-completion |
| 020 | The Loop Harness verification loop | Istasha | Eng | Only output a **second** Claude session verifies ships | generator–verifier separation · worktree isolation |
| 021 | The Boeing 747 benchmark | @victormustar | Design | Nine fixed camera angles clear the rubric; keep best; named stop | latent-vs-deterministic-split · keep-best + critic |
| 022 | War Loops: frontend reconstruction | Swayam | Design | Static/motion/responsive fidelity gates all pass | latent-vs-deterministic-split · surgical-critic |
| 023 | The self-improving champion loop | Jose C. Munoz | Eval | Challenger promoted only on a fresh-**holdout** win, no must-pass regression | overfit-resistant self-improvement · evidence-gated-completion |
| 024 | The devil's-advocate loop | Anonymous | Eval | No high-impact objection open; persistent `redteam.md` log; evidence to close | generator–verifier separation · persistent-objection-log |
| 025 | The fresh-clone loop | 0xUmbra | Eng/Ops | One uninterrupted clean clone reaches ready state from README only | evidence-gated-completion · discard-state-between-attempts |
| 026 | The Infinite Clickbait thumbnail loop | @Alex_FF | Design | One accurate thumbnail clears a fixed rubric at real sizes | latent-vs-deterministic-split · keep-best · reject-misleading |
| 027 | The autonomy-loop builder-reviewer loop | @inferencegod | Eng | New test fails-without/passes-with the fix (revert-or-mutate proof) | generator–verifier separation · proof-of-test |
| 028 | The Codex completion-contract loop | 3goblack | Eng | Every requirement **proved** before closure; budget exhaustion ≠ success | **evidence-gated-completion (direct)** · completion-contract |
| 029 | The Revolve versioned-experiment loop | Agent Zero | Eval | Win within one frozen evaluation revision; checkpoint + rollback | overfit-resistant self-improvement · checkpointed-experiments |
| 030 | The five-minute repository maintainer loop | P. Steinberger | Eng/Ops | Every item landed (with proof) / decision-ready / blocked / no-op | heartbeat-orchestration · separated-permissions · evidence-gated-completion |
| 031 | The recent-feedback sweep | M. Berman | Eng | Issue inventory closed + a fresh pattern audit comes back clean | complexity-ratchet · evidence-gated-completion |

**Reading the catalog:** the dominant spine is [[patterns/behavioral/evidence-gated-completion]] — almost every loop names an observable gate and forbids confidence-only or budget-exhaustion "done." Three sub-families recur: **generator–verifier separation** (#019, #020, #024, #027 — one actor builds, a different one approves), **overfit-resistant self-improvement** (#023, #029 — judge final acceptance on fresh/held-out cases, not the working set), and **latent→deterministic conversion** (#021, #022, #026 — turn "looks good" into a fixed rubric over fixed views).

## Patterns demonstrated

- [[patterns/behavioral/evidence-gated-completion]] — **the core pattern, and this is its confirming 2nd artifact.** The SKILL.md states both halves: a positive gate ("Make the success gate observable and reproducible. Replace 'until happy' with a rubric, threshold, benchmark…") and a negative gate ("Never report an error or exhausted budget as success") ([[sources/forward-future--loop-library#skill-feedback-cycle]], [[sources/forward-future--loop-library#skill-terminal-states]]). Loop #028 wraps Codex Goals' requirement→evidence audit directly ([[sources/forward-future--loop-library#loop-028-completion-contract]]); ~25 of 31 loops carry an observable `verify` gate.
- [[patterns/behavioral/latent-vs-deterministic-split]] — the loop *is* the discipline of moving the stop decision off latent judgment onto an observable surface; "Replace 'until happy' with a rubric, threshold, benchmark, reviewer decision, or finite scenario set." The Boeing-747 (#021) and clickbait (#026) loops convert a visual "looks good" into a fixed rubric over fixed views ([[sources/forward-future--loop-library#loop-021-boeing]]).
- [[patterns/behavioral/skill-as-method-call]] — published loops are **parameterized templates**: `[N]`, `[budget]`, `[margin]`, `[quality threshold]`, `[lookback window]`, `[repositories]` are the call slots, and the Adapt path is "same template, new arguments" ([[sources/forward-future--loop-library#loop-009-quality-streak]], [[sources/forward-future--loop-library#loop-023-champion]]).
- [[patterns/composition/resolver-routing-table]] — "Route the request" maps an intent (find / adapt / design / find-then-design) to a path, "smallest useful path" first ([[sources/forward-future--loop-library#skill-route]]).
- [[patterns/composition/single-source-multi-surface-distribution]] — one canonical `loop-data.mjs` fans out to site pages, `catalog.json`, `catalog.md`, the bundled skill fallback, structured data, sitemap, and feed, and the build's drift check rejects any change that lets a surface diverge ([[sources/forward-future--loop-library#AGENTS.md-canonical]]) — the same "never maintain a fact in two places" rule this wiki applies to itself.
- [[patterns/behavioral/persona-lens-review-panel]] — **sibling / proposed extension.** Loops #019/#020/#024/#027 separate a *builder* from an independent *verifier/critic* (Codex reviews Claude; a 2nd Claude session verifies; a critic argues a design is wrong; a reviewer proves the test). This is the two-role *generator–verifier* cousin of the parallel-persona panel — a proposed pattern with four in-source instances (needs a 2nd wiki artifact to confirm as its own page).

## Source citations

- Trigger / description — [[sources/forward-future--loop-library#skill-description]]
- Router (find/adapt/design) — [[sources/forward-future--loop-library#skill-route]], [[sources/forward-future--loop-library#skill-find]]
- Grounding rules — [[sources/forward-future--loop-library#skill-grounding]]
- Design interview — [[sources/forward-future--loop-library#skill-interview]]
- Six-step cycle + design rules + terminal states — [[sources/forward-future--loop-library#skill-feedback-cycle]], [[sources/forward-future--loop-library#skill-terminal-states]]
- Compressed delivery format — [[sources/forward-future--loop-library#skill-deliver]]
- "Loops are not permission to run forever" — [[sources/forward-future--loop-library#README-why-bounded]]
- Non-action guarantee — [[sources/forward-future--loop-library#README-skill]]
- Canonical data + drift check — [[sources/forward-future--loop-library#AGENTS.md-canonical]], [[sources/forward-future--loop-library#loop-data]]

## What makes it great

The skill refuses the two failure modes that ruin most "automation prompt" packs. First, it **hides its own vocabulary** from beginners and infers the hard parts (the repeatable action, the handoff) from plain answers — so a non-expert gets a correctly-bounded loop without learning the theory ([[sources/forward-future--loop-library#skill-interview]]). Second, it is *aggressively* anti-hallucination at two layers: it won't invent a catalog entry (Find is gated on the live catalog) and it won't invent the user's stack/metrics/limits ("Never present a guess as a 'sensible default'") — the lazy alternative, a plausible-sounding loop full of fabricated specifics, is exactly what it forbids ([[sources/forward-future--loop-library#skill-find]], [[sources/forward-future--loop-library#skill-grounding]]). And the whole catalog is opinionated in one direction — every loop must name *how it verifies* and *when it stops*, enforced mechanically by the drift check.

## What we'd steal

**Exhaustive ledger** (★ = highest-value, clearly portable):

- ★ **"Replace 'until happy' with a rubric, threshold, benchmark, reviewer decision, or finite scenario set."** A one-line test for whether a loop's stop condition is real — directly usable as a LINT check on any agent instruction we write (incl. our own operations).
- ★ **Named terminal-state vocabulary** (success / clean no-op / blocked / approval-required / exhausted / stagnated) + the rule "never report an error or exhausted budget as success." A reusable checklist for any autonomous task spec; the wiki's own `_definition-of-done.md` "If blocked" section is the same idea — adopt the full six-state taxonomy.
- ★ **No-progress stop over an invented limit.** "Use a user-supplied limit when one exists. Otherwise use a no-progress stop instead of inventing a time, iteration, cost, retry, or scope limit." Avoids fake precision.
- ★ **Separate the working signal from a fresh acceptance gate** (champion/challenger holdout; Revolve frozen revisions) — the cleanest stated defense against Goodharting an eval. Portable to our `analyses/_eval-rubric.md`.
- ★ **Generator–verifier separation** — "Use independent verification when the same actor should not both create and approve high-impact output." Loops #019/#020/#024/#027 are four concrete implementations (Codex-reviews-Claude, second-session-verifies, critic/builder + `redteam.md`, revert-or-mutate proof-of-test).
- **The six-step Observe→Choose→Act→Verify→Record→Repeat-or-stop skeleton** as a loop template.
- **"Re-read current state before consequential actions. Do not ship stale code, partial artifacts, or assumptions carried from an earlier cycle."** — the freshness rule (mirrors the wiki's "verify before recommending").
- **Recommend a one-shot when no new feedback can change the next action** — don't manufacture a loop where iteration is pointless.
- **The <80-word compressed-prompt delivery format** + "keep its internal design private unless the user asks" (progressive disclosure of the *answer*, not just the docs).
- **Parameterized prompt slots** (`[N]`, `[budget]`, `[margin]`) as the Adapt interface — loops as method calls.
- **`useWhen` / `verify` / `note` as required fields on every catalog entry** — and a drift check that rejects a loop missing any of them (a mechanical quality bar on prose).
- **Proof-of-test by revert-or-mutate** (#027) — prove a new test actually catches its fix, not just that it executes lines. A sharper bar than coverage (#005's note admits coverage is a weak proxy).
- **"Discard the environment and start again, carrying nothing"** (#025) — destructive reset between attempts so local state can't hide the next problem.
- **Persistent objection log at `.agent-reviews/redteam.md`, kept out of commits** (#024) — durable adversarial state that prevents circular debate.
- **Curated submission behind review** + a canonical data file as the single source — the catalog model itself.

## Open questions / what's unclear

- **Is "generator–verifier separation" its own pattern?** Four in-source instances strongly suggest yes, but the wiki needs a 2nd *artifact*. Candidates already here: [[artifacts/plugins/compound-engineering]]'s `/ce-code-review` and [[artifacts/plugins/pm-os]]'s reviewer panel both separate build from review — a focused pass could confirm a `generator-verifier-separation` page (distinct from the *parallel-persona* panel).
- **How real is the verification?** The catalog *prescribes* observable gates, but the loops are prompts, not harnesses — whether a given agent actually honors "exhausted ≠ done" is unverified. Loop #005 (100% coverage) even encodes a gate its own `note` admits is gameable.
- **Adoption vs. age.** 92★ at one week is a weak signal; the stronger signal is the named-builder submissions (Steinberger, Shah, Marks, Kucinski). Re-check stars in 30 days.
- **Overlap with the `agentic-loop` concept page.** Keep this page about the *runnable skill + catalog*; keep the idea (loop vs one-shot, terminal states) on [[concepts/agentic-loop]] to avoid duplication.
