# Wiki Log

Append-only chronological record of operations on this wiki. Format per [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):

```
## [YYYY-MM-DD] <operation> | <subject>
- bullet of what was done, what was decided, what to note
```

Operations: `ingest`, `query`, `lint`, `scaffold` (one-time setup), `decision` (design choices that shaped the wiki). Append new entries to the bottom.

---

## [2026-05-21] scaffold | wiki bootstrap

- Created project structure: `_schemas/` (6 templates: skill, plugin, mcp-server, pattern, creator, source), domain dirs (`artifacts/`, `patterns/`, `creators/`, `sources/`, `analyses/`) each with `_index.md`.
- Created `CLAUDE.md` with operating instructions and (post-Karpathy-alignment) Ingest/Query/Lint operations vocabulary.
- Created `README.md` (human entry point) and `.gitignore` (guards nested `.git/` accidents, OS noise, scratch).
- Decided: wiki-style output (vs. report); curated-list collection mode; "speedrun bullets" first depth (later revised to "go deeper").

## [2026-05-21] decision | adopt Karpathy LLM Wiki pattern

- After bootstrap and first 3 ingests, user pointed at https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.
- Confirmed: structure already aligned with the three-layer model (raw sources / wiki / schema).
- Added missing pieces: root `index.md` (single front door catalog), this `log.md` (append-only chronicle), and the `LINT` operation defined in `CLAUDE.md`.
- Reframed `CLAUDE.md` workflow sections around Karpathy's Ingest / Query / Lint vocabulary.

## [2026-05-21] ingest | sources/anthropic--skills

- Cloned `github.com/anthropics/skills` shallow + stripped `.git/`. Commit `690f15c` (2026-05-19). 11 MB.
- Created [[sources/anthropic--skills]] with anchor map covering: `marketplace.json` (3 child plugins, owner Keith Lazuka), `spec/`, `template/`, 17 skills under `skills/`.
- Created [[creators/anthropic]].
- Created [[artifacts/plugins/anthropic-skills-marketplace]] (speedrun depth).
- Patterns proposed (need 2nd example): marketplace-as-multi-plugin, minimal frontmatter, license segmentation within one repo, demonstration-mode disclaimer.

## [2026-05-21] ingest | sources/garrytan--gstack

- Cloned `github.com/garrytan/gstack` shallow + stripped `.git/`. Commit `029356e` (2026-05-20). 41 MB.
- Created [[sources/garrytan--gstack]] with anchor map covering root docs (README, SKILL.md, ETHOS.md, ARCHITECTURE.md, BROWSER.md, CHANGELOG.md) and 30+ skill directories.
- Created [[creators/garry-tan]].
- Created [[artifacts/plugins/gstack]] (speedrun depth).
- Patterns proposed (need 2nd example): persona-shaped command naming, philosophy injection via preamble (ETHOS), frontmatter extensions (`preamble-tier`, `version`, `triggers`, `benefits-from`, `gbrain:` block), voice-trigger aliases, heavy bash preamble as "skill OS", pack-branding suffix (`(gstack)`).

## [2026-05-21] ingest | sources/garrytan--gbrain

- Cloned `github.com/garrytan/gbrain` shallow + stripped `.git/`. Commit `1580c6d` (2026-05-20). 71 MB. Version 0.36.4.0 at snapshot.
- Created [[sources/garrytan--gbrain]] with anchor map covering root docs (huge CLAUDE.md at 342 KB, `AGENTS.md`, `INSTALL_FOR_AGENTS.md`, `llms.txt`, `llms-full.txt`, `openclaw.plugin.json`) and 53 skill entries under `skills/`.
- Created [[artifacts/plugins/gbrain]] (speedrun depth).
- Patterns proposed (need 2nd example): three-shape distribution (CLI + MCP + skillpack), skill-router file `RESOLVER.md`, underscore-prefixed universal rules (`_AGENT_README`, `_brain-filing-rules`, etc.), agent-first install protocol (`AGENTS.md`), `[AGENT]`-marked operator-decision banner, `llms.txt` + `llms-full.txt` dual files.
- Observation worth a future analysis: gstack and gbrain represent *opposite* philosophies on skill selection. gstack uses rich frontmatter + Claude's auto-trigger heuristic. gbrain uses an explicit `RESOLVER.md` file the agent reads once per request to pick a skill.

## [2026-05-21] decision | speedrun depth deemed too shallow

- Pages turned out ~150 lines each despite "speedrun bullets" mandate (too much surface area to compress).
- User feedback: go deeper. Switch to full schema treatment (prose sections, mechanism deep-dives, source line-citations) on next batch.
- Also: expand candidate queue ("keep finding more repos") via discovery sweep before next ingests.

## [2026-05-31] ingest | sources/anthropic--plugins-reference

- Added Claude Code **Plugins reference** docs page (`code.claude.com/docs/en/plugins-reference`) as the first `docs-page` source. Requested specifically for the `#plugin-caching-and-file-resolution` section.
- Living page (no commit stamp) → claims pinned to retrieval date 2026-05-31. Couldn't clone; saved a **partial verbatim snapshot** at `sources/anthropic--plugins-reference/snapshot.md` covering: caching/file-resolution (verbatim), `${CLAUDE_PLUGIN_ROOT}` env-var (verbatim), persistent-data-directory (verbatim), plus the full H2/H3 heading outline. Extracted via page DOM after WebFetch returned an un-sliceable 77KB blob.
- Created [[sources/anthropic--plugins-reference]] citation page with anchor map. No artifact/pattern page created — this is a spec/reference, not an artifact demonstrating patterns (per anti-rule: patterns must be grounded in observed artifacts).
- Wired into: [[sources/_index]] (Docs section), [[index]] (Sources table), [[creators/anthropic]] (source citations).
- Key facts captured for future citation: marketplace plugins are **copied** into `~/.claude/plugins/cache` (not run in-place); each version is its own dir; orphaned versions GC'd after a **7-day grace period**; Glob/Grep skip orphaned dirs; `${CLAUDE_PLUGIN_ROOT}` is the path-resolution convention; persistent data belongs **outside** the install dir.

## [2026-06-01] ingest | sources/anthropic--financial-services

- Cloned `github.com/anthropics/financial-services` shallow + stripped `.git/`. Commit `120a31d` (2026-05-29). 2.7 MB, 371 files, Apache 2.0. Owner `Matt Piccolella` / `Anthropic FSI`.
- **First "full" depth ingest** (vs. the earlier speedruns) per the 2026-05-21 "go deeper" decision. ~14 pages touched.
- Created [[sources/anthropic--financial-services]] with a thorough anchor map (root docs, marketplace.json, cookbooks, agent plugins, verticals, partners, scripts, CI, MSFT-365 installer).
- Created [[artifacts/plugins/anthropic-financial-services-marketplace]] — the marketplace as a whole (20 plugins: 7 vertical + 10 agent + 2 partner + 1 installer; 10 managed-agent cookbooks; 55 skills; 39 commands; 30 subagents). Used `gl-reconciler` as a fully-cited worked example.
- **Confirmed the wiki's first two patterns** (each got its 2nd grounded example here):
  - [[patterns/composition/single-source-multi-surface-distribution]] — FSI (Cowork plugin + Managed Agents API) + gbrain (CLI + MCP + skillpack). Created `patterns/composition/`.
  - [[patterns/structural/marketplace-as-multi-plugin]] — FSI (20) + anthropic-skills (3); counter-example gstack/gbrain (one plugin, many internal skills). Created `patterns/structural/`.
- Proposed (1 example, tracked on the marketplace page): **trust-tiered subagent privilege separation** (the standout — only the reader touches untrusted docs, exactly one leaf holds Write, a critic re-verifies), structured-output-as-injection-defense, single-source skill vendoring + drift check, provenance-first data-source hierarchy, version-as-update-gate, audience-segmented skill output.
- **Finding (verified):** `plugins/vertical-plugins/financial-analysis/.mcp.json` is **malformed JSON** (missing comma after the `egnyte` entry; `python3 -m json.tool` fails), and `check.py` doesn't validate `.mcp.json` — so it slipped through. Bounds the otherwise-rigorous drift-check story. Surfaced to Sidney as a possible upstream report; left as-is in the immutable snapshot.
- Wired into: [[creators/anthropic]] (Plugins + design philosophy + citations; FSI is a distinct internal team), [[sources/_index]], [[creators/_index]], [[artifacts/plugins/_index]] (promoted + 18 child candidates queued), [[artifacts/skills/_index]] (~7 pattern-bearing skill candidates), [[artifacts/mcp-servers/_index]] (12 connectors queued), [[patterns/_index]], [[index]] (sources + plugins tables, confirmed-patterns section), `README.md` (status counts).
- Note for a future analysis: FSI's `gl-reconciler` / `statement-auditor` / `valuation-reviewer` / PE `ic-memo`+`returns-analysis` map closely onto Sidney's music-catalog royalty-audit / NAV-tie-out / IC-memo work; the trust-tiered "untrusted counterparty statement reader" is directly liftable to third-party royalty statements.

## [2026-06-01] ingest | Garry Tan "AI Explainer" series (essays #1–#7)

- Completed Garry Tan's **8-part "AI Explainer" series** (#8 foxconn-factories was ingested earlier same day; this entry covers the remaining 7). New `article` sources: [[sources/garrytan--thin-harness-fat-skills]] (#1), [[sources/garrytan--resolvers]] (#2), [[sources/garrytan--loc-controversy]] (#3), [[sources/garrytan--naked-models]] (#4), [[sources/garrytan--skillify-manifesto]] (#5), [[sources/garrytan--meta-meta-prompting]] (#6), [[sources/garrytan--complexity-ratchet]] (#7). Each has a verbatim snapshot + a full citation page (anchor map, popularity-signal time-series, series context, contradictions).
- **Method (multi-agent, user opted into workflows):** main agent wrote the 7 verbatim snapshots by hand (immutable evidence — one-hop fidelity). Then **Workflow #1** (7 agents, 613K tokens) authored the 7 source citation pages + returned structured analyses (isolated writes, no shared-file contention; agents verified groundings against the real gstack/gbrain snapshots). Then **Workflow #2** (6 agents, 717K tokens) authored the 6 new pattern pages from grounding packets. Main agent did all shared-layer synthesis (patterns/_index, index, creators, README, foxconn series footer, log) + the skill-pack-bundle extension + lint. (First workflow attempt failed instantly — `args` arrived as a JSON *string*, so `args.essays` was undefined; fixed with a parse-if-string guard and re-ran.)
- **Patterns extracted (the research payload):** the 7 essays collapse into a tight canonical set.
  - **3 newly CONFIRMED** (each grounded in 2 distinct in-wiki artifacts, gstack + gbrain — same-creator caveat tracked on every page): [[patterns/composition/resolver-routing-table]] (gbrain `RESOLVER.md` + 14+ `routing-eval.jsonl` + `check-resolvable.ts`; gstack `scripts/resolvers/` + resolver evals — **supersedes** the old proposed "skill-router file RESOLVER.md" bullet), [[patterns/behavioral/latent-vs-deterministic-split]] (gstack deterministic `browse/`+`bin/` vs latent skills; gbrain "zero-LLM" graph — note "latent" is the essays' label, 0 hits in gstack docs), and **promoted** [[patterns/quality-bar/skill-pack-bundle]] from proposed→confirmed (the Skillify Manifesto's 10-step checklist + gbrain's `gbrain doctor` *enforcing* it = the full 2nd example).
  - **4 PROPOSED, each with a dedicated page** (1 grounded artifact so far): [[patterns/structural/thin-harness-fat-skills]] (fat-skills grounded; the thin *harness* = OpenClaw, not ingested), [[patterns/behavioral/skill-as-method-call]] (gstack `/qa` tiers, `/investigate`), [[patterns/behavioral/diarization]] (gbrain `enrich/` + brain-page schema), [[patterns/quality-bar/complexity-ratchet]] (gstack TTY review-floor tests + gbrain extraction-ratchet; kept proposed because it rests on the same test-evidence as skill-pack-bundle and both are Garry's).
  - Created two new pattern categories' first pages: `behavioral/` (3) and reinforced `structural/`+`quality-bar/`.
- **Contradictions/tensions tracked for LINT** (surfaced repeatedly across the essays, not silently resolved): OpenClaw = Peter Steinberger's harness (every essay says "my OpenClaw" = his deployment, not authorship — reconciliation stands); tokenmaxxing (spend freely) vs gbrain's `[AGENT]` cost-banner (rationing) — same author, same axis; the "ratchet vs Foxconn factory" tension (the *same* ~276K-line test corpus is celebrated in #7 and pejorative in #8 — reconciled by "tests = behavioral contracts good / distrust-the-model cages bad"); and a **provenance boundary** the source-page agents flagged well — the per-skill counts ("179 unit tests," "35 daily evals," `calendar-recall`/`context-now`) are author self-claims about Garry's *private* brain, while the *machinery* (`check-resolvable.ts`, `doctor.ts`, `_brain-filing-rules.md`, `skillify/generator.ts`) is verified in the *public* gbrain repo.
- **Longitudinal popularity dataset captured:** the series quotes gstack stars climbing **72K (#2) → 75K (#3) → 87K (#6) → 93K (#7) → 105K (#8, verified 105,761)** and gbrain **14K (#7) → 20,403 (measured)**, each with an as-of date — a verifiable growth curve, not a single decaying signal. Datable anchors: #3 ≈ 2026-04-18 ("day 108"), #7 = 2026-05-12 (byline).
- **Lint (clean):** all wikilinks resolve (the 2 flagged are the `joe-dev--my-skill-pack` citation-convention *examples*); every cited source anchor is registered; fixed a real drift the agents caught — gstack `#bin` said "62 entries" but the snapshot has **60** (corrected). Karpathy connection worth noting: #6 credits "Karpathy's LLM Wiki" as GBrain's inspiration — the *same* pattern this wiki itself is built on.
- ~17 pages touched/created beyond the 7 snapshots + 7 source pages: 6 pattern pages, skill-pack-bundle (extended+promoted), index, sources/_index, patterns/_index, creators/garry-tan, README, foxconn (series footer), gstack source (#bin fix).

## [2026-06-01] ingest | sources/garrytan--foxconn-factories

- First **article** source (vs. repos / docs-page). Garry Tan's essay *"Stop building Foxconn factories for your agents."* Pasted verbatim by Sidney; saved immutable snapshot at `sources/garrytan--foxconn-factories/snapshot.md` (author's typos preserved). Canonical URL + publication date unconfirmed — TODO.
- Created [[sources/garrytan--foxconn-factories]] with a 14-anchor thematic map (`#thesis`, `#economics-flip`, `#jit-software`, `#skill-pack`, `#skillify-loop`, `#hackathon-judge`, `#factory-audit`, `#tokenmaxxing`, `#openclaw`, `#esalen`, `#gstack-stars`, `#ios-testing`, …).
- **New pattern (first `quality-bar/` page):** [[patterns/quality-bar/skill-pack-bundle]] — a skill ships as a *tested bundle* (markdown skill + thin code + unit test + LLM eval + integration test + resolver + **resolver eval**). Grounded by **verifying gstack's real `test/` harness**, not just the essay's claim: `skill-validation` + `skill-llm-eval` + `skill-e2e-*` + `scripts/resolvers/*` + `resolver-ask-user-format`/`writing-style-resolver`/`resolvers-gbrain-put-rewrite` tests, under diff-based `gate`/`periodic` tiers. Kept **`proposed`**: both examples (gstack full, gbrain partial) are Garry's — needs a non-Garry artifact, ideally one with a *resolver eval*.
- Verified nuance: gstack's shipped `/skillify` is *narrower* than the essay's loop — it codifies a `/scrape` flow into `script.ts + script.test.ts + fixture`, not the full 7-part bundle. Documented on both the artifact and pattern pages so we don't conflate them.
- **Contradictions surfaced for LINT (not silently overwritten):**
  - **OpenClaw authorship** — essay says *"Peter Steinberger built OpenClaw"*; wiki had implied `garrytan/openclaw` was Garry's platform. Annotated [[creators/garry-tan]] + [[artifacts/plugins/gbrain]] with the correction (OpenClaw = Steinberger's harness; `garrytan/openclaw` likely a fork; gbrain *targets* it). Possible missing wiki axis: **harnesses/runtimes**.
  - **Tokenmaxxing vs. cost-rationing** — essay preaches free token spend; gbrain's `[AGENT]` banner forces a 25× cost-spread confirmation. Logged as a cross-artifact open question on the gbrain page + source page (candidate future analysis).
- **Popularity signal (caveated):** GStack ~105,000 stars in <3 months ("hundred most-starred OSS in GitHub history") — **author self-claim, unverified**. Filled the previously-empty star field on [[sources/garrytan--gstack]] + [[artifacts/plugins/gstack]] as a *claim* with a `gh api` verification TODO (sibling gbrain only showed ~14K, so flagged for skepticism). Also: "more than 350 skillpacks" (author usage), OpenAI's $2M uncapped-SAFE token credits to YC cos.
- Touched ~12 pages: source page + snapshot (new), pattern page (new, new `quality-bar/` dir), [[creators/garry-tan]], [[artifacts/plugins/gstack]], [[sources/garrytan--gstack]] (added `#test` anchor), [[artifacts/plugins/gbrain]], [[index]], [[sources/_index]], [[patterns/_index]], [[creators/_index]], README.

## [2026-06-01] query | gstack star count verification

- Ran `gh api repos/garrytan/gstack` + `…/gbrain`. **GStack = 105,761 stars** (created 2026-03-11) — Garry's essay self-claim of "~105,000 in under three months" **VERIFIED** (he rounded *down*; timeframe holds). The companion "hundred most-starred OSS in GitHub history" ranking is plausible but NOT independently checked (no leaderboard). Updated [[sources/garrytan--gstack]], [[artifacts/plugins/gstack]], [[sources/garrytan--foxconn-factories]] from "unverified self-claim" → measured fact (as-of 2026-06-01); essay's wording preserved alongside the measurement.
- **Stale-signal finding (for LINT):** sibling **gbrain now = 20,403 stars**, not the ~14K the wiki recorded at the 2026-05-21 snapshot — and that stale ~14K was the basis for doubting the gstack claim, so the doubt is retired. [[artifacts/plugins/gbrain]] still shows ~14K; flag to refresh.
