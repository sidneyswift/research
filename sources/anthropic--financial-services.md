---
domain: sources
type: repo
url: https://github.com/anthropics/financial-services
retrieved: 2026-06-01
snapshot-location: sources/anthropic--financial-services/
upstream-commit: 120a31dcede4affa1d771cbf286a63ee331f92a4
upstream-commit-date: 2026-05-29
last-reviewed: 2026-06-01
license: Apache-2.0
marketplace-name: claude-for-financial-services
marketplace-owner: Matt Piccolella (Anthropic FSI)
---

# Claude for Financial Services (`anthropics/financial-services`)

> Anthropic's official reference marketplace for financial-services (FSI) agents, skills, and data connectors — investment banking, equity research, private equity, wealth management, fund admin, operations. The headline idea: **every named agent ships "two ways from one source"** — as a Claude Cowork/Code plugin *and* as a [Claude Managed Agents API](https://docs.claude.com/en/api/managed-agents) template (`POST /v1/agents`), referencing the *same* system prompt and skills. 20 registered plugins + 10 managed-agent cookbooks.

## Snapshot details

- **Retrieved**: 2026-06-01
- **Location**: `sources/anthropic--financial-services/` (2.7 MB, 371 files, `.git/` stripped)
- **Upstream URL**: https://github.com/anthropics/financial-services
- **Upstream commit**: `120a31d` (2026-05-29)
- **License**: Apache 2.0 ([[sources/anthropic--financial-services#license]])
- **Marketplace owner**: `Matt Piccolella` (per `marketplace.json`); plugin manifests authored by `Anthropic FSI`. (Same pattern as the skills repo: an individual owner on an org-official artifact — cf. Keith Lazuka on [[sources/anthropic--skills]].)

## Anchor map

Citations into this source must use an anchor registered below.

### Root docs
- `#root` — the repo as a whole
- `#README` — `README.md` (16 KB) — the "two ways from one source" pitch, agent/vertical tables, install (Cowork / Claude Code / Managed Agents), MCP connector table, skill+command reference, "Making It Yours"
- `#CLAUDE.md` — `CLAUDE.md` (3 KB) — repo structure, the `check.py` / `sync-agent-skills.py` workflow, the version-bump-on-commit rule, key-files glossary
- `#disclaimer` — the `> [!IMPORTANT]` block in README: nothing here is investment/legal/tax/accounting advice; agents "draft analyst work product… for review by a qualified professional"; they "do not make investment recommendations, execute transactions, bind risk, post to a ledger, or approve onboarding; every output is staged for human sign-off"
- `#license` — `LICENSE` (Apache 2.0)
- `#repo-layout` — the repository-layout code block in README/CLAUDE.md

### Marketplace + manifests
- `#marketplace.json` — `.claude-plugin/marketplace.json` — registers **20 plugins**: 7 vertical, 10 agent, 2 partner, 1 MSFT-365 installer. Owner: Matt Piccolella
- `#plugin-json` — the per-plugin `.claude-plugin/plugin.json` shape (name, version, description, author) — components auto-discovered by directory convention, not declared

### Managed-agent cookbooks (`managed-agent-cookbooks/`)
- `#cookbooks-README` — `managed-agent-cookbooks/README.md` — "two ways from one source," the agent↔vertical↔leaf-worker table, the **manifest→API mapping** table, the one-delegation-level preview note, the cross-agent-handoff mechanism, "**Bold leaf = the only worker with `Write`**"
- `#cookbook-agent-yaml` — `managed-agent-cookbooks/<slug>/agent.yaml` — the orchestrator deploy manifest (real `/v1/agents` field names + `{file:}`/`{from_plugin:}`/`{manifest:}` conveniences). Exemplar: `gl-reconciler/agent.yaml`
- `#cookbook-reader-subagent` — `managed-agent-cookbooks/gl-reconciler/subagents/reader.yaml` — the untrusted-document **reader** leaf worker: Read/Grep only, no MCP, no write, plus a non-API `output_schema` (length-capped, character-class-restricted) consumed by `validate.py`
- `#cookbook-readme-security` — per-agent cookbook `README.md` security/handoff section (trust tiers table). Exemplar: `gl-reconciler/README.md`
- `#cookbook-steering-examples` — `managed-agent-cookbooks/<slug>/steering-examples.json` — example steering events (the headless equivalent of a user prompt)

### Agent plugins (`plugins/agent-plugins/`)
- `#agent-plugin-layout` — `plugins/agent-plugins/<slug>/` = `.claude-plugin/plugin.json` + `agents/<slug>.md` (canonical system prompt) + `skills/` (vendored copies)
- `#agent-system-prompt` — `plugins/agent-plugins/<slug>/agents/<slug>.md` — the **one source, two wrappers** system prompt. Frontmatter (`name`, `description` with sibling-disambiguation, `tools`) + body (What you produce / Workflow / Guardrails / Skills this agent uses). Exemplar: `gl-reconciler/agents/gl-reconciler.md`

### Vertical plugins (`plugins/vertical-plugins/`)
- `#vertical-financial-analysis` — `plugins/vertical-plugins/financial-analysis/` — the **core** vertical: 13 skills, 7 commands, and all data connectors. `plugin.json` version `0.1.1`
- `#mcp-connectors` — `plugins/vertical-plugins/financial-analysis/.mcp.json` — the 12 centralized HTTP MCP connectors. **NOTE: this file is malformed JSON** (missing comma after the `egnyte` entry); see `#scripts-check`
- `#hooks-stub` — `plugins/vertical-plugins/financial-analysis/hooks/hooks.json` — present but an empty stub (`{"hooks": {}}`)
- `#skill-comps-analysis` — `…/financial-analysis/skills/comps-analysis/SKILL.md` — "Perfect for / Not ideal for" trigger anchoring + a "⚠️ CRITICAL: Data Source Priority (READ FIRST)" preamble that hard-prefers MCP connectors over web search
- `#vertical-others` — the other six verticals: `investment-banking`, `equity-research`, `private-equity`, `wealth-management`, `fund-admin`, `operations` (skills + commands by FSI domain)

### Partner-built plugins (`plugins/partner-built/`)
- `#partner-lseg` — `plugins/partner-built/lseg/` — LSEG's own plugin: 8 commands + 8 skills + `CONNECTORS.md` + `.mcp.json` (the LFA MCP). Wraps LSEG's low-level MCP tools into command↔skill workflow pairs ("each command orchestrates 4-5 tools")
- `#partner-spglobal` — `plugins/partner-built/spglobal/` — S&P Global's plugin: 3 skills (`tear-sheet`, `earnings-preview-beta`, `funding-digest`), each with **its own `LICENSE` file**; `tear-sheet` is audience-segmented (4 reference files)
- `#skill-tear-sheet` — `…/spglobal/skills/tear-sheet/SKILL.md` — audience-segmented output (equity research / IB-M&A / corp dev / sales-BD; "If the user doesn't specify an audience, ask") + a firm-customizable "Style Configuration" brand block

### Scripts (`scripts/`)
- `#scripts` — `scripts/` overview: `check.py`, `sync-agent-skills.py`, `deploy-managed-agent.sh`, `orchestrate.py`, `validate.py`, `version_bump.py`, `test-cookbooks.sh`
- `#scripts-sync` — `scripts/sync-agent-skills.py` — re-vendors each agent plugin's `skills/` from the `vertical-plugins/` **source of truth** (`rmtree` + `copytree` by skill name)
- `#scripts-check` — `scripts/check.py` — lints every `plugin.json`/`marketplace.json`/`steering-examples.json`/agent `.md` frontmatter, resolves all `system.file`/`skills.path`/`callable_agents.manifest` references, fails on bundled-skill drift, and self-installs the git hook (`core.hooksPath -> .githooks`). **Does not validate `.mcp.json`** — see `#mcp-connectors`
- `#scripts-deploy` — `scripts/deploy-managed-agent.sh` — resolves manifest conveniences and `POST`s to `/v1/agents` (`anthropic-beta: managed-agents-2026-04-01`). Sanitizes `${ENV}` interpolation, refusing values outside `[A-Za-z0-9._/:@-]`. Wraps `output_schema` readers in a validation step
- `#scripts-orchestrate` — `scripts/orchestrate.py` — reference event loop routing `handoff_request` events between agents. Hard-allowlists target slugs + JSON-schema-validates payloads; header documents the prompt-injection threat model and recommends a typed-event alternative
- `#scripts-version-bump` — `scripts/version_bump.py` + `.githooks/pre-commit` — patch-bumps any changed plugin's `plugin.json` `version` so a branch ends exactly one patch ahead of `main` (once per branch, not per commit); a plugin's `version` gates update delivery to installed users
- `#ci-workflows` — `.github/workflows/` — `plugin-validate.yml`, `secret-scan.yml`, `version-bump.yml`

### MSFT-365 installer
- `#msft-365-install` — `claude-for-msft-365-install/` — a **Claude Code** plugin (not Cowork) of admin tooling that provisions the Claude Microsoft 365 add-in against the firm's *own* cloud (Vertex AI / Bedrock / internal LLM gateway). Commands: `bootstrap`, `consent`, `debug`, `manifest`, `setup`, `update-user-attrs`. `plugin.json` version `0.1.4`, author `Anthropic <support@anthropic.com>`

## Why we cite this

This is the wiki's richest single artifact and a different *kind* of artifact than the others. We cite it for:

- **Single-source, multi-surface distribution** — one agent definition, two runtimes (Cowork plugin + Managed Agents API). 2nd in-wiki example of the "multi-surface distribution" idea (cf. gbrain's CLI+MCP+skillpack). See [[patterns/composition/single-source-multi-surface-distribution]].
- **Marketplace-as-multi-plugin at scale** — 20 plugins in one repo. 2nd in-wiki example (cf. [[sources/anthropic--skills]]'s 3). See [[patterns/structural/marketplace-as-multi-plugin]].
- **Managed-agent cookbook format** — `agent.yaml` + depth-1 `subagents/*.yaml` + `steering-examples.json`. The first time this wiki documents the `/v1/agents` deploy shape (not the SKILL.md/plugin.json shape).
- **Trust-tiered subagent privilege separation** — prompt-injection containment by role: only the `reader` touches untrusted docs (Read/Grep, no MCP, no Write); exactly one leaf holds `Write`; a `critic` re-verifies before write. Output is schema-validated to strip injected instructions.
- **Single-source-of-truth skill vendoring with drift detection** — skills authored once in `vertical-plugins/`, copied into agent bundles by `sync-agent-skills.py`, drift-failed by `check.py`.
- **Compliance-grade human-in-the-loop positioning** — "staged for human sign-off"; an explicit list of actions the agents do *not* take.
- **Provenance-first skill behavior** — connector-over-web-search data-source hierarchies for auditability.
- **Version-as-update-gate maintenance discipline** — automated patch-bump tied to update delivery.
- **Partner-contributed plugins** — LSEG and S&P Global author their own command/skill bundles inside Anthropic's marketplace.

## Popularity signals

- **Official Anthropic** — published under `github.com/anthropics`, linked from the Claude Managed Agents and Cowork product pages. (Authoritative reference, by definition.)
- **Recency** — commit `120a31d` of 2026-05-29; references the `managed-agents-2026-04-01` beta and `callable_agents` "research preview." This is a *current-frontier* artifact, not a settled one.
- **GitHub stars**: not captured at snapshot — TODO `gh api repos/anthropics/financial-services` to record a value + date.

## Related sources

- [[sources/anthropic--skills]] — sibling Anthropic demonstration marketplace; the *simplest* marketplace shape (skills only). This repo is the *most complex* (agents + skills + commands + hooks + MCP + a second runtime).
- [[sources/anthropic--plugins-reference]] — the mechanism layer (`plugin.json`, `${CLAUDE_PLUGIN_ROOT}`, plugin caching) underneath these plugins.
- [[sources/garrytan--gbrain]] — independent example of multi-surface distribution (CLI + MCP + skillpack), the pairing that lets us confirm the distribution pattern.
