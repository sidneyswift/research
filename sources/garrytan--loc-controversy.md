---
domain: sources
type: article
url: https://x.com/garrytan # profile; canonical post URL not yet confirmed — TODO
retrieved: 2026-06-01
snapshot-location: sources/garrytan--loc-controversy/snapshot.md
upstream-commit: n/a (essay, not a repo)
last-reviewed: 2026-06-01
---

# "On the LOC controversy" (`garrytan`, essay)

> Garry Tan's data-driven rebuttal to the "600K lines is just AI slop" pile-on: he concedes LOC is a garbage metric, then runs the deflation math anyway — `garry-output-comparison.ts` across all 41 `garrytan/*` repos — to land on **11,417 logical lines/day** (5,708 after a 2× AI-verbosity haircut), an **~408×** jump over his 2013 part-time baseline. Our primary source for Garry's articulation that **multi-level testing is the unlock that makes AI-assisted coding work** ("without those layers you're just generating confident garbage at high speed"), and a fresh longitudinal popularity snapshot for GStack (75K stars / 14,965 installs / 305,309 invocations).

## Snapshot details

- **Retrieved**: 2026-06-01 (pasted verbatim by Sidney; we hold the full text, author's typos and smart-quotes preserved).
- **Where it lives in this wiki**: [`sources/garrytan--loc-controversy/snapshot.md`](garrytan--loc-controversy/snapshot.md) — verbatim, immutable.
- **Upstream URL**: not yet confirmed. Reads as an X long-form post / blog essay under [@garrytan](https://x.com/garrytan). **TODO**: locate canonical URL + publication date and add an archive.org link.
- **Publication date**: **≈2026-04-18**, with strong internal evidence — the essay states *"2026 is day 108 as of this writing (April 18)"* ([[sources/garrytan--loc-controversy#the-math]]). Day-108 of 2026 is indeed April 18, so the date is self-consistent. Corroborating: GStack is cited at **75,000+ stars in 5 weeks** and **14,965 installs** here, vs. ~105K stars in essay #8 ([[sources/garrytan--foxconn-factories#gstack-stars]], ≈2026-05-23) and 105,761 measured on 2026-06-01 — the lower star count places this essay **earlier in the series' timeline**, consistent with mid-April.
- **Cross-grounding (notable)**: a markdown copy of this same essay ships **inside the artifact it is about** at `sources/garrytan--gstack/docs/ON_THE_LOC_CONTROVERSY.md` (169 lines; our pasted snapshot is 162). The in-repo copy adds one detail our snapshot omits — `tax-app` is excluded via an `EXCLUDED_REPOS` constant in the script. We cite our pasted `snapshot.md` as canonical; the in-repo copy is corroborating evidence the essay is a real Tan document, not a reconstruction.

## Anchor map

Every claim citing this source uses a `#anchor` from this list. The essay is one prose file; anchors are thematic pointers into the author's own section headers (which make excellent, stable anchors).

- `#root` — the essay as a whole
- `#loc-is-garbage` — the concession up front: "The critique is right. LOC is a garbage metric." Dijkstra EWD1036 ("lines spent," 1988) + the Gates-attributed "measuring aircraft progress by weight" line; "true for 40 years and still true"
- `#the-replies` — the seven verbatim pile-on replies ("That's just AI slop." / "More lines is bad, not good." / "Where are your error rates? Your DAUs? Your revert counts?" / "This is embarrassing.")
- `#three-branches` — the critique split into three distinct arguments: (1) LOC ≠ quality [true, always], (2) AI inflates LOC [true, verbose by default], (3) therefore bragging is embarrassing ["where the argument jumps the track"]. "Branch 2 is the interesting one… compute the deflation and report the deflated number"
- `#the-math` — `scripts/garry-output-comparison.ts` enumerates every commit across all 41 `garrytan/*` repos (15 public, 26 private) for 2013 vs 2026; counts logical (non-blank, non-comment) lines added; 2013 corpus includes Bookface; "2026 is day 108 as of this writing (April 18)"; 2013 baseline = 14 logical lines/day part-time
- `#historical-baselines` — the literature band for full-time output: Brooks ~10/day (OS/360), Capers Jones ~16–38, McConnell's *Code Complete* 1.5–125 depending on project size ("size-dependent, not a single number"); "My 2013 baseline isn't cherry-picked"
- `#two-deflations` — deflation #1 = logical SLOC (cloc/scc, 20-year-old tooling); deflation #2 = assume AI code is **2× more verbose** than senior hand-crafted at the logical level ("aggressive — most measurements put it at 1.3–1.8× — but the upper bound a skeptic would demand"); NCLOC 11,417/day → 5,708/day deflated → **408×** multiple; sensitivity table (5×→162×, 10×→81×, 100×→8×): "The number is large regardless"
- `#weekly-distribution` — rebuts "show the distribution / if it's a single burst your run-rate is bogus": "It's not a spike. The rate has been approximately consistent and slightly increasing. Run the script yourself."
- `#quality-question` — the Cramer/Sentry-voiced challenge ("Where are your error rates? Post-merge reverts? Bug density? If you're typing at 10× speed but shipping 20× more bugs, you're not leveraged, you're making noise at scale") and the data answer below
- `#reverts-and-fixes` — **revert rate 2.0%** (7 reverts / 351 commits across 15 active repos; "mature OSS typically 1–3%"); **post-merge fix rate 6.3%** (22/351 `^fix:`; "a zero-fix rate would mean I'm not catching my own mistakes")
- `#testing-is-the-unlock` — the load-bearing thesis: tests went from ~100 (January) to **2,000+**, run in CI; "testing at multiple levels is what makes AI-assisted coding actually work. Unit tests, E2E tests, LLM-as-judge evals, smoke tests, slop scans. Without those layers, you're just generating confident garbage at high speed. With them, you have a verification loop that lets the AI iterate until the code is actually correct." "Every gstack PR has a coverage audit in the PR body"
- `#qa-browser-cli` — GStack's "core real-code feature — the thing that isn't just markdown prompts" is a Playwright-based CLI browser; `/qa` opens a real browser, navigates a staging URL, runs automated checks; "2,000+ lines of real systems code (server, CDP inspector, snapshot engine, content security, cookie management) that exists because testing is the unlock, not the overhead"
- `#gbrowser-pair-agent` — the GBrowser preview (Claude Code in a browser sidebar; "compiled Chromium, all 60 GB of it," Comet/Atlas-style; simplified version already in GStack via `/open-gstack-browser`); `/pair-agent` (MCP bearer token + ngrok/tailscale tunnel so a remote OpenClaw can drive the real desktop Chromium); promise of a Claude Code skill to "let YOU compile Chromium like I did"
- `#slop-scan` — Ben Vinegar (founding engineer at Sentry) built `slop-scan` (deterministic rules calibrated against mature OSS baselines, higher = more slop); ran it on gstack, scored **5.24** ("the worst he'd measured at the time"); Garry "cut the score by 62% in one session"; "Run `bun test` and watch 2,000+ tests pass"
- `#review-rigor` — every gstack branch goes through CEO review + Codex outside-voice review + DX review + eng review, "often 2–3 passes of each"; the `/plan-tune` skill had a scope **ROLLBACK** from the CEO expansion plan because Codex's outside-voice review surfaced **15+ findings the four Claude reviews missed**; "The review infrastructure catches the slop. It's visible in the repo."
- `#what-ill-concede` — five steelman concessions: greenfield-dominated (not legacy-maintenance proof); 2013 survivorship bias (true rate maybe 50/day → 228× not 810×); quality-adjusted productivity is "evidence, not proof"; "shipped" means different things across eras (if 80% is dead in two years, "you built unused stuff" gets teeth); **"Time to first user is the metric that matters, not LOC"** — the 60-day "I wish this existed" → "someone is using it" cycle is the real shift
- `#what-lines-became` — the GStack usage dump: 75,000+ stars in 5 weeks; 14,965 unique installs (opt-in telemetry, "real number at least 2× higher"); 305,309 skill invocations since Jan 2026; ~7,000 WAU at peak; 95.2% success (290,624 / 305,309); per-skill counts (57,650 `/qa`, 28,014 `/plan-eng-review`, 24,817 `/office-hours`, 18,899 `/ship`); 27,157 browser sessions; median session 2 min / avg 6.4 min
- `#engineers-can-fly` — the close: "One engineer in 2026 has the output of a 100 person team in 2013… the code-generation cost curve collapsed by two orders of magnitude"; "The delta isn't that I became a better programmer. If anything, my mental model of coding has atrophied"; the gap from "I want this tool" to "this tool exists and I'm using it" collapsed "from 3 weeks to 3 hours"; "you can fly too"

## Why we cite this

- **The strongest first-person statement in the series of the testing/verification-loop thesis.** "Testing at multiple levels is what makes AI-assisted coding actually work… without those layers, you're just generating confident garbage at high speed" ([[sources/garrytan--loc-controversy#testing-is-the-unlock]]) is the *rationale* under [[patterns/quality-bar/skill-pack-bundle]] (why a skill ships as a tested bundle) and the affordability claim under [[patterns/quality-bar/complexity-ratchet]] (tests went 100→2,000+; "every gstack PR has a coverage audit in the PR body" = the ratchet, forward-only).
- **Concrete proof that the harness is thin and the real code is deterministic, narrow systems code.** The essay names the *one* large code artifact in gstack — a Playwright browser CLI — as the exception that proves the rule ([[sources/garrytan--loc-controversy#qa-browser-cli]]). This is the cleanest external statement of [[patterns/structural/thin-harness-fat-skills]] (intelligence up in markdown, execution down in deterministic code) and [[patterns/behavioral/latent-vs-deterministic-split]] (the browser CLI is the *deterministic* side; the skills are *latent*).
- **An adversarial-review / outside-voice datapoint.** The `/plan-tune` rollback driven by Codex finding 15+ issues four Claude passes missed ([[sources/garrytan--loc-controversy#review-rigor]]) grounds the "multiple reviewers / outside voice" facet of [[patterns/quality-bar/skill-pack-bundle]] and the review side of [[patterns/quality-bar/complexity-ratchet]].
- **A third-party quality measurement.** Ben Vinegar's `slop-scan` score (5.24, cut 62% in one session) ([[sources/garrytan--loc-controversy#slop-scan]]) is rare *external* evidence about a Garry Tan artifact, and a real tool wired into gstack's `review`/`ship` skills (see grounding below).
- **A longitudinal popularity snapshot** for GStack at an earlier point on the series' timeline (75K stars / 14,965 installs / 305,309 invocations / 95.2% success) — see the time-series note in Popularity signals.
- **A useful counter-weight to the rest of the series.** The essay's own punchline — *"Time to first user is the metric that matters, not LOC"* ([[sources/garrytan--loc-controversy#what-ill-concede]]) — partially undercuts the headline number it spends 600 words defending, and is worth quoting whenever the wiki risks over-citing LOC as a success signal.

## Popularity signals (this source IS one)

This is a "talked-about / named-person-quoted" signal in its own right (a YC CEO publicly defending his output against a pile-on, quoting Sentry's David Cramer and Ben Vinegar), **and** it is a dense bundle of hard metrics. The eight essays form a **longitudinal time-series** of GStack/GBrain growth; capture this essay's numbers precisely and treat the GStack figures as an **earlier** waypoint than essay #8.

GStack metrics (all **author self-claim**, as-of essay date **≈2026-04-18**):

- **GitHub stars** — **75,000+ in 5 weeks** (author self-claim). *Time-series context*: 75K here (#3, ~Apr 18) → ~105K in essay #8 ([[sources/garrytan--foxconn-factories#gstack-stars]], ~May 23) → **105,761 measured** via `gh api repos/garrytan/gstack` on 2026-06-01. The lower count here corroborates the earlier publication date. ([[sources/garrytan--loc-controversy#what-lines-became]])
- **Unique installations** — **14,965** (opt-in telemetry; author notes "real number at least 2× higher") (author self-claim).
- **Skill invocations** — **305,309** recorded since January 2026 (author self-claim).
- **Weekly active users** — **~7,000 at peak** (author self-claim).
- **Success rate** — **95.2%** across all skill runs (**290,624 successes / 305,309 total**) (author self-claim).
- **Per-skill usage** — **57,650** `/qa`; **28,014** `/plan-eng-review`; **24,817** `/office-hours`; **18,899** `/ship` (author self-claim).
- **Browser sessions** — **27,157** used the (real Playwright) browser (author self-claim).
- **Session length** — median **2 min**, average **6.4 min** (author self-claim).
- *Note*: the essay includes a "Top skills by usage" header with no list under it (a snapshot gap / truncation, not data we can cite) ([[sources/garrytan--loc-controversy#what-lines-became]]).

Output / productivity metrics (author self-claim, his own repos):

- **600,000 lines** of production code shipped in the **last 60 days** ([[sources/garrytan--loc-controversy#root]]).
- **11,417 logical (NCLOC) lines/day** in 2026; **5,708/day** after a 2× AI-verbosity deflation ([[sources/garrytan--loc-controversy#two-deflations]]).
- **2013 baseline: 14 logical lines/day** (part-time, while a YC partner + Posterous cofounder) ([[sources/garrytan--loc-controversy#the-math]]).
- **Multiple: 408×** at NCLOC+2× deflation; **810×** undeflated vs 14/day; **228×** if the true 2013 rate were 50/day ([[sources/garrytan--loc-controversy#two-deflations]], [[sources/garrytan--loc-controversy#what-ill-concede]]).
- **41 repos** total analyzed (15 public, 26 private) ([[sources/garrytan--loc-controversy#the-math]]).

Quality metrics (author self-claim, his own repos):

- **Revert rate 2.0%** (7 / 351 commits, 15 active repos) ([[sources/garrytan--loc-controversy#reverts-and-fixes]]).
- **Post-merge fix rate 6.3%** (22 / 351 `^fix:` commits) ([[sources/garrytan--loc-controversy#reverts-and-fixes]]).
- **Tests: ~100 (January) → 2,000+** now, in CI ([[sources/garrytan--loc-controversy#testing-is-the-unlock]]).
- **slop-scan score 5.24**, then **cut 62% in one session** (third-party tool, Ben Vinegar) ([[sources/garrytan--loc-controversy#slop-scan]]).
- **`/plan-tune` review: 15+ findings** surfaced by Codex outside-voice that four Claude passes missed ([[sources/garrytan--loc-controversy#review-rigor]]).
- **`/qa` browser CLI: "2,000+ lines of real systems code"** (author self-claim — and *understated*: the gstack snapshot's `browse/src` measures **22,009 lines**; see grounding note below) ([[sources/garrytan--loc-controversy#qa-browser-cli]]).

## Series context

This is **essay #3 of 8** in Garry Tan's "AI Explainer" series. Siblings, by canonical slug:

1. [[sources/garrytan--thin-harness-fat-skills]] — #1
2. [[sources/garrytan--resolvers]] — #2
3. **[[sources/garrytan--loc-controversy]]** — #3 *(this page)*
4. [[sources/garrytan--naked-models]] — #4
5. [[sources/garrytan--skillify-manifesto]] — #5
6. [[sources/garrytan--meta-meta-prompting]] — #6
7. [[sources/garrytan--complexity-ratchet]] — #7
8. [[sources/garrytan--foxconn-factories]] — #8 (already ingested; this page follows its house style)

**Ordering evidence.** The GStack star count is a reliable monotonic clock across the series: **75,000+** here (#3) climbs to **~105,000** by #8 ([[sources/garrytan--foxconn-factories#gstack-stars]]). Combined with the explicit internal date ("day 108 … April 18"), #3 sits firmly **earlier** than #8 (whose hackathon dates to ≈May 23). The install figure tells the same story: **14,965** here vs the larger numbers cited later in the series. This essay is also self-aware of being one entry in a larger argument — it repeatedly defers detail ("Run the script yourself," "Someone else will have to run their own script on a different context"), the posture of a series rather than a standalone post.

## Contradictions & tensions (for LINT)

1. **LOC defended vs LOC disowned — within the same essay.** Garry spends the piece computing and defending a deflated LOC number, then concedes *"Time to first user is the metric that matters, not LOC … LOC is downstream evidence"* ([[sources/garrytan--loc-controversy#what-ill-concede]]). Not a true contradiction (his claim is about *rate of change*, not LOC-as-goal), but any wiki page tempted to cite "11,417 lines/day" as a quality signal must carry this caveat. Tracked as a framing tension.
2. **"My mental model of coding has atrophied" vs the series' craftsmanship thesis.** Here Garry says the delta is *not* that he became a better programmer — *"If anything, my mental model of coding has atrophied"* ([[sources/garrytan--loc-controversy#engineers-can-fly]]). Essay #8 closes on the opposite-sounding note: *"the scarce resource becomes clarity, taste, and judgment. The engineer who writes the least code is often the one building the most"* ([[sources/garrytan--foxconn-factories#clarity-taste-judgment]]). Reconcilable (low-level syntax recall atrophies; high-level taste/judgment is what's scarce and rising) but worth a note for any "does AI deskill engineers?" analysis.
3. **`/qa` "2,000+ lines" undercounts the real artifact.** The essay says the browser CLI is "2,000+ lines of real systems code" ([[sources/garrytan--loc-controversy#qa-browser-cli]]); the gstack snapshot's `browse/src` alone is **22,009 lines** (`find … -name '*.ts' | wc -l`, as-of the 2026-05-20 snapshot). Either the essay refers to an earlier/narrower slice or simply rounds way down. Not a credibility problem — the self-claim is *understated* — but flag if a future page quotes "2,000 lines" as the size of gstack's browser.
4. **Pro-test stance here vs the "Foxconn factory" 276K-test self-audit in #8.** This essay celebrates tests as the unlock ([[sources/garrytan--loc-controversy#testing-is-the-unlock]]); essay #8 reports a self-audit of **~262K app LOC + ~276K test LOC** ([[sources/garrytan--foxconn-factories#factory-audit]]) inside a manifesto *against* over-building "Foxconn factories." The tension is real and productive: where is the line between "verification loop that lets AI iterate" and "a cage of tests bolted onto a capable model"? Flag for a future analysis; both claims are the same author, weeks apart.
5. **OpenClaw attribution (carry-over).** This essay says *"my OpenClaw can surf the web"* ([[sources/garrytan--loc-controversy#gbrowser-pair-agent]]), reinforcing the wiki's standing tension: OpenClaw is **Peter Steinberger's** harness ([[sources/garrytan--foxconn-factories#openclaw]]), and `garrytan/openclaw` is most likely Garry's fork/deployment. Consistent with the existing reconciliation on [[creators/garry-tan]] and [[sources/garrytan--gbrain]]; no new conflict, just another instance of the possessive "my OpenClaw."
6. **Tokenmaxxing vs cost-rationing (carry-over, latent here).** This essay's "spend whatever it takes on verification / run 2,000+ tests, multiple review passes" posture aligns with the tokenmaxxing thesis of #8 ([[sources/garrytan--foxconn-factories#tokenmaxxing]]) and stands against gbrain's cost-rationing banner ([[sources/garrytan--gbrain#AGENTS.md]]). No new datapoint, but this essay is more evidence on the "spend freely" side of that open question.

## Related sources

- [[sources/garrytan--gstack]] — the artifact this essay is *about*; nearly every concrete claim here grounds in a real gstack file (see notes below). A markdown copy of the essay itself ships at `docs/ON_THE_LOC_CONTROVERSY.md`.
- [[sources/garrytan--gbrain]] — sibling memory product; the "says vs actually building" diarization the series talks about is grounded in gbrain's `docs/takes-vs-facts.md` + `docs/contradictions.md` and `skills/RESOLVER.md` ([[sources/garrytan--gbrain#docs-takes-vs-facts]], [[sources/garrytan--gbrain#skills-resolver]]).
- [[creators/garry-tan]] — author.
- Sibling essays: [[sources/garrytan--thin-harness-fat-skills]] · [[sources/garrytan--resolvers]] · [[sources/garrytan--naked-models]] · [[sources/garrytan--skillify-manifesto]] · [[sources/garrytan--meta-meta-prompting]] · [[sources/garrytan--complexity-ratchet]] · [[sources/garrytan--foxconn-factories]].

**Grounding notes (verified against the snapshots, as-of the 2026-05-20 gstack snapshot):**

- `/qa` + the Playwright browser CLI → real: `sources/garrytan--gstack/qa/SKILL.md` (72 KB) and `sources/garrytan--gstack/browse/src/` (**22,009 TS lines**) containing exactly the subsystems the essay names — `snapshot.ts` (snapshot engine), `browser-manager.ts`, `cdp-allowlist.ts` (CDP), `content-security.ts` + `security-classifier.ts` (content security), `cookie-picker-routes.ts` + `cookie-import-browser.ts` (cookie management), `network-capture.ts`. Grounds [[sources/garrytan--gstack#qa]] and [[sources/garrytan--gstack#browse]].
- `/pair-agent` and `/open-gstack-browser` → real: `sources/garrytan--gstack/pair-agent/` and `sources/garrytan--gstack/open-gstack-browser/` both exist ([[sources/garrytan--gstack#pair-agent]], [[sources/garrytan--gstack#open-gstack-browser]]).
- Multi-level test harness ("unit / E2E / LLM-as-judge / smoke / slop scan") → real: `sources/garrytan--gstack/test/` holds **153 test files** including `skill-validation.test.ts`, `skill-llm-eval.test.ts`, and 50+ `skill-e2e-*.test.ts`, plus resolver evals (`resolver-ask-user-format.test.ts`, `writing-style-resolver.test.ts`). Grounds [[sources/garrytan--gstack#test]] and the bundle/ratchet patterns.
- `slop-scan` → real and *integrated*: `sources/garrytan--gstack/scripts/slop-diff.ts`, `sources/garrytan--gstack/docs/designs/SLOP_SCAN_FOR_REVIEW_SHIP.md`, and slop-scan wiring inside `review/SKILL.md` and `ship/SKILL.md`. The essay's third-party tool is wired into the ship gate.
- Review rigor (CEO / Codex / DX / eng) + `/plan-tune` → real: `scripts/resolvers/review-army.ts` + `review.ts` encode the multi-reviewer fan-out; `codex/` skill dir exists; `plan-tune/` exists with a dedicated `test/skill-e2e-plan-tune.test.ts`. Grounds [[sources/garrytan--gstack#plan-eng-review]] and the review facet of the bundle pattern.
- "Coverage audit in every PR body" → real: referenced in `ship/SKILL.md` (and `CLAUDE.md`/`README.md`). Grounds [[patterns/quality-bar/complexity-ratchet]].
- `scripts/garry-output-comparison.ts` + `EXCLUDED_REPOS` → the script the essay cites is referenced from the in-repo essay copy; the `EXCLUDED_REPOS` constant (excluding `tax-app`) is named in `docs/ON_THE_LOC_CONTROVERSY.md`. We did not separately open the .ts file; treat the script's existence as essay-asserted + in-repo-corroborated, not independently executed.
