---
domain: sources
type: docs-page
url: https://code.claude.com/docs/en/plugins-reference
retrieved: 2026-05-31
snapshot-location: sources/anthropic--plugins-reference/snapshot.md
upstream-commit: # n/a — living docs page, no version stamp exposed
last-reviewed: 2026-05-31
---

# Claude Code — Plugins reference (`code.claude.com/docs`)

> Anthropic's authoritative technical reference for the Claude Code **plugin** system: component schemas, the `plugin.json` manifest, the CLI, and runtime behavior. We cite this as the spec for *how plugins are packaged, resolved, and cached* — the layer beneath the individual plugin artifacts we study (gstack, gbrain, anthropic-skills-marketplace).

## Snapshot details

- **Retrieved**: 2026-05-31
- **Where it lives in this wiki**: `sources/anthropic--plugins-reference/snapshot.md` (partial verbatim — cited sections + full heading outline). Living docs page, so not fully cloned.
- **Upstream URL**: https://code.claude.com/docs/en/plugins-reference
- **Section the request pointed at**: `#plugin-caching-and-file-resolution`
- **Extraction method**: page DOM (Mintlify docs site), captured 2026-05-31.

## Anchor map

Citations to this source use `#anchor` suffixes registered here. Anchors map to section ids on the live page and to headings captured in the snapshot.

- `#root` — the page as a whole
- `#caching-and-file-resolution` — "Plugin caching and file resolution" section (the `~/.claude/plugins/cache` copy-on-install behavior, orphaned-version GC, Glob/Grep skipping orphaned dirs). Captured verbatim in snapshot.
- `#env-vars` — "Environment variables" section; the three path variables `${CLAUDE_PLUGIN_ROOT}` (install dir, ephemeral, changes on update), `${CLAUDE_PROJECT_DIR}` (project root), and `${CLAUDE_PLUGIN_DATA}` (persistent data dir). Captured verbatim. Note: mid-session updates keep the session on the old paths; new sessions pick up new paths.
- `#persistent-data-directory` — "Persistent data directory" section; `${CLAUDE_PLUGIN_DATA}` resolves to `~/.claude/plugins/data/{id}/` (sanitized id), survives updates; recommended manifest-diff reinstall pattern. Captured verbatim.
- `#components` — "Plugin components reference" (skills, agents, hooks, MCP servers, LSP servers, monitors, themes)
- `#manifest` — "Plugin manifest schema" / `plugin.json` (all fields optional; `name` required if present)
- `#installation-scopes` — "Plugin installation scopes"
- `#path-behavior-rules` — "Path behavior rules" (component path resolution)
- `#path-traversal` — "Path traversal limitations"
- `#marketplace-symlinks` — "Share files within a marketplace with symlinks"
- `#cli` — "CLI commands reference"
- `#versioning` — "Distribution and versioning reference"

(Outline of all H2/H3 headings is in the snapshot. Add anchors here as we cite more sections.)

## Why we cite this

This is the **mechanism layer** the wiki has been missing. Our plugin artifact pages describe what a plugin *contains*; this doc defines how Claude Code *loads and runs* it. We cite it for:

- **File resolution**: the `${CLAUDE_PLUGIN_ROOT}` convention — why well-built plugins never hardcode paths. Directly relevant to gstack/gbrain's bash-heavy preambles and bundled scripts.
- **Caching semantics**: marketplace plugins are *copied* into `~/.claude/plugins/cache`, versioned per install, orphaned versions GC'd after a 7-day grace period, and Glob/Grep skip orphaned dirs. Explains dev-loop friction (restart to pick up changes) and the `--plugin-dir` local-dev escape hatch.
- **Manifest authority**: the canonical `plugin.json` shape and field rules — the baseline that gstack/gbrain's frontmatter extensions deviate from.
- **Persistent data**: `${CLAUDE_PLUGIN_DATA}` (`~/.claude/plugins/data/{id}/`) survives updates while the install dir does not — relevant to gbrain, which ships a memory store.

## Popularity / authority signals

- **Official Anthropic documentation** (`code.claude.com/docs`) — authoritative, not a popularity signal per se but the canonical reference everything else defers to.
- Living page: no version/commit stamp exposed, so claims are pinned to the **2026-05-31** retrieval date and decay accordingly.

## Related sources

- [[sources/anthropic--skills]] — the *skills* spec + demonstration skills; this page is the *plugins* spec that packages skills (plus agents/hooks/MCP) for Claude Code.
- [[sources/garrytan--gstack]] — plugin that bundles scripts; subject to the `${CLAUDE_PLUGIN_ROOT}` and caching rules described here.
- [[sources/garrytan--gbrain]] — plugin shipping a persistent memory store; the "persistent data directory" guidance applies.
- [[sources/openai--plugins]] — **the cross-lab counterpart.** OpenAI's Codex plugin spec (`.codex-plugin/`) is near-identical to the one this page documents — same auto-discovered `skills/`/`commands/`/`agents/`, the same `hooks.json` `PostToolUse`/`matcher` grammar, `.mcp.json`, and a `marketplace.json`. Cite both together for [[concepts/convergent-agent-plugin-spec]]; OpenAI even references Anthropic's "skill-creator naming rules."

## Related wiki pages

- [[creators/anthropic]] — author of this doc
- [[artifacts/plugins/anthropic-skills-marketplace]] — a marketplace subject to the install/cache behavior documented here
- [[concepts/convergent-agent-plugin-spec]] — this page is one of the concept's two grounding sources (the Anthropic side of the convergence)
