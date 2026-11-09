---
domain: sources
type: repo
url: https://github.com/Nutlope/jev-fraud
retrieved: 2026-11-09
upstream-commit: 9b015f5782f555424107f6b4bb9d67811df62b7d
snapshot-location: sources/nutlope--jev-fraud/
last-reviewed: 2026-11-09
---

# Nutlope Jev + Kimi fraud cascade

Supporting implementation and a stored recording for [[concepts/typed-decision-cascades]], not a fresh model-quality benchmark. Creator: [[creators/nutlope]].

## Snapshot details

Full shallow checkout saved locally at `9b015f5782f555424107f6b4bb9d67811df62b7d`; restore with `./setup.sh --only nutlope--jev-fraud`. Clone is ignored, with manifest URL/pin tracked. [Selected-file hashes](nutlope--jev-fraud-evidence/source-hashes.json) and [offline verification](nutlope--jev-fraud-evidence/offline-verification.json) are committed. No dependencies installed, service started, or paid inference run.

## Anchor map

### root
[README.md L1–L82](https://github.com/Nutlope/jev-fraud/blob/9b015f5782f555424107f6b4bb9d67811df62b7d/README.md#L1-L82) — Demo architecture, results, replay versus paid live mode.

### results
[VALIDATION.md L1–L14](https://github.com/Nutlope/jev-fraud/blob/9b015f5782f555424107f6b4bb9d67811df62b7d/VALIDATION.md#L1-L14) — Reported release validation; code/model tests versus live claims; 92/100, 84% fraud recall, estimates.

### pipeline
[lib/pipeline.mjs L1–L37](https://github.com/Nutlope/jev-fraud/blob/9b015f5782f555424107f6b4bb9d67811df62b7d/lib/pipeline.mjs#L1-L37) — Typed parsing, confidenceBasis fallback, independent Kimi input, output checks and unresolved error paths.

### accounting
[lib/pipeline.mjs L5–L8](https://github.com/Nutlope/jev-fraud/blob/9b015f5782f555424107f6b4bb9d67811df62b7d/lib/pipeline.mjs#L5-L8) — Summary: class errors, fixes/regressions, failed-call costs and unknown/estimated counts.

### queues
[lib/batch.mjs L1–L28](https://github.com/Nutlope/jev-fraud/blob/9b015f5782f555424107f6b4bb9d67811df62b7d/lib/batch.mjs#L1-L28) — Independent 20/25 pools, bounded 429 retries, abort and provider failures.

### tests
[tests/pipeline.test.mjs L1–L20](https://github.com/Nutlope/jev-fraud/blob/9b015f5782f555424107f6b4bb9d67811df62b7d/tests/pipeline.test.mjs#L1-L20) — Mocked providers, threshold boundary, labels excluded, errors and accounting.

### batch-tests
[tests/batch.test.mjs L1–L25](https://github.com/Nutlope/jev-fraud/blob/9b015f5782f555424107f6b4bb9d67811df62b7d/tests/batch.test.mjs#L1-L25) — Separate pools, retries, abort and stream tests.

### dataset
[data/provenance.json L1–L13](https://github.com/Nutlope/jev-fraud/blob/9b015f5782f555424107f6b4bb9d67811df62b7d/data/provenance.json#L1-L13) — Seed 42, 50 fraud/50 legitimate, test split, length-filtered sample, not production prevalence.

### recording
[Stored recording](https://github.com/Nutlope/jev-fraud/blob/9b015f5782f555424107f6b4bb9d67811df62b7d/data/recording.json#L1-L9481), started 2026-09-20T03:53:28.501Z: 6,114ms, 100 completed, 30 escalated, 92 correct; Jev 90 correct; two fixes/no regressions; fraud TP42/FP0/FN8. Stored summary recomputed offline using the pinned `summarize` and matched within floating tolerance 1e-9. This confirms file arithmetic, not that the original network calls occurred or that accuracy generalizes. All 100 Jev rows record `provider confidence`; no exact resolved Jev model version is saved, only gateway alias.

### verification
Twelve bundled mock/stub tests executed locally on 2026-11-09 and passed. No UI/build/current-provider acceptance test performed. Test suite does not prove calibration, attack resistance, complete cancellation, or live billing. Recorded cost $0.101775 combines zero provider-reported Jev cost with 30 token-estimated Kimi calls; zero is not missing data or evidence of a free service.

### guarantee-boundaries
The source fallback validates classification/reason and receives the original email without Jev's guess or label. It is less fragile than the article's `sure` truthiness example, but still accepts a valid Kimi classification without a calibrated second-stage abstention rule. Jev parsing falls back from native confidence to selected-class probability while retaining the same threshold; `confidenceBasis` exposes this semantic difference, not equivalence. Production live mode requires an env opt-in; origin checks are not authentication, and README separately requires deployment protection. These are source-reading findings, not live exploits.

## Why we cite this

Distinguishes historical post metrics from revision-specific recordings; shows queues, uncertainty handling, cost provenance and error accounting. Links [[sources/buzzoni--jev-engineering]] and [[sources/typesafe--decision-model-docs]].

## Coverage

Inspected README, validation, provenance, recording metadata/row structure and recomputed aggregate metrics, pipeline, batch, API route, mocked tests and package scripts. Dataset emails not exhaustively re-labeled; neither original model calls nor announcement video independently replayed. Public dataset remains in ignored upstream clone, not duplicated into wiki Git. This is not a comprehensive application/security audit.
