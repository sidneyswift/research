---
domain: meta
type: ledger
last-reviewed: 2026-06-01
---

# Self-Improvements Ledger

The output of the **REFLECT** operation (see [CLAUDE.md](../CLAUDE.md)). This wiki studies how to build great agents/skills — and it *is* one (the `CLAUDE.md` harness + `_schemas/` skills + operations routing + `index.md`/`log.md` memory). So every confirmed pattern is a candidate upgrade to our own machinery. This ledger keeps that loop honest: each entry traces a concrete wiki change back to a pattern **observed in this wiki** (never generic advice), so we can see *why* we work the way we do — and avoid re-proposing the same thing.

**Anti-rule:** no entry without a `[[patterns/...]]` or `[[concepts/...]]` citation. If you can't cite the learning, it's not a reflection — it's an opinion.

## Status legend

- `proposed` — candidate, not yet applied; needs human confirmation (REFLECT is human-gated like LINT).
- `applied` — change is live; links to where + the `log.md` entry.
- `rejected` — considered and declined; keep the reasoning so we don't relitigate.

## Ledger

### [2026-06-01] Seed pass — reflecting the AI-Explainer patterns onto the wiki

The first six entries are a retroactive REFLECT over the patterns extracted from Garry Tan's essay series. They were catalogued but never applied to the wiki itself; this pass closes that gap. All `proposed` pending review.

| # | Learning (cited) | Proposed wiki change | Status |
|---|---|---|---|
| 1 | [[patterns/composition/resolver-routing-table]] — a tested table mapping *intent → which skill/doc to load* | Add an explicit **Routing** table to `CLAUDE.md`: *request shape → operation* (Ingest/Query/Lint/Reflect) and *source type → schema + destination dir*. Today that routing is implicit prose; a table is the resolver. | proposed |
| 2 | [[patterns/quality-bar/complexity-ratchet]] — every session adds tests/docs that reload into context, so quality only rises (forward-only) | Make ingests **ratchet**: an ingest may not reduce cross-link density or leave a new orphan without a logged reason. Add this as a LINT check + a one-line "links added / orphans introduced" note in each ingest log entry. | proposed |
| 3 | [[patterns/behavioral/diarization]] — read everything about a subject, write *one* page of distilled judgment | Name this explicitly in the artifact/concept schemas: a page is a **judgment distillation**, not a summary. Add a one-line reminder to the schema headers so pages don't drift into transcription. | proposed |
| 4 | [[patterns/behavioral/latent-vs-deterministic-split]] — every step is model-judgment (latent) or same-in/same-out (deterministic); put each on the right side | Annotate each operation step in `CLAUDE.md` as **(det)** or **(latent)**. The deterministic ones (clone, add index row, append log) are future tooling candidates; the latent ones (extract patterns, write "what we'd steal") stay model work. Sets up the optional-CLI-tools path Karpathy mentions. | proposed |
| 5 | [[patterns/structural/thin-harness-fat-skills]] — push intelligence up into markdown, execution down into code, keep the harness thin | Treat `CLAUDE.md` as the **thin harness** and the `_schemas/` as the **fat skills**: detailed how-to belongs in templates, not in `CLAUDE.md`. Add a guard to LINT: flag `CLAUDE.md` growth that should have gone into a schema. | proposed |
| 6 | [[patterns/quality-bar/skill-pack-bundle]] — a skill isn't done until it ships with tests/evals | A **pattern page isn't done** until it has a falsifiable *"how to detect this in a new artifact"* recipe (its ≥2 examples are the fixtures, the counter-example is the negative test). Add a `## Detection recipe` section to `_schemas/pattern.md`. | proposed |

## Open meta-questions

- Should REFLECT run automatically every N ingests, or only on demand? (Karpathy keeps the human in the loop; default to on-demand + the lightweight INGEST step-9 nudge.)
- Is `meta/` itself in scope for LINT's orphan/staleness checks? (Yes — it's a wiki page like any other.)
