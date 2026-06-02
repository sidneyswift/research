---
domain: artifacts
type: index
subdomain: mcp-servers
last-reviewed: 2026-05-21
---

# MCP Servers

MCP servers cataloged. Each page uses [../../\_schemas/mcp-server.md](../../_schemas/mcp-server.md).

## By external system category

### Productivity (Slack, Notion, Linear, Asana, etc.)
*(none yet)*

### Engineering (GitHub, GitLab, Datadog, PagerDuty, etc.)
*(none yet)*

### Data (Postgres, BigQuery, Supabase, Hex, etc.)
*(none yet)*

### Design (Figma, Canva)
*(none yet)*

### Sales / CRM (Apollo, Close, Outreach, ZoomInfo)
*(none yet)*

### Custom / vertical
*(none paged yet — but see the 12 FSI financial-data connectors in the candidate list below)*

## Candidate list

**FSI financial-data connectors** — referenced (not authored) by [[artifacts/plugins/anthropic-financial-services-marketplace]]; centralized in `financial-analysis/.mcp.json` ([[sources/anthropic--financial-services#mcp-connectors]]). All hosted HTTP endpoints (`type: http`), most behind a provider subscription/API key — so any future page is `link-only`, not a clone. NOTE: the manifest file itself is malformed JSON (missing comma after `egnyte`).

- `daloopa` — `https://mcp.daloopa.com/server/mcp` (fundamentals)
- `morningstar` — `https://mcp.morningstar.com/mcp`
- `sp-global` / Kensho — `https://kfinance.kensho.com/integrations/mcp` (also backs the `sp-global` partner plugin)
- `factset` — `https://mcp.factset.com/mcp`
- `moodys` — `https://api.moodys.com/genai-ready-data/m1/mcp`
- `mtnewswire` — `https://vast-mcp.blueskyapi.com/mtnewswires`
- `aiera` — `https://mcp-pub.aiera.com`
- `lseg` — `https://api.analytics.lseg.com/lfa/mcp` (the LFA MCP; also backs the `lseg` partner plugin — a good first paged example since partner skills show how its tools are consumed)
- `pitchbook` — `https://premium.mcp.pitchbook.com/mcp`
- `chronograph` — `https://ai.chronograph.pe/mcp` (PE portfolio monitoring)
- `egnyte` — `https://mcp-server.egnyte.com/mcp` (document store)
- `box` — `https://mcp.box.com` (document store)
