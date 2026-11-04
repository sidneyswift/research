---
domain: sources
type: repo
url: https://github.com/NVIDIA/auto-ontology
retrieved: 2026-11-04
snapshot-location: sources/nvidia--auto-ontology/
upstream-commit: caced11e69e19663dfa0f73778dbecbcb71e87a0
last-reviewed: 2026-11-04
---

# NVIDIA/auto-ontology

> Pinned source evidence for [[artifacts/projects/auto-ontology]]; implementation, documentation, prompt policy and structural checks are distinguished.

## Snapshot details

- **Revision:** `caced11e69e19663dfa0f73778dbecbcb71e87a0`, retrieved 2026-11-04. Local clone with `.git` retained; ignored and registered in `sources/repos.manifest.tsv`. Restore with `./setup.sh --only nvidia--auto-ontology`.
- **Scope:** README, inspected architecture image, selected compilation/SQL/coverage paths, MCP surface and auth, modeling/publication skills, connection docs and focused tests. Not an exhaustive repository audit. Counted 119 OpenAPI operations versus a stale docs/comment count of 87; seven curated generated plus two custom tools; canonical and packaged OpenAPI copies match byte-for-byte.
- **Execution boundary:** application, model calls and benchmarks not run. Referenced upstream tests inspected, not executed: system Python had no pytest; no dependencies installed.
- **Metadata:** [capture.json](nvidia--auto-ontology-evidence/capture.json) records both repository pins, GitHub attention, dated issue states and offline structural checks.

## Popularity signals

- GitHub API at retrieval: **3,590 stars, 309 forks**, as-of 2026-11-04. Attention is not demonstrated accuracy or adoption.

## Anchor map

### root

- [README.md:1–75](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/README.md#L1-L75)

### architecture

- [README.md:179–263](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/README.md#L179-L263)

### license

- [LICENSE:1–25](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/LICENSE#L1-L25)
- [pyproject.toml:1–15](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/pyproject.toml#L1-L15)

### compile

- [auto_ontology/semantic/compile.py:1–127](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/semantic/compile.py#L1-L127)

### ordered-commits

- [auto_ontology/semantic/pipeline.py:25–239](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/semantic/pipeline.py#L25-L239)

### grounded-names

- [auto_ontology/semantic/term_extractor.py:30–85](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/semantic/term_extractor.py#L30-L85)

### measure-contracts

- [skills/nvidia-ontology-management/references/modeling.md:14–96](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/skills/nvidia-ontology-management/references/modeling.md#L14-L96)

### publication

- [skills/nvidia-ontology-management/references/publication.md:7–100](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/skills/nvidia-ontology-management/references/publication.md#L7-L100)

### certification

- [auto_ontology/dal/schema.py:121–130](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/dal/schema.py#L121-L130)
- [auto_ontology/dal/terms.py:156–260](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/dal/terms.py#L156-L260)
- [auto_ontology/dal/candidates.py:177–229](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/dal/candidates.py#L177-L229)

### coverage

- [auto_ontology/retrieval/entity_coverage/graph.py:26–49](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/retrieval/entity_coverage/graph.py#L26-L49)
- [auto_ontology/retrieval/entity_coverage/agents/coverage.py:24–75](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/retrieval/entity_coverage/agents/coverage.py#L24-L75)
- [auto_ontology/retrieval/entity_coverage/agents/coverage.py:151–222](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/retrieval/entity_coverage/agents/coverage.py#L151-L222)

### llm-sql

- [auto_ontology/retrieval/text_to_sql/agents/sql_from_semantic.py:350–390](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/retrieval/text_to_sql/agents/sql_from_semantic.py#L350-L390)

### retry-boundaries

- [auto_ontology/retrieval/text_to_sql/text_to_sql_graph.py:80–171](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/retrieval/text_to_sql/text_to_sql_graph.py#L80-L171)
- [auto_ontology/retrieval/text_to_sql/agents/sql_parse_validation.py:68–79](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/retrieval/text_to_sql/agents/sql_parse_validation.py#L68-L79)

### degenerate-sql

- [auto_ontology/retrieval/text_to_sql/agents/sql_parse_validation.py:206–280](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/retrieval/text_to_sql/agents/sql_parse_validation.py#L206-L280)

### query-timeout

- [auto_ontology/retrieval/text_to_sql/chat_sql.py:1–86](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/retrieval/text_to_sql/chat_sql.py#L1-L86)

### probe-guard

- [auto_ontology/retrieval/text_to_sql/db_probe/executor.py:43–179](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/retrieval/text_to_sql/db_probe/executor.py#L43-L179)

### curated-tools

- [mcp/auto_ontology_mcp/tools.py:5–229](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/mcp/auto_ontology_mcp/tools.py#L5-L229)

### readiness

- [mcp/auto_ontology_mcp/readiness.py:5–249](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/mcp/auto_ontology_mcp/readiness.py#L5-L249)

### structured-answer

- [mcp/auto_ontology_mcp/chat.py:5–116](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/mcp/auto_ontology_mcp/chat.py#L5-L116)

### mcp-auth

- [mcp/auto_ontology_mcp/auto_ontology_auth.py:25–149](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/mcp/auto_ontology_mcp/auto_ontology_auth.py#L25-L149)
- [docs/mcp.md:83–107](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/docs/mcp.md#L83-L107)

### gateway

- [frontend/auth/with-auth.ts:47–66](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/frontend/auth/with-auth.ts#L47-L66)
- [frontend/auth/proxy-backend.ts:31–71](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/frontend/auth/proxy-backend.ts#L31-L71)
- [frontend/lib/internalIdentity.ts:1–14](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/frontend/lib/internalIdentity.ts#L1-L14)
- [auto_ontology/server/identity.py:1–42](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/server/identity.py#L1-L42)

### connection-storage

- [docs/connections.md:7–71](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/docs/connections.md#L7-L71)

### query-skill

- [skills/nvidia-ontology-query/SKILL.md:1–180](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/skills/nvidia-ontology-query/SKILL.md#L1-L180)

### management-skill

- [skills/nvidia-ontology-management/SKILL.md:1–147](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/skills/nvidia-ontology-management/SKILL.md#L1-L147)

### setup-skill

- [skills/nvidia-ontology-setup/SKILL.md:1–275](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/skills/nvidia-ontology-setup/SKILL.md#L1-L275)

### prediction-drift

- [README.md:414–420](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/README.md#L414-L420)
- [auto_ontology/retrieval/text_to_sql/text_to_sql_graph.py:183–196](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/retrieval/text_to_sql/text_to_sql_graph.py#L183-L196)

### readiness-tests

- [mcp/tests/test_readiness.py:87–200](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/mcp/tests/test_readiness.py#L87-L200)

### cancellation-tests

- [auto_ontology/semantic/tests/test_cancellation.py:119–170](https://github.com/NVIDIA/auto-ontology/blob/caced11e69e19663dfa0f73778dbecbcb71e87a0/auto_ontology/semantic/tests/test_cancellation.py#L119-L170)

## Why we cite this

Supports the implementation and evidence boundaries in [[artifacts/projects/auto-ontology]], not a replicated benchmark or blanket correctness guarantee.

## Related sources

- [[sources/nvidia--auto-ontology-eval]] — separately pinned companion; same team, not independent validation. The evaluation dependency pins a different application revision.
