---
domain: creators
type: org
name: Braintrust
url: https://www.braintrust.dev
last-reviewed: 2026-11-04
---

# Braintrust

> Vendor studied for its Trace Lake framing: queryable agent history, investigations, evaluations and a specialized storage/query engine. [[sources/ankrgyl--trace-lake#root]]

## Attributes

- **Documented product components:** Brainstore storage/query engine, Nitro asynchronous execution, Topics classifications, Patterns findings and Loop investigations/automations. These are vendor documentation claims, not independently tested capabilities in this wiki. [[sources/ankrgyl--trace-lake#product-claims]]
- **Distribution studied:** official blog/docs plus [[creators/ankur-goyal]]'s X article. No company financial, market-share or executive-title claims were investigated.
- **Boundary worth tracking:** own-cloud trace storage and the inference route for analysis are distinct. Topics docs state all deployment types use Braintrust-hosted model endpoints with Zero Data Retention. [[sources/ankrgyl--trace-lake#analysis-data-boundary]]

## Artifacts produced

### Concepts and documentation

- [[concepts/trace-lake]] — retained traces as evidence for future evals and investigations.
- [[sources/ankrgyl--trace-lake]] — article and eight linked primary pages. No runnable artifact page yet; this was documentation-level research.

## Design philosophy (if discernible)

Specialize storage and query execution for large nested agent records; separate broad classification from deep investigation, then lower recurring measurement cost through focused checks. Preserve evidence and query context rather than relying on a narrative finding alone. [[sources/ankrgyl--trace-lake#brainstore-architecture]] [[sources/ankrgyl--trace-lake#patterns-verification]]

## Timeline (append-only)

- 2026-11-03 — Ankur Goyal's article frames the Trace Lake around the vendor's existing foundation. [[sources/ankrgyl--trace-lake#root]]
- 2026-11-04 — Article and linked docs ingested with explicit measurement, retention and data-boundary caveats. [[sources/ankrgyl--trace-lake#capture]]

## Source citations

- [[sources/ankrgyl--trace-lake#product-claims]] — component roles.
- [[sources/ankrgyl--trace-lake#benchmark-scope]] — reported measurements, baselines and limitations.
- [[sources/ankrgyl--trace-lake#analysis-data-boundary]] — storage versus inference locality.
