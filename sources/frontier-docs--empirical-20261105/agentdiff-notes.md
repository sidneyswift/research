# Agent-Diff documentation ablation — original reading notes

Hubert M. Pysklo, Artem Zhuravel, Patrick D. Watson. arXiv2602.11224v1, submitted2026-02-11. Exact version: https://arxiv.org/pdf/2602.11224v1 . Read 2026-11-05: methods/task construction/evaluation, main results and Tables4–6, error analysis, appendix replica validation.47 pages. Preprint: PDF has placeholder conference/DOI formatting; do not present it as verified peer-reviewed proceedings. OpenReview page/PDF downloads were blocked; claims here belong to this arXiv version, not an assumed identical later revision.

## Task and metric

224 enterprise tasks span Box48,Slack59,Linear57,Calendar60 and108 unique endpoints. Tasks are generated using frontier models then curated by humans; tasks average5.3 minimum API calls, range1–24. Each task belongs to a service; this is not proof of cross-service workflow success. Models write Bash/Python requests against containerized API replicas, not live customer accounts. Replica authors describe conformance tests and adversarial edge probing against production interfaces; this research session did not independently verify parity.

Success uses before/after state-diff assertions plus a closed-world rule: an unintended nonignored state change zeroes the task. Binary pass requires all assertions and no side effects. The separate aggregate score weights assertions, so a complex task contributes more denominator weight. These metrics answer different questions.

Nine models run three trials per task per condition: no_docs(~400-token service/base-URL/ReAct setup), relevant_docs(target service,~3200–10000tokens), all_docs(four services,~22300tokens). Episodes end at done,40turns,8minutes or context/token overflow. Each model has2016traces across all three conditions. Effects use a paired Bayesian bootstrap with10000draws; reported probabilities are Bayesian posterior probabilities, not classical p-values.

## Results

Relevant docs improve pooled binary pass rate by7.0±2.3percentage points, posterior P(delta>0)=1.00. Assertion-weighted score improves only2.4points,P=.73, so it is not a reliable aggregate score gain. All-docs similarly improves pass6.8points but changes score only+.2,P=.53. A negative Linear all-docs average is heterogeneous across models; irrelevant-context dilution is the authors’ interpretation, not an independently isolated mechanism.

Box subgroup:13Hub tasks versus35non-Hub tasks. Relevant docs improve assertion-weighted Hub score19.0±10.5points versus3.4±4.4 for non-Hub; posterior P(Hub benefit>non-Hub benefit)=.999. This is consistent with docs being more valuable for unfamiliar endpoints. The paper calls it a training-cutoff natural experiment because Hubs launched July2025. Actual training inclusion is unobserved: release date does not prove a model never saw the endpoint, and endpoint/task groups differ. Preserve that distinction when reasoning about agent knowledge over1/5/10years.

## Design implication and limits

Inference: use task-specific retrieval and explicit tests of novel/internal APIs; a benchmark on familiar APIs can understate the need for runtime documentation. Report binary task completion, weighted partial completion and side effects independently. Docs do not eliminate planning, temporal reasoning or outcome verification failures. These findings are one scaffold, nine model versions, generated/curated tasks and replica-backed services. They do not establish a universal ideal context size, prove that all-docs always hurts, or validate production notifications, authorization effects and downstream customer outcomes.

## Restoration and preservation

Full PDF is a temporary, uncommitted reading aid. Restore from https://arxiv.org/pdf/2602.11224v1 and verify SHA-256 `099242eba6c0e292eafd67224b3be160f72f8b9c9353f85ea506d34627721c4f`, 1490804 bytes, 47 pages. Only these original notes and metadata are preserved; extracted full text is not committed.
