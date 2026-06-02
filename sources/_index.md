---
domain: sources
type: index
last-reviewed: 2026-05-21
---

# Sources

Primary evidence backing every claim in the wiki. Snapshotted, not just linked. Each source page uses [../_schemas/source.md](../_schemas/source.md).

## Citation convention

Wikilinks to sources use **anchors that are defined on the source page itself**. Don't invent anchor names ad-hoc — register them in the source's "Anchor map" section first.

✅ `[[sources/anthropic--skills#SKILL.md-L1-L20]]`
✅ `[[sources/joe-dev--my-skill-pack#manifest]]`
❌ `[[sources/anthropic--skills#somewhere-near-the-top]]` — anchor not registered

## Cloned repos

Repos sit at `sources/<creator>--<repo>/` (the actual git clone, `.git/` stripped) and have a corresponding `sources/<creator>--<repo>.md` page that is the citation target.

- [[sources/anthropic--skills]] — `anthropics/skills` (11 MB, commit `690f15c` of 2026-05-19). The official Anthropic skills + spec + template.
- [[sources/garrytan--gstack]] — `garrytan/gstack` (41 MB, commit `029356e` of 2026-05-20). Garry Tan's 23-skill engineering-team pack.
- [[sources/garrytan--gbrain]] — `garrytan/gbrain` (71 MB, commit `1580c6d` of 2026-05-20, version 0.36.4.0). Garry Tan's memory system.
- [[sources/anthropic--financial-services]] — `anthropics/financial-services` (2.7 MB, commit `120a31d` of 2026-05-29, Apache 2.0). Anthropic's FSI reference marketplace — 20 plugins, dual-runtime (Cowork plugin + Managed Agents API), 10 managed-agent cookbooks with trust-tiered subagents.

## Articles, posts, threads

External writing we cite. Always include retrieval date and a snapshot path (PDF / screenshot / archive.org URL).

*(none yet)*

## Marketplace listings

Marketplace pages capture install counts, ratings, descriptions — popularity signals decay so we capture values *at retrieval date*.

*(none yet)*

## Social

Tweets, Reddit threads, HN comments. Capture full text + author + date.

*(none yet)*

## Docs

Official Anthropic / Cowork / vendor docs we cite as authoritative. Living pages — pin claims to the retrieval date.

- [[sources/anthropic--plugins-reference]] — Claude Code "Plugins reference" (`code.claude.com/docs`, retrieved 2026-05-31). The mechanism layer: `plugin.json` schema, `${CLAUDE_PLUGIN_ROOT}` file resolution, and the `~/.claude/plugins/cache` caching behavior. Partial verbatim snapshot.
