---
domain: concepts
type: concept
name: evidence-calibrated-research
creators: ["[[creators/lauren-tan]]"]
sources: ["[[sources/cursor--plugins-pstack]]"]
status: emerging
last-reviewed: 2026-10-24
---

# evidence-calibrated-research

> Make the strength of each claim match its evidence, while preserving what was searched, what could not be searched, and which explanations still compete.

## What it is

An agent investigation should return more than a plausible answer. It should leave the reader able to distinguish an explicit statement in a source, a conclusion supported by several observations, an interpretation, a speculative explanation, and an unresolved question. The research process preserves those distinctions from collection through synthesis and final presentation. “Calibrated” here means that language matches the available evidence; this source does not demonstrate statistically calibrated confidence probabilities. [[sources/cursor--plugins-pstack#RE08]], [[sources/cursor--plugins-pstack#RE09]]

The process also makes coverage inspectable. It anchors the question to specific code and history, assigns sources to investigators, records searches including empty results, and distinguishes missing access or expired retention from evidence that something did not happen. Synthesis resolves disagreements by returning to sources where possible, and otherwise shows the disagreement. This is a research contract, not a persistent memory architecture or an autonomous completion controller. [[sources/cursor--plugins-pstack#RE03]], [[sources/cursor--plugins-pstack#RE05]], [[sources/cursor--plugins-pstack#RE06]], [[sources/cursor--plugins-pstack#RE12]]

## Where it came from

This is the wiki’s descriptive name for a mechanism in [[creators/lauren-tan]]’s [[artifacts/plugins/pstack]], inspected at commit `9580c23696ac8d7abed0c166f2f9918800afb819` on October 24, 2026. The strongest expression is the `why` skill and its epistemics, investigator, synthesizer, and source-playbook references. `how` contributes bounded architectural exploration; `arena` contributes explicit comparison of alternatives; `interrogate` contributes evidence-based filtering of review findings. These are related procedures with different outputs, not one interchangeable kind of research. [[sources/cursor--plugins-pstack#RE01]], [[sources/cursor--plugins-pstack#RE07]], [[sources/cursor--plugins-pstack#RE22]], [[sources/cursor--plugins-pstack#RE25]]

The source material is predominantly **prompt policy**. This investigation did not run its agents, search private integrations, or evaluate model accuracy. The source prescribes the behavior; it does not establish historical priority or a measured reduction in hallucination. [[sources/cursor--plugins-pstack#RE08]], [[sources/cursor--plugins-pstack#RE15]]

## Why it matters

Code reveals behavior more readily than motivation. A retry loop can be traced directly, while its original reason may live in an incident, a customer constraint, an abandoned design, or nowhere accessible. An agent that fills that gap with a sensible story can make a future refactor less safe. Keeping mechanics and motives separate lets a reader preserve a real constraint while questioning an unsupported explanation. [[sources/cursor--plugins-pstack#RE01]], [[sources/cursor--plugins-pstack#RE05]], [[sources/cursor--plugins-pstack#RE09]]

A coverage map also makes the next step cheaper. “Unknown because the relevant telemetry expired” asks for a different action than “no result after searching the matching dates and error signature.” A cited contradiction can justify another source check; an unsupported hypothesis can become a discriminating experiment. The practical aim is decisions that remain useful when reviewed, rather than prose that merely sounds authoritative. [[sources/cursor--plugins-pstack#RE06]], [[sources/cursor--plugins-pstack#RE12]], [[sources/cursor--plugins-pstack#RE47]]

## Evidence & claims

- **Prompt policy: choose the inquiry contract.** `how` answers mechanics and layering; `why` investigates rationale; blast-radius tests consequences; teach explains the result at the reader’s pace. A single module normally gets one explainer, while a larger subsystem gets a few distinct explorers. [[sources/cursor--plugins-pstack#RE01]], [[sources/cursor--plugins-pstack#RE02]]
- **Prompt policy: ground before broadening.** Why builds a common seed of exact paths, lines, symbols, commits, PR discussions, and ticket IDs. Source control includes rename history, pickaxe searches, co-change, tests, and architectural records. [[sources/cursor--plugins-pstack#RE05]]
- **Prompt policy: collect sources separately.** Each investigator owns one source, reads full items, records exact queries, and returns cross-source leads instead of silently taking over another worker’s scope. Its output distinguishes direct evidence, circumstantial evidence, contradictions, gaps, and additional leads. [[sources/cursor--plugins-pstack#RE07]]
- **Prompt policy: account for coverage.** Why maps available integrations to seven evidence categories and includes unavailable, skipped, and empty searches in the final answer. This is category coverage, not proof that every relevant repository, workspace, document, or data stream was searched. [[sources/cursor--plugins-pstack#RE06]]
- **Prompt policy: retain confidence through transformations.** Direct, Supported, Inferred, Speculative, and Unknown claims have different wording and output locations. The presenting parent and teaching layer must preserve that confidence language. A cited author statement establishes what the author said; its truth and present applicability remain separate questions. [[sources/cursor--plugins-pstack#RE08]], [[sources/cursor--plugins-pstack#RE45]]
- **Prompt policy: actively challenge the story.** Investigators test whether the evidence would look similar if the favored interpretation were wrong. Synthesis keeps competing hypotheses and contradictory sources, and treats the user’s suggested explanation as a candidate rather than a conclusion. [[sources/cursor--plugins-pstack#RE09]]
- **Prompt playbooks: interpret source-specific failure modes.** Ticket scopes change, drafts diverge from code, chat messages lose context, telemetry expires, schemas drift, instrumentation changes mimic behavioral changes, and analytics refreshes lag. The playbooks explicitly retain these qualifications. [[sources/cursor--plugins-pstack#RE10]], [[sources/cursor--plugins-pstack#RE11]], [[sources/cursor--plugins-pstack#RE12]], [[sources/cursor--plugins-pstack#RE13]]
- **Prompt policy: compare alternatives without calling agreement proof.** Arena separates candidate generation from rubric-based judging, picks one coherent base, and records grafts, rejections, dropouts, and verification. Interrogate requires a concrete execution path for a defect and retains minority correctness/security findings. These are supporting comparison methods; neither model consensus nor a rubric score establishes truth. [[sources/cursor--plugins-pstack#RE22]], [[sources/cursor--plugins-pstack#RE23]], [[sources/cursor--plugins-pstack#RE24]], [[sources/cursor--plugins-pstack#RE26]], [[sources/cursor--plugins-pstack#RE27]]

## Patterns demonstrated

- [[patterns/behavioral/persona-lens-review-panel]] — a related decomposition strategy. How separates subsystem angles and Why separates evidence sources; Interrogate explicitly seeks model diversity rather than assigned personas. Preserve those differences instead of counting every parallel worker as the same kind of panel. [[sources/cursor--plugins-pstack#RE03]], [[sources/cursor--plugins-pstack#RE07]], [[sources/cursor--plugins-pstack#RE25]]
- [[patterns/behavioral/evidence-gated-completion]] — the claim-publication analogue: unsupported findings must be downgraded or left open; a safety claim should advance toward execution evidence. The source offers a prompt contract, not an enforced runtime termination predicate. [[sources/cursor--plugins-pstack#RE08]], [[sources/cursor--plugins-pstack#RE09]], [[sources/cursor--plugins-pstack#RE47]]
- [[patterns/composition/resolver-routing-table]] — source-category playbooks and the distinction between How, Why, Recall, and Teach route different questions to different evidence work. This narrower routing is not evidence of a tested global reachability audit. [[sources/cursor--plugins-pstack#RE01]], [[sources/cursor--plugins-pstack#RE06]], [[sources/cursor--plugins-pstack#RE35]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — interpretation belongs to synthesis, while checkable claims should be tied to inspected or executed artifacts. Most controls in this source remain instructions; deterministic citation or entailment validation is a possible extension, not an implementation shown here. [[sources/cursor--plugins-pstack#RE14]], [[sources/cursor--plugins-pstack#RE47]]

## Tensions & counter-arguments

**Confidence labels do not validate evidence.** Direct testimony can be wrong or retrospective; several indirect sources can repeat one original account. The distinction between Supported and Inferred also needs judgment. The source gives wording rules and spot checks, not a calibrated scoring model or provenance-dependency graph. An implementation should retain original source identities and distinguish existence, entailment, credibility, and independence. [[sources/cursor--plugins-pstack#RE08]], [[sources/cursor--plugins-pstack#RE14]]

**Coverage has a cost.** Why defaults to a full category sweep and permits only narrow reasons to skip. How defaults to the simple route, and Teach explicitly narrows Why because its sweep is slow. These policies can coexist if the caller supplies a scope and budget; without that, “complete coverage” can spend more attention than the decision warrants. No source-count threshold establishes sufficiency. [[sources/cursor--plugins-pstack#RE02]], [[sources/cursor--plugins-pstack#RE06]], [[sources/cursor--plugins-pstack#RE45]]

**Parallelism can multiply correlated error.** Shared grounding is useful, but it also shares assumptions. Different model families do not ensure independence. Arena’s hidden grading rubric may reduce superficial gaming, yet can make evaluation unfair when requirements were never stated to candidates. Disagreement calls for evidence review, not automatic preference for the majority or the supposedly stronger model. [[sources/cursor--plugins-pstack#RE18]], [[sources/cursor--plugins-pstack#RE22]], [[sources/cursor--plugins-pstack#RE27]]

**Research intent is weaker than capability restriction.** Why requests agent mode because its documented environment removes MCP access in read-only mode, then prohibits writes in prose. A reusable implementation should grant read capabilities independently of mutation capabilities. The source’s permission workaround is not proof that investigators cannot alter external state. [[sources/cursor--plugins-pstack#RE15]]

**Good history can still be a bad current constraint.** A customer request, incident, or old threshold may no longer apply. Translating lineage into Preserve / Change / Avoid / Risk is useful, but retaining a historical reason should not freeze the design indefinitely. Verify current requirements before treating an old rationale as binding. [[sources/cursor--plugins-pstack#RE10]], [[sources/cursor--plugins-pstack#RE14]]

## Timeline

- 2026-10-24 — Extracted this research contract from pstack’s How/Why workflow and adjacent comparison/review skills at the pinned source revision. Evidence is source policy; no agent-quality experiment was run. [[sources/cursor--plugins-pstack#RE01]], [[sources/cursor--plugins-pstack#RE08]], [[sources/cursor--plugins-pstack#RE22]]

## Related

- [[artifacts/plugins/pstack]] — the runnable skill collection containing these procedures and the complete extraction ledger.
- [[creators/lauren-tan]] — creator catalog entry for the source.
- [[concepts/artifact-centered-agent-context]] — gives research a durable handoff surface; this concept specifies the evidence distinctions that handoff should preserve.
- [[concepts/review-cost-aware-workflows]] — research can make later decisions easier to review, while its own coverage cost must fit the decision.
- [[concepts/completion-contract]] — specifies when an autonomous objective is done; this concept specifies what an investigation may responsibly claim.
- [[patterns/behavioral/diarization]] — both synthesize heterogeneous evidence, but this workflow does not implement a persistent subject dossier, append-only subject timeline, or holder-aware belief store.
- [[concepts/imitation-vs-correctness-eval]] — separates appearing like an accepted answer from independently satisfying a correctness signal; research fluency and model agreement are similarly insufficient proxies.

## What we'd steal

- ★ **Give mechanics, historical intent, impact, and teaching separate entry points.** Their evidence requirements differ even when they concern the same code. [[sources/cursor--plugins-pstack#RE01]]
- **Start narrow when the question is narrow.** Use one investigator for a single module and fan out only when distinct angles buy coverage. State an interpretation rather than stalling on minor ambiguity. [[sources/cursor--plugins-pstack#RE02]]
- **Make exploration output inspectable.** Return components, control/data flow, files read, boundaries, surprising behavior, and unanswered questions. [[sources/cursor--plugins-pstack#RE03]]
- **Explain the working model before the file inventory.** Keep optional concepts and gotchas only when they help someone begin work. [[sources/cursor--plugins-pstack#RE04]]
- ★ **Anchor a historical question to the precise code and lineage.** Include symbols, line ranges, blame, rename-aware history, PR discussions, linked tickets, and co-changed files. [[sources/cursor--plugins-pstack#RE05]]
- ★ **Publish coverage alongside findings.** Separate searched-and-empty, unavailable, expired, and explicitly skipped; state the query/window that supports each negative result. [[sources/cursor--plugins-pstack#RE06]], [[sources/cursor--plugins-pstack#RE12]]
- **Give each investigator one evidence owner.** Follow same-source links deeply and return cross-source leads for a deliberate handoff. [[sources/cursor--plugins-pstack#RE07]]
- **Collect evidence before composing the final explanation.** Preserve author, date, precise location, quotes or accurate paraphrases, relevance, and alternative readings. [[sources/cursor--plugins-pstack#RE07]]
- ★ **Carry confidence as data through every rewrite.** An editor may simplify language without upgrading an inference into a fact. [[sources/cursor--plugins-pstack#RE08]], [[sources/cursor--plugins-pstack#RE45]]
- **Separate evidence of intent from evidence of behavior.** A sensible implementation does not establish why its author chose it. [[sources/cursor--plugins-pstack#RE09]]
- ★ **Try to falsify the favored account.** Ask what would look different if it were wrong, and treat the user’s hypothesis as one candidate. [[sources/cursor--plugins-pstack#RE09]]
- **Keep contradictions visible.** Recheck the underlying source where possible; otherwise retain both readings and what could distinguish them. [[sources/cursor--plugins-pstack#RE03]], [[sources/cursor--plugins-pstack#RE09]]
- **Read the artifact’s history, not just its title.** Follow ticket parents/duplicates, full threads, finalized documents, and changed scope; boilerplate is weak rationale. [[sources/cursor--plugins-pstack#RE10]]
- **Use source-specific questions.** Infrastructure, error tracking, product analytics, tickets, docs, and chat reveal different kinds of motivation. Add incident-shaped searches for defensive code. [[sources/cursor--plugins-pstack#RE11]]
- **Check instrumentation before interpreting a chart.** Logging changes, refresh lag, schema drift, retention, and duplicate events can imitate a behavioral trend. [[sources/cursor--plugins-pstack#RE12]]
- **Keep analytical queries bounded and reproducible.** Discover schemas, use exact windows, prefer typed/deduplicated models, poll running queries, and retain SQL with concise numeric results. [[sources/cursor--plugins-pstack#RE13]]
- **Treat AI diagnoses as leads.** Return to real events and traces before accepting a generated root cause. [[sources/cursor--plugins-pstack#RE14]]
- **Translate history into explicit change constraints.** Preserve / Change / Avoid / Risk is a useful planning handoff, with current applicability checked separately. [[sources/cursor--plugins-pstack#RE14]]
- **Separate read access from write authority.** A research worker should not need mutation powers merely to query a connector. [[sources/cursor--plugins-pstack#RE15]]
- **Compare genuinely different designs.** Shared grounding and isolated output locations help preserve candidate differences before synthesis. [[sources/cursor--plugins-pstack#RE18]]
- **Define success criteria before judging candidates.** Score each criterion, inspect all candidates, and compare rationales; do not let holistic taste silently become the rubric. [[sources/cursor--plugins-pstack#RE22]]
- **Choose a coherent base instead of averaging alternatives.** Port only useful ideas, retain their provenance, and reframe if divergence reveals an underspecified task. [[sources/cursor--plugins-pstack#RE23]]
- **Keep failed candidates and verification visible.** A dropout changes the evidence available; the synthesis note should say so. [[sources/cursor--plugins-pstack#RE24]]
- **Allow no findings and unsupported outcomes.** Empty review is valid. A concrete reachable path matters more than a hypothetical complaint. [[sources/cursor--plugins-pstack#RE26]]
- **Retain minority concerns with reasons.** Act on, Consider, Noted, and Dismissed make the lead’s judgment auditable without turning votes into truth. [[sources/cursor--plugins-pstack#RE27]]
- ★ **Escalate decisive safety claims toward an experiment.** Record whether the claim is asserted, cited, path-checked, executed, or reproduced; say unproven when the needed level is unavailable. [[sources/cursor--plugins-pstack#RE47]]

## Open questions

- Can a structured claim ledger distinguish source existence, entailment, credibility, and source independence without imposing excessive authoring cost?
- How should a caller choose the cheapest sufficient source coverage for a consequential decision, and measure whether another source changes the answer?
- Which phrasing or output checks catch real confidence inflation rather than rewarding cosmetic hedges?
- Do cross-family judges find additional supported defects after controlling for additional tokens and repeated sampling from one model?
- What should expire or trigger revalidation when historical rationale becomes a standing design constraint?
