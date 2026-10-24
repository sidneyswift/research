---
domain: concepts
type: concept
name: commit-history-as-training-data
creators: "[[creators/shl0ms]]"
sources: "[[sources/SHL0MS--skill-diffs]]"
status: emerging
last-reviewed: 2026-07-22
popularity-signals:
  - signal: adoption
    value: "1 documented instance (skill-diffs, 75 HF downloads/month); named prior-art comparison (huzey/claude-skills-diff, ~85x smaller, snapshot-only)"
    as-of: 2026-07-22
    source: "[[sources/SHL0MS--skill-diffs#README]]"
---

# commit-history-as-training-data

> **One-line:** don't just collect snapshots of an artifact you want a model to learn to produce or edit — mine the **commit-by-commit revision history** of many public instances of it, so every merged edit becomes a natural `(before, after, intent)` training triple that captures how the thing actually gets improved over time, not just what it currently looks like.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): read across the source's README/TRAINING docs and enrichment scripts, then write distilled judgment — not a summary of any single file.*

## What it is

Most datasets for "teach a model to produce artifact X" are built from final, published instances of X — a corpus of finished code files, finished essays, finished configs. This concept is the alternative move: go to the *version control history* behind many public instances of X and extract every commit-by-commit revision as a labeled training example, where the label (the "intent") is the commit message or PR title that describes *why* the change was made. The training signal becomes an edit operation — `(current state, stated intent) → next state` — rather than a generation-from-scratch task, and it captures a population's actual editing behavior (what gets fixed, what gets added, what gets reworded) instead of a single frozen best-practice example. It's most valuable for artifacts that are (a) structured/parseable, (b) maintained iteratively in public repos, and (c) numerous enough across the ecosystem that commit history at scale beats hand-curated examples.

## Where it came from

Named and demonstrated by SHL0MS's `skill-diffs` pipeline, applied to `SKILL.md` agent-skill files across four platforms (Anthropic Claude, OpenClaw, OpenCode, Hermes Agent). The source states the framing directly: "Existing public datasets capture *snapshots*; this one captures the **evolution** — every commit-by-commit revision with diffs, commit messages, PR titles + bodies (where available), and authorship metadata" ([[sources/SHL0MS--skill-diffs#why-mining-evolution]]). The source itself names a smaller prior-art snapshot dataset (`huzey/claude-skills-diff`) it claims to be "~85x larger" than by mining history instead of snapshots ([[sources/SHL0MS--skill-diffs#README]]) — evidence the *snapshot* approach was the default before this technique.

## Why it matters

If this generalizes, it's a data-sourcing strategy applicable to any structured artifact maintained via public commits — not just agent skills. It changes what "training data" means for a maintenance-model task: instead of asking a model to imitate a static best example, you're asking it to imitate an *editing distribution* mined from thousands of real maintainers' actual fixes. For an agent-tooling wiki specifically, it reframes "what makes a skill good" from a design question (what should a great `SKILL.md` look like) into an empirical one (what do real skills actually get fixed to look like) — see [[patterns/quality-bar/defect-derived-validation]] for the sharpest instance of that reframe.

## Evidence & claims

- *"Agent skills are a rare kind of training data: structured procedural specs that get iteratively refined through merged commits in public repos"* — the corpus covers 5,891 repos, 664,872 unique skills, 986,515 total revision records, 130,631 "clean" diff pairs — citation: [[sources/SHL0MS--skill-diffs#README]]
- Authorship (human vs. coding-agent vs. collaborative) is deliberately **not** distinguished — "we don't distinguish" — which the source treats as acceptable because the target task is imitating *what gets merged*, not imitating *humans specifically* — citation: [[sources/SHL0MS--skill-diffs#why-mining-evolution]]
- The intent label is a fallback chain: PR title+body where available (documented at only 7.7% of the full corpus / 18.8% of the "clean" tier), falling back to the bare commit subject otherwise — a *demonstrated*, not merely asserted, coverage gap — citation: [[sources/SHL0MS--skill-diffs#README]]

## Patterns demonstrated

- [[patterns/quality-bar/defect-derived-validation]] — the concept's sharpest downstream application: once you've mined a commit-history corpus, you can derive *validation rules* (not just training pairs) from the same "what got fixed" signal. Citation: [[sources/SHL0MS--skill-diffs#skill_linter]].
- (Candidate, needs a 2nd artifact) A "curator model" pattern — a small fine-tuned model whose whole job is `(current_artifact, stated_intent) → patched_artifact`, evaluated against both an imitation metric and a gold-independent correctness metric. Tracked as an open question on [[artifacts/projects/skill-diffs]] pending a 2nd in-wiki example.

## Tensions & counter-arguments

- **The "gold" isn't a correctness signal.** The source itself argues against over-trusting this technique: the AFTER state in every mined pair is just "whatever got merged," a mix of human, LLM, and human-AI-collaborative authorship with no verification that it's *actually correct* — only that it's what maintainers accepted. This is the central limitation the technique inherits from its own strength (real-world scale) — see [[concepts/imitation-vs-correctness-eval]] for how the source works around it.
- **Sparse rich labels.** The richest intent signal (PR title+body) covers under 20% of even the filtered corpus; most of the training signal is a bare commit subject, which is a much weaker description of *why* an edit happened.
- **n=1 in this wiki.** This is currently a single demonstrated instance. Whether the technique generalizes cleanly to other structured artifacts (configs, IaC templates, prompt libraries) — where the intent-label sparsity or the authorship-mixing problem might be worse or better — is untested here.

## Timeline (append-only)

- 2026-04-30 — `skill-diffs` repo created; mining begins ([[sources/SHL0MS--skill-diffs#root]]).
- 2026-05-04 — dataset at v0.5, pipeline repo's last commit ([[sources/SHL0MS--skill-diffs#status-log]]).
- 2026-07-22 — ingested into this wiki via [[sources/SHL0MS--skill-diffs]].

## Related

- [[concepts/imitation-vs-correctness-eval]] — the eval-methodology consequence of mining a corpus whose gold isn't guaranteed correct.
- [[artifacts/projects/skill-diffs]] — the artifact that embodies this concept.
- [[patterns/quality-bar/defect-derived-validation]] — the pattern this concept's data enables.

## What we'd steal

**Exhaustive ledger, not a curated top-3:**

- ★ **If you want a model to maintain an artifact well, mine how real instances of it actually got maintained** — commit history over a large public population beats a single hand-authored "best example," because it captures the *distribution* of real fixes, not one person's idea of best practice.
- ★ **Treat the intent label as a fallback chain, and document the coverage at each tier.** PR title+body (rich) → commit subject (weak) is a reusable shape for any commit-mining project, and reporting exactly what fraction hits the rich tier (7.7%/18.8% here) keeps downstream users honest about label quality.
- **Explicitly decline to distinguish authorship when the target task doesn't need to.** If your task is "imitate what gets merged," don't spend effort on an authorship classifier you don't need — but say so, so the decision reads as deliberate rather than an oversight.
- **Publish multiple filtered tiers of the same corpus** (default / strict / eval-holdout) rather than one undifferentiated dump, so downstream users can trade recall for precision without re-deriving filters themselves.
- **Name your nearest prior art and quantify the delta** ("~85x larger than X") — gives a reader an instant calibration point for how much of an advance this actually is.

## Open questions

- Does this technique generalize past `SKILL.md`-shaped artifacts to other structured, commit-maintained specs (IaC, prompt libraries, CI configs)? No 2nd example exists yet in this wiki.
- How much does intent-label sparsity (only ~19% at the rich tier) actually hurt downstream training quality, versus the bare commit subject being "good enough"? Untested here.
- Is there a cleaner way to handle the mixed-authorship problem than "don't distinguish" — e.g., a co-author-signature detector, even an imperfect one, as an optional filter dimension?
