---
domain: sources
type: repo
url: https://github.com/SHL0MS/skill-diffs
retrieved: 2026-07-22
snapshot-location: sources/SHL0MS--skill-diffs/
upstream-commit: 2ded6c0b37e256d6934bf91349a5079ef146c6cf
last-reviewed: 2026-07-22
---

# SHL0MS--skill-diffs

> **One-line description**: a scraping + enrichment pipeline that mines the **commit history** of `SKILL.md` files across four agent platforms (Anthropic Claude, OpenClaw, OpenCode, Hermes Agent) into a published HuggingFace dataset of `(before, after, intent)` diff triples, plus two companion tools — a rule-based `SKILL.md` linter and a skill-patch eval harness — for training/evaluating a small "curator" model that maintains skill files automatically.

*Done when it passes the [page checklist](_definition-of-done.md).*

## Snapshot details

- **Retrieved**: 2026-07-22
- **Where it lives in this wiki**: `sources/SHL0MS--skill-diffs/` (live git-ignored clone; 924 KB, 33 files — no `data/` directory in the repo itself, the multi-GB dataset lives on HuggingFace)
- **Upstream URL**: https://github.com/SHL0MS/skill-diffs
- **Upstream identifier**: commit `2ded6c0b37e256d6934bf91349a5079ef146c6cf` (2026-05-04, the only commit on `main` at retrieval — single-commit repo; the dataset itself has iterated to v0.5 on the HuggingFace hub without a corresponding new GitHub commit, so the *pipeline* snapshot and the *published dataset* version are on separate clocks — see `#version-clock-split` below)
- **License**: repo license is `other` (per `gh api`, unresolved SPDX); the *published dataset*'s compilation is CC-BY-4.0, with each source repo's own SPDX license (or lack of one) tracked per-row in `repos.parquet`/`license_spdx`

## Anchor map

- `#root` — the repo as a whole
- `#README` — `README.md` — what's in the dataset, why, companion tools, pipeline script list, reproduction steps, per-version status log
- `#TRAINING` — `TRAINING.md` — the fine-tuning handoff doc: task framing, "gold isn't ground truth" caveat, recommended training config, baseline eval table, failure modes
- `#status-log` — `README.md`'s "## Status" section — the v0.1→v0.6(planned) changelog
- `#pipeline-scripts` — `README.md`'s "## Pipeline" + "## Files" tables — the ordered script chain (`discover.py` → `batch*.py` → `consolidate_v04.py` → enrichment scripts → `upload_hf.py`)
- `#skill_linter` — `skill_linter.py` (387 lines) — the rule-based `SKILL.md` linter; docstring + `ALL_RULES` (7 rule functions; `L1-L24` states it's "derived from the most common defect patterns observed... revealed by what skill maintainers actually fix in merged commits")
- `#skill_linter-rules` — `skill_linter.py` `L44-L387` — the actual rule set: `E001-no-frontmatter`, `E002-missing-name`, `E003-missing-description` (`L60-L92`); `W001/W002/W003` description-quality checks (`L100-L146`); `W004-codeblock-no-lang` (`L149-L168`); `I001`–`I008` deprecated-model/legacy-API patterns (`L172-L200`); `W005-no-heading` (`L211-L226`); `W006-short-body` (`L228-L239`); `--report` mode against the corpus (`L305-L336`)
- `#add_semantic_diff` — `add_semantic_diff.py` — the structured `diff_summary` column: `frontmatter_changed`/`body_added_chars`/`sections_added`/`sections_removed` + the `edit_kind` taxonomy (`frontmatter_only` / `body_only` / `structural` / `code_only` / `both` / `trivial` / `addition` / `deletion`)
- `#add_quality_score` — `add_quality_score.py` `L1-L75` — the aggregate `quality_score` (0.0–1.0) formula: +0.20 SPDX license, +0.10/+0.20 stars≥10/≥100, +0.15 has `pr_title`, +0.20/+0.10 absence of disqualifying/strict-disqualifying `quality_tags`, +0.05 high-signal `intent_class`, +0.10 body length 500–30,000 chars
- `#add_injection_tag` — `add_injection_tag.py` — the `prompt_injection_pattern` advisory quality tag (~0.27% of records, mostly defensive content in security skills)
- `#eval_curator` — `eval_curator.py` — the held-out skill-patch eval harness: `identity`/`intent_only` baselines + OpenAI/Anthropic/OpenRouter model adapters; metrics `edit_dist_ratio`, `rouge_l`, `judge_overall` (Sonnet-as-judge, 0–5), `linter_delta`
- `#baseline-table` — `TRAINING.md` `L51-L62` and `L174-L193` — the v0.5 stratified 250-example baseline table (identity / claude-haiku-4-5 / claude-sonnet-4-5) across imitation metrics + `linter_delta`
- `#gold-caveat` — `TRAINING.md` `L43` — "**Note on the 'ground truth' AFTER**": the merged AFTER is a mix of human/LLM/human-AI-collaborative authorship, undercounted even where PR-body co-author signatures exist; the eval "measures relative imitation quality, not absolute correctness"
- `#why-mining-evolution` — `README.md` "## Why" section (`L43-L53`) — the core framing: "existing public datasets capture *snapshots*; this one captures the **evolution**"
- `#hf-dataset` — the published dataset page, `huggingface.co/datasets/shl0ms/skill-diffs` (external; not part of the git snapshot) — v0.5, 2,531,798 total rows across all configs, 8.05 GB, tags `agent-skills`/`claude-skills`/`hermes-agent`/`opencode`/`code-edits`/`preference-pairs`
- `#version-clock-split` — observed discrepancy: the GitHub repo is pinned at a single commit (2026-05-04) while `README.md`'s own "## Status" section documents dataset iterations through v0.5 and a v0.6 plan — the *pipeline code* and the *published dataset* version independently, and the repo was not re-committed as the dataset advanced past whatever version was current at `2ded6c0`

## Why we cite this

Grounds the wiki's first source that treats **agent-skill files themselves as a mined corpus** rather than as artifacts to study directly — a meta-turn relative to everything else in this wiki (which reads skills; this reads *how skills get edited*). Supports claims about: mining commit history as a training-data source ([[concepts/commit-history-as-training-data]]); deriving validation rules from observed real-world defects rather than generic best-practice guessing ([[patterns/quality-bar/defect-derived-validation]]); the imitation-vs-correctness eval split for training data whose "gold" isn't guaranteed correct ([[concepts/imitation-vs-correctness-eval]]); and a fresh, cross-domain supporting sighting of [[patterns/behavioral/latent-vs-deterministic-split]] (the linter/quality-score pipeline is explicit "no LLM, no clone, no network" deterministic code sitting beside `llm_classify.py`'s latent classification and the Sonnet-judge eval).

## Popularity signals (if this source provides them)

- **Signal type**: github-repo (author account) + huggingface-dataset-downloads
- **Value at snapshot**: GitHub — 0★ / 0 forks, 8 public repos, 45 followers (author account `SHL0MS`, created 2023-04-17); HuggingFace dataset — **75 downloads in the last month**, 0 likes
- **As-of**: 2026-07-22
- **Read carefully**: this is a low-traction source by raw popularity (0 stars, 0 likes) — cited here for the *idea* and the *evidence base* (665k skills mined, 4 platforms, a working eval harness with real baseline numbers) rather than for adoption signal. Flag any claim of "this technique is catching on" as unsupported; the honest framing is "a well-evidenced, not-yet-popular technique."

## Related sources

- [[sources/mattpocock--skills]] — a skill *pack* this dataset's discovery scripts would plausibly have crawled (Anthropic-platform skill repo); no direct citation link, but the same ecosystem this dataset mines.
- [[sources/anthropic--skills]] — the canonical `SKILL.md` format this dataset's Anthropic-platform slice (and `skill_linter.py`'s frontmatter rules) is built against.
- **Unstudied, referenced context**: Hermes Agent's **Curator** feature (Nous Research, `hermes-agent.nousresearch.com/docs/user-guide/features/curator`) — the named downstream consumer this dataset is built to train a drop-in model for; not separately ingested (external product doc, not a repo/article we've snapshotted), but its description — "a background maintenance pass for agent-created skills" tracking usage and moving skills active→stale→archived — is directly relevant to this wiki's own LINT operation (see [[meta/self-improvements]] Pass 13).
