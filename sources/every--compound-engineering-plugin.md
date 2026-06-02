---
domain: sources
type: repo
url: https://github.com/everyinc/compound-engineering-plugin
retrieved: 2026-06-02
snapshot-location: sources/every--compound-engineering-plugin/ (live clone, git-ignored; in repos.manifest.tsv)
upstream-commit: 3e77a7b
last-reviewed: 2026-06-02
---

# `everyinc/compound-engineering-plugin` (the repo)

> The official **Compound Engineering** plugin from Every — a coding-agent skill pack
> (38 skills + 43 sub-agents) authored *once* in Claude format and **converted to ~11
> agent platforms** (Claude Code, Codex, Cursor, Copilot, Droid, Qwen, OpenCode, Pi,
> Gemini, Kiro) by a Bun/TypeScript CLI. It operationalizes Kieran Klaassen's
> "compound engineering" loop (`/ce-brainstorm` → `/ce-plan` → `/ce-work` →
> `/ce-code-review` → `/ce-compound`) and **dogfoods that loop on its own
> development** (27 brainstorms + 57 plans + 30 documented solutions in `docs/`). Our
> primary, fully-verifiable evidence for the [[concepts/compound-engineering]] concept
> and the [[artifacts/plugins/compound-engineering]] artifact — and the wiki's first
> **non-Garry-Tan** tested skill pack.

## Snapshot details

- **Retrieved**: 2026-06-02 via `git clone --depth 1`. Kept as a **live local clone**
  (git-ignored, in `sources/repos.manifest.tsv`); only this citation page is committed.
- **Where it lives in this wiki**: `sources/every--compound-engineering-plugin/`
  (reconstruct with `sources/clone-all.sh`, pinned to the commit below).
- **Upstream URL**: https://github.com/everyinc/compound-engineering-plugin (the
  GitHub org is `EveryInc`; case-insensitive).
- **Upstream commit**: `3e77a7bd8450fef7270f8b46c0f1865fd7125741` (`3e77a7b`), authored
  **2026-06-01 17:24 -0700** — *"fix(ce-resolve-pr-feedback): drop clustering, default
  to merit-based fixing (#893)"*. Day-old at retrieval; very actively developed.
- **Size / shape**: 11 MB, **556 tracked files** — 373 `.md`, 102 `.ts`, 25 `.json`,
  17 `.py`, 12 `.sh`, 8 `.yaml`. `package.json` = `@every-env/compound-plugin` v3.9.4.
- **License**: MIT.

## Anchor map

Every claim citing this source uses a `#anchor` from this list. **Do not invent
anchors beyond this list** — register new ones here first.

- `#root` — the repo as a whole
- `#README` — root `README.md`: the philosophy ("each unit of engineering work should
  make subsequent units easier — not harder"; "80% planning and review, 20% execution"),
  the workflow/skill table, the multi-platform **Install** matrix, and the "About
  Contributions" note.
- `#AGENTS.md` — root `AGENTS.md` (19.5 KB): canonical repo instructions. Working
  Agreement (branch protection on `main` requires the `test` check; release automation
  owns versions), the OS-temp-vs-`.context/` scratch policy, cross-platform character
  rules, the "Adding a New Target Provider" checklist.
- `#CLAUDE.md-shim` — root `CLAUDE.md` is **11 bytes: `@AGENTS.md`**. AGENTS.md states:
  *"`AGENTS.md` is the canonical repo instruction file. Root `CLAUDE.md` exists only as
  a compatibility shim for tools and conversions that still look for it."* (The plugin's
  *own* `plugins/compound-engineering/CLAUDE.md` is likewise `@AGENTS.md`.)
- `#marketplace.json` — `.claude-plugin/marketplace.json`: marketplace
  `compound-engineering-plugin` v1.0.2, **owner Kieran Klaassen**, registers **2
  plugins** (`compound-engineering` by Kieran; `coding-tutor` by Nityesh Agarwal). Repo
  also ships parallel `.cursor-plugin/marketplace.json` and `.agents/plugins/marketplace.json`
  (Codex schema) — three marketplace formats kept in parity by `release:validate`.
- `#plugin.json` — `plugins/compound-engineering/.claude-plugin/plugin.json`: name
  `compound-engineering`, **version 3.9.4**, **MIT**, author Kieran Klaassen
  (`kieran@every.to`), homepage = the origin essay
  (`every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it`).
- `#plugin-README` — `plugins/compound-engineering/README.md`: the component-inventory
  tables (skills grouped Core Workflow / Research / Git / Utilities / Frameworks /
  Review / Beta; agents grouped Review / Document Review / Research / Design / Workflow /
  Docs). Header counts: "Agents 50+ · Skills 38+".
- `#plugin-AGENTS.md` — `plugins/compound-engineering/AGENTS.md`: the **Skill Design
  Principles** ("Skills are guardrails for an intelligent agent, not a step-by-step
  controller for a non-intelligent one"; "Calibrate prescription level to the failure
  mode"), the **Skill Compliance Checklist**, the `ce-` prefix rule, the file-reference
  rules, and the cross-platform authoring rules.
- `#ce-compound` — `skills/ce-compound/SKILL.md`: the **compounding mechanism**. Parallel
  research subagents (Context Analyzer / Solution Extractor / Related Docs Finder) return
  **text only**; the orchestrator writes **one** file to `docs/solutions/<category>/`;
  5-dimension overlap scoring (high → *update* existing doc, not duplicate); the
  Discoverability Check (edit `AGENTS.md`/`CLAUDE.md` so future agents find the store);
  headless vs interactive modes; auto-invoke trigger phrases ("that worked", "it's fixed").
- `#ce-code-review` — `skills/ce-code-review/SKILL.md`: multi-agent review — *"dynamically
  selected reviewer personas… spawns parallel sub-agents that return structured JSON, then
  merges and deduplicates findings into a single report"*; modes interactive / autofix /
  report-only / headless; `safe_auto`/`gated_auto`/`manual`/`human`/`release` autofix
  classes; short-circuits to the harness's built-in `/review` for quick reviews.
- `#skills` — `plugins/compound-engineering/skills/`: **38 skill directories** (filesystem
  count), each a `SKILL.md` + optional `references/`/`assets/`/`scripts/`. Invoked as
  `/ce-*` slash commands (commands were migrated to skills in v2.39.0). 3 legacy
  unprefixed skills allowed (`every-style-editor`, `file-todos`, `lfg`).
- `#agents` — `plugins/compound-engineering/agents/`: **43 agent files** (`ce-*.md`, flat).
  Review **lenses** (correctness, security ×3, performance ×2, maintainability,
  reliability, testing, data-integrity…), **researchers** (best-practices, framework-docs,
  web, repo, learnings, git-history, issue-intelligence, slack, session-historian),
  **adversarial** reviewers, and **named-expert personas** (`ce-julik-frontend-races-reviewer`,
  `ce-ankane-readme-writer`, `ce-swift-ios-reviewer`).
- `#docs-solutions` — `docs/solutions/`: **30 documented solutions** (skill-design 14,
  best-practices 4, integrations 3, workflow 3, developer-experience 2), each with YAML
  frontmatter (`title`, `problem_type`, `component`, `tags`, `date`, …). The compounding
  knowledge store `/ce-compound` writes to — dogfooded on the plugin's own development.
- `#docs-brainstorms` — `docs/brainstorms/`: **27 dated requirements docs** (the output
  of `/ce-brainstorm`).
- `#docs-plans` — `docs/plans/`: **57 dated implementation plans** (the output of
  `/ce-plan`). Together with `#docs-brainstorms` + `#docs-solutions`, the literal
  brainstorm→plan→compound audit trail.
- `#docs-skills` — `docs/skills/`: per-skill *user-facing* docs (purpose, novel mechanics,
  chain position) — separate from the runtime `SKILL.md`.
- `#docs-specs` — `docs/specs/`: target-platform format specs (claude-code, codex, copilot,
  cursor, gemini, kiro, opencode) — the conversion contracts.
- `#converter` — `src/` Bun/TypeScript CLI: `parsers/claude.ts` (read Claude format once),
  `converters/claude-to-{codex,copilot,droid,gemini,kiro,opencode,pi}.ts`, `targets/*.ts`
  (per-platform writers), `types/*` (per-platform types), `utils/legacy-cleanup.ts`,
  `release/*`. Entry `src/index.ts` (`bun run src/index.ts {convert,install,list,...}`).
- `#tests` — `tests/`: **52 test files, ~1,094 `describe/test/it` cases**. Includes
  behavioral **contract** tests (`review-skill-contract.test.ts`,
  `pipeline-review-contract.test.ts`), convention-enforcing tests
  (`skill-agent-ce-prefix.test.ts`, `frontmatter.test.ts`), safety tests
  (`skill-shell-safety.test.ts`, `path-sanitization.test.ts`, `manifest-path-safety.test.ts`),
  invariant tests (`legacy-registry-invariants.test.ts`), and per-platform converter/writer
  tests. `bun test` is the merge gate (branch protection).
- `#release-automation` — release is owned by automation: `release-please` +
  `linked-versions` (keeps `cli` and `compound-engineering` at the same version) +
  `semantic-release`; `bun run release:validate` enforces Claude/Cursor/Codex manifest
  parity. Contributors must **not** hand-bump versions. CI (`.github/workflows/ci.yml`)
  validates the PR title against Conventional Commits and runs `bun test`.
- `#install-matrix` — README Install section: Claude Code (`/plugin marketplace add` →
  `/plugin install`, no Bun needed), Cursor, Codex (marketplace + Bun agent step + TUI),
  GitHub Copilot (VS Code + CLI), Factory Droid, Qwen Code, and converter-backed OpenCode /
  Pi / Gemini / Kiro (`bunx @every-env/compound-plugin install … --to <target>`). Pi needs
  `pi-subagents` (+ `pi-ask-user`). `--to all` auto-detects.
- `#self-containment` — `plugin-AGENTS.md` rule: a `SKILL.md` must **only** reference files
  within its own directory tree; duplicate shared files rather than cross-reference. Driven
  by converter portability (each skill is copied as an isolated unit) + versioned
  install-path caching (absolute paths break). Cites Claude Code path-resolution issues
  #11011 / #17741 / #12541.
- `#cross-platform-authoring` — `plugin-AGENTS.md`: skills must not assume platform env vars
  (`${CLAUDE_PLUGIN_ROOT}`, `CODEX_SESSION_ID`) without a fallback; must name per-platform
  tool equivalents (`AskUserQuestion`/`request_user_input`/`ask_user`; `Agent`/`spawn_agent`/
  `subagent`; `TaskCreate`/`update_plan`); the `!`-backtick pre-resolution safety rules.
- `#caching-gotcha` — `plugin-AGENTS.md`: *"Plugin agent and skill definitions both cache at
  session start"* — edits don't propagate within a live session; use `skill-creator` to test,
  or restart. (Grounds the same caching behavior documented in
  [[sources/anthropic--plugins-reference#caching-and-file-resolution]].)
- `#legacy-cleanup` — when a skill/agent/command is removed, its name is registered in
  `STALE_SKILL_DIRS`/`STALE_AGENT_NAMES`/`STALE_PROMPT_FILES` (`src/utils/legacy-cleanup.ts`)
  + `EXTRA_LEGACY_ARTIFACTS_BY_PLUGIN` so stale flat-install artifacts are swept on upgrade.
- `#no-contributions` — README "About Contributions": *"I do not accept outside
  contributions for any of my projects… it's my name on the thing… Instead, I'll have
  Claude or Codex review submissions via `gh` and independently decide whether and how to
  address them."* The solo-high-velocity posture.
- `#coding-tutor` — `plugins/coding-tutor/` — the **second** plugin in the marketplace, by
  **Nityesh Agarwal**: 3 commands (`teach-me`, `quiz-me`, `sync-tutorials`) + 1 skill;
  personalized tutorials with spaced-repetition quizzes.
- `#package.json` — `@every-env/compound-plugin` v3.9.4; `bin: compound-plugin →
  src/index.ts`; deps `citty` + `js-yaml`; `semantic-release` toolchain.

## Why we cite this

- **The fully-verifiable embodiment of [[concepts/compound-engineering]].** The two
  every.to essays state the *philosophy*; this repo is the runnable proof, and uniquely it
  **dogfoods the loop on itself** — `docs/brainstorms/` (27) → `docs/plans/` (57) →
  `docs/solutions/` (30) is the literal artifact trail of brainstorm→plan→compound.
  ([[sources/every--compound-engineering-plugin#docs-solutions]], `#docs-brainstorms`,
  `#docs-plans`)
- **The wiki's first non-Garry tested skill pack.** 52 test files / ~1,094 cases including
  *behavioral contract* tests — the independent evidence that retires the "same-creator"
  caveat on [[patterns/quality-bar/skill-pack-bundle]] and [[patterns/behavioral/latent-vs-deterministic-split]],
  and the 2nd example that promotes [[patterns/quality-bar/complexity-ratchet]].
  ([[sources/every--compound-engineering-plugin#tests]])
- **A new axis for [[patterns/composition/single-source-multi-surface-distribution]]:** one
  Claude-format definition → ~11 *competing agent harnesses* via a converter CLI (not just
  runtimes you deploy to). ([[sources/every--compound-engineering-plugin#converter]],
  `#install-matrix`)
- **The `CLAUDE.md = @AGENTS.md` shim** — the cleanest in-wiki example of treating
  `AGENTS.md` as the canonical agent-facing doc with the harness-specific file as a 1-line
  redirect (2nd example after gbrain). ([[sources/every--compound-engineering-plugin#CLAUDE.md-shim]])
- **A masterclass in cross-platform skill authoring** — the `plugin-AGENTS.md` compliance
  checklist (description ≤1024 chars, quoted colons, no angle-bracket tokens, relative-path
  references, `!`-backtick safety) is hard-won portability knowledge.
  ([[sources/every--compound-engineering-plugin#cross-platform-authoring]], `#self-containment`)
- **Multi-agent review with structured-output + dedup** — `ce-code-review` spawns parallel
  persona/lens sub-agents returning JSON, then merges/dedups with confidence gating.
  ([[sources/every--compound-engineering-plugin#ce-code-review]])

## Popularity / credibility signals (captured at retrieval date)

- **Official Every artifact**: `package.json` "Official Compound Engineering plugin for
  Claude Code, Codex, and more"; published to npm as `@every-env/compound-plugin` v3.9.4;
  authored by Kieran Klaassen (GM of Cora at Every). As-of 2026-06-02.
- **Development velocity**: HEAD `3e77a7b` is PR **#893**, dated **2026-06-01** (one day
  before retrieval); 55 KB `CHANGELOG.md`; 27 brainstorms + 57 plans + 30 solutions; ~1,094
  test cases. A heavily-maintained, fast-moving repo, not a demo. As-of 2026-06-02.
- **GitHub stars / npm downloads**: **not captured** — `gh api repos/EveryInc/compound-engineering-plugin`
  not run this session. **TODO** (LINT): record a star/download count + date.
- **Talked-about signal**: subject of two Every essays ([[sources/every--compound-engineering]],
  [[sources/every--compound-engineering-gets-an-upgrade]]) and the origin piece *"My AI Had
  Already Fixed the Code Before I Saw It"* (plugin homepage). As-of 2026-06-02.

## Related sources

- [[sources/every--compound-engineering]] — the guide this plugin implements (the loop, the
  50/50 rule, the adoption ladder).
- [[sources/every--compound-engineering-gets-an-upgrade]] — Kieran's essay on the 4→8-step
  evolution; the conceptual companion.
- [[sources/anthropic--plugins-reference]] — the Claude Code plugin mechanism underneath:
  `plugin.json`, `${CLAUDE_PLUGIN_ROOT}`, and the **versioned-cache / session-cache** behavior
  this repo's `#caching-gotcha` and `#self-containment` rules navigate.
- [[sources/garrytan--gstack]] / [[sources/garrytan--gbrain]] — the other tested skill packs;
  the non-Garry comparison that retires same-creator caveats.
- [[creators/every]] — the publisher; Kieran Klaassen (author) + Dan Shipper (amplifier).
- Patterns grounded here: [[patterns/quality-bar/complexity-ratchet]],
  [[patterns/quality-bar/skill-pack-bundle]], [[patterns/composition/single-source-multi-surface-distribution]],
  [[patterns/behavioral/latent-vs-deterministic-split]], [[patterns/structural/thin-harness-fat-skills]],
  [[patterns/quality-bar/version-as-update-gate]].
