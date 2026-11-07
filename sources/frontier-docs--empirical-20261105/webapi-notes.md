# Beyond Browsing: API-Based Web Agents — original reading notes

Yueqi Song, Frank F. Xu, Shuyan Zhou, Graham Neubig. ACL Findings, July 2025, pp.11066–11085. Canonical paper: https://aclanthology.org/2025.findings-acl.577/ . Read 2026-11-05: main text §§1–8; appendix API sources, task distribution and action-cost analysis; inspected prompt text selectively. This is a published study, not an independently rerun benchmark.

## Experimental unit and treatment

The unit is a WebArena task, scored using benchmark-specific output/state/navigation checks. The appendix lists 180 GitLab, 109 map, 187 shopping, 182 shopping-admin, 106 Reddit and 48 multisite tasks (812 total). Three GPT-4o-based agents use OpenHands: browser-only, Python/code API-only, and a hybrid that can interleave browsing and APIs. These are different action spaces and prompts, not a randomized comparison of documentation formats alone.

The authors manually assemble API access and documentation. Below 100 endpoints they supply complete docs; larger sets receive an endpoint list with short summaries and a get_api_documentation tool for exact endpoint details. GitLab has 988 endpoints, map53, shopping/admin556, Reddit31 after author extensions. README and OpenAPI YAML are both used; this does not compare their quality head-to-head. The 100-endpoint threshold is an implementation choice, not an established universal optimum.

## Results and mechanism

Table2 reports task success14.8% browser-only,29.2% API-only,38.9% hybrid: gains of14.4 and24.1 percentage points relative to that browser baseline. Hybrid does not solve most tasks. A separate Reddit intervention expands the API from18 to31 endpoints, increasing API-only success9.4%→18.9%; it changes capability coverage, not merely documentation. The extra endpoints were designed without access to benchmark tasks, according to the authors.

In a random100-task error audit,33 tasks succeeded using APIs,50 were judged not solvable by APIs alone,6 failed task understanding and11 failed API usage. Thus66% success among the50 judged API-solvable tasks is a conditional subgroup result; it must not replace the full-benchmark success rate. Average2.1 actual API calls for solvable tasks coexists with7.8 agent steps overall; docs lookup, correction and verification consume steps too.

## Interpretation and limits

This supports treating API coverage and agent navigation to contracts as separate platform concerns. Hierarchical discovery is a demonstrated workable implementation, but the paper has no isolated one-stage/two-stage documentation ablation. Different websites also differ in functionality, task mix and maturity; their performance is not a clean causal estimate of documentation quality. The study uses one base model, self-hosted text-oriented WebArena services, manual API integration, and generated Reddit documentation. Author-built APIs and limited image support constrain transfer to arbitrary live services.

Portable design inference: publish concise capability discovery plus detailed endpoint contracts; make absence explicit; allow a caller to choose API or browser fallback where authorized. Evaluate actual task/state success separately from whether it found the correct documentation. These are design inferences, not demonstrated gains for Flex or a WebMCP implementation.

## Restoration and preservation

Full PDF is a temporary, uncommitted reading aid. Restore from https://aclanthology.org/2025.findings-acl.577.pdf and verify SHA-256 `8e83e3e413979e7112430725d02b40a8246a348dc6bbb06686f2d88f5abf73c5`, 1513525 bytes, 20 pages. Only these original notes and metadata are preserved; extracted full text is not committed.
