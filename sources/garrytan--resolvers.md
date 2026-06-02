---
domain: sources
type: article
url: https://x.com/garrytan # profile; canonical post URL not yet confirmed — TODO
retrieved: 2026-06-01
snapshot-location: sources/garrytan--resolvers/snapshot.md
upstream-commit: n/a (essay, not a repo)
last-reviewed: 2026-06-01
---

# "Resolvers: The Routing Table for Intelligence" (`garrytan`, essay)

> Garry Tan's essay #2 of his "AI Explainer" series, arguing that the **resolver** — a ~200-line markdown routing table that maps "when task type X appears, load document Y first" — is the most important and most-ignored of the patterns from essay #1. It reframes the resolver as the *governance / management layer* of an agent organization (org chart + filing clerk + audit + performance review), and tells the war stories (a 20,000-line `CLAUDE.md`, a misfiled Will Manidis essay, an invisible signature-tracking skill, the `check-resolvable` meta-skill) that produced the real gbrain/gstack resolver machinery. Our primary source for Garry's articulation of [[patterns/composition/resolver-routing-table]] and the "resolvers are fractal" claim.

## Snapshot details

- **Retrieved**: 2026-06-01 (pasted verbatim by Sidney Swift; we hold the full text).
- **Where it lives in this wiki**: [`sources/garrytan--resolvers/snapshot.md`](garrytan--resolvers/snapshot.md) — verbatim, immutable, author's typos and smart-quotes preserved.
- **Upstream URL**: not yet confirmed. Reads as an X long-form post / blog essay under [@garrytan](https://x.com/garrytan). **TODO**: locate the canonical URL + publication date and add an archive.org link.
- **Publication date**: unconfirmed; estimate **≈April–May 2026**. Internal evidence:
  - **Builds directly on essay #1** "Thin Harness, Fat Skills" — opens by recapping its "five definitions" (skill-as-method-call, diarization, thin harness) ([[sources/garrytan--resolvers#the-20000-line-confession]] / [[sources/garrytan--resolvers#intro]]).
  - **References Will Manidis's "No New Deal for OpenAI"** as a piece the author's agent recently ingested ([[sources/garrytan--resolvers#the-misfiling]]).
  - **References Claude Code's "AutoDream"** memory-consolidation system as a shipped, primitive version of the self-healing resolver ([[sources/garrytan--resolvers#context-rot]]).
  - **GStack star count cited at "72,000+"** ([[sources/garrytan--resolvers#open-source-close]]) — strictly *below* the ~105K that essay #8 cites and the **105,768** measured live (2026-06-01), placing this essay **earlier in the time-series** (see Series context).
  - Describes the author's personal production system at **"25,000 files," "200 inputs a day," "40+ skills"** ([[sources/garrytan--resolvers#fractal]] / [[sources/garrytan--resolvers#build-your-own-brain]]).

## Anchor map

Every claim citing this source uses a `#anchor` from this list. The essay is one prose file; anchors are thematic pointers into the author's own section headers. **Do not invent anchors outside this list.**

- `#root` — the essay as a whole
- `#intro` — the opening definition: *"A resolver is a routing table for context. When task type X appears, load document Y first."* The thesis that resolvers are "invisible when they work, and catastrophic when they don't."
- `#the-20000-line-confession` — the 20,000-line `CLAUDE.md` that "drowned" the model; Claude Code itself told him to cut it back; the fix was "about 200 lines… a numbered decision tree. Pointers to documents." (person → `/people/`, company → `/companies/`, policy → `/civic/`)
- `#the-misfiling` — the Will Manidis "No New Deal for OpenAI" essay misfiled to `sources/` instead of `civic/`; root cause: idea-ingest had "hardcoded `brain/sources/` as the default" and "didn't consult the resolver"
- `#the-audit` — the audit of "13 skills that write to the brain"; only "3 of 13 referenced the resolver"; the fix was a shared `_brain-filing-rules.md` + a mandate that "every brain-writing skill reads `RESOLVER.md` before creating any page"; "One rule. Ten skills fixed." "Zero misfilings since."
- `#filing-mandate` — the literal two-line mandate added to every brain-writing skill: *"Before creating any new brain page, read `brain/RESOLVER.md` and `skills/_brain-filing-rules.md`. File by primary subject, not by source format or skill name."*
- `#invisible-skill` — the "invisible skill" problem: a signature-tracking capability inside the executive-assistant skill that the resolver had no trigger for. *"A skill that exists but isn't reachable creates the illusion of capability."* "After a month… 40+ skills."
- `#trigger-evals` — "resolver trigger evals": a suite of "50 sample inputs with expected outputs" (e.g. `"check my signatures"` → executive-assistant); the two failure modes — **false negative** (skill should fire but doesn't) and **false positive** (wrong skill fires) — "Both fixable by editing markdown. No code changes." *"If you can't prove the right skill fires for the right input, you don't have a system."*
- `#check-resolvable` — the `check-resolvable` **meta-skill** that "walks the entire chain — AGENTS.md → skill file → code — and finds dead links." First run found "6 unreachable skills" out of 40+ ("Fifteen percent of the system's capabilities were dark"); "Now check-resolvable runs weekly… the resolver equivalent of a linter."
- `#context-rot` — resolvers "decay": Day 1 perfect → Day 90 "a historical document." The YC-CTO question about an **RLM** (reinforcement-learning loop over task dispatches) that "rewrites the resolver based on observed evidence"; "Eight hundred task dispatches over a month." Claude Code's **AutoDream** named as "a primitive version." *"A resolver that learns from its own traffic. That's the endgame for agent governance."*
- `#fractal` — "Resolvers are fractal" / "resolvers all the way down": the **skill resolver** (AGENTS.md, task→skill), the **filing resolver** (RESOLVER.md, content-type→directory), and the **context resolver** *inside each skill* (executive-assistant routes email-triage vs scheduling vs signatures). "Claude Code already has this pattern. Every skill has a description field… The description *is* the resolver." Scales "from 5 skills to 50, from 1,000 files to 25,000… processes 200 inputs a day."
- `#shape-of-the-thing` — the five-line summary pattern: *Load the right context at the right moment. Don't cram. / Mandate that every skill consults the resolver. / Test the routing, not just the output. Trigger evals. / Audit reachability. Check-resolvable. Weekly. / Make the resolver learn from its own traffic.* "The resolver is the governance layer of an agent system."
- `#management-metaphor` — "What I actually built is closer to management." Skills = employees; the resolver = the org chart (+ escalation logic); filing rules = internal process; `check-resolvable` = audit & compliance; trigger evals = performance reviews. *"The problem isn't that models aren't smart enough… we've been building organizations with no management layer."*
- `#build-your-own-brain` — the open-source close: GBrain ships the resolver pattern built in ("`gbrain init` creates RESOLVER.md, the decision tree, and the disambiguation rules"; "The check-resolvable skill comes built-in"); GStack is "the coding layer… Fat skills in markdown"; "OpenClaw or Hermes Agent is the conductor — the thin harness."
- `#open-source-close` — the hard metrics + ownership pitch in the close: "72,000+ stars on GitHub" (GStack), "25,000 files," "200 inputs daily"; *"the brain is a git repo you own… If any piece disappeared tomorrow, your knowledge survives as plain text files."* "the new dawn of personal software… your own personal mini-AGI."

## Why we cite this

- **The single clearest first-person articulation of the resolver pattern** — the author defining the routing table as *governance*, with five concrete sub-mechanisms (the resolver doc, the filing-rules mandate, trigger evals, `check-resolvable`, the self-healing loop). The canonical grounding text for [[patterns/composition/resolver-routing-table]].
- **The "resolvers are fractal" claim** ([[sources/garrytan--resolvers#fractal]]) — resolvers exist at the skill layer (AGENTS.md), the filing layer (RESOLVER.md), and *inside* each skill; ties Garry's pattern directly to Claude Code's native "description field = the resolver" mechanism. Supports both [[patterns/composition/resolver-routing-table]] and [[patterns/structural/thin-harness-fat-skills]].
- **The "test the routing, not just the output" discipline** — trigger evals with explicit false-negative / false-positive failure modes ([[sources/garrytan--resolvers#trigger-evals]]). Grounded by the **real** `routing-eval.jsonl` fixtures that ship in gbrain (see Related sources), and the gstack `scripts/resolvers/` + resolver tests. Reinforces [[patterns/quality-bar/skill-pack-bundle]] (resolver + resolver-eval are two of its parts).
- **The "invisible skill" / reachability anti-pattern** ([[sources/garrytan--resolvers#invisible-skill]], [[sources/garrytan--resolvers#check-resolvable]]) — "a surgeon the hospital can't find"; the counter-example that a skill-pack bundle and a resolver exist to prevent. The grounding for treating reachability auditing as a quality bar.
- **The "don't cram the context window" thesis** ([[sources/garrytan--resolvers#the-20000-line-confession]]) — a vivid, quotable framing (200 lines of pointers replacing 20,000 lines of instructions) of *why* intelligence belongs in load-on-demand skills, not a fat system prompt. The behavioral half of [[patterns/structural/thin-harness-fat-skills]].
- **A longitudinal popularity data-point** for GStack ("72,000+ stars") and Garry's private brain ("25,000 files / 200 inputs/day / 40+ skills") — see Popularity signals. These let the wiki track gstack/gbrain growth across the 8-essay series.
- **An "ecosystem governance" framing** ([[sources/garrytan--resolvers#management-metaphor]]) — the "agents are an organization, the resolver is the missing management layer" metaphor, useful for analyses on why mature skill packs converge on routing + eval + audit machinery.

## Popularity signals (this source IS one)

This essay is itself a **"talked-about / named-person-quoted"** signal (a YC CEO's widely-circulated explainer, written from live YC office-hours with founders), and it carries several hard metrics. The 8-essay series is a **longitudinal time-series of gstack/gbrain growth** — capture each datapoint with its as-of context and flag author self-claims.

- **GStack GitHub stars (author self-claim, this essay)**: **"72,000+ stars on GitHub"** ([[sources/garrytan--resolvers#open-source-close]]). *As-of: essay-internal, ≈April–May 2026 (author self-claim).* **For comparison — measured live**: `gh api repos/garrytan/gstack` returns **105,768 stars** (as-of 2026-06-01); repo created **2026-03-11**. The 72K figure is therefore an **earlier reading** in the series (75K→87K→93K→105K are cited by later essays), consistent with this being essay #2. Stars move — re-measure before citing later.
- **GBrain (sibling) — measured live for context**: **20,405 stars** via `gh api repos/garrytan/gbrain` (as-of 2026-06-01); repo created **2026-04-05**. This essay does not state a gbrain star count; recorded here only to anchor the series' gbrain track (≈14K→20K across the series).
- **Garry's personal production brain (author self-claim)**: **"25,000 files"**, **"200 inputs a day"** / "processes 200 inputs daily", **"40+ skills"** ([[sources/garrytan--resolvers#fractal]], [[sources/garrytan--resolvers#build-your-own-brain]], [[sources/garrytan--resolvers#open-source-close]]). *As-of: essay-internal, ≈April–May 2026 (author self-claim).* Note: these describe Garry's **private** brain, distinct from the open-source gbrain repo's own demo banner ("17,888 pages, 4,383 people, 723 companies, 21 cron jobs" — [[sources/garrytan--gbrain#README]]) captured 2026-05-21. The essay's "25,000 files" exceeds the repo banner's "17,888 pages," i.e. the private brain is larger / later than the snapshotted demo numbers.
- **Audit / reachability metrics (author self-claim, narrative)**: "13 skills that write to the brain," "**only 3 of 13** referenced the resolver"; `check-resolvable` first run found "**6 unreachable** skills out of 40+ (**fifteen percent**… dark)"; "**14,700 files**" cited mid-essay as the then-size of the knowledge base ([[sources/garrytan--resolvers#the-audit]], [[sources/garrytan--resolvers#check-resolvable]]). *(Author self-claim; note the mid-essay "14,700 files" vs the close's "25,000 files" — see Contradictions.)*
- **Trigger-eval / RLM figures (author self-claim, illustrative)**: trigger-eval suite of "**50 sample inputs**"; the RLM thought-experiment cites "**Eight hundred task dispatches over a month**" ([[sources/garrytan--resolvers#trigger-evals]], [[sources/garrytan--resolvers#context-rot]]). *(Illustrative author self-claims, not measured artifacts.)*

## Series context

This is **essay #2 of 8** in Garry Tan's "AI Explainer" series. The series reads as a longitudinal log of building gstack/gbrain, with GitHub star counts climbing across the run (≈72K→75K→87K→93K→105K for gstack; ≈14K→20K for gbrain), which gives a coarse ordering signal.

Siblings (canonical slugs):
1. [[sources/garrytan--thin-harness-fat-skills]] — **#1**, the conceptual parent. This essay opens by recapping its "five definitions" and explicitly says the resolver "is the one that got almost no attention" there. *(Snapshot present in this wiki; its `/enrich-founder` + "says vs actually building" diarization example grounds [[patterns/behavioral/diarization]].)*
2. [[sources/garrytan--resolvers]] — **#2** (this page).
3. [[sources/garrytan--loc-controversy]] — #3.
4. [[sources/garrytan--naked-models]] — #4.
5. [[sources/garrytan--skillify-manifesto]] — #5 (the 10-step skill-pack checklist; richest articulation of [[patterns/quality-bar/skill-pack-bundle]]).
6. [[sources/garrytan--meta-meta-prompting]] — #6.
7. [[sources/garrytan--complexity-ratchet]] — #7 (grounds [[patterns/quality-bar/complexity-ratchet]]).
8. [[sources/garrytan--foxconn-factories]] — **#8**, ALREADY INGESTED; this page matches its structure. It cites gstack at ~105,000 stars vs this essay's 72,000+, confirming #2 sits earlier in the time-series.

**Ordering evidence**: (a) explicit back-reference to essay #1's "five definitions" ([[sources/garrytan--resolvers#intro]]); (b) the 72,000+ star reading is well below #8's ~105,000 ([[sources/garrytan--foxconn-factories#gstack-stars]]) and the live 105,768 (2026-06-01); (c) reference to Claude Code's AutoDream and to a *recent* YC office-hours conversation place it in the same ≈April–May 2026 window as the rest of the series.

## Contradictions & tensions (for LINT)

1. **OpenClaw / Hermes authorship.** This essay says *"OpenClaw or Hermes Agent is the conductor — the thin harness"* and "For my OpenClaw, we built a signature-tracking system" ([[sources/garrytan--resolvers#build-your-own-brain]], [[sources/garrytan--resolvers#invisible-skill]]), treating OpenClaw as *his*. Essay #8 explicitly attributes it: *"Peter Steinberger built OpenClaw, my favorite harness"* ([[sources/garrytan--foxconn-factories#openclaw]]). **Reconciliation (already flagged on [[creators/garry-tan]] and [[sources/garrytan--gbrain]])**: OpenClaw is Steinberger's harness; `garrytan/openclaw` is most likely Garry's fork/deployment, and gbrain/gstack are skills that *target* / plug into it. "my OpenClaw" reads as "my deployment of OpenClaw," consistent with the correction — do not silently overwrite.
2. **Internal file-count drift.** The essay quotes the knowledge base at "**14,700 files**" mid-narrative ([[sources/garrytan--resolvers#the-audit]]) and "**25,000 files**" in the close ([[sources/garrytan--resolvers#open-source-close]]). Likely growth over the period described (or rhetorical rounding), not a true contradiction, but flag if any wiki page cites a single canonical file count for Garry's brain.
3. **"72,000+ stars" vs the wiki's measured 105,768.** Not a contradiction — a **time-series** artifact. The wiki's [[sources/garrytan--gstack]] / [[sources/garrytan--foxconn-factories]] record the *current* ~105K; this essay records an *earlier* 72K. LINT should treat divergent star numbers across these essay pages as expected, **provided each carries its own as-of context** (this one is essay-internal, ≈April–May 2026).
4. **Tokenmaxxing vs. cost-rationing (series-level tension, carried over).** This essay's "don't drown the model… give it the right book at the right moment" frugality-with-*context* ([[sources/garrytan--resolvers#the-20000-line-confession]]) is about *attention budget*, not *token spend* — so it does not directly contradict essay #8's "tokenmaxxing" ([[sources/garrytan--foxconn-factories#tokenmaxxing]]) or gbrain's cost-rationing banner ([[sources/garrytan--gbrain#AGENTS.md]]), but all three live on the same "how much to spend / load" axis. Tracked as an open question for a future analysis; noted here so LINT links the three.
5. **Essay narrative vs. the snapshotted repo state (provenance, not contradiction).** The essay describes the *discovery* of the misfiling bug and the *before* state ("idea-ingest had hardcoded `brain/sources/` as the default… didn't consult the resolver"). The gbrain snapshot captures the *after* state: `skills/idea-ingest/SKILL.md` still lists `sources/` under `writes_to:` **but** now opens with the filing mandate *"Read `skills/_brain-filing-rules.md` before creating any new page"* and warns against "Filing everything in `sources/`" as an anti-pattern. So the snapshot is *evidence the fix landed*, not a counterexample. Note for LINT: do not read the lingering `sources/` entry as the bug — it's a sanctioned target, gated by the mandate.

## Related sources

**Sibling essays** — see Series context for the full ordered list:
- [[sources/garrytan--thin-harness-fat-skills]] (#1, parent) · [[sources/garrytan--loc-controversy]] (#3) · [[sources/garrytan--naked-models]] (#4) · [[sources/garrytan--skillify-manifesto]] (#5) · [[sources/garrytan--meta-meta-prompting]] (#6) · [[sources/garrytan--complexity-ratchet]] (#7) · [[sources/garrytan--foxconn-factories]] (#8, style template).

**The real artifacts this essay is *about* (grounding for every claim)**:
- [[sources/garrytan--gbrain]] — the memory system whose **actual** resolver machinery grounds this essay almost line-for-line:
  - The "200-line resolver" ↔ `skills/RESOLVER.md` (128 lines, the literal "dispatcher… Read before any task" table) — [[sources/garrytan--gbrain#skills-resolver]].
  - The shared filing-rules doc ↔ `skills/_brain-filing-rules.md` (192 lines), which states *"The PRIMARY SUBJECT… determines where it goes. Not the format, not the source, not the skill"* and tabulates the exact misfilings the essay names (incl. "Analysis of a topic → `sources/`" as **wrong**) — [[sources/garrytan--gbrain#skills-brain-filing-rules]].
  - The filing mandate ↔ `AGENTS.md` line 43 (*"`skills/RESOLVER.md` — skill dispatcher. Read before any task."*) and `skills/idea-ingest/SKILL.md`'s top-of-file *"Read `skills/_brain-filing-rules.md` before creating any new page"* — [[sources/garrytan--gbrain#AGENTS.md]], [[sources/garrytan--gbrain#skill-ingest]].
  - The "citation fixer that existed but wasn't reachable" ↔ the real `skills/citation-fixer/` skill, which ships its own `routing-eval.jsonl` — [[sources/garrytan--gbrain#skill-citation-fixer]].
  - The "trigger evals" ↔ **14+ real `routing-eval.jsonl` fixture files** across gbrain skills (citation-fixer, query, frontmatter-guard, book-mirror, …), each with `intent` → `expected_skill` cases **and** negative/`null` cases — i.e. the essay's false-negative/false-positive coverage, shipped.
  - The "resolvers are fractal / compress the resolver" thread ↔ the real `skills/functional-area-resolver/` skill (a dispatcher *inside* a skill), whose SKILL.md documents an **A/B Eval Results** section ("20 hand-authored training fixtures + 5 held-out blind fixtures, n=3 seeded; dispatcher pattern outperforms naive pipe-table compression") — [[sources/garrytan--gbrain#skill-functional-area-resolver]].
  - The "context resolver inside each skill" (executive-assistant routing email-triage vs scheduling vs signatures) ↔ the real `skills/cold-start/SKILL.md`'s "Email triage" sub-scoping and "executive-assistant pattern handles email triage."
- [[sources/garrytan--gstack]] — the coding layer ("72,000+ stars" here); its `scripts/resolvers/` preamble compiler plus resolver evals (`writing-style-resolver.test.ts`, `resolver-ask-user-format.test.ts`, `resolvers-gbrain-put-rewrite.test.ts`) ground the "test the routing" discipline on the gstack side — [[sources/garrytan--gstack#test]].

**Author**: [[creators/garry-tan]].

**Artifacts (wiki pages about the repos)**: [[artifacts/plugins/gstack]] · [[artifacts/plugins/gbrain]].

**Patterns this source grounds**: [[patterns/composition/resolver-routing-table]] (primary) · [[patterns/structural/thin-harness-fat-skills]] · [[patterns/quality-bar/skill-pack-bundle]] · [[patterns/behavioral/latent-vs-deterministic-split]] (the "load the right book" framing) · [[patterns/behavioral/skill-as-method-call]] (cross-referenced from essay #1).
