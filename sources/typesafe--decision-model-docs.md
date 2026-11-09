---
domain: sources
type: docs-page
url: https://docs.typesafe.ai/
retrieved: 2026-11-09
snapshot-location: sources/typesafe--decision-model-docs/
last-reviewed: 2026-11-09
---

# TypeSafe decision-model documentation — November 9 capture

Official, living documentation; current contract evidence kept separate from the September Buzzoni article. No API calls or performance replication.

## Snapshot details

Fifteen immutable captures with URLs and hashes in [capture.json](typesafe--decision-model-docs/capture.json): twelve official Markdown pages, discovery index, readable TypeSafe homepage and Kimi platform landing page. The latter is link-resolution evidence only. The index is not a claim to have read every linked page. Markdown preserves code/tables, not all embedded playground contents or interactive rendering.

## Anchor map

### root
[Models](typesafe--decision-model-docs/models.md) and [primitives](typesafe--decision-model-docs/primitives.md). Provider describes typed decisions; model capabilities are documentation claims, not exercised behavior.
### confidence
[Confidence](typesafe--decision-model-docs/confidence.md), including exact Choice/Noul/Score formulas, action probability versus concentration statistic, and per-action thresholds. Choice confidence `(p_max - 1/n)/(1 - 1/n)` is not selected-class probability. Checking both for fixed n adds no independent evidence.
### primitives
[Primitives](typesafe--decision-model-docs/primitives.md): independent questions, IDs not sent to model, field references and genuine dependencies requiring new requests. Current guidance favors a companion Noul over an `other` option when none of the choices may fit; this is provider-reported guidance, not our comparative experiment.
### models
[Models](typesafe--decision-model-docs/models.md): 1.14.0 and 1.13.0, $0.042/M input/free output, default 64k per-request/32k per-question; optional 262k both with long-context header; aliases resolve to 1.14.0 at capture. Organization-specific limits supersede treating the article's global RPS figures as current guarantees. Pinning a model does not freeze prompt, candidate set, gateway or data distribution.
### images
[Images](typesafe--decision-model-docs/images.md): experimental/not production-ready warning, explicit danger-zone header, PNG/JPEG input for both 1.13 and 1.14; Box needs 1.14. Images repeat in expanded context per reference. Byte/context limits and image preprocessing are separate contracts. This qualifies the article's text-only framing, not historical availability.
### fan-out
[Fan-out](typesafe--decision-model-docs/patterns--fan-out.md): evaluate independent speculative questions once over shared state; code ignores irrelevant answers.
### jaggedness
[Model jaggedness](typesafe--decision-model-docs/model-jaggedness.md): literal conditions, numeric/date errors, indirection, distraction, adversarial data, contradictory criteria, option-order effects and inability to generate prose reliably.
### design
[How to build](typesafe--decision-model-docs/concepts--how-to-build-with-system-one.md): code-owned workflow, narrow judgments, structured criteria, contrastive descriptions, probabilities as features and observation-based threshold tuning.
### routing
[Probability routing](typesafe--decision-model-docs/patterns--probability-routing.md) and [confidence routing](typesafe--decision-model-docs/patterns--confidence-routing.md): probability of intended action does not authorize it; high-probability transfer still opens confirmation. For Score, inspect probability mass across the action boundary; an expected value can obscure a split.
### batching-evidence
[Parallel-questions cookbook](typesafe--decision-model-docs/cookbooks--parallel_questions.md): Jev 1.14.0, pinned 53,777-character document, 13 questions, five repeats/strategy; $0.000497 vs $0.006090, 0.24s vs 2.81s, 12.2× cheaper/11.8× faster. Time compares against **serial sum** of single-call latencies; concurrent singles shrink the latency advantage. Small output differences remain (six answers vary, means within .004); this tests stability, not legal-answer correctness. Separate revision from article's 1.12/10× figure.
### api
[API schema](typesafe--decision-model-docs/api--system-one.md): request model/state/questions/assets; typed answer properties, image/long-context headers, Choice max 255, Score max 10. Its schema minItems 1 differs from article's 2–10 instructional description; no one-level score request was tested. Request/answer schemas and examples inspected, not every generated error variant.
### errors
[Request rules/errors](typesafe--decision-model-docs/api--errors.md): finite values, body/decompression limits, validation errors, 429/529 backoff. Failures are not successful model decisions.
### vendor-claims
[TypeSafe homepage](typesafe--decision-model-docs/typesafe-home.md): RLCD, speed/cost and zero-hallucination marketing. Output-space constraints do not establish semantic correctness or calibration on new tasks; the jaggedness page explicitly documents failures.
### kimi-link
[Kimi platform landing](typesafe--decision-model-docs/kimi-platform.md): resolved but insufficient to verify context size, weights, swarm capacity or current API pricing. Those article claims stay attributed/unverified.

## Why we cite this

[[concepts/typed-decision-cascades]]; creator [[creators/typesafe-ai]]. Resolves the difference between output type, numerical score, calibration evidence and effect permission.

## Related sources

- [[sources/buzzoni--jev-engineering]] — historical playbook.
- [[sources/rubriclabs--jev-use-cases]] — independently authored exploratory applications, already preserved.
- [[sources/nutlope--jev-fraud]] — pinned client pipeline and stored recording.

## Review scope

Read the twelve named pages: full substantive guidance for eleven; API inspected selectively as identified above. Long encoded playground URL in cookbook preserved but not decoded/executed. Documentation images/interactive widgets were not separately rendered or downloaded; only the primary article's nine images were visually inspected. No claims of package installation, runtime availability, calibrated error bounds, production suitability or generalized savings.
