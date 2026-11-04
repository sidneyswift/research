---
domain: sources
type: paper
url: https://arxiv.org/abs/2611.00544v1
retrieved: 2026-11-04
published: 2026-10-31
snapshot-location: sources/zhang--skill-plus-plus/
upstream-commit: n/a (arXiv 2611.00544v1)
last-reviewed: 2026-11-04
---

# Skill++: Towards Lifelong Agents via Routing-Aware Skill Refinement

> Research on preserving access to existing skills as similar skills enter a library, by refining the incoming skill's routing metadata.

## Snapshot details

- **Authors:** Hanrong Zhang, Minghao Liang, Jiawei Wu, Yankai Chen, Shicheng Fan, Zhiwei Liu, Enze Ma, Junwei Yuan, Tianyi Wang, Dehai Min, Kening Zheng, Xue Liu and Philip S. Yu. Hanrong Zhang and Minghao Liang are marked equal contributors. Author/affiliation information comes from PDF page 1, not a separate biography investigation.
- **Version:** arXiv `2611.00544v1`, submitted October 31, 2026, 01:58:58 UTC. [Abstract](https://arxiv.org/abs/2611.00544v1), [PDF](https://arxiv.org/pdf/2611.00544v1), [HTML](https://arxiv.org/html/2611.00544v1). The unversioned URL supplied for ingestion resolved to this version.
- **Read coverage:** all 20 PDF pages: main argument, mathematical formulation, experimental results, limitations, references and Appendices A–C. Text extraction was checked against rendered pages 5, 8, 14, 16, 18 and 20 for the method, error chart, result tables, ablations and downstream-task caveat. Bibliography entries were read, but their papers were not recursively investigated.
- **Preservation:** full PDF, HTML, abstract metadata, page-by-page text, extracted PDF links and inspected page images are retained in ignored local `raw/`. The public repository preserves this original analysis, the [capture manifest](zhang--skill-plus-plus/capture.json), hashes and [version-pinned restoration instructions](zhang--skill-plus-plus/README.md). The arXiv record selects its nonexclusive distribution license, not a Creative Commons redistribution license; the full paper is not republished here.
- **Evidence class:** author-reported experiments in an arXiv preprint. We read and cross-checked the paper, not independently replicated it. No venue acceptance, citation count or production adoption is established by this capture.
- **Reproduction boundary:** no Skill++ author implementation/release URL was located in the PDF hyperlinks, arXiv record or bounded exact-title/arXiv-ID search on the retrieval date. This is not proof that no code exists. The cited SRA-Bench repository is a benchmark source, not a verified Skill++ release. Exact executable prompts, code revision and dollar/latency costs remain unverified.

## Anchor map

The page references below are **1-based PDF pages in v1**, not HTML line numbers. The local extraction has matching `page-NN.txt` files and page separators in `paper.txt`.

- `#root` — PDF pp. 1–20 and versioned arXiv metadata; title, attribution and overall scope.
- `#capture` — snapshot details above, capture manifest and restoration README.
- `#access-forgetting` — §§1–2, pp. 1–4; Fig. 1 and Appendix Fig. A1, p. 13: unchanged skill bodies/router can lose correct access after similar additions.
- `#formulation` — §3.1, pp. 4–5: fixed router, top-K skill selection, incoming metadata refinement, stability, plasticity and body fidelity.
- `#method` — §3.2, pp. 5–6; Appendix A, pp. 12–13; Algorithm 1: description differentiation, exclusions, name clarification, original reference records.
- `#implementation` — Appendix A, pp. 12–13: models, body-prefix budgets, synthetic queries, three ranking signals, lexicographic rank fusion, name-head rule, retries and length handling.
- `#benchmark-construction` — §4.1 and Appendix B.1, pp. 6–7, 13–14: 198 SRA-Bench/BigCodeBench queries, confusable nonsubstitute filtering, 27→731 skill stream and gold-skill metadata handling.
- `#metrics` — Appendix B.2, pp. 14–15: shortlist 10→top 5 routing, FC@5, Recall@5, query bootstrap and evaluation protocol.
- `#baselines` — Appendix B.3, p. 15; Table A1, p. 14: body-only summaries, neighbor edits, retrieval/rerank, hybrid retrieval, continual embedding tuning and CC-Pages; adapted comparison settings.
- `#main-results` — §4.2, pp. 7–8; Table A1, p. 14; Appendix C.1, pp. 15–16: final and checkpoint-average routing, paired confidence intervals and longitudinal forgetting.
- `#plasticity` — Appendix C.1, pp. 15–16: 1,864 body-derived queries for 673 refined incoming skills; first-place match, distinct from main FC@5.
- `#errors` — Fig. 5, p. 8; Appendix C.2, pp. 16–17, and Table A3, p. 16: 200→62 missing-skill errors, substitution/crowding counts, fixed baseline denominator, body-substitute adjudication.
- `#ablations` — Table A3/Fig. A2, p. 16; Appendix C.4, p. 19: component removal, similarity-based differentiation and meaningful versus arbitrary renaming.
- `#transfer` — Appendix C.3, pp. 17–19; Tables A4–A6: four additional routers, SkillRet and SkillRouter tasks, three addition orders and random-addition streams.
- `#harness` — Appendix C.3, p. 18; Table A7/Fig. A3, pp. 19–20: native Codex CLI skill installation, expanded skill-list budget, fresh sessions and first-five-named scoring.
- `#task-success` — Appendix C.3, p. 18, “Task success”: separate 87-skill/150-query run with a workflow prompt requiring five skills before tools; routing versus hidden-test pass-rate changes.
- `#robustness` — Appendix C.5 and Table A8, p. 20: display-order shuffle, rerun and a different arrival order under specified model settings.
- `#limitations` — limitations discussion, p. 9; experimental boundaries in Appendices A–C: text-only skills, selected-confusability benchmark and limited end-to-end evaluation. Missing release/cost evidence is our capture limitation, not an author claim.

## Why we cite this

Grounds [[concepts/lifelong-skill-routing]]: a library-level failure mode that individual skill correctness cannot detect. Connects [[patterns/composition/resolver-routing-table]] and [[patterns/quality-bar/complexity-ratchet]] to measured routing interference, while [[concepts/imitation-vs-correctness-eval]] keeps annotated selection separate from functional success.

## Popularity signals (if this source provides them)

- **Signal:** user-selected preprint, with a versioned public record; no citation/adoption count captured as of 2026-11-04. Publication on arXiv is not peer-review certification.

## Related sources

- [[sources/garrytan--resolvers]] — practitioner routing-table and routing-eval guidance; different evidence class.
- [[sources/mattpocock--skills]] — skill-authoring and invocation design; Skill++ adds a growing-library stress test.
- [[sources/SHL0MS--skill-diffs]] — empirical skill maintenance, but edit imitation and rule compliance are different evaluation targets.
- [[sources/ankrgyl--trace-lake]] — production failures can supply future routing-regression cases; not the data source for Skill++.
