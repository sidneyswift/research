---
domain: artifacts
type: plugin
name: openai-curated
creator: "[[creators/openai]]"
source: "[[sources/openai--plugins]]"
ecosystem: codex (OpenAI Codex CLI plugins — NOT Claude Code)
discovered-via: user-curated (Sidney pasted the repo link)
marketplace-listing: ".agents/plugins/marketplace.json (name: openai-curated, display: \"Codex official\")"
status: active
last-reviewed: 2026-06-02
ingestion-mode: full
license: per-plugin (no repo-level license)
components:
  plugins-registered: 167
  categories: 6              # Productivity 85, Developer Tools 38, Research 29, Design 9, Lifestyle 5, Security 1
  skill-bearing-plugins: 56
  skills: 479               # SKILL.md files across the repo
  app-backed-plugins: 144   # .app.json (hosted OpenAI connector by id)
  mcp-plugins: 2            # cloudflare (remote http), build-ios-apps (local stdio)
  command-bearing-plugins: 6
  agents-dir-plugins: 14    # mostly agents/openai.yaml presentation manifests; figma has real agent .md
  hooks-plugins: 1         # figma (PostToolUse Write|Edit → parity check)
  openai-authored: 27      # remainder (~140) partner/vendor-authored
popularity-signals:
  - signal: github-stars
    value: 1334
    as-of: 2026-06-02
    source: "[[sources/openai--plugins#root]]"
  - signal: official-openai
    value: "Codex's official 'openai-curated' marketplace under github.com/openai"
    as-of: 2026-06-02
    source: "[[sources/openai--plugins#marketplace.json]]"
  - signal: frontier-recency
    value: "created 2026-03-04, last pushed 2026-06-02; HEAD bebc3d6 = 'Package Wix and Base44 plugins (#299)'"
    as-of: 2026-06-02
    source: "[[sources/openai--plugins#root]]"
---

# openai-curated — the Codex plugin marketplace

> **One-line:** OpenAI's official curated marketplace of **167 Codex plugins** — most are thin wrappers binding a hosted OAuth connector (`.app.json`) plus a skills layer that teaches Codex to drive it; a minority are large skill libraries (Twilio 55, Zoom 53, Vercel 47) or build kits (iOS/macOS/web/Expo). Its defining significance for this wiki is **convergence**: OpenAI independently shipped a plugin format near-identical to Anthropic's — same `skills/`/`commands/`/`agents/`/`hooks.json` grammar — wrapped in a far more *productized storefront* (install/auth policies, categories, `codex://` deeplinks, brand metadata). The first non-Claude-Code marketplace in the wiki.

## Attributes

- **Publisher**: OpenAI; marketplace name `openai-curated`, display name "Codex official" ([[sources/openai--plugins#marketplace.json]]). **OpenAI authors only 27** of the 167 plugins; ~140 are **partner/vendor-authored** (Mixpanel, HeyGen, Vercel Labs, Wix, ZoomInfo, Zoho, base44, airSlate, Windsor.ai, …) ([[sources/openai--plugins#authorship]]).
- **Target user**: Codex CLI users wanting one-click integrations with the SaaS tools they already use (issue trackers, mail/calendar, CRMs, data warehouses, design, research) — plus developers building app/web/mobile, who get skill-heavy build kits. Categories: Productivity 85, Developer Tools 38, Research 29, Design 9, Lifestyle 5, Security 1 ([[sources/openai--plugins#categories]]).
- **Component inventory** (by surface — the distribution is the analysis):
  - **`.app.json` hosted-connector binding — 144/167** ([[sources/openai--plugins#app-json]]). The dominant primitive: `{"apps":{"linear":{"id":"asdk_app_…"}}}` binds the plugin to a brokered OpenAI "app," OAuth'd on install. The plugin's skills assume those tools are connected (linear's skill literally has a "Step 0: connect the app").
  - **`.mcp.json` — 2 only** ([[sources/openai--plugins#mcp-json]]): `cloudflare` (remote HTTP MCP at `mcp.cloudflare.com`) and `build-ios-apps` (local `npx xcodebuildmcp`). Raw MCP is the **escape hatch** when no hosted app exists.
  - **Skills — 479 SKILL.md across 56 plugins** ([[sources/openai--plugins#skill-md]]): spectrum from 1-skill connector wrappers (`linear`) to large libraries (`twilio-developer-kit` 55, `zoom` 53, `life-science-research` 50, `vercel` 47). Identical anatomy to Anthropic skills.
  - **`agents/` — 14 plugins**, but mostly `agents/openai.yaml` *presentation* manifests (composer display metadata), **not** Anthropic-style agent system prompts. Only figma ships real agent `.md` files ([[sources/openai--plugins#agents-openai-yaml]], [[sources/openai--plugins#figma]]).
  - **`commands/` — 6 plugins**; **`hooks.json` — 1** (figma); **`plugin.lock.json` — 3**.
- **Install footprint**: file-based plugins (markdown + JSON) installed from the curated marketplace; each carries `policy.authentication: ON_INSTALL` so connectors OAuth at install time. Hosted apps need no local server; the 2 MCP plugins need either network OAuth (cloudflare) or local Node + Xcode (build-ios-apps) ([[sources/openai--plugins#mcp-json]]).
- **Plugin layout**: every plugin is `plugins/<name>/` with a required `.codex-plugin/plugin.json` + optional `skills/`, `.app.json`, `.mcp.json`, `agents/`, `commands/`, `hooks.json`, `assets/`, `scripts/`, `ui/` ([[sources/openai--plugins#README]]). The registry lives at `.agents/plugins/marketplace.json`; the meta-skill at `.agents/skills/plugin-creator/`.
- **License**: **no repo-level license** (`gh api` → `license: null`); 8 plugins ship their own `LICENSE`, e.g. figma's `LicenseRef-Figma-Developer-Terms`. Mixed/unclear for the unlicensed majority ([[sources/openai--plugins#licensing]]).

## Relationships

- **Creator**: [[creators/openai]] — OpenAI's second studied artifact (after [[artifacts/projects/codex-goals]]); the *packaging/distribution* Codex surface to Goals' *behavioral* one.
- **Source**: [[sources/openai--plugins#root]].
- **Cross-lab analog**: [[artifacts/plugins/anthropic-financial-services-marketplace]] (large Anthropic marketplace) and [[artifacts/plugins/anthropic-skills-marketplace]] (simplest). Same *marketplace-as-multi-plugin* mechanism; this one is bigger, more productized, and connector-app-first rather than skill-first.
- **Mechanism layer (the other lab's)**: [[sources/anthropic--plugins-reference]] — the convergence target; cite both for [[concepts/convergent-agent-plugin-spec]].
- **Depends on**: the Codex CLI + OpenAI's hosted-app/connector platform (`asdk_app_…` ids); for the 2 MCP plugins, Cloudflare's remote MCP / the `xcodebuildmcp` package.
- **Composes**: 167 child plugins — too many to page individually; standouts queued in [[artifacts/plugins/_index]] (figma, plugin-eval, superpowers, build-ios-apps, twilio-developer-kit).

## What problem it solves

Two jobs. (1) **Make Codex useful against the tools people already pay for** — without each user hand-wiring an MCP server. The `.app.json` binding turns "integrate Linear" into "install the Linear plugin, OAuth once," and the bundled skill turns raw connector tools into a guided workflow ("read/create/update tickets," with a connect-the-app preflight) ([[sources/openai--plugins#app-json]], [[sources/openai--plugins#skill-md]]). (2) **Give third parties a publishing platform.** ~140 of 167 plugins are vendor-authored: the repo is the supply side of a Codex app store, with OpenAI curating order and policy ([[sources/openai--plugins#authorship]], [[sources/openai--plugins#marketplace.json]]). A plugin earns its place by bundling a *coherent connector workflow* (the connector + the skill that drives it + storefront metadata), not a grab-bag.

## Composition strategy

The repo's signature is the **hosted-app + skill pairing**, and a hard split between *integration* and *behavior*:

1. **App = capability, skill = competence.** `.app.json` supplies the *tools* (via a brokered OAuth connector); `skills/<name>/SKILL.md` supplies the *know-how* to use them well (numbered workflows, prerequisites, a Step-0 connect check). Linear is the minimal case: a 1-line `.app.json` + one skill ([[sources/openai--plugins#app-json]], [[sources/openai--plugins#skill-md]]).
2. **Components auto-discovered, then *supplemented* by manifest paths.** The spec is explicit that `skills`/`hooks`/`mcpServers` manifest paths "are supplemented on top of default component discovery, not replacements" — i.e. drop a `skills/` dir and it's found by convention (same model as Anthropic) ([[sources/openai--plugins#component-discovery]]).
3. **Storefront metadata lives in the manifest.** The `interface{}` block carries displayName, category, capabilities, brandColor, screenshots, and ≤3 starter `defaultPrompt`s — the plugin card renders straight from `plugin.json` ([[sources/openai--plugins#interface-block]]).
4. **The registry encodes policy, not just a list.** Each `marketplace.json` entry carries `policy.installation` (NOT_AVAILABLE / AVAILABLE / INSTALLED_BY_DEFAULT), `policy.authentication` (ON_INSTALL / ON_USE), and `category`; array order = render order ([[sources/openai--plugins#plugin-json-spec]]).
5. **A meta-skill closes the loop.** `plugin-creator` scaffolds the whole shape (`create_basic_plugin.py`), writes/updates marketplace entries, and ends by handing the user **`codex://plugins/<name>?marketplacePath=…`** View/Share deeplinks — the authoring path is itself a productized Codex flow ([[sources/openai--plugins#plugin-creator]]).

**Where the lines are drawn**: *app* = the connector/tools; *skill* = the workflow that drives them (the bulk of the value); *commands* = explicit slash actions (rare — 6 plugins); *agents/openai.yaml* = composer presentation (not a subagent); *hooks* = deterministic post-action checks (used once: figma's parity check). MCP is reserved for when no hosted app fits.

## Worked example — `figma` (the richest plugin) and the connector taxonomy

**figma** is the one plugin that exercises nearly every primitive at once ([[sources/openai--plugins#figma]]): 7+ skills (`figma-use`, `figma-code-connect`, design-system-rules, generate-design/library/diagram/slides), **real agent `.md` files** (implementation, code-connect, design-parity-review, design-system-rules), 4 `commands/`, a `ui/figma-workbench.html`, its own `LICENSE.txt`, an `.app.json` binding the Figma connector — and **the repo's only `hooks.json`**, a `PostToolUse` hook matching `Write|Edit` that runs `post_write_figma_parity_check.sh` after every code write to check design parity ([[sources/openai--plugins#hooks-json]]). That hook is **byte-identical in schema to a Claude Code hook** — the single sharpest piece of convergence evidence.

The **connector taxonomy** is the other lesson — three tiers, in descending frequency:

| Tier | How tools arrive | Count | Example |
|---|---|---|---|
| **Hosted app** (`.app.json`) | brokered OpenAI connector by id, OAuth on install | 144 | `linear`, `gmail`, `slack`, `stripe`, `figma` |
| **Remote MCP** (`.mcp.json`, http) | official vendor-hosted MCP over HTTP | 1 | `cloudflare` (`mcp.cloudflare.com`) |
| **Local MCP** (`.mcp.json`, stdio) | spawn a local process | 1 | `build-ios-apps` (`npx xcodebuildmcp`) |

The hosted-app tier is the default; raw MCP appears only when there's no app to bind (a vendor's own remote MCP, or local-only tooling like Xcode) ([[sources/openai--plugins#app-json]], [[sources/openai--plugins#mcp-json]]).

## Patterns demonstrated

**Confirmed (this ingest adds an example):**
- [[patterns/structural/marketplace-as-multi-plugin]] — **167 plugins from one `marketplace.json`**; the 3rd in-wiki example and the first *outside Claude Code*. Generalizes the pattern across labs ([[sources/openai--plugins#marketplace.json]]).
- [[patterns/quality-bar/skill-pack-bundle]] — **`plugin-eval`** is a plugin whose *job* is scoring other plugins (token budgets, baselines, benchmark harness, result schema), and ships `tests/` — the Codex embodiment of "a skill pack has tests/evals" ([[sources/openai--plugins#plugin-eval]]).
- [[patterns/composition/single-source-multi-surface-distribution]] — **`plugin-eval` is dual-surface** ("both a local Node.js CLI and a Codex plugin bundle"); **Superpowers is cross-runtime** (same skills on Codex *and* Claude Code) ([[sources/openai--plugins#plugin-eval]], [[sources/openai--plugins#superpowers]]).

**Confirmed (reinforced):**
- [[patterns/structural/thin-harness-fat-skills]] — Codex is another **thin harness** carrying fat markdown skills + thin deterministic scripts (figma's parity check); the first ingested *non-Anthropic* harness, which fills that pattern's missing-harness gap.

**Proposed (strong here; need a 2nd in-wiki example to confirm):**
- **Hosted-app connector binding** — bind to a brokered, OAuth-on-install connector by opaque id (`.app.json`) instead of self-hosting/configuring an MCP server. A distinct distribution+auth model from Anthropic's `.mcp.json`. *The single most novel structural idea in this repo.* ([[sources/openai--plugins#app-json]])
- **Productized storefront manifest** — bake install policy, auth timing, category, brandColor, screenshots, and starter prompts into the manifest so the marketplace card + deeplinks render from one file ([[sources/openai--plugins#interface-block]], [[sources/openai--plugins#plugin-creator]]).
- **Curated third-party plugin platform** — ~140 vendor-authored plugins under one curated registry (vs financial-services' 2 partner plugins). Escalates the "partner-contributed plugins" idea from *exception* to *dominant mode* ([[sources/openai--plugins#authorship]]).
- **Meta-skill that scaffolds + registers + deeplinks** — `plugin-creator` automates the whole authoring path and ends with a `codex://` app handoff ([[sources/openai--plugins#plugin-creator]]). (Relative of Anthropic's skill-creator, which it cites for naming rules.)

## Source citations

- [[sources/openai--plugins#marketplace.json]] — 167-entry registry, policy blocks, render order
- [[sources/openai--plugins#app-json]] / [[sources/openai--plugins#mcp-json]] — connector taxonomy (144 hosted apps, 2 MCP)
- [[sources/openai--plugins#plugin-json]] / [[sources/openai--plugins#interface-block]] — manifest + storefront metadata
- [[sources/openai--plugins#component-discovery]] — auto-discovery + supplemental paths (matches Anthropic)
- [[sources/openai--plugins#hooks-json]] — figma's PostToolUse hook, identical to Claude Code's schema
- [[sources/openai--plugins#plugin-creator]] / [[sources/openai--plugins#plugin-json-spec]] — meta-skill, deeplinks, policy values
- [[sources/openai--plugins#plugin-eval]] / [[sources/openai--plugins#superpowers]] — eval meta-plugin, cross-runtime skill pack
- [[sources/openai--plugins#figma]] / [[sources/openai--plugins#build-kits]] — flagship + skill-library spectrum
- [[sources/openai--plugins#authorship]] / [[sources/openai--plugins#categories]] / [[sources/openai--plugins#licensing]] — publishing platform, categories, mixed licensing

## What makes it great

The repo answers a question Anthropic's marketplaces mostly leave to the developer: **how does a non-technical user get a working integration?** The `.app.json` + skill pairing makes "install Linear" a one-OAuth operation, and the bundled skill means the model already knows the good workflow instead of fumbling raw tools. Layered on top is a genuinely *productized* storefront — categories, install/auth policy, brand cards, starter prompts, and even `codex://` View/Share deeplinks emitted by the authoring skill — so the same artifact is both a dev repo and a consumer app store. And it does this **at 167 plugins, ~140 of them third-party**, which is itself the proof that the format is learnable and publishable by outsiders. The convergence with Anthropic's spec (down to an identical hook grammar) is the deeper "great": it's strong evidence that the plugin/skill shape is becoming an industry standard rather than one lab's house style.

## What we'd steal

**Exhaustive ledger — ★ marks highest-value.**

- ★ **Hosted-app connector binding (`.app.json`).** Bind an integration to a brokered, OAuth-on-install connector by id, and pair it with a skill that drives it — so users get a working tool with one auth step, not a server to configure. The cleanest "integration as a product" primitive in the wiki.
- ★ **Convergence as a portability bet.** Because Codex and Claude Code plugins share grammar (skills, hooks `PostToolUse`/`matcher`, `.mcp.json`, marketplace registry), authoring to the common subset buys you both runtimes — exactly what Superpowers demonstrates. Author skills to the lab-agnostic core, branch only where forced.
- ★ **`plugin-eval` as a model for our own eval gate.** A token-budget-aware evaluator that scores a skill/plugin, explains *why* it scored that way, says *what to fix first*, and runs as both a CLI and a chat-first skill. Maps directly onto this wiki's `analyses/_eval-rubric.md` + `wiki-doctor.py` ambitions (see [[meta/self-improvements]]).
- ★ **App = capability, skill = competence** as a design rule: keep the tool-granting layer (connector) separate from the know-how layer (skill workflow), so either can change without the other.
- **Storefront metadata in the manifest** — displayName/category/capabilities/brandColor/screenshots/`defaultPrompt` so a card and deeplinks render from one source (no parallel registry to drift). `defaultPrompt` capped at ≤3 / ≤128 chars / ~50 preferred is a nice concrete UX constraint.
- **Policy in the registry** — `installation` (NOT_AVAILABLE / AVAILABLE / INSTALLED_BY_DEFAULT) and `authentication` (ON_INSTALL / ON_USE) as first-class fields; array order = render order. A tiny, expressive governance vocabulary for a catalog.
- **The connect-the-app preflight (Step 0)** — a skill that begins by checking its connector is available and, if not, pauses and tells the user how to connect + retry. Graceful degradation when the tool layer is missing.
- **Deterministic post-action hook for an invariant** — figma's `PostToolUse: Write|Edit → parity check` runs a check after every code write rather than trusting the model to remember. Port the "hook the invariant, don't prompt it" move.
- **Meta-skill that scaffolds + registers + hands off** — `plugin-creator` writes the manifest, updates the marketplace, and emits a `codex://` View/Share link. The authoring path is itself a guided product.
- **Reusing skill-creator naming rules across tools** — one normalization spec (`My Plugin` → `my-plugin`) shared by skill-creator and plugin-creator; don't re-derive naming per tool.
- **Per-asset constraints written into the spec** — screenshots must be PNG under `./assets/`, paths relative + `./`-prefixed. Make packaging rules machine-checkable.
- **Curated third-party platform shape** — a single `marketplace.json` owner curates order/policy while outside vendors author the plugins. A model for any org wanting partners to extend its agent.

## Weird / surprising things

- **No repo-level license, but partner plugins carry their own.** The root repo returns `license: null`; figma ships `LicenseRef-Figma-Developer-Terms`, 7 others ship a `LICENSE` — a consumer pulling several plugins inherits a patchwork of terms with no umbrella ([[sources/openai--plugins#licensing]]). (Same mixed-license puzzle flagged on the S&P partner plugin in financial-services.)
- **`agents/` usually isn't agents.** 14 plugins have an `agents/` dir, but it's overwhelmingly `agents/openai.yaml` *presentation* manifests, not subagent prompts — a naming collision with the Anthropic meaning. Only figma uses `agents/` for real agent `.md` files ([[sources/openai--plugins#agents-openai-yaml]]).
- **Hooks barely used.** Every primitive exists, but `hooks.json` appears in exactly **one** plugin — the slot is reserved but almost entirely unexercised (mirrors financial-services, where hooks were a present-but-empty stub).
- **A third party's whole framework lives inside OpenAI's repo.** `superpowers` is Jesse Vincent's externally-developed methodology vendored verbatim into `openai/plugins` — and the same skills run in Claude Code ([[sources/openai--plugins#superpowers]]).
- **Opaque connector ids.** `.app.json` references apps as `asdk_app_69a089a3…` — meaningful only to OpenAI's backend; the binding is unresolvable from the repo alone ([[sources/openai--plugins#app-json]]).

## Open questions / what's unclear

- **What is the hosted-app platform?** `asdk_app_…` ids imply an "App SDK"/connector registry behind Codex. Its trust model, tool schemas, and whether third parties self-register apps is invisible from the repo — a key thing to chase (the connector layer is where the security questions live).
- **How do hosted apps handle untrusted input / prompt injection?** financial-services answered this explicitly with trust-tiered subagents; this repo's connector-first model doesn't surface an analogous containment story. Worth comparing.
- **Stability of the `.codex-plugin/` spec.** Repo is 3 months old and pushed daily; `plugin.lock.json` (3 plugins) hints at an evolving resolution model. How settled is the manifest?
- **Does `plugin-eval`'s scoring rubric generalize?** Its `references/` (metric-pack-manifest, evaluation-result-schema) are a candidate to mine for our own eval gate — a future QUERY/REFLECT target.
- **Cross-runtime drift.** Superpowers runs on both labs today; how much per-runtime branching does cross-platform authoring actually require? (CE's converter answered this for Claude→N platforms; the inverse, author-to-common-core, is what Superpowers tests.)
