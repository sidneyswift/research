---
domain: meta
type: ledger
last-reviewed: 2026-06-02
---

# Self-Improvements Ledger

The output of the **REFLECT** operation (see [CLAUDE.md](../CLAUDE.md)). This wiki studies how to build great agents/skills — and it *is* one (the `CLAUDE.md` harness + `_schemas/` skills + operations routing + `index.md`/`log.md` memory). So every confirmed pattern is a candidate upgrade to our own machinery. This ledger keeps that loop honest: each entry traces a concrete wiki change back to a pattern **observed in this wiki** (never generic advice), so we can see *why* we work the way we do — and avoid re-proposing the same thing.

**Anti-rule:** no entry without a `[[patterns/...]]` or `[[concepts/...]]` citation. If you can't cite the learning, it's not a reflection — it's an opinion.

## Status legend

- `proposed` — recorded but not yet applied. Rare and transient: REFLECT normally applies grounded changes immediately (no human gate), so this status mostly appears mid-session.
- `applied` — change is live; links to where + the `log.md` entry.
- `embodied` — the pattern is already satisfied by existing structure; no change needed (still recorded so we don't re-propose it).
- `rejected` — considered and declined; keep the reasoning so we don't relitigate.

## Ledger

### [2026-06-01] Seed pass — reflecting the AI-Explainer patterns onto the wiki

A retroactive REFLECT over the patterns extracted from Garry Tan's essay series. They were catalogued but never applied to the wiki itself; this pass closes that gap. **All 6 applied 2026-06-02** (REFLECT ships grounded changes without asking — see `CLAUDE.md`).

| # | Learning (cited) | Wiki change | Status |
|---|---|---|---|
| 1 | [[patterns/composition/resolver-routing-table]] — a tested table mapping *intent → which skill/doc to load* | Added an explicit **Routing** table to `CLAUDE.md` Operations: *request → operation* and *source type → citation `type:` + raw-material location + page schema*. | **applied** 2026-06-02 (`CLAUDE.md` §Routing) |
| 2 | [[patterns/quality-bar/complexity-ratchet]] — every session adds tests/docs that reload into context, so quality only rises (forward-only) | Ingests now **ratchet**: INGEST closes with a `ratchet: links +N · orphans +0 · patterns +N` tally; LINT check #12 flags any ingest that added a page but no links, or stranded an orphan. | **applied** 2026-06-02 (`CLAUDE.md` INGEST + LINT #12) |
| 3 | [[patterns/behavioral/diarization]] — read everything about a subject, write *one* page of distilled judgment | Added a "this page is a **judgment distillation**, not a transcription" reminder to every artifact + concept schema header. | **applied** 2026-06-02 (`_schemas/{skill,plugin,mcp-server,concept}.md`) |
| 4 | [[patterns/behavioral/latent-vs-deterministic-split]] — every step is model-judgment (latent) or same-in/same-out (deterministic) | Tagged each INGEST step **(det)** or **(latent)** with a legend; det steps (clone, index row, log) are flagged as future-tooling candidates. | **applied** 2026-06-02 (`CLAUDE.md` INGEST) |
| 5 | [[patterns/structural/thin-harness-fat-skills]] — push intelligence up into markdown, execution down into code, keep the harness thin | Added LINT check #13 (**harness bloat**): flag detailed how-to that crept into `CLAUDE.md` and belongs in a `_schemas/` template. | **applied** 2026-06-02 (`CLAUDE.md` LINT #13) |
| 6 | [[patterns/quality-bar/skill-pack-bundle]] — a skill isn't done until it ships with tests/evals | Added a `## Detection recipe` section to `_schemas/pattern.md` (look-for / confirm-with / rule-out); the ≥2 examples are the positive fixtures, the counter-example the negative test. | **applied** 2026-06-02 (`_schemas/pattern.md`) |

### [2026-06-02] Pass 2 — the remaining confirmed/with-page patterns

REFLECT over the patterns not covered by the seed pass. Applied immediately (grounded → ships).

| # | Learning (cited) | Wiki change | Status |
|---|---|---|---|
| 7 | [[patterns/behavioral/skill-as-method-call]] — a skill file is a parameterized procedure; same file + different args → different capability | Documented each operation as a **parameterized call** in `CLAUDE.md` Routing (`INGEST(<source>)`, `QUERY(<question>)`, `LINT(<scope?>)`, `REFLECT(<since?>)`); noted that a `_schemas/` template is likewise a parameterized page. | **applied** 2026-06-02 (`CLAUDE.md` §Routing) |
| 8 | [[patterns/composition/single-source-multi-surface-distribution]] — one definition, many runtime surfaces | Added an anti-rule: wiki pages are the single source; `DASHBOARD.html`, query deliverables, and any future `llms.txt` are *surfaces* rendered from them, never parallel copies that drift. | **applied** 2026-06-02 (`CLAUDE.md` anti-rules) |
| 9 | [[patterns/structural/marketplace-as-multi-plugin]] — one manifest registers N à-la-carte units | No change: already embodied. `index.md` (+ per-domain `_index.md`) is exactly this registry — it lists every page as an independently-linkable unit. Recorded so we don't re-propose it. | **embodied** 2026-06-02 (`index.md`) |

## Open meta-questions

- ~~Should REFLECT run automatically every N ingests, or only on demand?~~ **Resolved 2026-06-02:** REFLECT applies grounded changes directly (no human gate); the lightweight INGEST step-9 nudge runs every ingest, and a deeper pass runs on demand / after lint.
- Is `meta/` itself in scope for LINT's orphan/staleness checks? (Yes — it's a wiki page like any other.)
