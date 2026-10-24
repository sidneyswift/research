---
domain: artifacts
type: skill
name: writing-great-skills
creator: "[[creators/matt-pocock]]"
source: "[[sources/mattpocock--skills]]"
ecosystem: both
discovered-via: other
status: active
last-reviewed: 2026-06-19
popularity-signals:
  - signal: github-stars
    value: "ships in mattpocock/skills (135,831★ as-of 2026-06-19)"
    as-of: 2026-06-19
    source: "[[sources/mattpocock--skills#github-stars]]"
---

# writing-great-skills

> **One-line:** A reference skill for *authoring* skills — the vocabulary and levers (predictability, the two loads, the information-hierarchy ladder, leading words, the five failure modes) that make a skill behave the same way every run.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]). Done when it passes the [page checklist](_definition-of-done.md). This is the most directly self-applicable artifact in the wiki — see REFLECT in [[meta/self-improvements]].*

## Attributes

- **What it does**: hands the agent (and the human) a shared, precise vocabulary for writing and editing skills, plus the decision rules for each lever. It's pure **reference** — "this skill is all reference" — consulted on demand, not a step sequence.
- **Trigger conditions** (verbatim `description:`): *"Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable."* It is **user-invoked** (`disable-model-invocation: true`) — the description is human-facing.
- **Bundled resources**: a sibling **`GLOSSARY.md`** holding the full definitions of every **bold term**; the body points at it (its own worked example of progressive disclosure).
- **SKILL.md size**: ~83 lines / ~1.3k tokens of dense reference.
- **Progressive disclosure depth**: 2 levels (SKILL.md → `GLOSSARY.md`).
- **External dependencies**: none.
- **License**: MIT.

## Relationships

- **Creator**: [[creators/matt-pocock]]
- **Source**: [[sources/mattpocock--skills#skill-writing-great-skills]]
- **Defines**: [[concepts/skill-invocation-axis]] (the user-vs-model split + the two-load trade-off live here and in `docs/invocation.md`).
- **Part of**: [[artifacts/plugins/mattpocock-skills]]; reachable from `ask-matt`'s Standalone list.
- **Compare-with**: Anthropic's / FSI's / gbrain's `skill-creator` meta-skills (queued in [[artifacts/skills/_index]]) — this is the *principles* counterpart to those *scaffolders*.

## What problem it solves

Skill packs decay: skills drift, bloat, and start behaving differently run-to-run. `writing-great-skills` gives a name to each force that causes that and a lever to counter it — so "make this skill better" becomes a checkable activity instead of taste. Its thesis: *"A skill exists to wrangle determinism out of a stochastic system. **Predictability** — the agent taking the same process every run, not producing the same output — is the root virtue; every lever below serves it."* ([[sources/mattpocock--skills#skill-writing-great-skills]])

## How it works (mechanism)

The reference is organized as a flat peer-set of levers, each serving predictability ([[sources/mattpocock--skills#skill-writing-great-skills]]):

- **Invocation = two loads.** A **model-invoked** skill keeps a `description` (the model or another skill can fire it) but pays **context load** every turn; a **user-invoked** skill (`disable-model-invocation: true`) pays zero context load but spends **cognitive load** — *you* become the index that must remember it. Pick model-invocation only when the agent or another skill must reach it. Piled-up cognitive load is cured by a **router skill**. (Formalized as [[concepts/skill-invocation-axis]].)
- **Writing the description**: front-load the leading word; **one trigger per branch** (synonyms renaming one branch are duplication); cut identity already in the body.
- **Information hierarchy** (the ladder, ranked by how immediately the agent needs material): **in-skill step** → **in-skill reference** → **external reference**. Each step ends on a **completion criterion** that must be *checkable* and, where it matters, *exhaustive* ("every modified model accounted for") — a vague one invites **premature completion**. **Progressive disclosure** is the move down the ladder; **co-location** decides what sits beside a piece once there.
- **When to split** (each cut spends a load): **by invocation** (a distinct leading word must trigger it, or another skill must reach it) or **by sequence** (hide post-completion steps that tempt the agent to rush the current one).
- **Pruning**: single source of truth; check each line for **relevance**; hunt **no-ops** sentence-by-sentence and delete the whole sentence, aggressively.
- **Leading words**: a compact pretrained concept (*lesson*, *fog of war*, *tracer bullets*, *tight*, *red*) that anchors a region of behavior in the fewest tokens — and serves predictability twice: in the body it anchors *execution*, in the description it anchors *invocation*.
- **Five failure modes** (the diagnostic kit): **premature completion**, **duplication**, **sediment** (stale layers that accrete because adding feels safe), **sprawl** (too long even when every line is live — cured by the ladder), **no-op** (a line the model already obeys; the test is "does it change behavior vs default?").

## Patterns demonstrated

- [[concepts/skill-invocation-axis]] — this skill is the canonical source for the concept.
- [[patterns/structural/thin-harness-fat-skills]] — it's the *craft manual* for the fat-skills layer: how to keep a fat markdown skill legible (ladder), cheap (pruning, no-ops), and reliable (leading words, completion criteria).
- [[patterns/behavioral/evidence-gated-completion]] / [[concepts/completion-contract]] — "**completion criterion** must be checkable and exhaustive, or you get **premature completion**" is the skill-authoring twin of "done is decided by evidence, not confidence." Same idea, different altitude.
- [[patterns/quality-bar/complexity-ratchet]] — **sediment** and the no-op pruning discipline are the per-skill version of forward-only quality: without a pruning ritual, skills only accrete.
- [[patterns/composition/resolver-routing-table]] — names the **router skill** as the cure for multiplied cognitive load (the `ask-matt` move).

## Source citations

- predictability as root virtue; the two loads; ladder; leading words; five failure modes — all: [[sources/mattpocock--skills#skill-writing-great-skills]]
- the invocation rule restated (user-invoked can't be reached by model or other skills): [[sources/mattpocock--skills#docs-invocation]]

## What makes it great

It converts skill-authoring *taste* into a **vocabulary you can apply** — every fuzzy intuition ("this skill is bloated") gets a named cause (sediment vs sprawl vs duplication vs no-op) and a specific fix. And it dogfoods itself: it's all-reference (so it models the "flat reference peer-set is fine" claim), it discloses its definitions to `GLOSSARY.md` (modeling progressive disclosure), and it's terse (modeling no-op pruning). The lazy alternative — "tips for writing good skills" — would be exactly the no-op prose it tells you to delete.

## What we'd steal

**Exhaustive ledger — ★ = highest-value, and unusually, most of these apply to *this wiki itself*.**

- ★ **The two-load model (context load vs cognitive load)** as the explicit criterion for model- vs user-invocation — a real design lever, not a footnote ([[concepts/skill-invocation-axis]]).
- ★ **The information-hierarchy ladder** (in-skill step → in-skill reference → external reference) as the rule for *what goes in `CLAUDE.md` vs `_schemas/` vs a linked file* — directly maps onto this wiki's thin-harness/fat-schema split.
- ★ **Completion criterion: checkable + exhaustive, or premature completion.** Our `_schemas/_definition-of-done.md` and per-operation steps should phrase completion this way ("every entity the source touches cross-linked," not "cross-link some").
- ★ **Leading words.** Anchor behavior in a pretrained token instead of a paragraph; hunt restatements that collapse into one word. Applies to our schemas and operation prose.
- ★ **No-op pruning, sentence by sentence** ("does it change behavior vs the default? if not, delete the whole sentence") — a concrete LINT move for our own harness bloat ([[patterns/structural/thin-harness-fat-skills]] §harness-bloat).
- **The five failure modes as a diagnostic vocabulary** — sediment / sprawl / duplication / no-op / premature completion — usable verbatim when auditing any skill (or `CLAUDE.md`).
- **"One trigger per branch"** description discipline — collapse synonym-restatements; keep only genuinely distinct branches.
- **Split by sequence to defeat premature completion** — hide post-completion steps so the agent does the legwork on the current one.
- **Co-location** — keep a concept's definition, rules, and caveats under one heading so reading one part brings its neighbours.

## Open questions / what's unclear

- **How does this scale past ~20 skills?** The vocabulary is per-skill; it says less about *pack-level* health (cross-skill duplication, resolver rot) than gbrain's `check-resolvable` machinery does — they may be complementary halves.
- **Is "predictability, not reproducibility" testable** without a test suite? The pack ships none — so the discipline is asserted, not enforced (ties to the [[patterns/quality-bar/skill-pack-bundle]] counter-example).
- Worth a side-by-side with `superpowers`' `writing-skills` and Anthropic's `skill-creator` to see whether this vocabulary is converging across authors.
