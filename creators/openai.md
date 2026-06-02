---
domain: creators
type: org
name: OpenAI
handle: openai
url: https://openai.com
last-reviewed: 2026-06-02
---

# OpenAI

> The lab behind GPT and the **Codex** agentic-coding CLI. In this wiki, OpenAI is the **first non-Anthropic / non-Garry-Tan creator** — and now the first creator studied on **two different layers of the same CLI**: a *behavioral* surface (Codex **Goals**) and a *packaging/distribution* surface (the **167-plugin Codex marketplace**, `openai/plugins`).

**Scope note:** this page is grounded in the **two** OpenAI sources ingested so far ([[sources/openai--using-goals-in-codex]], [[sources/openai--plugins]]) — both about the Codex CLI. OpenAI's broader catalog (GPT model family, the API, ChatGPT, the rest of the Codex CLI internals) is **context, not yet studied** — claims below stay close to what those sources support.

## Attributes

- **What they ship (studied here)**: the **Codex CLI** — an agentic coding tool installed via `npm i -g @openai/codex` or `brew … codex` — its **Goals** feature (persistent, evidence-verified objectives via `/goal`, shipped in Codex **0.128.0** — [[sources/openai--using-goals-in-codex#lifecycle-commands]]), and the **Codex plugin platform**: a `.codex-plugin/` plugin spec + an official **167-plugin curated marketplace** (`openai/plugins`, "Codex official"), plus the `plugin-creator` meta-skill that scaffolds and registers plugins ([[sources/openai--plugins#marketplace.json]], [[sources/openai--plugins#plugin-creator]]).
- **What they ship (context, unstudied)**: GPT model family, the OpenAI API, ChatGPT, and the **OpenAI Cookbook** (`developers.openai.com/cookbook`, backed by the public `openai/openai-cookbook` repo) — a widely-referenced library of first-party how-to guides.
- **Distribution channels**: `developers.openai.com` (docs + cookbook), `github.com/openai` (incl. `openai-cookbook`), npm (`@openai/codex`), Homebrew.
- **Position in ecosystem**: a frontier lab and the **counterweight to Anthropic** in this wiki's scope — useful precisely because it lets us check whether a "pattern" is field-level or just one ecosystem's house style. The Codex Goals source already did this work: it supplied the **non-Garry** documented-parameter-signature that promoted [[patterns/behavioral/skill-as-method-call]].
- **House style (discernible from one source)**: cookbook guides are authored (named bylines), versioned in a public repo, and notably **scope their own technique** — the Goals guide ships an explicit "when NOT to use" section and a weak→strong worked example ([[sources/openai--using-goals-in-codex#when-not-to-use]], [[sources/openai--using-goals-in-codex#weak-vs-strong-perf]]).

## Artifacts produced

### Plugins
- [[artifacts/plugins/openai-codex-plugins-marketplace]] — the official **Codex plugin marketplace** (`openai/plugins`): 167 plugins (mostly hosted-connector `.app.json` wrappers + a skills layer), the `.codex-plugin/` manifest with a productized storefront, and the `plugin-creator` meta-skill. The wiki's first non-Claude-Code marketplace. ([[sources/openai--plugins#root]])

### Projects
- [[artifacts/projects/codex-goals]] — the Goals feature of the Codex CLI: persistent, thread-scoped, evidence-gated objectives via the `/goal` command surface. *(The broader Codex CLI internals — model, sandboxing, approval — remain queued in [[artifacts/projects/_index]] and unstudied.)*

### Concepts originated / popularized
- [[concepts/completion-contract]] — the crisp framing of an agent objective as a "scoped, user-controlled completion contract," named in the Goals guide.
- [[concepts/convergent-agent-plugin-spec]] — *co-grounds* (with Anthropic): OpenAI's `.codex-plugin/` format is near-identical to Anthropic's `.claude-plugin/` (same skills/hooks/MCP/marketplace grammar), evidence that the agent plugin shape is consolidating across labs. OpenAI's `plugin-creator` even cites "skill-creator naming rules" ([[sources/openai--plugins#plugin-creator]]).

## Design philosophy (discernible from artifacts)

- **Autonomy on a leash.** The standout choice in the one artifact we've studied: a "keep working until done" loop fenced by budget accounting, a conservative event-driven dispatcher (with explicit anti-spin), evidence-gated completion, and user-held lifecycle authority — foregrounding the *constraints*, not the autonomy ([[sources/openai--using-goals-in-codex#completion-contract-architecture]], [[sources/openai--using-goals-in-codex#event-driven-continuation]]).
- **Evidence over confidence.** Completion is defined as an audit against concrete artifacts, never the model's self-assessment ([[sources/openai--using-goals-in-codex#evidence-based-completion]]).
- **Documentation that scopes itself.** The Goals guide tells you when *not* to use the feature and grades research output by epistemic level (confirmed / approximate / blocked / uncertain) rather than flattening to "done" ([[sources/openai--using-goals-in-codex#when-not-to-use]], [[sources/openai--using-goals-in-codex#epistemic-levels]]).

## Source citations

- [[sources/openai--using-goals-in-codex#root]] — the Codex Goals cookbook guide (authors Raj Pathak, Stefano Fabbri; published 2026-05-09; notebook commit `9b4e627`).
- [[sources/openai--using-goals-in-codex#lifecycle-commands]] — Codex CLI version (0.128.0) + install channels (npm / Homebrew).
- [[sources/openai--using-goals-in-codex#completion-contract-architecture]] — the "completion contract" framing.
- [[sources/openai--plugins#marketplace.json]] — the 167-plugin Codex marketplace registry ("openai-curated" / "Codex official").
- [[sources/openai--plugins#app-json]] — hosted-app connector binding (`asdk_app_…`), the dominant integration primitive (144/167).
- [[sources/openai--plugins#plugin-creator]] — the `plugin-creator` meta-skill, `codex://` deeplinks, and the "skill-creator naming rules" reference.
- [[sources/openai--plugins#hooks-json]] — figma's `PostToolUse`/`matcher` hook, schema-identical to Claude Code (the convergence exhibit).

## Open questions / what to study next

- **The hosted-app / connector platform behind `.app.json`.** 144 plugins bind apps by opaque `asdk_app_…` ids ([[sources/openai--plugins#app-json]]) — an "App SDK"/connector registry whose trust model, tool schemas, and third-party registration are invisible from the repo. This is where Codex's integration *and* its security story live; the single highest-value next OpenAI ingest.
- **The rest of the Codex CLI** — model, sandboxing, approval model, tool surface. The *distribution* layer is now studied (plugins/marketplace); the *runtime* (the harness loop, the sandbox) is not. One full ingest would let us compare Codex vs. Claude Code head-to-head and finally inspect a real "thin harness" ([[patterns/structural/thin-harness-fat-skills]]).
- **Is the plugin-spec convergence deliberate or independent?** OpenAI's `plugin-creator` cites Anthropic's "skill-creator naming rules" ([[sources/openai--plugins#plugin-creator]]) — so at least partly deliberate. How much of the `.codex-plugin/` shape is adoption vs. parallel invention? (Tracked on [[concepts/convergent-agent-plugin-spec]].)
- **Does OpenAI name patterns the way Anthropic/Garry do?** Two sources still isn't enough to read a house vocabulary. More ingests would tell us whether "completion contract" is an OpenAI coinage or field-wide.
- **The OpenAI Cookbook as a source vein** — it's a large, first-party, repo-backed library of agent/AI guides; likely a rich future ingest target (it's how we found this one).
