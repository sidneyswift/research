---
domain: sources
type: article
url: https://x.com/garrytan # profile; canonical post URL not yet confirmed — TODO
retrieved: 2026-06-01
snapshot-location: sources/garrytan--complexity-ratchet/snapshot.md
upstream-commit: n/a (essay, not a repo)
last-reviewed: 2026-06-01
---

# "The AI Agent Complexity Ratchet: Why 90% Test Coverage Is Required" (`garrytan`, essay)

> Garry Tan's argument that AI coding agents make 90% test coverage *free* for the first time, turning a codebase into a **complexity ratchet** — a forward-only mechanism where every agent session adds tests + docs + evals that load into the next session's context, so quality can only go up. Essay #7 of 8 in the "AI Explainer" series. Our primary source for the [[patterns/quality-bar/complexity-ratchet]] thesis and the "everything harnessable is testable" expansion of the test surface (TTY-level, OS-level, browser-level, behavioral-level), grounded in real gstack/gbrain test machinery.

## Snapshot details

- **Retrieved**: 2026-06-01 (pasted verbatim by Sidney; we hold the full text, author's typos preserved).
- **Where it lives in this wiki**: [`sources/garrytan--complexity-ratchet/snapshot.md`](garrytan--complexity-ratchet/snapshot.md) — verbatim, immutable.
- **Upstream URL**: not yet confirmed. Reads as an X long-form post / blog essay under [@garrytan](https://x.com/garrytan). **TODO**: locate canonical URL + add an archive.org link.
- **Publication date**: **2026-05-12** — strong internal evidence:
  - Explicit byline: **"Garry Tan · @garrytan · May 12"** (snapshot L12).
  - **"This is the seventh in a series"** (L22) — fixes series position at #7.
  - Star/scale figures consistent with the series' growth curve: gstack **"93,000 GitHub stars, 701,000 lines of code, 46 skills"** (L106), **37 contributors** (L160); gbrain **"14K stars"** (L191), **25 contributors** (L160). These sit *between* essay #6's numbers and essay #8's ~105K/20K, fixing the order (see [Series context](#series-context-7-of-8)).
  - Combined-scale framing: **"about 970,000 lines of code and 665 test files"** (L14); a week of **14 PRs / 72 hours / ~29,000 lines** (L16). Year-stamp "I've been coding with AI for the past year" (L14) is consistent with a 2026 dateline.

## Anchor map

Every claim citing this source uses a `#anchor` from this list. The essay is one prose file; anchors are thematic pointers into the author's own sections (the essay's section headers make excellent, stable anchors). **Do not invent new anchors** — extend this list if a future citation needs one.

- `#root` — the essay as a whole
- `#thesis-ratchet-free` — the core claim: speed/quality no longer trade off because **AI made 90% coverage free**; the result is "the complexity ratchet: a system that can only get better, never worse" (L20)
- `#brittle-software` — "Software used to be brittle": 50 years of engineering organized around *preventing* errors because errors were catastrophic; complexity ceiling = what one team can hold in their heads (L24-30)
- `#squishy-software` — "Now software is squishy" (resilient, not sloppy): agents read/understand/diagnose/fix, so the *error model* changed — most errors are now the fixable kind; only state-destroying errors stay catastrophic (L32-42)
- `#ratchet-three-things` — the mechanism: every session adds **(1) tests that encode "correct", (2) documentation of why, (3) evaluation results that set quality thresholds**; the next agent loads all three into context, so it can't regress (L44-56). The definitional anchor for [[patterns/quality-bar/complexity-ratchet]].
- `#gbrain-extraction-ratchet` — the worked example: gbrain's epistemological extraction pulled **100,720 claims** across **28,000 pages**, scored **6.8/10** by a GPT-5.5 + Claude cross-model eval; **holder confusion** wrong 35% of the time in v1; v2 fixed 6 failure modes, enforced weight-rounding at the DB layer, locked **17 tests** (L58-72)
- `#holder-confusion` — the specific failure mode: *who* holds a belief (author / person quoted / the system's inference engine) — "if you're building a system that tracks what people believe, you need to know WHO believes it" (L62-70)
- `#vibecoding-death` — "Why most vibecoded projects die": Karpathy's term defined; projects that **skip the ratchet** (no tests/docs/evals) become "a haunted house where every change breaks something" by v0.5 — "AI coding works fine. They just didn't build the ratchet." (L74-84)
- `#ratchet-not-the-person` — the rebuttal to "good engineers write tests anyway": the ratchet "isn't about the person — it's about what happens on the next turn"; it "works even when the human isn't at their best" (new contributor / model-version change / coding at 2am) (L82)
- `#tests-as-institutional-memory` — tests/docs survive employee turnover; "// DO NOT CHANGE THIS -- ask Dave" and Dave left three years ago; "The agent's context window doesn't quit." For a one-person project, tests are "the only institutional memory you have." (L86-94)
- `#everything-harnessable-testable` — the surface-area expansion: OS (process trees, fs, sockets, cron), terminal (keystrokes/output), browser (rendered pages, button states), APIs (schemas), AI agents (observable behavior). **"If you can harness it… observe it… assert on it… you can ratchet it."** (L96-104). Grounds the [[patterns/behavioral/latent-vs-deterministic-split]] "deterministic side is testable" corollary.
- `#tty-interactive-review-test` — gstack's interactive plan-review contract tested at the **TTY level**: a Bun-TTY harness (**PR #1354**) spawns Claude Code in a pseudo-terminal and fails if the agent dumps findings without firing an interactive question. The ratchet response = **STOP gates + anti-rationalization clauses + an anti-shortcut clause ("the plan file is the OUTPUT of the interactive review, not a substitute for it") + gate-tier floor tests** (L106-123). Grounds [[patterns/composition/resolver-routing-table]]'s "trigger evals" sibling and the gstack `#test` harness.
- `#openclaw-plugin-test` — gstack's end-to-end OpenClaw plugin test (**PR #880**): builds the plugin, spawns a real OpenClaw instance in an isolated profile, installs via CLI, runs `plugins inspect` / sets config / validates / `plugins doctor` for zero diagnostics — **359 lines** Claude wrote "in about five minutes." "The effort wall disappearing in real time." (L124)
- `#90pct-coverage-data` — the empirical case: Capers Jones (>10,000 projects) — DRE jumps from ~65-75% (below 70% coverage) to **92-97%** (85-95% coverage), a *knee* near 85%; DO-178C / MC/DC for avionics → >99% DRE; Six Sigma 3σ→4σ→5σ as phase changes; **"Going from 70% to 90% coverage isn't 30% better. It's an order of magnitude fewer escapes."** (L130-152)
- `#effort-wall-gone` — the unlock: Mockus/Nagappan/Dinh-Trong (Windows Vista) — the last 20% of coverage costs disproportionately more, which is why human teams stopped at 70-80%; **"AI coding agents don't experience effort"** ("the fourteenth edge-case test… at 2am, without complaining"). "It's not that AI lets you write code faster… AI lets you verify at a level that was previously too expensive to sustain." (L142-154)
- `#coverage-as-contract-proxy` — the reframe: line coverage is **not a vanity metric** but a *proxy* for "how much of the system's behavior is under contract"; at 90% nearly every behavior change trips a test signal; the remaining 10% (integration / infra / genuinely-hard) is fine (L150-152). The clearest statement that the ratchet is about **behavioral contracts** (holder-confusion test, weight-rounding test, interactive-review gate), not coverage-for-its-own-sake.
- `#proof-of-concept-contributors` — the social proof: gstack **37 contributors**, v1.30 incorporated **21 community PRs** in one release; gbrain **25 contributors**, v0.31.1.1 landed **22 community fixes** in one PR. "A new contributor doesn't need to understand the whole system. They need to make the tests pass." (L156-171)
- `#gbrain-release-log` — the week's gbrain releases as ratchet evidence: v0.31.0 (facts table + dream-consolidation phase), v0.31.1 (fixed 25 CLI commands routing to an empty local DB), v0.31.1.1 (22 community fixes), v0.31.2 (30-second timeout for sync hanging on symlinks) — "Each release shipped with more tests than the last." (L164-171)
- `#new-complexity-ceiling` — the close: the complexity ceiling is no longer "one team's ability to hold the system in their heads" but "one person plus agents who can load the full codebase, schema history, test suite, and documentation into context… a much bigger number" that grows with context windows; **"90% coverage, every PR, no exceptions."** (L173-187)
- `#projects-and-stars` — the byline scale claims + sign-off: two MIT projects — **GStack "93K stars"** ("makes Claude Code dramatically better"), **GBrain "14K stars"** ("your second brain for AI agents") — and the closing series index (L14, L188-200) (author self-claim)
- `#series-index` — the explicit 7-essay backref list and the closing 7-title index naming all siblings (L22, L193-200)
- `#conductor-sessions` — production-method detail: "(15 simultaneous Conductor sessions most of the time)" + "Claude Code and Codex at my direction" (L14) — grounds the [[patterns/structural/thin-harness-fat-skills]] "harness-agnostic" claim (multiple harnesses, one skill layer)

## Why we cite this

- **The richest articulation of the [[patterns/quality-bar/complexity-ratchet]] pattern** we have — the author defining the exact three-part mechanism (tests + docs + evals, all reloaded into the next session's context) and the "forward-only motion" property ([[#ratchet-three-things]], [[#thesis-ratchet-free]]). This is the *behavioral* "why" behind [[patterns/quality-bar/skill-pack-bundle]]'s tested-bundle structure.
- **"Everything harnessable is testable"** — the strongest case in the series that the test surface is *much* larger than unit tests: TTY-level, OS-level, browser-level, behavioral-level ([[#everything-harnessable-testable]]). Directly supports the [[patterns/behavioral/latent-vs-deterministic-split]] corollary that the deterministic side is exactly what you assert on, and gives [[patterns/composition/resolver-routing-table]] its "trigger eval / floor test" vocabulary.
- **Coverage-as-behavioral-contract** ([[#coverage-as-contract-proxy]]) — the clearest defense against the obvious "coverage is a vanity metric" objection: each test "locks in a specific lesson learned." Useful framing for [[patterns/quality-bar/skill-pack-bundle]].
- **Two concrete, verifiable gstack test artifacts** — the Bun-TTY interactive-review harness ([[#tty-interactive-review-test]], PR #1354) and the end-to-end OpenClaw plugin test ([[#openclaw-plugin-test]], PR #880). Both map onto real files in [[sources/garrytan--gstack]] (see Related sources for the grounding).
- **A gbrain eval worked-example** ([[#gbrain-extraction-ratchet]]) — holder confusion + weight rounding + 17 locked tests — grounds the [[patterns/behavioral/diarization]] "says vs. believes / who holds the belief" distinction with a real failure mode and fix.
- **Fresh longitudinal popularity signals** — gstack 93K / gbrain 14K *at the May-12 point of the series' growth curve* (see below).
- **A "tests are institutional memory" framing** ([[#tests-as-institutional-memory]]) that reframes the whole skill-pack-bundle pattern as durable knowledge transfer, not just regression safety.

## Popularity signals (this source IS one)

This essay is itself a **"talked-about / named-person-quoted"** signal (a YC CEO's manifesto, essay #7 of a widely-read series). It also carries hard metrics. **These 8 essays form a longitudinal time-series of gstack/gbrain growth** — capture each precisely with its as-of and mark author self-claims as such.

- **Signal type**: github-stars + LOC + contributors + skill-count — **all author self-claims**, captured as a dated point on the series curve.
- **As-of (claim)**: **2026-05-12** (essay byline; see Snapshot details).

| Metric | Value (this essay) | As-of | Note |
|---|---|---|---|
| gstack GitHub stars | **93,000** ([[#projects-and-stars]], [[#everything-harnessable-testable]]) | 2026-05-12 | author self-claim. Series curve: **72K → 75K → 87K → 93K → 105K** across essays; this is the 4th point. |
| gstack lines of code | **701,000** ([[#everything-harnessable-testable]]) | 2026-05-12 | author self-claim |
| gstack skills | **46** ([[#everything-harnessable-testable]]) | 2026-05-12 | author self-claim (the [[sources/garrytan--gstack]] snapshot one-liner says "23+ skills + 8 tools"; the 46 figure is later/broader — likely counts sub-skills) |
| gstack contributors | **37** ([[#proof-of-concept-contributors]]) | 2026-05-12 | author self-claim |
| gstack v1.30 community PRs | **21 in one release** ([[#proof-of-concept-contributors]]) | 2026-05-12 | author self-claim |
| gbrain GitHub stars | **14,000** ("14K") ([[#projects-and-stars]]) | 2026-05-12 | author self-claim. Series curve: **14K → 20K**; this is the early point. (Independently measured **20,403** as-of 2026-06-01 — see [[sources/garrytan--gstack#popularity-signals]].) |
| gbrain contributors | **25** ([[#proof-of-concept-contributors]]) | 2026-05-12 | author self-claim |
| gbrain v0.31.1.1 community fixes | **22 in one PR** ([[#proof-of-concept-contributors]], [[#gbrain-release-log]]) | 2026-05-12 | author self-claim |
| combined lines of code | **~970,000** ([[#root]]) | 2026-05-12 | author self-claim (gstack + gbrain) |
| combined test files | **665** ([[#root]]) | 2026-05-12 | author self-claim |
| week's throughput | **14 PRs / 72 hours / ~29,000 LOC** ([[#root]]) | 2026-05-12 | author self-claim |
| gbrain extraction run | **100,720 claims** across **28,000 pages**, eval **6.8/10** ([[#gbrain-extraction-ratchet]]) | 2026-05-12 | author self-claim (cross-model: GPT-5.5 + Claude) |
| holder-confusion error rate (v1) | **35%** ([[#holder-confusion]]) | 2026-05-12 | author self-claim |
| locked tests for extraction contract | **17** ([[#gbrain-extraction-ratchet]]) | 2026-05-12 | author self-claim |
| OpenClaw plugin test size | **359 lines** ([[#openclaw-plugin-test]]) | 2026-05-12 | author self-claim (PR #880) |
| production method | **15 simultaneous Conductor sessions** ([[#conductor-sessions]]) | 2026-05-12 | author self-claim |

External-research figures the essay *cites* (not Garry's own metrics, but recorded for traceability): Capers Jones **>10,000 projects**, DRE **65-75% → 92-97%** across the 85% knee; Six Sigma **3σ ≈ 67,000 dpm → 4σ ≈ 6,200 → 5σ ≈ 233**; avionics MC/DC **>99% DRE**; branch coverage alone **misses 10-20% of faults** ([[#90pct-coverage-data]], [[#effort-wall-gone]]). Treat these as the essay's citations of third-party literature, not as wiki-verified facts.

## Series context (#7 of 8)

This is **essay #7 of the 8-part "AI Explainer" series**. The essay opens with an explicit backref — *"This is the seventh in a series about building with AI: 1 2 3 4 5 6"* ([[#series-index]]) — and closes with a titled index naming every sibling (L193-200):

1. [[sources/garrytan--thin-harness-fat-skills]] — "Fat Skills, Fat Code, Thin Harness — the architecture"
2. [[sources/garrytan--resolvers]] — "Resolvers — the routing table for intelligence"
3. [[sources/garrytan--loc-controversy]] — "The LOC Controversy — what 600K lines actually produced"
4. [[sources/garrytan--naked-models]] — "Naked Models Are Stupider — the model is the engine, not the car"
5. [[sources/garrytan--skillify-manifesto]] — "The Skillify Manifesto — every workflow becomes a testable skill"
6. [[sources/garrytan--meta-meta-prompting]] — "Meta-Meta-Prompting — compounding skills produce emergent capabilities"
7. [[sources/garrytan--complexity-ratchet]] — **"The Agent Complexity Ratchet — you are here"** (this page)
8. [[sources/garrytan--foxconn-factories]] — "Stop building Foxconn factories for your agents" (already ingested)

**Ordering evidence** is unusually strong for this essay: the literal "seventh in a series" statement, the May-12 byline, and the star-count position on the series curve (gstack 93K sits between #3/#4's 87K-ish and #8's ~105K; gbrain 14K precedes #8's measured ~20K). The closing index also matches the canonical slug list exactly. This essay is the **most test-focused** installment — it operationalizes the [[patterns/quality-bar/skill-pack-bundle]] "tested bundle" requirement (introduced in #5, the Skillify Manifesto) into a *why* (the ratchet) and a *number* (90%).

## Contradictions & tensions (for LINT)

1. **OpenClaw authorship (cross-essay).** This essay treats OpenClaw as a first-class harness gstack tests against ([[#openclaw-plugin-test]]: "spawns a real OpenClaw instance… installs the plugin via the CLI… `plugins doctor`") without attributing it. Essay #8 explicitly attributes it: *"Peter Steinberger built OpenClaw, my favorite harness"* ([[sources/garrytan--foxconn-factories#openclaw]]). The wiki elsewhere implies `garrytan/openclaw` is Garry's ([[creators/garry-tan]], [[sources/garrytan--gbrain]]). **Reconciliation already tracked** on the foxconn page: OpenClaw is Steinberger's; `garrytan/openclaw` is most likely Garry's fork/deployment. No new contradiction — this essay just *uses* OpenClaw without re-attributing.
2. **Tokenmaxxing vs. cost-rationing (latent).** This essay's whole thesis is "spend agent effort freely — verification is now free" ([[#effort-wall-gone]]: agents "don't get bored… at 2am, without complaining"), echoing essay #8's tokenmaxxing ([[sources/garrytan--foxconn-factories#tokenmaxxing]]). That sits against gbrain's own `[AGENT]`-marked cost banner forcing an operator to confront a 25× cost spread before proceeding ([[sources/garrytan--gbrain#AGENTS.md]]). The reconciliation is the same as the one tracked on the foxconn page (don't *architecturally* ration intelligence vs. do give the operator an informed choice). Worth a future analysis; not a hard contradiction.
3. **"Tests-everywhere" vs. essay #8's self-audit framing.** Essay #8's "Foxconn factory" self-audit reports gbrain at **~262K app LOC + ~276K test LOC** ([[sources/garrytan--foxconn-factories#factory-audit]]) — i.e. *more test code than app code* — which this essay celebrates as the ratchet working ([[#proof-of-concept-contributors]], [[#gbrain-release-log]]). But #8 uses "Foxconn factory" pejoratively for "code written to police a capable model." **Tension to flag**: is a 276K-line test corpus a *ratchet* (this essay's framing) or a *Foxconn factory* (#8's framing)? Likely reconciled by #8's own carve-out — tests that encode *behavioral contracts* are the good kind, generic distrust-the-model scaffolding is the bad kind ([[#coverage-as-contract-proxy]] makes exactly this distinction) — but the two essays use the same large test number with opposite valence. Candidate for human review / a synthesis note.
4. **Coverage as a number vs. coverage as a contract (intra-essay, by design).** The title says "**90% Test Coverage Is Required**" (a number) but the body insists coverage is "the proxy… not… a vanity metric" ([[#coverage-as-contract-proxy]]). Not a real contradiction — the essay resolves it itself — but worth noting so a future citation doesn't quote the 90% headline without the contract caveat.

## Related sources

- [[sources/garrytan--gstack]] — the artifact two of this essay's examples are *about*. **Real grounding verified at 2026-06-01:**
  - [[#tty-interactive-review-test]] (PR #1354) → the TTY mechanism is real: `extension/` uses `gstackInjectToTerminal` / `gstackScanForPTYInject` (PTY injection), enforced by `test/extension-pty-inject-invariant.test.ts`; the "interactive-question floor" is realized as `test/skill-e2e-plan-{ceo,eng,design,devex}-finding-floor.test.ts`; STOP-gate / anti-rationalization language lives in `plan-eng-review/SKILL.md`, `plan-ceo-review/SKILL.md`, `plan-design-review/SKILL.md` ([[sources/garrytan--gstack#test]], [[sources/garrytan--gstack#plan-eng-review]]).
  - [[#everything-harnessable-testable]] → the multi-tier harness (`skill-validation` Tier-1, `skill-llm-eval` Tier-3, `skill-e2e-*` Tier-2) and `scripts/resolvers/` + resolver evals (`resolver-ask-user-format.test.ts`, `writing-style-resolver.test.ts`) are exactly the layered test surface the essay describes ([[sources/garrytan--gstack#test]]).
  - [[#openclaw-plugin-test]] (PR #880) → OpenClaw references exist throughout the repo (`README.md`, `BROWSER.md`, `setup/`); the `plugins inspect` / `plugins doctor` round-trip is the kind of E2E the `skill-e2e-*` tier runs.
- [[sources/garrytan--gbrain]] — the other example subject. **Real grounding verified:** [[#gbrain-extraction-ratchet]] / [[#holder-confusion]] / weight-rounding → `docs/takes-vs-facts.md`, `docs/contradictions.md`, `skills/conventions/calibration.md`, `skills/_brain-filing-rules.md`, and cross-model judging in `src/core/eval-contradictions/judge.ts`; [[#gbrain-release-log]] v0.31.0 facts table + dream consolidation → `test/migration-orchestrator-v0_31_0.test.ts`, `test/insert-facts-batch.test.ts` ([[sources/garrytan--gbrain#docs-takes-vs-facts]], [[sources/garrytan--gbrain#evals]]).
- [[artifacts/plugins/gstack]] / [[artifacts/plugins/gbrain]] — the artifact pages this essay's claims feed.
- [[creators/garry-tan]] — author.
- **Sibling essays**: [[sources/garrytan--thin-harness-fat-skills]] · [[sources/garrytan--resolvers]] · [[sources/garrytan--loc-controversy]] · [[sources/garrytan--naked-models]] · [[sources/garrytan--skillify-manifesto]] · [[sources/garrytan--meta-meta-prompting]] · [[sources/garrytan--foxconn-factories]] (#8, the style template for this page).
