---
domain: creators
type: individual
name: Matt Pocock
handle: mattpocock
url: https://github.com/mattpocock
country: UK
last-reviewed: 2026-06-19
---

# Matt Pocock

> **One-line:** TypeScript educator (Total TypeScript / AI Hero) who open-sourced his daily-driver agent skills "straight from my .claude directory" — and, at 135K★, became the wiki's highest-signal *individual* skill pack and the clearest articulation of a **small-composable-skills, fundamentals-over-frameworks** house style.

*Page shape: compiled truth on top, append-only `## Timeline` at the bottom. Done when it passes the [page checklist](_definition-of-done.md).*

## Attributes

- **What they ship**: a single open-source skills repo — [[artifacts/plugins/mattpocock-skills]] (~17 published `SKILL.md` files) — distributed via the `skills.sh` installer (`npx skills@latest add mattpocock/skills`). Two skills get their own wiki pages: [[artifacts/skills/grilling]] and [[artifacts/skills/writing-great-skills]].
- **Distribution channel**: personal GitHub (`mattpocock/skills`, MIT) + the skills.sh marketplace + an `aihero.dev` newsletter (~60,000 devs) that announces changes ([[sources/mattpocock--skills#README-philosophy]], [[sources/mattpocock--skills#github-stars]]).
- **Position in ecosystem**: established **independent educator**, not a lab or a founder-operator. Author of Total TypeScript and AI Hero; the skills are a side-output of his own coding, which is the credibility backdrop for the repo's velocity (created 2026-02-03, 135K★ by 2026-06-19).
- **Notable quotes / framings**:
  - *"Skills … designed to be small, easy to adapt, and composable. They work with any model. … real engineering - not vibe coding."* ([[sources/mattpocock--skills#README-philosophy]])
  - On frameworks: *"Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve."* ([[sources/mattpocock--skills#README-philosophy]])
  - On skills as engineering: *"A skill exists to wrangle determinism out of a stochastic system. **Predictability** … is the root virtue."* ([[sources/mattpocock--skills#skill-writing-great-skills]])

## Artifacts produced

### Skills
- [[artifacts/skills/grilling]] — the relentless one-question-at-a-time alignment interview (his self-described most-popular skill family).
- [[artifacts/skills/writing-great-skills]] — the reference skill for *authoring* skills; the richest skill-craft vocabulary in the wiki.

### Plugins
- [[artifacts/plugins/mattpocock-skills]] — the whole pack (the home page for the other ~15 skills: `grill-with-docs`, `domain-modeling`, `codebase-design`, `tdd`, `diagnosing-bugs`, `to-prd`, `to-issues`, `triage`, `improve-codebase-architecture`, `ask-matt`, `handoff`, `teach`, `prototype`, `setup-matt-pocock-skills`, …).

### MCP servers
- *(none)*

## Design philosophy (if discernible)

A coherent, unusually legible house style — and the **near-perfect inverse of [[creators/prodmgmt-world]]**:

- **Fundamentals over frameworks.** Each of the four "why" sections pins an agent failure mode to a classic software-engineering book — misalignment → *The Pragmatic Programmer*, verbosity → Evans's *DDD* (ubiquitous language), broken code → small-deliberate-steps + TDD, ball-of-mud → Beck's "invest in design every day" + Ousterhout's deep modules ([[sources/mattpocock--skills#README-why]]). The bet is that decades-old fundamentals matter *more* with agents, not less.
- **Small, composable, unopinionated about process.** Skills are deliberately tiny (`grilling` is 3 sentences; `grill-with-docs` is one line that composes two other skills) and are meant to be hacked on. He refuses to "own the process" the way GSD/BMAD/Spec-Kit do ([[sources/mattpocock--skills#README-philosophy]], [[sources/mattpocock--skills#skill-grill-with-docs]]).
- **Model-agnostic by construction.** "They work with any model"; distribution is via skills.sh, which installs the same `SKILL.md` files into whichever coding agents you pick — the run-natively form of [[patterns/composition/single-source-multi-surface-distribution]].
- **Enforcement-light, predictability-first.** Where pm-os enforces with pre-flight gates and Context Guards, Pocock relies on *predictability* engineered into each skill (leading words, sharp completion criteria, aggressive pruning) rather than a fat behavioral harness ([[sources/mattpocock--skills#skill-writing-great-skills]]). There is no root mega-preamble (contrast gstack's 962-line `SKILL.md`).
- **Dogfoods his own discipline.** The repo runs a `CONTEXT.md` glossary, a `docs/adr/`, and an `.out-of-scope/` registry of explicitly-rejected scope — the same `domain-modeling` / decision-recording habits his skills teach ([[sources/mattpocock--skills#CONTEXT.md]], [[sources/mattpocock--skills#out-of-scope]]).
- **Bets against the test-bundle.** Notably ships **no test suite** — the deliberate counter-bet to Garry Tan's "a skill pack has tests" ([[patterns/quality-bar/skill-pack-bundle]]). The wager is that smallness + composability + fundamentals beats a heavy tested bundle for an individual's daily driver.

## Timeline (append-only)

- 2026-02-03 — `mattpocock/skills` repository created ([[sources/mattpocock--skills#github-stars]]).
- 2026-06-18 — snapshot HEAD `6eeb81b`, package `version: 1.0.1` ([[sources/mattpocock--skills#root]]).
- 2026-06-19 — ingested into this wiki at **135,831 ★ / 11,770 forks** — surpassing gstack's ~105K as the highest star count in the corpus to date ([[sources/mattpocock--skills#github-stars]]).

## Source citations

- [[sources/mattpocock--skills#README-philosophy]] — the anti-framework, small-composable-model-agnostic stance + newsletter reach
- [[sources/mattpocock--skills#README-why]] — the four failure modes + their classic-book grounding
- [[sources/mattpocock--skills#skill-writing-great-skills]] — predictability-as-root-virtue
- [[sources/mattpocock--skills#github-stars]] — stars/forks/created date
