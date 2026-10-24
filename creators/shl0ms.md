---
domain: creators
type: individual
name: SHL0MS
handle: SHL0MS (GitHub + X/Twitter)
url: https://github.com/SHL0MS
country: # unstated
last-reviewed: 2026-07-22
---

# SHL0MS

> **One-line:** a GitHub handle (real name not disclosed; profile lists company `@shl0ms`) who built and published `skill-diffs` — a commit-history mining pipeline that turns the evolution of public `SKILL.md` files into training data for an automated "skill curator" model.

*Page shape (gbrain's brain-page schema, per [[patterns/behavioral/diarization]] applied to ourselves): **compiled truth on top** — edited in place — and an **append-only `## Timeline`** below. Done when it passes the [page checklist](_definition-of-done.md).*

## Attributes

- **What they ship**: a single, dense research-infrastructure repo — a scraping/enrichment pipeline plus two standalone companion CLI tools (a rule-based linter, an eval harness) plus the published HuggingFace dataset itself.
- **Distribution channel**: personal GitHub (`github.com/SHL0MS/skill-diffs`) for the pipeline code; HuggingFace Hub (`huggingface.co/datasets/shl0ms/skill-diffs`) for the actual data.
- **Position in ecosystem**: independent researcher/builder working on **agent-tooling infrastructure one level removed from agents themselves** — not a skill author, not a framework builder, but someone building the training data and eval scaffolding for a *model that maintains other models' skill files*. The wiki's first creator whose artifact is a dataset-and-tooling pipeline rather than something an agent runs directly.
- **Notable framing**: "Agent skills are a rare kind of training data: structured procedural specs that get iteratively refined through merged commits in public repos... Existing public datasets capture *snapshots*; this one captures the **evolution**" ([[sources/SHL0MS--skill-diffs#why-mining-evolution]]). Explicitly named downstream target: dropping the trained model into [Hermes Agent's Curator](https://hermes-agent.nousresearch.com/docs/user-guide/features/curator) `auxiliary.curator` slot or "any equivalent skill-maintenance loop" ([[sources/SHL0MS--skill-diffs#TRAINING]]).

## Artifacts produced

### Projects
- [[artifacts/projects/skill-diffs]]

## Design philosophy (if discernible)

Evidence-first and unusually honest about the limits of their own dataset. Two house-style tells stand out:

1. **Derive rules from real defects, don't guess them.** `skill_linter.py`'s 13 rules are explicitly "derived from the most common defect patterns observed across the skill-diffs corpus" — i.e., mined from what maintainers actually fixed in merged commits, not authored from generic best-practice intuition ([[sources/SHL0MS--skill-diffs#skill_linter]]). See [[patterns/quality-bar/defect-derived-validation]].
2. **Don't let a training signal quietly claim more than it can prove.** `TRAINING.md` foregrounds, unprompted, that the "gold" AFTER in every training pair is a merged edit of unknown/mixed authorship (human, LLM, or collaborative) — so an eval against it measures "relative imitation quality, not absolute correctness" — and ships a *second*, gold-independent correctness metric (`linter_delta`) specifically so a model can be judged as objectively better without trusting the gold ([[sources/SHL0MS--skill-diffs#gold-caveat]]). See [[concepts/imitation-vs-correctness-eval]].

Both instincts are unusual restraint for a solo dataset-release repo — most published datasets assert their gold is correct by omission; this one argues against its own ground truth in the primary handoff doc.

## Timeline (append-only)

- 2026-04-30 — `skill-diffs` GitHub repo created ([[sources/SHL0MS--skill-diffs#root]]).
- 2026-05-04 — last (only) commit on `main`, `2ded6c0`, at v0.5 of the dataset per `README.md`'s status log ([[sources/SHL0MS--skill-diffs#status-log]]).
- 2026-07-22 — wiki retrieval: HuggingFace dataset shows 75 downloads/month, 0 likes; GitHub repo 0★ ([[sources/SHL0MS--skill-diffs#hf-dataset]]).

## Source citations

- [[sources/SHL0MS--skill-diffs#root]]
