---
domain: projects
type: discovery-brief
status: proposed-refinement
last-reviewed: 2026-11-02
---

# Conversation classification — finding the unknowns

**Operation: QUERY, with a revised reclassification brief.** User requested the finding-unknowns skill before the authorized reclassification. This pass inspects the existing contract, protocol, pilot and canonical extracted records; it does not assign new corpus labels. The revised work order below preserves the earlier authorization while identifying which judgments need calibration.

## Framing and evidence

The apparent task is to classify specific requirements versus exploration. The evidence calls for reconstructing **how decisions became established, what information the agent had, and what each exchange accomplished**. A failure-only taxonomy would miss useful discovery and would confuse new information, changed decisions, user preference and execution errors.

**Count line: 6 landmines · 4 missing concepts · 5 open questions.** These are discovery findings, not measured incident frequencies.

Verified means supported for the stated local scope; inference means a proposed interpretation or design; question means unresolved. Primary evidence remains private. Wiki anchors below identify captures; canonical review annotations retain item-level locators and their limitations. This discovery uses those existing observations, not a fresh independent verification of every historical event.

### Known knowns

- **Verified:** 498 chats were reviewed with eight documented source gaps. Existing annotations are model-authored, human-unreviewed, private-analysis-only and training-ineligible. [[projects/conversation-learning/runs/all-chats-20261102/README]]
- **Verified local structure:** reading `interventions.jsonl` yields 786 message-linked candidates, all with top-level `context_cutoff: null` and `desired_target: null`. The source fields comprise 737 `interventions` and 49 `observed_agent_corrections`. This is not 786 independently verified human corrections. Reading `lessons.jsonl` yields 640 chat-level candidates. Some parent annotations contain richer evidence and repair locators; unset normalized fields do not mean the private source cannot supply them. Reproduce with the canonical view builder and inspect its output; these are a dated audit of current files, not permanent corpus statistics. [[projects/conversation-learning/runs/all-chats-20261102/learnings]]
- **Verified:** the contract already specifies authorship, uncertainty, review provenance, context cutoffs, allowed uses, task grouping and independent acceptance/correctness/outcome fields. The problem is incomplete population and inconsistent annotation granularity, not absence of every useful concept. [[projects/conversation-learning/data-contract]] [[projects/conversation-learning/review-protocol]]

### Weakest quadrants

- **Known unknowns:** opening-intent clarity, exploration share, true decision-time context, exact targets and sustainable review burden have not been measured consistently.
- **Unknown knowns:** the user may recognize implicit business priorities, audience expectations or reasons for reconsideration that the transcript never states. These need a few concrete cases to react to, not inferred mind-reading.
- **Unknown unknowns:** model-led changes to the user's goal, unobserved successful work, repeated continuations, context delivery gaps and historical instruction conflicts can distort apparently straightforward labels.

## Six landmines

| Blindspot | Evidence and status | Hard-way consequence | Sentence to add to the revised request |
| --- | --- | --- | --- |
| Later clarity gets backdated into the initial request | **Verified observation:** the SOW pilot contains later approval clarification, user-origin numerical terms and reconsideration of a disclosed change. [[sources/codex--commercial-redline-pilot#operational-intent]] [[sources/codex--commercial-redline-pilot#commitment-evolution]] | Legitimate adaptation becomes a false instruction-violation example. | “For each requirement, cite its earliest supported establishment and any later superseding decision; judge the action using the state active then.” |
| Available somewhere is confused with available to this agent | **Verified capture limitation:** hidden instructions, prior chats, artifacts and tool payloads are not uniformly captured. **Inference:** failures of delivery, retrieval and use need separate labels. [[projects/conversation-learning/data-contract]] [[projects/conversation-learning/runs/all-chats-20261102/README]] | A retrieval or context-delivery problem is attributed to reasoning, or a missing prompt is silently invented. | “Distinguish present in the captured decision context, available through an evidenced retrieval route, not yet supplied, and unknown; do not infer actual model attention.” |
| Human response is treated as correct gold | **Verified observation:** model-authored grades were later described as human-reviewed; the contract preserves disagreement and independent correctness. [[sources/codex--conversation-corpus-20261102#C0221]] [[projects/conversation-learning/data-contract]] | Sycophancy, human mistakes or model reviews become desired behavior. | “Separate who supplied feedback, whether it was accepted, and whether its factual correctness was independently supported.” |
| Productive evolution and model-induced drift look alike | **Verified observations:** planner requirements evolved; messaging architecture displaced an immediate milestone while later audience policy genuinely changed. **Inference:** record who proposed each change and what authorized it. [[sources/codex--conversation-corpus-20261102#C0132]] [[sources/codex--conversation-corpus-20261102#C0472]] | Co-design is punished, or an agent's unsupported expansion is credited as user intent. | “Track proposal origin, decision status, tradeoff explanation and authorization independently; goal clarity does not authorize every action.” |
| Counted annotations masquerade as rates or independent examples | **Verified local structure:** extraction includes agent corrections and chat-level lessons; related and duplicated chats have only provisional grouping. [[projects/conversation-learning/runs/all-chats-20261102/README]] [Task-family ledger](runs/all-chats-20261102/task-families.jsonl) | Long correction-heavy tasks dominate; the denominator excludes smooth success; duplicated tasks leak across splits. | “Name the counting unit, review window, selection rule and family relationship; do not calculate a failure or exploration rate from selected interventions alone.” |
| A reported fix or last message becomes terminal success | **Verified observations:** fixes recur, passing reruns hide earlier failures, and local/released/installed states differ. [[sources/codex--conversation-corpus-20261102#C0136]] [[sources/codex--conversation-corpus-20261102#C0482]] | Training rewards confident completion language instead of durable recovery. | “Keep repair attempt, observed verification, later recurrence and terminal observation separate; an unfinished capture is censored, not automatically failed.” |

## Four missing concepts to make explicit

These are **proposed annotation concepts**, grounded extensions to the existing contract; not new confirmed wiki patterns.

1. **Decision establishment.** A suggestion, acknowledged constraint, chosen tradeoff, approval, waiver and executed action are different events. Record issuer and scope. Silence and a preselected option do not establish approval. A human can accept one artifact property while leaving the wider task unaccepted. [[sources/codex--conversation-corpus-20261102#C0136]]
2. **Contribution to discovery.** Record whether an exchange supplied a useful option, exposed a tradeoff, elicited a constraint, created a testable example, resolved a question, or repeated established information. Progress needs visible evidence; length and politeness cannot establish it. The SOW and planner observations motivate measuring collaborative discovery rather than just compliance. [[sources/codex--commercial-redline-pilot#communication]] [[sources/codex--conversation-corpus-20261102#C0132]]
3. **Justified disagreement and justified abstention.** The model may appropriately challenge a premise or stop at an actual authority boundary. Safe behavior, user satisfaction, task completion and factual correctness remain independent. This prevents training the agent to agree with every objection or bypass every blocker. [[sources/codex--commercial-redline-pilot#successful-controls]] [[sources/codex--conversation-corpus-20261102#C0221]]
4. **Recurrence versus transfer.** A repair succeeding locally differs from the same mechanism being handled on its next occurrence. Link repeated cases while preserving task-family dependence and changed environments. Do not count an explanation of the rule as adoption of the rule. [[sources/codex--conversation-corpus-20261102#C0136]]

## Proposed classification: a small core with conditional detail

Do not require every label on every message. Use three units: **task/episode**, **phase** and **decision/intervention**. Store relation edges rather than copying the same fact into every row. “Mixed” is allowed, but should identify which part is exploratory and which is committed. Unknown requires a reason. An absent annotation means not assessed, not no problem.

### Core fields for the second pass

| Axis | Proposed values or structure | Why it earns its review cost |
| --- | --- | --- |
| Phase purpose | explore options; develop requirements; plan; execute; diagnose; evaluate/review; mixed; unknown | Exploration/execution alone misses diagnosis and reviewing, which have different success criteria. |
| Clarity by dimension | objective, deliverable, audience, constraints, success criterion, action authority: explicit / inferred / unresolved / conflicting / outside captured context | A clear outcome can coexist with unknown means or no authority to publish. Avoid one misleading clarity score. |
| Human contribution | reaffirm known requirement; clarify ambiguity; add fact; add requirement; change/waive decision; express preference; approve/reject; ask/probe; other; unknown | Multi-label spans prevent new information being treated as correction. |
| Decision provenance | proposer; establishment event; active interval; acknowledged-by-agent event if observed; supersedes; scoped authorization | Shows what was settled and when without backdating intent. |
| Information state | captured at cutoff; evidenced retrieval route available; supplied later; inaccessible; unknown | Separates missing information, missed retrieval and failure to use available information. Actual attention remains unobserved. |
| Observed response and result | helpful discovery; follows established state; conflicts with established state; unsupported assumption/expansion; justified challenge; unresolved; evidence and verification class | Allows positive and negative learning without forcing causal blame. Preserve existing acceptance/correctness/outcome fields. |

### Conditional extensions

| Add when relevant | Fields | Evidence motivating it |
| --- | --- | --- |
| Clarifying questions and autonomy | what was asked; decision it would change; whether already answered; authorized next action; observed resolution | Premature handbacks and overlooked access routes recur; inquiry can also resolve real ambiguity. [[sources/codex--conversation-corpus-20261102#C0492]] |
| Repair and recurrence | repair revision; verification evidence; later recurrence edge; changed environment; unresolved remainder | Passing repairs did not always persist. [[sources/codex--conversation-corpus-20261102#C0136]] |
| Transfer and taste | preference owner; audience/domain/artifact scope; explicit generalization; known exceptions | Directness, visual density and creative intent are scoped, not universal correctness. [[sources/codex--conversation-corpus-20261102#C0426]] [[sources/codex--conversation-corpus-20261102#C0101]] |
| Operational consequence and effort | reversibility; requested versus actual side effect; observed rework; measured costs with scope; effort unknowns | UI actions can mutate state; planned spend and measured cost differ. Do not infer severity or active labor from frustration or elapsed duration. [[sources/codex--conversation-corpus-20261102#C0449]] [[sources/codex--conversation-corpus-20261102#C0221]] |

Existing evidence/access/author/review metadata are prerequisites, not optional extra classifications. Root-cause attribution and ideal behavior remain separate hypotheses requiring their own evidence or synthetic-target labels.

## Instances the rubric must handle

| Instance | Treatment |
| --- | --- |
| One message both corrects and adds scope | Split claims/spans; retain multiple contribution labels. |
| Goal explicit, implementation deliberately open | Execute the goal through exploration; do not call openness an unclear request. |
| Two constraints conflict | Preserve both issuers, timing and unresolved priority; do not silently choose one as the real intent. |
| User changes mind after a useful explanation | Credit discovery; supersede the decision without labeling the earlier authorized action a violation. |
| Agent proposes an option, user accepts | Record agent-origin proposal and human decision; acceptance alone does not prove factual correctness. |
| Agent leads user into unnecessary complexity | Record proposal/decision sequence and evidence; manipulation or causal influence is not inferred merely from ordering. |
| User is mistaken or tests a premise | Preserve the objection and supported disagreement; do not manufacture a preferred wrong answer. |
| A repeated instruction was in a file but not in capture | Record retrievability and capture limits; do not assume the model saw it or excuse a demonstrably missed retrieval. |
| Permission, preference and business goal differ | Keep them separate; authorization for a draft is not authorization to send. |
| Human role is an automation envelope or tool wrapper | Preserve transport role and actual/unknown authorship; do not count it as direct human feedback. |
| Visual/audio quality cannot be checked from text | Record modality gap; “looks right” from an agent report does not establish it. |
| Quiet success, abandonment or no reply | Sample quiet work; preserve unknown outcome and possible capture censoring. Silence is not acceptance. |
| Correct repair later regresses | Keep both outcomes and a recurrence relation. |
| Tool/provider failure with good agent recovery | Evaluate environment failure and agent response separately. |
| A necessary experiment fails | Record hypothesis, bounded authorization and information gained; failure of the experiment is not automatically poor collaboration. |
| Same task spans chats, branches or models | Preserve chronology, family membership and config unknowns; do not count independent evidence or assign different splits by chat alone. |

Grounding for these edge cases is the pilot's changing-decision timeline and the corpus's transport, recurrence, evaluation and task-family findings. Unobserved motives and counterfactual outcomes remain questions, even where a label would be convenient. [[projects/conversation-learning/pilots/commercial-redline-001/README]] [[projects/conversation-learning/data-contract]] [Task-family ledger](runs/all-chats-20261102/task-families.jsonl)

## Five open questions

1. **Which unwritten expectations are stable?** The user can adjudicate ambiguous examples about commercial priorities, tone and autonomy. Do not retroactively make a newly stated preference an original explicit instruction.
2. **What decision-time context is reconstructible?** Some exact prompts, prior chats, artifacts, media and model/config versions may be unavailable. Preserve unknowns and replay-ineligibility instead of recreating plausible history.
3. **Can annotators distinguish clarification from changed requirements reliably?** Model disagreement can locate hard cases but is not independent human validation. Measure agreement on defined units and retain disagreements; no reliability result exists yet.
4. **What is the denominator for “how much”?** Share of tasks, phases, human turns, elapsed time and intervention types answer different questions. Use chat-level summaries only as a derived view; active-time share remains unknown without measurement.
5. **Which use justifies deeper annotation?** Harness diagnosis, personalized preferences, supervision targets and evaluation require different evidence. A provider-format export cannot substitute for this decision. No new permission for training or publication is inferred.

No answer is required to complete this discovery. The first calibration can proceed under explicit unknowns; unresolved intent stays unadjudicated rather than blocking all other records.

## Make the data more valuable before making it larger

**Proposed priorities, not measured improvements:**

1. **Reconstruct decision windows first.** Link the active requirement, exact action/output, feedback and repair with a decision-time boundary. A message locator alone is not an example the model can be trained against.
2. **Include productive exploration and quiet successes.** Select windows from whole phase timelines, not only existing intervention candidates. Record selection probability where random sampling is used; do not call a deliberately varied calibration sample representative.
3. **Use matched contrasts.** Find similar decisions where a question helped versus delayed work, or an assumption worked versus broke a known constraint. Preserve differing context; do not pretend unrelated contexts are preference pairs.
4. **Preserve negatives and unresolved cases.** “No supported violation,” “human changed the decision” and “insufficient context” are useful labels. Do not force a lesson from every window.
5. **Calibrate labels on actual boundary cases.** Start with a proposed 24-window development sample across commercial drafting, product/design, engineering, operations and creative work; include quiet successful windows and at least some uncertain cases. This sample size is a workflow choice, not a statistical sufficiency claim. Review ambiguity by evidence, not majority vote among models.
6. **Make the second pass additive and revisioned.** Keep first-pass observations immutable at their cited revision; add new phase/decision annotations with `supersedes` links for changed interpretations. Bind annotations to capture and rubric hashes. No silent rewriting of the completed run.
7. **Keep causal and training claims behind stronger gates.** A reported improvement is not an experiment. Same-context alternatives need actual comparisons or explicit synthetic origins. Link future interventions to prospective outcomes where authorized; reserve later unseen task families before remedy development because this corpus has already informed the taxonomy.
8. **Measure review usefulness.** Track adjudication burden, unresolved fields and examples eligible for a specific permitted use. Label count alone is not a value metric. Configuration/model metadata supports descriptive comparisons only unless task and context differences are addressed.

## Revised request and work order

> Add a versioned second-pass annotation layer to the frozen accessible-chat corpus. Preserve original evidence, first-pass findings, private-source boundaries and existing use restrictions. Classify task phases and decision/intervention windows using the six core axes above; apply conditional extensions only where supported. For every violation judgment, cite the requirement's establishment, the action cutoff, information state and actual response. Distinguish discovery, clarification, added facts, changed decisions, preferences and justified disagreement from missed requirements. Include successes, necessary experiments and unresolved cases. Reconstruct exact decision windows before writing targets; unknown context remains unknown. Start with the SOW pilot and a deliberately varied 24-window development calibration sample, document adjudication disagreements, then apply the stable rubric across all reviewable chats with a coverage ledger. Report phase and task distributions with explicit units and limitations; never use intervention totals as a denominator. Keep all results model-authored/unreviewed until actually adjudicated. Training, public release and behavioral-improvement claims remain outside this classification pass.

**Accepted:** reclassification is authorized; preserve existing data; distinguish exploration from execution; source boundaries and permissions persist.

**Proposed:** six-axis core, conditional detail, 24-window calibration and phase-first distributions. No claim that the user has approved each proposed rubric choice.

**Work order:** freeze/hash first-pass annotation revision → define evidence-bound label rules and examples → reconstruct pilot/calibration windows → record model labels and ambiguity → obtain human adjudication where intent cannot be established → revise rubric/version affected annotations → classify remaining reviewable phases → validate provenance and report bounded distributions.

**Stop points:** stop an individual violation claim when the active requirement or context cannot be established; stop a training-target claim without a trustworthy target; stop publication/export without its own permission gate. Continue independent source-supported classification rather than manufacturing certainty or blocking the whole corpus. User review is required to call a disputed intent interpretation human-adjudicated, not to begin authorized model annotation.

## Related

- [[projects/conversation-learning/README]]
- [[projects/conversation-learning/data-contract]]
- [[projects/conversation-learning/review-protocol]]
- [[projects/conversation-learning/runs/all-chats-20261102/learnings]]
