---
domain: sources
type: article
url: https://x.com/garrytan # profile; canonical post URL not yet confirmed — TODO
retrieved: 2026-06-01
snapshot-location: sources/garrytan--foxconn-factories/snapshot.md
upstream-commit: n/a (essay, not a repo)
last-reviewed: 2026-06-01
---

# "Stop building Foxconn factories for your agents" (`garrytan`, essay)

> Garry Tan's manifesto arguing that 540K-line apps "wrapped around an LLM" are cages built for a worker who doesn't need them, and that the real artifact of the AI era is the **skill pack** — a tested, versioned bundle of markdown + minimal code produced by a one-word "skillify" loop. Our primary source for Garry's articulation of the skill-pack primitive, the "tokenmaxxing" thesis, and the GStack popularity claim (~105K stars).

## Snapshot details

- **Retrieved**: 2026-06-01 (pasted verbatim by Sidney; we hold the full text).
- **Where it lives in this wiki**: [`sources/garrytan--foxconn-factories/snapshot.md`](garrytan--foxconn-factories/snapshot.md) — verbatim, immutable, author's typos preserved.
- **Upstream URL**: not yet confirmed. Reads as an X long-form post / blog essay under [@garrytan](https://x.com/garrytan). **TODO**: locate canonical URL + publication date and add an archive.org link.
- **Publication date**: unconfirmed. Internal evidence ("Two Saturdays ago we ran a GStack/GBrain hackathon") dates the hackathon to **≈2026-05-23** *if* the essay was written near our retrieval date — treat as approximate.

## Anchor map

Every claim citing this source uses a `#anchor` from this list. The essay is one prose file; anchors are thematic pointers into the author's own sections.

- `#root` — the essay as a whole
- `#thesis` — the core claim: code written to "police" a model is a Foxconn factory bolted onto "a worker who can already do the job"
- `#economics-flip` — "LLMs were expensive so we had to harness them"; both halves flipped (model cheap + can write code) → stop writing code to babysit it
- `#jit-software` — "just-in-time-software"; "Markdown is the program now" (markdown = instruction layer, TypeScript = thin deterministic I/O layer)
- `#skill-pack` — the 7-part skill-pack definition (markdown skill + minimal code + unit test + LLM eval + integration test + resolver + resolver eval); "A skill pack has tests"
- `#skillify-loop` — the one-word "skillify it" loop; "I have more than 350 skillpacks"
- `#hackathon-judge` — the 85-submission hackathon-judge skillpack ("about thirty minutes"), built by OpenClaw then skillified into a reusable tarball
- `#factory-audit` — the self-audit: ~262K app LOC + ~276K test LOC; 127 background jobs (33 on cron); the 1,778-line claim-fact-checker that fans each claim out to 5 sources
- `#tokenmaxxing` — the token-spend thesis: Steinberger's ~$1M/yr, OpenAI's $2M uncapped-SAFE token credits to YC cos, "live in 2028… in 2026"
- `#openclaw` — OpenClaw attribution ("Peter Steinberger built OpenClaw, my favorite harness"); "a Ferrari you have to bring a wrench for… the model is the engine, not the car"
- `#esalen` — the ethos: build Esalen, not Foxconn; "places where the workers, both human and AI, are free and not enslaved"
- `#clarity-taste-judgment` — the close: "the scarce resource becomes clarity, taste, and judgment. The engineer who writes the least code is often the one building the most."
- `#gstack-stars` — "one of the hundred most-starred open source projects in GitHub history, about 105,000 stars in under three months" (author self-claim)
- `#ios-testing` — hackathon winner's iOS-test feature (simulator + real devices) landed on GStack `main`, "made in less than 8 hours… by a single person"

## Why we cite this

- **The clearest first-person articulation of the "skill pack" primitive** we have — the author who coined the term defining its exact 7-part shape and its production rationale ("coverage on the skill is what lets it change without breaking"). Grounds [[patterns/quality-bar/skill-pack-bundle]].
- The **"just-in-time software / markdown is the program"** thesis — the philosophy underneath every Garry Tan artifact in this wiki.
- The **"tokenmaxxing"** economic argument — useful context, and an interesting *tension* against gbrain's cost-rationing banner (see Related sources).
- The **Foxconn-factory anti-pattern** — a vivid, quotable framing of "code written to distrust a capable model," and the counter-example anchor for the skill-pack pattern.
- A fresh **popularity signal** for GStack (the ~105K-star claim) the repo snapshots didn't capture.
- An **attribution correction**: OpenClaw is **Peter Steinberger's** harness, not Garry's (see Related sources).

## Popularity signals (this source IS one)

This is a "talked-about / named-person-quoted" signal in its own right (a YC CEO's manifesto), and it contains a hard metric claim about GStack:

- **Signal type**: github-stars — **author self-claim, now VERIFIED** (star count + timeframe; the ranking sub-claim only partially)
- **Claimed (essay)**: "about 105,000 stars in under three months"; "one of the hundred most-starred open source projects in GitHub history" for `garrytan/gstack` ([[sources/garrytan--foxconn-factories#gstack-stars]])
- **Measured**: **105,761 stars** via `gh api repos/garrytan/gstack` (as-of 2026-06-01); repo created **2026-03-11**, so "under three months" holds. The author rounded *down* — the count is, if anything, slightly understated. The "hundred most-starred in GitHub history" ranking is plausible at 105K+ but we did **not** independently confirm it (no GitHub-wide leaderboard checked).
- **As-of**: 2026-06-01 (claim retrieval **and** measurement)
- **✓ Verification outcome**: the extraordinary self-claim **held up** against live evidence — it is no longer recorded as a mere claim; it *is* the measured fact now. The earlier skepticism leaned on the gbrain snapshot's ~14K for the sibling repo, but that number was stale: gbrain now measures **20,403** (as-of 2026-06-01), and gstack is confirmed on its own terms regardless. (Stars are a moving figure; re-measure on a new as-of before citing later.)
- **Secondary signals**: "more than 350 skillpacks" (author's own usage) ([[sources/garrytan--foxconn-factories#skillify-loop]]); OpenAI's $2M uncapped-SAFE token credits to every YC company ([[sources/garrytan--foxconn-factories#tokenmaxxing]]).

## Contradictions & corrections this source raises (for LINT)

1. **OpenClaw authorship.** Essay: *"Peter Steinberger built OpenClaw, my favorite harness"* ([[sources/garrytan--foxconn-factories#openclaw]]). The wiki currently implies OpenClaw is Garry's: [[creators/garry-tan]] lists "`garrytan/openclaw` — the agent platform gbrain primarily targets," and [[sources/garrytan--gbrain]] calls it "Garry's OpenClaw… deployments." **Reconciliation**: OpenClaw is Steinberger's harness; `garrytan/openclaw` is most likely Garry's fork/deployment, and gbrain *targets* OpenClaw rather than being part of it. Flagged on both pages; not silently overwritten (the snapshots are immutable evidence and `garrytan/openclaw` may genuinely exist as a fork).
2. **Tokenmaxxing vs. cost-rationing.** This essay preaches spending freely on tokens ([[sources/garrytan--foxconn-factories#tokenmaxxing]]); gbrain's `[AGENT]`-marked banner forces the operator to confront a 25× cost spread *before* proceeding ([[sources/garrytan--gbrain#AGENTS.md]]). Same author, apparently opposite instincts. Likely reconcilable (don't *architecturally* ration the model's intelligence vs. do give the operator an *informed* choice on a configurable knob), but worth a future analysis. Tracked as an open question.

## Series context

This is **essay #8 (the finale) of Garry Tan's 8-part "AI Explainer" series** (ingested 2026-06-01). It pairs with #7 as the bookend manifesto and quotes the series' terminal star figure (~105K, verified 105,761). Siblings, in order:

1. [[sources/garrytan--thin-harness-fat-skills]] — the architecture (five primitives + three layers).
2. [[sources/garrytan--resolvers]] — the routing table / governance layer.
3. [[sources/garrytan--loc-controversy]] — the LOC math + quality data.
4. [[sources/garrytan--naked-models]] — model = engine, harness = car (rebuts Kingsbury).
5. [[sources/garrytan--skillify-manifesto]] — the 10-step skillify checklist (the richest [[patterns/quality-bar/skill-pack-bundle]] articulation; this essay #8 gives the 7-part version).
6. [[sources/garrytan--meta-meta-prompting]] — compounding skills + diarization at scale.
7. [[sources/garrytan--complexity-ratchet]] — 90% coverage / forward-only quality.
8. **#8, this page.**

**Patterns this essay grounds:** [[patterns/quality-bar/skill-pack-bundle]] (the 7-part bundle / "skillify" loop), and the "Foxconn factory" framing is the key counter-example for [[patterns/quality-bar/complexity-ratchet]] (tests-as-contracts vs. tests-as-cage).

## Related sources

- [[sources/garrytan--gstack]] — the artifact this essay is *about*; its real test architecture (`skill-validation` / `skill-llm-eval` / `skill-e2e` / `scripts/resolvers/` + resolver tests) is the grounding for the skill-pack pattern the essay describes.
- [[sources/garrytan--gbrain]] — "GBrain, the retrieval engine and skillpacks I give away"; also the source of the OpenClaw-attribution and tokenmaxxing tensions above.
- [[creators/garry-tan]] — author.
