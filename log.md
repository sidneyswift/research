# Wiki Log

Append-only chronological record of operations on this wiki. Format per [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):

```
## [YYYY-MM-DD] <operation> | <subject>
- bullet of what was done, what was decided, what to note
```

Operations: `ingest`, `query`, `lint`, `reflect` (apply the wiki's learnings to itself), `scaffold` (one-time setup), `decision` (design choices that shaped the wiki). Append new entries to the bottom.

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

## [2026-06-01] decision | broaden scope to all AI/agents + Karpathy re-alignment

- **Scope broadened** from "Anthropic ecosystem only" to **all things AI/agents** — skills, plugins, MCP servers, frontier projects, and the essays/papers/threads about the field. Reason: the Garry Tan essay ingests already spilled past the Anthropic boundary, so the schema was lying about what the wiki is. Updated `CLAUDE.md` (title + purpose + scope), `README.md` (title + scope paragraph, old scope preserved as history), `index.md`, and `artifacts/_index.md`.
- **Made INGEST source-type-aware.** The ritual was repo-only (`git clone`); added explicit branches for **article/essay/thread**, **paper**, and **docs-page** (snapshot to markdown, version-stamp by publish date instead of commit SHA) — matching what the `garrytan--*` essays already did in practice.
- **New layer — `concepts/`.** Essays/papers yield *ideas*, and a pattern needs ≥2 artifacts, so ideas had no home. Added `concepts/` + `_schemas/concept.md` + `concepts/_index.md`. Defined the artifact-vs-concept-vs-pattern distinction in `CLAUDE.md`.
- **New artifact sub-type — `artifacts/projects/`.** For frontier systems/products bigger than one skill/plugin/MCP. Added stub `_index.md`.
- **Karpathy gaps closed:** LINT now checks (9) concepts mentioned but page-less, (10) web-fillable data gaps, (11) next questions/sources to chase; QUERY notes answer-format options (table/Marp/chart/canvas) file back to the wiki; added the `grep "^## \[" log.md` tip; added `paper` to `_schemas/source.md` `type:` enum.
- Touched ~9 pages: `CLAUDE.md`, `README.md`, `index.md`, `artifacts/_index.md`, `_schemas/source.md`, `_schemas/concept.md` (new), `concepts/_index.md` (new), `artifacts/projects/_index.md` (new), this log.

## [2026-06-01] decision | exhaustive-steal + self-improving REFLECT operation

- **"What we'd steal" is now an exhaustive ledger, not a curated top-3.** Risk it addressed: if the LLM only mines a thin steal list, attention narrows and ideas get silently discarded over time. New rule: capture *everything* portable, ★-mark the best; idea-mining queries must read whole pages + `## Patterns demonstrated`, not just steal sections. Updated the anti-rules in `CLAUDE.md` and the section instructions in all four schemas (`skill`, `plugin`, `mcp-server`, `concept`).
- **Added a 4th operation: REFLECT** — turn the wiki's own learnings on its machinery (the wiki is itself an LLM agent/skill system). Added the operation to `CLAUDE.md`, a quick-pass trigger as INGEST step 9, and `reflect` to the log op vocabulary.
- **Created `meta/self-improvements.md`** — the REFLECT ledger; every entry must cite a `[[patterns/...]]` page. Seeded with 6 grounded candidates reflecting the AI-Explainer patterns back onto the wiki (resolver-routing-table → routing table in CLAUDE.md; complexity-ratchet → forward-only ingests; diarization → "distillation not summary"; latent-vs-deterministic → annotate op steps; thin-harness-fat-skills → keep CLAUDE.md thin; skill-pack-bundle → pattern pages need a detection recipe). All `proposed`, human-gated.
- **Open / deferred:** point #2 (clone-with-`.git` vs. immutable snapshot so we can `git pull` upstream updates) — left for a decision because it changes how `sources/` is stored/tracked. Not yet implemented.

## [2026-06-01] decision | source storage model — "Option B" (live local clones, git-ignored)

- **Decided (Sidney):** repos are kept as **live local clones with `.git` intact** so we can `git pull`, but **git-ignored from the wiki** (no longer committed) — only their `.md` citation pages are tracked. Captured article/paper/docs snapshots **stay committed** (immutable evidence, nothing to clone). Replaces the old "clone then `rm -rf .git`, commit the snapshot" model.
- **Why:** (a) enables tracking upstream updates over time; (b) keeps the wiki lean now that scope = all of AI/agents (vendoring full frontier repos would balloon git history fast). The old model had already committed ~125 MB.
- **Migration done:** `git rm -r --cached` the 4 repo clones (`anthropic--skills`, `anthropic--financial-services`, `garrytan--gstack`, `garrytan--gbrain`) — 3,144 files untracked, still present on disk. Article snapshots (`garrytan--*` essays, `anthropic--plugins-reference`) + all citation pages remain tracked.
- **New tooling:** `sources/repos.manifest.tsv` (slug + url + pinned commit, single source of truth) and `sources/clone-all.sh` (rebuilds clones on fresh checkout, pinned to the cited commit; `--pull` fetches without moving the pin). Rewrote `.gitignore` to ignore the 4 clone dirs (each future repo ingest adds its dir + a manifest row).
- **Citation safety:** because we cite specific line ranges, updating a repo is a **deliberate re-ingest** (pull → diff old→new SHA → fix affected anchors → bump manifest + citation page → log), never a silent sync. Documented in `CLAUDE.md` INGEST.
- Updated `CLAUDE.md` (layer 1, INGEST repo step + update flow, naming, anti-rule), `README.md` (working agreement #4 + fresh-checkout note).

## [2026-06-02] reflect | apply all 6 seeded self-improvements

- **Policy change (Sidney):** REFLECT no longer asks — grounded changes ship directly. Updated the REFLECT operation + INGEST step 9 in `CLAUDE.md` accordingly.
- **Applied all 6 candidates** from `meta/self-improvements.md`, each traced to a wiki pattern:
  1. `resolver-routing-table` → added a **Routing** table to `CLAUDE.md` Operations (request→operation, source type→schema/location).
  2. `complexity-ratchet` → INGEST closes with a `ratchet:` tally + LINT check #12.
  3. `diarization` → "judgment distillation, not transcription" note in all 4 page schemas.
  4. `latent-vs-deterministic-split` → tagged every INGEST step **(det)**/**(latent)** with a legend.
  5. `thin-harness-fat-skills` → LINT check #13 (harness bloat: how-to that belongs in a schema).
  6. `skill-pack-bundle` → `## Detection recipe` section added to `_schemas/pattern.md`.
- Marked all 6 ledger entries `applied`; resolved the open "auto vs on-demand" meta-question.
- Touched: `CLAUDE.md`, `_schemas/{skill,plugin,mcp-server,concept,pattern}.md`, `meta/self-improvements.md`, this log. ratchet: links +7 · orphans +0 · patterns +0 (self-application, no new artifacts).

## [2026-06-02] reflect | pass 2 — remaining patterns + fix stale legend

- Second REFLECT pass over the patterns the seed pass didn't cover:
  7. `skill-as-method-call` → documented operations as **parameterized calls** in `CLAUDE.md` Routing (`INGEST(<source>)`, `QUERY(<question>)`, …); templates noted as parameterized pages.
  8. `single-source-multi-surface-distribution` → anti-rule: pages are the single source, `DASHBOARD.html`/query deliverables/`llms.txt` are generated *surfaces*, never parallel copies.
  9. `marketplace-as-multi-plugin` → **embodied** already by `index.md`/`_index.md` (the registry of à-la-carte pages); recorded, no change.
- **Fixed a contradiction (LINT #7):** the ledger's status legend still called REFLECT "human-gated like LINT" — stale since the 2026-06-02 auto-apply policy. Reworded; added an `embodied` status.
- Confirmed the original 6 (seed pass) were already `applied` + pushed in `6d9be73`; no rework.
- Touched: `CLAUDE.md`, `meta/self-improvements.md`, this log. ratchet: links +4 · orphans +0 · patterns +0.

## [2026-06-02] reflect | pass 3 — deep review of the full Garry Tan corpus

- At Sidney's request, reviewed all the Garry Tan material (gstack + gbrain pages + all 8 essays, esp. #5 Skillify Manifesto and #6 Meta-Meta-Prompting — which credits Karpathy's LLM Wiki as gbrain's own origin) and added every candidate wiki-project improvement to `meta/self-improvements.md` (entries #10–#21).
- **Applied 5 small/safe items** (REFLECT ships): #10 routing-eval table (`CLAUDE.md` §Routing); #11 entity propagation in INGEST step 5; #12 LINT #15 check-resolvable/reachability; #13 LINT #16 DRY/overlap audit; #14 LINT #17 frustration/TODO backlog.
- **Recorded 7 bigger items as `proposed`:** #15 compiled-truth+timeline page schema (creator/concept), #16 per-page + wiki health score, #17 page "definition of done" checklist (belongs in `_schemas/`, not the harness), #18 local search tool (grep→qmd; gbrain retrieval), #19 LINT doctor/autopilot with `[AGENT]` cost guard, #20 multi-model cross-modal eval for analyses, #21 "skillify-the-wiki" process reflex (extends REFLECT).
- Each entry cites an in-wiki pattern or artifact (ledger anti-rule honored).
- Touched: `CLAUDE.md`, `meta/self-improvements.md`, this log. ratchet: links +12 · orphans +0 · patterns +0.

## [2026-06-02] reflect | skillify — apply the two remaining gaps (#17, #21)

- Mapped skillify onto the wiki: most of it was already built (REFLECT = "skills that build skills"; routing evals; LINT #15 check-resolvable; #16 DRY audit). Two gaps remained — closed both:
  - **#17 definition of done.** Created `_schemas/_definition-of-done.md` — an underscore-prefixed shared-rules file (gbrain's `_brain-filing-rules.md` convention) with per-page-type checklists (source/artifact/concept/pattern), the page analogue of the 10-step skillify list. Linked from all six schema headers (DRY — one gate, not copied). Grounds: [[patterns/quality-bar/skill-pack-bundle]].
  - **#21 skillify the verb.** Named **skillify** as a reflex in the REFLECT operation: a *repetition* trigger (3rd time you do an ad-hoc move → codify it as a schema/operation/Routing row/`(det)` script with a definition of done). Grounds: [[patterns/quality-bar/skill-pack-bundle]] + [[patterns/composition/resolver-routing-table]].
- Both ledger rows flipped proposed → applied. Remaining proposed: #15 timeline schema, #16 health score, #18 search tool, #19 doctor autopilot, #20 cross-modal eval.
- Touched: `_schemas/_definition-of-done.md` (new), `_schemas/{source,skill,plugin,mcp-server,concept,pattern}.md`, `CLAUDE.md`, `meta/self-improvements.md`, this log. ratchet: links +9 · orphans +0 · patterns +0.

## [2026-06-02] reflect | build the 5 remaining proposed items (#15, #16, #18, #19, #20)

- "Build it all" — shipped every remaining `proposed` ledger item; all 21 self-improvements now `applied`/`embodied`.
- **#18 `scripts/wiki-search.sh`** — grep-based search over git-tracked pages (auto-excludes ignored clones), grouped by page + title; `-s` includes sources, `-l` lists files. (`rg` isn't on PATH, so built on portable grep.)
- **#19 + #16 `scripts/wiki-doctor.py`** — the LINT autopilot: deterministic checks (broken links, orphans, missing sections, staleness, gitlinks, TODO backlog) + a 0–100 **health score** (target 90). `--json`/`--strict`/`--target`. Report-only by design. First run = **76/100**: caught 9 pattern pages predating the `## Detection recipe` requirement (real backlog) + fixed 2 of my own parser bugs (Obsidian `|alias`, and `[[...]]` inside code spans).
- **#15 compiled-truth + timeline** — added gbrain's brain-page shape to `creator.md`/`concept.md` schemas; retrofitted [[creators/garry-tan]] with the star/essay time-series (72K→105K; gbrain 5K→20K).
- **#20 `analyses/_eval-rubric.md`** — cross-modal (multi-model, different families) review gate for analyses; 5-dimension rubric + procedure.
- Wired tooling into `CLAUDE.md` (LINT → run doctor first; new `## Tooling` section; layout), `README.md`, `analyses/_index.md`.
- **Open backlog (doctor-surfaced):** 9 pattern pages need a `## Detection recipe` to reach the 90 health target. Not done here (each is careful per-pattern content work) — next focused pass.
- Touched ~14 files. ratchet: links +10 · orphans +0 · patterns +0.

## [2026-06-02] lint | backfill detection recipes → wiki health 100/100

- Closed the doctor's only finding: added a grounded `## Detection recipe` (look-for / confirm-with / rule-out) to all **9** original pattern pages that predated the requirement — `diarization`, `latent-vs-deterministic-split`, `skill-as-method-call`, `resolver-routing-table`, `single-source-multi-surface-distribution`, `complexity-ratchet`, `skill-pack-bundle`, `marketplace-as-multi-plugin`, `thin-harness-fat-skills`. Each recipe's foils are the page's own counter-examples (the negative test).
- Fixed 2 `wiki-doctor.py` parser bugs surfaced by its own first run: Obsidian `[[target|alias]]` links, and `[[...]]` examples inside code spans/fences (false-positive broken links).
- **`wiki-doctor.py` now reports 100/100** (76 pages; clean on broken links, orphans, sections, staleness, gitlinks). The ratchet loop worked end-to-end: schema requirement (#6) → doctor flagged the gap → backfilled → green.
- Committed scoped (the 9 pattern files + this log only) — `CLAUDE.md`, `README.md`, `index.md`, `meta/`, `_schemas/` left untouched (the compound-engineering agent is editing those concurrently).

## [2026-06-02] ingest | OpenAI Codex Goals (cookbook docs-page)

- Ingested [[sources/openai--using-goals-in-codex]] — OpenAI Cookbook guide *"Using Goals in Codex"* (authors Raj Pathak & Stefano Fabbri; published 2026-05-09). Captured **verbatim from the notebook source** (`openai/openai-cookbook`, `examples/codex/using_goals_in_codex.ipynb`, commit `9b4e627`) rather than the JS-rendered page; the 7 figures (base64 attachments, ~8 MB) left upstream-reconstructable per the lean-snapshot ethos, captions preserved. Classed `docs-page` but pinned to a commit. **First OpenAI source in the wiki.**
- **New pages:** [[concepts/completion-contract]] (the idea — an agent objective as a persistent, evidence-verified contract; "done" = evidence, not confidence); [[artifacts/projects/codex-goals]] (the runnable feature — `/goal` lifecycle, Codex ≥ 0.128.0; **first `projects/` artifact paged**); [[patterns/behavioral/evidence-gated-completion]] (new **proposed** pattern, 1 example); [[creators/openai]] (**first non-Anthropic / non-Garry creator**).
- **Promoted [[patterns/behavioral/skill-as-method-call]] → `confirmed`.** Codex `/goal`'s six-slot template is the *documented parameter signature from a non-Garry pack* that page named as its exact promotion gate — now 2 creators (Garry Tan + OpenAI) and 2 harnesses (Claude Code + Codex CLI). Research output, not bookkeeping.
- Indexes updated: `concepts/_index`, `artifacts/projects/_index`, `creators/_index`, `sources/_index` + root `index.md` (sources, creators, projects, concepts, patterns).
- **REFLECT (Pass 4, below in [[meta/self-improvements]]):** `completion-contract` maps onto our own `_schemas/_definition-of-done.md`, which lacks a *blocked stop condition* — added one (mark-the-gap / budget≠done / don't-fake-completion).
- *Concurrency note:* landed alongside an in-flight `compound-engineering` ingest (separate session) editing the same shared indexes; all edits here are additive (distinct rows/bullets). That ingest's own `index.md`/`README`/`log` bookkeeping was still pending as of this write.
- ratchet: links +~65 · orphans +0 · patterns +1 new (`evidence-gated-completion`) + 1 promoted (`skill-as-method-call` → confirmed).
