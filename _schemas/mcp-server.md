---
domain: artifacts
type: mcp-server
name: # kebab-case
creator: # [[creators/...]]
source: # [[sources/<creator>--<repo>]]
language: # python | typescript | go | rust | other
transport: # stdio | sse | http | multiple
auth-model: # none | api-key | oauth | dynamic-client-registration | other
discovered-via:
status: # active | deprecated | beta | abandoned
last-reviewed: # YYYY-MM-DD
tool-count: # number of MCP tools exposed
popularity-signals:
  # - signal: github-stars
  #   value: 1234
  #   as-of: YYYY-MM-DD
  #   source: # [[sources/...#stars-badge]]
---

# {mcp-server-name}

> **One-line:** what external system this MCP server connects Claude to, and what it lets Claude do with it.

## Attributes

- **External system**: the underlying API/service (e.g., Slack, Linear, Postgres, custom internal).
- **What Claude can do**: high-level capabilities (read X, write Y, search Z).
- **Tool surface**: enumerate the MCP tools — name + one-line. If many (>15), group by function.
- **Resource surface**: any MCP resources exposed?
- **Prompts surface**: any MCP prompts exposed?
- **Auth flow**: how does the user authenticate? Long-lived API key, OAuth dance, dynamic client registration, headers?
- **Rate limit handling**: does the server back off, retry, surface limits to the model?
- **Error surface**: how do errors come back to the model — structured JSON, plain text, exception traces?
- **Read/write split**: which tools are destructive vs read-only? Does the server gate destructive ops?

## Relationships

- **Creator**: [[creators/...]]
- **Source**: [[sources/...#root]]
- **Used by skills**: [[artifacts/skills/...]] that explicitly require this server
- **Used by plugins**: [[artifacts/plugins/...]] that bundle this server in their manifest
- **Competing servers**: other MCP servers for the same external system worth comparing

## What problem it solves

Why MCP and not just "let the model curl the API"? What does this server add over raw HTTP — type safety, auth abstraction, schema, semantic helpers?

## Tool design philosophy

This is where MCP servers differ wildly. Document:
- **Granularity**: many small tools vs few composable tools?
- **Naming**: verb-first (`create_record`), noun-first (`record_create`), or domain-shaped (`add-record-to-list`)?
- **Parameter style**: minimal required + many optional, or strict schemas?
- **Tool descriptions**: terse one-liners vs full prompt-style instructions inside the description?
- **Selection logic**: how does the model know when to use tool X vs tool Y? Are tool descriptions written to *disambiguate* from siblings?

## Patterns demonstrated

- [[patterns/structural/...]]
- [[patterns/behavioral/...]] — especially around tool selection prompting
- [[patterns/quality-bar/...]]

## Source citations

## What makes it great

Often the difference between a great MCP server and a mediocre one is tool *design*, not coverage. Be specific about what choices the creator made.

## What we'd steal

**Exhaustive ledger, not a curated top-3.** List *every* portable, concrete lesson — even minor ones; a thin list narrows our attention later. ★-mark the highest-value bullets.

- ★ *highest-value, clearly portable*
- *minor-but-worth-noting*

## Open questions / what's unclear
