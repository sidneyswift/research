---
domain: sources
type: repo
url: https://github.com/mattpocock/skills
retrieved: 2026-06-19
snapshot-location: sources/mattpocock--skills/
upstream-commit: 6eeb81b5fcfeeb5bd531dd47ab2f9f2bbea27461
last-reviewed: 2026-06-19
---

# mattpocock/skills — "Skills For Real Engineers"

> Matt Pocock's personal, daily-driver agent-skills pack (`npx skills@latest add mattpocock/skills`) — ~17 published `SKILL.md` files organized into invocation-typed buckets, built explicitly *against* process-owning frameworks (GSD/BMAD/Spec-Kit) and grounded in classic software-engineering books. The wiki's first **individual-engineer skill pack distributed via skills.sh**, and (at 135K★) one of its highest-signal sources.

*Done when it passes the [page checklist](_definition-of-done.md).*

## Snapshot details

- **Retrieved**: 2026-06-19
- **Where it lives in this wiki**: `sources/mattpocock--skills/` (live local clone, `.git/` intact, git-ignored, in `repos.manifest.tsv` — rebuildable via `sources/clone-all.sh`)
- **Upstream URL**: https://github.com/mattpocock/skills
- **Upstream identifier**: commit `6eeb81b5fcfeeb5bd531dd47ab2f9f2bbea27461` (HEAD of 2026-06-18 09:41 +0100), package `version: 1.0.1`, MIT license
- **Repo shape**: `.claude-plugin/plugin.json` (17-skill manifest) · `skills/` in 6 buckets · `docs/` (invocation guide + 1 ADR) · `.out-of-scope/` (3 rejected-scope notes) · `README.md` · `CLAUDE.md` · `CONTEXT.md` · `CHANGELOG.md` + `.changeset/` (release-please-style) · `scripts/` (`link-skills.sh`, `list-skills.sh`). **No test suite** (verified against the tree).

## Anchor map

Every claim that cites this source uses a `#anchor` suffix. Defined anchors:

- `#root` — the source as a whole
- `#README-philosophy` — README.md L17-19 — "small, easy to adapt, and composable… work with any model… real engineering - not vibe coding"; the explicit anti-framework stance ("GSD, BMAD, and Spec-Kit … take away your control")
- `#README-why` — README.md L42-140 — "Why These Skills Exist": the four failure modes (didn't-do-what-I-want / too-verbose / doesn't-work / ball-of-mud) each paired with a fix and a classic-book epigraph (Pragmatic Programmer, DDD, XP, Philosophy of Software Design)
- `#README-reference` — README.md L142-191 — the skill catalog, grouped User-invoked / Model-invoked
- `#CLAUDE.md` — CLAUDE.md (whole file) — the bucket taxonomy + the rule that engineering/productivity/misc skills must appear in README + plugin.json while personal/in-progress/deprecated must not
- `#CONTEXT.md` — CONTEXT.md (whole file) — the repo's own ubiquitous-language doc (Issue tracker / Issue / Triage role + flagged ambiguities)
- `#docs-invocation` — docs/invocation.md — definitions of user-invoked vs model-invoked, the "user-invoked may call model-invoked but never another user-invoked" rule, prose `/skill`-style invocation, passive-vs-active domain work
- `#plugin.json` — .claude-plugin/plugin.json — the 17-skill manifest (12 engineering + 5 productivity; misc skills present in README but **absent from this manifest**)
- `#skill-grilling` — skills/productivity/grilling/SKILL.md — the reusable interview loop (one question at a time; explore the codebase instead of asking)
- `#skill-grill-with-docs` — skills/engineering/grill-with-docs/SKILL.md — a 2-line composite: "Run a `/grilling` session, using the `/domain-modeling` skill"
- `#skill-writing-great-skills` — skills/productivity/writing-great-skills/SKILL.md — the skill-authoring vocabulary (predictability, the two loads, the information-hierarchy ladder, leading words, the five failure modes)
- `#skill-codebase-design` — skills/engineering/codebase-design/SKILL.md — the deep-module glossary (Module/Interface/Implementation/Depth/Seam/Adapter/Leverage/Locality) + the deletion test + "one adapter = hypothetical seam, two = real"
- `#skill-ask-matt` — skills/engineering/ask-matt/SKILL.md — the human-facing router over the user-invoked skills; the idea→ship "main flow"; the "smart zone" (~120k-token) context-hygiene note
- `#skill-domain-modeling` — skills/engineering/domain-modeling/SKILL.md — the active build/sharpen discipline; `CONTEXT.md` is "a glossary and nothing else"; ADRs only when hard-to-reverse + surprising + a real trade-off
- `#buckets` — the six-bucket taxonomy (engineering / productivity / misc / personal / in-progress / deprecated) and the promotion rule
- `#out-of-scope` — .out-of-scope/ — the rejected-scope registry (mainstream-issue-trackers-only, question-limits, setup-skill-verify-mode)
- `#github-stars` — popularity signal captured at retrieval (see below)

## Why we cite this

Claims about: how a *small, composable, model-agnostic* skill pack is designed against process-frameworks; the user-invoked vs model-invoked invocation axis and its two-load trade-off; the grilling / align-before-execute interview; ubiquitous-language / `CONTEXT.md` for agents; deep-module design vocabulary; the skill-authoring vocabulary in `writing-great-skills`; and a high-popularity pack that ships **no tests** (the counter-example to [[patterns/quality-bar/skill-pack-bundle]]).

## Popularity signals (if this source provides them)

- **Signal type**: github-stars / forks (via `gh api repos/mattpocock/skills`)
- **Value at snapshot**: **135,831 ★**, **11,770 forks**, MIT. Repo created 2026-02-03; last push 2026-06-18. Listed on skills.sh (`skills.sh/mattpocock/skills`).
- **As-of**: 2026-06-19
- **Creator reach (secondary)**: author states "~60,000 … devs on my newsletter" (aihero.dev) ([[sources/mattpocock--skills#README-philosophy]]); Matt Pocock is the author of Total TypeScript / AI Hero — an established TypeScript educator, which is the credibility backdrop for the repo's velocity.

## Related sources

- [[sources/anthropic--skills]] — the official Agent Skills demonstration repo; mattpocock is the high-traffic *individual* counterpart (same `SKILL.md` format, opposite authorship).
- [[sources/agentskills--specification]] — the open standard these `SKILL.md` files conform to; `skills.sh` is the cross-harness installer that distributes them.
- [[sources/garrytan--gstack]] — the other individual-authored opinionated engineering pack; gstack is heavy/tested/harness-OS, mattpocock is small/untested/composable — a direct house-style contrast.
- [[sources/every--compound-engineering-plugin]] — shares the align-before-build move (CE's brainstorm/plan vs mattpocock's grill) and fat-markdown-skills shape.
