---
domain: artifacts
type: plugin
name: claude-for-financial-services
creator: "[[creators/anthropic]]"
source: "[[sources/anthropic--financial-services]]"
ecosystem: claude-code + cowork (plugins) AND claude-managed-agents-api (/v1/agents)
discovered-via: user-curated (Sidney named explicitly)
marketplace-listing: "claude plugin marketplace add anthropics/financial-services"
status: active
last-reviewed: 2026-06-01
ingestion-mode: full
license: Apache-2.0
components:
  plugins-registered: 20            # 7 vertical + 10 agent + 2 partner + 1 installer
  vertical-plugins: 7
  agent-plugins: 10
  partner-plugins: 2
  managed-agent-cookbooks: 10       # /v1/agents wrappers mirroring the 10 agent-plugins
  skills: 55 (in vertical-plugins; vendored into agent-plugins by sync script)
  commands: 39 (across vertical-plugins) + 8 (lseg partner)
  subagents: 30 (3 per managed-agent cookbook × 10)
  hooks: 0 active (hooks.json present but empty stub)
  mcp-connectors: 12 (centralized in financial-analysis .mcp.json; file is malformed JSON)
popularity-signals:
  - signal: official-anthropic
    value: "Anthropic's official FSI reference repo (github.com/anthropics), linked from Managed Agents + Cowork product pages"
    as-of: 2026-06-01
    source: "[[sources/anthropic--financial-services#README]]"
  - signal: frontier-recency
    value: "references managed-agents-2026-04-01 beta + callable_agents 'research preview'; commit 120a31d of 2026-05-29"
    as-of: 2026-06-01
    source: "[[sources/anthropic--financial-services#cookbooks-README]]"
---

# claude-for-financial-services (the marketplace)

> **One-line:** Anthropic's official FSI reference marketplace — 20 plugins covering investment banking, equity research, private equity, wealth management, fund admin, and operations. Its defining move: **every named agent ships "two ways from one source"** — as a Cowork/Claude Code plugin *and* as a Claude Managed Agents API template — referencing the same system prompt and skills. The richest, most architecturally ambitious artifact in this wiki.

## Attributes

- **Marketplace owner**: `Matt Piccolella`; plugin manifests authored by `Anthropic FSI` ([[sources/anthropic--financial-services#marketplace.json]]).
- **Target user**: FSI practitioners (bankers, equity-research analysts, PE/VC deal teams, wealth advisors, fund accountants, KYC/onboarding ops) — *and* the platform/IT teams who deploy agents for them. The README addresses both "analysts install today" and "your platform team deploys behind your own workflow engine" ([[sources/anthropic--financial-services#cookbooks-README]]).
- **Component inventory** (by type):
  - **7 vertical plugins** ([[sources/anthropic--financial-services#marketplace.json]]): `financial-analysis` (core: comps/DCF/LBO/3-statement/deck-QC + all connectors), `investment-banking`, `equity-research`, `private-equity`, `wealth-management`, `fund-admin`, `operations`. These hold the **55 source skills** + **39 slash commands**.
  - **10 agent plugins** ([[sources/anthropic--financial-services#agent-plugin-layout]]): `pitch-agent`, `market-researcher`, `earnings-reviewer`, `meeting-prep-agent`, `model-builder`, `gl-reconciler`, `kyc-screener`, `valuation-reviewer`, `month-end-closer`, `statement-auditor`. Each = one system prompt + the vendored subset of skills it needs.
  - **10 managed-agent cookbooks** ([[sources/anthropic--financial-services#cookbooks-README]]): the `/v1/agents` mirror of those 10 agents — `agent.yaml` orchestrator + 3 depth-1 `subagents/*.yaml` each (**30 leaf workers**) + `steering-examples.json` + a security README.
  - **2 partner plugins** ([[sources/anthropic--financial-services#partner-lseg]], [[sources/anthropic--financial-services#partner-spglobal]]): `lseg` (8 commands/8 skills on the LFA MCP) and `sp-global` (3 skills on S&P Capital IQ / Kensho).
  - **1 admin installer** ([[sources/anthropic--financial-services#msft-365-install]]): `claude-for-msft-365-install` — Claude-Code-only tooling to provision the Microsoft 365 add-in against the firm's own cloud.
- **Install footprint**: file-based, **no build step** — "Everything is file-based — markdown and JSON" ([[sources/anthropic--financial-services#README]]). Plugins install via `claude plugin install <name>@claude-for-financial-services`. Managed Agents deploy via `scripts/deploy-managed-agent.sh <slug>` → `POST /v1/agents` (`anthropic-beta: managed-agents-2026-04-01`). **12 HTTP MCP connectors** (Daloopa, Morningstar, S&P/Kensho, FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, Egnyte, Box) — most behind the provider's own subscription/API key ([[sources/anthropic--financial-services#mcp-connectors]]).
- **Plugin layout**: typed by directory — `plugins/{vertical-plugins,agent-plugins,partner-built}/`, `managed-agent-cookbooks/`, `claude-for-msft-365-install/`, `scripts/`. Per-plugin `plugin.json` carries only name/version/description/author; components are **auto-discovered** from `skills/`, `commands/`, `agents/`, `hooks/` by convention ([[sources/anthropic--financial-services#plugin-json]]).
- **License**: Apache 2.0 repo-wide; S&P Global ships **per-skill `LICENSE` files** inside its partner plugin ([[sources/anthropic--financial-services#partner-spglobal]]).

## Relationships

- **Creator**: [[creators/anthropic]] (the FSI team specifically; owner Matt Piccolella).
- **Source**: [[sources/anthropic--financial-services#root]].
- **Sibling**: [[artifacts/plugins/anthropic-skills-marketplace]] — same marketplace mechanism, opposite end of the complexity spectrum (skills-only, one runtime).
- **Mechanism layer**: [[sources/anthropic--plugins-reference]] — `plugin.json`, `${CLAUDE_PLUGIN_ROOT}`, plugin caching underneath these plugins.
- **Depends on**: 12 third-party MCP servers (provider subscriptions); the Claude Managed Agents API (`/v1/agents`, preview); for the installer, Microsoft Graph + Azure + a customer LLM cloud (Vertex/Bedrock/gateway).
- **Composes**: too many child plugins to page individually yet — candidates queued in [[artifacts/plugins/_index]] and skills in [[artifacts/skills/_index]].

## What problem it solves

FSI work is **document-heavy, audit-bound, and human-signed-off**: a comps set, a DCF, an IC memo, a GL reconciliation, a KYC packet. The repo packages those whole jobs as installable agents that "draft analyst work product… for review by a qualified professional" — explicitly *not* decision-makers. The disclaimer enumerates what the agents do **not** do: "make investment recommendations, execute transactions, bind risk, post to a ledger, or approve onboarding; every output is staged for human sign-off" ([[sources/anthropic--financial-services#disclaimer]]). The second problem it solves is **deployment shape**: the same analyst agent has to run interactively for an analyst *and* headlessly inside a bank's workflow engine — so the repo ships both surfaces from one definition rather than making the firm choose or fork.

## Composition strategy

This is the most composition-dense artifact in the wiki. Four moves stack:

1. **Marketplace-as-multi-plugin** ([[patterns/structural/marketplace-as-multi-plugin]]). One `marketplace.json` registers 20 plugins, typed by directory. Install the core (`financial-analysis`) plus whichever verticals/agents you need ([[sources/anthropic--financial-services#marketplace.json]]).

2. **Single-source-of-truth skill vendoring with drift detection.** Skills are authored once in `vertical-plugins/<vertical>/skills/`. Each agent plugin carries **vendored copies** in its own `skills/`, propagated by `scripts/sync-agent-skills.py` (`rmtree` + `copytree` by skill name — [[sources/anthropic--financial-services#scripts-sync]]). `scripts/check.py` fails the build if a bundled copy has drifted from source ([[sources/anthropic--financial-services#scripts-check]]). So agents stay self-contained ("installing the agent is all you need") *without* the copies rotting.

3. **Single-source, multi-surface distribution** ([[patterns/composition/single-source-multi-surface-distribution]]). The agent's system prompt at `agents/<slug>.md` is referenced — not copied — by the Managed Agent `agent.yaml` via `system: {file: …}` and `skills: [{from_plugin: …}]`; the deploy script resolves those into a `/v1/agents` payload ([[sources/anthropic--financial-services#cookbook-agent-yaml]], [[sources/anthropic--financial-services#scripts-deploy]]). "Same agent, same skills — pick your surface."

4. **Trust-tiered subagent privilege separation** (the standout — see worked example below). Within each managed agent, an orchestrator delegates to depth-1 leaf workers split by *privilege*: only a `reader` touches untrusted documents, exactly one leaf holds `Write`, and a `critic` re-verifies before anything is written ([[sources/anthropic--financial-services#cookbook-readme-security]]).

**Where the lines are drawn** — the repo is unusually explicit ([[sources/anthropic--financial-services#README]]): *skills* = domain expertise Claude draws on automatically; *commands* = explicit slash actions (`/comps`, `/ic-memo`); *agents* = a system prompt that owns a workflow end-to-end and bundles its skills; *connectors* = MCP servers centralized in the core vertical; *managed-agent wrappers* = `agent.yaml` + subagents for headless deploy. **Hooks exist as a directory but are an empty stub** (`hooks.json = {"hooks": {}}`) — the one primitive present-but-unused ([[sources/anthropic--financial-services#hooks-stub]]).

## Worked example — `gl-reconciler` (one agent, both surfaces, trust-tiered)

The clearest single illustration ([[sources/anthropic--financial-services#agent-system-prompt]], [[sources/anthropic--financial-services#cookbook-readme-security]]):

- **One prompt, two wrappers.** `plugins/agent-plugins/gl-reconciler/agents/gl-reconciler.md` is the canonical system prompt (a fund-accounting controller; "What you produce / Workflow / Guardrails / Skills this agent uses"). The Cowork plugin bundles it directly; `managed-agent-cookbooks/gl-reconciler/agent.yaml` references it with an `append:` that adds headless instructions ("Produce files in ./out/; do not assume an open Office document").
- **Sibling-disambiguating description.** Its frontmatter `description` ends "…**not for journal-entry posting (use month-end-closer for that)**" — routing logic written *into* the description to disambiguate from a neighbor, the agent-level analog of MCP tool-selection disambiguation.
- **Privilege-separated leaf workers.** Three subagents, split by trust ([[sources/anthropic--financial-services#cookbook-readme-security]]):

  | Tier | Touches untrusted docs? | Tools | Connectors |
  |---|---|---|---|
  | `reader` | **Yes** | Read, Grep only | none |
  | orchestrator | No | Read, Grep, Glob, Agent | read-only GL + subledger MCP |
  | `resolver` (**Write-holder**) | No | Read, Write, Edit | none |

  The convention is legible at a glance: in the cookbook index, "**Bold leaf = the only worker with `Write`**" ([[sources/anthropic--financial-services#cookbooks-README]]).
- **Structured output as injection defense.** The `reader` returns *only* JSON matching a non-API `output_schema` in its yaml — string fields are length-capped and character-class-restricted (`maxLength`, `pattern: "^[A-Za-z0-9_-]+$"`) so "injected instructions cannot survive intact"; `scripts/validate.py` enforces it before the orchestrator sees the output ([[sources/anthropic--financial-services#cookbook-reader-subagent]]).
- **Independent re-verification.** A `critic` re-checks each reported break against trusted sources before the orchestrator hands the set to the `resolver` to write ([[sources/anthropic--financial-services#cookbook-readme-security]]).
- **Hand-off, not direct call.** To pass verified breaks to `month-end-closer`, the orchestrator emits a `handoff_request` in its output; `scripts/orchestrate.py` routes it as a new steering event — hard-allowlisting target slugs and JSON-schema-validating the payload, with a header documenting the prompt-injection threat model and recommending a typed-event alternative ([[sources/anthropic--financial-services#scripts-orchestrate]]).
- **Terminal human gate.** "None of this writes to a system of record. Ledger adjustments require human approval outside the agent" ([[sources/anthropic--financial-services#cookbook-readme-security]]).

## Patterns demonstrated

**Confirmed (this ingest supplied the 2nd example for both):**

- [[patterns/composition/single-source-multi-surface-distribution]] — one agent definition, two runtimes (Cowork plugin + Managed Agents API), references resolved at deploy. Pairs with gbrain.
- [[patterns/structural/marketplace-as-multi-plugin]] — 20 plugins from one `marketplace.json`. Pairs with anthropic-skills-marketplace.

**Proposed (strong here, need a 2nd in-wiki example to confirm):**

- **Trust-tiered subagent privilege separation** — prompt-injection containment by role: only the untrusted-doc reader is sandboxed (no MCP/no Write), exactly one leaf holds Write, a critic re-verifies. *The single best idea in this repo to steal.* ([[sources/anthropic--financial-services#cookbook-readme-security]], [[sources/anthropic--financial-services#cookbook-reader-subagent]])
- **Single-source-of-truth skill vendoring + drift check** — author once in verticals, vendor into agents, fail the build on drift ([[sources/anthropic--financial-services#scripts-sync]], [[sources/anthropic--financial-services#scripts-check]]).
- **Structured-output-as-injection-defense** — constrain a worker's only output channel to a length/character-class-bounded schema so injected text can't survive ([[sources/anthropic--financial-services#cookbook-reader-subagent]]).
- **Provenance-first data-source hierarchy** — skills hard-prefer audited MCP connectors over web search ("NEVER use web search as a primary data source… lacks accuracy, audit trails") ([[sources/anthropic--financial-services#skill-comps-analysis]]).
- **Sibling-disambiguating description clause** — write the "use X not Y for Z" routing into the agent/skill description itself ([[sources/anthropic--financial-services#agent-system-prompt]]).
- **Version-as-update-gate** — a pre-commit hook patch-bumps a changed plugin's `version` once per branch; `version` gates update delivery to installed users; a CI Action backstops it ([[sources/anthropic--financial-services#scripts-version-bump]]).
- **Audience-segmented skill output** — one skill, N audiences, N reference files, "if unspecified, ask" (S&P `tear-sheet`: equity research / IB-M&A / corp dev / sales-BD) ([[sources/anthropic--financial-services#skill-tear-sheet]]).
- **Partner-contributed plugins** — outside vendors (LSEG, S&P) author command/skill bundles inside the marketplace; LSEG wraps its *own* low-level MCP tools into 8 command↔skill workflow pairs ([[sources/anthropic--financial-services#partner-lseg]]).
- **Compliance-grade HITL positioning** — an explicit "the agent does NOT do X" list; everything staged for sign-off ([[sources/anthropic--financial-services#disclaimer]]). (Relative of gbrain's `[AGENT]` operator-decision banner, but at the product-positioning layer.)

## Source citations

- [[sources/anthropic--financial-services#README]] — two-ways pitch, agent/vertical tables, install paths, 12-connector table, "no build step"
- [[sources/anthropic--financial-services#marketplace.json]] — 20 registered plugins, owner, à-la-carte install
- [[sources/anthropic--financial-services#cookbooks-README]] — manifest→API mapping, one-delegation-level preview, handoffs, "bold leaf = Write"
- [[sources/anthropic--financial-services#cookbook-agent-yaml]] / [[sources/anthropic--financial-services#cookbook-reader-subagent]] — orchestrator + sandboxed reader with output_schema
- [[sources/anthropic--financial-services#cookbook-readme-security]] — the gl-reconciler trust-tier table + terminal human gate
- [[sources/anthropic--financial-services#scripts-sync]] / [[sources/anthropic--financial-services#scripts-check]] — vendoring + drift detection
- [[sources/anthropic--financial-services#scripts-deploy]] / [[sources/anthropic--financial-services#scripts-orchestrate]] — `/v1/agents` deploy + handoff routing with allowlist
- [[sources/anthropic--financial-services#scripts-version-bump]] — version-as-update-gate
- [[sources/anthropic--financial-services#skill-comps-analysis]] / [[sources/anthropic--financial-services#skill-tear-sheet]] — provenance hierarchy + audience segmentation
- [[sources/anthropic--financial-services#disclaimer]] — the not-advice / staged-for-sign-off framing

## What makes it great

The repo treats **deployment surface and security as first-class design problems**, not afterthoughts. Most skill/plugin artifacts stop at "here's the prompt"; this one answers "where does it run?" (two surfaces, one source) and "what happens when a counterparty PDF contains an attack?" (a reader that can't write or call a connector, an output schema that strips instructions, a critic that re-verifies, a Write-holder that never sees raw outsider content). The privilege-tier table and the one-line "**bold leaf = the only worker with `Write`**" convention turn an abstract threat model into something a reviewer can audit in seconds. And it is honest about its limits to the point of listing the actions it refuses to take — exactly the posture a regulated buyer needs. The lazy alternative — one agent with all tools reading untrusted docs straight into a Write context — is precisely the thing this design exists to prevent.

## What we'd steal

- **The trust-tier subagent table** as a reusable security primitive: classify each worker by *does it touch untrusted input?* and *does it hold Write?*, and make it a legible table in the README. Port directly to any pipeline that ingests outsider documents.
- **"Bold leaf = the only Write-holder"** — a one-glance convention for "where can this system mutate state?"
- **Structured output as an injection boundary** — when a sub-step reads untrusted text, force its output through a length- and character-class-bounded schema and validate before the parent consumes it.
- **Single-source + vendored copies + drift-failing linter** — lets sub-artifacts be self-contained *and* DRY at once; the linter makes the contract enforceable.
- **Reference, don't copy, the load-bearing prompt** across runtimes; let a deploy script resolve references into each surface's format.
- **`{file:}` / `{from_plugin:}` / `{manifest:}` manifest conveniences** that resolve to verbose API fields — keeps the human-authored manifest readable.
- **Sibling-disambiguation in descriptions** ("use month-end-closer for posting") to make auto-routing reliable across a crowded catalog.
- **Provenance-first data hierarchy** in any skill where audit trails matter — pin to trusted connectors, name web search as a last resort *and say why*.
- **The explicit "does NOT do" list** — set the human-in-the-loop boundary in writing.
- **`${ENV}` sanitization in deploy tooling** — interpolated secrets/URLs refused if they contain characters outside a safe class ([[sources/anthropic--financial-services#scripts-deploy]]).

## Weird / surprising things

- **A malformed connector manifest ships in the reference repo.** `financial-analysis/.mcp.json` is **invalid JSON** — a missing comma after the `egnyte` entry (verified: `python3 -m json.tool` fails) — and `check.py` never catches it because the linter validates `plugin.json`/`marketplace.json`/`agent.yaml`/frontmatter but **not** `.mcp.json` ([[sources/anthropic--financial-services#mcp-connectors]], [[sources/anthropic--financial-services#scripts-check]]). A precise, useful boundary on an otherwise-rigorous QC story: the drift-checker is thorough about *manifests and references*, blind to *connector syntax*.
- **Owner is an individual, not a team** — `Matt Piccolella` on an org-official artifact, exactly mirroring Keith Lazuka on [[artifacts/plugins/anthropic-skills-marketplace]]. Two-for-two: Anthropic ships official marketplaces under a named employee. Likely still emerging-product territory internally.
- **Hooks present but empty.** Every other primitive (skills, commands, agents, MCP, subagents) is exercised hard; `hooks/hooks.json` is a `{}` stub — a deliberate "slot reserved, not yet used" signal.

## Open questions / what's unclear

- **The malformed `.mcp.json`** — is Box meant to be the 12th connector (README prose says "11 data connectors" in one place, the table lists 12)? Worth reporting upstream; flagged to Sidney separately.
- **`callable_agents` is a "research preview"** with exactly **one** delegation level (orchestrator→workers, no deeper). How stable is the `/v1/agents` shape these cookbooks target? This artifact sits on a moving API.
- **Do the two surfaces ever silently diverge on *tools*?** The plugin prompt's `tools:` frontmatter and the `agent.yaml` toolset blocks are specified separately; the drift check covers skills, not necessarily this.
- **Per-skill licensing** (S&P) inside an Apache-2.0 repo — how does a consumer reason about mixed licenses pulled in by one `plugin install`?
- **Relevance to Sidney's catalog-deal work** (worth a future analysis): `gl-reconciler`, `statement-auditor`, `valuation-reviewer`, and PE skills like `ic-memo` / `returns-analysis` (IRR/MOIC) / `dd-checklist` are near-isomorphic to music-catalog royalty audit, NAV tie-out, and IC-memo workflows. The **trust-tiered reader for untrusted counterparty statements** maps almost directly onto ingesting third-party royalty statements of unknown provenance — a concrete pattern to lift into the catalog-research wiki.
