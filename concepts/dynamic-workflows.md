---
domain: concepts
type: concept
name: dynamic-workflows
creators:
  - "[[creators/anthropic]]"
sources:
  - "[[sources/anthropic--dynamic-workflows]]"
status: active
last-reviewed: 2026-06-02
popularity-signals:
  - signal: tweet-traction
    value: "3,340 likes · 7,574 bookmarks · 597K impressions"
    as-of: 2026-06-02
    source: "[[sources/anthropic--dynamic-workflows#root]]"
---

# Dynamic Workflows

> **One-line:** The model writes its own JavaScript harness on the fly — spawning subagents with isolated context windows, routing models, and composing orchestration patterns — to solve tasks that break down in a single context window due to agentic laziness, self-preferential bias, and goal drift.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): read everything about the idea across sources, then write distilled judgment — not a summary of any single source. Shape: **compiled truth on top** (edited in place) + an **append-only `## Timeline`** below (gbrain's brain-page schema). Done when it passes the [page checklist](../_schemas/_definition-of-done.md).*

## What it is

Dynamic workflows are a Claude Code feature (released week of 2026-05-26, documented 2026-06-02) where the model generates a JavaScript workflow file that orchestrates multiple subagents, each running in their own context window with focused, isolated goals. Unlike static workflows (Claude Agent SDK / `claude -p`) which are pre-written and generic, dynamic workflows are **custom-built per task** — the model analyzes the task, selects appropriate orchestration patterns, and writes the harness on the fly.

The JavaScript runtime provides special functions for spawning/coordinating subagents plus standard JS functions (JSON, Math, Array) for data processing. Crucially, workflows can decide **which models** subagents use and whether they run in **isolated worktrees**, allowing intelligence-level and isolation routing ([[sources/anthropic--dynamic-workflows#model-routing]]).

Workflows are resumable (interruption → resume picks up where it left off), saveable (press "s" → `~/.claude/workflows/`), and distributable via skills (put JS files in a skill folder, reference in SKILL.MD) ([[sources/anthropic--dynamic-workflows#saving-workflows]], [[sources/anthropic--dynamic-workflows#skill-distribution]]).

## Where it came from

Built by Thariq Shihipar and Sid Bidasaria at Anthropic, working on Claude Code. Published 2026-06-02 as an X article and simultaneously on the Claude Blog. The feature itself shipped with Claude Code the week prior. Requires Claude Opus 4.8 or later — "Claude is now intelligent enough to write a custom harness tailor-made for your use case" ([[sources/anthropic--dynamic-workflows#opus-4-8]]).

Prior art within Claude Code: Research, security analysis, agent teams, and Code Review were all custom harnesses built *on top of* Claude Code by Anthropic — dynamic workflows generalize that pattern so users can create equivalent harnesses without Anthropic building them ([[sources/anthropic--dynamic-workflows#root]]).

## Why it matters

### The three failure modes it solves

Dynamic workflows exist because single-context-window execution breaks down on complex tasks in three specific, named ways ([[sources/anthropic--dynamic-workflows#why-workflows]]):

1. **Agentic laziness** — Claude stops before finishing a complex multi-part task and declares done after partial progress (e.g., 20 of 50 items in a security review) ([[sources/anthropic--dynamic-workflows#agentic-laziness]]).
2. **Self-preferential bias** — Claude prefers its own results when asked to verify or judge against a rubric ([[sources/anthropic--dynamic-workflows#self-preferential-bias]]).
3. **Goal drift** — gradual loss of fidelity to the original objective across many turns, especially after compaction. "Each summarization step is lossy, and details like edge-case requirements or 'don't do X' constraints can get lost" ([[sources/anthropic--dynamic-workflows#goal-drift]]).

### Six composable patterns

The article catalogs six workflow patterns Claude uses and composes ([[sources/anthropic--dynamic-workflows#patterns]]):

| Pattern | Mechanism | Key property |
|---------|-----------|-------------|
| **Classify-and-act** | Classifier routes to specialized agents | Task-type routing |
| **Fan-out-and-synthesize** | Split → parallel agents → barrier → merge | Isolation prevents cross-contamination |
| **Adversarial verification** | For each agent, a separate verifier checks output | Defeats self-preferential bias |
| **Generate-and-filter** | Generate ideas → filter by rubric → dedupe → return best | Quality through elimination |
| **Tournament** | N agents compete, pairwise judging until winner | Comparative judgment > absolute scoring |
| **Loop-until-done** | Loop until stop condition (no new findings) | Unknown-scope work |

### The harness-as-JIT-software implication

This concept directly addresses the wiki's longest-standing open question about [[patterns/structural/thin-harness-fat-skills]]: *what does the harness middle actually look like?* The answer from inside Anthropic: the harness is a generated JS file — definitionally thin because it's written per-task and composed from a small set of primitives (spawn, coordinate, synthesize). The model itself decides the orchestration shape, then executes it. This is Garry Tan's "just-in-time software" ([[sources/garrytan--foxconn-factories]]) applied to the harness layer itself.

## Evidence & claims

- **Dynamic workflows generate a JS file with special spawn/coordinate functions.** — *demonstrated* (feature shipped). Citation: [[sources/anthropic--dynamic-workflows#how-it-works]]
- **Three named failure modes: agentic laziness, self-preferential bias, goal drift.** — *asserted with examples but not quantified*. Citation: [[sources/anthropic--dynamic-workflows#why-workflows]]
- **Bun was rewritten from Zig to Rust using workflows** (Jarred Sumner). — *asserted, linked*. Citation: [[sources/anthropic--dynamic-workflows#bun-rewrite]]
- **`/deep-research` skill uses dynamic workflows** (fan-out + adversarial verify + synthesize). — *demonstrated* (shipped skill). Citation: [[sources/anthropic--dynamic-workflows#deep-research-skill]]
- **"Ultracode" trigger word ensures workflow creation.** — *demonstrated*. Citation: [[sources/anthropic--dynamic-workflows#ultracode]]
- **Workflows can be distributed via skills** (JS files in skill folder, referenced in SKILL.MD). — *demonstrated*. Citation: [[sources/anthropic--dynamic-workflows#skill-distribution]]
- **Quarantine pattern for triage:** bar untrusted-content-reading agents from high-privilege actions. — *asserted*. Citation: [[sources/anthropic--dynamic-workflows#quarantine-pattern]]
- **Workflows use significantly more tokens** — the article warns about this repeatedly. — *asserted*. Citation: [[sources/anthropic--dynamic-workflows#when-not-to-use]]

## Patterns demonstrated

- [[patterns/structural/thin-harness-fat-skills]] — *the article is the harness viewed from the inside.* Dynamic workflows are literally generated harnesses — thin by definition (written per-task from primitives, not a permanent fat layer). This is the strongest evidence yet for the "thin harness" claim: the harness is so thin the model can write it. The fat-skills layer (SKILL.MD, CLAUDE.md rules) provides the domain knowledge; the harness JS provides the orchestration. Citation: [[sources/anthropic--dynamic-workflows#how-it-works]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — *workflows separate model judgment from deterministic orchestration.* The JS file is the deterministic backbone (spawn order, barrier waits, merge logic); each subagent brings model judgment in an isolated context. The "sorting" use case makes this explicit: "the deterministic loop holds the bracket and only the running order stays in context." Citation: [[sources/anthropic--dynamic-workflows#patterns]]
- [[patterns/behavioral/evidence-gated-completion]] — *"/goal" is paired with workflows for hard completion requirements.* Citation: [[sources/anthropic--dynamic-workflows#goal-and-loop]]
- [[patterns/composition/resolver-routing-table]] — *"classify-and-act" is a dynamic resolver: a classifier agent routes to specialized agents based on task type.* Citation: [[sources/anthropic--dynamic-workflows#classify-and-act]]. Also: "model and intelligence routing" — a classifier decides which model to use based on codebase shape. Citation: [[sources/anthropic--dynamic-workflows#model-routing]]
- [[patterns/behavioral/skill-as-method-call]] — *each workflow pattern is a parameterized template (same pattern, different task → different harness).* Citation: [[sources/anthropic--dynamic-workflows#patterns]]

**Proposed new patterns (1 example each, candidates for promotion):**

- **Adversarial verification via isolated subagents** — structurally defeating self-preferential bias by spawning a separate verifier agent per producer agent. Distinctly named and documented. Citation: [[sources/anthropic--dynamic-workflows#adversarial-verification]]. Note: FSI's trust-tiered subagents (reader/writer/critic separation) are a related but structurally different take — FSI separates by *privilege*, Anthropic separates by *adversarial role*. If both are paged, they may form a confirmed pattern about "structural bias defeat via agent isolation."
- **Quarantine (triage privilege separation)** — agents reading untrusted content are barred from taking high-privilege actions; privileged agents act on classified/clean data only. Citation: [[sources/anthropic--dynamic-workflows#quarantine-pattern]]. This is the same principle as FSI's trust-tiered subagents — could confirm that proposed pattern.

## Tensions & counter-arguments

- **Token cost.** The article itself warns repeatedly that workflows use significantly more tokens. Every subagent gets its own context window — the total token consumption can be much higher than a single-context approach. The question is whether the quality improvement justifies the cost for a given task.
- **"Thin harness" or "no harness"?** If the model writes the harness dynamically, is the harness *thin* or *absent*? Garry Tan's essay describes a persistent ~200-line loop; dynamic workflows generate a disposable JS file per task. These are different architectures — one is a permanent thin layer, the other is JIT orchestration that didn't exist before the task. The wiki should track whether "thin harness" evolves to "generated harness" as the concept matures.
- **Best practices still developing.** The authors explicitly say so. The patterns cataloged are initial observations, not battle-tested best practices.
- **Opus 4.8 dependency.** The feature requires a model intelligent enough to write correct JS orchestration code. This makes it model-generation-dependent in a way that static workflows (pre-written by humans) are not.

## Timeline (append-only)

- 2026-05-26 (approx) — Dynamic workflows feature ships in Claude Code ([[sources/anthropic--dynamic-workflows#root]])
- 2026-06-02 — Thariq Shihipar and Sid Bidasaria publish "A harness for every task" X article + Claude Blog post documenting the feature, patterns, and use cases ([[sources/anthropic--dynamic-workflows#root]]). 7,574 bookmarks in first ~4 hours.

## Related

- [[concepts/completion-contract]] — `/goal` pairs with workflows; dynamic workflows are the *execution substrate* for completion contracts
- [[concepts/convergent-agent-plugin-spec]] — workflows distributed via skills extend the skill spec into orchestration territory
- [[patterns/structural/thin-harness-fat-skills]] — dynamic workflows are the harness *viewed from the inside*; the strongest evidence for "thin" yet
- [[patterns/behavioral/evidence-gated-completion]] — `/goal` + `/loop` explicitly paired with workflows

## What we'd steal

- ★ **The three failure modes as a design checklist.** Before building any multi-agent system, ask: does this task suffer from agentic laziness (partial completion), self-preferential bias (self-review), or goal drift (long context + compaction)? If yes, isolated subagents are the structural fix.
- ★ **Six composable patterns as a pattern library.** Classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done — these are the building blocks. Our own wiki operations (INGEST, LINT) could use these.
- ★ **Quarantine pattern for untrusted content.** Agents reading untrusted input can't take privileged actions — clean separation of read-untrusted and write-privileged roles. Directly applicable to any system processing external content (webhooks, user submissions, wiki ingest from URLs).
- ★ **Workflow distribution via skills.** JS workflow files in a skill folder, referenced in SKILL.MD, treated as templates not verbatim scripts — extends the skill spec into orchestration. Directly implementable in our research wiki's own operations.
- **"Ultracode" trigger word.** A single keyword to force workflow creation — useful UX pattern for any system with an optional heavyweight mode.
- **Pairwise comparison > absolute scoring for qualitative ranking.** The sorting/tournament pattern — comparative judgment is more reliable than having the model assign scores.
- **Resumable workflows.** Interrupt → resume picks up where it left off. Essential for long-running agent tasks.
- **Token budget prompting.** "Use 10k tokens" as a prompt-level cap for workflow cost control.
- **Model routing by complexity.** A classifier agent researches the task shape (how many files, how complex) and routes to Sonnet or Opus accordingly.

## Open questions

- What does the generated JS actually look like? The article describes the primitives (spawn, coordinate, synthesize) but doesn't show a full generated workflow file. Understanding the real shape would resolve questions about harness complexity.
- How does the "save" mechanism interact with the skill distribution story? If a workflow is saved and distributed via a skill, does it become a static workflow again? Is it a starting template the model customizes?
- What's the actual token multiplier for a typical workflow vs. single-context? "Significantly more" is imprecise.
- How does the quarantine pattern compose with Claude Code's permission model? Can you structurally enforce that a subagent can't use certain tools?
