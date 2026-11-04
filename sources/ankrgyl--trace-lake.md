---
domain: sources
type: article
url: https://x.com/ankrgyl/status/2117696780741771638
retrieved: 2026-11-04
published: 2026-11-03
snapshot-location: sources/ankrgyl--trace-lake/
upstream-commit: n/a (X article plus dated vendor documentation)
last-reviewed: 2026-11-04
---

# Ankur Goyal — The Trace Lake

> Retain searchable agent execution history, investigate behavior across runs, and convert production examples into reproducible evaluations.

## Snapshot details

- **Author:** Ankur Goyal / `@ankrgyl`, confirmed by X API metadata; writes from Braintrust's product perspective.
- **Post / article:** [original post](https://x.com/ankrgyl/status/2117696780741771638), [X article](https://x.com/i/article/2117682615494823936). Published `2026-11-03T19:13:52Z`; mirror article last-modified `2026-11-03T19:33:51Z`.
- **Complete body:** [snapshot.md](ankrgyl--trace-lake/snapshot.md), reconstructed from all 34 ordered rich-text blocks, including both embedded SQL examples and inline links. The official X API returned the title/link but not the body. [article-public-response.json](ankrgyl--trace-lake/article-public-response.json) is the unmodified public FxTwitter response; post ID, article ID and title matched. [tweet-api.json](ankrgyl--trace-lake/tweet-api.json) preserves independent official metadata.
- **Media:** [cover.png](ankrgyl--trace-lake/cover.png) inspected: title artwork, no additional technical claims. The two atomic body blocks are SQL Markdown, not missing images. No body media entities were returned.
- **Linked context:** eight distinct primary pages read and preserved under `linked/`: four official blog pages (HTML plus text extraction) and four living docs pages (official Markdown). Original `braintrust.dev/docs` links redirect to `docs.braintrust.dev`. The duplicate Nitro preview link is represented by the public canonical article, not a separate preview capture.
- **Integrity / coverage:** [capture.json](ankrgyl--trace-lake/capture.json) records URLs, capture boundaries, byte counts and SHA-256 hashes. Blog text captures are not complete visual reproductions: benchmark tables expose the default cold-cache view; embedded video was not played. No deployed product, SQL query, benchmark or automated investigation was independently run.
- **Evidence class:** author argument + vendor architecture/product documentation + vendor-reported measurements and testimonials. Living documentation retrieved November 4 can clarify or qualify the article; it is not proof of the precise product state when the post was published.

## Anchor map

- `#root` — `snapshot.md`, complete article and author/date/URL attribution.
- `#capture` — capture details above; `capture.json`, official API metadata and mirror rich-text JSON.
- `#historical-corpus` — article introduction and “How to build a Trace Lake”: retain queryable history; compare similar behaviors instead of only opening individual traces.
- `#query-latency` — requirement 1: target ingest under 10 seconds, SQL in hundreds of milliseconds, full-text search plus structured queries.
- `#storage` — requirement 2: author's workload estimates, object-storage economics and own-cloud motivation.
- `#trace-to-eval` — requirement 3: incoming-trace analysis, recurring failure patterns, focused inexpensive evals, pre-action state and resource versions for reproduction.
- `#trace-query-semantics` — “What's missing,” both SQL blocks: trace summary metrics plus span-scoped predicates; nested and unstructured payloads.
- `#product-claims` — “What the Trace Lake makes possible”: Topics, Patterns, Loop, Nitro, Notion testimonial and application-log preview.
- `#brainstore-architecture` — `linked/brainstore-architecture.txt`, “Architecture goals and strategy,” “Write path,” “Read path,” “Real-time reads”: tenant partitions, object-store WAL, trace colocation, multiple indexes, asynchronous compaction and bounded fresh reads. Blog dated 2026-04-06.
- `#nitro` — `linked/nitro.txt`, “Nitro schedules storage and compute separately” and “Fewer reads and less work”: separate concurrency limits, prefetch/coalescing and selective early phrase checks. Blog dated 2026-09-24.
- `#benchmark-scope` — `linked/nitro.txt`, “Faster searches on production data” and “A separate comparison on 40 GB of text”: vendor's three-day, >1M-query A/B test (>10K full-text queries), >2× full-text / 15% other-query speedup versus prior Brainstore; separate selected slow-query and synthetic tests, cache/sample caveats, competitor aggregate win.
- `#customer-testimonials` — `linked/brainstore.txt`, “Customer testimonials”: vendor-hosted Notion, Zapier and Day.ai statements. Blog dated 2025-03-03; historical rollout and benchmarks are not current guarantees.
- `#application-logs` — `linked/application-logs.txt`, dated 2026-10-08: correlate logs with trace context, preserve message templates, inspect retries and outcomes, start with one service.
- `#filter-semantics` — `linked/docs-filter.md`, “How filters match your data,” “Identify spans and traces,” and failed-LLM-call example: same-span conjunction differs from independent existential conditions; individual span `id` versus `root_span_id`.
- `#retention-window` — `linked/docs-filter.md`, “Apply a filter” note: hosted plan retention windows enforced across query paths; older data silently excluded. Documentation reports Starter 14 days, Pro 30 days by default, Enterprise custom; these are dated product terms, not the conceptual requirement.
- `#topics` — `linked/docs-topics.md`, “How it works” and “Group traces into conversations”: facet summaries, clustering, classification, grouping, daily regeneration threshold of 100 summaries.
- `#analysis-data-boundary` — `linked/docs-topics.md`, “Models and data handling”: SaaS, BYOC and self-hosted Topics use Braintrust-hosted model endpoints with stated Zero Data Retention; Baseten named as subprocessor. Retention claims do not mean inference remains inside the customer's cloud.
- `#patterns-verification` — `linked/docs-patterns.md`, “How discovery works” and “Verification”: evidence-backed findings, compare cohorts without causal overclaiming, consult code/requirements, label hypotheses, preserve status when checks are inconclusive.
- `#automation-contract` — `linked/docs-automations.md`, investigation/schedule/permissions configuration and recipes: explicit windows, exclusions, stop conditions, sampling, independent conversation counts and raw-evidence checks.
- `#automation-authority` — same docs, “Set write permissions,” “Pause,” “Delete”: Braintrust tool permissions do not govern connected MCP authority; scheduled runs cannot push GitHub branches/PRs; created online scoring rules can outlive the automation and keep costing money.
- `#traction` — `tweet-api.json`: 102 likes, 140 bookmarks, 10 reposts, 6 quotes, 9 replies, 18,924 impressions at retrieval on 2026-11-04.

## Why we cite this

Grounds [[concepts/trace-lake]]: the evidence substrate for a production-learning loop, not simply another tracing UI or a recommendation to build a custom database. Connects [[concepts/compound-engineering]], [[concepts/review-cost-aware-workflows]] and [[concepts/agent-control-plane]].

## Popularity signals (if this source provides them)

- **Signal:** X post engagement, recorded at `#traction`; attention, not adoption or correctness.
- **As-of:** 2026-11-04. Vendor customer quotes and benchmarks remain separately attributed evidence classes.

## Related sources

- [[sources/poteto--verification-over-adversarial-review]] — verification-first budget allocation; the Trace Lake supplies empirical examples for that work.
- [[sources/mattpocock--domain-orchestrator-factory]] — proposed persistent coordinator/factory; trace-based investigation is a complementary evidence loop, not proof the proposal was implemented.
- [[sources/SHL0MS--skill-diffs]] — different corpus and validation target: historical maintainer edits versus runtime agent behavior.
