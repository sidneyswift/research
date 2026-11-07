---
domain: sources
type: repo
url: https://github.com/mintlify/docs-url-discovery-bench
retrieved: 2026-11-05
snapshot-location: sources/mintlify--docs-url-discovery-bench/
upstream-commit: 5f055a89336cb94050e36eaa479374b390e92462
last-reviewed: 2026-11-05
---

# Mintlify Docs URL Discovery Bench

## Snapshot details

Ignored clean local clone with .git retained; manifest pins `5f055a89336cb94050e36eaa479374b390e92462`, dated2026-07-14.25tracked files. Read README/RESULTS, grader, proxy transformations, report filtering, audit and selected runner setup; inspected static result-row counts. No dependencies installed, vendor scripts imported/executed, benchmark rerun, provider request or site intervention performed. The row inventory uses our standard-library data inspection only.

## Anchor map

### root

[README](https://github.com/mintlify/docs-url-discovery-bench/blob/5f055a89336cb94050e36eaa479374b390e92462/README.md#L1-L153). MIT license, four proxy arms, reproducibility tiers, scope and limitations.

### methods

[Arms/metrics](https://github.com/mintlify/docs-url-discovery-bench/blob/5f055a89336cb94050e36eaa479374b390e92462/README.md#L17-L35), [proxy arm transformations](https://github.com/mintlify/docs-url-discovery-bench/blob/5f055a89336cb94050e36eaa479374b390e92462/url_discovery_bench/proxy.py#L37-L110) and [runner restriction](https://github.com/mintlify/docs-url-discovery-bench/blob/5f055a89336cb94050e36eaa479374b390e92462/url_discovery_bench/runners.py#L35-L42). URL-discovery task, not implementation correctness or business outcome; source models/date retained rather than treated as current defaults.

### grading

[Answer extraction and normalized-path grading](https://github.com/mintlify/docs-url-discovery-bench/blob/5f055a89336cb94050e36eaa479374b390e92462/url_discovery_bench/grade.py#L1-L55). Correctness is an allowed URL path under the local proxy, not understanding or executing the page. Fragment/query and .md suffix normalization changes what equality means.

### results

[Published core aggregate and exclusions](https://github.com/mintlify/docs-url-discovery-bench/blob/5f055a89336cb94050e36eaa479374b390e92462/RESULTS.md#L1-L69) and [replication](https://github.com/mintlify/docs-url-discovery-bench/blob/5f055a89336cb94050e36eaa479374b390e92462/RESULTS.md#L164-L219).20sites,100questions,2400valid core attempts, additional3600valid replication attempts. Publisher-reported efficiency effects conditioned on completed attempts; token accounting not comparable between agents. Results are not independently rerun here.

### audit

[Command audit](https://github.com/mintlify/docs-url-discovery-bench/blob/5f055a89336cb94050e36eaa479374b390e92462/url_discovery_bench/audit.py#L1-L55) and [report excludes error rows](https://github.com/mintlify/docs-url-discovery-bench/blob/5f055a89336cb94050e36eaa479374b390e92462/url_discovery_bench/report.py#L48-L73). Recognized fetch binaries/literal hosts; shell variables and runtime-mediated fetches limit coverage. Read-only inspection does not validate network containment.

### inventory

Our [static inventory](../projects/writing-amazing-developer-docs/experiments/mintlify-benchmark-inventory-2026-11-05.json) records2672core rows (2400valid/272errors) and3756replication rows (3600valid/156errors), source hashes and the exact tree. Result JSON and page inventory are present. Contrary to prose claiming committed proxy logs, no `data/full/logs/` files exist in this pinned tree. Snapshots are also absent and explicitly ignored in README. This is partial preservation, not a full replay artifact.

### reproducibility-gap

[404 decomposition depends on logs](https://github.com/mintlify/docs-url-discovery-bench/blob/5f055a89336cb94050e36eaa479374b390e92462/analysis/breakdown_404.py#L76-L97), while [RESULTS claims committed logs](https://github.com/mintlify/docs-url-discovery-bench/blob/5f055a89336cb94050e36eaa479374b390e92462/RESULTS.md#L110-L113). Inspect the inventory above before claiming the cause-specific decomposition can be regenerated from this checkout. Aggregate data remain available; a new live crawl is not restoration of the original frozen responses.

## Why we cite this

Supports [[artifacts/projects/mintlify]] and [[concepts/developer-documentation-design]] by narrowing what the vendor URL benchmark measures and what its public evidence preserves.

## Popularity and credibility signals

- Signal: Mintlify-published MIT benchmark source with committed result data; no star ranking or independent replication claimed.
- As-of:2026-11-05.

## Related sources

- [[sources/mintlify--agent-docs-research#root]] — blog claims and dates.
- [[sources/mintlify--agent-documentation-docs#llms]] — current product index behavior.
- [[creators/mintlify]] — publisher.
