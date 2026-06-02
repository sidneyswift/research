---
domain: artifacts
type: plugin
name: # kebab-case plugin name
creator: # [[creators/...]]
source: # [[sources/<creator>--<repo>]]
ecosystem: # claude-code (plugins are Claude Code only as of 2026)
discovered-via: # marketplace | official-docs | tweet | colleague | other
marketplace-listing: # Cowork marketplace URL if applicable
status: # active | deprecated | beta | community-fork
last-reviewed: # YYYY-MM-DD
components:
  skills: # count
  commands: # count
  agents: # count
  hooks: # count
  mcp-servers: # count
popularity-signals:
  # - signal: marketplace-rank
  #   value: # raw number or text
  #   as-of: YYYY-MM-DD
  #   source: # [[sources/...#anchor]]
---

# {plugin-name}

> **One-line:** what this plugin gives a Claude Code installation in plain English.

## Attributes

- **What it does**: the user-facing capability, not the component inventory.
- **Target user**: who is this for? (engineers / PMs / marketers / lawyers / sales / vertical-specific role)
- **Component inventory**: enumerate skills/commands/agents/hooks/MCP — names, one-line each.
- **Install footprint**: dependencies, MCP servers required, env vars or auth flows triggered, disk size.
- **Plugin layout**: top-level directory structure with file counts.
- **License**: MIT / Apache / proprietary / unclear.

## Relationships

- **Creator**: [[creators/...]]
- **Source**: [[sources/...#root]]
- **Composes**: list every [[artifacts/skills/...]] this plugin bundles (each gets its own page if we deep-dive)
- **Depends on**: [[artifacts/mcp-servers/...]], external services, auth providers
- **Marketplace neighbors**: similar plugins worth comparing

## What problem it solves

The whole-job-to-be-done. A plugin earns the right to exist over individual skills by bundling a *coherent workflow*, not just a grab-bag — does this one?

## Composition strategy

Plugins are the place where composition shows up most clearly. Document:
- How do the components hand off to each other? (e.g., skill A produces output X, command B consumes X)
- Are there shared resources (templates, scripts, prompts) across components?
- Where does the plugin draw the line between "this should be a skill" vs "this should be a command" vs "this should be an agent"?
- Does the plugin install hooks? If so, what behavior do they automate without LLM involvement?

## Patterns demonstrated

- [[patterns/composition/...]] — *how this plugin uses the pattern*
- [[patterns/structural/...]] — *how this plugin uses the pattern*
- [[patterns/quality-bar/...]] — *how this plugin uses the pattern*

## Source citations

Bullet list of every non-obvious claim with `[[sources/...#anchor]]`.

## What makes it great

Specific, plugin-level. The coherence of the bundle, the workflow chained across components, the surprising-but-correct design choices.

## What we'd steal

**Exhaustive ledger, not a curated top-3.** List *every* portable lesson — even minor ones; a thin list narrows our attention later. ★-mark the highest-value bullets. Plugin-level lessons (composition, hooks, MCP integration) usually transfer better than skill-level lessons, so capture them all.

- ★ *highest-value, clearly portable*
- *minor-but-worth-noting*

## Open questions / what's unclear
