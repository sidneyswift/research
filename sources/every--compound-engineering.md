---
domain: sources
type: docs-page
url: https://every.to/guides/compound-engineering
retrieved: 2026-06-02
snapshot-location: sources/every--compound-engineering/snapshot.md (committed; PARTIAL capture)
upstream-commit: n/a (living guide page)
last-reviewed: 2026-06-02
---

# Compound Engineering (the Every guide)

> Every's living guide to **compound engineering** — the methodology that "each unit of
> engineering work should make subsequent units easier — not harder." States the 80/20
> (planning+review / execution) split, the eight-step loop (ideate → brainstorm → plan →
> work → review → polish → compound → repeat), the **eight beliefs to "unlearn,"** the
> **50/50 rule**, "taste belongs in systems, not review," and a 5-stage adoption ladder.
> Our framing source for the [[concepts/compound-engineering]] concept; the runnable
> embodiment is [[sources/every--compound-engineering-plugin]].

## Snapshot details

- **Retrieved**: 2026-06-02 (WebFetch). **PARTIAL capture** — `every.to` is a subscription
  publication; the snapshot at `sources/every--compound-engineering/snapshot.md` holds
  confirmed metadata + verbatim-quoted fragments + a paraphrased outline, **not** full
  verbatim prose. **TODO**: paste the complete guide text from a subscriber session.
- **Where it lives in this wiki**: [`snapshot.md`](every--compound-engineering/snapshot.md) (committed).
- **Upstream URL**: https://every.to/guides/compound-engineering
- **Version**: living guide, **no commit stamp** — claims pinned to retrieval date
  2026-06-02. The companion essay [[sources/every--compound-engineering-gets-an-upgrade]]
  (2026-05-29) notes "an updated compound engineering guide," i.e. the guide tracks the
  methodology as it evolves; treat it as `n/a (living page)`.
- **Authorship**: Every (every.to); the methodology is Kieran Klaassen's (see
  [[creators/every]]).

## Anchor map

Thematic pointers into the guide's named claims (and the labeled fragments in the
snapshot). **Do not invent anchors beyond this list.**

- `#root` — the guide as a whole
- `#thesis` — *"Each unit of engineering work should make subsequent units easier—not
  harder"*; the 80% planning+review / 20% execution split.
- `#loop` — the eight-step loop: *"Ideate → brainstorm → plan → work → review → polish →
  compound → repeat"* (with each phase's one-line role).
- `#unlearn` — the eight beliefs to discard ("the code must be written by hand," "every
  line must be manually reviewed," "first attempts should be good," …) + the higher-order
  "engineering thinking is separate from product thinking."
- `#50-50` — *"allocate 50 percent of engineering time to building features, and 50 percent
  to improving the system… any work that helps build institutional knowledge rather than
  shipping something specific"* (inverse of the traditional ~90/10).
- `#taste-in-systems` — *"Taste belongs in systems, not in review. Bake your judgment into
  configuration, schemas, and automated checks."*
- `#adoption-ladder` — Stage 0 (manual) → 1 (chat) → 2 (agentic + line review) → 3
  (plan-first, PR-only) → 4 (idea→PR, single machine) → 5 (parallel cloud); compound
  engineering "begins" at Stage 3.
- `#garbage-rate` — *"95 percent garbage rate"* on first attempts, *"50 percent"* on second.
- `#plugin-counts` — the guide's stated plugin size: "40+ specialized agents," "30+ slash
  entry points," "35+ skills" (cf. filesystem 43 agents + 38 skills at
  [[sources/every--compound-engineering-plugin#plugin-README]]).

## Why we cite this

- **The clearest statement of the [[concepts/compound-engineering]] thesis** and the
  inversions it demands of traditional engineering (the eight beliefs to unlearn, the 50/50
  rule). ([[sources/every--compound-engineering#thesis]], `#unlearn`, `#50-50`)
- **"Taste belongs in systems, not review"** — the single most quotable line, and the bridge
  to [[patterns/quality-bar/skill-pack-bundle]] / [[patterns/quality-bar/complexity-ratchet]]
  (bake judgment into automated checks rather than re-applying it manually each time).
  ([[sources/every--compound-engineering#taste-in-systems]])
- **The adoption ladder** — a 6-rung maturity model for human↔agent division of labor,
  useful for situating any agent-coding setup. ([[sources/every--compound-engineering#adoption-ladder]])

## Popularity / credibility signals

- **Talked-about**: an Every guide, the canonical reference the plugin's README links to
  ("Learn more"). As-of 2026-06-02. Hard adoption numbers not captured (paywalled).
- **Named author/origin**: methodology by Kieran Klaassen (GM of Cora at Every); origin essay
  *"My AI Had Already Fixed the Code Before I Saw It."* As-of 2026-06-02.

## Related sources

- [[sources/every--compound-engineering-gets-an-upgrade]] — Kieran's essay on the 4→8-step
  evolution (the dated companion to this living guide).
- [[sources/every--compound-engineering-plugin]] — the runnable embodiment; fully verifiable.
- [[creators/every]] — publisher; Kieran Klaassen + Dan Shipper.
- [[concepts/compound-engineering]] — the concept this guide defines.
