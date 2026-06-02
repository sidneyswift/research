# CLAUDE.md — AI & Agents Research Wiki

## Project purpose

Collect and analyze the most important and talked-about work across the AI and agent ecosystem — skills, plugins, MCP servers, **frontier projects/systems**, and the **essays, papers, and threads** explaining where the field is going — so we can identify the patterns, structures, and ingenuity that make them great, and eventually build our own.

**Scope:** broad and frontier-facing. Anything notable in AI/agents is in scope — Anthropic *and* OpenAI, Cursor, Google, open-source projects, individual builders, research labs. The unit of study is not "an Anthropic skill" but "a great idea, technique, or artifact in AI/agents, with evidence." We catalog *artifacts* (things you can run: skills, plugins, MCP servers, projects), *concepts* (ideas/techniques worth their own page), and *patterns* (recurring techniques observed across ≥2 artifacts).

This wiki is structured as an **LLM-maintained living wiki** in the [Karpathy "LLM Wiki" pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The deliverables are markdown pages, evidence snapshots in `sources/`, and synthesis writeups in `analyses/`. The LLM (you) is the maintainer — you can touch 15 cross-referenced files in one pass without getting bored, which is the *whole point* of doing this as a wiki rather than as a one-shot report.

## Three layers (the LLM wiki pattern)

1. **Raw sources** — evidence in `sources/`. Every source has a sibling **citation page** `sources/<creator>--<slug>.md` (always committed) plus its raw material, stored one of two ways:
   - **Repos** → kept as a **live local clone** `sources/<creator>--<slug>/` *with its `.git/` intact* so we can `git pull` upstream. Clones are **git-ignored from the wiki** (they're large and reconstructable) — only the citation page is committed. Each repo is listed in `sources/repos.manifest.tsv` (slug + url + pinned commit); `sources/clone-all.sh` rebuilds the clones on a fresh checkout, pinned to the cited commit. We cite a *specific commit*, so the working tree may advance but every claim is anchored to a known SHA.
   - **Articles / papers / docs-pages** → captured to `sources/<creator>--<slug>/snapshot.md` (+ assets). These **are committed** — they're immutable evidence with no upstream to clone (often pasted or web-captured text we can't reliably re-fetch). Never edit a captured snapshot.
   Read sources as read-only evidence; the analysis lives in the wiki layer, not here.
2. **Wiki layer (mutable, LLM-maintained)** — `artifacts/`, `concepts/`, `patterns/`, `creators/`, `analyses/`, plus the indexes and `log.md`. This is where ingest writes, query refines, and lint cleans.
3. **Schema (config)** — this file (`CLAUDE.md`), `_schemas/` page templates, and `index.md` (the master catalog). Defines wiki structure and operations.

## Operations

Every interaction with this wiki is one of four operations. Be explicit about which one you're performing. Three are Karpathy's (Ingest / Query / Lint); the fourth, **Reflect**, exists because this wiki studies how to build great agents/skills — so it must turn that knowledge on *itself*.

### 1. INGEST — adding new knowledge

Triggered when adding a new source (and the artifact / concept / pattern it yields). The full ritual:

1. **Snapshot the source** into `sources/<creator>--<slug>/` — branch by source type:
   - **Repo** → `cd sources && git clone <url> <creator>--<slug>` then `cd <creator>--<slug> && git rev-parse HEAD` (capture the SHA) `&& git log -1 --format="%ci"` (capture the date). **Keep `.git/`** — the clone stays live so we can `git pull` later. Then make it a local-only evidence clone: add `sources/<creator>--<slug>/` to `.gitignore` and a row (`slug url commit`) to `sources/repos.manifest.tsv`. The clone is never committed; only its citation page is.
   - **Article / essay / blog post / forum thread** → save the rendered text to `sources/<creator>--<slug>/snapshot.md`; download referenced images alongside if they carry meaning. There's no commit SHA — record the canonical URL + publish date (or "n/a (living page)" for docs that change). This snapshot **is committed** — it's immutable evidence; never edit it after capture.
   - **Paper** → save the PDF (or its extracted text) into the snapshot dir; committed like an article. Record title, authors, venue/arXiv id, and date.
   - **Docs-page** → snapshot to `snapshot.md` like an article (committed); mark it `n/a (living page)` since it changes upstream.
2. **Create the citation page** at `sources/<creator>--<slug>.md` (sibling to the snapshot dir) using `_schemas/source.md`. Frontmatter (`type:` = `repo` / `article` / `paper` / `docs-page`), retrieval date, version stamp (commit SHA *or* publish date), popularity/credibility signals captured *at retrieval date*, and the `## Anchor map`.
3. **Create the right wiki page(s).** A source yields one or more of:
   - **Artifact page** (something you can run) → `artifacts/{skills,plugins,mcp-servers,projects}/` using the matching `_schemas/` template. Fill `## Attributes` and `## Relationships`.
   - **Concept page** (an idea/technique worth tracking, common for essays & papers) → `concepts/` using `_schemas/concept.md`.
   Every non-trivial claim links to `[[sources/<creator>--<slug>#anchor]]`.
4. **Extract patterns in the same session.** End each artifact/concept page with `## Patterns demonstrated`. Link to existing `patterns/...` pages where the source uses a known pattern. If you see a new pattern, create the pattern page now — but mark it `status: proposed` until ≥2 examples exist. Don't defer; deferred extraction never happens.
5. **Update the creator page** with the new artifact/concept under `## Artifacts produced` (create the creator page if new).
6. **Update domain `_index.md`** to promote the new page out of the candidate list.
7. **Update `index.md`** (root) — add a row in the appropriate section.
8. **Append to `log.md`** — `## [YYYY-MM-DD] ingest | <subject>` with a 1-line note on what was added.
9. **Reflect (quick pass).** Before closing the session, ask: *did anything I just learned apply to this wiki's own machinery?* A new pattern about how great skills/agents are built is also a candidate improvement to our `CLAUDE.md`, schemas, indexes, or tooling. If yes, add a candidate to `meta/self-improvements.md` (don't apply it silently — see the REFLECT operation). This step is why we ingest in the first place: the research is supposed to change how we work.

Karpathy estimates ingesting one source touches ~10–15 pages. For us it's been ~7–10. Don't shortcut this — the cross-links are the whole product.

**Updating a repo source (deliberate re-ingest).** Because we cite *specific line ranges*, a `git pull` can silently break citations — so updating is a reviewed operation, never a background sync:
1. `git -C sources/<slug> pull` (or `clone-all.sh --pull` then check out the new HEAD).
2. `git -C sources/<slug> diff <old-sha> HEAD` — read what changed.
3. Update any wiki claims/anchors the diff affected; re-verify every citation into that source still points where we said.
4. Bump the commit in `sources/repos.manifest.tsv` and on the citation page; refresh its `as-of` popularity signals.
5. Log it — `## [YYYY-MM-DD] ingest | <slug> (update <old-sha>→<new-sha>)`.

### 2. QUERY — using the wiki to answer something

Triggered when the user (or you) need to look something up *or* draw a comparison across artifacts. The discipline:

1. **Start in the wiki**, not in the source clones. The wiki is where the analysis lives; sources are evidence. If you find yourself reading source files first, stop and check whether the wiki already covers the question.
2. **If the answer is missing from the wiki**, you found a gap. File the finding back into the wiki: extend an existing page, write a new concept page, propose a new pattern, or note an open question on the relevant page. Don't answer the user from sources without also writing it down. The answer's *delivery* format can vary (a comparison table, a chart, a Marp deck, a canvas) — but the durable version belongs in the wiki, not just in chat.
3. **Follow citations.** Every claim links to a source — read the cited section, don't assume the wiki is up to date.
4. **Verify before recommending.** Memory and wiki pages decay. If the user is about to act on a recommendation, confirm the cited source still says what we claimed.
5. **Log the query if it surfaced something durable.** Append `## [YYYY-MM-DD] query | <topic>` to `log.md` when a query produced a finding worth coming back to.

### 3. LINT — periodic health check

Triggered explicitly (user asks "lint the wiki" or "check for staleness") or after a large batch of ingests. **This is the operation that makes the wiki actually durable** — without it, the wiki ages the same way human wikis do.

What to check, in order:

1. **Broken wikilinks.** Every `[[...]]` should resolve to a file that exists. Especially watch for: links to source anchors that aren't in the source's `## Anchor map` (those are *de facto* broken even if the file exists).
2. **Orphan pages.** Pages no other page links to. Often a sign of an aborted ingest. Either link them in or move them to `scratch/`.
3. **Missing required sections.** Every artifact page must have `## Patterns demonstrated` and `## What we'd steal`. Every pattern page must have `## Counter-examples or anti-pattern` and ≥2 `## Examples in this wiki` entries (else status should be `proposed`).
4. **Stale popularity signals.** `as-of:` dates older than 30 days on `popularity-signals` blocks. These decay fast — re-check or mark `(stale)`.
5. **Stale `last-reviewed:` dates.** Anything older than 90 days on a page that hasn't been touched.
6. **Promoted-but-unconfirmed patterns.** Pattern pages with `status: confirmed` but fewer than 2 listed examples.
7. **Contradictions.** Two pages making opposing factual claims about the same thing. Hard to catch automatically; flag candidates for human review. (Newer sources often *supersede* older claims — note which wins and why.)
8. **Missing log entries.** Recent additions to `index.md` or `_index.md` files that don't appear in `log.md`.
9. **Concepts mentioned but page-less.** A concept/technique referenced across multiple pages but with no `concepts/` page of its own deserves one. (Karpathy: "important concepts mentioned but lacking their own page.")
10. **Web-fillable data gaps.** Claims hedged with "unknown," "TBD," or a stale signal that a quick web search could resolve. Flag these as ingest candidates rather than guessing.
11. **New questions and sources to chase.** Lint isn't only cleanup — propose the next questions worth investigating and the next sources worth ingesting. This is where the wiki tells you what to read next.

Lint produces a report — list each finding with file path and a one-line fix suggestion. Don't auto-fix without confirmation; some "stale" signals are intentional.

### 4. REFLECT — turn the wiki's learnings on itself

**The whole point of researching how to build great agents/skills is to build them — starting with this wiki.** This wiki *is* an LLM-maintained agent/skill system: `CLAUDE.md` is its harness, the `_schemas/` are its skill definitions, the operations are its routing table, `index.md`/`log.md` are its memory. So every pattern we confirm is a candidate upgrade to our own machinery. Without this operation, we'd catalog brilliant techniques and never use them — exactly the failure that prompted adding it.

Triggered after an ingest (quick pass, INGEST step 9), after a lint, or on demand ("reflect on the wiki"). The discipline:

1. **Scan recent learnings.** Look at patterns/concepts added or confirmed since the last reflect (use `log.md`).
2. **Map each onto the wiki itself.** Ask, concretely: does this technique apply to `CLAUDE.md`, the `_schemas/`, the index/log, the (future) dashboard, or our tooling? A pattern about skills usually *does* — because the wiki is built from the same primitives.
3. **Write a grounded proposal**, not a vibe. Each goes in `meta/self-improvements.md`: which pattern (cite the `[[patterns/...]]` page), how it maps to our machinery, the specific change, and expected benefit. Same anti-rule as everywhere: no improvements from generic knowledge — they must trace to a pattern *observed in this wiki*.
4. **Human-gated, like lint.** Propose; don't silently rewrite the schema. Apply on confirmation, then mark the ledger entry `applied` and log it.
5. **Log it** — `## [YYYY-MM-DD] reflect | <subject>`.

The ledger at `meta/self-improvements.md` is the durable record so we don't re-propose the same thing and can see how the wiki's own design traces back to the research.

## Anti-rules (cut across all operations)

- **Never** write a pattern or concept page from generic knowledge. Pages must be grounded in observed sources *in this wiki* with citations.
- **Never** claim "popular" or "important" without a signal: install/star count + date, marketplace position + date, named person quoted + date, paper citations/venue + date. "Talked about" is a signal too — quote the talk.
- **Never** treat an artifact or concept page as complete without `## Patterns demonstrated` and `## What we'd steal`. The latter is the whole point — the research is for *us*.
- **Never** let `## What we'd steal` become a lossy filter. Capture *everything* portable, even minor choices — ★-mark the best to keep a priority signal, but don't pre-curate down to a top-3. A thin steal list silently narrows our attention over time and discards ideas we can't get back. When *mining* the wiki for ideas, read whole pages + `## Patterns demonstrated`, never just the steal sections.
- **Never** hand-edit source material in `sources/`. Repo clones change *only* via `git pull` as a deliberate re-ingest (bump the manifest + recheck citations); captured article/paper snapshots never change at all. It's evidence, not a draft.
- **Never** invent wikilink anchors. Source pages have an `## Anchor map` section; citations must use anchors registered there.

## Layout

```
Research/
├── CLAUDE.md          # this file — schema + operations
├── README.md          # human entry point
├── index.md           # master catalog (single front door — Karpathy pattern)
├── log.md             # append-only chronicle (Karpathy pattern)
├── DASHBOARD.html     # (later) tabbed overview, after ≥10 artifacts
├── _schemas/          # page templates — use these, don't invent
├── artifacts/         # things you can run
│   ├── skills/        # individual skills
│   ├── plugins/       # plugins (collections of skills + commands + agents + hooks + MCP)
│   ├── mcp-servers/   # MCP servers as a separate axis
│   └── projects/      # frontier projects/systems/products that aren't a single skill/plugin/MCP
├── concepts/          # ideas & techniques worth their own page (esp. from essays & papers)
├── patterns/          # recurring techniques across ≥2 artifacts (the actual research output)
│   ├── structural/    # how artifacts are organized
│   ├── behavioral/    # how artifacts steer the model
│   ├── composition/   # how artifacts call other artifacts
│   └── quality-bar/   # what separates great from mediocre
├── creators/          # people, orgs, and labs behind the work — context
├── sources/           # cloned repos + snapshotted articles/papers/pages + their .md citation pages
├── analyses/          # synthesis pieces — wait until ≥5 artifacts/concepts of relevant type
└── meta/              # the wiki applied to itself — self-improvements.md ledger (see REFLECT)
```

**Artifact vs. concept vs. pattern** — the call that trips people up:
- **Artifact** = a concrete thing you could run or install (a skill, a plugin, an MCP server, a named project/system).
- **Concept** = an idea or technique discussed in a source but not itself runnable (e.g. "context engineering," "the bitter lesson"). Essays and papers usually yield concepts, not artifacts.
- **Pattern** = a recurring technique we've observed across **≥2 artifacts** in this wiki. Promote a concept/proposed-pattern to a confirmed `patterns/` page only when the second example lands.

## Naming conventions

- **Filenames**: kebab-case. Artifact pages match the artifact's own name verbatim (`skill-creator.md`, not `skill_creator.md`).
- **Source storage**: each source is a directory `sources/<creator>--<slug>/` (a live git-ignored clone listed in `repos.manifest.tsv`, *or* a committed `snapshot.md` + assets for an article/paper/page) plus a sibling citation page `sources/<creator>--<slug>.md` (always committed). Use `--` as the creator/slug separator.
- **Citation anchors**: `[[sources/<creator>--<slug>#anchor-name]]` where `anchor-name` is registered in the source page's `## Anchor map`.
- **Dates**: ISO format (`2026-05-21`). Convert any relative dates ("yesterday") to absolute before writing.
- **`log.md` is grep-able**: every entry starts with `## [YYYY-MM-DD] <op> | <subject>`, so `grep "^## \[" log.md | tail -5` shows recent activity (Karpathy's tip).

## Dashboard (not yet built)

Once we have ≥10 artifacts cataloged, build `DASHBOARD.html` at the project root with tabs: Overview · Artifacts · Patterns · Creators · Sources. Mirror the Flex Seal second-brain dashboard pattern.

## Status

See `README.md` for current ingestion counts and `log.md` for the chronological record.
