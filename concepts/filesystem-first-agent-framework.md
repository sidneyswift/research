---
domain: concepts
type: concept
name: filesystem-first-agent-framework
creators: ["[[creators/vercel]]"]
sources: ["[[sources/vercel--eve]]"]
status: emerging
last-reviewed: 2026-06-20
popularity-signals:
  - signal: adoption
    value: "eve (vercel/eve) 1,671★ four days after public preview; positioned as 'Next.js for agents'"
    as-of: 2026-06-20
    source: "[[sources/vercel--eve#github-stars]]"
---

# filesystem-first-agent-framework

> **One-line:** Build an agent the way Rails/Next.js build a web app — **convention over configuration**: an agent *is* a directory, each capability is a file in a known slot, identity is derived from the path, and the framework *discovers* the tree instead of reading a central registry or one big config object.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): compiled truth on top + an append-only `## Timeline`.*

## What it is

A framework design where the **filesystem is the authoring interface**: "instead of one large configuration object, each part of your agent gets a clear home. Instructions go in one file, tools in one folder, channels in another," and the framework "discovers that structure and turns it into an agent" ([[sources/vercel--eve#docs-introduction]]). Three rules define it: (1) **a file's location declares what it is** — a file under `tools/` is a tool, under `channels/` a channel; (2) **identity comes from the path** — "you never write a `name` or `id` field on a `define*` call"; `agent/tools/get_weather.ts` is the tool `get_weather` ([[sources/vercel--eve#docs-project-layout]]); (3) **there is no registry to keep in sync** — "add the file and eve discovers it; move or rename it and its identity moves with it" ([[sources/vercel--eve#docs-introduction]]). It is the agent-domain port of the *convention-over-configuration* idea that made Rails' `app/models` and Next.js' `pages/` legible: the directory tells you what the thing can do before it runs.

## Where it came from

The pattern is old (Rails 2004, Next.js file-based routing) but its application to **agents** is new. [[creators/vercel]]'s **eve** (public preview 2026-06-17) is the purest in-wiki instance and the source of the framing — Vercel explicitly markets it as "Next.js for agents" and titles a README section "The filesystem is the authoring interface" ([[sources/vercel--eve#README]], [[sources/vercel--eve#docs-introduction]]). There is partial lineage in the skill world: the **Agent Skills** standard and packs like `anthropic/skills` / `mattpocock/skills` already take a skill's identity from its *directory name* — but those are single-capability conventions, not a whole-agent framework where tools, channels, connections, subagents, schedules, hooks, and sandboxes are *all* path-derived slots. eve generalizes "directory = skill" into "directory = agent."

## Why it matters

It changes the unit of review from "read the config" to "read the tree." Because every capability is a file in a fixed slot with a path-derived name, **the agent is legible before it runs** ("the result stays readable before it runs. The directory tells you what the agent can do" — [[sources/vercel--eve#docs-introduction]]), an agent can grow without a config file becoming a bottleneck (add a folder when you need it), and a whole class of bug disappears: **registry drift** (the name in the manifest disagreeing with the thing) cannot happen when there is no separate registry. It also makes agents *diffable* and *AI-navigable* — a coding agent can reason about "what does this agent do" from `ls` + the slot table, the same way it reasons about a Next.js app. The cost is the inverse: behavior becomes implicit in structure, so the conventions must be learned and discovery failures need a debugging story (eve's answer is `eve info` + `.eve/` diagnostics — [[sources/vercel--eve#docs-cli]]).

## Evidence & claims

- *"A file's location says what it does, and its path usually gives it a name."* — demonstrated (the slot table + naming rule) — [[sources/vercel--eve#docs-project-layout]]
- *"There is no separate registry to keep in sync."* — demonstrated — [[sources/vercel--eve#docs-introduction]]
- *"You never write a `name` or `id` field on a `define*` call."* — demonstrated (path-derived identity across tools/connections/skills/subagents/channels/schedules/hooks) — [[sources/vercel--eve#docs-project-layout]]
- *"Start with only `instructions.md` and `agent.ts`. Add the other folders when the agent needs them."* — asserted as the growth model (flat → nested layout) — [[sources/vercel--eve#docs-introduction]], [[sources/vercel--eve#docs-project-layout]]
- The framework has real `discover/` and `compiler/` modules that walk the tree into a manifest — demonstrated (repo source) — [[sources/vercel--eve#packages-src]]

## Patterns demonstrated

- [[patterns/structural/thin-harness-fat-skills]] — filesystem-first is *how* eve organizes the three layers: fat skills in `skills/`, thin tools in `tools/`, the harness owned by the framework. The directory layout is the architecture made physical. Citation: [[sources/vercel--eve#docs-project-layout]].
- *Candidate pattern (1 example so far, tracked here for a future 2nd):* **path-derived identity / convention-over-configuration discovery** — capability declared by file location, name derived from path, no registry. eve is the clean instance; the Agent Skills "directory = skill name" convention is a partial second. Promote to a `patterns/` page when a second whole-framework example lands.

## Tensions & counter-arguments

- **Implicit-over-explicit has real costs.** Convention-over-configuration trades a readable config for *learned* conventions; a newcomer must know the slot table to know what `agent/hooks/auth/load-profile.ts` does, and a misplaced file silently does nothing until `eve info` is run ([[sources/vercel--eve#docs-project-layout]]). The competing school (explicit registries / one config object) makes the wiring greppable in one place.
- **Magic discovery vs. debuggability.** "Add the file and eve discovers it" is great until it *doesn't* discover it; the framework needs a strong diagnostic story (eve ships `eve info` + `.eve/discovery/diagnostics.json`) precisely because the magic can fail opaquely ([[sources/vercel--eve#docs-cli]]).
- **n=1 as a *framework*.** The idea is well-established for web frameworks and for single skills, but eve is the only whole-agent framework instance in the wiki — so "filesystem-first agents" is `emerging`, not a confirmed cross-artifact pattern. The danger is mistaking one well-marketed framework's house style for an inevitability.
- **Not all agent state wants to be a file.** Durable session state, secrets, and runtime config legitimately live elsewhere (env, the workflow store); filesystem-first is about the *authored surface*, and over-applying it ("everything is a file") would be the inverse error.

## Timeline (append-only)

- 2026-06-17 — Vercel ships **eve** in public preview, the first whole-agent framework built on the filesystem-first principle ("Next.js for agents") ([[sources/vercel--eve#README]]).
- 2026-06-20 — Ingested into the wiki as the grounding source for this concept ([[sources/vercel--eve]]).

## Related

- [[concepts/durable-agent-execution]] — the *other* half of eve's design; filesystem-first is how you *author*, durable execution is how it *runs*.
- [[patterns/structural/thin-harness-fat-skills]] — the architecture this layout physically expresses.
- [[concepts/convergent-agent-plugin-spec]] — a *different* axis: that's about the plugin/skill packaging grammar converging across labs; this is about a framework deriving everything from the tree. (Agent Skills' "directory = skill" is where they touch.)
- [[artifacts/projects/eve]] — the embodying artifact.

## What we'd steal

**Exhaustive ledger** (★ = highest-value, clearly portable):

- ★ **Derive identity from the path; ban redundant `name`/`id` fields.** The single most portable rule — it kills registry drift and makes rename = re-identify. (We apply a weaker version: `index.md` is our registry; the stronger move is making it unnecessary.) ([[sources/vercel--eve#docs-project-layout]])
- ★ **A small, total slot table with per-slot "add it when…" triggers.** Each directory has one job and one reason to exist; the table *is* the mental model. ([[sources/vercel--eve#docs-project-layout]])
- ★ **Legible-before-it-runs as a design goal.** Optimize the authored surface so `ls` + the conventions tell you what the system does — especially valuable when the reader is a coding agent. ([[sources/vercel--eve#docs-introduction]])
- **A flat→nested growth path.** Start with two files; promote to directories only when a concern needs more than one. Avoids premature structure. ([[sources/vercel--eve#docs-project-layout]])
- **Pair magic discovery with a discovery doctor.** If location-implies-behavior, ship the `info`/diagnostics command that explains why a file *wasn't* picked up. ([[sources/vercel--eve#docs-cli]])
- **Build-time failure on ambiguity.** A subagent that collides with a tool name "rejects the build rather than picking a winner"; an unknown disable-slug fails rather than no-op'ing. Convention systems should fail loud on conflict. ([[sources/vercel--eve#docs-subagents]], [[sources/vercel--eve#docs-default-harness]])

## Open questions

- **Does a *second* whole-agent framework adopt filesystem-first?** That's the promotion gate from `emerging` concept to confirmed pattern. Candidates: other harnesses (Mastra, LangGraph, Claude Code's own project layout) — do any derive identity from the tree the way eve does?
- **Where's the line between "a file" and "config"?** eve keeps runtime config in `agent.ts` and durable state in the workflow store, not files. What *shouldn't* be a slot? A crisp rule would sharpen the concept.
- **Does convention-over-configuration survive multi-tenant / dynamic agents?** eve's answer is `defineDynamic` (resolve capabilities per caller at runtime) layered *on top of* the static tree ([[sources/vercel--eve#docs-dynamic-capabilities]]) — does the filesystem-first legibility hold when much of the real capability set is computed per session?
