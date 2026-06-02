# Agent Skills & Plugins Research

A research wiki cataloging the most popular and talked-about skills and plugins in the Anthropic agent ecosystem — Claude Code skills/plugins, Claude.ai Skills, MCP servers — to understand what makes them great so we can build our own.

**Scope (decided 2026-05-21):** Anthropic ecosystem only. Claude Code skills + plugins, general Claude.ai Skills, and MCP servers. Cross-platform tooling (Cursor, OpenAI Agents, etc.) is out of scope for this pass.

**Output format:** Wiki-style knowledge base. Same shape as the Flex Seal second-brain — typed entity pages with `domain:` + `type:` frontmatter, `## Attributes` + `## Relationships` sections, source citations via `[[sources/...#anchor]]`.

**Collection mode:** Curated. Sidney provides candidate artifacts; we deep-dive each one and extract patterns as we go.

## Start here

- **For everyone — master catalog:** [index.md](index.md) — single front door listing every page.
- **For agents (LLM sessions):** read [CLAUDE.md](CLAUDE.md) before any operation. It defines the three operations (Ingest / Query / Lint) per [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
- **For "what was done when":** [log.md](log.md) — append-only chronological record.
- **For browsing patterns:** [patterns/](patterns/) — the research output. What separates great artifacts from the rest.
- **For browsing artifacts:** [artifacts/skills/](artifacts/skills/), [artifacts/plugins/](artifacts/plugins/), [artifacts/mcp-servers/](artifacts/mcp-servers/).
- **For evidence:** [sources/](sources/) — every claim in the wiki points here.

## Status

| Domain | Count | Last updated |
|---|---|---|
| Skills cataloged | 0 paged (candidate queue: 17+ from anthropic-skills, ~55 from financial-services, dozens in gstack/gbrain) | 2026-06-01 |
| Plugins cataloged | 4 — `anthropic-skills-marketplace`, `gstack`, `gbrain` (speedrun) + `anthropic-financial-services-marketplace` (full) | 2026-06-01 |
| MCP servers cataloged | 0 paged (12 FSI data connectors + 1 gbrain server referenced; queued) | 2026-06-01 |
| Patterns extracted | **5 confirmed** (`single-source-multi-surface-distribution`, `marketplace-as-multi-plugin`, `skill-pack-bundle`, `resolver-routing-table`, `latent-vs-deterministic-split`) + **4 proposed-with-pages** (`thin-harness-fat-skills`, `skill-as-method-call`, `diarization`, `complexity-ratchet`); ~17 proposed bullets | 2026-06-01 |
| Creators cataloged | 2 — Anthropic, Garry Tan | 2026-06-01 |
| Source repos snapshotted | 4 repos (~126 MB) + 1 docs-page + **8 essays** (Garry Tan's "AI Explainer" series, `garrytan--*`) | 2026-06-01 |

(Update this table after each ingestion.)

## Working agreements

1. **Every claim cites a source.** No exceptions, no "everyone knows."
2. **Patterns require ≥2 artifact examples.** One example is a coincidence.
3. **"What we'd steal" is mandatory** on every artifact page — the research is for *us*.
4. **Sources are cloned, not linked.** Snapshots beat URLs.
5. **Every ingest gets a log entry.** Append to `log.md` — `## [YYYY-MM-DD] ingest | <subject>` plus 1–3 bullets. Future-you needs this.
6. **Lint periodically.** Karpathy's whole point: the LLM is the maintainer. Run a Lint pass after every batch of ingests and on demand.
