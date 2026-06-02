---
domain: concepts
type: concept
name: compound-engineering
creators: "[[creators/every]]"  # Kieran Klaassen (originator) + Dan Shipper (amplifier)
sources: "[[sources/every--compound-engineering]], [[sources/every--compound-engineering-gets-an-upgrade]], [[sources/every--compound-engineering-plugin]]"
status: active
last-reviewed: 2026-06-02
popularity-signals:
  - signal: quoted-by
    value: "Every's named methodology, productized as an official multi-platform plugin (@every-env/compound-plugin v3.9.4) and documented in a living guide + dated essays"
    as-of: 2026-06-02
    source: "[[sources/every--compound-engineering-plugin#README]]"
---

# compound-engineering

> **One-line:** structure agent-assisted development so that **each unit of work makes the
> next one easier** — front-load planning, let AI do the middle, and spend real effort
> "compounding" reusable knowledge (tests, docs, learnings, checks) so the system gets
> smarter every cycle instead of accruing debt.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): read across
the guide, the essay, and the runnable plugin, then write distilled judgment — not a summary
of any single source.*

## What it is

Compound engineering is an **AI-native development methodology** built on one inversion:
traditional development accumulates complexity (every feature adds debt; the next change gets
slower), whereas compound engineering treats every unit of work as something that *teaches the
system*, so the next unit is cheaper ([[sources/every--compound-engineering#thesis]]). In
practice that means an explicit loop — **ideate → brainstorm → plan → work → review → polish →
compound → repeat** — where roughly **80% of effort is planning + review and 20% is execution**
([[sources/every--compound-engineering#loop]]), and a budgeting rule (**the 50/50 rule**) that
splits engineering time evenly between shipping features and improving the system that ships
them ([[sources/every--compound-engineering#50-50]]). The load-bearing step is **compound**:
after a problem is solved, the lesson is written down (into `CLAUDE.md`/`AGENTS.md` or a
documented-solutions store) so no future agent re-learns it. As models improve, the "work"
middle shrinks and human judgment migrates to the *ends* — *"AI is the stuff in the middle;
humans are the bread on either end"* ([[sources/every--compound-engineering-gets-an-upgrade#sandwich]]).
It is an **idea/methodology**, not a runnable thing — the runnable embodiment is
[[artifacts/plugins/compound-engineering]].

## Where it came from

Coined and popularized by **Every** (every.to). The methodology is **Kieran Klaassen's** (GM of
Cora at Every); the origin essay is *"My AI Had Already Fixed the Code Before I Saw It"* (Every's
*Source Code* column — the plugin's `homepage`), and **Dan Shipper** (CEO) amplified it as "how
Every codes with agents" in *Chain of Thought* ([[sources/every--compound-engineering-plugin#README]],
[[creators/every]]). The term is Every's coinage (~early 2026); the **4-step → 8-step evolution**
is recorded in Kieran's 2026-05-29 essay ([[sources/every--compound-engineering-gets-an-upgrade#original-loop]],
`#eight-loop`). It is not the *only* articulation of the underlying principle — see Tensions.

## Why it matters

It reframes the engineer's job. If each unit of work should make the next easier, then the
valuable skills are **judgment and system-design**, not typing — and several traditional beliefs
must be "unlearned" ("the code must be written by hand," "every line must be manually reviewed,"
"first attempts should be good"; [[sources/every--compound-engineering#unlearn]]). The concrete
consequence is a **budget shift**: the 50/50 rule deliberately spends half of engineering time on
institutional knowledge rather than shipping, which is the inverse of the traditional ~90/10
split. And it makes a falsifiable bet about capability progress: as the agent gets better, the
human bottleneck moves *outward* to deciding what to build and judging whether it feels right —
not away ([[sources/every--compound-engineering-gets-an-upgrade#work-is-boring]]). For this wiki
specifically, it matters because it is the **named, productized, independently-arrived-at twin**
of [[patterns/quality-bar/complexity-ratchet]] — strong evidence that "forward-only quality from
agent-maintained systems" is a real field-level idea, not one builder's habit.

## Evidence & claims

- *"Each unit of engineering work should make subsequent units easier — not harder."* — the
  thesis; **asserted** as principle ([[sources/every--compound-engineering#thesis]]), but
  **demonstrated** in the plugin's own development trail: 27 `docs/brainstorms/` → 57 `docs/plans/`
  → 30 `docs/solutions/` ([[sources/every--compound-engineering-plugin#docs-solutions]]).
- **80/20 planning-vs-execution; 50/50 features-vs-systems** — **asserted** budgeting rules
  ([[sources/every--compound-engineering#thesis]], `#50-50`); no measured study offered.
- *"The work phase has become boring — in the best way."* — Kieran's **experiential** claim that a
  good plan + right context makes execution reliable
  ([[sources/every--compound-engineering-gets-an-upgrade#work-is-boring]]); first-person, not
  benchmarked.
- *"Taste belongs in systems, not in review. Bake your judgment into configuration, schemas, and
  automated checks."* — **asserted** principle ([[sources/every--compound-engineering#taste-in-systems]]),
  **demonstrated** by the plugin's behavioral contract tests + `/ce-compound`'s Discoverability
  Check ([[sources/every--compound-engineering-plugin#tests]], `#ce-compound`).
- **"95% garbage on first attempts, 50% on second."** — **asserted** statistic with no source
  ([[sources/every--compound-engineering#garbage-rate]]); treat as illustrative.
- *"The pattern applies to knowledge work much more broadly."* — **asserted** generalization
  hypothesis ([[sources/every--compound-engineering-gets-an-upgrade#knowledge-work]]); evidence so
  far is one engineering domain.

## Patterns demonstrated

- [[patterns/quality-bar/complexity-ratchet]] — **the core.** Compound engineering *is* the named,
  productized complexity ratchet: the `compound` step + `docs/solutions/` store is the forward-only
  knowledge floor, and CI branch protection is the "can't regress below the floor" mechanism. This
  is the **independent, non-Garry second example** that promotes the ratchet to `confirmed`.
  ([[sources/every--compound-engineering-plugin#docs-solutions]], `#release-automation`)
- [[patterns/quality-bar/skill-pack-bundle]] — "taste belongs in systems" cashes out as tested
  skills; the plugin ships ~1,094 test cases incl. contract tests — the non-Garry bundle that
  retires that pattern's same-creator caveat. ([[sources/every--compound-engineering-plugin#tests]])
- [[patterns/behavioral/latent-vs-deterministic-split]] — "skills are guardrails for an intelligent
  agent, not a controller for a dumb one; calibrate prescription to the failure mode" is a non-Garry
  statement of the split. ([[sources/every--compound-engineering-plugin#plugin-AGENTS.md]])
- [[patterns/composition/single-source-multi-surface-distribution]] — author once in Claude format,
  convert to ~11 harnesses. ([[sources/every--compound-engineering-plugin#converter]])
- [[patterns/structural/thin-harness-fat-skills]] — capability lives in fat markdown skills over a
  thin deterministic converter/CLI; CE rides harnesses it doesn't own.

## Tensions & counter-arguments

- **Is it distinct from [[patterns/quality-bar/complexity-ratchet]], or Every's branding of it?**
  The two describe the same forward-only principle, named independently (Kieran Klaassen / Every vs.
  Garry Tan). Convergence is *evidence the idea is real* — but "compound engineering" adds a specific
  loop, the 50/50 rule, and the humans-at-the-ends framing the ratchet doesn't, so it earns a
  concept page rather than collapsing into the pattern. Watch for the boundary blurring.
- **The Foxconn-factory counter-weight.** Garry Tan's essay #8 warns that over-investing in "systems"
  — validators, sanitizers, mountains of tests to *police* a capable model — is a cage, not leverage
  ([[sources/garrytan--foxconn-factories#thesis]]). The 50/50 rule could slide exactly there: "spend
  half your time on systems" is only good if those systems are **contracts**, not distrust scaffolding.
  Compound engineering's "taste in systems" has to stay on the ratchet side of that line.
- **Aspirational vs. measured.** The 50/50 rule and "95% garbage" are stated, not benchmarked, and
  the lived evidence is one expert operator's practice (Kieran) plus one plugin — not a team study.
  Whether the discipline survives non-expert teams or scale is unproven
  ([[sources/every--compound-engineering-gets-an-upgrade#root]]).
- **Generalization claim is a hypothesis.** "Applies to knowledge work broadly" is asserted with
  engineering-only evidence ([[sources/every--compound-engineering-gets-an-upgrade#knowledge-work]]).

## Related

- [[patterns/quality-bar/complexity-ratchet]] — *is-the-pattern-form-of:* the cross-artifact technique
  compound engineering names and productizes.
- [[artifacts/plugins/compound-engineering]] — *embodied-by:* the runnable plugin.
- [[patterns/quality-bar/skill-pack-bundle]] · [[patterns/behavioral/latent-vs-deterministic-split]] ·
  [[patterns/composition/single-source-multi-surface-distribution]] — sub-techniques it relies on.
- Karpathy's "LLM Wiki" pattern (this wiki's own foundation) — *kindred:* a knowledge store that
  compounds; #6 of the Garry Tan series credits the same Karpathy pattern as gbrain's inspiration
  ([[sources/garrytan--meta-meta-prompting#book-mirror]]). Compound engineering applies the same
  "knowledge that reloads and compounds" idea to a *coding* workflow.

## What we'd steal

**Exhaustive ledger** (★ = highest-value, clearly portable):

- ★ **Make "compound" a first-class loop step.** After solving something non-trivial, *immediately*
  write the reusable learning so the next pass is cheaper — don't let it evaporate. (This wiki's
  INGEST step 8 + log + the ratchet reflection already do a version of this; the plugin's
  `/ce-compound` 5-dimension overlap check — *update the existing doc when overlap is high, don't
  duplicate* — is a recipe worth importing into our INGEST/LINT.)
- ★ **"Taste belongs in systems, not review."** Encode judgment as schemas, checks, and tests rather
  than re-applying it by hand each time. Directly maps to our `_schemas/` + LINT + the det/latent
  step tagging.
- ★ **The 50/50 budget.** Spend half your effort on the system that produces work, not just the work.
  A blunt, memorable allocation rule that resists the "always ship features" gravity.
- ★ **Humans at the ends, AI in the middle.** As capability rises, move human attention *outward* to
  "what's worth building" (ideate/brainstorm) and "does it feel right" (polish) — not to babysitting
  execution.
- **The 8-step loop** (ideate → brainstorm → plan → work → review → polish → compound → repeat) as a
  default agent-coding workflow with a named artifact per step (requirements doc → plan → PR →
  review → learning).
- **The adoption ladder** (Stage 0 manual → Stage 5 parallel cloud) as a maturity model for
  human↔agent division of labor — useful for diagnosing "where is this team/setup."
- **The "work is boring now" signal.** When the execution middle stops needing you, that's the cue to
  invest at the ends, not to declare victory.
- **The eight beliefs to unlearn** as a provocation list for any team adopting agents
  ([[sources/every--compound-engineering#unlearn]]).
- **Dogfooding as the proof.** Build the tool with the tool and keep the audit trail
  (brainstorms/plans/solutions) — it's both evidence and the ratchet's substrate.

## Open questions

- Is compound engineering a genuinely distinct concept or Every's productized branding of the same
  forward-only principle as [[patterns/quality-bar/complexity-ratchet]]? (Best answer so far: distinct
  enough — it adds the loop, the 50/50 budget, and the humans-at-the-ends framing — but the core is
  shared.)
- Does the 50/50 rule survive team scale and non-expert operators, or is it an expert-solo discipline?
- Where exactly is the line between "taste in systems" and the Foxconn-factory cage? (Same boundary
  the ratchet pattern flags — contracts vs. distrust scaffolding.)
- Is "95% garbage / 50% on the second try" a real measured rate or an illustrative figure?
- Does the claim that it "applies to knowledge work broadly" hold outside software?
