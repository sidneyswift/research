# AI & Agents Research

A research wiki cataloging the most important and talked-about work across the AI and agent ecosystem — skills, plugins, MCP servers, frontier projects/systems, and the essays, papers, and threads explaining where the field is going — to understand what makes them great so we can build our own.

**Scope (broadened 2026-06-01):** frontier-facing and cross-platform. Anthropic *and* OpenAI, Cursor, Google, open-source projects, individual builders, and research labs are all in scope. We catalog **artifacts** (runnable things), **concepts** (ideas/techniques worth a page), and **patterns** (techniques recurring across ≥2 artifacts). *Originally (2026-05-21) scoped to the Anthropic ecosystem only; widened once the Garry Tan essay ingests showed the research naturally spans the whole frontier.*

**Output format:** Wiki-style knowledge base. Same shape as the Flex Seal second-brain — typed entity pages with `domain:` + `type:` frontmatter, `## Attributes` + `## Relationships` sections, source citations via `[[sources/...#anchor]]`.

**Collection mode:** Curated. Sidney provides candidate artifacts; we deep-dive each one and extract patterns as we go.

## Start here

- **For everyone — master catalog:** [index.md](index.md) — single front door listing every page.
- **For agents (LLM sessions):** read [CLAUDE.md](CLAUDE.md) before any operation. It defines the four operations (Ingest / Query / Lint / Reflect) per [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
- **For agents mining the wiki from another project (to build something):** start at [for-builders.md](for-builders.md) — the consumer front door, with a build-intent→pages routing table, an extraction protocol, and a copy-paste prompt.
- **For "what was done when":** [log.md](log.md) — append-only chronological record.
- **For browsing patterns:** [patterns/](patterns/) — the research output. What separates great artifacts from the rest.
- **For browsing artifacts:** [artifacts/skills/](artifacts/skills/), [artifacts/plugins/](artifacts/plugins/), [artifacts/mcp-servers/](artifacts/mcp-servers/), [artifacts/projects/](artifacts/projects/).
- **For browsing concepts:** [concepts/](concepts/) — ideas and techniques (often from essays & papers) that aren't runnable artifacts.
- **For evidence:** [sources/](sources/) — every claim in the wiki points here.
- **For tooling:** [scripts/](scripts/) — `wiki-search.sh` (search), `wiki-doctor.py` (health check + score). Run `python3 scripts/wiki-doctor.py` anytime to see wiki health.

## Status

| Domain | Count | Last updated |
| --- | --- | --- |
| Skills cataloged | 0 paged (candidate queue: 17+ from anthropic-skills, ~55 from financial-services, dozens in gstack/gbrain) | 2026-06-01 |
| Plugins cataloged | 5 — `anthropic-skills-marketplace`, `gstack`, `gbrain`, `anthropic-financial-services-marketplace`, `compound-engineering` | 2026-06-02 |
| Projects cataloged | 1 — `codex-goals` (OpenAI Codex Goals feature) | 2026-06-02 |
| MCP servers cataloged | 0 paged (12 FSI data connectors + 1 gbrain server referenced; queued) | 2026-06-01 |
| Concepts cataloged | 4 — `compound-engineering`, `completion-contract`, `convergent-agent-plugin-spec`, `ai-search-as-parallel-discovery-layer` | 2026-06-02 |
| Patterns extracted | **8 confirmed** + 3 proposed-with-pages (`thin-harness-fat-skills`, `diarization`, `evidence-gated-completion`); ~20 proposed bullets — see [Patterns](index.md#patterns) | 2026-06-02 |
| Creators cataloged | 5 — Anthropic, Garry Tan, Every, OpenAI, Ahrefs | 2026-06-02 |
| Sources snapshotted | 5 repos (~137 MB) + 3 docs-pages + 9 articles (incl. Garry Tan's 8-essay "AI Explainer" series) + 1 tweet | 2026-06-02 |

(Update this table after each ingestion.)

## Working agreements

1. **Every claim cites a source.** No exceptions, no "everyone knows."
2. **Patterns require ≥2 artifact examples.** One example is a coincidence.
3. **"What we'd steal" is an exhaustive ledger** on every artifact/concept page — capture *everything* portable (★-mark the best), never a curated top-3. A thin list narrows our attention over time.
4. **Sources are cloned, not linked.** Repos are kept as live local clones (git-ignored, re-clonable via [sources/clone-all.sh](sources/clone-all.sh) from [sources/repos.manifest.tsv](sources/repos.manifest.tsv), pinned to the cited commit); captured articles/papers are committed snapshots. Either way we point at evidence, never a bare URL. **On a fresh checkout, run `sources/clone-all.sh` to rebuild the repo evidence cache.**
5. **Every ingest gets a log entry.** Append to `log.md` — `## [YYYY-MM-DD] ingest | <subject>` plus 1–3 bullets. Future-you needs this.
6. **Lint periodically.** Karpathy's whole point: the LLM is the maintainer. Run a Lint pass after every batch of ingests and on demand.
7. **Reflect, don't just collect.** This wiki researches how to build great agents/skills — so it must improve *itself* with what it learns. After ingests, ask whether new patterns apply to our own machinery and log candidates in [meta/self-improvements.md](meta/self-improvements.md).
