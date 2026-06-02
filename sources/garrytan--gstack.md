---
domain: sources
type: repo
url: https://github.com/garrytan/gstack
retrieved: 2026-05-21
snapshot-location: sources/garrytan--gstack/
upstream-commit: 029356e1f0693f22cb1fa4524c9b0f28ceab5a1b
upstream-commit-date: 2026-05-20
last-reviewed: 2026-05-21
license: MIT
---

# gstack (`garrytan/gstack`)

> Garry Tan's opinionated Claude Code skills pack. 23+ workflow skills + 8 power tools, structured as a virtual engineering team (CEO, Designer, Eng Manager, QA Lead, CSO, Release Engineer). Installs into `~/.claude/skills/gstack` via a setup script.

## Snapshot details

- **Retrieved**: 2026-05-21
- **Location**: `sources/garrytan--gstack/` (41 MB, `.git/` stripped)
- **Upstream URL**: https://github.com/garrytan/gstack
- **Upstream commit**: `029356e` (2026-05-20)
- **Author claim** ([sources/garrytan--gstack/README.md L1-30](sources/garrytan--gstack/README.md)): "President & CEO of Y Combinator." Co-authored with Claude Opus 4.6 per commit history.

## Anchor map

### Root docs (each large, citation-worthy)
- `#root` — repo as a whole
- `#README` — `README.md` (42 KB) — pitch, install, philosophy
- `#SKILL.md` — root `SKILL.md` (47 KB) — generated from `SKILL.md.tmpl`; the unified `/browse` preamble + auto-loading skill chooser
- `#CLAUDE.md` — `CLAUDE.md` (49 KB) — operating instructions injected into projects that install gstack
- `#ETHOS.md` — `ETHOS.md` (7 KB) — the "Builder Ethos" philosophy preamble; injected into every workflow skill
- `#ARCHITECTURE.md` — `ARCHITECTURE.md` (32 KB)
- `#BROWSER.md` — `BROWSER.md` (60 KB) — browser-automation contract
- `#DESIGN.md` — `DESIGN.md` (4 KB)
- `#CHANGELOG.md` — `CHANGELOG.md` (690 KB! — every version detail)
- `#TODOS.md` — `TODOS.md` (111 KB)
- `#using-gbrain-with-gstack` — `USING_GBRAIN_WITH_GSTACK.md` (28 KB) — the cross-product integration doc

### Skill directories (each has its own SKILL.md + often references/, templates/)
Slash command → directory:
- `#office-hours` — `office-hours/` (CEO brainstorming intake)
- `#plan-ceo-review` — `plan-ceo-review/`
- `#plan-eng-review` — `plan-eng-review/`
- `#plan-design-review` — `plan-design-review/`
- `#plan-devex-review` — `plan-devex-review/`
- `#design-consultation`, `#design-shotgun`, `#design-html`, `#design-review` — design family
- `#review` — `review/` (production-bug-hunting reviewer)
- `#ship` — `ship/` (one-command release)
- `#land-and-deploy` — `land-and-deploy/`
- `#canary` — `canary/`
- `#qa` — `qa/` (Playwright browser QA)
- `#qa-only` — `qa-only/` (QA without auto-fix)
- `#cso` — `cso/` (chief security officer — OWASP+STRIDE)
- `#investigate` — `investigate/` (debugging)
- `#retro` — `retro/` (engineering retrospective)
- `#freeze`, `#guard`, `#unfreeze` — release-train safety family
- `#document-release`, `#document-generate` — doc-engineering family
- `#browse` — `browse/` (the unified browser tool gstack-wide)
- `#setup-gbrain`, `#sync-gbrain` — gbrain integration
- `#autoplan`, `#pair-agent`, `#careful`, `#codex`, `#learn`, `#skillify`, `#open-gstack-browser` — auxiliary

### Infrastructure dirs
- `#bin` — `bin/` (60 entries — gstack CLI scripts)
- `#lib` — `lib/` (shared shell library)
- `#test` — `test/` — the skill-pack test harness: `skill-validation.test.ts` + `gen-skill-docs.test.ts` (Tier 1 unit, free), `skill-llm-eval.test.ts` (Tier 3 LLM-as-judge, ~$0.15/run), `skill-e2e-*.test.ts` (Tier 2 E2E via `claude -p`, ~$3.85/run), and resolver evals (`resolver-ask-user-format.test.ts`, `writing-style-resolver.test.ts`, `resolvers-gbrain-put-rewrite.test.ts`). `test/helpers/touchfiles.ts` drives diff-based selection; `E2E_TIERS` splits `gate` (CI-blocking) from `periodic` (weekly cron).
- `#agents`, `#contrib`, `#extension`, `#claude`, `#scripts`, `#docs`

## Why we cite this

This is the most talked-about Claude Code skills pack of 2026. We cite it for:
- The "virtual engineering team" persona pattern (CEO, Designer, etc.) vs. task-category patterns
- Custom frontmatter extensions (`preamble-tier`, `version`, `allowed-tools`, `triggers`, voice triggers)
- The ETHOS preamble injection — embedding *philosophy* into every skill call
- The unified `/browse` skill as a *shared substrate* for other skills
- Multi-tier skill modes (Quick / Standard / Exhaustive for `/qa`)
- The "skill pack as a real shipping product" — versioning, changelog, team-mode setup, auto-update checks

## Popularity signals

- **Hacker News**: front-page thread at https://news.ycombinator.com/item?id=47418576 — TODO snapshot
- **Product Hunt**: shipped (per search) — TODO capture launch-day metrics
- **GitHub stars**: **105,761** — **verified** via `gh api repos/garrytan/gstack` (as-of 2026-06-01). The essay's self-claim ([[sources/garrytan--foxconn-factories#gstack-stars]]) of "about 105,000 stars in under three months" **checks out**: measured 105,761 (the author rounded *down*), and the repo was created **2026-03-11** — just under three months ago, so the timeframe holds. The companion "one of the hundred most-starred open source projects in GitHub history" is *plausible* at this count but is a ranking claim we did **not** independently verify (would need a current GitHub-wide stars leaderboard). The earlier skepticism cited the sibling gbrain at only ~14K; that figure was itself stale — gbrain now measures **20,403** (as-of 2026-06-01), and gstack's count is confirmed on its own terms regardless. Promoted from caveated self-claim to **measured fact** at this date; stars move, so re-measure before citing later.
- **Press coverage**: at least 6 third-party writeups (sitepoint, mindstudio, augmentcode, buildthisnow, awesomeagents, explainx) — TODO snapshot one or two
- **Author position**: Garry Tan, President/CEO of Y Combinator — distribution advantage built-in

## Related sources

- [[sources/garrytan--foxconn-factories]] — Garry's essay *about* this artifact: the "skill pack" definition (grounded in this repo's `#test` harness), the ~105K-star claim, and the OpenClaw-authorship correction.
- [[sources/garrytan--gbrain]] — sibling memory product; gstack ships `/setup-gbrain` and `/sync-gbrain` to integrate
- [[sources/anthropic--skills]] — gstack extends Anthropic's skill format with custom frontmatter
