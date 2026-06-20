---
domain: concepts
type: concept
name: ubiquitous-language-for-agents
creators: "[[creators/matt-pocock]]"
sources: "[[sources/mattpocock--skills]]"
status: emerging
last-reviewed: 2026-06-19
popularity-signals:
  - signal: quoted-by
    value: author calls it "the single coolest technique in this repo"
    as-of: 2026-06-19
    source: "[[sources/mattpocock--skills#README-why]]"
---

# ubiquitous-language-for-agents

> **One-line:** Maintain a small, precise project glossary (`CONTEXT.md`) *for the coding agent* — the same "ubiquitous language" DDD prescribes for human teams — so jargon collapses to single canonical terms, naming stays consistent, and the agent spends fewer tokens decoding the domain.

*Judgment distillation ([[patterns/behavioral/diarization]]): compiled truth on top + append-only `## Timeline`. Done when it passes the [page checklist](_definition-of-done.md).*

## What it is

The agent version of Eric Evans's **ubiquitous language**: a single shared vocabulary, written down, that everyone — and now the *agent* — uses in conversation, docs, and code. Pocock's framing: agents are "dropped into a project and asked to figure out the jargon as they go. So they use 20 words where 1 will do." The fix is a **`CONTEXT.md`** glossary the agent reads and helps maintain, turning "there's a problem when a lesson inside a section of a course is made 'real' (given a spot in the file system)" into "there's a problem with the **materialization cascade**" ([[sources/mattpocock--skills#README-why]]). The doc is *only* a glossary — "totally devoid of implementation details … not a spec, a scratch pad, or a repository for implementation decisions" — with **ADRs** (architecture decision records) as the separate home for decisions ([[sources/mattpocock--skills#skill-domain-modeling]]).

It is **actively built, not passively read.** Merely consulting `CONTEXT.md` for vocabulary is a one-line habit any skill can do; the *discipline* of challenging terms, inventing edge-case scenarios, cross-checking against code, and writing the glossary inline is the `domain-modeling` skill ([[sources/mattpocock--skills#docs-invocation]], [[sources/mattpocock--skills#skill-domain-modeling]]).

## Where it came from

**Ubiquitous language** is Eric Evans's, from *Domain-Driven Design* (2003): *"conversations among developers and expressions of the code are all derived from the same domain model."* Pocock's contribution is **porting it to the human↔agent gap** — treating the agent as the new team member who doesn't speak the domain — and operationalizing it as two skills (`domain-modeling`, and `grill-with-docs` = `grilling` + `domain-modeling`) plus a file convention (`CONTEXT.md` + `docs/adr/`) ([[sources/mattpocock--skills#README-why]], [[sources/mattpocock--skills#skill-grill-with-docs]]). Notably, a standalone `ubiquitous-language` skill once existed but is now in the repo's `deprecated/` bucket — the *technique* graduated into `domain-modeling`, the *skill* was retired ([[sources/mattpocock--skills#buckets]]).

## Why it matters

Pocock claims it "might be the single coolest technique in this repo," and the payoff is concrete and compounding ([[sources/mattpocock--skills#README-why]]):

- **Fewer tokens on thinking** — the agent reasons in compact canonical terms instead of re-deriving long descriptions each turn.
- **Consistent naming** — variables, functions, and files inherit the glossary, so the codebase is more navigable *for the agent*.
- **Less verbosity** — the #2 failure mode ("the agent is way too verbose") is addressed at the root, not patched per-response.

This is the same "concision pays off session after session" logic that motivates [[patterns/structural/thin-harness-fat-skills|loading capability on demand]] — a small persistent artifact that lifts every future session's floor.

## Evidence & claims

- *"This concision pays off session after session"* and the materialization-cascade before/after — **demonstrated** with a real repo example (`course-video-manager`) — citation: [[sources/mattpocock--skills#README-why]]
- *"`CONTEXT.md` should be totally devoid of implementation details … It is a glossary and nothing else"* — **asserted** discipline — citation: [[sources/mattpocock--skills#skill-domain-modeling]]
- *Offer an ADR only when all three hold: hard-to-reverse ∧ surprising-without-context ∧ the result of a real trade-off* — **asserted** rule — citation: [[sources/mattpocock--skills#skill-domain-modeling]]
- The repo dogfoods it: its own `CONTEXT.md` defines Issue tracker / Issue / Triage role and flags resolved ambiguities ("backlog" split into tool vs work) — **demonstrated** — citation: [[sources/mattpocock--skills#CONTEXT.md]]

## Patterns demonstrated

- [[patterns/behavioral/diarization]] — `CONTEXT.md` is **compiled truth**: read the messy domain talk, write one structured, edited-in-place glossary (the brain-page move applied to vocabulary rather than entities).
- *(candidate, 1 example)* a "shared-vocabulary doc the agent maintains" technique — promote to a `patterns/` page if a 2nd artifact ships the same `CONTEXT.md`-as-glossary convention (gbrain's `_brain-filing-rules`/glossary habits are a candidate to compare).

## Tensions & counter-arguments

- **Glossary purity vs practicality.** "Glossary and nothing else" is clean but fights the gravity of teams that want one doc for everything; the discipline only holds if something (a skill, a review) enforces the separation from ADRs/specs.
- **Up-front cost.** Building a domain model via a grilling interview spends tokens and user time before any code — worth it for long-lived repos, overhead for throwaways (the same scope boundary as [[artifacts/skills/grilling]]).
- **Staleness risk.** A glossary that drifts from the code actively *mis*-leads the agent; `domain-modeling`'s "cross-reference with code, surface contradictions" move is the counter, but nothing tests it.

## Timeline (append-only)

- 2003 — Eric Evans coins **ubiquitous language** in *Domain-Driven Design*.
- 2026-06-19 — ingested here as the agent-facing application: `CONTEXT.md` + `domain-modeling`/`grill-with-docs`; the standalone `ubiquitous-language` skill found in the repo's `deprecated/` bucket (technique folded into `domain-modeling`) ([[sources/mattpocock--skills#README-why]], [[sources/mattpocock--skills#buckets]]).

## Related

- [[concepts/skill-invocation-axis]] — sibling idea from the same source (how skills are reached vs how the domain is named).
- [[artifacts/skills/grilling]] — `grill-with-docs` runs a grilling session *plus* `domain-modeling`, building the glossary as it interrogates.
- [[artifacts/plugins/mattpocock-skills]] — the pack this lives in; fix for failure mode #2 (verbosity).
- [[patterns/structural/thin-harness-fat-skills]] — a small persistent doc loaded on demand, not crammed into the prompt.

## What we'd steal

- ★ **Keep a `CONTEXT.md` glossary for the workspace the agent operates in.** Directly applicable to *this* consulting-OS and to this wiki — collapse house jargon (deal stages, "skillify," "ratchet," operation names) to canonical terms so every session reasons in the same compact vocabulary.
- ★ **Collapse jargon to a single leading word** — the "materialization cascade" move is exactly the [[artifacts/skills/writing-great-skills|leading-word]] technique applied to the *domain* instead of the *skill*. Same lever, two altitudes.
- ★ **"Glossary and nothing else"** — separate the *vocabulary* doc from the *decisions* doc (ADRs) and the *spec*; don't let one file become all three.
- **The ADR three-test gate** (hard-to-reverse ∧ surprising ∧ real trade-off) — a crisp filter for *when* a decision is worth recording, portable to our `knowledge/`/decision logs.
- **Active-maintenance moves**: challenge a term against the glossary, sharpen fuzzy/overloaded terms ("account = Customer or User?"), stress-test with edge-case scenarios, cross-reference against code and surface contradictions ([[sources/mattpocock--skills#skill-domain-modeling]]).
- **Create files lazily** — write `CONTEXT.md`/`docs/adr/` only when the first term/decision crystallizes, not as empty scaffolding.

## Open questions

- Does a second creator ship the same agent-maintained-glossary convention (promotes the candidate pattern)? Compare gbrain's filing-rules/glossary and any `CONTEXT.md`-style files in CE/pm-os.
- How is the glossary kept honest against the code over time without a test — is the "cross-reference with code" move enough, or does it need a `(det)` check?
- Where's the boundary between this and a full domain model / `CONTEXT-MAP.md` for multi-context repos ([[sources/mattpocock--skills#skill-domain-modeling]])?
