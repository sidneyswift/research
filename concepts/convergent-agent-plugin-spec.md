---
domain: concepts
type: concept
name: convergent-agent-plugin-spec
creators:
  - "[[creators/anthropic]]"
  - "[[creators/openai]]"
sources:
  - "[[sources/openai--plugins]]"
  - "[[sources/anthropic--plugins-reference]]"
status: emerging
last-reviewed: 2026-06-02
popularity-signals:
  - signal: adoption
    value: "Two frontier labs ship the format: Anthropic (.claude-plugin/, Claude Code) and OpenAI (.codex-plugin/, Codex — 167 plugins, 1,334★)"
    as-of: 2026-06-02
    source: "[[sources/openai--plugins#marketplace.json]]"
---

# convergent-agent-plugin-spec

> **One-line:** Two independent frontier labs have shipped agent **plugin formats that are near-identical** — directory-discovered `skills/` / `commands/` / `agents/`, the *same* `hooks.json` (`PostToolUse` + `matcher` + `type: command`) grammar, a `.mcp.json` for MCP servers, and a `marketplace.json` registry — differing mainly in namespace (`.claude-plugin/` vs `.codex-plugin/`) and in how connectors and storefronts are handled. The plugin/skill *shape* is becoming a de-facto cross-lab standard rather than one vendor's house style.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): the convergence as it reads across both labs' specs, written as distilled judgment. Shape: **compiled truth on top** + an **append-only `## Timeline`** below.*

## What it is

Independently of each other, Anthropic's Claude Code and OpenAI's Codex package agent capabilities the same way: a **plugin** is a directory with a small JSON manifest plus convention-named component folders that the harness auto-discovers. The overlapping core, observed in both:

- **A manifest** — `.claude-plugin/plugin.json` / `.codex-plugin/plugin.json` — carrying `name` (required), `version`, `description`, `author`, with most fields optional and components found by directory convention ([[sources/anthropic--plugins-reference#manifest]], [[sources/openai--plugins#plugin-json]], [[sources/openai--plugins#component-discovery]]).
- **Skills** — `skills/<name>/SKILL.md` with YAML frontmatter (`name`, a "Use when…" `description`) + body + optional `references/`/`scripts/`/`assets/`. The anatomy is the same on both ([[sources/openai--plugins#skill-md]]).
- **Hooks** — `hooks.json` with the **identical schema**: `{"hooks":{"PostToolUse":[{"matcher":"Write|Edit","hooks":[{"type":"command","command":"…"}]}]}}` (Codex/figma) maps one-to-one onto Claude Code's hook events ([[sources/openai--plugins#hooks-json]], [[sources/anthropic--plugins-reference#components]]).
- **MCP servers** — a `.mcp.json` with the same `mcpServers{}` shape (stdio `command`/`args`/`env` or remote `type:http`/`url`) ([[sources/openai--plugins#mcp-json]]).
- **A marketplace registry** — `marketplace.json` listing N plugins, enabling one repo to ship many à-la-carte plugins ([[sources/openai--plugins#marketplace.json]], [[sources/anthropic--plugins-reference#marketplace-symlinks]]).

It is **convergence, not a shared standard body**: there is no joint spec. The formats agree because they're solving the same problem against models trained on overlapping conventions — which is exactly what makes the agreement interesting.

## Where it came from

Anthropic defined the Claude Code plugin/skill spec first (the `plugin.json` manifest, `${CLAUDE_PLUGIN_ROOT}`, component discovery, marketplaces — [[sources/anthropic--plugins-reference#root]]). OpenAI's `openai/plugins` repo (created 2026-03-04; 167 plugins, 1,334★ by 2026-06-02) ships the Codex equivalent under `.codex-plugin/` ([[sources/openai--plugins#root]]). OpenAI's own tooling makes the lineage partly **explicit**: the `plugin-creator` skill says plugin names are "normalized using **skill-creator naming rules**" — i.e. it references the same naming convention Anthropic's skill-creator uses ([[sources/openai--plugins#plugin-creator]]). So the convergence is a mix of *independent re-derivation* (same problem, same model priors) and *deliberate compatibility* (OpenAI adopting recognizable conventions) — the page's central uncertainty (see Tensions).

## Why it matters

If the plugin shape is a cross-lab standard, three things follow for anyone building agent tooling:

1. **Portability becomes a design target, not a fantasy.** Author skills to the common subset and they run on both harnesses — demonstrated in this wiki by `superpowers`, whose skill set runs on Codex *and* Claude Code ([[sources/openai--plugins#superpowers]]), and by [[artifacts/plugins/compound-engineering]], which converts one Claude-format source to ~11 platforms. Two directions of the same bet: author-to-common-core (Superpowers) and author-then-convert (CE).
2. **Patterns generalize.** A technique observed in a Claude Code plugin is more likely *field-level* than *house style* once the same primitive exists in Codex — which is why this ingest let [[patterns/structural/marketplace-as-multi-plugin]] and [[patterns/structural/thin-harness-fat-skills]] shed their single-ecosystem caveats.
3. **The divergences become the signal.** Where the two formats *don't* agree is where each lab is making a real bet — connectors and storefront (below).

## The divergences (where the bets are)

Convergence on the *component grammar*; divergence on *distribution + connectors* ([[sources/openai--plugins#app-json]], [[sources/openai--plugins#interface-block]]):

| Axis | Anthropic (Claude Code) | OpenAI (Codex) |
|---|---|---|
| Namespace | `.claude-plugin/` | `.codex-plugin/` |
| Connector model | `.mcp.json` — you host/configure an MCP server | **`.app.json`** — bind a *hosted* OpenAI app by opaque id (`asdk_app_…`), OAuth on install (144/167 plugins) |
| Storefront | dev-facing; metadata minimal | **productized**: `interface{}` with category, capabilities, brandColor, screenshots, `defaultPrompt`; `policy.installation`/`authentication`; `codex://` View/Share deeplinks |
| Path/runtime | `${CLAUDE_PLUGIN_ROOT}`, copy-on-install cache, versioned GC ([[sources/anthropic--plugins-reference#caching-and-file-resolution]]) | `plugin.lock.json` lockfile (3 plugins); hosted-app brokering opaque from the repo |

Read together: Anthropic optimizes for **developer control of the connector**; OpenAI optimizes for **consumer one-click install of a brokered connector**. Same plugin body, different go-to-market.

## Evidence & claims

- *The hook schema is identical across labs* — **demonstrated** (figma's `hooks.json` is a valid Claude Code hook verbatim): [[sources/openai--plugins#hooks-json]].
- *Skill anatomy is identical* — **demonstrated** (SKILL.md frontmatter + references/scripts on both): [[sources/openai--plugins#skill-md]].
- *Both auto-discover components and treat manifest paths as supplemental* — **demonstrated** (Codex spec note) + asserted (Anthropic docs): [[sources/openai--plugins#component-discovery]], [[sources/anthropic--plugins-reference#components]].
- *OpenAI references "skill-creator naming rules"* — **demonstrated** (literal text in plugin-creator): [[sources/openai--plugins#plugin-creator]].
- *A single skill pack runs on both harnesses* — **demonstrated** (superpowers, same skill names on both): [[sources/openai--plugins#superpowers]].
- *The labs diverge on connector + storefront* — **demonstrated** (`.app.json` vs `.mcp.json`; `interface{}`/`policy{}` blocks): [[sources/openai--plugins#app-json]], [[sources/openai--plugins#interface-block]].

> **Asserted vs. demonstrated:** that the formats *overlap* is demonstrated from the files. That the overlap reflects *independent* convergence (vs. deliberate copying) is **inference** — the `skill-creator naming rules` reference is evidence of at least partial deliberate compatibility. Hold the "independent" reading loosely.

## Patterns demonstrated

- [[patterns/structural/marketplace-as-multi-plugin]] — the `marketplace.json`-registers-N-plugins technique now exists in **both** labs; this concept is the reason that pattern is no longer Claude-Code-specific. Citation: [[sources/openai--plugins#marketplace.json]].
- [[patterns/structural/thin-harness-fat-skills]] — both labs are *thin harnesses* loading fat markdown skills; Codex is the first non-Anthropic harness ingested, which is what a cross-lab spec predicts. Citation: [[sources/openai--plugins#skill-md]].
- [[patterns/composition/single-source-multi-surface-distribution]] — a shared spec is what makes "one source, many runtimes" achievable; superpowers (author-to-common-core) and compound-engineering (author-then-convert) are the two embodiments. Citation: [[sources/openai--plugins#superpowers]].

## Tensions & counter-arguments

- **Is it independent convergence or imitation?** Codex post-dates Claude Code's plugin system, and `plugin-creator` cites "skill-creator naming rules" ([[sources/openai--plugins#plugin-creator]]). So some overlap is *adoption*, not parallel invention — which weakens "two labs independently arrived here" but, if anything, *strengthens* the "this is becoming the standard" claim (a standard spreads by adoption). The honest statement is: **the format is consolidating across labs**; the mechanism (re-derivation vs. copying) is mixed and partly unknown.
- **Convergent grammar ≠ convergent semantics.** `agents/` means "subagent system prompt" in Anthropic's world but is mostly a *presentation manifest* (`agents/openai.yaml`) in Codex ([[sources/openai--plugins#agents-openai-yaml]]). Same folder name, different meaning — a trap for anyone assuming portability is total.
- **The connector layer doesn't converge at all.** `.app.json`'s hosted-app brokering vs `.mcp.json`'s self-hosting are genuinely different trust/distribution models; a plugin that's "just a connector + skill" does **not** port without rewiring its integration ([[sources/openai--plugins#app-json]]).
- **One repo isn't the whole field.** We have two labs. Cursor, Google, and open-source agent frameworks may package differently; calling this an "industry standard" on n=2 is premature — hence `status: emerging`.

## Timeline (append-only)

- 2026-05-31 — Anthropic plugins-reference snapshotted: the Claude Code `plugin.json`/components/marketplace spec ([[sources/anthropic--plugins-reference#root]]).
- 2026-06-02 — `openai/plugins` ingested (167 plugins, commit `bebc3d6`): Codex ships a near-identical format under `.codex-plugin/`, with an identical `hooks.json` grammar and a "skill-creator naming rules" reference — the second data point that turns "Anthropic's plugin spec" into "the agent plugin spec." ([[sources/openai--plugins#hooks-json]], [[sources/openai--plugins#plugin-creator]])

## Related

- [[artifacts/plugins/openai-codex-plugins-marketplace]] — the artifact that surfaced this concept.
- [[artifacts/plugins/anthropic-financial-services-marketplace]] / [[artifacts/plugins/anthropic-skills-marketplace]] — the Anthropic-side marketplaces.
- [[patterns/composition/single-source-multi-surface-distribution]] — the portability payoff a shared spec enables.
- [[concepts/compound-engineering]] — CE's converter is the "author-then-convert" answer to the same cross-platform problem this concept frames.

## What we'd steal

**Exhaustive ledger** (★ = highest-value):

- ★ **Author skills to the lab-agnostic core.** Frontmatter (`name` + "Use when…" `description`), a markdown body, `references/`/`scripts/` — the subset both labs share — and you get a skill that runs on Codex *and* Claude Code (the superpowers proof). Branch only where a connector or hook forces it.
- ★ **Treat the overlap as a portability checklist.** When building a plugin, ask per component: is this in the shared core (skills, hooks `PostToolUse`/`matcher`, `.mcp.json`, marketplace) or a lab-specific bet (`.app.json`, `interface{}` storefront, `${CLAUDE_PLUGIN_ROOT}`)? Keep the value in the core.
- ★ **Use the divergences as a buyer's lens.** "Hosted-app-brokered connector vs self-hosted MCP" is the real decision when picking an ecosystem — control + auditability (Anthropic) vs one-click consumer install (OpenAI).
- **Mind the `agents/` semantic trap** — same folder, different meaning across labs; never assume a folder name implies identical behavior.
- **Watch for n→3.** The moment a third lab/framework ships the same grammar, this graduates from "emerging" to a genuine standard — and any wiki pattern tied to it generalizes further. A standing QUERY trigger.
- **Reuse one naming spec across tools** — OpenAI's plugin-creator borrowing skill-creator's normalization is a small, copyable DRY move for any toolchain with multiple scaffolders.

## Open questions

- **Independent or imitative?** How much of the overlap is OpenAI deliberately matching Anthropic vs. both converging from shared model priors? The `skill-creator naming rules` reference says "at least partly deliberate," but not how much.
- **Will the connector layers ever converge?** Is there pressure toward a shared connector/app protocol, or do hosted-app vs MCP stay as the durable fork?
- **Does a third example exist already?** Cursor rules, Google's agent packaging, open frameworks — do any match this grammar? Finding one would move `status: emerging → active` and is the next ingest worth chasing.
- **How total is portability in practice?** Superpowers runs on both — but what fraction of its skills needed per-runtime tweaks? (The inverse of CE's converter question.)
