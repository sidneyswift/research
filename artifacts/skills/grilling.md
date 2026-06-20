---
domain: artifacts
type: skill
name: grilling
creator: "[[creators/matt-pocock]]"
source: "[[sources/mattpocock--skills]]"
ecosystem: both
discovered-via: other
status: active
last-reviewed: 2026-06-19
popularity-signals:
  - signal: quoted-by
    value: author calls grill-me/grilling "my most popular skills"
    as-of: 2026-06-19
    source: "[[sources/mattpocock--skills#README-why]]"
---

# grilling

> **One-line:** Interview the user relentlessly — one question at a time, each with a recommended answer — walking the design tree until you and the agent share an understanding *before* any code is written.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): read everything about the skill, then write distilled judgment. Done when it passes the [page checklist](_definition-of-done.md). The wiki's **first individual skill page**.*

## Attributes

- **What it does**: turns the agent into a relentless interviewer. It walks each branch of the design tree, resolving inter-decision dependencies one at a time, asking a *single* question per turn (with its own recommended answer) and waiting for the reply before moving on — until plan and agent are aligned.
- **Trigger conditions** (verbatim `description:`): *"Interview the user relentlessly about a plan or design. Use when the user wants to stress-test a plan before building, or uses any 'grill' trigger phrases."*
- **Bundled resources**: none. The entire skill is **5 sentences of body** — no `scripts/`, `references/`, or sub-skills.
- **SKILL.md size**: ~11 lines incl. frontmatter (~3 sentences of instruction). One of the smallest skills in the wiki.
- **Progressive disclosure depth**: 1 level — everything is inline; there is nothing to disclose.
- **External dependencies**: none.
- **License**: MIT.

## Relationships

- **Creator**: [[creators/matt-pocock]]
- **Source**: [[sources/mattpocock--skills#skill-grilling]]
- **Composes with**: it is the **reusable loop** behind two user-invoked orchestrators — `grill-me` (stateless; no codebase, saves nothing) and `grill-with-docs` (stateful; adds [[concepts/ubiquitous-language-for-agents|domain-modeling]], writing `CONTEXT.md` + ADRs inline). `grill-with-docs` is literally *"Run a `/grilling` session, using the `/domain-modeling` skill"* ([[sources/mattpocock--skills#skill-grill-with-docs]]).
- **Part of**: [[artifacts/plugins/mattpocock-skills]]; sits at the head of its idea→ship "main flow" ([[sources/mattpocock--skills#skill-ask-matt]]).

## What problem it solves

The #1 agent failure mode the pack names: **misalignment** — *"No-one knows exactly what they want"* (Pragmatic Programmer). You think the agent understood you; it builds the wrong thing. `grilling` closes that communication gap *up front* by forcing the decisions into the open before code exists, when they're cheapest to change ([[sources/mattpocock--skills#README-why]]).

## How it works (mechanism)

Three moves, all in the body ([[sources/mattpocock--skills#skill-grilling]]):

1. **Relentless, tree-structured interrogation.** "Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one." Decisions are ordered by dependency, not asked at random.
2. **One question at a time, with a recommendation.** "Ask the questions one at a time, waiting for feedback … Asking multiple questions at once is bewildering." And: "For each question, provide your recommended answer" — so the user can confirm cheaply instead of composing from scratch.
3. **Prefer evidence over interrogation.** "If a question can be answered by exploring the codebase, explore the codebase instead." The interview is for what only the human knows, not for facts the agent can fetch.

The whole skill leans on the **leading word** *relentless* (and the *grill* trigger) to anchor a region of behavior in a few tokens — the technique its sibling [[artifacts/skills/writing-great-skills]] preaches.

## Patterns demonstrated

- **align-before-execute** *(proposed, tracked)* — a structured interview that forces shared understanding *before* building. This page is the strongest in-wiki articulation; candidate 2nd examples are CE's brainstorm/plan stage, `superpowers`' `brainstorming` skill, and **[[artifacts/skills/loop-library]]'s design interview** — "Ask one short question at a time in everyday language… infer the smallest repeatable action… instead of asking" ([[sources/forward-future--loop-library#skill-interview]]), the same one-question-at-a-time/infer-don't-interrogate shape on a different creator's pack. Promote to a `patterns/` page when one of those is deep-dived. (Tracked on [[artifacts/plugins/mattpocock-skills]] and root `index.md` proposed list.)
- [[concepts/skill-invocation-axis]] — a model-invoked **reusable-discipline** skill that two user-invoked orchestrators reach via prose `/skill` invocation; the textbook "extract the loop, let callers wrap it" shape.
- [[patterns/behavioral/skill-as-method-call]] — one parameterized procedure called by `grill-me` (no-codebase arg) and `grill-with-docs` (codebase + docs arg).

## Source citations

- body (relentless / one-at-a-time / explore-instead): [[sources/mattpocock--skills#skill-grilling]]
- misalignment failure mode + "most popular skills": [[sources/mattpocock--skills#README-why]]
- the `grill-with-docs` composite + `grill-me` standalone: [[sources/mattpocock--skills#skill-grill-with-docs]], [[sources/mattpocock--skills#skill-ask-matt]]

## What makes it great

It does a lot with almost nothing. The behavioral payload — *relentless, depth-first, one-question-at-a-time, always recommend, fetch-don't-ask* — fits in three sentences because each phrase recruits a strong pretrained prior. The lazy alternative is a long checklist of "good interview" rules; instead it trusts a leading word and one sharp anti-instruction ("asking multiple questions at once is bewildering") to do the steering. It's the cleanest demonstration in the pack that **smallness is a feature**, and that an alignment interview is a *reusable primitive* other skills compose, not a one-off.

## What we'd steal

- ★ **One question at a time, each with a recommended answer.** Cuts user cognitive load and keeps the thread legible — directly portable to any of our interview-style skills (and to the wiki's own grilling-adjacent skills).
- ★ **"If a question can be answered by exploring the codebase, explore instead."** A one-line rule that stops an agent from interrogating the human for facts it can fetch — generally useful in any data-rich workspace (e.g. "check Attio/Granola before asking").
- ★ **Extract the loop, wrap it twice.** Keep the reusable interview model-invoked and let thin user-invoked orchestrators add context (stateless vs stateful, no-docs vs docs). A clean composition template.
- **Leading-word steering** (*relentless*) instead of a rules list — fewer tokens, sharper behavior.
- **Depth-first dependency ordering** ("resolve dependencies between decisions one-by-one") rather than a flat question dump.

## Open questions / what's unclear

- **When does "relentless" become annoying?** There's no stated stop condition besides "shared understanding"; the repo's `.out-of-scope/question-limits.md` suggests the author deliberately *rejected* a hard question cap — worth reading why ([[sources/mattpocock--skills#out-of-scope]]).
- **Does the recommended-answer habit bias the user** toward the agent's framing? A possible failure mode for high-stakes decisions.
- How does `grilling` interact with the "smart zone" budget — a long interview consumes the same window the build needs ([[sources/mattpocock--skills#skill-ask-matt]]).
