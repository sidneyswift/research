---
domain: projects
type: experiment
status: executed-synthetic
last-reviewed: 2026-11-05
---

# Documentation-test context probe

A local, synthetic demonstration supporting [[concepts/developer-documentation-design]]. It tests Python doctest mechanics, not a company's actual documentation or human/agent task performance.

## Question

Can a passing documentation test rely on context missing from the displayed fragment, or on an output match too weak to check success? Python documents injected execution globals and broad ellipsis matching. [[sources/docs-research--executable-reference-20261105#python-context]] [[sources/docs-research--executable-reference-20261105#python-flags]]

## Reproduce

From the Research root, run:

```bash
python3 projects/writing-amazing-developer-docs/experiments/example-context-probe.py
```

The script uses standard-library doctest with fixed synthetic strings; it makes no network requests and uses no credentials. Printed results include Python version and script SHA-256. The script raises an error if behavior differs from its explicit expected cases. Preserved run: [example-context-result-2026-11-05.json](example-context-result-2026-11-05.json).

## Executed result

Python 3.12.4, 2026-11-05:

| Case | Examples attempted | Examples failed |
| --- | --- | --- |
| Fragment with injected context | 1 | 0 |
| Same fragment without injected context | 1 | 1 |
| Complete example without injected context | 2 | 0 |
| Failed-job text with broad output match | 1 | 0 |
| Failed-job text with exact expected-success output check | 1 | 1 |

The two failures are intentional controls, not broken production tests. The demonstration constructs the conditions; it establishes feasibility under this runtime, not prevalence, impact or user confusion. It does not exercise Rust or Sphinx. Their published mechanisms are investigated separately. [[sources/docs-research--executable-reference-20261105#rust-tests]] [[sources/docs-research--executable-reference-20261105#sphinx-fixtures]]

## Patterns demonstrated

Application of [[patterns/quality-bar/revision-bound-review]]: tie the result to script hash, runtime and exact scope. No new confirmed cross-artifact pattern.

## What we'd steal

Report setup context, skip/compile/run modes and outcome assertions separately. Verify the context promised to a reader; retain deterministic semantic checks without treating incidental output as the contract.

## Mintlify benchmark inventory — 2026-11-05

A separate static data/Git-tree inspection is preserved in [mintlify-benchmark-inventory-2026-11-05.json](mintlify-benchmark-inventory-2026-11-05.json). It counts published valid/error rows and records source-file hashes and missing proxy-log/snapshot paths at the pinned revision. No vendor benchmark or replay code was executed; this is not a replication. See [[sources/mintlify--docs-url-discovery-bench#inventory]] and [[artifacts/projects/mintlify]].
