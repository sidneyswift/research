---
domain: sources
type: paper
url: https://aclanthology.org/2025.findings-acl.577/
retrieved: 2026-11-05
snapshot-location: sources/frontier-docs--empirical-20261105/
last-reviewed: 2026-11-05
---

# Frontier research on API documentation, demonstrations and agent execution

> Three primary studies beyond the earlier documentation research: API/browser hybrid agents, learning tool contracts from demonstrations, and documentation ablations against enterprise API replicas.

## Snapshot details

Original reading notes only, plus exact PDF URLs, SHA-256/byte receipts and restoration metadata. Full PDFs/extracted text remain temporary local reading aids and are not preserved in this repository. Read and retrieved2026-11-05. No experiments, production services or model-provider calls were run. The two ACL papers are published Findings papers; Agent-Diff is pinned to arXiv2602.11224v1 and treated as a preprint. Its placeholder conference/DOI text is not proof of publication. An inaccessible OpenReview revision was not substituted silently for the pinned version.

| Study and original notes | Source/version | Reviewed scope |
| --- | --- | --- |
| [Beyond Browsing notes](frontier-docs--empirical-20261105/webapi-notes.md) | [ACL2025 Findings577](https://aclanthology.org/2025.findings-acl.577/),20pages | Main §§1–8; API source/task distribution/action-cost appendices; prompt text selectively. |
| [API learning notes](frontier-docs--empirical-20261105/api-learning-notes.md) | [EMNLP2025 Findings994](https://aclanthology.org/2025.findings-emnlp.994/),19pages | Main §§1–9; train/test and dataset appendices; prompt/example captions. |
| [Agent-Diff notes](frontier-docs--empirical-20261105/agentdiff-notes.md) | [arXiv2602.11224v1](https://arxiv.org/abs/2602.11224v1),47pages | Task construction, evaluation, Tables4–6, main error analysis, replica-validation appendix. |

[papers.json](frontier-docs--empirical-20261105/papers.json) owns exact PDF URLs/version/hash/byte restoration. [captures.json](frontier-docs--empirical-20261105/captures.json) verifies original preserved note bytes. These receipts prove file identity, not study validity, source currency, independent replication or full-PDF preservation.

## Anchor map

- `#root` — collection provenance, publication/version limits and review scope above.
- `#web-api` — [webapi-notes.md](frontier-docs--empirical-20261105/webapi-notes.md), sections Experimental unit and treatment; Results and mechanism; Interpretation and limits. Source [paper §§3.2–3.3,5–6,8 and AppendixA.2–A.4](https://aclanthology.org/2025.findings-acl.577.pdf):812tasks; endpoint catalog/detail retrieval; GPT-4o action-space comparison; capability-coverage confounding. Hierarchical lookup is implemented, not isolated as a causal treatment.
- `#api-learning` — [api-learning-notes.md](frontier-docs--empirical-20261105/api-learning-notes.md), sections Method and denominator; What changes behavior; Transfer to documentation design. Source [paper §§3–6,9,AppendicesA–C](https://aclanthology.org/2025.findings-emnlp.994.pdf): three benchmark splits, demo filtering, context-window failures, schema loss, targeted '#'-format repair10%→49%. Different Table1/Table2 denominators cannot be pooled.
- `#agent-diff` — [agentdiff-notes.md](frontier-docs--empirical-20261105/agentdiff-notes.md), sections Task and metric; Results; Design implication and limits. Source [arXivv1 §§3–6,Tables5–6,Appendix8.10](https://arxiv.org/pdf/2602.11224v1):224tasks; pass vs assertion-weighted score; no/relevant/all-docs; closed-world side-effect rule; Box Hub subgroup. Familiarity explanation is plausible but training inclusion unobserved.
- `#restoration` — [papers.json](frontier-docs--empirical-20261105/papers.json) and each note's Restoration and preservation section: PDF version,URL,SHA-256,bytes,pages; no full source reproduction preserved.

## Why we cite this

These studies separate finding a contract, learning parameter semantics, choosing actions, completing a task and avoiding unintended state changes. They supply counterevidence to “more context is better” and “examples make reference docs unnecessary.” They support targeted, measurable hypotheses rather than one universal agent-documentation format.

These are additions to [[sources/docs-research--empirical-20261105]], [[concepts/developer-documentation-design]] and [[concepts/agent-api-learning-and-evolution]]. The API/browser study complements existing [[concepts/business-platform-api-design]] research by separating documentation gaps from missing business capability.

## Popularity and credibility signals

- Two published ACL Findings papers,July andNovember2025; identifiers and author lists in the notes. Publication is a credibility signal, not a universal effect guarantee.
- Agent-Diff is an author preprint dated2026-02-11, not a peer-review claim. No citation-count, adoption or popularity claim was checked. As-of2026-11-05.

## Related sources

- [[sources/docs-research--empirical-20261105]] — older developer-observation/intervention work plus later agent documentation work; do not combine their sample sizes or outcomes.

## Documentation collection review scope

Manual primary-paper reading and local PDF text extraction. Diagram screenshots and every prompt-image variant were not exhaustively reviewed. No trial was reproduced, code environment installed, or provider execution invoked. Original notes explicitly distinguish reported measures, author interpretations and our design inferences. Citations are version-bound; changing upstream versions requires a deliberate re-ingest rather than editing these immutable notes.
