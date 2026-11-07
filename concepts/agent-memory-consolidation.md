---
domain: concepts
type: concept
name: agent-memory-consolidation
creators:
  - "[[creators/anthropic]]"
sources:
  - "[[sources/anthropic--components-of-agent-memory]]"
  - "[[sources/anthropic--agent-memory-support]]"
status: emerging
last-reviewed: 2026-11-07
popularity-signals:
  - signal: other
    value: Anthropic primary research article published 2026-11-06
    as-of: 2026-11-07
    source: "[[sources/anthropic--components-of-agent-memory#root]]"
---

# agent-memory-consolidation

> Preserve experience as evidence; turn selected observations into tested, discoverable knowledge; inject only a small useful index, and evaluate the effect on future work.

## What it is

An external-memory architecture with four distinct layers: raw transcripts, in-session memory notes, compiled representations such as a linked wiki, and a small injected context. Background consolidation—called dreaming here—can verify, correct, reorganize and promote information between those layers. It is not merely a bigger context window, compression of the current conversation, or an update to model weights. The important unit is a **claim with provenance, relevance and a future use**, not a file count. [[sources/anthropic--components-of-agent-memory#layers]] [[sources/anthropic--components-of-agent-memory#learning-loop]]

This page specializes [[concepts/artifact-centered-agent-context]]: that page owns task handoffs and standing guidance; this one owns learned-memory selection, offline consolidation, retrieval comparisons and adoption/consistency limits. [[concepts/trace-lake]] owns searchable execution evidence and eval generation. No new generic memory pattern is proposed.

## Where it came from

Anthropic's November 6, 2026 research report, read November 7 with all fifteen figures and supporting product docs/examples. The article credits prior sleep-time compute and the LLM-wiki idea; it does not originate all external memory. Google's linked Sleep system changes model weights, so identical terminology is not an identical architecture. [[sources/anthropic--components-of-agent-memory#root]] [[sources/anthropic--agent-memory-support#sleep-contrast]]

## Why it matters

Memory can compound knowledge **or compound a mistake**. An incorrect note may persist after its original context disappears, and promotion can repeat it in every new session. Too much writing also competes with doing the task. The system must distinguish evidence retention, useful interpretation, discoverability, adoption and actual improvement. Raw search remains valuable even after a wiki exists. [[sources/anthropic--components-of-agent-memory#salience]] [[sources/anthropic--components-of-agent-memory#correction]] [[sources/anthropic--components-of-agent-memory#wiki-search]]

## Architecture and ownership

| Layer | Job | Failure to watch |
| --- | --- | --- |
| Transcripts | Retain observations, actions and outcomes for later inspection | Agent narration or tool errors mistaken for ground truth |
| Notes | Capture useful learned rules, plans and corrections while working | Untested guesses, redundant volatile state, endless housekeeping |
| Representation | Join facts, expose conflicts and map relevant relationships | Lossy summaries, missing facts, collisions and invented links |
| Injected context | Put a small index/high-value lesson in every fresh session | Stale or malicious note becomes pervasive; useful detail falls past load limit |
| Consolidation | Check lower-level evidence, restructure and propose/adopt updates | Cost without downstream gain; partial output mistaken for completed knowledge |

This is a synthesis of the article taxonomy and captured lifecycle docs, not a new implemented engine. [[sources/anthropic--components-of-agent-memory#layers]] [[sources/anthropic--components-of-agent-memory#correction]] [[sources/anthropic--components-of-agent-memory#injection]] [[sources/anthropic--agent-memory-support#dream-lifecycle]]

## Evidence & claims

### 1. Memory quality and reading behavior differ by model

The CL-Bench database task gives correct-answer feedback after each question and starts each question in a fresh session except the shared directory. Figure 3 reports mean rewards:

| Model | Stateless | With memory |
| --- | ---: | ---: |
| Opus 5.5 | 0.655 | 0.838 |
| Sonnet 5.5 | 0.644 | 0.833 |
| Opus 5 | 0.564 | 0.828 |
| Opus 4.7 | 0.383 | 0.700 |
| Sonnet 5 | 0.306 | 0.610 |
| Sonnet 4.6 | 0.330 | 0.364 |

These are **one task**, not overall CL-Bench rankings. The external benchmark release body was not recovered. Figure 5's Sonnet 4.6 instruction intervention raises 0.364 to 0.641 by asking it to read memory and test hypotheses; three runs/condition, standard-deviation bars. Failure-only memory restrictions reduce the gain for Opus 5 and 4.7; that panel uses standard-error bars and unequal run counts. Neither result implies that every model should receive the same memory prompt or that deterministic policy can be removed. [[sources/anthropic--components-of-agent-memory#database-results]] [[sources/anthropic--components-of-agent-memory#steering]] [[sources/anthropic--agent-memory-support#incomplete-context]]

### 2. Salience is not archival completeness

One run each near 10,000 Pokemon actions: Sonnet 3.7 produces 413 files and one badge; Fable 5 produces ten including its index and four badges. The larger folder repeatedly reorganizes redundant game state; the smaller one emphasizes goals, plans and learned strategies. Model capability and memory policy both differ, so this is not causal proof that fewer files produce better play. The Magikarp timing anecdote is a stored heuristic, not a demonstrated game mechanic. [[sources/anthropic--components-of-agent-memory#salience]]

### 3. Correction needs observations, not confidence

A wrong PokeCenter location yields a false Mt. Moon completion note, then repeated backtracking. Consolidation revisits the transcript and corrects the note; the shown run reaches the next city at action 1935. The lesson is to reopen the evidence that can falsify a note. A transcript can contain both observation and mistaken narration; it is not automatically truth just because it is raw. [[sources/anthropic--components-of-agent-memory#correction]]

### 4. Keep the search baseline and the cost denominator

Stainless experiment: ~350k files/~420M tokens, 25 questions, Opus 5, two to 128 consolidation sessions. Wiki-only meets 13→48% of graded criteria; **search alone is 53%**. Hybrid wiki+search rises 54→61%, eight percentage points above that search baseline at the endpoint. Reported online savings are ~20k tokens/question. Figure 10's 2M–128M axis is **allocated budget (1M/session), not measured spend**; it cannot support a cash-cost or break-even calculation. More graph links do not validate facts. [[sources/anthropic--components-of-agent-memory#wiki-search]] [[sources/anthropic--components-of-agent-memory#compute-budget]]

### 5. A wiki must match the downstream question

On the merger task's multi-document and/or judgment/arithmetic items, wiki 87% versus search 73%; not an all-LAB score. A largely single-document LAB task shows no clear gain; a separate ten-document/115 KB corpus grows into a 203 KB wiki. Figure 11's dependency labels are model-assigned. These results support evaluating retrieval workload and abstraction value, not generating a wiki for every collection. [[sources/anthropic--components-of-agent-memory#task-fit]] [[sources/anthropic--components-of-agent-memory#expansion]]

### 6. Concurrency and representation can destroy exact facts

Shared summarized contract terms lose facts through overwrites; generated brief includes 41/57. Iterative prompt revision, one owner per contract page and verbatim term preservation jointly produce 57/57. The experiment changes multiple things, so cannot isolate their individual contribution. The separately pinned knowledge-wiki quickstart **accepts ~5% line loss on its busiest shared entity page**: similar branding is not the article's lossless ownership contract. [[sources/anthropic--components-of-agent-memory#goal-ownership]] [[sources/anthropic--agent-memory-support#quickstart-boundaries]]

### 7. Product surfaces have different consistency and adoption contracts

| Surface | What the captured docs say | What does not follow |
| --- | --- | --- |
| Built-in Dreams | Clone input into distinct output; explicit future adoption | A returned store ID, failed/canceled output or archival means validated completion |
| Dynamic dreaming cookbook | Custom analyzer/organizer workflow; nightly store updated in place | Automatic review, atomic update or complete historical-session coverage |
| Hosted Managed memory | Shared filesystem mounts; read-only control; versioned writes | Notes are correct, all history retained forever, or learned content has policy authority |
| Self-hosted memory | Periodically reconciled local copies; store wins conflicts | Tool write success means durable commit; read_only makes local files immutable |
| Messages memory tool | Client handles requested operations and owns storage | Tool declaration alone provides persistence, authorization or path containment |
| Claude Code auto memory | Machine-local index plus topic files; bounded initial injection | Every saved byte loads, propagates across hosts or disappears with transcript cleanup |

These are documentation-based distinctions, not runtime acceptance tests. [[sources/anthropic--agent-memory-support#dream-lifecycle]] [[sources/anthropic--agent-memory-support#dynamic-nightly]] [[sources/anthropic--agent-memory-support#store-access]] [[sources/anthropic--agent-memory-support#self-hosted-conflicts]] [[sources/anthropic--agent-memory-support#client-memory]] [[sources/anthropic--agent-memory-support#code-retention]]

## Patterns demonstrated

- [[patterns/behavioral/diarization]] — compile current understanding plus provenance and explicit history. [[sources/anthropic--agent-memory-support#dynamic-workflow]]
- [[patterns/behavioral/context-is-not-authority]] — stored or injected text remains learned input, not permission. [[sources/anthropic--agent-memory-support#dynamic-trust]] [[sources/anthropic--agent-memory-support#code-injection]]
- [[patterns/behavioral/evidence-gated-completion]] — output creation, worker completion, factual retention and downstream success need separate checks. [[sources/anthropic--agent-memory-support#dream-lifecycle]] [[sources/anthropic--components-of-agent-memory#goal-ownership]]
- [[patterns/behavioral/latent-vs-deterministic-split]] — model judges salience; storage preconditions and path checks enforce a separate contract. [[sources/anthropic--components-of-agent-memory#learning-loop]] [[sources/anthropic--agent-memory-support#store-versions]]
- [[patterns/composition/resolver-routing-table]] — concise injected index routes to detailed topic files. [[sources/anthropic--components-of-agent-memory#injection]]
- [[patterns/quality-bar/complexity-ratchet]] — merge duplicates and repair reachability without treating page/link growth as improvement. [[sources/anthropic--components-of-agent-memory#repair]] [[sources/anthropic--components-of-agent-memory#expansion]]

## Tensions & counter-arguments

- **Freedom versus reliable procedure:** capable models can be hurt by arbitrary content restrictions; older models needed explicit read/test guidance. Neither removes security enforcement or task-specific invariants. [[sources/anthropic--components-of-agent-memory#steering]]
- **Fast reuse versus changing reality:** notes lower repeated work but can fossilize stale state. Background updates trade online attention for cost and a lag before new experience is usable. [[sources/anthropic--components-of-agent-memory#open-questions]] [[sources/anthropic--components-of-agent-memory#salience]]
- **Abstraction versus exactness:** a synthesis is useful only if it preserves the facts needed for its task. Contract terms may demand source-exact detail even where ordinary summaries suffice elsewhere. [[sources/anthropic--components-of-agent-memory#goal-ownership]]
- **Source retention versus privacy:** derived memory can outlive transcripts; historical versions and notebook exports need their own deletion/redaction policies. Read-only protects some mutations, not the reader from poisoned content. [[sources/anthropic--agent-memory-support#code-retention]] [[sources/anthropic--agent-memory-support#store-versions]] [[sources/anthropic--agent-memory-support#dynamic-nightly]]
- **No universal dreaming guarantee:** external-context consolidation, weight-based learning, built-in clone-and-adopt and nightly in-place workflows differ materially. The name is not a contract. [[sources/anthropic--agent-memory-support#sleep-contrast]] [[sources/anthropic--agent-memory-support#dream-lifecycle]] [[sources/anthropic--agent-memory-support#dynamic-nightly]]
- **Evaluation leakage remains a question:** task-specific instruction iteration is valuable but not held-out evidence of generalization. The report does not establish that a revised wiki recipe transfers unchanged to unrelated corpora. [[sources/anthropic--components-of-agent-memory#goal-ownership]]

## Timeline

- 2026-11-06 — Anthropic publishes the four-layer memory account and illustrative evaluations. [[sources/anthropic--components-of-agent-memory#root]]
- 2026-11-07 — Ingested the complete article/figures, documented product contracts and selected supporting examples; no memory system installed or live store altered. [[sources/anthropic--agent-memory-support#root]]

## Related

- [[concepts/artifact-centered-agent-context]] — explicit task artifacts versus generalized learned knowledge.
- [[concepts/trace-lake]] — retained execution evidence can support correction and recurring evals.
- [[concepts/evidence-calibrated-research]] — claims, sample sizes, comparison conditions and omitted evidence.
- [[concepts/compound-engineering]] — learning must change future work, not only accumulate pages.
- [[concepts/agent-api-learning-and-evolution]] — validate portable procedural knowledge before reuse.
- [[concepts/lifelong-skill-routing]] — a useful item that cannot be selected is functionally absent.
- [[concepts/agent-habitat-architecture]] — independent boundaries around untrusted learned context.
- [[concepts/durable-agent-execution]] — storage durability does not imply complete or replay-safe execution.
- [[artifacts/plugins/gbrain]] — existing wiki/distillation machinery; no claim these experiments benchmark it.

## What we'd steal

Portable judgments below are our synthesis of the cited evidence, not claims every mechanism was implemented or experimentally isolated.

1. **★ Give each memory layer a distinct job.** Keep raw evidence, provisional notes, compiled knowledge and injected context separately inspectable. [[sources/anthropic--components-of-agent-memory#layers]]

2. **★ Save a rule with how it was established.** Turn feedback into a tested hypothesis, provenance and known traps; do not promote guesses as settled knowledge. [[sources/anthropic--components-of-agent-memory#learning-loop]]

3. **Diagnose retrieval before adding more memory.** Observe whether agents read existing notes and use them before expanding the store. [[sources/anthropic--components-of-agent-memory#steering]]

4. **Adapt guidance to the observed model failure.** Read/test prompts helped the weaker model; failure-only restrictions hurt stronger ones. Re-evaluate after model changes. [[sources/anthropic--components-of-agent-memory#steering]]

5. **Prefer durable insight over observable state.** Keep strategy and non-obvious constraints; re-read fast-changing state from its authoritative system. [[sources/anthropic--components-of-agent-memory#salience]]

6. **Budget memory housekeeping against task progress.** Count tool steps and attention diverted into reorganizing notes, not just stored bytes. [[sources/anthropic--components-of-agent-memory#salience]]

7. **★ Correct from observation-level evidence.** Trace a suspected error back to actual actions/results; separate narration, inference and verified fact. [[sources/anthropic--components-of-agent-memory#correction]]

8. **Preserve conflicts rather than guessing a winner.** A later passing remark is not necessarily an authorized correction; retain dates, scope and both sources. [[sources/anthropic--agent-memory-support#dynamic-workflow]]

9. **Distinguish absence of support from contradiction.** One transcript failing to mention a fact does not invalidate evidence from another; downgrade when uncertainty is actually shown. [[sources/anthropic--agent-memory-support#dynamic-workflow]]

10. **Choose representation for the future task.** A personal assistant, contract reviewer and navigation agent need different schemas and levels of precision. [[sources/anthropic--components-of-agent-memory#goal-ownership]]

11. **Preserve exact terms when the answer depends on them.** Keep quantities, qualifiers, identifiers and source-exact contract language rather than a lossy universal summary. [[sources/anthropic--components-of-agent-memory#goal-ownership]]

12. **★ Make write ownership explicit.** Use disjoint pages or a proven merge protocol; reread-after-write instructions alone are not an atomic consistency guarantee. [[sources/anthropic--components-of-agent-memory#goal-ownership]]

13. **Separate concurrent enrichment from global reorganization.** Defer renames/merges until writers finish; copy, verify, redirect links, then retire old locations. [[sources/anthropic--agent-memory-support#dynamic-workflow]]

14. **Repair reachability after consolidation.** Resolve missing targets, merge duplicate topics and update indexes, then separately check claim entailment. [[sources/anthropic--components-of-agent-memory#repair]]

15. **★ Retain search alongside compiled memory.** Compare raw search, wiki-only and hybrid retrieval; the best reported configuration was hybrid. [[sources/anthropic--components-of-agent-memory#wiki-search]]

16. **Segment evaluation by question structure.** Distinguish single-document lookup from cross-document synthesis, judgment and arithmetic. [[sources/anthropic--components-of-agent-memory#task-fit]]

17. **Reject organization that has no retrieval value.** Measure whether the representation reduces future work, not whether it has more nodes or exceeds source size. [[sources/anthropic--components-of-agent-memory#expansion]]

18. **Separate budgets, spend and online savings.** Log actual construction/maintenance costs and amortized query costs; a token allowance is not a bill. [[sources/anthropic--components-of-agent-memory#compute-budget]]

19. **Carry trial counts and uncertainty with scores.** Keep task-specific versus aggregate scores, standard deviation versus standard error and uneven repeats visible. [[sources/anthropic--components-of-agent-memory#steering]]

20. **Test revised memory recipes on new tasks.** An in-task reflect/rebuild success is evidence of repair, not proof of transferable generalization. [[sources/anthropic--components-of-agent-memory#goal-ownership]]

21. **★ Keep injection small and navigational.** Promote high-value validated guidance; leave links to detail so every session does not pay for every memory. [[sources/anthropic--components-of-agent-memory#injection]]

22. **Verify loaded context, not just successful writes.** Claude Code can save an oversized index whose tail is never loaded; record the consuming surface and its actual limits. [[sources/anthropic--agent-memory-support#code-injection]]

23. **Treat promotion as a trust boundary.** A poisoned memory reaches more tasks when injected; a read-only consumer can still follow bad content. [[sources/anthropic--agent-memory-support#dynamic-trust]]

24. **Distinguish persistence from adoption.** Inspect a completed candidate store before attaching it to consumers; record which version/store a session used. [[sources/anthropic--agent-memory-support#dream-lifecycle]]

25. **Treat failed/canceled outputs as partial candidates.** A new store ID and plausible notes do not prove the consolidation finished. [[sources/anthropic--agent-memory-support#dream-lifecycle]]

26. **Separate cancel, archive and delete.** Cancellation can leave in-flight usage and partial data; archival preserves status/output and is not erasure. [[sources/anthropic--agent-memory-support#dream-cancellation]]

27. **Use scoped stores and explicit access modes.** Partition by purpose/tenant/lifecycle and choose read_only for reference consumers; do not rely on a writable default. [[sources/anthropic--agent-memory-support#store-access]]

28. **Use version preconditions for read-modify-write.** On a content hash mismatch, reread and reconcile; returning an old version to service is a new mutation. [[sources/anthropic--agent-memory-support#store-versions]]

29. **Design retention across raw and derived data.** Notes can outlive logs; redacting history, deleting current memory and purging exports are different operations. [[sources/anthropic--agent-memory-support#store-versions]]

30. **Budget store capacity and preserve required audit history.** Prune/split with provenance before limits block new writes; export history if the retention window is insufficient. [[sources/anthropic--agent-memory-support#store-lifecycle]]

31. **Keep client memory enforcement in the handler.** Validate canonical paths, reject root deletion and enforce secret/size controls; a tool name or prompt is not isolation. [[sources/anthropic--agent-memory-support#client-memory]]

32. **★ Verify durable memory after asynchronous sync.** Self-hosted write success can later lose to the remote store without an agent-visible error; inspect committed state. [[sources/anthropic--agent-memory-support#self-hosted-conflicts]]

33. **Separate remote read-only from local immutability.** Bash/custom tools can modify a self-hosted local copy even when upload is disabled; choose tool capabilities accordingly. [[sources/anthropic--agent-memory-support#self-hosted-conflicts]]

34. **Make shutdown and sync lag part of the contract.** Use per-session filesystems, retain store markers, stop workers gracefully and account for edits lost on abrupt kill. [[sources/anthropic--agent-memory-support#self-hosted-sync]]

35. **Prove the store is actually mounted.** A prompt can describe memory while a disabled worker never downloads it; test operational readiness separately. [[sources/anthropic--agent-memory-support#self-hosted-controls]]

36. **Observe deletion propagation before trusting it.** A log-only mode can expose proposed deletes; it does not disable other uploads or downloads. [[sources/anthropic--agent-memory-support#self-hosted-controls]]

37. **Use least-capability consolidation workers.** Keep shell/network/credentials out of file-only analysis; treating inputs as data is necessary but not a proof against poisoning. [[sources/anthropic--agent-memory-support#dynamic-trust]]

38. **★ Specify incremental-ingest completeness.** A creation-time watermark can skip unfinished sessions and later turns; retain pending IDs or overlap/reconcile windows as an adaptation. [[sources/anthropic--agent-memory-support#dynamic-nightly]]

39. **Make consolidation retries reconciliation-safe.** A failed in-place run may already have written memory; replaying its input window needs provenance/deduplication, not an assumption of no effects. [[sources/anthropic--agent-memory-support#dynamic-nightly]]

40. **Benchmark the actual example you plan to adopt.** Do not combine the article's 57/57 retention, the quickstart's price claims and Dreams' adoption lifecycle into one imaginary product guarantee. [[sources/anthropic--agent-memory-support#quickstart-boundaries]]

## What we'd apply here

Keep immutable source captures underneath mutable wiki judgment. Continue mechanical citation/link checks, and add a builder route that asks for raw-search/wiki/hybrid baselines plus measured construction and maintenance cost. Do not launch a dreaming cron or rewrite the whole wiki on the strength of this article. Promotion trigger: repeated cross-document questions with measurable retrieval/quality cost, a representative held-out set and demonstrated benefit over current search. This application specializes existing [[patterns/quality-bar/complexity-ratchet]] and [[patterns/behavioral/evidence-gated-completion]], not an installed agent-memory policy. [[sources/anthropic--components-of-agent-memory#wiki-search]] [[sources/anthropic--components-of-agent-memory#compute-budget]] [[sources/anthropic--components-of-agent-memory#task-fit]]

## Open questions

- How much gain survives held-out tasks, different corpora, models and access-control scopes?
- What is measured—not budgeted—construction plus maintenance cost, and the break-even workload?
- Which source changes invalidate which derived claims, and who can authorize their promotion?
- How do we detect poisoning that remains plausible through multiple consolidation passes?
- What consistency protocol prevents lost concurrent edits without throwing away useful cross-document synthesis?
- Can incremental session selection cover long-running/reopened sessions without excessive replay?

## Evidence boundary

**31 preserved evidence files** with URL/byte/hash receipts. Full article and fifteen figures read; supporting-doc scope and incomplete CL-Bench capture disclosed in the citation maps. Current docs and pinned README are separate evidence from the original research experiments. No memory API calls, benchmark replication, installed skills or production policy changes.
