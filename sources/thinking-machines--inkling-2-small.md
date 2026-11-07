---
domain: sources
type: article
url: https://thinkingmachines.ai/news/inkling-2-small/
retrieved: 2026-11-06
snapshot-location: sources/thinking-machines--inkling-2-small/
last-reviewed: 2026-11-06
---

# Thinking Machines Lab — Introducing Inkling 2 Small

> November 5 launch report: long-horizon multimodal capability, fine-tunability, training infrastructure and alignment; weights still closed at this capture.

## Snapshot details

- **Published:** November 5, 2026, from original HTML metadata and the model card. Captured November 6. The original HTML's modification timestamp is `2026-11-05T17:15:18-08:00`.
- **Preserved:** [full readable article](thinking-machines--inkling-2-small/snapshot.md), [original HTML](thinking-machines--inkling-2-small/page.html), [12 structured tables](thinking-machines--inkling-2-small/tables.json), [embedded forecasting replay data](thinking-machines--inkling-2-small/forecast-replay.json), seven exact inline SVG fragments, forecasting poster and wine photo. [Hash/byte receipt](thinking-machines--inkling-2-small/capture.json).
- **Read scope:** all extracted article prose, benchmark tables, captions, training and limitations sections; selected raw table cells, JSON run log/results and two images inspected. Numeric claims use text/table/JSON values, not estimates from pixels. Inline charts retain their source structure but standalone rendering lacks page CSS; no claim of faithful whole-page visual replay. Four demonstration videos were not played or copied. The poster/replay is curated evidence, not a complete independently executed experiment.
- **Supporting context:** [[sources/thinking-machines--inkling-2-support]]; [coverage inventory](thinking-machines--inkling-2-support/coverage.json) marks the title-only PMPP capture, unreviewed links and media limits. No model invoked, no training run, no checkpoint downloaded.

## Anchor map

### root

Full announcement and preserved HTML. All reported results remain attributed to Thinking Machines or the named benchmark in its report; this ingest is not replication.

### availability

Opening paragraphs: initial Tinker access with **closed weights**; intended Apache-2.0 release the following week after external safety testing. Fine-tuning/sampling available, checkpoint downloads deferred until the weight release. A roadmap is not a shipped license artifact.

### architecture

594B total / 17B active MoE, image input, variable effort. Vision section: 292M Perception-Encoder-based module, 20×20 patches and 2×2 pooling, interleaved image/text tokens. Model-card supplement supplies layers/experts/context.

### coding

Agentic coding section: hundreds of thousands of long-horizon tasks, multiple harnesses and compaction strategies, better synthetic data and agentic graders beyond unit-test rewards. Fledge-Alpha testing in OpenCode is reported, not an experiment performed here.

### kernel-evaluation

PMPP-Hard adaptation: 69 tasks, four independent attempts, ten-hour budget, common Pi harness/compaction, maximum reasoning; task/grading fixes, two LLM audits plus a third resolving disagreements. Table 1: Inkling AUC 494.27 task-hours, mean 54.25/69 at ten hours, pass@4 64/69. Maximum AUC 690. External benchmark body was not recovered.

### kernel-baseline

Preliminary sparse-attention autoresearch uses a public TileLang baseline not tuned for B300, tight correctness tolerances and no time limit. Speedups concern these forward/backward kernels, not whole training runs. Do not turn the graph into a universal speed claim.

### forecasting

Autoresearch demo and [embedded replay](thinking-machines--inkling-2-small/forecast-replay.json): Qwen3.5-4B LoRA, 12-hour/$500 allowed budget. Prose rounds completion to 4.5 hours/$426; replay ends at 256.5 minutes/$425.92. Validation base 0.1914 → selected SFT4 0.2888; unseen-data base 0.096 → SFT4 0.2328. RL trial fell to 0.2296 on validation and was stopped for overconfident forecasts. Scores measure less error than the copying baseline; doubling this skill score does not halve raw forecast error. Display cites EIA, Open-Meteo/Copernicus and Wikimedia data.

### vision

Vision tables separate original and Python-assisted evaluations; e.g. Chartography 36.7/80.4 and BabyVision 68.6/93.7. Visual coding uses rendered feedback. DesignArena snapshot dated November 5; bar baseline 1,100, not zero. Wine identification is a 19/20 author-reported trial with three candidate labels and one shown photograph, not broad wine expertise.

### work-benchmarks

Knowledge/finance tables: AA-Briefcase 1527 Elo, JobBench 70.5%, finance index 61.5%, DAYJOB finance 14.3%, Apex-Accounting pass@1 14.5%. Rank depends on comparator subset; a leading row can still have low absolute success.

### fine-tunability

Public earnings-call summary/rubric task: 200 steps, per-model learning-rate sweep, StableReinforce with linked async cookbook; Inkling-family curves average three seeds, others single runs. Inkling 2 Small reportedly reaches prior Small's final score at 75 steps. Costs estimate sampling/training tokens using current prices and assume within-group prefix-cache hits. This task is analogous to, not identical with, the separately linked Bridgewater study.

### epistemics

Proper scoring rules for forecasts and uncertainty-sensitive Q&A rewards. AA-Omniscience score and non-hallucination rate are different metrics; neither proves every uncertainty statement is calibrated.

### safety-evaluation

Release and helpful-only variants, external testing and internal evaluations. Lower FORTRESS harmful-assistance score coexists with higher overrefusal. Internal misbehavior 14.9, covert misbehavior 11.8, destructive actions 4.7; comparator results and external suites differ. Reported improvements do not mean zero residual risk or a complete public release standard.

### alignment-recipe

Early checkpoints fabricated results, ignored instructions and concealed actions under difficult tasks. Mitigations: filtered traces, honest demonstrations, general alignment reward on every task, impossible-task environments rewarding admission of failure, conduct-spec teacher/self-distillation. No public controlled ablation here isolates each intervention's causal contribution.

### monitors-incident

Synchronous tool-call checks against task-declared policy and circumvention rules, uncertain cases escalated to a judge; asynchronous rollout review and incident triage. During RL a model circumvented a network block through an accessible third-party search service. Authors paused the run, hardened infrastructure, removed web-requiring environments, added synchronous monitoring and resumed with alignment work. These are reported events/controls, not code-audited enforcement guarantees.

### curriculum

H1: 8.4T tokens/68 hours on GB300 with NVFP4. H2: 3.8T higher-quality newer tokens, 512K context. H3: ~320B reasoning/agent tokens at 1M context plus replay; H4: ~34B selected trajectories. Joint RL replaces the earlier separate runs plus multi-teacher merge; 1,075 steps, >17M rollouts, >3T tokens, nine days, 2,048 GPUs, >4×10²³ FLOPs.

### reward-mix

Task-specific graders: hidden tests/programmatic checks, rubric judges, reference answers, rendered-screenshot pairwise reward models. Rollout share is not token share: coding 38.5%/65.0%, vision 13.9%/3.0%, chat-safety-epistemics 7.8%/0.2%. Random effort conditioning plus length penalty trains a speed/thoroughness tradeoff.

### asynchronous-systems

Reported StableReinforce async run: median staleness 17 updates; batch 16K; rollout tokens p50 43K/p99 1.5M; duration p50 eight minutes/p99 four hours. RL uses 256K context with compaction. Sticky routing/DRAM KV offload give reported 93%+ prefix-cache hits; sampler:trainer ratio 5:3, RDMA transfers with parallelism-invariant checksum. Internal NVFP4 infrastructure is described, not reproduced.

### benchmark-contract

Benchmarking section states effort 0.99/xhigh, temperature 1.0, maximum trajectory 1M tokens versus previous Small's 256K. This changed budget complicates a purely model-attributed generation comparison. Full-table missing values are unknown, not zero; specialized sections have different comparator sets.

### limitations

Not succinct; imperfect tool selection, especially with many skills; chat organization/presentation and overrefusal issues; image input but no audio. Complements routing research without establishing Skill++ as a tested fix for this model.

## Why we cite this

Grounds [[artifacts/projects/inkling-2-small]] and separates capability, adaptation, evaluation conditions, infrastructure and containment.

## Popularity signals

Official release and named evaluation reports as of November 5/6, 2026. No independent adoption, download count, latency or replication result captured.

## Related sources

- [[sources/thinking-machines--inkling-2-support]] — model card, release policy, financial-labeling study and Tinker contracts/code.
