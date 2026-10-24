---
domain: concepts
type: concept
name: skill-invocation-axis
creators: "[[creators/matt-pocock]]"
sources: "[[sources/mattpocock--skills]]"
status: emerging
last-reviewed: 2026-06-19
popularity-signals:
  - signal: github-stars
    value: "articulated in mattpocock/skills (135,831★ as-of 2026-06-19)"
    as-of: 2026-06-19
    source: "[[sources/mattpocock--skills#github-stars]]"
---

# skill-invocation-axis

> **One-line:** Every skill splits on one axis — *who can invoke it.* **Model-invoked** skills keep a `description` (model or user or another skill can fire them) and cost **context load**; **user-invoked** skills (`disable-model-invocation: true`) are reachable only by a human typing their name and cost **cognitive load** instead. Choosing the right side per skill is a deliberate context-budget lever.

*Judgment distillation ([[patterns/behavioral/diarization]]): compiled truth on top + append-only `## Timeline`. Done when it passes the [page checklist](_definition-of-done.md).*

## What it is

Pocock reduces all skill taxonomy to a single distinction — invocation — and attaches a precise cost to each side ([[sources/mattpocock--skills#skill-writing-great-skills]], [[sources/mattpocock--skills#docs-invocation]]):

- **Model-invoked** (default; omit `disable-model-invocation`): the `description` field stays in the model's reach, so the agent can fire the skill autonomously *and* other skills can reach it. Price: **context load** — that description sits in the window every turn. Write it model-facing, with rich trigger phrasing ("Use when the user wants…, mentions…").
- **User-invoked** (`disable-model-invocation: true`): the description is stripped from the agent's reach; *only* the human, typing the name, can invoke it — and **no other skill can**. Price: **cognitive load** — *you* are the index that must remember it exists. The description becomes a human-facing one-liner.

Two rules fall out. **The choosing test:** pick model-invocation only when the agent must reach the skill on its own, or another skill must — *"Reuse is the reason to extract a skill, not the test"* for invocation ([[sources/mattpocock--skills#docs-invocation]]). **The composition rule:** because a user-invoked skill has no description, nothing but a human can fire it — so *a user-invoked skill may invoke model-invoked skills, but never another user-invoked one.* And the cure for too many user-invoked skills (piled-up cognitive load) is a **router skill**: one user-invoked skill that names the others and when to reach for each ([[sources/mattpocock--skills#skill-writing-great-skills]]).

## Where it came from

The *mechanism* — model auto-invocation keyed off the `description` field — is part of the Agent Skills standard and Claude Code's native resolver ([[sources/agentskills--specification]], and "the description **is** the resolver," [[patterns/composition/resolver-routing-table]]). Pocock's contribution is the **explicit axis + the two-load economic framing + the composition rule + the router cure**, written down as authoring doctrine in `writing-great-skills` and `docs/invocation.md` ([[sources/mattpocock--skills#skill-writing-great-skills]], [[sources/mattpocock--skills#docs-invocation]]). It's `emerging`: one source articulates it sharply; the underlying mechanism is multi-source.

## Why it matters

It turns "should this be a skill?" into two separate, cheaper questions: *does it need its own trigger?* and *who needs to reach it?* — and makes the **context budget explicit**. You pay the always-loaded `description` cost *only* for skills the model must reach autonomously; everything human-only is free to store (zero context load) and reached through a router. That's the same "attention is the scarce resource" logic behind [[patterns/structural/thin-harness-fat-skills]], applied at the per-skill granularity. It also predicts a real failure: a user-invoked skill you forget is a **dead skill** — the human-side version of the resolver essay's "invisible skill" ([[patterns/composition/resolver-routing-table]]).

## Evidence & claims

- *Model-invoked = context load; user-invoked = cognitive load; pick model-invocation only when the agent or another skill must reach it* — **asserted** doctrine — citation: [[sources/mattpocock--skills#skill-writing-great-skills]]
- *A user-invoked skill may invoke model-invoked skills but never another user-invoked one* — **asserted**, with the mechanism (no description ⇒ unreachable) — citation: [[sources/mattpocock--skills#docs-invocation]]
- *Reuse is not the test for invocation; autonomy-of-reach is* — **asserted** — citation: [[sources/mattpocock--skills#docs-invocation]]
- **Demonstrated** in the pack: orchestrators (`grill-me`, `grill-with-docs`, `to-prd`, `ask-matt`, `writing-great-skills`) are user-invoked; reusable discipline (`grilling`, `tdd`, `domain-modeling`, `codebase-design`) is model-invoked; `ask-matt` is the router — citation: [[sources/mattpocock--skills#README-reference]]

## Patterns demonstrated

- [[patterns/composition/resolver-routing-table]] — the **router skill** that cures piled cognitive load is a human-facing resolver; `ask-matt` is the worked example. This concept explains *why* user-invoked skills need a router at all (the description-resolver can't see them).
- [[patterns/structural/thin-harness-fat-skills]] — the two-load model is context-budget discipline: don't pay always-loaded description cost unless the model must auto-reach the skill.
- [[patterns/behavioral/skill-as-method-call]] — invocation is *how the method is called*; this axis says which callers are even allowed.

## Tensions & counter-arguments

- **Cognitive load is unmeasured and real.** "You'll remember it" is exactly what fails as a pack grows — which is why the router exists, but a router is itself a user-invoked skill you must remember. There's a regress the pattern only partly escapes.
- **Foresight assumption.** The choosing test ("will the model need to reach it?") demands you predict autonomy needs up front; misjudge it and you either pay context load for nothing or strand a skill the model should have been able to fire.
- **Portability gap.** "User-invoked / model-invoked" is Claude-Code-flavored frontmatter (`disable-model-invocation`); how it maps onto Codex/Cursor slash-commands-without-descriptions is unspecified, and discovery paths differ ([[concepts/workspace-skill-distribution]], [[concepts/convergent-agent-plugin-spec]]).

## Timeline (append-only)

- 2026-06-19 — ingested from `mattpocock/skills` (`writing-great-skills` + `docs/invocation.md`): the explicit axis, the context-load vs cognitive-load trade-off, the "never call another user-invoked skill" rule, and the router cure ([[sources/mattpocock--skills#skill-writing-great-skills]], [[sources/mattpocock--skills#docs-invocation]]).

## Related

- [[concepts/ubiquitous-language-for-agents]] — sibling idea from the same source (how skills are *reached* vs how the domain is *named*).
- [[artifacts/skills/writing-great-skills]] — the artifact that defines this axis.
- [[patterns/composition/resolver-routing-table]] — the router/resolver layer this concept hands work to.
- [[concepts/convergent-agent-plugin-spec]] — the `description`-as-trigger mechanism is part of the convergent standard the axis sits on top of.

## What we'd steal

- ★ **Classify every skill (and every wiki operation) by invocation**, and pay always-loaded `description` cost *only* where the model must auto-reach it — a concrete context-budget rule for our own skills and for what this wiki's `CLAUDE.md` advertises as auto-loadable vs router-reached.
- ★ **"Reuse is not the test; autonomy-of-reach is."** Stops the reflex of making everything model-invoked "just in case," which silently bloats the context window.
- ★ **The router-as-cognitive-load-cure.** Our `index.md` / `for-builders.md` already function as human-facing routers over otherwise-unreachable pages — name that role explicitly and keep it current (the dead-skill failure mode is the same as a stale front door).
- **The composition rule** (orchestrators can't chain orchestrators) — a clean constraint to honor when designing skill→skill hand-offs: push shared logic *down* into a model-invoked skill both orchestrators can call.
- **Human-facing vs model-facing descriptions** — write the `description` for its actual reader (a person browsing commands vs the model's trigger matcher), not one generic blurb.

## Open questions

- Does a second creator articulate (not just use) the two-load axis? Many packs *have* user/model commands; few *frame* the trade-off — find the 2nd to consider promoting this toward a pattern.
- What's the cross-harness mapping of `disable-model-invocation` (Codex/Cursor/Copilot)? Needed before the axis is portable advice.
- Is there a measurable context-load number per description (tokens/turn) that would let the trade-off be computed rather than judged?
