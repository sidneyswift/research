---
domain: sources
type: repo
url: https://github.com/garrytan/gbrain
retrieved: 2026-05-21
snapshot-location: sources/garrytan--gbrain/
upstream-commit: 1580c6d1ca8cfcfc1add72708dbf76bb40b1078c
upstream-commit-date: 2026-05-20
last-reviewed: 2026-05-21
license: MIT
version-at-snapshot: 0.36.4.0
---

# gbrain (`garrytan/gbrain`)

> Garry Tan's AI agent memory system. CLI + MCP server + 43-skill "skillpack" scaffold for OpenClaw/Hermes/etc. Hybrid vector + graph search with auto-extracting typed knowledge graph. Bills itself as "the production brain behind Garry's OpenClaw and Hermes deployments — 17,888 pages, 4,383 people, 723 companies, 21 cron jobs."

## Snapshot details

- **Retrieved**: 2026-05-21
- **Location**: `sources/garrytan--gbrain/` (71 MB, `.git/` stripped)
- **Upstream URL**: https://github.com/garrytan/gbrain
- **Upstream commit**: `1580c6d` (2026-05-20)
- **Version at snapshot**: 0.36.4.0 (from `VERSION` file)
- **Released**: April 5, 2026 per Vectorize.io coverage

## Anchor map

### Root docs (very large — most are citation-worthy)
- `#root` — repo as a whole
- `#README` — `README.md` (15 KB) — pitch, install, three install modes
- `#AGENTS.md` — `AGENTS.md` (7 KB) — install + operating protocol *for AI agents* (not humans). Mandatory pre-install read for any agent.
- `#CLAUDE.md` — `CLAUDE.md` (342 KB!) — architecture reference. Massive.
- `#INSTALL_FOR_AGENTS.md` — `INSTALL_FOR_AGENTS.md` (12 KB) — the 9-step agent install flow
- `#CHANGELOG.md` — `CHANGELOG.md` (1.1 MB!)
- `#TODOS.md` — `TODOS.md` (155 KB)
- `#DESIGN.md`, `#SECURITY.md`, `#CONTRIBUTING.md`
- `#llms-txt` — `llms.txt` (4 KB) — documentation map for LLM ingestion
- `#llms-full-txt` — `llms-full.txt` (544 KB) — same map with core docs inlined
- `#openclaw-plugin-json` — `openclaw.plugin.json` — the OpenClaw plugin manifest (skill inventory, MCP server config, shared deps, excluded-from-install)
- `#gbrain-yml` — `gbrain.yml` — runtime config

### Skill directories (53 entries under `skills/`)
- `#skills-resolver` — `skills/RESOLVER.md` (the skill router — picked once per request)
- `#skills-AGENT_README` — `skills/_AGENT_README.md` (read first, applies to every skill)
- `#skills-brain-filing-rules` — `skills/_brain-filing-rules.md` + `.json` (universal filing rules)
- `#skills-output-rules` — `skills/_output-rules.md` (universal output constraints)
- `#skills-friction-protocol` — `skills/_friction-protocol.md` (escalation when stuck)
- Per-skill dirs: `#skill-ingest`, `#skill-enrich`, `#skill-query`, `#skill-citation-fixer`, `#skill-signal-detector`, `#skill-cron-scheduler`, `#skill-daily-task-manager`, `#skill-minion-orchestrator`, `#skill-skill-creator`, `#skill-skillify`, `#skill-skillpack-harvest`, `#skill-meeting-ingestion`, `#skill-media-ingest`, `#skill-voice-note-ingest`, `#skill-perplexity-research`, `#skill-archive-crawler`, `#skill-book-mirror`, `#skill-brain-pdf`, `#skill-academic-verify`, `#skill-data-research`, `#skill-cross-modal-review`, `#skill-strategic-reading`, `#skill-concept-synthesis`, `#skill-soul-audit`, `#skill-functional-area-resolver`, `#skill-frontmatter-guard`, `#skill-conventions`, ...

### Docs
- `#docs-architecture` — `docs/architecture/`
- `#docs-ENGINES` — `docs/ENGINES.md`
- `#docs-skillpack-anatomy` — `docs/skillpack-anatomy.md`
- `#docs-mcp` — `docs/mcp/`
- `#docs-eval` — `docs/eval/`, `docs/eval-bench.md`, `docs/eval-capture.md`
- `#docs-takes-vs-facts` — `docs/takes-vs-facts.md`
- `#docs-contradictions` — `docs/contradictions.md`
- `#docs-storage-tiering` — `docs/storage-tiering.md`

### Other dirs
- `#src` — `src/` (TypeScript source)
- `#bin` — gbrain CLI binary
- `#admin` — admin dashboard sources
- `#evals` — evaluation framework
- `#tests`, `#test`
- `#examples`, `#templates`, `#recipes`, `#scripts`

## Why we cite this

gbrain is a *multi-shape* artifact: CLI + MCP server + skill scaffold. We cite it for:
- **Manifest extensions beyond Claude Code's plugin schema** — `shared_deps`, `excluded_from_install`, `contracts.contextEngines`
- **`RESOLVER.md` as a skill router** — agent reads it once per request, then picks the right skill. An alternative to skill-trigger auto-matching.
- **`_AGENT_README.md` and underscore-prefixed convention files** — universally-applicable rules that prefix every skill
- **The "BrainBench" eval framework** — quantitative skill evaluation built in (P@5, R@5 metrics)
- **The 9-cell cost matrix install protocol** — agents *required* to relay cost choices to operator before continuing
- **`llms.txt` + `llms-full.txt` dual files** — documentation discoverability for LLM consumers
- **Hybrid retrieval + auto-extracting graph** — patterns the skill ecosystem may need to adopt for memory
- **Trust scopes per remote** — read-write / read-only / no-access per MCP-connected agent

## Popularity signals

- **GitHub stars**: ~14,000 within weeks of April 2026 launch (per Vectorize.io article) — TODO snapshot live count via `gh api repos/garrytan/gbrain`
- **Released**: April 5, 2026 (~5,000 stars in 24 hours per Vectorize.io)
- **Press coverage**: multiple third-party reviews (Vectorize.io, Little Might, Saeloun blog)
- **Author position**: same as gstack — Garry Tan, YC CEO. Distribution advantage.
- **Cross-citation**: gstack ships `/setup-gbrain` and `/sync-gbrain` skills explicitly to integrate

## Related sources

- [[sources/garrytan--gstack]] — sibling product; gstack uses gbrain as memory layer
- [[sources/anthropic--skills]] — gbrain's skills follow Anthropic's SKILL.md shape but extend the manifest
