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
