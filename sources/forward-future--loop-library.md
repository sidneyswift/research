---
domain: sources
type: repo
url: https://github.com/Forward-Future/loop-library
retrieved: 2026-06-20
snapshot-location: sources/forward-future--loop-library/
upstream-commit: 6ee3345b2a8c8bc6c3e2ecbcc51ddf8f4e56c5a1
last-reviewed: 2026-06-20
---

# Forward-Future/loop-library — the Loop Library

> Forward Future's open catalog of **loops** — copy-ready AI-agent prompts that each pair a task with a feedback check and an explicit stopping condition — plus the installable `loop-library` skill that helps an agent *find / adapt / design* one. 31 published loops at retrieval (a public site + machine-readable `catalog.json`/`catalog.md`, all generated from one canonical data file). The wiki's first source whose entire subject is the **agentic loop** as a prompt-design unit, and a strong second artifact for [[patterns/behavioral/evidence-gated-completion]].

*Done when it passes the [page checklist](_definition-of-done.md).*

## Snapshot details

- **Retrieved**: 2026-06-20
- **Where it lives in this wiki**: `sources/forward-future--loop-library/` (live local clone, `.git/` intact, git-ignored, in `repos.manifest.tsv` — rebuildable via `sources/clone-all.sh`)
- **Upstream URL**: https://github.com/Forward-Future/loop-library — published site at https://signals.forwardfuture.ai/loop-library/
- **Upstream identifier**: commit `6ee3345b2a8c8bc6c3e2ecbcc51ddf8f4e56c5a1` (HEAD of 2026-06-19 14:18 -0700), MIT license, repo created 2026-06-12
- **Repo shape**: `README.md` (what a loop is, why loops are bounded) · `AGENTS.md` (operating rules: canonical data + drift check, form security, clean-main deploys) · `scripts/loop-data.mjs` (**the canonical 31-loop dataset**) + sibling build scripts (`build-skill-catalog`, `build-loop-pages`, `build-social-images`, `audit-seo-geo`, `check`) · `skills/loop-library/` (`SKILL.md` + `references/catalog.md` offline fallback + `agents/openai.yaml` Codex interface) · `site/` (generated static site + `catalog.json`/`catalog.md`/`sitemap.xml`/`feed.xml`) · `worker/` (Cloudflare Worker guarding the submission forms) · `audits/`. Hundreds of versioned social-card images under `site/assets/social/` (skipped as evidence).

## Anchor map

Every claim that cites this source uses a `#anchor` suffix. Defined anchors:

- `#root` — the source as a whole
- `#README-what-is-a-loop` — README.md L13-39 — "What is a loop?": one-shot vs feedback prompt, the four questions a good loop answers (accomplish / how it knows it worked / what to do with the result / when to finish or ask for help)
- `#README-why-bounded` — README.md L40-54 — "Why loops are powerful": a clear finish line beats "keep improving"; "Loops are not permission for an agent to run forever… a real check, a clear stopping point, and a moment to hand control back to a person"
- `#README-skill` — README.md L56-91 — what the installable skill does (find / adapt / design / compress) + the explicit non-action guarantee ("does not quietly start schedules, change production, or send messages")
- `#SKILL.md` — skills/loop-library/SKILL.md (whole file)
- `#skill-description` — SKILL.md L3 — the `description:` trigger field (verbatim)
- `#skill-route` — SKILL.md L13-26 — "Route the request": the Find / Adapt / Design / Find-then-design router; "Choose the smallest useful path"
- `#skill-find` — SKILL.md L28-53 — "Find a published loop": live `catalog.md`/`catalog.json` is source of truth; "Never invent a Loop Library title, number, contributor, or URL"
- `#skill-grounding` — SKILL.md L55-66 — "Keep adaptations grounded": "Do not invent a technology stack, tool, metric…"; "Never present a guess as a 'sensible default.'"
- `#skill-interview` — SKILL.md L68-90 — "Run the design interview": one short question at a time, plain language, the five questions; "do not use terms such as trigger, success gate, terminal state, guardrail"
- `#skill-feedback-cycle` — SKILL.md L92-126 — "Design the feedback cycle": the six-step Observe / Choose / Act / Verify / Record / Repeat-or-stop sequence + the design rules (observable success gate, named terminal states, no-progress stop, re-read state, preserve work, separate working-signal from acceptance gate, independent verification, recommend one-shot when no feedback helps)
- `#skill-terminal-states` — SKILL.md L110-113 — "Define success, clean no-op, blocked, approval-required, exhausted, and stagnated outcomes… Never report an error or exhausted budget as success."
- `#skill-deliver` — SKILL.md L131-166 — "Deliver the loop": the <80-word compressed prompt format + the trigger/action/feedback-check/stop/approval compression guide
- `#AGENTS.md-canonical` — AGENTS.md L3-47 — `scripts/loop-data.mjs` is "the canonical SEO/GEO content catalog"; generated surfaces (homepage rows, live catalogs, installable-skill fallback, detail pages, structured data, sitemap, feed) must stay aligned or `check.mjs` reports **drift** and the loop is rejected
- `#loop-data` — scripts/loop-data.mjs — the 31-loop dataset; each entry carries `slug`, `title`, `summary`, `seoTitle`, `description`, `categoryLabel`, `author`, `sourceUrl?`, `published`, `modified`, `prompt`, `verifyTitle`, `verifyDetail`, `useWhen`, `steps[]`, `why`, `note`, `keywords[]`, `related[]`
- `#loop-001-docs-sweep` — loop-data.mjs L52-89 — the docs sweep (Matthew Berman)
- `#loop-005-test-coverage` — loop-data.mjs L207-243 — the 100% test coverage loop (the shortest prompt; "Add tests until we have 100% test coverage")
- `#loop-009-quality-streak` — loop-data.mjs L361-399 — the quality streak loop (failure → regression coverage → restart streak)
- `#loop-019-clodex` — loop-data.mjs L756-795 — Clodex adversarial-review loop (Codex reviews Claude's PR)
- `#loop-020-loop-harness` — loop-data.mjs L796-835 — Loop Harness verification loop (second-agent gate in an isolated worktree)
- `#loop-021-boeing` — loop-data.mjs L836-875 — Boeing 747 benchmark (nine-angle render + critic)
- `#loop-023-champion` — loop-data.mjs L916-954 — self-improving champion loop (promote only on fresh-holdout wins)
- `#loop-024-devils-advocate` — loop-data.mjs L955-993 — devil's-advocate loop (critic/builder + persistent objection log)
- `#loop-027-autonomy` — loop-data.mjs L1072-1111 — autonomy-loop builder/reviewer (red-before/green-after + revert-or-mutate proof-of-test)
- `#loop-028-completion-contract` — loop-data.mjs L1112-1152 — Codex completion-contract loop (define done up front; requirement→evidence table; "budget exhaustion never counts as success")
- `#loop-029-revolve` — loop-data.mjs L1153-1192 — Revolve versioned-experiment loop (frozen evaluation revision + checkpoints)
- `#loop-031-recent-feedback` — loop-data.mjs L1235-1274 — recent-feedback sweep (recent corrections → failure patterns → project-wide audit)
- `#openai-yaml` — skills/loop-library/agents/openai.yaml — the Codex `agents/openai.yaml` interface extension (display name, short description, default prompt)
- `#catalog-md` — skills/loop-library/references/catalog.md — the generated, dated offline catalog the skill falls back to when live web access is unavailable
- `#github-stars` — popularity signal captured at retrieval (see below)

## Why we cite this

Claims about: the **loop** as a prompt-design unit (feedback + observable verification + named terminal states, vs a one-shot prompt); evidence-gated completion stated in plain language and at scale ("Never report an error or exhausted budget as success"); the six-step Observe→Choose→Act→Verify→Record→Repeat-or-stop cycle; loops as **parameterized templates** (`[N]`, `[budget]`, `[margin]`, `[quality threshold]`); generator/verifier role separation (Clodex, Loop Harness, autonomy-loop, devil's-advocate); overfit-resistant self-improvement (separate the working signal from a fresh acceptance gate; champion/challenger; Revolve revisions); a single canonical data file fanned out to many surfaces behind a drift check; and the design-interview ("one short question at a time") as an align-before-execute move.

## Popularity signals (if this source provides them)

- **Signal type**: github-stars / forks (via `gh repo view Forward-Future/loop-library`)
- **Value at snapshot**: **92 ★**, **14 forks**, MIT. Repo created 2026-06-12; last push 2026-06-19 (one week old at retrieval).
- **As-of**: 2026-06-20
- **Publisher reach (secondary)**: Forward Future is **Matthew Berman**'s AI media brand (large YouTube/newsletter following); Berman authored ~15 of the 31 loops and is the named owner of the deploy infrastructure (`loop-library-forms.mberman84.workers.dev`, `/Users/matthewberman/.codex/deploy-locks/…` per [[sources/forward-future--loop-library#AGENTS.md-canonical]]). Several loops are contributed by recognizable builders (Peter Steinberger, Hiten Shah, Pierson Marks, Lukas Kucinski) — a curated-submission signal more than a raw-star one (the repo is one week old).
- **Distribution**: installable via `npx skills add Forward-Future/loop-library --skill loop-library -g` (the skills.sh installer, same channel as [[sources/mattpocock--skills]]); ships an `agents/openai.yaml` so it also surfaces as a **Codex** skill.

## Related sources

- [[sources/openai--using-goals-in-codex]] — Codex **Goals** state the evidence-gated-completion rule formally; loop #028 (the completion-contract loop) wraps exactly that mechanism (`$goal-planner-codex`), and the SKILL.md's "never report exhausted as success" restates it. The Loop Library is the plain-language, multi-instance counterpart.
- [[sources/mattpocock--skills]] — same installer (skills.sh) and same `SKILL.md` open-standard format; the Loop Library's "design interview" is the same align-before-execute / grilling move as `mattpocock/grilling`.
- [[sources/openai--codex-skills-doc]] — defines the `agents/openai.yaml` extension the Loop Library ships ([[sources/forward-future--loop-library#openai-yaml]]).
