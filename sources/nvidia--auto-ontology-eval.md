---
domain: sources
type: repo
url: https://github.com/NVIDIA/auto-ontology-eval
retrieved: 2026-11-04
snapshot-location: sources/nvidia--auto-ontology-eval/
upstream-commit: ec41b2c5b795637759297b90c1d19b42693200f9
last-reviewed: 2026-11-04
---

# NVIDIA/auto-ontology-eval

> Pinned source evidence for [[artifacts/projects/auto-ontology]]; implementation, documentation, prompt policy and structural checks are distinguished.

## Snapshot details

- **Revision:** `ec41b2c5b795637759297b90c1d19b42693200f9`, retrieved 2026-11-04. Local clone with `.git` retained; ignored and registered in `sources/repos.manifest.tsv`. Restore with `./setup.sh --only nvidia--auto-ontology-eval`.
- **Scope:** README, evaluation design, application dependency pin, optional treatment context, execution-match semantics, health gates, question-level flips and corresponding test assertions. No headline accuracy result established. Dataset contents, every benchmark server and seed scripts not exhaustively investigated.
- **Execution boundary:** application, model calls and benchmarks not run. Referenced upstream tests inspected, not executed: system Python had no pytest; no dependencies installed.
- **Metadata:** [capture.json](nvidia--auto-ontology-evidence/capture.json) records both repository pins, GitHub attention, dated issue states and offline structural checks.

## Popularity signals

- GitHub API at retrieval: **50 stars, 12 forks**, as-of 2026-11-04. Attention is not demonstrated accuracy or adoption.

## Anchor map

### root

- [README.md:1–73](https://github.com/NVIDIA/auto-ontology-eval/blob/ec41b2c5b795637759297b90c1d19b42693200f9/README.md#L1-L73)

### pin

- [pyproject.toml:1–30](https://github.com/NVIDIA/auto-ontology-eval/blob/ec41b2c5b795637759297b90c1d19b42693200f9/pyproject.toml#L1-L30)

### model-controls

- [README.md:108–140](https://github.com/NVIDIA/auto-ontology-eval/blob/ec41b2c5b795637759297b90c1d19b42693200f9/README.md#L108-L140)

### extra-context

- [docs/extra-prompts.md:1–55](https://github.com/NVIDIA/auto-ontology-eval/blob/ec41b2c5b795637759297b90c1d19b42693200f9/docs/extra-prompts.md#L1-L55)

### health-gate

- [ontology_sql_eval/gym/compare.py:37–162](https://github.com/NVIDIA/auto-ontology-eval/blob/ec41b2c5b795637759297b90c1d19b42693200f9/ontology_sql_eval/gym/compare.py#L37-L162)

### flips

- [ontology_sql_eval/gym/compare.py:168–212](https://github.com/NVIDIA/auto-ontology-eval/blob/ec41b2c5b795637759297b90c1d19b42693200f9/ontology_sql_eval/gym/compare.py#L168-L212)

### scoring

- [ontology_sql_eval/gym/exec_match.py:5–23](https://github.com/NVIDIA/auto-ontology-eval/blob/ec41b2c5b795637759297b90c1d19b42693200f9/ontology_sql_eval/gym/exec_match.py#L5-L23)
- [resources_servers/README.md:13–77](https://github.com/NVIDIA/auto-ontology-eval/blob/ec41b2c5b795637759297b90c1d19b42693200f9/resources_servers/README.md#L13-L77)

### health-tests

- [tests/gym/test_compare.py:1–65](https://github.com/NVIDIA/auto-ontology-eval/blob/ec41b2c5b795637759297b90c1d19b42693200f9/tests/gym/test_compare.py#L1-L65)

### scoring-tests

- [tests/gym/test_beaver_match.py:45–74](https://github.com/NVIDIA/auto-ontology-eval/blob/ec41b2c5b795637759297b90c1d19b42693200f9/tests/gym/test_beaver_match.py#L45-L74)
- [tests/gym/test_bird_official.py:48–83](https://github.com/NVIDIA/auto-ontology-eval/blob/ec41b2c5b795637759297b90c1d19b42693200f9/tests/gym/test_bird_official.py#L48-L83)

## Why we cite this

Supports the implementation and evidence boundaries in [[artifacts/projects/auto-ontology]], not a replicated benchmark or blanket correctness guarantee.

## Related sources

- [[sources/nvidia--auto-ontology]] — separately pinned companion; same team, not independent validation. The evaluation dependency pins a different application revision.
