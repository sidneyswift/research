---
domain: concepts
type: concept
name: trace-lake
creators: ["[[creators/ankur-goyal]]", "[[creators/braintrust]]"]
sources: ["[[sources/ankrgyl--trace-lake]]"]
status: emerging
last-reviewed: 2026-11-04
---

# Trace Lake

> **One-line:** Treat agent execution history as a reusable evidence corpus: search across runs, reproduce failures with their original context, and turn recurring findings into inexpensive regression evals.

## What it is

A Trace Lake combines retained execution records, interactive investigation and a production-to-evaluation loop. Its useful unit is not only a trace you can open, but a population you can query: which runs share a failure, what changed, and which evidence can become a rerunnable test? The article argues for fast ingest, full-text plus structured queries, economical storage and continuous analysis. Our distillation: observability compounds only when findings become durable checks, not merely dashboards or agent-written explanations. [[sources/ankrgyl--trace-lake#historical-corpus]] [[sources/ankrgyl--trace-lake#trace-to-eval]]

The boundary matters: a queryable record is not necessarily a replayable environment, and an observed tool sequence is not access to every internal model thought. Preserve emitted inputs, outputs, tool interactions and relevant application state; describe missing evidence explicitly. This is an adaptation of the article's reproduction requirement, not a claim that logging alone guarantees determinism. [[sources/ankrgyl--trace-lake#trace-to-eval]]

## Where it came from

[[creators/ankur-goyal]] framed the term in *The Trace Lake*, published November 3, 2026, from [[creators/braintrust]]'s product perspective. The linked architecture, Nitro and application-log posts describe the vendor's implementation choices; its living Topics, Patterns and Loop docs describe the investigation workflow. This ingest establishes this source's use of the term, not historical priority for the broader idea of learning from production traces. [[sources/ankrgyl--trace-lake#root]] [[sources/ankrgyl--trace-lake#brainstore-architecture]]

## Why it matters

It supplies the missing middle between “we saw a bad run” and “future changes cannot silently repeat it.” It also makes empirical review possible at useful scale: collect comparable cases, inspect the actual evidence, retain preconditions, then measure the failure cheaply. A domain coordinator can schedule those investigations, but the evidence corpus and the resulting evals must survive its conversation. That last separation is our synthesis with [[concepts/agent-control-plane]], not a claim that the two authors implemented the same system. [[sources/ankrgyl--trace-lake#trace-to-eval]] [[sources/ankrgyl--trace-lake#automation-contract]]

## Evidence & claims

- **Requirements, not universal SLOs:** the article proposes ingest under 10 seconds and query latency in hundreds of milliseconds. Its ~100,000 spans/sec and large-payload estimates motivate a particular workload; they are not measured requirements for every agent application. [[sources/ankrgyl--trace-lake#query-latency]] [[sources/ankrgyl--trace-lake#storage]]
- **Mechanism documented, not independently executed:** Brainstore separates durable object storage from compute, groups spans from one trace together, maintains multiple read indexes and merges fresh WAL data with compacted indexes. The architecture post also states freshness work is bounded by time/memory budgets. [[sources/ankrgyl--trace-lake#brainstore-architecture]]
- **Query grain is correctness:** `ANY_SPAN(A AND B)` requires one matching span; `ANY_SPAN(A) AND ANY_SPAN(B)` may match different spans. Trace summaries help aggregation but do not erase this distinction. [[sources/ankrgyl--trace-lake#trace-query-semantics]] [[sources/ankrgyl--trace-lake#filter-semantics]]
- **Discovery and measurement are different jobs:** Topics broadly classifies traces; Patterns deeply investigates selected cases; Loop schedules work. The docs explicitly say Topics and Patterns do not require each other. A known pattern can become a cheaper scorer, facet or monitor. [[sources/ankrgyl--trace-lake#topics]] [[sources/ankrgyl--trace-lake#patterns-verification]]
- **Vendor benchmark:** Nitro reportedly improved full-text search by >2× and other queries by 15% in a three-day A/B test exceeding one million queries, versus the prior Brainstore engine. This is distinct from selected slow-query tests and a synthetic cross-vendor comparison; one competitor wins the illustrated span-count aggregate. Neither proves universal superiority or a guaranteed latency. [[sources/ankrgyl--trace-lake#benchmark-scope]]
- **No operational validation here:** this ingest read the full article and eight linked primary pages; it did not run Brainstore, execute SQL, reproduce benchmarks, or validate the automatically generated findings. [[sources/ankrgyl--trace-lake#capture]]

## Patterns demonstrated

- [[patterns/quality-bar/complexity-ratchet]] — related mechanism: a production failure becomes a persistent eval instead of a recurring manual investigation. This article is design/product evidence, not a new independently tested artifact example. [[sources/ankrgyl--trace-lake#trace-to-eval]]
- [[patterns/behavioral/evidence-gated-completion]] — Patterns docs require evidence checks before saving/closing findings and preserve uncertainty when a check cannot run. Documentation-level comparison only. [[sources/ankrgyl--trace-lake#patterns-verification]]
- [[patterns/quality-bar/defect-derived-validation]] — related but not equivalent: runtime failures seed evals; the existing proposed pattern specifically mines maintainer fixes and backvalidates rules across a corpus. Do not promote it on the strength of this article. [[sources/ankrgyl--trace-lake#trace-to-eval]]

## Tensions & counter-arguments

- **Retention is a choice, not “keep everything forever.”** The article criticizes discarded evidence, while current hosted docs enforce retention windows and silently omit older data. Specify the investigation horizon and disclose coverage; absent query results are not proof a behavior never occurred. Privacy, deletion obligations and cost constrain the adaptation. [[sources/ankrgyl--trace-lake#retention-window]]
- **Storage residency is not inference residency.** Topics docs say even BYOC/self-hosted deployments call Braintrust-hosted endpoints, with stated Zero Data Retention and Baseten as a subprocessor. A product can keep stored traces in your cloud while sending data elsewhere for analysis. Inspect those boundaries independently. [[sources/ankrgyl--trace-lake#analysis-data-boundary]]
- **Correlations and classifier labels are leads, not verdicts.** Patterns docs disclaim causality from cohort differences and require raw evidence; missing data/failed queries should not close findings. Preserve representative successes and recoveries as well as failures to avoid an error-only picture. [[sources/ankrgyl--trace-lake#patterns-verification]] [[sources/ankrgyl--trace-lake#automation-contract]]
- **Historical inputs alone cannot reproduce external state.** Pre-action state and resource versions are explicit requirements. Our implementation implication: freeze or substitute external dependencies, isolate replay side effects, and record where stochastic behavior remains; do not claim byte-identical replay without testing it. [[sources/ankrgyl--trace-lake#trace-to-eval]]
- **Specialized database cost must be earned.** The vendor's architecture post describes a particular failed multi-backend stack and extreme workload. This does not establish that a small deployment needs a custom database. Adopt the capture→investigate→eval contract first; upgrade storage/indexing only when measured latency, volume or retention needs justify it. [[sources/ankrgyl--trace-lake#brainstore-architecture]]
- **Analysis can acquire lasting authority and cost.** Loop's Braintrust write-tool choices do not govern connected MCP tools. Created scoring rules can keep running after the parent automation is paused/deleted. Name external credentials, allowed writes and cleanup ownership separately. [[sources/ankrgyl--trace-lake#automation-authority]]

## Timeline (append-only)

- 2026-11-03 — Ankur Goyal publishes *The Trace Lake*, connecting trace retention, investigation and evaluations. [[sources/ankrgyl--trace-lake#root]]
- 2026-11-04 — Full article, SQL examples and eight linked primary pages ingested; vendor claims separated from portable principles and living-doc limitations. [[sources/ankrgyl--trace-lake#capture]]

## Related

- [[concepts/lifelong-skill-routing]] — prospective application: retain real misrouting queries, library versions and downstream outcomes as regression fixtures. Skill++ uses benchmark/synthetic probes; it does not evaluate a Trace Lake integration. [[sources/zhang--skill-plus-plus#metrics]]

- [[concepts/review-cost-aware-workflows]] — supplies actual behavior and rerunnable checks for verification-first review.
- [[concepts/compound-engineering]] — execution evidence compounds into future verification capability.
- [[concepts/agent-control-plane]] — persistent coordination can schedule investigations; it is not the evidence store.
- [[concepts/verification-model-fidelity]] — an eval must still represent the current implementation, state and intended behavior.
- [[concepts/imitation-vs-correctness-eval]] — reproducing observed output is not the same as proving it was correct.
- [[concepts/agentic-loop]] — the wider observe→investigate→verify cycle needs explicit scope and stopping conditions.

## What we'd steal

Portable design ledger; ★ marks the highest-leverage ideas. Concrete adaptations below are ours unless explicitly attributed.

1. ★ **Close the evidence loop.** Make every confirmed recurring failure point to a reproducible case and a focused regression eval, with the originating trace attached. [[sources/ankrgyl--trace-lake#trace-to-eval]]
2. ★ **Capture preconditions, not just the final answer.** Preserve input, relevant pre-action state and resource versions. As an implementation contract, also pin model/prompt/tool versions and record the expected behavior and observed failure. [[sources/ankrgyl--trace-lake#trace-to-eval]]
3. ★ **Search for a cohort before generalizing.** Retrieve similar executions, count distinct underlying conversations, inspect raw traces and check whether the failure recurred or recovered. A large cluster of duplicate spans is not many independent incidents. [[sources/ankrgyl--trace-lake#historical-corpus]] [[sources/ankrgyl--trace-lake#automation-contract]]
4. ★ **Use expensive discovery to create cheap monitoring.** Investigate broadly when necessary; once understood, move the recurring behavior into a narrow scorer/classifier/check rather than repeatedly paying for an open-ended agent investigation. [[sources/ankrgyl--trace-lake#trace-to-eval]] [[sources/ankrgyl--trace-lake#patterns-verification]]
5. **Set a searchable evidence horizon.** Record actual retention, sampling and missing intervals with investigation results; do not treat silently filtered history as negative evidence. [[sources/ankrgyl--trace-lake#historical-corpus]] [[sources/ankrgyl--trace-lake#retention-window]]
6. **Make discovery interactive for agents too.** Measure ingest-to-query visibility and query latency separately; support exact text searches alongside structured/nested filters. Choose targets from real investigation needs, not copied headline numbers. [[sources/ankrgyl--trace-lake#query-latency]]
7. **Name span, trace and conversation grain.** Keep identifiers explicit; distinguish same-span predicates from trace-wide existential predicates and group multi-turn conversations where a single trace is insufficient. [[sources/ankrgyl--trace-lake#filter-semantics]] [[sources/ankrgyl--trace-lake#topics]]
8. **Separate durable history from serving capacity.** Where scale warrants, let object storage grow independently of query workers; preserve tenant partitioning and colocate related spans for targeted reads. [[sources/ankrgyl--trace-lake#storage]] [[sources/ankrgyl--trace-lake#brainstore-architecture]]
9. **Keep write visibility independent of index completion.** The documented implementation merges unprocessed, processed and compacted records; bound the fresh-data work so freshness does not silently destroy latency. [[sources/ankrgyl--trace-lake#brainstore-architecture]]
10. **Budget I/O and CPU separately.** Nitro's portable mechanism is separate concurrency limits, coalesced/prefetched reads and cheap selective checks before expensive work—not simply increasing worker count. [[sources/ankrgyl--trace-lake#nitro]]
11. **Split broad classification from deep investigation.** Use coarse themes to choose candidates, then inspect evidence; do not make either stage a mandatory dependency if a known failure can be queried directly. [[sources/ankrgyl--trace-lake#topics]] [[sources/ankrgyl--trace-lake#patterns-verification]]
12. **Correlate operational logs with agent actions.** Preserve trace context, error/retry details and message templates so an infrastructure failure can be distinguished from the agent's response to it. [[sources/ankrgyl--trace-lake#application-logs]]
13. **Give scheduled investigations a contract.** Pin time windows, sampling limits, output shape, exclusions, stop conditions and permissions. Report what could not be checked; missing scores are not zero scores. [[sources/ankrgyl--trace-lake#automation-contract]]
14. **Track a finding's lifecycle.** Discover, verify, monitor, refresh and close with evidence; don't silently equate “query failed” with “issue fixed.” [[sources/ankrgyl--trace-lake#patterns-verification]]
15. **Map storage and analysis data flows separately.** Document where payloads persist and where they are sent for inference, then apply scoped access/redaction appropriate to each boundary. [[sources/ankrgyl--trace-lake#analysis-data-boundary]]
16. **Own downstream artifacts and costs.** Keep a ledger of scorers, monitors and other writes created by investigators; pausing their creator is not a cleanup policy. Audit external tool authority separately from the platform's checkbox. [[sources/ankrgyl--trace-lake#automation-authority]]
17. **Benchmark the actual query mix and correctness.** Keep production A/B, selected slow cases and synthetic comparisons separate; include warm/cold cache, returned-result correctness and cases the new engine loses. [[sources/ankrgyl--trace-lake#benchmark-scope]]
18. **Start with one service and one failure class.** Connect a small slice of real logs to a rerunnable eval, measure usefulness, then expand. The application-log post suggests one service; the failure-class-first rollout is our adaptation. [[sources/ankrgyl--trace-lake#application-logs]] [[sources/ankrgyl--trace-lake#trace-to-eval]]

## Open questions

- What is the smallest retained record that can reproduce our costly failure classes without retaining unnecessary private data?
- Which investigations are blocked by missing state versus query latency versus a weak correctness oracle?
- How many regressions do trace-derived evals catch on unseen future runs, after controlling for duplicated conversations and traffic shifts?
- When does recurring discovery cost more than the incidents it prevents, and what measured threshold warrants specialized storage?
- How should an eval be retired or revised when the intended behavior changes, while preserving the original failure evidence?

## Diagnosable evaluation deltas — 2026-11-04

[[artifacts/projects/auto-ontology]]'s evaluator preserves question-level fixed/broken flips alongside the aggregate delta. Our connection: those cases can seed targeted regression cohorts, provided the model, ontology revision, inputs and scoring rule travel with them. The companion does not implement a Trace Lake, and no such integration was tested here. [[sources/nvidia--auto-ontology-eval#flips]] [[sources/nvidia--auto-ontology-eval#pin]]

## Raw evidence before diagnostic interpretation — 2026-11-04

[[artifacts/projects/codex]] provides an implementation-level complement: opt-in local ordered event/payload bundles reduce offline into conversation, runtime objects and cross-agent edges. Runtime output and model-visible input remain distinct; trace closure can describe an interrupted task. This is local diagnostic infrastructure, not a deployed trace lake or measured eval-improvement loop. [[sources/openai--codex#trace]] [[sources/openai--codex#trace-writer]] [[sources/openai--codex#trace-tests]]
