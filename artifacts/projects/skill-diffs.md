---
domain: artifacts
subdomain: projects
type: project
name: skill-diffs
creator: "[[creators/shl0ms]]"
source: "[[sources/SHL0MS--skill-diffs]]"
ecosystem: cross-platform-training-data # spans Anthropic Claude / OpenClaw / OpenCode / Hermes Agent skill formats; not itself an agent runtime
discovered-via: direct-link
status: active # v0.5 published, v0.6 planned; single-commit pipeline repo, dataset iterated on the HF hub past the pinned commit
last-reviewed: 2026-07-22
popularity-signals:
  - signal: huggingface-dataset-downloads
    value: "75 downloads/month, 0 likes; GitHub repo 0★/0 forks"
    as-of: 2026-07-22
    source: "[[sources/SHL0MS--skill-diffs#hf-dataset]]"
---

# skill-diffs

> **One-line:** a pipeline that scrapes the commit history of `SKILL.md` files from ~5,900 public GitHub repos across four agent platforms, packages every commit-by-commit revision as `(before, after, intent)` diff triples, and ships two companion tools built on that corpus — a rule-based linter whose rules were mined from real merged-commit fixes, and an eval harness for benchmarking a model that patches skills automatically.

*This page is a **judgment distillation** ([[patterns/behavioral/diarization]]): read across the repo's `README.md`, `TRAINING.md`, and its enrichment/linter/eval scripts, written as distilled judgment — not a transcription.*

**Scope note:** grounded in [[sources/SHL0MS--skill-diffs]] (the `SHL0MS/skill-diffs` pipeline repo, commit `2ded6c0`). The multi-GB published dataset itself lives on HuggingFace and was **not** downloaded or inspected row-by-row — claims about its contents are drawn from the repo's own documentation (`README.md`/`TRAINING.md`) and its enrichment scripts, plus the HF hub's page-level metadata (download count). This is the wiki's **first artifact that is a dataset-and-tooling pipeline**, not something an agent runs directly — a different axis from skills/plugins/MCP servers/frameworks.

## Attributes

- **What it is**: a Python pipeline (`uv`-managed, dependency-free of any agent framework) that (1) discovers public repos containing skill files for four platforms, (2) walks each repo's full commit history via `git log` extraction to capture every revision of every `SKILL.md`-equivalent file, (3) consolidates that into versioned parquet releases, and (4) runs a chain of idempotent enrichment passes (licenses, PR metadata, MinHash + embedding dedup, structural diff summaries, quality scoring, injection-pattern tagging) before publishing to HuggingFace ([[sources/SHL0MS--skill-diffs#pipeline-scripts]]).
- **Scale (v0.5, as documented — not independently verified)**: 5,891 source repos, 664,872 unique skills (MinHash-deduped), 986,515 total revision records, 130,631 "clean" diff pairs, 76,142 records with PR title+body as intent labels, 630,119 bundled-resource snapshots across all 4 platforms ([[sources/SHL0MS--skill-diffs#README]]).
- **The core framing**: existing skill datasets capture *snapshots*; this one captures **evolution** — "structured procedural specs that get iteratively refined through merged commits," with authorship (human / agent / collaborative) deliberately undistinguished ([[sources/SHL0MS--skill-diffs#why-mining-evolution]]).
- **Target user**: someone fine-tuning a small model to do the `(before_skill, intent_text) → patched_skill` task — explicitly framed as the "LLM review pass for Hermes Agent's Curator or any equivalent maintenance loop" ([[sources/SHL0MS--skill-diffs#README]]).
- **Companion tool 1 — `skill_linter.py`**: a rule-based, no-LLM, no-network, no-clone linter for `SKILL.md` files. 7 rule functions covering missing/incomplete frontmatter, weak descriptions, code blocks missing a language tag, deprecated model names (`gpt-3.5-turbo`, `claude-2.x`, `claude-instant`, `text-davinci-*`) and legacy API calls (`openai.ChatCompletion.create`), missing top-level heading, and suspiciously short bodies — validated with a `--report` mode against the full corpus (**61% of skills trigger at least one finding**) ([[sources/SHL0MS--skill-diffs#skill_linter]], [[sources/SHL0MS--skill-diffs#skill_linter-rules]]).
- **Companion tool 2 — `eval_curator.py`**: a held-out benchmark for the skill-patch task, with built-in `identity`/`intent_only` baselines and OpenAI/Anthropic/OpenRouter model adapters. On the v0.5 stratified 250-example eval set, `claude-sonnet-4-5` wins `judge_overall` (2.30/5) but *loses* on lexical match (`edit_dist_ratio` 0.752 vs identity's 0.817) — **bigger model → higher judge score, lower lexical fidelity** — while `linter_delta` shows Sonnet introduces a small number of *new* defects relative to the merged gold (−0.036) ([[sources/SHL0MS--skill-diffs#baseline-table]]). The stated fine-tune target is to beat *both* axes at once, which neither generic baseline does.
- **License**: repo license `other`/unresolved SPDX (per `gh api`); the published dataset's *compilation* is CC-BY-4.0, with each source repo's own SPDX license tracked per-row so redistribution can be filtered (`curator_training_strict` requires a known license) ([[sources/SHL0MS--skill-diffs#root]]).
- **Verified-against-the-tree note (the wiki's usual manifest-vs-disk check)**: `README.md`'s own docstring calls `skill_linter.py` a "13 rules" linter; the file currently defines **7 rule functions** producing **17 distinct rule codes** (`E000` read-error, `E001`–`E003`, `W001`–`W006`, `I001`–`I008`) depending how you count categories vs. individual codes. Neither count lines up cleanly with "13" — likely a stale count from an earlier rule-set revision, in the same family as the manifest/README drift this wiki has flagged on other packs ([[artifacts/plugins/mattpocock-skills]], [[artifacts/plugins/compound-engineering]], [[artifacts/plugins/pm-os]]), not a functional defect.

## Relationships

- **Creator**: [[creators/shl0ms]] — the wiki's first dataset-and-tooling-pipeline creator.
- **Source**: [[sources/SHL0MS--skill-diffs#root]]
- **Embodies**: [[concepts/commit-history-as-training-data]] (the core "mine evolution, not snapshots" idea) and [[concepts/imitation-vs-correctness-eval]] (the eval methodology that separates "matches the merged edit" from "is objectively correct").
- **Demonstrates**: [[patterns/quality-bar/defect-derived-validation]] (the linter's rules are mined from real fix-commit patterns, not generic guessing — this artifact is the pattern's founding example) and [[patterns/behavioral/latent-vs-deterministic-split]] (a fresh, cross-domain supporting sighting: `skill_linter.py`/`add_quality_score.py` are explicitly deterministic — "no LLM, no clone, no network" — while `llm_classify.py` and the Sonnet-judge eval are the latent counterpart, in a *data-engineering* pipeline rather than an agent skill pack).
- **Supporting sighting for**: [[patterns/quality-bar/complexity-ratchet]] — the versioned enrichment chain (v0.1→v0.5) is additive and idempotent (each script "must run last" in a fixed order, drops-then-re-adds its own column, never removes another script's column), so the dataset's quality floor — license coverage, dedup, structural tags, `quality_score` — only rises release over release, applied to a *dataset* rather than a codebase.
- **Named downstream consumer (unstudied)**: Hermes Agent's **Curator** feature (Nous Research) — a background maintenance pass that tracks skill usage and moves skills through active→stale→archived states, consolidating overlaps. Not separately ingested, but directly relevant to this wiki's own LINT operation (see [[meta/self-improvements]] Pass 13).

## What problem it solves

Two, stacked. First, an ML-data problem: skill/agent-config files (`SKILL.md` and equivalents) are edited over time by a messy mix of humans and coding agents, and every public repo hosting them is sitting on a natural, structured `(before, after, intent)` training signal that nobody had mined at scale — prior public datasets ("~85x smaller," per the README's comparison to `huzey/claude-skills-diff`) captured only single snapshots. Second, a production problem: any system that lets an agent maintain its own skill library (Hermes Agent's Curator is the named example) needs a cheap, fast model to do the actual patch-writing, and a generic frontier model is both too slow/expensive to run in a background maintenance loop and — per the baseline table — doesn't actually match the *style* of real merged edits.

## How it works (the mechanism the source describes)

- **Discovery → extraction → consolidation.** `discover.py`/`discover_v04.py` find candidate repos per platform via GitHub search; `batch.py`/`batch_v04.py` walk each repo's full commit history extracting every revision of the target file (`extract.py`, with a per-repo timeout to stop monorepo stragglers from hanging the batch); `consolidate_v04.py` merges everything into per-format parquet releases tagged with a `platform` column ([[sources/SHL0MS--skill-diffs#pipeline-scripts]]). Every phase is resumable — manifest-based for batch jobs, per-repo cache for API fetches.
- **A strictly ordered, idempotent enrichment chain.** After consolidation, a fixed sequence of scripts each add exactly one column to the same release parquets and are individually re-runnable without duplicating work: PR metadata join → SPDX license/stars → MinHash near-duplicate clustering + frontmatter validation → quality tags (no-license/low-engagement/placeholder/PII) → structured `diff_summary` (the `edit_kind` taxonomy) → prompt-injection tagging → embedding-based semantic clustering (catching cross-author reimplementations MinHash misses) → the aggregate `quality_score`, which explicitly "must run last" because it reads several of the upstream columns ([[sources/SHL0MS--skill-diffs#add_quality_score]]).
- **The linter is derived, not designed.** `skill_linter.py`'s rule set reads as a direct transcription of the corpus's own PR titles ("fix YAML frontmatter," "update outdated model names," "add language tags to code blocks") into executable checks, then validated by running the linter back over the corpus and reporting per-rule trigger rates ([[sources/SHL0MS--skill-diffs#skill_linter]]).
- **The eval decouples two different questions.** `eval_curator.py` scores a candidate model on *imitation* (does the output match the merged-edit distribution — `edit_dist_ratio`, `rouge_l`, an LLM-judge `judge_overall`) and, separately, on *correctness* (`linter_delta` — does it introduce fewer or more rule-detectable defects than the gold, independent of whether the gold itself is correct). `TRAINING.md` is explicit that the two can diverge — Sonnet wins on judge score while losing on lexical match and introducing a small negative `linter_delta` — and frames the fine-tune target as clearing *both* bars at once ([[sources/SHL0MS--skill-diffs#baseline-table]], [[sources/SHL0MS--skill-diffs#gold-caveat]]).

## Patterns demonstrated

- [[patterns/quality-bar/defect-derived-validation]] — **founding example.** `skill_linter.py`'s 13-rules-by-docstring (7 functions / 17 codes in the current snapshot) are explicitly mined from what maintainers actually fixed in merged commits across the corpus, not authored from generic best-practice intuition, and the rule set is validated by running it back over the same corpus and reporting trigger rates (61% of skills flagged). Citation: [[sources/SHL0MS--skill-diffs#skill_linter]], [[sources/SHL0MS--skill-diffs#skill_linter-rules]].
- [[patterns/behavioral/latent-vs-deterministic-split]] — **supporting sighting, new domain.** The pipeline's own quality machinery is split cleanly: `skill_linter.py` and `add_quality_score.py` are explicit "no LLM, no clone, no network" deterministic code; `llm_classify.py` (a one-off Claude Haiku 4.5 batch classifier) and the eval harness's `judge_overall` (Sonnet-as-judge) are the latent counterpart. First sighting of the split inside a *data-engineering* pipeline rather than an agent skill pack. Citation: [[sources/SHL0MS--skill-diffs#skill_linter]], [[sources/SHL0MS--skill-diffs#eval_curator]].
- [[patterns/quality-bar/complexity-ratchet]] — **supporting sighting.** The v0.1→v0.5 enrichment chain is strictly additive and idempotent — each version's script adds a column without touching or removing prior columns, and the documented "## Status" log records the dataset's quality floor rising release over release (license coverage, cross-author dedup, structural tags, an aggregate score) rather than resetting. Citation: [[sources/SHL0MS--skill-diffs#status-log]], [[sources/SHL0MS--skill-diffs#add_quality_score]].

## Source citations

- What's in the dataset, scale, use cases — [[sources/SHL0MS--skill-diffs#README]]
- The training handoff, baseline table, gold-authorship caveat — [[sources/SHL0MS--skill-diffs#TRAINING]]
- The linter rule set — [[sources/SHL0MS--skill-diffs#skill_linter]], [[sources/SHL0MS--skill-diffs#skill_linter-rules]]
- The structural diff taxonomy — [[sources/SHL0MS--skill-diffs#add_semantic_diff]]
- The quality-score formula — [[sources/SHL0MS--skill-diffs#add_quality_score]]
- The eval harness + baselines — [[sources/SHL0MS--skill-diffs#eval_curator]], [[sources/SHL0MS--skill-diffs#baseline-table]]
- Version/status log — [[sources/SHL0MS--skill-diffs#status-log]]

## What makes it great

- **It mines evolution instead of collecting snapshots.** The single sharpest framing in the whole repo — "existing public datasets capture snapshots; this one captures the evolution" — is a genuinely different data-sourcing idea, not just a bigger version of an existing one ([[sources/SHL0MS--skill-diffs#why-mining-evolution]]).
- **The linter's rules are earned, not guessed.** Deriving validation rules from what real maintainers actually fixed (and then proving the rule set against the same corpus) is a stronger evidence chain than most rule-based linters ship with.
- **It argues against its own ground truth.** `TRAINING.md` volunteers, in its own handoff doc, that the gold AFTER isn't a reliable "correct answer" — then ships a second, gold-independent metric specifically to route around that weakness. Most dataset releases would quietly let the imitation metric stand in for correctness.
- **Every enrichment pass is idempotent and independently re-runnable.** The pipeline can be re-entered at any stage without re-deriving upstream columns — a property that made the v0.1→v0.5 iteration cheap enough to actually happen.

## What we'd steal

**Exhaustive ledger** (★ = highest-value, clearly portable):

- ★ **Derive your validation rules from historical fix commits, not from generic guessing.** Mine what people actually corrected (commit messages, PR titles) into a rule set, then validate the rule set by running it back over the historical corpus and reporting hit rates. Directly applicable to `wiki-doctor.py` — see [[patterns/quality-bar/defect-derived-validation]] and [[meta/self-improvements]] Pass 13.
- ★ **Ship a gold-independent correctness metric alongside any imitation/lexical metric**, whenever your "ground truth" is itself unreliable (mixed authorship, no guarantee of optimality). `linter_delta` is the concrete shape: count rule-detectable defects in the prediction vs. the gold, so "the model is objectively cleaner" doesn't depend on trusting the gold. See [[concepts/imitation-vs-correctness-eval]].
- ★ **State the gold-authorship caveat explicitly, in the primary handoff doc, before anyone trains on the data.** A one-paragraph honesty check ("this isn't human-verified ground truth") that changes how every downstream number should be read.
- **Idempotent, strictly-ordered enrichment scripts that each own exactly one column.** Makes a multi-version pipeline (v0.1→v0.5) cheap to re-run and easy to reason about — "must run last" as an explicit, documented ordering constraint rather than an implicit assumption.
- **A `--report` mode on the linter itself** — run the validation tool over the whole corpus and print per-rule trigger rates, so the rule set's coverage is measured, not assumed.
- **Companion tools that outlive the dataset.** `skill_linter.py` and `eval_curator.py` are useful even to someone who never touches the parquet files — worth designing any data-release repo's tooling to stand alone.
- **Name the version-clock split.** When a pipeline repo and its published artifact iterate independently (dataset hits v0.5 on HuggingFace; the GitHub repo sits at one commit), say so plainly rather than letting a reader assume the repo's HEAD matches the current dataset.

## Open questions / what's unclear

- **Independent verification of scale claims.** The 664,872-skill / 986,515-record / 5,891-repo figures come entirely from the repo's own documentation; we did not download the multi-GB dataset to spot-check them.
- **How real is the "13 rules" count?** The current `skill_linter.py` snapshot doesn't cleanly produce 13 by any counting convention we tried (7 functions, 17 distinct codes) — likely a stale docstring from an earlier revision rather than a functional issue, but unresolved.
- **Does the fine-tune target ever get hit?** `TRAINING.md` states a clear bar (`edit_dist_ratio` > 0.82 *and* `judge_overall` > 2.3, simultaneously) that neither Haiku nor Sonnet clears — whether anyone has actually trained and cleared it isn't documented here.
- **Adoption.** 75 HF downloads/month and 0 GitHub stars is a genuinely low-traction signal; cited for the technique and evidence quality, not for popularity. Re-check in a future LINT pass.
- **Is "curator model" itself a nameable concept/pattern the wiki should track independently** of this one source — i.e., is an aux model whose whole job is "patch this artifact given (current-state, intent)" a recurring shape worth its own page once a 2nd example (e.g. Hermes Agent's Curator itself, if ever ingested) lands?
