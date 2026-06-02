---
domain: sources
type: article
url: https://x.com/garrytan # profile; canonical post URL not yet confirmed — TODO
retrieved: 2026-06-01
snapshot-location: sources/garrytan--skillify-manifesto/snapshot.md
upstream-commit: n/a (essay, not a repo)
last-reviewed: 2026-06-01
---

# "How to really stop your agents from making the same mistakes (The Skillify Manifesto)" (`garrytan`, essay)

> Garry Tan's manifesto arguing that AI-agent reliability is "vibes-based" until you adopt an opinionated workflow: turn every failure into a tested skill so the bug becomes *structurally impossible* to recur. The source for the canonical **10-step skillify checklist**, the two worked failure→skill examples (`calendar-recall`, `context-now`), the latent-vs-deterministic "wrong side, not wrong answer" framing, and the GBrain-vs-Hermes "creation vs. verification" split. Essay #5 of Garry's 8-part AI Explainer series.

## Snapshot details

- **Retrieved**: 2026-06-01 (pasted verbatim by Sidney; we hold the full text, author's typos preserved).
- **Where it lives in this wiki**: [`sources/garrytan--skillify-manifesto/snapshot.md`](garrytan--skillify-manifesto/snapshot.md) — verbatim, immutable.
- **Upstream URL**: not yet confirmed. Reads as an X long-form post / blog essay under [@garrytan](https://x.com/garrytan). **TODO**: locate canonical URL + publication date and add an archive.org link.
- **Publication date**: unconfirmed; **estimated ~May 2026** from internal evidence:
  - Back-references the resolvers essay ("I wrote about resolvers in detail here" → [[sources/garrytan--resolvers]], essay #2) and the thin-harness/fat-skills framing (essay #1, [[sources/garrytan--thin-harness-fat-skills]]).
  - Cites **LangChain "$160 million" / "billion-dollar valuation" / LangSmith** as the funded-but-workflow-less foil.
  - Cites **Nous Research's "Hermes Agent"** with its **`skill_manage`** tool, **MEMORY.md capped at 2,200 chars**, progressive disclosure, and conditional activation — a contemporaneous competitor framing.
  - Contains the **canonical 10-step skillify checklist** and the **calendar-recall / context-now** failure→skill examples (calendar history "3,146 calendar files spanning 2013 through 2026"; a "2026-04-21" timestamp inside a `context-now.mjs` payload).
  - Star-count signals (gstack/gbrain) are *absent* from this essay — unlike the bookend essays #1 (72K) and #8 (105K) — so date is bounded only by the cross-references above, not by a star figure (see Series context).

## Anchor map

Every claim citing this source uses a `#anchor` from this list. The essay is one prose file; anchors are thematic pointers into the author's own section headers and worked examples. **Do not invent anchors beyond this map.**

- `#root` — the essay as a whole
- `#pieces-arent-a-practice` — the LangChain/LangSmith critique: funded testing *primitives* (trajectory evals, trace-to-dataset, LLM-as-judge, regression suites) but "no opinionated workflow that says, in order…"; "a gym membership without a workout plan"
- `#vibes-based-reliability` — "Most AI agent 'reliability' is vibes-based" — prompt tweaks, bigger system messages, "please don't hallucinate" incantations that decay as context grows
- `#failure-1-calendar` — Failure 1, "The Trip That Was Already in the Database": the OpenClaw spent 5 minutes hitting blocked live calendar APIs + noisy email search when the answer was one `grep` away in the local brain (3,146 indexed calendar files, 2013–2026)
- `#wrong-side-not-wrong-answer` — the core diagnosis: "That's the bug. Not a wrong answer. A wrong side." — deterministic work (calendar grep, timestamp math) executed in latent space
- `#latent-vs-deterministic` — the binary: **latent** = requires judgment; **deterministic** = same-input/same-output, "no model needed"; put each task on the correct side
- `#skill-as-method-call` — "a skill is a markdown procedure that teaches the model how to approach a task… Think of it like a method call: same procedure, radically different outputs depending on what you pass in" (the user supplies the *what*, the skill supplies the *process*)
- `#latent-builds-deterministic` — the load-bearing loop: "the latent space builds the deterministic tool, then the deterministic tool constrains the latent space"; "The model's intelligence created the constraint that prevents the model from being stupid"; the agent itself wrote `calendar-recall.mjs`, then the skill forces it to run the script. Old failure path becomes "structurally unreachable"
- `#calendar-recall-skill` — the `calendar-recall` SKILL.md (Steps 1+2): "Brain-first historical calendar lookup. ALWAYS use this before any live API"; hard rule = live APIs ONLY for future/last-48h; `node scripts/calendar-recall.mjs search "Singapore"` returns in <100ms (Bun startup), zero LLM/network calls
- `#failure-2-timezone` — Failure 2, "28 Minutes": agent did UTC→PT math in its head, off by exactly an hour (said 28 min, reality 88); `context-now.mjs` already existed and outputs `minutesUntil: 88` in ~50ms — "The agent just didn't run it"
- `#context-now-skill` — the `context-now` SKILL.md (Steps 1+2): "ALWAYS-ON discipline: run context-now.mjs before making ANY time-sensitive claim. Never do UTC→PT conversion in your head"
- `#skillify-checklist` — **the canonical 10-step checklist** when a failure gets promoted: (1) SKILL.md contract (2) deterministic code (3) unit tests/vitest (4) integration tests/live endpoints (5) LLM evals (6) resolver trigger in AGENTS.md (7) resolver eval (8) check-resolvable + DRY audit (9) E2E smoke test (10) brain filing rules. "A feature that doesn't pass all ten is not a skill. It's just code that happens to work today."
- `#skillify-as-verb` — "skillify" as a one-word command: prototype in conversation → see it work → say "skillify it" → the ad-hoc session becomes a durable tested skill + resolver entry + docs. Worked examples: OAuth webhook, headless/headed browser decision tree, ngrok-link curl check, double-booked-calendar check. "I don't write specs. I don't file tickets."
- `#step3-unit-tests` — vitest on pure functions (`parseEventLine`, `eventMatchesKeyword`, `searchKeyword`, `formatJson`) against fixtures; DST-boundary test that reproduces the exact "28 minutes" bug. **"179 unit tests across 5 suites… run in under 2 seconds"** (author self-claim)
- `#step4-integration-tests` — live-endpoint/real-data tests catching what clean fixtures miss (malformed event lines, Windows line endings, midnight-spanning events). Rule: "if you find yourself manually checking… that check should be an integration test"
- `#step5-llm-evals` — LLM-as-judge for judgment-requiring outputs; **"35 evals run daily"** for context-now (author self-claim); evals check the *process* (did it run the script?) not just the answer. "Search your conversation history for when you said 'fucking shit' or 'wtf.' Those are the test cases you're missing."
- `#step6-resolver-trigger` — "A resolver is a routing table for context: when task type X appears, load skill Y"; each skill needs a trigger row in AGENTS.md; bug caught = a skill that exists but is unreachable ("a surgeon on staff but not in the hospital directory")
- `#step7-resolver-eval` — "the layer most people miss entirely": tests that a trigger *actually routes*. **"50+ test cases"** like `{ intent: 'find my 2016 trip', expectedSkill: 'calendar-recall' }` (author self-claim). Two failure modes: false negative (should fire, doesn't) and false positive (wrong skill fires on overlapping triggers). Run as both structural (does AGENTS.md table map right?) AND LLM routing (does the model actually pick right?) tests
- `#step8-check-resolvable-dry` — after a month, "40+ skills"; `check-resolvable` walks AGENTS.md resolver → SKILL.md → script/cron and flags unreachable ("dark") skills. **"First run found 6 unreachable skills out of 40+. Fifteen percent of the system's capabilities were dark."** Now runs weekly in `gbrain doctor`. DRY audit parses an in-`SKILL.md` lane matrix and fails the build if a new skill steps on another's lane (author self-claim)
- `#step9-e2e-smoke` — the full pipeline end-to-end; "the last line of defense" because skill+script+resolver can all be correct and "the agent can still choose to ignore all of it and wing it"
- `#step10-brain-filing` — every brain-writing skill must consult filing rules; **"I caught 10 out of 13 brain-writing skills filing to the wrong directory"** because each hardcoded its own paths; filing-rules doc catalogs misfiling patterns. "Zero misfilings since" (author self-claim)
- `#gbrain-skillpack` — "A GBrain SkillPack is a portable bundle of skills, resolver triggers, deterministic scripts, and tests that you can install into any agent setup just by asking OpenClaw/Hermes Agent"; "The skillify checklist… is what `gbrain doctor` actually checks"; `gbrain doctor --fix` auto-repairs DRY violations, guarded by git working-tree checks
- `#hermes-creation-vs-verification` — Hermes Agent (Nous Research) has `skill_manage` (agent creates/patches/deletes its own skills), progressive disclosure, MEMORY.md capped at 2,200 chars, conditional activation — "Smart design." **But** "Hermes doesn't test its skills." "Hermes handles creation beautifully. GBrain handles verification. You need both."
- `#untested-skills-rot` — the failure modes of any untested skill system: duplicate skills (`deploy-k8s` Mon vs `kubernetes-deploy` Thu) with ambiguous routing; skills that silently return garbage after an upstream API change; orphan skills with weak triggers "eating index tokens… slowly rotting." "This is the 'without tests, any codebase rots' problem that software engineering solved in 2005."
- `#big-idea` — the thesis: "In a healthy software engineering team, every bug gets a test. That test lives forever… AI agents should work the same way." "Every failure becomes a skill. Every skill has evals. Every eval runs daily. The agent's judgment improves permanently."
- `#boil-the-ocean` — the close: "Boil the ocean. Make your agent do something, then skillify it… and you have a god damn smart OpenClaw"; or "load GBrain, use all the code I've already written, and skip ahead to your own Jarvis from Iron Man sooner"
- `#repo-links` — the sign-off links: `github.com/garrytan/gstack` and `github.com/garrytan/gbrain`

## Why we cite this

- **The single richest articulation of [[patterns/quality-bar/skill-pack-bundle]] we have.** Essay #8 ([[sources/garrytan--foxconn-factories]]) names the 7-part skill pack; *this* essay expands it to a **10-step ordered checklist** with a worked rationale for each step (and explicitly states the checklist "is what `gbrain doctor` actually checks") ([[sources/garrytan--skillify-manifesto#skillify-checklist]], [[sources/garrytan--skillify-manifesto#gbrain-skillpack]]). The two extra steps over the essay-#8 list — **check-resolvable + DRY audit** (Step 8) and **brain filing rules** (Step 10) — are the system-hygiene layer.
- **The clearest statement of [[patterns/behavioral/latent-vs-deterministic-split]]:** "That's the bug. Not a wrong answer. A wrong side." ([[sources/garrytan--skillify-manifesto#wrong-side-not-wrong-answer]], [[sources/garrytan--skillify-manifesto#latent-vs-deterministic]]). The calendar-grep and timezone-math examples are the canonical illustrations of deterministic work mistakenly done in latent space.
- **The "latent builds deterministic, then deterministic constrains latent" loop** ([[sources/garrytan--skillify-manifesto#latent-builds-deterministic]]) — the mechanism underneath [[patterns/structural/thin-harness-fat-skills]]: the model's judgment writes the script that then prevents the model from improvising.
- **The "skill as a parameterized method call" framing** ([[sources/garrytan--skillify-manifesto#skill-as-method-call]]) — grounds [[patterns/behavioral/skill-as-method-call]] in the author's own words.
- **The resolver-routing material** ([[sources/garrytan--skillify-manifesto#step6-resolver-trigger]], [[sources/garrytan--skillify-manifesto#step7-resolver-eval]], [[sources/garrytan--skillify-manifesto#step8-check-resolvable-dry]]) — the most operational description of [[patterns/composition/resolver-routing-table]] in the series: trigger evals, false-positive/false-negative modes, the `check-resolvable` reachability audit, and the "dark skills" failure (15% unreachable on first audit).
- **The forward-only quality thesis** ("every bug gets a test… that test lives forever") grounds [[patterns/quality-bar/complexity-ratchet]] — quality only goes up because every failure adds a permanent daily-running eval ([[sources/garrytan--skillify-manifesto#big-idea]]).
- **The GBrain-vs-Hermes "creation vs. verification" distinction** ([[sources/garrytan--skillify-manifesto#hermes-creation-vs-verification]]) — a sharp competitive framing: a peer system (Nous Research's Hermes Agent) has agent-driven skill *creation* but no *testing*; positions GBrain's value as the verification layer.
- **A "talked-about / named-person-quoted" popularity signal** in its own right (a YC CEO's reliability manifesto), and a longitudinal data point in the gstack/gbrain growth time-series (here: notably *no* star claim — see below).

## Popularity signals (this source IS one)

This essay is itself a **"talked-about / named-person-quoted"** signal (a YC CEO's manifesto on agent reliability). Distinct from the bookend essays, it carries **no GitHub-star claim** — its hard metrics are the author's **personal skillpack-test footprint**, useful as evidence of real production usage, but author self-claims that we have only *partially* grounded in the public repos.

- **Signal type**: named-person-quoted manifesto + author-self-claim usage metrics. No star/install/marketplace number in this essay.
- **As-of**: 2026-06-01 (retrieval of the essay text).
- **Time-series note**: across the 8-essay series, gstack stars climb **72K → 75K → 87K → 93K → 105K** and gbrain **14K → 20K**. **This essay contributes no star figure** — date-ordering for essay #5 must lean on the cross-references (resolvers essay back-ref; LangChain $160M; Hermes Agent), not a star count.
- **Hard metrics in this essay (ALL author self-claims; grounding status noted):**
  - **"179 unit tests across 5 suites… run in under 2 seconds"** ([[sources/garrytan--skillify-manifesto#step3-unit-tests]]) — *author self-claim*, about his **personal** brain repo (the public gbrain repo has its own large test suite but not these exact `calendar-recall` unit tests; see Contradictions).
  - **"35 evals run daily"** for context-now ([[sources/garrytan--skillify-manifesto#step5-llm-evals]]) — *author self-claim*, personal repo.
  - **"50+ [resolver-eval] test cases"** ([[sources/garrytan--skillify-manifesto#step7-resolver-eval]]) — *author self-claim*. The public gbrain DOES ship resolver evals (`test/resolver.test.ts`, `test/check-resolvable.test.ts`) but they use reachability/structural assertions, not the literal `{ intent, expectedSkill }` JSON table shown (see Contradictions).
  - **"First run found 6 unreachable skills out of 40+. Fifteen percent of the system's capabilities were dark."** ([[sources/garrytan--skillify-manifesto#step8-check-resolvable-dry]]) — *author self-claim*; the `check-resolvable` tool it describes **is real and verified** in public gbrain (`src/commands/check-resolvable.ts`).
  - **"I caught 10 out of 13 brain-writing skills filing to the wrong directory"; "Zero misfilings since"** ([[sources/garrytan--skillify-manifesto#step10-brain-filing]]) — *author self-claim*; the filing-rules doc it describes **is real** in public gbrain (`skills/_brain-filing-rules.md`, with the exact "Common Misfiling Patterns" table).
  - **"3,146 calendar files spanning 2013 through 2026"** ([[sources/garrytan--skillify-manifesto#failure-1-calendar]]) — *author self-claim* about his personal brain corpus.
- **Third-party / ecosystem signals referenced (not Garry's):**
  - **LangChain: "$160 million" raised, "billion-dollar valuation," three years, LangSmith** ([[sources/garrytan--skillify-manifesto#pieces-arent-a-practice]]) — cited as the funded-but-workflow-less foil. **Unverified** by us (no LangChain/LangSmith snapshot in this wiki); treat as the author's framing.
  - **Nous Research "Hermes Agent": `skill_manage` tool, MEMORY.md capped at 2,200 chars** ([[sources/garrytan--skillify-manifesto#hermes-creation-vs-verification]]) — cited as a real competitor doing agent-driven skill creation. **Unverified** by us.

## Series context

This is **essay #5 of 8** in Garry Tan's "AI Explainer" series. The series is a longitudinal record of the gstack/gbrain thesis (and, via star counts, their growth). Sibling essays by canonical slug:

1. [[sources/garrytan--thin-harness-fat-skills]] — #1, the core architecture (thin harness, fat skills; latent vs deterministic). **This essay explicitly leans on it** ("In the framework I've been writing about (thin harness, fat skills)…").
2. [[sources/garrytan--resolvers]] — #2, the resolver routing table. **This essay explicitly back-references it** ("I wrote about resolvers in detail here") — strong ordering evidence that #5 post-dates #2.
3. [[sources/garrytan--loc-controversy]] — #3, the lines-of-code controversy.
4. [[sources/garrytan--naked-models]] — #4, naked models.
5. **[[sources/garrytan--skillify-manifesto]]** — #5, **this essay** (the 10-step skillify checklist; GBrain-vs-Hermes).
6. [[sources/garrytan--meta-meta-prompting]] — #6, meta-meta-prompting.
7. [[sources/garrytan--complexity-ratchet]] — #7, the complexity ratchet (forward-only quality). **Thematically adjacent**: this essay's "every bug gets a test that lives forever" is the seed of the ratchet idea.
8. [[sources/garrytan--foxconn-factories]] — #8, the "skill pack" definition + ~105K-star claim + OpenClaw-authorship correction. **Already ingested**; this page mirrors its structure.

**Ordering evidence specific to #5:** the explicit back-references to the resolvers essay (#2) and the thin-harness framing (#1) place this *after* both. The absence of a star figure means we cannot pin it on the 72K→105K curve; the LangChain "$160M / billion-dollar valuation" and Hermes "skill_manage" references anchor it to **~May 2026**.

## Contradictions & tensions (for LINT)

1. **Personal repo vs. public repo grounding.** The essay's hero examples — `calendar-recall` and `context-now` with "179 unit tests," "35 daily evals" — live in Garry's **personal** brain repo, **not** the public [[sources/garrytan--gbrain]] we snapshotted. Partial grounding exists: `context-now` appears in public gbrain only as a **test fixture** (`test/fixtures/openclaw-reference-minimal/skills/context-now/SKILL.md`), and `calendar-recall` does not appear at all. **Implication for the wiki:** cite the *pattern* (skillify checklist, latent/deterministic split) to this essay, but ground the *machinery* (check-resolvable, doctor, dry-fix, filing-rules, skillify scaffold) to the verified public gbrain files — do not present the per-skill counts as repo-verifiable. Flag for human review; not a contradiction, a provenance boundary.
2. **Resolver-trigger location: AGENTS.md (essay) vs. RESOLVER.md (public repo).** The essay repeatedly says triggers are "an entry in AGENTS.md" ([[sources/garrytan--skillify-manifesto#step6-resolver-trigger]]). In public gbrain the trigger *table* actually lives in `skills/RESOLVER.md`, with `AGENTS.md` merely *pointing* to it ("RESOLVER.md — skill dispatcher. Read before any task" — [[sources/garrytan--gbrain#AGENTS.md]], [[sources/garrytan--gbrain#skills-resolver]]). Reconcilable (AGENTS.md is the entry doc, RESOLVER.md the dispatcher it loads), but a future reader citing "AGENTS.md table" should know the literal table is in RESOLVER.md.
3. **Resolver-eval format: illustrative JSON vs. real test.** The essay shows `{ intent, expectedSkill }` literal cases ([[sources/garrytan--skillify-manifesto#step7-resolver-eval]]). The real public test (`test/resolver.test.ts`) delegates to `checkResolvable()` and uses structural `expect(...).toContain(...)` assertions over RESOLVER.md, not that JSON array. The essay's format is pedagogical; the verified mechanism is reachability + structural validation. Note when grounding [[patterns/composition/resolver-routing-table]].
4. **"Latent" is essay vocabulary, not repo vocabulary.** "deterministic" appears in gstack `CLAUDE.md` / `ARCHITECTURE.md`, but the literal word **"latent" has zero hits** in those gstack docs. The latent/deterministic *binary* is the essay's framing (shared with essay #1); the repo grounding for the *split* is the real deterministic CLIs (gstack `bin/`, `scripts/resolvers/`) vs. latent markdown skills — not a literal "latent" label in code.
5. **OpenClaw authorship (carried from essay #8).** This essay says "building my OpenClaw (and GBrain)" and "your own OpenClaw" ([[sources/garrytan--skillify-manifesto#skillify-as-verb]], [[sources/garrytan--skillify-manifesto#boil-the-ocean]]), again implying OpenClaw is Garry's. Per [[sources/garrytan--foxconn-factories#openclaw]], **OpenClaw is Peter Steinberger's harness**; `garrytan/openclaw` is most likely Garry's fork/deployment. Same correction applies here.
6. **Tokenmaxxing vs. cost-rationing (carried from essay #8).** This essay's "Boil the ocean" / "load GBrain and skip ahead" ([[sources/garrytan--skillify-manifesto#boil-the-ocean]]) extends the spend-freely instinct of [[sources/garrytan--foxconn-factories#tokenmaxxing]], still in apparent tension with gbrain's cost-confrontation banner ([[sources/garrytan--gbrain#AGENTS.md]]). Tracked as an open question, not resolved here.
7. **Pro-test stance vs. the essay-#8 "Foxconn factory" 276K-test self-audit.** This essay is maximally pro-test ("a feature that doesn't pass all ten is not a skill"). Essay #8 simultaneously audits gstack at **~262K app LOC + ~276K test LOC** ([[sources/garrytan--foxconn-factories#factory-audit]]) and warns against over-building "Foxconn factories." The reconciliation Garry would draw — *test the skill, don't build a cage around the model* — is implicit but not stated in either essay; worth a synthesis note when both are cross-linked.

## Related sources

- [[sources/garrytan--foxconn-factories]] — sibling essay #8; the 7-part skill-pack definition that *this* essay expands into the 10-step checklist. Read together for the full [[patterns/quality-bar/skill-pack-bundle]] articulation.
- [[sources/garrytan--thin-harness-fat-skills]] — sibling #1; the architecture this essay assumes ("the framework I've been writing about").
- [[sources/garrytan--resolvers]] — sibling #2; the resolver deep-dive this essay back-references for Steps 6–8.
- [[sources/garrytan--complexity-ratchet]] — sibling #7; the forward-only-quality idea this essay seeds.
- [[sources/garrytan--gbrain]] — the repo that **really grounds the machinery**: `skills/skillify/SKILL.md`, `skills/RESOLVER.md` (Step 6), `src/commands/check-resolvable.ts` + `test/check-resolvable.test.ts` (Step 8), `src/commands/doctor.ts` + `test/doctor-fix.test.ts` + `src/core/dry-fix.ts` (`gbrain doctor --fix`, Step 8), `skills/_brain-filing-rules.md` (Step 10), `src/core/skillify/generator.ts` + `test/skillify-scaffold.test.ts` (the skillify scaffold). Anchors: [[sources/garrytan--gbrain#skills-resolver]], [[sources/garrytan--gbrain#skills-brain-filing-rules]], [[sources/garrytan--gbrain#skill-skillify]], [[sources/garrytan--gbrain#AGENTS.md]].
- [[sources/garrytan--gstack]] — sibling product; ships its own `/skillify` skill (`skillify/SKILL.md` — codify a `/scrape` flow into `script.ts + script.test.ts + fixture`) and the deterministic/latent substrate (`bin/`, `scripts/resolvers/` + resolver tests `test/resolver-ask-user-format.test.ts`, `test/writing-style-resolver.test.ts`). Anchors: [[sources/garrytan--gstack#skillify]], [[sources/garrytan--gstack#test]], [[sources/garrytan--gstack#ARCHITECTURE.md]].
- [[creators/garry-tan]] — author.
