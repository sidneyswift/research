---
domain: creators
type: individual
name: Garry Tan
handle: garrytan
url: https://github.com/garrytan
twitter: https://x.com/garrytan
role: President & CEO, Y Combinator
last-reviewed: 2026-05-21
---

# Garry Tan

> President & CEO of Y Combinator. Ships opinionated open-source agent tooling (gstack, gbrain) co-authored with Claude Opus 4.6. Brings distribution scale to the agent ecosystem — when he ships something, the agent community pays attention.

## Attributes

- **Background** (per [[sources/garrytan--gstack#README]]): Twenty years building products. Cofounder Posterous (sold to Twitter). Early eng/PM/designer at Palantir. Built Bookface (YC's internal social network) in 2013.
- **Current role**: President & CEO, Y Combinator.
- **Distribution channels**: github.com/garrytan, x.com/garrytan, public speaking via No Priors and Hacker News.
- **Position in ecosystem**: Bridge between Anthropic's ecosystem and the broader builder/founder community. Not an Anthropic employee — an outside power-user with reach.
- **Self-claim** ([[sources/garrytan--gstack#README]]): "~810× my 2013 pace" of logical code change in 2026; 1,237 GitHub contributions YTD; 3 production services + 40+ features in 60 days, part-time, while running YC.
- **Co-authoring credit**: Both `gstack` and `gbrain` are co-authored with Claude Opus 4.6 per commit history (per Augment Code coverage).

## Artifacts produced

### Plugins / skill packs
- [[artifacts/plugins/gstack]] — virtual engineering team for Claude Code (23 skills + 8 power tools)
- [[artifacts/plugins/gbrain]] — agent memory system (MCP server + CLI + 43-skill scaffold)

### Adjacent artifacts (not yet deep-dived)
- `garrytan/openclaw` — the agent platform gbrain primarily targets ([referenced in [[sources/garrytan--gbrain#openclaw-plugin-json]]])
- `garrytan/hermes` — another agent deployment Garry runs
- `garrytan/gbrain-evals` — sibling repo with BrainBench scorecards
- Bookface (private, YC-internal)

### Public framing
- Quoted reference to Karpathy on No Priors podcast (March 2026), "haven't typed code since December" ([[sources/garrytan--gstack#README]])
- HN thread: https://news.ycombinator.com/item?id=47418576 — TODO snapshot

## Design philosophy (discernible from artifacts)

- **Opinionated over generic.** gstack is "Garry's exact setup" — the README explicitly markets the opinionation. Compare to Anthropic's skills which are demonstration-mode and unopinionated.
- **Personas over task categories.** gstack organizes skills as roles (CEO, Designer, Eng Manager, QA Lead, CSO) instead of as workflows. ([[sources/garrytan--gstack#README]])
- **Inject philosophy into every skill via preamble.** `ETHOS.md` is appended to every workflow skill's preamble — "Boil the Lake", "Completeness is cheap". ([[sources/garrytan--gstack#ETHOS.md]])
- **Custom frontmatter beyond Anthropic's spec.** `preamble-tier:`, `version:`, `allowed-tools:`, `triggers:` — extensions used in gstack SKILL.md files. ([[sources/garrytan--gstack#SKILL.md]])
- **Voice triggers as first-class.** gstack skills declare speech-to-text aliases in frontmatter ("quality check" → /qa).
- **Agent-first install docs.** gbrain ships `AGENTS.md` *separate from* `CLAUDE.md`, with agent-specific install protocols. Treats LLMs as the primary readers of operational docs.
- **Force human-in-the-loop on cost-bearing choices.** gbrain's 9-cell cost matrix `[AGENT]`-marked banner — the agent MUST relay to operator before continuing. ([[sources/garrytan--gbrain#AGENTS.md]])
- **Heavy versioning + changelog discipline.** gstack CHANGELOG is 690 KB; gbrain CHANGELOG is 1.1 MB. These aren't side projects.

## Source citations

- [[sources/garrytan--gstack#README]] — personal background, productivity claims, gstack pitch
- [[sources/garrytan--gstack#ETHOS.md]] — the "Builder Ethos" doc
- [[sources/garrytan--gbrain#README]] — gbrain pitch, production scale claims (17,888 pages, etc.)
- [[sources/garrytan--gbrain#AGENTS.md]] — agent-first protocol design
- [[sources/garrytan--gbrain#openclaw-plugin-json]] — manifest format extensions
