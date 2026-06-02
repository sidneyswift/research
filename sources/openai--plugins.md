---
domain: sources
type: repo
url: https://github.com/openai/plugins
retrieved: 2026-06-02
snapshot-location: sources/openai--plugins/
upstream-commit: bebc3d6a757ca882fd2436210b6b1ae5263b437b
upstream-commit-date: 2026-06-01
last-reviewed: 2026-06-02
license: # n/a at repo level — per-plugin licenses (see #licensing)
marketplace-name: openai-curated
marketplace-display: Codex official
---

# OpenAI Plugins (`openai/plugins`)

> OpenAI's official curated marketplace of **Codex** plugins — **167 plugins** registered in one `marketplace.json`, spanning hosted-connector integrations (Linear, Gmail, Slack, Stripe, Figma…) and skill-heavy build kits (iOS/macOS/web apps, Expo, Vercel, Twilio). The headline finding: OpenAI has shipped a **plugin spec that is near-identical to Anthropic's** — `skills/`, `commands/`, `agents/`, `hooks.json` (same `PostToolUse`/`matcher` grammar), `.mcp.json`, and a `marketplace.json` registry — but under its own `.codex-plugin/` namespace and with a far more *productized storefront* layer (install/auth policies, categories, `codex://` deeplinks, brand metadata). The repo's dominant integration primitive is **`.app.json`** — a binding to a hosted, OAuth-on-install OpenAI "app" (144/167 plugins), with raw `.mcp.json` reserved for the 2 exceptions that need it.

## Snapshot details

- **Retrieved**: 2026-06-02
- **Location**: `sources/openai--plugins/` (4,580 files, `.git/` kept as a live clone; git-ignored from the wiki, listed in `repos.manifest.tsv`)
- **Upstream URL**: https://github.com/openai/plugins
- **Upstream commit**: `bebc3d6` (2026-06-01, "[codex] Package Wix and Base44 plugins (#299)")
- **Repo created**: 2026-03-04 (≈3 months old at snapshot)
- **License**: **none at repo level** (`gh api` returns `license: null`); plugins carry their own licenses where present (see `#licensing`)
- **Publisher**: OpenAI (the marketplace is named `openai-curated`, display name "Codex official")

## Anchor map

Citations into this source must use an anchor registered below.

### Root + registry
- `#root` — the repo as a whole
- `#README` — top-level `README.md`: "a curated collection of Codex plugin examples," the `plugins/<name>/` layout with required `.codex-plugin/plugin.json` and optional `skills/`, `.app.json`, `.mcp.json`, `agents/`, `commands/`, `hooks.json`, `assets/`; lists the "richer examples" (figma, notion, build-ios-apps, build-macos-apps, build-web-apps, expo, netlify, remotion, google-slides)
- `#marketplace.json` — `.agents/plugins/marketplace.json`: the registry. `name: openai-curated`, `interface.displayName: "Codex official"`, and an **ordered `plugins[]` of 167 entries**, each `{name, source:{source:local, path}, policy:{installation, authentication}, category}`. Order = render order in Codex
- `#categories` — the 6 marketplace categories + counts (Productivity 85, Developer Tools 38, Research 29, Design 9, Lifestyle 5, Security 1)
- `#licensing` — per-plugin licensing: 8 plugins ship a `LICENSE`/`LICENSE.txt`; figma uses `LicenseRef-Figma-Developer-Terms`; most plugins carry no license file; repo root has none

### Manifest + spec (the `.codex-plugin/` format)
- `#plugin-json` — the per-plugin `.codex-plugin/plugin.json`. Top-level: `name`, `version`, `description`, `author{name,email,url}`, `homepage`, `repository`, `license`, `keywords[]`, plus **component paths** `skills`, `hooks`, `mcpServers`, `apps`, and a rich **`interface{}`** storefront block. Exemplar: `plugins/figma/.codex-plugin/plugin.json` (version `2.0.7`)
- `#interface-block` — the `interface{}` storefront metadata: `displayName`, `shortDescription`, `longDescription`, `developerName`, `category`, `capabilities[]` (Interactive/Read/Write), `websiteURL`, `privacyPolicyURL`, `termsOfServiceURL`, `defaultPrompt[]` (≤3, ≤128 chars each, ~50 preferred), `brandColor`, `composerIcon`, `logo`, `screenshots[]` (PNG under `./assets/`)
- `#plugin-creator` — `.agents/skills/plugin-creator/SKILL.md`: OpenAI's **meta-skill that scaffolds plugins** (`scripts/create_basic_plugin.py`), manages `marketplace.json` entries (personal `~/.agents/plugins/marketplace.json` vs repo `<root>/.agents/plugins/marketplace.json`), and emits **`codex://plugins/<name>?marketplacePath=…`** View/Share deeplinks as a Codex-app handoff. Explicitly reuses "skill-creator naming rules"
- `#plugin-json-spec` — `.agents/skills/plugin-creator/references/plugin-json-spec.md`: the canonical `plugin.json` + `marketplace.json` sample + field guide. Documents `policy.installation` ∈ {NOT_AVAILABLE, AVAILABLE, INSTALLED_BY_DEFAULT}, `policy.authentication` ∈ {ON_INSTALL, ON_USE}, `policy.products` override
- `#component-discovery` — spec note: `skills`/`hooks`/`mcpServers` paths are **supplemented on top of default component discovery, not replacements** — i.e. components are auto-discovered by directory convention (same model as Anthropic's plugins)

### Components (the surfaces)
- `#app-json` — `.app.json`: binds a plugin to a **hosted OpenAI "app"/connector by opaque id**, e.g. `{"apps":{"linear":{"id":"asdk_app_69a089a326dc8191b32a3f2553f5be2c"}}}`. Present in **144/167** plugins — the dominant integration primitive. App is OAuth'd on install; skills assume its tools are connected
- `#mcp-json` — `.mcp.json`: only **2 plugins**. `cloudflare` → a **remote HTTP MCP** (`https://mcp.cloudflare.com/mcp`, OAuth + optional bearer, "token-efficient access via search() and execute()"); `build-ios-apps` → a **local stdio MCP** (`npx -y xcodebuildmcp@latest mcp`, workflows env-gated to `simulator,ui-automation,debugging,logging`). Same `mcpServers{}` schema as Claude Code
- `#skill-md` — per-skill `skills/<name>/SKILL.md`: identical anatomy to Anthropic skills — YAML frontmatter (`name`, `description` with "Use when…" trigger), body, optional `references/`, `assets/`, `scripts/`, and a per-skill `agents/openai.yaml`. **479 SKILL.md files** across 56 skill-bearing plugins. Exemplar: `plugins/linear/skills/linear/SKILL.md` (a numbered "Required Workflow," Step 0 = connect the app)
- `#agents-openai-yaml` — `agents/openai.yaml`: **a presentation manifest, not an Anthropic-style agent prompt** — `interface{display_name, short_description, icon_small, icon_large, default_prompt}` for how the skill/plugin surfaces in the Codex composer. (Distinct from figma's real agent `.md` files under `#figma`.)
- `#hooks-json` — `hooks.json`: only **1 plugin** (figma). Schema is **byte-identical to Claude Code's**: `{"hooks":{"PostToolUse":[{"matcher":"Write|Edit","hooks":[{"type":"command","command":"./scripts/post_write_figma_parity_check.sh"}]}]}}`
- `#plugin-lock` — `plugin.lock.json`: a lockfile present in 3 plugins (figma, …) — pins resolved plugin state

### Standout child plugins (exemplars)
- `#figma` — `plugins/figma/` (Figma-authored, v2.0.7): the **flagship richest example** — 7+ skills (`figma-use`, `figma-code-connect`, design-system-rules, generate-design/library/diagram/slides), real `agents/*.md` (implementation, code-connect, design-parity-review, design-system-rules), 4 `commands/`, the only `hooks.json` (post-write parity check), a `ui/figma-workbench.html`, `.app.json` (Figma connector), and `LICENSE.txt`. README: "app-backed through `.app.json`"
- `#plugin-eval` — `plugins/plugin-eval/`: a **meta-plugin that evaluates other Codex skills/plugins** — "both a local Node.js CLI and a Codex plugin bundle." Real `src/` (`core/scoring.js`, `budget.js`, `baseline.js`, `benchmark.js`, `measurement-plan.js`, `analyze.js`, `compare.js`; `renderers/html|markdown`), `tests/`, and `references/` (benchmark-harness, metric-pack-manifest, evaluation-result-schema, chat-first-workflows). "Chat-first… while still routing to explicit local commands." Token-budget-aware
- `#superpowers` — `plugins/superpowers/`: **Jesse Vincent's (obra's) Superpowers framework, ported to Codex** (author `Jesse Vincent <jesse@fsck.com>`, github.com/obra). 14 skills — `brainstorming`, `test-driven-development`, `systematic-debugging`, `writing-plans`, `executing-plans`, `subagent-driven-development`, `using-git-worktrees`, `verification-before-completion`, `writing-skills`, `dispatching-parallel-agents`, `receiving/requesting-code-review`, `finishing-a-development-branch`, `using-superpowers`. The **same skill names also run in Claude Code** (cross-platform skill pack)
- `#build-kits` — the skill-library end of the spectrum: `twilio-developer-kit` (55 skills), `zoom` (53), `life-science-research` (50), `vercel` (47), `build-web-data-visualization` (18), `expo` (13), `netlify` (12), `build-macos-apps` (11). These are large skill libraries, not thin connector wrappers
- `#authorship` — author diversity: **OpenAI authors 27** plugins; ~140 are **partner/vendor-authored** (Mixpanel, HeyGen, Vercel Labs, Wix, ZoomInfo, Zoom, Zoho, base44, airSlate, Windsor.ai, Vantage, United Rentals, …) — the marketplace is a third-party publishing platform, OpenAI-curated

## Why we cite this

- **Convergent cross-lab plugin spec** — the strongest reason. Two independent frontier labs (Anthropic `.claude-plugin/`, OpenAI `.codex-plugin/`) ship near-identical plugin grammar: auto-discovered `skills/`/`commands/`/`agents/`, the same `hooks.json` `PostToolUse`/`matcher` shape, `.mcp.json`, and a `marketplace.json` registry. Grounds [[concepts/convergent-agent-plugin-spec]]. ([[sources/openai--plugins#hooks-json]], [[sources/openai--plugins#component-discovery]], [[sources/openai--plugins#skill-md]])
- **Marketplace-as-multi-plugin at unprecedented scale** — 167 plugins in one registry; the 3rd and largest in-wiki example, and the first **outside the Claude Code ecosystem**. ([[sources/openai--plugins#marketplace.json]]) → [[patterns/structural/marketplace-as-multi-plugin]]
- **Hosted-app connector binding (`.app.json`)** — a distinct distribution/auth model from self-hosted MCP: bind to a brokered OAuth app by opaque id, OAuth on install. ([[sources/openai--plugins#app-json]])
- **Productized app-store storefront** — install policies, auth timing, categories, render-order, `codex://` deeplinks, View/Share handoffs, brand/screenshot/defaultPrompt metadata baked into the manifest. ([[sources/openai--plugins#interface-block]], [[sources/openai--plugins#plugin-creator]])
- **A meta-plugin for evaluating plugins** — `plugin-eval` with token-budget accounting, baselines, and benchmark harnesses: the Codex embodiment of "a skill pack has tests/evals." ([[sources/openai--plugins#plugin-eval]]) → [[patterns/quality-bar/skill-pack-bundle]]
- **Cross-platform-portable skill packs** — Superpowers runs on both Codex and Claude Code from the same skill set. ([[sources/openai--plugins#superpowers]])
- **Codex as a "thin harness"** — the harness whose fat markdown skills carry the value; first ingested non-Anthropic harness. → [[patterns/structural/thin-harness-fat-skills]]
- **Partner-contributed plugins as the dominant mode** — ~140 vendor-authored plugins (vs financial-services' 2). ([[sources/openai--plugins#authorship]])

## Popularity / authority signals

- **Official OpenAI** — published under `github.com/openai`; the "Codex official" curated marketplace. Authoritative by definition for the Codex plugin surface.
- **GitHub stars**: **1,334** (forks 200, 30 open issues) as-of 2026-06-02 (`gh api repos/openai/plugins`). ~3 months old (created 2026-03-04), last pushed 2026-06-02 — an actively-developed, fast-moving repo.
- **Frontier recency** — commit `bebc3d6` of 2026-06-01 was literally "Package Wix and Base44 plugins (#299)"; the catalog is still growing weekly.

## Related sources

- [[sources/anthropic--plugins-reference]] — the **Anthropic** plugin spec (`plugin.json`, `${CLAUDE_PLUGIN_ROOT}`, components, marketplace). The other half of the convergence evidence for [[concepts/convergent-agent-plugin-spec]]; cite both together.
- [[sources/openai--using-goals-in-codex]] — the other OpenAI/Codex source. Codex Goals (`/goal`) is a *behavioral* Codex surface; this repo is the *packaging/distribution* Codex surface. Same creator, same CLI, different layer.
- [[sources/anthropic--financial-services]] — the closest Anthropic analog (a large marketplace); useful for contrasting **hosted-app vs self-config-MCP** connectors and **2 partner plugins vs ~140**.
- [[sources/anthropic--skills]] — the simplest Anthropic marketplace (skills-only); the SKILL.md anatomy this repo mirrors.

## Related wiki pages

- [[creators/openai]] — publisher of this repo
- [[artifacts/plugins/openai-codex-plugins-marketplace]] — the artifact page distilled from this source
- [[concepts/convergent-agent-plugin-spec]] — the concept this source co-grounds
