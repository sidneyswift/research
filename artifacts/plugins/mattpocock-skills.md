---
domain: artifacts
type: plugin
name: mattpocock-skills
creator: "[[creators/matt-pocock]]"
source: "[[sources/mattpocock--skills]]"
ecosystem: cross-lab
discovered-via: other
marketplace-listing: https://skills.sh/mattpocock/skills
status: active
last-reviewed: 2026-06-19
components:
  skills: 17 in plugin.json (12 engineering + 5 productivity); ~34 across all 6 buckets on disk
  commands: 0
  agents: 0
  hooks: 0
  mcp-servers: 0
popularity-signals:
  - signal: github-stars
    value: "135,831"
    as-of: 2026-06-19
    source: "[[sources/mattpocock--skills#github-stars]]"
  - signal: github-forks
    value: "11,770"
    as-of: 2026-06-19
    source: "[[sources/mattpocock--skills#github-stars]]"
---

# mattpocock-skills

> **One-line:** Matt Pocock's daily-driver engineering skills — small, composable, model-agnostic `SKILL.md` files that fix four recurring agent failure modes (misalignment, verbosity, broken code, ball-of-mud) with classic software-engineering fundamentals instead of a process framework.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): read everything, then write distilled judgment — not a transcription of the README. Done when it passes the [page checklist](_definition-of-done.md).*

## Attributes

- **What it does**: gives a coding agent a library of *opinionated practices* — interview-before-building, build-a-shared-vocabulary, test-first, diagnose-bugs-systematically, design-deep-modules — each as a tiny markdown skill you invoke (or the model invokes) at the right moment. It's a craft toolkit, not a workflow autopilot.
- **Target user**: working software engineers using Claude Code / Codex / Cursor for *real* applications (the README's repeated foil is "vibe coding"). Skews TypeScript/web (the author's domain) but the skills are language-agnostic.
- **Component inventory** (the manifest is the canonical published set; see drift note below):
  - **Engineering (12 in `plugin.json`)** — `ask-matt` (router), `grill-with-docs`, `triage`, `improve-codebase-architecture`, `setup-matt-pocock-skills` (per-repo config), `to-issues`, `to-prd`, `prototype` *(user-invoked)*; `diagnosing-bugs`, `tdd`, `domain-modeling`, `codebase-design` *(model-invoked)*.
  - **Productivity (5)** — `grill-me`, `handoff`, `teach`, `writing-great-skills` *(user-invoked)*; `grilling` *(model-invoked — the reusable loop behind the two grill commands)*.
  - **Misc (4, in README, NOT in `plugin.json`)** — `git-guardrails-claude-code`, `migrate-to-shoehorn`, `scaffold-exercises`, `setup-pre-commit`.
  - **Unpublished buckets** — `personal/` (edit-article, obsidian-vault), `in-progress/` (5 writing/decision drafts), `deprecated/` (design-an-interface, qa, request-refactor-plan, **ubiquitous-language** — the standalone skill folded into `domain-modeling`).
- **Install footprint**: zero runtime deps. Installed by the skills.sh CLI (`npx skills@latest add mattpocock/skills`), which copies the chosen `SKILL.md` files into the agent(s) you select; no MCP servers, no env vars, no auth. `setup-matt-pocock-skills` then writes per-repo config (issue tracker, triage labels, doc layout).
- **Plugin layout**: `.claude-plugin/plugin.json` (17-skill manifest) · `skills/{engineering,productivity,misc,personal,in-progress,deprecated}/` · `docs/` (`invocation.md` + `adr/0001`) · `.out-of-scope/` (3 rejected-scope notes) · `CLAUDE.md` (bucket rules) · `CONTEXT.md` (its own glossary) · `CHANGELOG.md` + `.changeset/` · `scripts/{link-skills,list-skills}.sh`. **No test suite.**
- **License**: MIT.

## Relationships

- **Creator**: [[creators/matt-pocock]]
- **Source**: [[sources/mattpocock--skills#root]]
- **Composes**: [[artifacts/skills/grilling]] · [[artifacts/skills/writing-great-skills]] (the two deep-dived; the other ~15 are catalogued on [[sources/mattpocock--skills#README-reference]]).
- **Depends on**: the skills.sh installer (distribution) + the Agent Skills standard ([[sources/agentskills--specification]]); nothing at runtime.
- **Marketplace neighbors**: [[artifacts/plugins/gstack]] (the other individual-authored engineering pack — direct house-style contrast), [[artifacts/plugins/compound-engineering]] (shares the align-before-build move), [[artifacts/plugins/anthropic-skills-marketplace]] (the official format reference).

## What problem it solves

The whole-job-to-be-done is **"make a coding agent ship real software, not slop"** — framed as four named failure modes, each with a fix and a classic-book epigraph ([[sources/mattpocock--skills#README-why]]):

1. **"The agent didn't do what I want"** (misalignment; *Pragmatic Programmer* — "no-one knows exactly what they want") → a **grilling** session: `grill-me` / `grill-with-docs` interrogate you until aligned.
2. **"The agent is too verbose"** (no shared language; *DDD* — ubiquitous language) → build a **`CONTEXT.md`** glossary so 20 words collapse to 1 ("the materialization cascade"). Called *"the single coolest technique in this repo."*
3. **"The code doesn't work"** (no feedback loops; *Pragmatic Programmer* — "the rate of feedback is your speed limit") → static types + browser + **`tdd`** (red-green-refactor) + **`diagnosing-bugs`**.
4. **"We built a ball of mud"** (entropy accelerates with agents; Beck "invest in design every day" + Ousterhout "deep modules") → **`codebase-design`** vocabulary + **`improve-codebase-architecture`** run every few days.

It earns the right to be a *pack* (over loose skills) because `ask-matt` chains these into one **idea→ship main flow** — `grill-with-docs` → (`prototype` detour via `handoff`) → `to-prd` → `to-issues` → `implement` — i.e. a coherent workflow, not a grab-bag ([[sources/mattpocock--skills#skill-ask-matt]]).

## Composition strategy

- **Two-axis split, one router.** Every skill is typed by *invocation* (see [[concepts/skill-invocation-axis]]): **user-invoked** orchestrators (`grill-*`, `to-prd`, `ask-matt`) vs **model-invoked** reusable discipline (`grilling`, `tdd`, `domain-modeling`, `codebase-design`). The load-bearing rule: *a user-invoked skill may invoke model-invoked skills, but never another user-invoked one* — because a user-invoked skill has no `description`, nothing (no model, no other skill) can reach it but a human typing its name ([[sources/mattpocock--skills#docs-invocation]]).
- **Hand-offs are prose, not file links.** Dependencies are expressed as **`/skill`-style prose invocation** ("Run a `/grilling` session, using the `/domain-modeling` skill") rather than `../other/FILE.md` cross-references; shared reference lives inside the skill that owns it ([[sources/mattpocock--skills#skill-grill-with-docs]], [[sources/mattpocock--skills#docs-invocation]]). `grill-with-docs` is the purest example — a **one-line composite** of two other skills.
- **`ask-matt` is the cognitive-load cure.** Because user-invoked skills are unreachable by the model, *you* are the index that must remember they exist — so a single human-facing **router skill** names them and when to reach for each (a [[patterns/composition/resolver-routing-table]] with **no eval**; see that page).
- **Buckets gate distribution.** `engineering`/`productivity`/`misc` are published (README + manifest); `personal`/`in-progress`/`deprecated` are withheld — a clean promote/demote lifecycle inside one repo ([[sources/mattpocock--skills#CLAUDE.md]]).
- **No hooks, no MCP, no agents, no commands.** Pure skills. (`git-guardrails-claude-code` *sets up* Claude Code hooks in a target repo, but the plugin itself ships none.) The intelligence is 100% in editable markdown — the fat-skills end of [[patterns/structural/thin-harness-fat-skills]].

## Patterns demonstrated

- [[patterns/structural/thin-harness-fat-skills]] — **4th-creator witness, fat-skills half.** All capability is fat markdown over an interchangeable harness ("work with any model"); no deterministic substrate of its own. Reinforces the fat-skills half; says nothing new about the thin *middle*. ([[sources/mattpocock--skills#README-philosophy]])
- [[patterns/composition/resolver-routing-table]] — `ask-matt` is a 4th example (2nd non-Garry) of an **explicit routing table**, with a new sub-mechanism: a router that exists *specifically to reach user-invoked skills* the description-resolver can't see. Ships **no routing eval** → reinforces "the tested half stays Garry-only." ([[sources/mattpocock--skills#skill-ask-matt]], [[sources/mattpocock--skills#docs-invocation]])
- [[patterns/composition/single-source-multi-surface-distribution]] — **run-natively variant**: skills.sh installs the *same* `SKILL.md` files into multiple coding agents with no transform (like superpowers), enabled by the convergent standard ([[concepts/convergent-agent-plugin-spec]]).
- [[patterns/behavioral/skill-as-method-call]] — skills are invoked as parameterized `/commands`; `grill-with-docs` = `grilling` + `domain-modeling` composed by prose call.
- [[concepts/skill-invocation-axis]] — the richest in-wiki articulation of the user-vs-model invocation axis (this source *defines* the concept).
- [[concepts/ubiquitous-language-for-agents]] — `domain-modeling` + `CONTEXT.md` are the worked embodiment ("the single coolest technique").
- **Proposed (tracked, 1 strong example here): align-before-execute** — a relentless interview to close the human↔agent communication gap *before* building. Candidate 2nd examples in-wiki: CE's brainstorm/plan stage and `superpowers`' `brainstorming`. Promote when one is deep-dived. (See [[artifacts/skills/grilling]].)
- **Counter-example to [[patterns/quality-bar/skill-pack-bundle]]** — a 135K★ pack that ships **no tests**; the deliberate inverse bet ("small, easy to adapt, composable"). Logged on that page's Counter-examples.

## Source citations

- 17-skill manifest; misc absent: [[sources/mattpocock--skills#plugin.json]]
- four failure modes + book epigraphs: [[sources/mattpocock--skills#README-why]]
- "small, composable, works with any model; not vibe coding"; anti-GSD/BMAD/Spec-Kit: [[sources/mattpocock--skills#README-philosophy]]
- bucket taxonomy + promotion rule: [[sources/mattpocock--skills#CLAUDE.md]]
- user/model invocation + prose `/skill` invocation: [[sources/mattpocock--skills#docs-invocation]]
- the idea→ship main flow + smart-zone hygiene: [[sources/mattpocock--skills#skill-ask-matt]]
- `grill-with-docs` one-line composite: [[sources/mattpocock--skills#skill-grill-with-docs]]
- 135,831★ / 11,770 forks, as-of 2026-06-19: [[sources/mattpocock--skills#github-stars]]

## What makes it great

- **It diagnoses, then prescribes.** The README is structured as *failure mode → fix*, each anchored to a named book — so the pack reads like applied engineering literature, not prompt-craft. That framing is why the skills feel principled rather than ad-hoc.
- **Radical smallness.** `grilling` is three sentences; `grill-with-docs` is one line. The lazy alternative is a 300-line mega-skill; Pocock instead leans on **leading words** ("relentless," "grill") and composition, banking on predictability over verbosity ([[artifacts/skills/writing-great-skills]]).
- **The invocation axis is a real design tool**, not a footnote — it lets him pay *zero* context load for orchestrators and reserve the always-loaded `description` budget for skills the model must reach on its own. Most packs never make this trade consciously.
- **Honest lifecycle.** `in-progress/`, `personal/`, `deprecated/`, and an `.out-of-scope/` registry mean the repo openly tracks what's *not* ready and what was *rejected* — a maturity most skill packs lack.

## What we'd steal

**Exhaustive ledger — ★ = highest-value.**

- ★ **The four-failure-mode framing** as a way to *teach* a skill pack: name the failure, quote the canon, ship the fix. A great structure for any of our own skill READMEs ([[sources/mattpocock--skills#README-why]]).
- ★ **The user-invoked vs model-invoked axis + the two-load trade-off** (context load vs cognitive load) — a concrete lever this wiki's own machinery could adopt (see REFLECT / [[concepts/skill-invocation-axis]]).
- ★ **`CONTEXT.md` as a ubiquitous-language doc for the agent** — collapse jargon to single terms; fewer tokens, consistent naming, easier navigation ([[concepts/ubiquitous-language-for-agents]]).
- ★ **The `writing-great-skills` vocabulary** — predictability, the information-hierarchy ladder, leading words, premature completion, sediment/sprawl/no-op pruning. The most directly portable artifact in the repo *for us* ([[artifacts/skills/writing-great-skills]]).
- ★ **Prose `/skill` invocation over file cross-refs** — skills reference each other by *invoking the command*, never by deep-linking another skill's files; keeps each skill's reference co-located and the dependency a behavior, not a path ([[sources/mattpocock--skills#docs-invocation]]).
- **The one-line composite skill** (`grill-with-docs` = `/grilling` + `/domain-modeling`) — composition as a first-class authoring move.
- **A human-facing router** (`ask-matt`) for the skills the model can't reach — the cognitive-load cure when user-invoked skills multiply.
- **Bucket lifecycle** (`in-progress`/`personal`/`deprecated`) + a manifest/README promotion rule for what's published vs withheld.
- **An `.out-of-scope/` registry** — explicitly recording *rejected* scope so it isn't relitigated (cf. our "Rejected framings" sections).
- **`docs/adr/`** with a tight three-test gate for *when* to write an ADR (hard-to-reverse ∧ surprising ∧ a real trade-off) ([[sources/mattpocock--skills#skill-domain-modeling]]).
- **The "smart zone" budget** (~120k tokens) as the explicit reason to `handoff` to a fresh session rather than push on a degraded window ([[sources/mattpocock--skills#skill-ask-matt]]).
- **Deep-module vocabulary** (Module/Interface/Depth/Seam/Adapter/Leverage/Locality + the deletion test + "one adapter = hypothetical seam, two = real") as a shared language for restructuring code for AI-navigability ([[sources/mattpocock--skills#skill-codebase-design]]).
- *(minor)* `changeset`-driven releases for a skills repo; `link-skills.sh`/`list-skills.sh` as the only scripts.

## Open questions / what's unclear

- **Manifest/README/tree drift (flag for LINT).** `plugin.json` lists **17** skills; the README "Reference" lists **21** (12 engineering + 5 productivity + 4 misc); the `engineering/` directory additionally contains `implement/` and `resolving-merge-conflicts/` that appear in **neither**. The repo's own `CLAUDE.md` rule says every engineering/productivity/misc skill must be in both README *and* `plugin.json` — so the **4 misc skills (missing from the manifest)** and the **2 unlisted engineering skills** are real inconsistencies (the same class of finding as CE's 43-vs-51 agents and pm-os's 235-vs-237). Verified by reading `plugin.json`, the README, and `ls skills/*/`.
- **Does it ship *any* verification?** No tests, no routing eval. Is correctness enforced anywhere, or is the bet entirely "small enough to eyeball + predictable by construction"? (This is the crux of the [[patterns/quality-bar/skill-pack-bundle]] counter-example.)
- **How much is the 135K★ the skills vs the author's audience?** Star velocity likely rides Total TypeScript / AI Hero reach; worth separating "great artifact" from "great distribution" before over-indexing on the pattern evidence.
- **Several high-value skills un-deep-dived**: `codebase-design`, `domain-modeling`, `tdd`, `diagnosing-bugs`, `improve-codebase-architecture`, `setup-matt-pocock-skills` — queued in [[artifacts/skills/_index]].
