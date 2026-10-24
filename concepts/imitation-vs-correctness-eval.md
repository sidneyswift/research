---
domain: concepts
type: concept
name: imitation-vs-correctness-eval
creators: "[[creators/shl0ms]]"
sources: "[[sources/SHL0MS--skill-diffs]]"
status: emerging
last-reviewed: 2026-07-22
popularity-signals:
  - signal: adoption
    value: "1 documented instance, with a worked baseline table showing the two axes actually diverge"
    as-of: 2026-07-22
    source: "[[sources/SHL0MS--skill-diffs#baseline-table]]"
---

# imitation-vs-correctness-eval

> **One-line:** when a model's training "gold" is just *whatever got accepted* (not a verified-correct reference), don't evaluate the model on a single axis — split the eval into **imitation** (does it match the accepted-edit distribution? lexical + LLM-judge) and **correctness** (is it objectively better, measured against a rule-based signal that doesn't depend on trusting the gold at all).

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): read across `TRAINING.md`'s framing and baseline table, then write distilled judgment.*

## What it is

Most fine-tuning evals implicitly assume the training gold is "correct" and score a candidate model by how closely it matches that gold (exact match, edit distance, ROUGE, an LLM judge comparing to the reference). That assumption breaks when the gold is really just "what got merged in practice" — a mix of good edits, mediocre edits, and edits from unknown or mixed authorship, with no independent verification that any given one was *right*. This concept is the fix: run two separate evals. An **imitation** axis measures distributional match to the gold (lexical similarity, an LLM judge scoring plausibility/quality) — it tells you "does this look like what actually gets merged in this ecosystem." A **correctness** axis measures something objective and gold-*independent* — typically a deterministic rule-checker applied to both the prediction and the gold, then differenced — so a model can score as "better than the gold" without that claim resting on the gold being right in the first place.

## Where it came from

Demonstrated in SHL0MS's `skill-diffs`/`eval_curator.py`, applied to the SKILL.md skill-patch task. `TRAINING.md` states the caveat unprompted, ahead of any eval numbers: *"the `after_content` in this corpus represents edits that got merged into a public skill repo — a mix of human-authored edits, LLM-authored edits... and human-AI-collaborative edits. We don't reliably distinguish authorship... The eval below measures relative imitation quality, not absolute correctness"* ([[sources/SHL0MS--skill-diffs#gold-caveat]]). The correctness axis is operationalized as `linter_delta` — "(# findings on gold) − (# findings on pred)," where the findings come from the same rule-based linter described in [[patterns/quality-bar/defect-derived-validation]] ([[sources/SHL0MS--skill-diffs#eval_curator]]).

## Why it matters

It's a general fix for any fine-tuning or preference-training setup whose "ground truth" is scraped from real-world accepted behavior rather than authored by an expert (merged PRs, accepted Stack Overflow answers, shipped code, accepted support-ticket resolutions) — i.e., most large real-world training corpora. Without the split, a strong imitation score gets silently read as "the model is good," when it may just mean "the model reproduces the ecosystem's mediocre-but-common edits equally well." With the split, you can make an honest, falsifiable claim: "our model matches the accepted-edit style (imitation) *and* independently introduces fewer objective defects than the historical average (correctness)" — two different, non-conflatable claims.

## Evidence & claims

- The baseline table shows the two axes **genuinely diverging**, which is the strongest evidence this isn't a redundant distinction: `claude-sonnet-4-5` beats `claude-haiku-4-5` on `judge_overall` (2.30 vs 2.08) but *loses* to it — and to the `identity` no-op baseline — on `edit_dist_ratio` (0.752 vs 0.777 vs 0.817) and `rouge_l` (0.819 vs 0.831 vs 0.860). "Bigger model → higher judge score, lower lexical match" — citation: [[sources/SHL0MS--skill-diffs#baseline-table]]
- On the correctness axis, `identity` (return the input unchanged) scores `linter_delta` +0.024 while `sonnet` scores −0.036 — i.e., the no-op baseline is *slightly* cleaner than the historical gold, and Sonnet's rewrites introduce marginally more rule-detectable defects than the gold has — citation: [[sources/SHL0MS--skill-diffs#baseline-table]]
- The stated fine-tune target is explicitly **both axes at once** — `edit_dist_ratio` > 0.82 (beats identity) *and* `judge_overall` > 2.3 (matches the Sonnet ceiling), which "neither generic aux currently does both" — citation: [[sources/SHL0MS--skill-diffs#baseline-table]]

## Patterns demonstrated

- [[patterns/quality-bar/defect-derived-validation]] — the correctness axis (`linter_delta`) is only possible *because* a defect-derived, gold-independent rule set already exists; the eval methodology is a direct downstream consumer of that pattern. Citation: [[sources/SHL0MS--skill-diffs#eval_curator]].

(No 2nd artifact yet demonstrates this split as a technique in this wiki — tracked here as a concept rather than promoted to a pattern page; promote if a 2nd example lands.)

## Tensions & counter-arguments

- **The correctness axis is only as good as the rule-checker.** `linter_delta` is bounded by whatever `skill_linter.py` actually catches (frontmatter validity, code-block languages, deprecated references) — it cannot detect a semantically wrong-but-well-formatted edit. The split doesn't solve the underlying "no ground truth" problem; it isolates *one narrow slice* of correctness that happens to be checkable without a gold reference.
- **The two axes may not be reconcilable in practice.** The baseline data shows a real tradeoff (bigger model = better judge score, worse lexical/defect scores) rather than two independently improvable dials — it's an open question whether a fine-tune can actually clear both bars simultaneously, or whether the tradeoff is structural.
- **Single-source concept.** This is one documented instance; whether the split is a broadly reusable eval discipline or specific to skill-editing tasks with a cheap rule-based linter available isn't yet tested elsewhere in this wiki.

## Timeline (append-only)

- 2026-05-04 — `eval_curator.py` + the v0.5 baseline table published as part of the dataset's status log ([[sources/SHL0MS--skill-diffs#status-log]]).
- 2026-07-22 — ingested into this wiki via [[sources/SHL0MS--skill-diffs]].

## Related

- [[concepts/commit-history-as-training-data]] — the data-sourcing technique that *creates* the ungrounded-gold problem this concept works around.
- [[patterns/quality-bar/defect-derived-validation]] — supplies the gold-independent correctness signal (`linter_delta`) this concept relies on.
- [[artifacts/projects/skill-diffs]] — the artifact demonstrating this concept via `eval_curator.py`.

## What we'd steal

**Exhaustive ledger, not a curated top-3:**

- ★ **Whenever your training/eval gold is "what got accepted in practice" rather than an expert-authored reference, split the eval into imitation and correctness axes explicitly** — don't let a single similarity score stand in for both.
- ★ **Build the correctness axis from a rule-based, gold-independent checker if one exists (or is cheap to build)**, and difference it between prediction and gold (`linter_delta`-style) rather than scoring the prediction alone — the *delta* framing is what makes "better than the historical average" a meaningful, falsifiable claim.
- **State the gold-authorship caveat in the primary handoff doc, unprompted, before any eval numbers appear.** Readers who skip straight to a benchmark table need the caveat to land first, not as a footnote.
- **Report when the two axes disagree, don't average them away.** The wiki-worthy finding here is precisely that Sonnet wins one axis and loses the other — a single blended score would have hidden the more useful insight.
- **Name the target as a conjunction, not a single number** ("beat identity on lexical AND match Sonnet on judge") — makes clear that neither existing baseline is good enough, which is the actual case for building something new.

## Open questions

- Can a fine-tune actually clear both bars simultaneously, or is the imitation/correctness tradeoff structural for this task (bigger/more-capable models systematically over-rewrite)? Not yet demonstrated either way.
- Would a stronger, LLM-based correctness checker (rather than a fixed rule set) close the gap between "narrow objective correctness" and "actual correctness," or would it just reintroduce the gold-dependency problem one level up?
- Does this two-axis discipline apply cleanly to non-code, non-lintable artifacts (e.g. prose edits) where no cheap rule-based correctness signal exists?
