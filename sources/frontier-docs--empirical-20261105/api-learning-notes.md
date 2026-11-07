# Learning API Functionality from In-Context Demonstrations — original reading notes

Bhrij Patel, Ashish Jagmohan, Aditya Vempaty. EMNLP Findings, November2025, pp.18318–18336. Anthology title omits “of”; PDF title includes “Learning of API Functionality”. Canonical: https://aclanthology.org/2025.findings-emnlp.994/ . Read 2026-11-05: main §§1–9, train/test and dataset appendices, prompt/example captions. Published paper; no rerun performed.

## Method and denominator

The question is whether a frozen LLM can infer tool functionality without original docs. Compare direct expert demonstrations(DxD), generated documentation(GD), generated documentation plus example calls(GDEC), and original documentation(OD). Expert traces come from successful agents using original docs: GPT-4 WorkBench, GPT-4.5 tau-bench retail, GPT-4o CRMArena. A successful final trace can include wrong intermediate calls, so “expert” does not guarantee every demonstration is correct.

Three seeds use an iterative approximately70/30 split that preserves API overlap and changes the test-set size. Demo-count experiments retain only tasks using functions with at least35 training demonstrations: average55 WorkBench,77.6 tau-bench,183 CRMArena tasks. Self-exploration uses at least5 per function, yielding167 WorkBench and83 tau-bench test tasks. These denominators differ; results across the two tables are not interchangeable. Six models appear across the paper, but not every model runs every condition. Core pipeline uses o3-mini, GPT-4o-mini and GPT-4o; added open-model analyses have narrower scopes.

## What changes behavior

Increasing demonstrations5→15→25→35 is not reliably better. Some zeros are context-window failures, not proof the agent understood nothing. More examples sometimes make optional time parameters appear mandatory, and summaries can invent parameter names. Supplying the actual observed parameter-name list fixes that particular generation issue for some models. Repeated examples can also induce repeated calls.

A concrete tau-bench failure: order_id requires a leading '#', but malformed identifiers return a generic not-found error. Generated documentation omits this requirement; generated critiques can wrongly recommend removing '#'. In the self-exploration attached-guidelines condition with o3-mini and direct demos before exploration, explicitly inserting the correct format rule raises average task success10%→49% (39 percentage points). This is a targeted repair ablation, not a39-point benefit for all documentation improvements. The same table reports original docs78% on that tau-bench subset.

Direct demonstrations sometimes outperform original docs on WorkBench. Authors explicitly warn of similar train/test task formats and possible leakage; this is not proof prose docs are obsolete. LLM critiques receive entire trajectories and binary success feedback; this is a more privileged learning setup than interpreting arbitrary production logs. Independent per-function summarization misses shared parameter semantics, which authors identify as a future direction.

## Transfer to documentation design

Inference: treat parameter schemas, identifier formats, optionality and validation errors as maintained contracts, with real examples and recoverable diagnostics. A generated summary should not replace these authoritative details without validation. Preserve task context and prerequisite lookup calls when they explain how to obtain an ID. Evaluate summaries with held-out end tasks and trace errors, not fluent appearance. This paper does not establish cross-provider MCP compatibility, autonomous production learning, or the effectiveness of llms.txt.

## Restoration and preservation

Full PDF is a temporary, uncommitted reading aid. Restore from https://aclanthology.org/2025.findings-emnlp.994.pdf and verify SHA-256 `d92dff197246792f0ed24fd99492a1a030cf6427a3c48ea4d2488cbd86294904`, 6034923 bytes, 19 pages. Only these original notes and metadata are preserved; extracted full text is not committed.
