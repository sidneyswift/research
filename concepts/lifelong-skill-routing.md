---
domain: concepts
type: concept
name: lifelong-skill-routing
creators: "[[creators/hanrong-zhang]] and Skill++ coauthors"
sources: "[[sources/zhang--skill-plus-plus]]"
status: emerging
last-reviewed: 2026-11-04
---

# Lifelong skill routing

> A growing skill library can forget how to **reach** intact capabilities. Treat each incoming skill's name and description as an interface to be tested against its neighbors, not as standalone advertising copy.

## What it is

Under progressive disclosure, a router chooses among skill names/descriptions before reading selected bodies. Adding a superficially similar skill can therefore displace an earlier correct skill without changing either the earlier body or the model. Skill++ studies this as an access-level stability/plasticity problem: preserve old routing while keeping genuinely new capabilities discoverable. Its intervention changes only incoming metadata; the router, bodies and previous entries stay fixed. This is not parameter-level catastrophic forgetting or proof that an agent acquired new execution ability. [[sources/zhang--skill-plus-plus#access-forgetting]] [[sources/zhang--skill-plus-plus#formulation]]

Our synthesis: **metadata quality is relational**. A description can be accurate in isolation yet ambiguous in a particular library. The paper's mechanism is distinct from [[concepts/skill-invocation-axis]] (who may invoke) and complements [[patterns/composition/resolver-routing-table]] (how intent reaches a capability).

## Where it came from

*Skill++: Towards Lifelong Agents via Routing-Aware Skill Refinement*, arXiv 2611.00544v1, submitted 2026-10-31 by Hanrong Zhang, Minghao Liang and eleven coauthors. “Lifelong skill routing” is the paper's problem formulation; this wiki page generalizes the builder lesson without claiming the authors invented skill descriptions or regression testing. Evidence is a preprint's reported experiments, not our replication or verified production adoption. [[sources/zhang--skill-plus-plus#root]]

## Why it matters

Testing an added skill alone misses damage to every older route. In a top-five budget, redundant or overbroad metadata can consume the slots needed for a multi-skill task. The paper distinguishes **substitution** (a misleading competitor replaces a required skill) from **crowding** (selected additions consume scarce slots). Its curated test deliberately makes these failures likely; a separate random-addition experiment shows a smaller, still positive improvement. [[sources/zhang--skill-plus-plus#errors]] [[sources/zhang--skill-plus-plus#transfer]]

For builders, the useful first step is a small routing regression set around a skill's nearest neighbors. The paper does **not** establish that every library needs its exact multi-model preprocessing pipeline, that 731 skills is a universal limit, or that a particular skill count should trigger an architectural rewrite.

## Evidence & claims

### Method: refine the incoming interface, preserve the implementation

1. **Differentiate the positive description.** Find the nearest predecessor using original name/description embeddings. Read both bodies and lead with a supported capability that differentiates the incoming skill. The description must stand alone, not name the neighboring skill. A body-only summary is a tested weaker baseline. [[sources/zhang--skill-plus-plus#method]]
2. **Specify relevant exclusions.** Generate body-grounded synthetic user queries, compare metadata-to-query, query-to-query and metadata-to-metadata similarities, then select up to three predecessors. Append short exclusions for neighboring scopes. A single overlapping use can matter, so similarity uses maxima. Candidate ranks are combined lexicographically by `(best rank, sum of ranks)`, with arrival order breaking remaining ties—**not** reciprocal-rank fusion, which appears in a baseline. [[sources/zhang--skill-plus-plus#implementation]]
3. **Clarify colliding names.** Where an earlier name head occurs in the incoming name, add a meaningful scope qualifier. Arbitrary uniqueness is not the goal: a suffix may avoid string collision while conveying no routing distinction. [[sources/zhang--skill-plus-plus#method]] [[sources/zhang--skill-plus-plus#ablations]]
4. **Assemble within the visible budget.** Keep the positive capability description; drop exclusions from the end to fit the threshold. Preserve original metadata/body in a reference store and refined metadata in the operational library, so later refinements do not recursively compare against rewritten references. [[sources/zhang--skill-plus-plus#implementation]]

**Implementation details worth retaining, not universal defaults:** the paper uses MiniLM for initial metadata similarity; Qwen3-Embedding-4B for query comparisons; DeepSeek-V4-Flash for up to eight cached synthetic queries per skill; Gemini 3.5 Flash-Lite for metadata generation, with Gemini 3.6 Flash fallback for description retries. Body prefixes are limited to 1,600/1,200 characters for incoming/reference differentiation, 2,600 for query generation and 1,400 for renaming. Positive descriptions target ≤220 characters; exclusions fit a 298-character threshold because the studied router reads only the first 300 description characters. Name proposals must be 4–60 characters; name heads of ≤3 characters are ignored. Invalid generation falls back to the original field. If an original fallback description already exceeds the threshold, removing exclusions alone does not guarantee a hard cap. These are the reported settings, not requirements of the conceptual approach. [[sources/zhang--skill-plus-plus#implementation]]

**Our caution:** the paper's body-fidelity constraint is an objective enforced through generation prompts/checks, not a formal proof. Body-prefix reading can miss late instructions; exclusions derived from neighbors can accidentally rule out legitimate overlap. Validate both positive claims and exclusions against the actual incoming capability before adopting them. [[sources/zhang--skill-plus-plus#formulation]] [[sources/zhang--skill-plus-plus#implementation]]

### What the main experiment measures

- **Tasks:** 198 SRA-Bench queries sourced from BigCodeBench, each requiring 3–5 annotated skills. A ten-session stream grows from 27 to 731 skills; the final library contains 45 required skills, seven diagnostic skills and 679 additions. Released queries accumulate across checkpoints. [[sources/zhang--skill-plus-plus#benchmark-construction]]
- **Deliberate stress test:** additions are drawn from 25,626 public skills, filtered for metadata similarity, model-judged confusability and inability to fully replace the required skill. Required-skill metadata stays original; the intervention targets the incoming confusable additions. The pipeline is training-free for the router, **not judge-free** or generation-free. [[sources/zhang--skill-plus-plus#benchmark-construction]]
- **Main router:** Claude Haiku 4.5 at medium effort; all metadata → shortlist of ten → ranked five. Query prefixes are limited to 1,500 characters and description prefixes to 300. [[sources/zhang--skill-plus-plus#metrics]]
- **FC@5:** fraction of queries for which **all** annotated required skills appear in the selected five. It allows extra selections when fewer than five are required. **Recall@5:** per-query fraction of required skills recovered. Neither metric is execution success or a correctness proof. [[sources/zhang--skill-plus-plus#metrics]]

### Reported final-checkpoint results

Table A1, percentages; the final checkpoint is S9. [[sources/zhang--skill-plus-plus#main-results]]

| Method | FC@5 | Recall@5 |
| --- | ---: | ---: |
| Original metadata (Vanilla) | 36.4 | 69.7 |
| Incoming body-only description | 44.4 | 75.6 |
| Edit neighboring descriptions | 50.0 | 79.1 |
| Retrieval + reranking | 58.6 | 83.5 |
| Retrieval + reranking + continual embedding tuning | 67.8 | 87.6 |
| Hybrid retrieval + reranking | 58.6 | 83.3 |
| Hybrid retrieval + reranking + continual embedding tuning | 65.0 | 86.9 |
| CC-Pages | 60.1 | 84.5 |
| **Skill++** | **76.3** | **92.0** |

The authors report **+39.9 percentage points** versus Vanilla (95% paired-query bootstrap interval 32.3–47.5) and **+8.4 points** versus the strongest final baseline (2.4–14.5). Rounded table cells yield 8.5; retain the authors' unrounded-computation delta rather than silently “correcting” it. Mean FC@5 across S1–S9 is 58.5% versus 86.3%. Intervals use 10,000 query resamples; they are not estimates of variation over arbitrary models, organizations or arrival streams. [[sources/zhang--skill-plus-plus#main-results]] [[sources/zhang--skill-plus-plus#metrics]]

Baselines differ in what they receive and update. For example, continual-tuning variants train an embedding retriever on synthetic queries, whereas Skill++ edits metadata; CC-Pages uses released full-corpus pages that can include future skills before the final checkpoint. These are adapted, specified comparisons, not an exhaustive ranking of every routing architecture. [[sources/zhang--skill-plus-plus#baselines]]

### Mechanism evidence and ablations

- **Error counts:** missing-required-skill errors fall 200→62. Substitution falls 92→13, crowding 83→40 and other errors 25→9. Figure 5 percentages use **200 baseline errors as a fixed denominator**; 6.5% is not substitution's share of the 62 remaining errors. The error audit excludes verified full substitutes, whereas the headline metric matches annotated skill identities. [[sources/zhang--skill-plus-plus#errors]]
- **Components matter together:** final FC@5 is 76.3% with all components, 56.6% without description differentiation, 64.6% without exclusions and 61.6% without name clarification. These are ablations, not independent additive effect sizes. [[sources/zhang--skill-plus-plus#ablations]]
- **Semantic naming matters:** meaningful renaming for 81 name collisions yields eleven additional fully covered queries; arbitrary unique suffixes lose one. Choosing the nearest reference beats random reference selection by a reported 9.5 points. [[sources/zhang--skill-plus-plus#ablations]]
- **New-skill usability:** on 1,864 synthetic queries for 673 refined incoming skills, first-place matches rise 51.9%→56.9%; reported unrounded improvement +5.1 points. This is a separate, body-derived plasticity probe, not old-task FC@5 or real-user utility. [[sources/zhang--skill-plus-plus#plasticity]]

### Transfer and the important end-to-end boundary

| Setting | Reported outcome | Boundary |
| --- | --- | --- |
| Four additional routers | S9 FC@5: GPT-5.4-mini 59.6→86.9; GPT-5.6 Luna 71.7→85.9; GPT-5.6 Sol 76.8→88.4; Qwen3.7-Flash 49.0→71.7 | Same main task stream; model-specific gains |
| Random additions, three streams | Vanilla 84.3%, body-only 89.6%, Skill++ 93.3% final FC@5; authors report +8.9 points over Vanilla | Smaller effect than curated confusables; rounded cells differ by 9.0 |
| SkillRet / SkillRouter | Final FC@5 15.6→30.0 and 19.8→38.7, respectively, averaged over three addition orders | Transfer is positive, absolute coverage remains low; FC@5 excludes SkillRouter queries requiring >5 skills |
| Native Codex CLI routing | S9: Luna 7.6→39.9; Sol 70.7→73.7 | First five skills named; skill-list budget raised to fit all 731; not task-pass scores |
| Separate task-success check | Luna routing 33.3→77.3, hidden-test pass **+4.0 points**; Sol routing 82.0→88.0, hidden-test pass **+0.7 points** | 87 skills, 150 queries, prompt explicitly requires naming five skills before tools; not the full 731-skill run |

Sources: [[sources/zhang--skill-plus-plus#transfer]], [[sources/zhang--skill-plus-plus#harness]], [[sources/zhang--skill-plus-plus#task-success]]. The task-success passage does not give absolute hidden-test pass rates or their uncertainty. Do not translate the headline routing gain into “40 points better at coding.”

Limited robustness checks cover display-order shuffling, a rerun and a changed arrival order. They do not establish complete permutation invariance or robustness to every subsequent body edit. [[sources/zhang--skill-plus-plus#robustness]]

## Patterns demonstrated

- [[patterns/composition/resolver-routing-table]] — empirical support for testing the routing boundary, including negative cases. Skill++ refines a metadata router, not an explicit table; this does not add a shipped routing-table artifact to the pattern count. [[sources/zhang--skill-plus-plus#metrics]]
- [[patterns/quality-bar/complexity-ratchet]] — growing the library should preserve old route behavior as well as add new capability; the paper exposes why additive files alone are not monotonic improvement. [[sources/zhang--skill-plus-plus#access-forgetting]]
- [[patterns/structural/thin-harness-fat-skills]] — useful knowledge can reside in skill bodies with the model/router fixed, but a body is useless on a task if the routing interface hides it. Supporting research comparison, not a new production example. [[sources/zhang--skill-plus-plus#method]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — body-grounded description/exclusion generation is model judgment; length/parse checks, reference retention and tie-breaking are deterministic. Neither syntactic acceptance nor similarity ranking proves semantic fidelity. [[sources/zhang--skill-plus-plus#implementation]]

## Tensions & counter-arguments

1. **Selected stress is not typical prevalence.** The main stream intentionally adds confusing nonsubstitutes. Random additions improve too, but much less. Production library composition matters at least as much as raw count. [[sources/zhang--skill-plus-plus#benchmark-construction]] [[sources/zhang--skill-plus-plus#transfer]]
2. **Routing is a means, not the product outcome.** Annotated IDs may under-credit a functional alternative; selecting the right skills can still produce a failing solution. Keep exact routing, adjudicated substitutability and executable outcomes separate. [[sources/zhang--skill-plus-plus#errors]] [[sources/zhang--skill-plus-plus#task-success]]
3. **Training-free is not cost-free.** The method uses several generators, embedding models, retries and cached synthetic queries. No measured dollar/latency break-even or deployment cost is established here. [[sources/zhang--skill-plus-plus#implementation]] [[sources/zhang--skill-plus-plus#capture]]
4. **Unchanged predecessors are a narrow intervention, not an ideal-library guarantee.** Existing bad metadata stays bad. Our inference: separate incoming admission from deliberate legacy cleanup and rerun regressions for either. [[sources/zhang--skill-plus-plus#method]]
5. **Names may be identifiers as well as prose.** Our integration concern: a rename can affect explicit calls, paths and references even if it helps model selection. The paper's routing benchmark does not verify every host's rename semantics; preserve a stable identifier or update references deliberately.
6. **No magical skill-count threshold.** Explicit tables, hierarchical routing or pruning may be useful alternatives; these experiments do not settle every such choice. Test the actual candidate-generation stage—later reranking cannot recover a skill that never reached its shortlist. [[sources/zhang--skill-plus-plus#baselines]] [[sources/zhang--skill-plus-plus#main-results]]
7. **Scope of evidence:** text-only skills, limited downstream tasks, no independent rerun or located author release. The source is promising support for a mechanism, not a verified universal recipe. [[sources/zhang--skill-plus-plus#limitations]] [[sources/zhang--skill-plus-plus#capture]]

## Timeline (append-only)

- 2026-10-31 — Skill++ v1 submitted to arXiv. [[sources/zhang--skill-plus-plus#root]]
- 2026-11-04 — Full 20-page paper ingested, including implementation details, supplementary results and task-success limits. [[sources/zhang--skill-plus-plus#capture]]

## Related

- [[creators/hanrong-zhang]] — co-first author; all coauthors recorded on the source page.
- [[artifacts/skills/writing-great-skills]] — add library-relative discriminability to predictable skill authoring.
- [[concepts/skill-invocation-axis]] — permitted invocation and successful selection are separate axes.
- [[concepts/imitation-vs-correctness-eval]] — annotated retrieval versus functional task completion.
- [[concepts/trace-lake]] — our prospective connection: use real misrouting traces to choose regression cases, not only synthetic task queries.

## What we'd steal

These are portable design lessons derived from the evidence above, not claims that this wiki has implemented or benchmarked Skill++.

1. ★ **Treat adding a skill as a routing change.** Replay relevant older requests, not only requests showcasing the addition. [[sources/zhang--skill-plus-plus#access-forgetting]]
2. ★ **Write descriptions relative to the nearest alternatives.** Identify what makes this body the correct choice for its intended task; body-only summarization misses that relationship. [[sources/zhang--skill-plus-plus#method]]
3. ★ **Ground every advertised capability in the body.** Make unsupported broad descriptions a maintenance target, not a discovery advantage. [[sources/zhang--skill-plus-plus#errors]]
4. ★ **Add precise exclusions where real ambiguity exists.** Validate them against legitimate overlapping capability; do not paste a blanket “does not” list into every skill. [[sources/zhang--skill-plus-plus#implementation]]
5. **Qualify names semantically.** A useful scope phrase is preferable to arbitrary numbering when names collide. [[sources/zhang--skill-plus-plus#ablations]]
6. **Preserve original and operational metadata separately.** Keep provenance and a stable reference basis for future refinements; do not silently compound generated descriptions. [[sources/zhang--skill-plus-plus#method]]
7. **Keep the initial intervention narrow.** Refine the incoming entry before rewriting all neighbors; evaluate broader cleanup separately. [[sources/zhang--skill-plus-plus#baselines]]
8. **Use several signals for neighborhood discovery.** Metadata similarity, typical-query overlap and query-to-metadata matches can expose different collisions. [[sources/zhang--skill-plus-plus#implementation]]
9. **Use synthetic queries as probes, not ground truth.** Generate from capabilities, avoid naming the target, cache once and check overlap with evaluation tasks. [[sources/zhang--skill-plus-plus#implementation]]
10. **Respect what the router actually sees.** Put differentiating information before truncation; verify the host's real visibility budget instead of copying 298 characters universally. [[sources/zhang--skill-plus-plus#metrics]]
11. **Protect the positive description first.** Trim lower-priority exclusions before destroying the core capability statement. [[sources/zhang--skill-plus-plus#implementation]]
12. **Bound generation and preserve fallbacks.** Validate output shape, cap retries and keep the original when no acceptable rewrite is produced. [[sources/zhang--skill-plus-plus#implementation]]
13. ★ **Track stability and plasticity separately.** An incoming skill that never steals old tasks because it is never selected is not a success. [[sources/zhang--skill-plus-plus#plasticity]]
14. **Measure both all-required coverage and partial recall.** High average recall can still miss one indispensable skill on many multi-skill tasks. [[sources/zhang--skill-plus-plus#metrics]]
15. **Diagnose substitution and crowding separately.** Correct a false promise differently from excess selection of redundant but plausible tools. [[sources/zhang--skill-plus-plus#errors]]
16. **Measure shortlist recall before tuning rerankers.** Missing candidates cannot be rescued downstream. [[sources/zhang--skill-plus-plus#main-results]]
17. **Use both confusable and ordinary addition streams.** Report where the stress test exaggerates real-world interference and where a random stream understates the hard cases. [[sources/zhang--skill-plus-plus#transfer]]
18. **Validate in the actual host, with its real discovery configuration.** Distinguish native routing from a special evaluation workflow that forces selection first. [[sources/zhang--skill-plus-plus#harness]] [[sources/zhang--skill-plus-plus#task-success]]
19. ★ **Keep routing gains and task-success gains on separate scorecards.** Promote only claims supported by the downstream measurement. [[sources/zhang--skill-plus-plus#task-success]]
20. **Record denominators, intervals and rounded deltas.** Error shares, per-query success and first-place synthetic-query matches are different populations. [[sources/zhang--skill-plus-plus#errors]] [[sources/zhang--skill-plus-plus#plasticity]]
21. **Turn observed collisions into durable regression fixtures.** Our synthesis with [[concepts/trace-lake]]: save the triggering query, candidate-library version, selected skills and outcome, then rerun it on the next addition. [[sources/ankrgyl--trace-lake#trace-to-eval]]

## Open questions

- Can the author implementation, exact prompts, model revisions, task lists and skill stream be reproduced independently?
- What is the generation/embedding cost per admitted skill, and how many prevented failures repay it?
- How much benefit remains in our actual library versus these selected confusables, under actual metadata visibility limits?
- Can cheaper deterministic checks or a small manually maintained neighborhood fixture set capture most of the benefit before adopting the full pipeline?
- How should exclusions handle genuinely overlapping, complementary or substitutable skills without making new capabilities undiscoverable?
- How should descriptions be revalidated when bodies change after admission, and how should legitimate legacy cleanup preserve stable identifiers?
- Does this approach help multimodal skills or retrieval trees where the full library is never visible at once?
- Which routing regressions measurably change human time, task success, latency or spend—not just annotated skill recall?

## Tool-surface comparison — 2026-11-04

[[artifacts/projects/auto-ontology]] illustrates an adjacent design response: explicitly allow-list seven API tools plus two composite tools, override developer-oriented names/descriptions for agent decision-making and fail startup if a selected operation disappears. This is inspected engineering, not a replication of Skill++ or proof that nine is an optimal tool count. [[sources/nvidia--auto-ontology#curated-tools]]

## Pinned Codex implementation comparison — 2026-11-04

[[artifacts/projects/codex]] supplies complementary mechanisms: explicit paths resolve name collisions, ambiguous bare names are refused, catalog budgets record omitted/truncated metadata, and a deterministic cheap-selector interface supports shadow experiments. These are not Skill++ replication or proof a listed selector improves task outcomes. Default metadata budget is 2% of a known context window (8,000-character fallback); configured token limits have a separate cap. [[sources/openai--codex#skill-selection]] [[sources/openai--codex#skill-budget]] [[sources/openai--codex#skill-shadow]]

## Open Inspect: A pinned skill can still lose effective availability

[[artifacts/projects/background-agents]] exposes a pre-routing boundary: session-pinned managed skills can be dropped when names collide with repository/user/bundled discovery. Its installer reports those drops. Differential routing evaluations should hold the effective installed catalog explicit; better descriptions cannot repair an entry absent from the harness’s discovery tree. [[sources/open-inspect--background-agents#skills-pinning]] [[sources/open-inspect--background-agents#skills-install]]

## Cloudflare security audit — 2026-11-06

[[artifacts/skills/security-audit]] provides a scope distinction worth testing in routing evaluations: its description includes broad security questions, but its body defaults to guidance and reserves full execution/file creation for explicit audit/report intent. Discovery of the skill is not authorization to run every phase. No routing-retention or task-success benchmark was executed for this source. [[sources/cloudflare--security-audit-skill#modes]]

## Vercel Schedules — 2026-11-06

[[artifacts/projects/vercel-schedules]] includes a captured skill with import/path/command signals and prompt exclusions for meetings/calendar events. This is declared routing metadata beside Skill++’s measured routing experiments, not evidence those selectors improve accuracy. [[sources/vercel--schedules-docs#skill]]
