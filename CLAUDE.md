# CLAUDE.md — Agent Skills & Plugins Research Wiki

## Project purpose

Collect and analyze the most popular and talked-about skills and plugins in the Anthropic agent ecosystem (Claude Code skills/plugins, Claude.ai Skills, MCP servers) so we can identify the patterns, structures, and ingenuity that make them great — eventually building our own.

This wiki is structured as an **LLM-maintained living wiki** in the [Karpathy "LLM Wiki" pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The deliverables are markdown pages, evidence snapshots in `sources/`, and synthesis writeups in `analyses/`. The LLM (you) is the maintainer — you can touch 15 cross-referenced files in one pass without getting bored, which is the *whole point* of doing this as a wiki rather than as a one-shot report.

## Three layers (the LLM wiki pattern)

1. **Raw sources (immutable)** — `sources/<creator>--<repo>/` cloned snapshots with `.git/` stripped. Treat as read-only evidence. Never edit. Re-clone if upstream changed and we need a fresh snapshot.
2. **Wiki layer (mutable, LLM-maintained)** — `artifacts/`, `patterns/`, `creators/`, `analyses/`, plus the indexes and `log.md`. This is where ingest writes, query refines, and lint cleans.
3. **Schema (config)** — this file (`CLAUDE.md`), `_schemas/` page templates, and `index.md` (the master catalog). Defines wiki structure and operations.

## Three operations

Every interaction with this wiki is one of three operations. Be explicit about which one you're performing.

### 1. INGEST — adding new knowledge

Triggered when adding a new artifact, source, creator, or pattern. The full ritual:

1. **Clone the source.** `cd sources && git clone --depth 1 <url> <creator>--<repo>` then `cd <creator>--<repo> && git rev-parse HEAD` (capture the SHA) `&& git log -1 --format="%ci"` (capture the date) `&& rm -rf .git`. Snapshots are immutable; we record the commit so we know which version we cited.
2. **Create the source page** at `sources/<creator>--<repo>.md` using `_schemas/source.md`. Frontmatter (`type: repo`), retrieval date, upstream commit SHA, popularity signals captured *at retrieval date*, and the anchor map.
3. **Create the artifact page** in the right domain dir using the right `_schemas/` template (skill / plugin / mcp-server). Fill `## Attributes` and `## Relationships`. Every non-trivial claim links to `[[sources/<creator>--<repo>#anchor]]`.
4. **Extract patterns in the same session.** End the artifact page with `## Patterns demonstrated`. Link to existing `patterns/...` pages where the artifact uses a known pattern. If you see a new pattern, create the pattern page now — but mark it `status: proposed` until ≥2 artifact examples exist. Don't defer; deferred extraction never happens.
5. **Update the creator page** with the new artifact under `## Artifacts produced`.
6. **Update domain `_index.md`** to promote the artifact out of the candidate list.
7. **Update `index.md`** (root) — add a row in the appropriate section.
8. **Append to `log.md`** — `## [YYYY-MM-DD] ingest | <artifact-name>` with a 1-line note on what was added.

Karpathy estimates ingesting one source touches ~10–15 pages. For us it's been ~7–10. Don't shortcut this — the cross-links are the whole product.

### 2. QUERY — using the wiki to answer something

Triggered when the user (or you) need to look something up *or* draw a comparison across artifacts. The discipline:

1. **Start in the wiki**, not in the source clones. The wiki is where the analysis lives; sources are evidence. If you find yourself reading source files first, stop and check whether the wiki already covers the question.
2. **If the answer is missing from the wiki**, you found a gap. File the finding back into the wiki: extend an existing page, propose a new pattern, or note an open question on the relevant page. Don't answer the user from sources without also writing it down.
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
7. **Contradictions.** Two artifact pages making opposing factual claims about the same thing. Hard to catch automatically; flag candidates for human review.
8. **Missing log entries.** Recent additions to `index.md` or `_index.md` files that don't appear in `log.md`.

Lint produces a report — list each finding with file path and a one-line fix suggestion. Don't auto-fix without confirmation; some "stale" signals are intentional.

## Anti-rules (cut across all operations)

- **Never** write a pattern page from generic knowledge. Patterns must be grounded in observed artifacts *in this wiki* with citations.
- **Never** claim "popular" without a signal: install count + date, GitHub stars + date, marketplace position + date, named person quoted + date. "Talked about" is a signal too — quote the talk.
- **Never** treat an artifact page as complete without `## Patterns demonstrated` and `## What we'd steal`. The latter is the whole point — the research is for *us*.
- **Never** edit files in `sources/<creator>--<repo>/` (the snapshots). They're immutable evidence.
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
├── artifacts/         # the things being studied
│   ├── skills/        # individual skills
│   ├── plugins/       # plugins (collections of skills + commands + agents + hooks + MCP)
│   └── mcp-servers/   # MCP servers as a separate axis
├── patterns/          # recurring techniques (the actual research output)
│   ├── structural/    # how artifacts are organized
│   ├── behavioral/    # how artifacts steer the model
│   ├── composition/   # how artifacts call other artifacts
│   └── quality-bar/   # what separates great from mediocre
├── creators/          # Anthropic, individuals, orgs — context
├── sources/           # cloned repos + snapshotted articles + their .md citation pages
└── analyses/          # synthesis pieces — wait until ≥5 artifacts of relevant type
```

## Naming conventions

- **Filenames**: kebab-case. Artifact pages match the artifact's own name verbatim (`skill-creator.md`, not `skill_creator.md`).
- **Source clones**: `sources/<creator>--<repo>/` (use `--` as the separator).
- **Citation anchors**: `[[sources/<creator>--<repo>#anchor-name]]` where `anchor-name` is registered in the source page's `## Anchor map`.
- **Dates**: ISO format (`2026-05-21`). Convert any relative dates ("yesterday") to absolute before writing.

## Dashboard (not yet built)

Once we have ≥10 artifacts cataloged, build `DASHBOARD.html` at the project root with tabs: Overview · Artifacts · Patterns · Creators · Sources. Mirror the Flex Seal second-brain dashboard pattern.

## Status

See `README.md` for current ingestion counts and `log.md` for the chronological record.
