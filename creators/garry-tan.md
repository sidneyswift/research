---
domain: creators
type: individual
name: Garry Tan
handle: garrytan
url: https://github.com/garrytan
twitter: https://x.com/garrytan
role: President & CEO, Y Combinator
last-reviewed: 2026-06-01
---

# Garry Tan

> President & CEO of Y Combinator. Ships opinionated open-source agent tooling (gstack, gbrain) co-authored with Claude Opus 4.6. Brings distribution scale to the agent ecosystem — when he ships something, the agent community pays attention.

*Page shape (gbrain's brain-page schema, per [[patterns/behavioral/diarization]]): the sections below are **compiled truth** (current best understanding, edited in place); the **append-only [`## Timeline`](#timeline-append-only)** at the bottom records dated events — the arc, not just the snapshot.*

## Attributes

- **Background** (per [[sources/garrytan--gstack#README]]): Twenty years building products. Cofounder Posterous (sold to Twitter). Early eng/PM/designer at Palantir. Built Bookface (YC's internal social network) in 2013.
- **Current role**: President & CEO, Y Combinator.
- **Distribution channels**: github.com/garrytan, x.com/garrytan, public speaking via No Priors and Hacker News.
- **Position in ecosystem**: Bridge between Anthropic's ecosystem and the broader builder/founder community. Not an Anthropic employee — an outside power-user with reach.
- **Self-claim** ([[sources/garrytan--gstack#README]]): "~810× my 2013 pace" of logical code change in 2026; 1,237 GitHub contributions YTD; 3 production services + 40+ features in 60 days, part-time, while running YC.
- **Co-authoring credit**: Both `gstack` and `gbrain` are co-authored with Claude Opus 4.6 per commit history (per Augment Code coverage).

## Artifacts produced

### Plugins / skill packs
- [[artifacts/plugins/gstack]] — virtual engineering team for Claude Code (23 skills + 8 power tools)
- [[artifacts/plugins/gbrain]] — agent memory system (MCP server + CLI + 43-skill scaffold)

### Adjacent artifacts (not yet deep-dived)
- **OpenClaw** — the agent *harness* gbrain primarily targets and Garry's "favorite harness." ⚠ **Authorship correction:** OpenClaw was **built by Peter Steinberger**, not Garry — *"Peter Steinberger built OpenClaw, my favorite harness"* ([[sources/garrytan--foxconn-factories#openclaw]]). Earlier notes here treated `garrytan/openclaw` as Garry's platform; that repo is most likely his **fork/deployment**, with gbrain *targeting* OpenClaw rather than being part of it. (Manifest referenced in [[sources/garrytan--gbrain#openclaw-plugin-json]].) Flagged for LINT; not yet re-verified.
- `garrytan/hermes` — another agent deployment Garry runs
- `garrytan/gbrain-evals` — sibling repo with BrainBench scorecards
- Bookface (private, YC-internal)

### Public framing
- **The "AI Explainer" series — 8 essays (~Apr–May 2026)**, the most complete statement of Garry's agent-engineering worldview and the source for most of the wiki's patterns. Ordered: #1 [[sources/garrytan--thin-harness-fat-skills]] (the architecture), #2 [[sources/garrytan--resolvers]] (routing as governance), #3 [[sources/garrytan--loc-controversy]] (the LOC math), #4 [[sources/garrytan--naked-models]] (model = engine, harness = car; rebuts Kyle Kingsbury), #5 [[sources/garrytan--skillify-manifesto]] (the 10-step skillify checklist; critiques LangChain), #6 [[sources/garrytan--meta-meta-prompting]] (compounding skills; credits Karpathy's LLM Wiki — *this wiki's own pattern* — as GBrain's inspiration), #7 [[sources/garrytan--complexity-ratchet]] (90% coverage / forward-only quality), #8 [[sources/garrytan--foxconn-factories]] (the skill-pack manifesto + "tokenmaxxing"). A self-documenting growth log: gstack stars 72K→105K across the run.
- Quoted reference to Karpathy on No Priors podcast (March 2026), "haven't typed code since December" ([[sources/garrytan--gstack#README]])
- HN thread: https://news.ycombinator.com/item?id=47418576 — TODO snapshot
- **People/projects he positions against or alongside** (context, not yet cataloged): Steve Yegge (the "100x" quote, #1), Kyle Kingsbury / Jepsen (the rebuttal target, #4), Pete Koomen / "AI Horseless Carriages" (#4, ally), Ben Vinegar & David Cramer / Sentry (slop-scan + the quality critique, #3), Peter Steinberger / OpenClaw (#8), Nous Research / Hermes Agent (#5, "creation without verification"), LangChain/LangSmith (#5, the funded-but-workflow-less foil).

## Design philosophy (discernible from artifacts)

- **Opinionated over generic.** gstack is "Garry's exact setup" — the README explicitly markets the opinionation. Compare to Anthropic's skills which are demonstration-mode and unopinionated.
- **Personas over task categories.** gstack organizes skills as roles (CEO, Designer, Eng Manager, QA Lead, CSO) instead of as workflows. ([[sources/garrytan--gstack#README]])
- **Inject philosophy into every skill via preamble.** `ETHOS.md` is appended to every workflow skill's preamble — "Boil the Lake", "Completeness is cheap". ([[sources/garrytan--gstack#ETHOS.md]])
- **Custom frontmatter beyond Anthropic's spec.** `preamble-tier:`, `version:`, `allowed-tools:`, `triggers:` — extensions used in gstack SKILL.md files. ([[sources/garrytan--gstack#SKILL.md]])
- **Voice triggers as first-class.** gstack skills declare speech-to-text aliases in frontmatter ("quality check" → /qa).
- **Agent-first install docs.** gbrain ships `AGENTS.md` *separate from* `CLAUDE.md`, with agent-specific install protocols. Treats LLMs as the primary readers of operational docs.
- **Force human-in-the-loop on cost-bearing choices.** gbrain's 9-cell cost matrix `[AGENT]`-marked banner — the agent MUST relay to operator before continuing. ([[sources/garrytan--gbrain#AGENTS.md]])
- **Heavy versioning + changelog discipline.** gstack CHANGELOG is 690 KB; gbrain CHANGELOG is 1.1 MB. These aren't side projects.
- **Markdown is the program; code is the thin deterministic layer.** *"The markdown is the instruction layer… The TypeScript is the thin deterministic layer… the parts that must never hallucinate"* ([[sources/garrytan--foxconn-factories#jit-software]]). This is the worldview behind ETHOS-injection and the persona skills: behavior should live in editable prose, not frozen code.
- **The skill pack is the unit, and it has tests.** A capability isn't done until "skillify it" emits the skill + minimal code + unit test + LLM eval + integration test + resolver + resolver eval. *"A skill pack has tests"* — the tests are what let prose behavior change without breaking ([[sources/garrytan--foxconn-factories#skill-pack]]). → [[patterns/quality-bar/skill-pack-bundle]].
- **Anti-pattern he now warns against: the "Foxconn factory."** Code written to *police* a capable model — sanitizers, validators, retry loops, 127 cron alarms, a 1,778-line fact-checker — is a cage bolted onto a worker who could do "1000x more if we let them" ([[sources/garrytan--foxconn-factories#thesis]], [[sources/garrytan--foxconn-factories#factory-audit]]). A direct tension with gstack's *own* heavy preamble/guardrail "skill OS" — worth watching whether his artifacts move toward this ethos.
- **Tokenmaxxing.** Willing to burn tokens freely; rationing model calls is "the 2013 instinct" holding people back. *"You can live in 2028 but in 2026"* ([[sources/garrytan--foxconn-factories#tokenmaxxing]]). NB: surface tension with gbrain's cost-rationing `[AGENT]` banner — see [[sources/garrytan--foxconn-factories]] "Contradictions."
- **Free systems over control systems.** "Esalen, not Foxconn" — build rough, trusting tools (OpenClaw as "a Ferrari you bring a wrench for") that free the agent, rather than polished cages ([[sources/garrytan--foxconn-factories#esalen]]).
- **Thin harness, fat skills** (the series' namesake architecture). Push intelligence *up* into markdown skills (~90% of the value), execution *down* into deterministic code, keep the harness thin (~200 lines, read-only by default). "The model is the engine, not the car." → [[patterns/structural/thin-harness-fat-skills]] ([[sources/garrytan--thin-harness-fat-skills#three-layer-architecture]]).
- **The resolver is the governance layer.** A ~200-line routing table beats a 20,000-line `CLAUDE.md`; skills are employees, the resolver is the org chart, `check-resolvable` is audit, trigger evals are performance reviews. Test the *routing*, not just the output. → [[patterns/composition/resolver-routing-table]] ([[sources/garrytan--resolvers#management-metaphor]]).
- **Latent vs. deterministic is the core triage.** Every step is model-judgment or same-in/same-out; the most common bug is "not a wrong answer — a wrong side" (mental timezone math, ad-hoc calendar reasoning). The latent model writes the deterministic tool that then constrains it. → [[patterns/behavioral/latent-vs-deterministic-split]] ([[sources/garrytan--skillify-manifesto#wrong-side-not-wrong-answer]]).
- **Diarization is the knowledge-work unlock.** Read everything about a subject, write one page of distilled judgment (the "says vs actually building" gap) — what no SQL/RAG can. → [[patterns/behavioral/diarization]] ([[sources/garrytan--meta-meta-prompting#book-mirror]]).
- **Skills are parameterized method calls.** One `/investigate` (TARGET/QUESTION/DATASET) is a medical analyst or a forensic investigator depending on what you pass. → [[patterns/behavioral/skill-as-method-call]] ([[sources/garrytan--thin-harness-fat-skills#skill-as-method-call]]).
- **The complexity ratchet: tests make quality forward-only.** Every session adds tests+docs+evals that reload into the next session's context; 90% coverage is "free" now that agents "don't experience effort." → [[patterns/quality-bar/complexity-ratchet]] ([[sources/garrytan--complexity-ratchet#ratchet-three-things]]).
- **Open harnesses you own beat corporate SaaS AI.** "The brain is a git repo you own… if any piece disappeared tomorrow, your knowledge survives as plain text." Open source is also *why verification works* — only an open skill lets the user write the check ([[sources/garrytan--naked-models#open-harness]], [[sources/garrytan--resolvers#build-your-own-brain]]).

## Timeline (append-only)

Dated arc of Garry's agent-tooling run. Append newest at the bottom; don't rewrite past entries. The star time-series is the headline signal — it climbs across the essay series.

- 2026-03 — Quoted Karpathy on the No Priors podcast; "haven't typed code since December" ([[sources/garrytan--gstack#README]]).
- 2026-03-11 — `gstack` repo created (per `gh api repos/garrytan/gstack`).
- 2026-04-05 — `gbrain` launched; ~5,000 stars in the first 24 hours ([[sources/garrytan--gbrain#README]]).
- 2026-04 → 2026-05 — published the 8-essay **"AI Explainer" series**; `gstack` stars climbed 72K → 87K → 105K across the run ([[sources/garrytan--meta-meta-prompting]], [[sources/garrytan--foxconn-factories#gstack-stars]]).
- 2026-05 — `gbrain` ~14,000 stars (Vectorize.io review) ([[sources/garrytan--gbrain#README]]).
- 2026-05-21 — first wiki snapshot of `gstack` (`029356e`) and `gbrain` (`1580c6d`).
- 2026-06-01 — measured via `gh api`: `gstack` **105,761** stars (self-claim of "~105,000 in <3 months" confirmed), `gbrain` **20,403** stars (up from the stale ~14K).

## Source citations

- [[sources/garrytan--gstack#README]] — personal background, productivity claims, gstack pitch
- [[sources/garrytan--gstack#ETHOS.md]] — the "Builder Ethos" doc
- [[sources/garrytan--gbrain#README]] — gbrain pitch, production scale claims (17,888 pages, etc.)
- [[sources/garrytan--gbrain#AGENTS.md]] — agent-first protocol design
- [[sources/garrytan--gbrain#openclaw-plugin-json]] — manifest format extensions
- **The AI Explainer series (8 essays)** — [[sources/garrytan--thin-harness-fat-skills]] (#1), [[sources/garrytan--resolvers]] (#2), [[sources/garrytan--loc-controversy]] (#3), [[sources/garrytan--naked-models]] (#4), [[sources/garrytan--skillify-manifesto]] (#5), [[sources/garrytan--meta-meta-prompting]] (#6), [[sources/garrytan--complexity-ratchet]] (#7), [[sources/garrytan--foxconn-factories]] (#8). The skill-pack primitive, JIT-software, tokenmaxxing, the resolver/latent-deterministic/diarization/ratchet patterns, the OpenClaw=Steinberger correction, and the gstack/gbrain star time-series.
