# for-builders.md — mining this wiki while you build

**Audience:** a coding agent (or person) pointed at this repo from *another* project, to extract design guidance while building a skill, plugin, MCP server, agent, or agent-shaped product.

This is the **consumer** front door. The other two: `README.md` (humans browsing), `CLAUDE.md` (the agent that *maintains* this wiki). You are neither — you're here to **mine**, then leave. This file is a routing surface only; it points at pages and never restates their content.

---

## Set expectations first (the honest scope)

This is a wiki about **how to architect agents, skills, plugins, and agent-products** — distilled from a small, opinionated set of frontier sources (Anthropic, Garry Tan's gstack/gbrain, Every's compound-engineering, OpenAI Codex). Calibrate before you rely on it:

- **High value, in-domain:** you're building something *agent-shaped* — a skill, a plugin/pack, a resolver, a self-improving loop, a multi-surface distribution, an MCP server. The patterns here are grounded, cited, and carry explicit `When NOT to use` + anti-patterns. Steal freely.
- **Limited scope outside agent products:** HumanLayer adds concrete examples of task/session data models, review UX, and execution authorization. These are source-specific examples, not a general app-architecture or security handbook.
- **Known gaps (2026-10-23):** individual skills have pages, but standalone MCP servers remain a candidate queue. The corpus is selective and several patterns still have only one verified example; watch their status and same-creator caveats. `analyses/` (cross-cutting synthesis) remains empty by design.

## The protocol (follow in order)

1. **Read `CLAUDE.md` → the `QUERY` operation.** Your task is a QUERY. The discipline there governs you.
2. **Enter through `index.md`**, then use the routing table below to jump to pages.
3. **Read *whole* pattern/artifact pages** — including each artifact's `## What we'd steal` ledger. Do **not** skim only the steal sections (the wiki's own anti-rule: a thin read narrows attention and discards ideas).
4. **Start in the wiki, not the source clones.** The analysis lives in the pages; `sources/` is evidence. Only follow a `[[sources/...#anchor]]` citation when you need to *verify* a claim before acting on it.
5. **If the cited source bodies are missing** (a fresh checkout git-ignores the repo clones), run `sources/clone-all.sh` once to rebuild them, then follow citations.
6. **If the answer isn't in the wiki, you found a gap** — note it in your output so the maintainer can file it back (`CLAUDE.md` QUERY step 2). Don't silently paper over a hole.

## Routing table — build-intent → read these first

| You're building… | Patterns / concepts to read first | Worked artifacts to study |
| --- | --- | --- |
| **A single skill** (`SKILL.md` ± thin code) | [[concepts/convergent-agent-plugin-spec]], [[patterns/quality-bar/skill-pack-bundle]], [[patterns/behavioral/skill-as-method-call]], [[patterns/behavioral/latent-vs-deterministic-split]], [[patterns/structural/thin-harness-fat-skills]] | [[artifacts/plugins/gstack]], [[artifacts/plugins/compound-engineering]], [[artifacts/plugins/openai-codex-plugins-marketplace]] |
| **A plugin / pack of many skills** | [[concepts/convergent-agent-plugin-spec]], [[patterns/structural/marketplace-as-multi-plugin]], [[patterns/composition/resolver-routing-table]], [[patterns/composition/single-source-multi-surface-distribution]], [[patterns/quality-bar/version-as-update-gate]], [[patterns/quality-bar/complexity-ratchet]] | [[artifacts/plugins/anthropic-skills-marketplace]], [[artifacts/plugins/anthropic-financial-services-marketplace]], [[artifacts/plugins/compound-engineering]], [[artifacts/plugins/gstack]], [[artifacts/plugins/gbrain]], [[artifacts/plugins/openai-codex-plugins-marketplace]] |
| **An MCP server** *(gap: no MCP page paged yet)* | [[patterns/composition/single-source-multi-surface-distribution]] | [[artifacts/plugins/gbrain]] (ships CLI + MCP + skillpack from one definition). Lean on this + the queued FSI connectors. |
| **Routing** — how the agent picks what to do | [[patterns/composition/resolver-routing-table]], [[patterns/behavioral/skill-as-method-call]] | [[artifacts/plugins/gbrain]] (`RESOLVER.md`), [[artifacts/plugins/gstack]] |
| **Reliability** — how the agent knows it's *done* | [[patterns/behavioral/evidence-gated-completion]], [[concepts/completion-contract]] | [[artifacts/projects/codex-goals]] |
| **A self-improving / compounding system** | [[patterns/quality-bar/complexity-ratchet]], [[patterns/behavioral/diarization]] | [[concepts/compound-engineering]], [[artifacts/plugins/compound-engineering]] |
| **Code-vs-prose** — what to freeze in code vs leave to the model | [[patterns/behavioral/latent-vs-deterministic-split]], [[patterns/structural/thin-harness-fat-skills]] | [[artifacts/plugins/gstack]], [[artifacts/plugins/compound-engineering]] |
| **Untrusted input / multi-agent privilege / security** *(proposed, single example — caveat)* | *(tracked as a proposed bullet)* | [[artifacts/plugins/anthropic-financial-services-marketplace]] (trust-tiered subagents: only the reader touches untrusted docs; one leaf holds Write; a critic re-verifies) |
| **Release / versioning / distribution** | [[patterns/quality-bar/version-as-update-gate]], [[patterns/composition/single-source-multi-surface-distribution]] | [[artifacts/plugins/anthropic-financial-services-marketplace]], [[artifacts/plugins/compound-engineering]] |
| **Collaborative agent work and human review** | [[concepts/agent-control-plane]], [[concepts/review-cost-aware-workflows]], [[concepts/artifact-centered-agent-context]], [[patterns/quality-bar/revision-bound-review]] | [[artifacts/projects/humanlayer]], [[artifacts/plugins/humanlayer-rpi]] |

No row fits? Run `scripts/wiki-search.sh "<your terms>"`, or browse [patterns/_index.md](patterns/_index.md). Still nothing → that's a gap; report it.

## Output contract (what to hand back to the human)

Produce a short **design brief**, not a dump:

- **3–7 stolen ideas**, each one sentence, **each citing the wiki page** it came from (`[[patterns/...]]` / `[[artifacts/...]]`). Prefer ideas with a clear `When NOT to use` so you carry the boundary, not just the technique.
- **Boundaries applied:** name which `When NOT to use` / counter-examples rule *out* an idea for this build (this is the high-value part — say what you deliberately did *not* steal and why).
- **Portability note:** for a skill/plugin, name what stays inside the shared core (`SKILL.md`, local `references/`/`scripts/`, marketplace grammar) vs. what is harness-specific (connectors, hooks, env vars, storefront metadata).
- **Out-of-domain flag:** explicitly list what the wiki did *not* cover for this task, so the human doesn't mistake silence for endorsement.
- **Gaps found:** anything you expected and the wiki lacked — flag for filing back (`CLAUDE.md` QUERY step 2).

## Copy-paste prompt (for a fresh agent in your build project)

```text
Read Research/for-builders.md, then Research/CLAUDE.md (the QUERY operation).
I'm building: <describe the skill / plugin / MCP / agent / feature>.
Use the routing table to read the relevant whole pattern + artifact pages
(including each "What we'd steal" ledger), start in the wiki not the source
clones, and follow citations only to verify before you rely on a claim.
Return a design brief per the output contract: stolen ideas (each citing a
wiki page), boundaries you applied (what you did NOT steal and why), a
portability note for shared-core vs harness-specific pieces, an out-of-domain
flag for what the wiki didn't cover, and any gaps to file back.
```
