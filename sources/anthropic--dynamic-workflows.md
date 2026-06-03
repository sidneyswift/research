---
domain: sources
type: article
url: https://x.com/trq212/status/2061907337154367865
retrieved: 2026-06-02
snapshot-location: sources/anthropic--dynamic-workflows/snapshot.md
upstream-commit: n/a (article)
last-reviewed: 2026-06-02
---

# A harness for every task: dynamic workflows in Claude Code

> **One-line:** Anthropic engineers Thariq Shihipar and Sid Bidasaria explain Claude Code's new *dynamic workflows* feature — where the model writes its own JavaScript harness on the fly, spawning subagents with isolated context windows to solve tasks that break down in a single context window (agentic laziness, self-preferential bias, goal drift).

*Done when it passes the [page checklist](../_schemas/_definition-of-done.md).*

## Snapshot details

- **Retrieved**: 2026-06-02
- **Where it lives in this wiki**: `sources/anthropic--dynamic-workflows/snapshot.md` (committed)
- **Upstream URL**: https://x.com/trq212/status/2061907337154367865 (X article: https://x.com/i/article/2061850535708483585)
- **Mirror**: https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
- **Upstream identifier**: X post ID `2061907337154367865`, published 2026-06-02T20:26:32Z
- **Authors**: Thariq Shihipar (@trq212) and Sid Bidasaria (@sidbid), members of technical staff at Anthropic, working on Claude Code

## Anchor map

- `#root` — the article as a whole
- `#title` — "A harness for every task: dynamic workflows in Claude Code" — the framing: dynamic harness creation
- `#example-prompts` — 8 example prompts showing workflow use cases
- `#how-it-works` — dynamic workflows execute a JS file with special functions to spawn/coordinate subagents
- `#model-routing` — workflows can decide which models subagents use and whether they run in their own worktree
- `#why-workflows` — the three failure modes: agentic laziness, self-preferential bias, goal drift
- `#agentic-laziness` — Claude stops before finishing, declares done after partial progress
- `#self-preferential-bias` — Claude prefers its own results when asked to verify/judge
- `#goal-drift` — gradual loss of fidelity to original objective across compaction; summarization is lossy
- `#dynamic-vs-static` — static workflows (Agent SDK / `claude -p`) are generic; dynamic workflows are custom-built per task
- `#opus-4-8` — "With Claude Opus 4.8 and dynamic workflows, Claude is now intelligent enough to write a custom harness tailor-made for your use case"
- `#patterns` — six workflow patterns: classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done
- `#classify-and-act` — classifier agent routes to different agents based on task type
- `#fan-out-and-synthesize` — split task → parallel agents → synthesize barrier → merge
- `#adversarial-verification` — for each agent, a separate agent adversarially verifies output
- `#generate-and-filter` — generate ideas → filter by rubric/verification → dedupe → return best
- `#tournament` — N agents compete on same task, pairwise judging until winner
- `#loop-until-done` — loop spawning agents until stop condition (no new findings, no errors)
- `#use-cases` — use case catalog: migrations, deep research, deep verification, sorting, memory/rule adherence, root-cause investigation, triaging, exploration/taste, evals, model routing
- `#bun-rewrite` — "Bun was rewritten from Zig to Rust using workflows" (Jarred Sumner reference)
- `#deep-research-skill` — `/deep-research` skill inside Claude Code uses dynamic workflows (fan-out + adversarial verify + synthesize)
- `#quarantine-pattern` — triage: bar untrusted-content-reading agents from high-privilege actions
- `#ultracode` — trigger word "ultracode" ensures Claude Code creates a workflow
- `#saving-workflows` — press "s" to save; check into `~/.claude/workflows` or distribute via skill
- `#skill-distribution` — put JS workflow files in skill folder, reference in SKILL.MD; treat as template not verbatim script
- `#when-not-to-use` — "most traditional coding tasks do not need a panel of 5 reviewers"; workflows use more tokens
- `#goal-and-loop` — combine with `/goal` (hard completion) and `/loop` (repeat at intervals)

## Why we cite this

This is the **first official Anthropic technical deep-dive on how the Claude Code harness works internally** — specifically how it spawns subagents, routes models, isolates context windows, and orchestrates multi-agent workflows. Critical for:

- **Resolving the `thin-harness-fat-skills` promotion question.** The wiki's longest-standing open question is "what does the harness middle actually look like?" This article describes the harness from inside Anthropic. The harness is a JS file that spawns/coordinates subagents — and with dynamic workflows, the *model itself writes the harness*, making it definitionally thin (generated per-task, not a permanent fat layer).
- **Naming the three failure modes** that justify multi-agent architectures: agentic laziness, self-preferential bias, goal drift.
- **Cataloging six reusable workflow patterns** from the team that builds the harness.
- **Grounding the `evidence-gated-completion` pattern** — `/goal` is explicitly paired with workflows for "hard completion requirements."
- **Connecting to `convergent-agent-plugin-spec`** — workflows can be distributed as skills (JS files in a skill folder referenced in SKILL.MD), extending the skill spec into orchestration.

## Popularity signals

- **Signal type**: tweet-engagement
- **Values at snapshot**: 3,340 likes · 331 retweets · 81 quotes · 7,574 bookmarks · 597,457 impressions · 91 replies
- **As-of**: 2026-06-02

Note: 7,574 bookmarks (2.3x the likes) — one of the highest bookmark-to-like ratios we've seen. People are saving this as a reference document, not just engaging with it.

## Related sources

- [[sources/anthropic--plugins-reference]] — the official plugins/skills spec that workflows extend (JS files distributed via skills)
- [[sources/openai--using-goals-in-codex]] — OpenAI's `/goal` in Codex; this article pairs `/goal` with workflows for the same purpose (evidence-gated completion)
- [[sources/garrytan--thin-harness-fat-skills]] — Garry Tan's essay defining the architecture; this article is the view *from inside* the harness
- [[sources/garrytan--foxconn-factories]] — the "Foxconn factory" anti-pattern this article implicitly argues against (dynamic workflows = JIT harness, not factory)
