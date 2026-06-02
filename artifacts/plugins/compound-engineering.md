---
domain: artifacts
type: plugin
name: compound-engineering
creator: "[[creators/every]]"
source: "[[sources/every--compound-engineering-plugin]]"
ecosystem: claude-code (native) + codex/cursor/copilot/droid/qwen/opencode/pi/gemini/kiro (converter-backed)
discovered-via: user-curated (Sidney named explicitly)
marketplace-listing: "/plugin marketplace add EveryInc/compound-engineering-plugin"
status: active
last-reviewed: 2026-06-02
ingestion-mode: full
license: MIT
components:
  plugins-registered: 2              # compound-engineering (Kieran Klaassen) + coding-tutor (Nityesh Agarwal)
  skills: 38                          # filesystem dir count; README prose hedges "38+"
  agents: 43                          # filesystem ce-*.md count; README prose claims "51"/"50+" (drift — see Weird)
  commands: 0                         # migrated to skills in v2.39.0; coding-tutor still ships 3
  hooks: 0
  mcp-servers: 0                      # none bundled; some skills opportunistically use XcodeBuildMCP, gh, GitHub/Slack/Proof/Gemini APIs
  converter-targets: 11              # Claude Code + Codex + Cursor + Copilot + Droid + Qwen + OpenCode + Pi + Gemini + Kiro (+ Windsurf legacy)
popularity-signals:
  - signal: official-every
    value: "Official Compound Engineering plugin; npm @every-env/compound-plugin v3.9.4; owner Kieran Klaassen (GM of Cora at Every)"
    as-of: 2026-06-02
    source: "[[sources/every--compound-engineering-plugin#plugin.json]]"
  - signal: development-velocity
    value: "HEAD 3e77a7b = PR #893 (2026-06-01); 55KB CHANGELOG; 27 brainstorms + 57 plans + 30 solutions; ~1,094 test cases"
    as-of: 2026-06-02
    source: "[[sources/every--compound-engineering-plugin#tests]]"
---

# compound-engineering (the plugin)

> **One-line:** Every's official agent-coding plugin — **38 skills + 43 sub-agents** that
> run a disciplined loop (`/ce-strategy` → `/ce-ideate` → `/ce-brainstorm` → `/ce-plan` →
> `/ce-work` → `/ce-code-review` → `/ce-compound`) so each unit of work makes the next one
> easier. Two defining moves: it is **authored once in Claude format and converted to ~11
> agent platforms** by a Bun/TypeScript CLI, and it **dogfoods its own loop** (the repo's 27
> brainstorms + 57 plans + 30 documented solutions are the loop's audit trail). The wiki's
> first **non-Garry-Tan tested skill pack**, and the runnable embodiment of
> [[concepts/compound-engineering]].

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): read across the
repo's README/AGENTS/skills/tests, then write distilled judgment — not a transcription of the README.*

## Attributes

- **What it does**: turns a rough idea into shipped, reviewed, *documented* work through a
  fixed loop, and captures the learning so the next cycle is cheaper. The user-facing surface
  is a set of `/ce-*` slash commands; under each, parallel sub-agents do research, review, and
  fixes. ([[sources/every--compound-engineering-plugin#README]])
- **Target user**: software engineers using an agent harness (Claude Code, Codex, Cursor, …)
  who want a repeatable, opinionated workflow rather than ad-hoc prompting — especially
  solo/high-velocity builders (the author's own posture). Rails/Ruby, TypeScript, Python, and
  Swift/iOS get first-class skills/agents.
- **Component inventory** (the `compound-engineering` plugin):
  - **38 skills** (slash-invoked `/ce-*`), grouped in the plugin README
    ([[sources/every--compound-engineering-plugin#plugin-README]]):
    - *Core Workflow* — `ce-strategy` (maintains `STRATEGY.md`, the durable anchor read by
      ideate/brainstorm/plan), `ce-ideate`, `ce-brainstorm`, `ce-plan`, `ce-work`, `ce-debug`,
      `ce-code-review`, `ce-compound`, `ce-compound-refresh`, `ce-optimize`, `ce-product-pulse`
      (read-side: time-windowed usage/perf/error report → `docs/pulse-reports/`).
    - *Research & Context* — `ce-sessions` (query Claude Code/Codex/Cursor session history),
      `ce-slack-research`, `ce-riffrec-feedback-analysis`.
    - *Git Workflow* — `ce-commit`, `ce-commit-push-pr`, `ce-worktree`, `ce-clean-gone-branches`.
    - *Utilities* — `ce-demo-reel`, `ce-resolve-pr-feedback`, `ce-test-browser`, `ce-test-xcode`,
      `ce-setup`, `ce-update`, `ce-release-notes`, `ce-report-bug`.
    - *Frameworks* — `ce-agent-native-architecture`, `ce-dhh-rails-style` (DHH/37signals Ruby),
      `ce-frontend-design`.
    - *Review & Quality* — `ce-doc-review`, `ce-simplify-code`.
    - *Content / Automation* — `ce-proof` (Proof collaborative editor), `ce-gemini-imagegen`.
    - *Beta* — `ce-polish-beta` (the human-in-the-loop polish phase), `ce-dogfood-beta`, `lfg`
      (full autonomous workflow). Beta skills use a `-beta` suffix + `disable-model-invocation`.
  - **43 sub-agents** (`ce-*.md`, invoked *by skills*, not directly —
    [[sources/every--compound-engineering-plugin#agents]]): review **lenses** (`ce-correctness-`,
    `ce-security-` ×3, `ce-performance-` ×2, `ce-maintainability-`, `ce-reliability-`,
    `ce-testing-`, `ce-data-integrity-guardian`, `ce-api-contract-`, `ce-adversarial-reviewer`,
    …), **document-review** lenses (`ce-coherence-`, `ce-scope-guardian-`, `ce-feasibility-`,
    `ce-product-lens-`, `ce-adversarial-document-reviewer`, …), **researchers**
    (`ce-best-practices-`, `ce-framework-docs-`, `ce-web-`, `ce-repo-research-`,
    `ce-learnings-researcher`, `ce-git-history-`, `ce-issue-intelligence-`, `ce-session-historian`),
    **design** (`ce-design-iterator`, `ce-figma-design-sync`, …), and **named-expert personas**
    (`ce-julik-frontend-races-reviewer`, `ce-ankane-readme-writer`, `ce-swift-ios-reviewer`).
  - **0 hooks, 0 bundled MCP servers, 0 separate commands** (commands were folded into skills in
    v2.39.0). Some skills *opportunistically* call external tools (XcodeBuildMCP for `ce-test-xcode`,
    `gh`, GitHub/Slack/Proof APIs, the Gemini API) — none are install-time dependencies.
  - **2nd plugin in the marketplace**: `coding-tutor` (Nityesh Agarwal) — 3 commands
    (`teach-me`, `quiz-me`, `sync-tutorials`) + 1 skill; personalized tutorials with
    spaced-repetition quizzes ([[sources/every--compound-engineering-plugin#coding-tutor]]).
- **Install footprint**: **Claude Code needs no Bun** — `/plugin marketplace add
  EveryInc/compound-engineering-plugin` then `/plugin install compound-engineering`. Converter-backed
  targets use `bunx @every-env/compound-plugin install compound-engineering --to <target>`; Codex
  also needs a Bun agent step (its native plugin spec doesn't yet register custom agents); Pi needs
  `pi-subagents` (+ `pi-ask-user`). `--to all` auto-detects.
  ([[sources/every--compound-engineering-plugin#install-matrix]])
- **Plugin layout** (repo root):
  ```
  .claude-plugin/marketplace.json     2-plugin catalog (parallel .cursor-plugin/, .agents/plugins/)
  plugins/compound-engineering/       skills/ (38) · agents/ (43) · .claude-plugin/plugin.json
                                      AGENTS.md (+ CLAUDE.md = @AGENTS.md shim) · README.md
  plugins/coding-tutor/               2nd plugin (Nityesh Agarwal)
  src/                                Bun/TS converter CLI: parsers/ · converters/ (×7) · targets/ · release/
  tests/                              52 files, ~1,094 cases
  docs/                               brainstorms/ (27) · plans/ (57) · solutions/ (30) · skills/ · specs/ (7)
  ```
- **License**: MIT.

## Relationships

- **Creator**: [[creators/every]] — Kieran Klaassen (owner/author; GM of Cora), with Dan Shipper
  (CEO) as editorial amplifier and Nityesh Agarwal authoring `coding-tutor`.
- **Source**: [[sources/every--compound-engineering-plugin#root]].
- **Embodies**: [[concepts/compound-engineering]] — the plugin is the runnable form of the concept;
  the [[sources/every--compound-engineering]] guide + [[sources/every--compound-engineering-gets-an-upgrade]]
  essay are the framing.
- **Mechanism layer**: [[sources/anthropic--plugins-reference]] — the Claude Code plugin system
  (`plugin.json`, `${CLAUDE_PLUGIN_ROOT}`, versioned + session caching) the plugin rides on and whose
  caching/path constraints its authoring rules navigate.
- **Closest siblings**: [[artifacts/plugins/gstack]] (Garry Tan's opinionated engineering-team pack —
  the other solo-auteur tested skill pack; persona-based) and [[artifacts/plugins/gbrain]] (the other
  `AGENTS.md`-canonical, multi-surface artifact).
- **Composes**: 38 skills + 43 sub-agents; each gets its own page if deep-dived later (candidates
  queued in [[artifacts/skills/_index]]).

## What problem it solves

Agent-assisted coding tends to **accumulate debt and re-learn the same lessons**: each session
starts cold, every fix leaves local knowledge someone rediscovers later, and "review" means a human
re-applying the same taste by hand every time. The plugin packages a *whole workflow* that inverts
this — it front-loads planning (`/ce-brainstorm`, `/ce-plan`), makes review a parallel multi-lens
pass (`/ce-code-review`), and — the load-bearing move — **captures each solved problem into a
searchable store** (`/ce-compound` → `docs/solutions/`) so the next agent (or a teammate without the
plugin) doesn't start from zero ([[sources/every--compound-engineering-plugin#README]],
`#ce-compound`). The second problem it solves is **harness lock-in**: engineers use different agent
tools (Claude Code, Codex, Cursor, …), so the plugin is authored once and *converted* to each rather
than forked, with a drift-checked manifest parity gate ([[sources/every--compound-engineering-plugin#converter]],
`#release-automation`).

## Composition strategy

Four moves stack:

1. **The loop is the composition.** Skills hand off via *files on disk*, not in-memory state:
   `STRATEGY.md` (the durable anchor) grounds `/ce-ideate`, which routes the chosen idea into
   `/ce-brainstorm` → a requirements doc in `docs/brainstorms/`; `/ce-plan` consumes that doc → a plan
   in `docs/plans/`; `/ce-work` executes the plan; `/ce-code-review` reviews the diff; `/ce-compound`
   writes the learning to `docs/solutions/`; `/ce-product-pulse` reads real usage back in to seed the
   next strategy/brainstorm. Each artifact is the next skill's input — a pipeline of durable documents
   ([[sources/every--compound-engineering-plugin#README]], `#docs-plans`, `#docs-solutions`).

2. **Skills orchestrate sub-agents; sub-agents don't call each other.** The 38 skills are entry
   points; the 43 `ce-*` agents are workers a skill dispatches in parallel. `/ce-code-review`
   dynamically selects reviewer personas, spawns them as parallel sub-agents that **return structured
   JSON**, then **merges and deduplicates** into one confidence-gated report
   ([[sources/every--compound-engineering-plugin#ce-code-review]]). `/ce-compound` dispatches research
   subagents that **return text only** while the orchestrator owns the single write (see Worked
   example).

3. **Author once, convert to every harness.** `src/parsers/claude.ts` reads the Claude format;
   `src/converters/claude-to-<target>.ts` + `src/targets/<target>.ts` emit each platform's layout;
   `bun run release:validate` enforces Claude/Cursor/Codex *manifest parity* so the three catalogs
   can't drift ([[sources/every--compound-engineering-plugin#converter]], `#release-automation`).

4. **Skills are self-contained, by rule.** A `SKILL.md` may reference *only* files inside its own
   directory — shared material is duplicated, never cross-referenced — because the converter copies
   each skill as an isolated unit and versioned install paths break absolute references
   ([[sources/every--compound-engineering-plugin#self-containment]]).

**Where the lines are drawn** — the repo is explicit ([[sources/every--compound-engineering-plugin#plugin-AGENTS.md]]):
*skills* = slash entry points (judgment + orchestration); *agents* = the parallel workers skills
spawn (never invoked directly; the `ce-` prefix prevents cross-plugin name collisions); *commands* =
folded into skills (v2.39.0); *converter/CLI* = the deterministic infrastructure (parse, convert,
validate, clean up); *hooks* = unused. The single most distinctive authoring rule is
**"Skills are guardrails for an intelligent agent, not a step-by-step controller for a non-intelligent
one"** — calibrate prescription to the failure mode (hard rules for deterministic safety, trust for
judgment), which is a non-Garry statement of [[patterns/behavioral/latent-vs-deterministic-split]].

## Worked example — `/ce-compound` (the compounding step, dogfooded)

The clearest single illustration of *why* the plugin is called what it is
([[sources/every--compound-engineering-plugin#ce-compound]]):

- **The job**: after a problem is solved, capture it into `docs/solutions/<category>/<slug>.md` with
  YAML frontmatter (`problem_type`, `component`, `tags`, `date`, …) so the next occurrence is a 2-minute
  lookup instead of 30 minutes of re-research. *"Each documented solution compounds your team's
  knowledge."* The store is real and self-applied: **30 solutions** across 5 categories
  ([[sources/every--compound-engineering-plugin#docs-solutions]]).
- **Latent research, deterministic write (the explicit boundary).** Phase 1 launches parallel
  subagents — *Context Analyzer*, *Solution Extractor*, *Related Docs Finder* — that **return TEXT
  DATA to the orchestrator and must NOT write files**; only the orchestrator writes, and it writes
  **exactly one** solution doc (plus, at most, a small edit to an instruction file). That "research is
  parallel + latent; the write is single + deterministic" split is [[patterns/behavioral/latent-vs-deterministic-split]]
  drawn inside one skill.
- **Dedup before create (the anti-drift discipline).** The Related Docs Finder scores overlap with
  existing docs across **five dimensions** (problem statement, root cause, solution, referenced files,
  prevention). **High overlap → *update* the existing doc, not create a duplicate** ("two docs
  describing the same problem will inevitably drift apart"). This is the consolidation rule that keeps
  a compounding store from rotting — and the exact discipline this wiki imported into its own INGEST
  (see [[meta/self-improvements]]).
- **Discoverability Check (the store only compounds if agents can find it).** After writing, the skill
  checks whether the project's `AGENTS.md`/`CLAUDE.md` would lead a *fresh* agent to discover and
  search `docs/solutions/`, and adds the smallest natural mention if not. Notably it **handles the
  `CLAUDE.md = @AGENTS.md` shim correctly**: *"one file may just be a shim that `@`-includes the other…
  The substantive file is the assessment and edit target; ignore shims"*
  ([[sources/every--compound-engineering-plugin#CLAUDE.md-shim]]).
- **Deterministic safety gate.** The orchestrator runs `python3 scripts/validate-frontmatter.py` and
  must reach exit 0 (catches silent YAML corruption — unquoted ` #`, unquoted `: `) before declaring
  success — a deterministic check guarding a latent author.
- **Modes**: *Interactive* (asks Full vs Lightweight, session-history opt-in, "What's next?"),
  *Lightweight* (single pass, no dedup), *Headless* (no questions; for skill-to-skill/automation). One
  skill, three interaction shapes — the same artifact output regardless.
- **Auto-invoke**: trigger phrases ("that worked", "it's fixed", "problem solved") let the skill
  self-fire when a fix lands.

This one skill demonstrates the ratchet (a forward-only knowledge floor), the latent/deterministic
write-boundary, the dedup discipline, and the `AGENTS.md`-canonical handling — in ~580 lines of
markdown over a 3-line Python validator. `/ce-code-review` is the complementary showcase (parallel
persona lenses → JSON → merge/dedup → confidence-gated report;
[[sources/every--compound-engineering-plugin#ce-code-review]]).

## Patterns demonstrated

**Confirmed — this ingest supplied a key example for each:**

- [[patterns/quality-bar/complexity-ratchet]] — **the non-Garry 2nd example that promotes it to
  `confirmed`.** `docs/solutions/` is the forward-only knowledge floor `/ce-compound` writes; branch
  protection on `main` (requires the `test` check) is the "a later session structurally cannot regress
  below the floor" mechanism the pattern's promotion bar demanded; behavioral *contract* tests
  (`review-skill-contract`, `pipeline-review-contract`) pin skill behavior.
  ([[sources/every--compound-engineering-plugin#docs-solutions]], `#release-automation`, `#tests`)
- [[patterns/quality-bar/skill-pack-bundle]] — **the non-Garry example that retires the same-creator
  caveat.** ~1,094 test cases across 52 files: convention tests (`skill-agent-ce-prefix`, `frontmatter`),
  contract tests, safety tests (`skill-shell-safety`, `path-sanitization`). *Honest nuance:* CE leans on
  Claude Code's built-in description-resolver rather than shipping a dedicated *resolver eval* (the rare
  part), so the bundle is test-complete but resolver-light. ([[sources/every--compound-engineering-plugin#tests]])
- [[patterns/composition/single-source-multi-surface-distribution]] — **a 3rd example on a new axis:
  competing harnesses.** One Claude-format plugin → ~11 platforms via `src/converters/` + `src/targets/`,
  with `release:validate` as the drift guard. ([[sources/every--compound-engineering-plugin#converter]])
- [[patterns/behavioral/latent-vs-deterministic-split]] — **non-Garry 3rd example; retires its
  same-creator caveat.** Markdown skills (latent) over the TS converter + `validate-frontmatter.py`
  (deterministic); `/ce-compound`'s text-returning research vs single-writer; and the explicit
  authoring rule "calibrate prescription to the failure mode."
  ([[sources/every--compound-engineering-plugin#plugin-AGENTS.md]], `#ce-compound`)

**Proposed-with-page:**

- [[patterns/structural/thin-harness-fat-skills]] — a 2nd-creator **fat-skills** witness: capability in
  fat markdown over a thin deterministic converter/CLI, riding harnesses CE doesn't own. (Doesn't
  resolve the unverified thin-*harness*-middle; stays proposed.)
- [[patterns/quality-bar/version-as-update-gate]] — **2nd example (with FSI) — confirmed via this
  ingest.** release-please + `linked-versions` + `semantic-release` own all versions; contributors must
  not hand-bump; `version` gates update delivery. ([[sources/every--compound-engineering-plugin#release-automation]])

**Proposed — tracked here, awaiting a 2nd clean example (some confirmable):**

- **agent-first canonical docs (`CLAUDE.md` = `@AGENTS.md` shim)** — `AGENTS.md` is the source of
  truth; the harness file is a 1-line redirect. 2nd example after gbrain's `AGENTS.md`-separate-from-
  `CLAUDE.md` — *confirmable on a dedicated pass*. ([[sources/every--compound-engineering-plugin#CLAUDE.md-shim]])
- **persona/lens multi-agent review panel** — `/ce-code-review` fans out tiered persona + named-expert
  lenses returning JSON → merge/dedup → confidence gate. 2nd example alongside gstack's QA personas —
  *confirmable*. ([[sources/every--compound-engineering-plugin#ce-code-review]], `#agents`)
- **skill-self-containment for portability** — a skill references only its own directory; duplicate,
  never cross-link (converter + versioned-cache driven). ([[sources/every--compound-engineering-plugin#self-containment]])
- **cross-platform-portable skill authoring** — never assume platform env vars without a fallback; name
  per-platform tool equivalents (`AskUserQuestion`/`request_user_input`/`ask_user`; `Agent`/`spawn_agent`/
  `subagent`). ([[sources/every--compound-engineering-plugin#cross-platform-authoring]])
- **dedup-before-create** — score overlap across dimensions; update the existing doc when overlap is
  high. Relative of structured consolidation; ([[sources/every--compound-engineering-plugin#ce-compound]]).
- **structured-output multi-agent merge** — sub-agents return JSON; the orchestrator dedups (relative
  of FSI's structured-output-as-injection-defense). ([[sources/every--compound-engineering-plugin#ce-code-review]])
- **legacy-artifact cleanup registry** — removed skills/agents are registered in `STALE_*` lists and
  swept on upgrade. ([[sources/every--compound-engineering-plugin#legacy-cleanup]])
- **auto-invoke trigger phrases** — a skill self-fires on natural-language cues (relative of gstack's
  voice-trigger aliases). ([[sources/every--compound-engineering-plugin#ce-compound]])

## Source citations

- [[sources/every--compound-engineering-plugin#README]] — philosophy, 80/20, workflow table, install matrix, "no contributions"
- [[sources/every--compound-engineering-plugin#AGENTS.md]] / `#CLAUDE.md-shim` — canonical-doc shim, working agreement, scratch policy
- [[sources/every--compound-engineering-plugin#plugin-AGENTS.md]] — Skill Design Principles, compliance checklist, `ce-` prefix, cross-platform rules
- [[sources/every--compound-engineering-plugin#ce-compound]] — the compounding mechanism (latent research / single write / dedup / discoverability)
- [[sources/every--compound-engineering-plugin#ce-code-review]] — parallel persona lenses → JSON → merge/dedup, modes
- [[sources/every--compound-engineering-plugin#converter]] / `#release-automation` — the multi-harness converter + version gate
- [[sources/every--compound-engineering-plugin#tests]] — ~1,094 cases incl. contract/safety/convention tests
- [[sources/every--compound-engineering-plugin#docs-solutions]] / `#docs-brainstorms` / `#docs-plans` — the dogfooded loop trail
- [[sources/every--compound-engineering-plugin#self-containment]] — the no-cross-skill-reference rule
- [[sources/every--compound-engineering-plugin#marketplace.json]] / `#plugin.json` / `#coding-tutor` — ownership, 2-plugin marketplace, MIT

## What makes it great

It is the first artifact in the wiki where **the methodology, the runnable tool, and the proof are the
same object**: compound engineering is stated in an essay, shipped as a plugin, and *demonstrated by the
plugin's own development trail* (27 brainstorms → 57 plans → 30 solutions). The `/ce-compound` skill is
a small masterpiece of altitude — it pushes parallel research into latent subagents that may not write,
funnels everything through a single deterministic write, refuses to create a duplicate when an existing
doc overlaps, and then *checks that future agents can even find the store it just wrote to* (handling
the `@AGENTS.md` shim correctly along the way). And the converter is a genuinely hard problem solved
pragmatically: rather than bet on one harness winning, it treats "which agent tool you use" as a
packaging detail and keeps eleven of them in parity behind a `release:validate` gate. The authoring
discipline in `AGENTS.md` — "skills are guardrails for an intelligent agent, not a controller for a dumb
one," calibrate prescription to the failure mode, every line of a SKILL.md loads on every invocation so
cut rationale that doesn't change behavior — is some of the most clear-eyed skill-design writing in the
wiki, and it comes from outside the Garry Tan corpus, which is exactly what the wiki needed.

## What we'd steal

**Exhaustive ledger** (★ = highest-value, clearly portable):

- ★ **The `/ce-compound` shape as a reusable "capture the learning" primitive**: parallel latent
  research → *single* deterministic write → 5-dimension overlap dedup (update, don't duplicate) →
  discoverability edit so the store is findable. Portable to any knowledge-accreting system (this wiki
  included — see [[meta/self-improvements]]).
- ★ **"Skills are guardrails for an intelligent agent, not a controller for a dumb one" + calibrate
  prescription to the failure mode** (hard rules for deterministic safety, strong-guidance-with-examples
  for biased judgment calls, trust for the rest). The single best heuristic for *how prescriptive* a
  skill/agent instruction should be.
- ★ **Author once, convert to many harnesses** — treat the agent tool as a packaging target, parse one
  canonical format, emit per-platform layouts, and gate manifest parity in CI so they can't drift.
- ★ **`CLAUDE.md` = `@AGENTS.md` shim** — make `AGENTS.md` the canonical agent doc and leave a 1-line
  redirect for harness-specific lookups; then teach tooling to "ignore shims; edit the substantive file."
- ★ **Skill self-containment** — a skill references only its own directory; duplicate shared files. Ugly
  but correct under converters + versioned install caches.
- **Dedup-before-create with dimensional overlap scoring** — before writing a new doc, score overlap
  (problem / root cause / solution / files / prevention); high overlap updates the existing doc.
- **Behavioral contract tests** — test that a *skill/agent* conforms to its contract (`review-skill-contract`,
  `pipeline-review-contract`), and enforce conventions as tests (`skill-agent-ce-prefix`).
- **Name per-platform tool equivalents in skill content** with a graceful fallback — the portability tax
  paid at the right layer.
- **Mode duality in one skill** (interactive / headless / report-only / autofix) — same logic, different
  interaction, selected by an argument token; lets a skill serve both a human and a calling skill.
- **The `ce-` prefix as namespace hygiene** — short pack-prefix on every skill/agent so they don't
  collide with the harness's built-ins (`/plan`, `/review`) or other plugins; enforced by a test.
- **Legacy-artifact cleanup registry** — when you delete a component, register its name so stale
  flat-install copies are swept on upgrade.
- **The 80/20 + 50/50 budget framing** and the **8-step loop with one durable artifact per step** —
  liftable as a default agent-coding workflow (see [[concepts/compound-engineering]]).
- **`disable-model-invocation` for beta skills** — keep experimental skills from auto-firing while still
  letting a user invoke them by slash.
- **The "About Contributions" stance written down** — set the no-outside-PRs boundary explicitly so
  contributors aren't surprised.

## Weird / surprising things

- **Agent-count drift.** The filesystem has **43** `ce-*.md` agent files; the root `README.md` prose
  says **"51 agents,"** the plugin `README.md` says **"50+."** `release:validate` supposedly enforces
  counts, so either the prose drifted or it counts something not on disk (converter-generated? both
  plugins?). A precise, useful boundary on an otherwise-rigorous QC story — exactly the kind of
  claim-vs-tree gap the wiki catches (cf. FSI's malformed `.mcp.json`, gstack's "62 vs 60"). **TODO**
  (LINT): reconcile against `release:validate`'s own count. ([[sources/every--compound-engineering-plugin#agents]])
- **Two `CLAUDE.md` files, both 11 bytes, both `@AGENTS.md`** — the root and the plugin each redirect to
  their sibling `AGENTS.md`. The shim is applied fractally.
- **The repo documents its own caching gotcha.** `plugin-AGENTS.md` warns that plugin agent/skill
  definitions cache at session start, so editing a skill and re-dispatching it in the same session tests
  the *old* copy — and tells contributors to use `skill-creator` or restart. It is unusually honest about
  the harness it ships on. ([[sources/every--compound-engineering-plugin#caching-gotcha]])
- **A media company's engineering plugin.** Every is known for essays; the plugin is production-grade
  infra (semantic-release, linked-versions, 52 test files). The narrative arm and the tooling arm are
  the same loop.

## Open questions / what's unclear

- **What does `release:validate` actually count for "agents," and why 51 vs the 43 files?** Resolving
  this would either find missing agent definitions or confirm prose drift.
- **Does the converter preserve behavior, or just structure?** `SKILL.md` bodies are "copied almost
  exactly" to other platforms ([[sources/every--compound-engineering-plugin#plugin-AGENTS.md]]); the
  cross-platform tool-equivalent rules exist precisely because copied prose can subtly misbehave on a
  different harness. How well-tested is *behavioral* parity across targets vs. *structural* conversion?
- **Is the `docs/solutions/` ratchet load-bearing for a non-author?** The store compounds value only if
  agents discover it (hence the Discoverability Check). For users who install the plugin into *their*
  repo, does the store actually get populated and read, or is the dogfooded trail unique to Every?
- **Resolver evals.** CE tests skill *output* and *contracts* but leans on the harness's built-in
  description-resolver — it doesn't ship resolver-trigger evals the way gstack/gbrain do. Is that a gap,
  or the correct call when you don't own the resolver?
- **Relevance to Sidney's work** (worth a note): the `/ce-compound` "capture-the-learning" primitive and
  the dedup-before-create discipline map directly onto *this research wiki's* INGEST/LINT — already
  partially imported (see [[meta/self-improvements]]). The author's solo-high-velocity + agent-reviewed
  posture parallels [[creators/garry-tan]].
