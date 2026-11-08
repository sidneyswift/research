# AI & Agents Research

A research wiki cataloging the most important and talked-about work across the AI and agent ecosystem — skills, plugins, MCP servers, frontier projects/systems, and the essays, papers, and threads explaining where the field is going — to understand what makes them great so we can build our own.

**Scope (broadened 2026-06-01):** frontier-facing and cross-platform. Anthropic *and* OpenAI, Cursor, Google, open-source projects, individual builders, and research labs are all in scope. We catalog **artifacts** (runnable things), **concepts** (ideas/techniques worth a page), and **patterns** (techniques recurring across ≥2 artifacts). *Originally (2026-05-21) scoped to the Anthropic ecosystem only; widened once the Garry Tan essay ingests showed the research naturally spans the whole frontier.*

**Output format:** Wiki-style knowledge base — typed entity pages with `domain:` + `type:` frontmatter, `## Attributes` + `## Relationships` sections, source citations via `[[sources/...#anchor]]`.

**Collection mode:** Curated. Sidney provides candidate artifacts; we deep-dive each one and extract patterns as we go.

## Shared across projects

Canonical local home: `Projects/Research`. This repository supports research across Sidney, Flex, Recoup, and other projects. Source code lives in ignored clones under `sources/`; the manifest records exactly how to restore it.

```bash
git clone https://github.com/sidneyswift/research.git Research
cd Research
./setup.sh
```

Requires Git, Python 3, network access, and any credentials needed by private source repositories. For selective downloads and storage rules, see [remote-setup.md](remote-setup.md).

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

## Internal builds

See [[projects/_index]] for projects created from the research, starting with [[projects/conversation-learning/README]]. These design projects are separate from the external artifact counts below.

## Status

| Domain | Count | Inventory checked |
| --- | --- | --- |
| Skills cataloged | 6 paged | 2026-11-06 |
| Plugins cataloged | 10 | 2026-11-04 |
| Projects cataloged | 32 | 2026-11-07 |
| MCP servers cataloged | 0 paged | 2026-11-04 |
| Concepts cataloged | 33 | 2026-11-08 |
| Patterns extracted | 11 confirmed + 8 proposed with pages | 2026-11-04 |
| Creators cataloged | 72 | 2026-11-08 |
| Source citation pages | 109: 26 article, 47 docs-page, 5 other, 6 paper, 24 repo, 1 tweet | 2026-11-08 |

Consolidated research includes [[artifacts/projects/shopify-api]], [[analyses/frontier-and-business-api-design]], [[projects/conversation-learning/README]] and the newer upstream studies through [[artifacts/projects/superplane]]. Analyses retain their existing draft/review status.

Latest MCP ingest: [[concepts/model-context-protocol]], [[concepts/mcp-extension-architecture]], [[artifacts/projects/mcp-apps]], [[artifacts/projects/openai-mcp-extensions]], [[concepts/mcp-enterprise-managed-authorization]] and [[concepts/skills-over-mcp]]. The synthesis [[analyses/mcp-and-extensions]] remains draft pending cross-family review. Counts describe existing wiki pages, including prior local drafts; inventory does not refresh older source claims or popularity signals.

(Update this table after each ingestion.)

## Working agreements

1. **Every claim cites a source.** No exceptions, no "everyone knows."
2. **Patterns require ≥2 artifact examples.** One example is a coincidence.
3. **"What we'd steal" is an exhaustive ledger** on every artifact/concept page — capture *everything* portable (★-mark the best), never a curated top-3. A thin list narrows our attention over time.
4. **Sources are cloned, not linked.** Repos are kept as live local clones (git-ignored, re-clonable via [sources/clone-all.sh](sources/clone-all.sh) from [sources/repos.manifest.tsv](sources/repos.manifest.tsv), pinned to the cited commit); captured articles/papers are normally committed snapshots. Full-paper redistribution exceptions retain local evidence plus tracked version pins, hashes and restoration notes (see [Skill++ evidence](sources/zhang--skill-plus-plus/README.md)). Either way we point at evidence, never a bare URL. **On a fresh checkout, run `sources/clone-all.sh` to rebuild the repo evidence cache.**
5. **Every ingest gets a log entry.** Append to `log.md` — `## [YYYY-MM-DD] ingest | <subject>` plus 1–3 bullets. Future-you needs this.
6. **Lint periodically.** Karpathy's whole point: the LLM is the maintainer. Run a Lint pass after every batch of ingests and on demand.
7. **Reflect, don't just collect.** This wiki researches how to build great agents/skills — so it must improve *itself* with what it learns. After ingests, ask whether new patterns apply to our own machinery and log candidates in [meta/self-improvements.md](meta/self-improvements.md).

Latest documentation research: [[projects/writing-amazing-developer-docs/README]] → [[concepts/developer-documentation-design]], with practical [[projects/writing-amazing-developer-docs/page-blueprints]].

Wider documentation research now includes [[projects/writing-amazing-developer-docs/platform-documentation-system]] and an [[projects/writing-amazing-developer-docs/experiments/README|executed synthetic documentation-test probe]].

Mintlify investigation: [[artifacts/projects/mintlify]] — current docs, first-party research and pinned URL-benchmark source/data; evidence limits explicit.

Frontier agent-documentation follow-up: [[concepts/agent-documentation-interfaces]] — Context7, Fern, ReadMe, WebMCP, Dokimi and three independent API-agent papers; documentation/specification investigation, no runtime integration.

Latest skill ingest: [[artifacts/skills/security-audit]] — 48 evidence/coverage/review principles, full source pinned locally, and 65 bundled validator tests passed. This is not a completed target audit or detection benchmark.

Latest concept ingest: [[concepts/proactive-agent-discernment]] — 32 principles from three Rubric field guides, 18 evidence files preserved. Distinguishes wake, authorized work and interruption; no live policy or automation changed.

Latest project ingest: [[artifacts/projects/inkling-2-small]] — 44 adaptation/evaluation/containment principles, 25 preserved evidence files. Hosted access and promised weights kept separate; no model training or benchmark replication.

Latest project investigation: [[artifacts/projects/t3code]] —79 source-backed service, runtime, authority, review, context and engineering practices; full SHA and restore manifest, selected tests inspected rather than executed.
