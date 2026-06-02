---
domain: creators
type: org
name: Every
handle: everyinc
url: https://every.to
last-reviewed: 2026-06-02
---

# Every

> A media-and-software company that both *writes about* and *builds with* AI agents.
> Home and origin of **compound engineering** — the methodology that each unit of
> engineering work should make the next one easier. The concept and the official plugin
> are **Kieran Klaassen's** (GM of Cora at Every); **Dan Shipper** (co-founder & CEO)
> amplifies it editorially. When Every ships an essay *and* the runnable plugin behind
> it, the agent-coding community treats the pair as a reference workflow.

## Attributes

- **What they ship**:
  - **Writing** at [every.to](https://every.to) — confirmed columns include *Chain of
    Thought* (Dan Shipper; e.g. ["Compound engineering: how Every codes with
    agents"](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents))
    and *Source Code* (engineering; the origin essay ["My AI Had Already Fixed the Code
    Before I Saw It"](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it),
    which is the plugin's `homepage`). Plus the living [[sources/every--compound-engineering]]
    guide and dated essays like [[sources/every--compound-engineering-gets-an-upgrade]].
  - **Software** — AI products built in-house, including **Cora** (an AI email product;
    Kieran Klaassen is its GM). *(Other Every products exist but are not yet cataloged here
    — not fabricating a list.)*
  - **Open-source tooling** — [[artifacts/plugins/compound-engineering]], the official
    Compound Engineering plugin (`@every-env/compound-plugin`), shipped to ~11 agent
    platforms.
- **Distribution channels**: every.to (essays + guides + newsletter), github.com/EveryInc,
  npm (`@every-env/*`), and the Claude Code / Codex / Cursor plugin marketplaces.
- **Position in ecosystem**: a **media company that builds** — narrative and tooling in one
  loop. It documents a methodology in prose *and* ships the agent that runs it, then writes
  about what changed. Closest in-wiki analog to [[creators/garry-tan]] (an opinionated
  builder publishing both essays and the repos they describe), but org-shaped: multiple
  named authors under one brand.

## Key people

- **Kieran Klaassen** ([github.com/kieranklaassen](https://github.com/kieranklaassen),
  `kieran@every.to`) — **GM of Cora at Every**; originator of compound engineering and
  **owner/author of the plugin** ([[sources/every--compound-engineering-plugin#marketplace.json]],
  `#plugin.json`). Author of [[sources/every--compound-engineering-gets-an-upgrade]] and the
  origin "Source Code" essay. Solo-auteur posture: *"I do not accept outside contributions…
  it's my name on the thing… I'll have Claude or Codex review submissions via `gh` and
  independently decide"* ([[sources/every--compound-engineering-plugin#no-contributions]]).
- **Dan Shipper** — co-founder & CEO of Every; writes *Chain of Thought*; the editorial
  amplifier who frames compound engineering as "how Every codes with agents."
- **Nityesh Agarwal** — author of the second plugin in the marketplace, `coding-tutor`
  ([[sources/every--compound-engineering-plugin#coding-tutor]]).

## Artifacts produced

### Plugins
- [[artifacts/plugins/compound-engineering]] — the official Compound Engineering plugin: 38
  skills + 43 sub-agents, authored once in Claude format and converted to ~11 agent
  platforms; dogfoods its own loop. (Marketplace also ships `coding-tutor` by Nityesh
  Agarwal.)

### Concepts
- [[concepts/compound-engineering]] — the methodology: each unit of work makes the next
  easier; 80/20 planning-vs-execution; "taste belongs in systems, not review."

### Public framing (essays/guides)
- [[sources/every--compound-engineering]] — the living guide (loop, 50/50 rule, beliefs to
  unlearn, adoption ladder).
- [[sources/every--compound-engineering-gets-an-upgrade]] — Kieran's 2026-05-29 essay on the
  4-step → 8-step evolution ("AI is the stuff in the middle; humans are the bread").
- *Not yet ingested (candidates)*: "Compound engineering: how Every codes with agents"
  (Chain of Thought, Dan Shipper) and "My AI Had Already Fixed the Code Before I Saw It"
  (Source Code, the origin essay / plugin homepage).

## Design philosophy (discernible from artifacts)

- **Forward-only / compounding.** The whole thesis: "each unit of engineering work should
  make subsequent units easier — not harder" ([[sources/every--compound-engineering#thesis]]).
  Operationalized as a documented-solutions store (`docs/solutions/`) that `/ce-compound`
  writes to so the next agent doesn't re-learn a lesson. → [[patterns/quality-bar/complexity-ratchet]].
- **80/20, judgment at the ends.** ~80% planning+review, ~20% execution; as models improve,
  human judgment migrates to the *ends* of the loop (ideate/brainstorm + polish), not away —
  "AI is the stuff in the middle" ([[sources/every--compound-engineering-gets-an-upgrade#sandwich]]).
- **Taste belongs in systems, not review.** Bake judgment into configuration, schemas, and
  automated checks rather than re-applying it manually each pass
  ([[sources/every--compound-engineering#taste-in-systems]]).
- **Write once, convert to every harness.** One Claude-format plugin → Codex/Cursor/Copilot/
  Gemini/Kiro/OpenCode/Pi via a TypeScript converter; portability is a first-class design
  constraint on how skills are authored ([[sources/every--compound-engineering-plugin#converter]],
  `#cross-platform-authoring`). → [[patterns/composition/single-source-multi-surface-distribution]].
- **`AGENTS.md` is canonical; `CLAUDE.md` is a shim.** The agent-facing doc is the source of
  truth; the harness-specific file is a 1-line `@AGENTS.md` redirect
  ([[sources/every--compound-engineering-plugin#CLAUDE.md-shim]]).
- **Skills are guardrails for an intelligent agent, not a controller for a dumb one.**
  Calibrate prescription to the failure mode — hard rules for deterministic safety, trust for
  judgment ([[sources/every--compound-engineering-plugin#plugin-AGENTS.md]]). → a non-Garry
  statement of [[patterns/behavioral/latent-vs-deterministic-split]].
- **Tested prose, enforced by CI.** ~1,094 test cases incl. behavioral contract tests; branch
  protection blocks merges below the floor ([[sources/every--compound-engineering-plugin#tests]],
  `#release-automation`). → [[patterns/quality-bar/skill-pack-bundle]].
- **Solo-auteur, high-velocity.** No outside contributions merged; the author + agents own the
  whole surface — the same velocity-over-collaboration stance as [[creators/garry-tan]]
  ([[sources/every--compound-engineering-plugin#no-contributions]]).
- **Dogfooding as proof.** The plugin is built using the plugin — `docs/brainstorms/` (27),
  `docs/plans/` (57), and `docs/solutions/` (30) are the loop's own audit trail
  ([[sources/every--compound-engineering-plugin#docs-solutions]]).

## Source citations

- [[sources/every--compound-engineering-plugin#marketplace.json]] / `#plugin.json` — ownership
  (Kieran Klaassen, `kieran@every.to`), MIT, two-plugin marketplace.
- [[sources/every--compound-engineering-plugin#no-contributions]] — the solo-auteur posture.
- [[sources/every--compound-engineering]] — the methodology guide.
- [[sources/every--compound-engineering-gets-an-upgrade]] — Kieran's role (GM of Cora) + the
  4→8-step evolution.
