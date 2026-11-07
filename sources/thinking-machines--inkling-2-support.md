---
domain: sources
type: docs-page
url: https://thinkingmachines.ai/model-card/inkling-2-small/
retrieved: 2026-11-06
snapshot-location: sources/thinking-machines--inkling-2-support/
last-reviewed: 2026-11-06
---

# Inkling 2 Small — model card, customization evidence and Tinker contracts

> Bounded supporting collection; documentation, author experiments and selected public code are distinct evidence classes.

## Snapshot details

- Captured November 6, 2026. [Receipt](thinking-machines--inkling-2-support/capture.json), [coverage and omissions](thinking-machines--inkling-2-support/coverage.json).
- Read all extracted prose of model card, release-policy essay, Bridgewater financial-task article, StableReinforce, Datum and model/pricing docs. Parsed the two current pricing JSON resources. Inspected selected sections of one pinned cookbook file, not the entire repository or hosted implementation. PMPP-Hard retrieval returned a title only and supplies no additional methodology evidence.
- Original model-card HTML preserves full table boundaries; the announcement's raw HTML preserves charts and replay data. Extracted docs code contains line-link prefixes; consult upstream or captured source, not these snippets verbatim as runnable code. No training/service request was executed.

## Anchor map

### model-card

[Model card](thinking-machines--inkling-2-support/model-card.md), [HTML](thinking-machines--inkling-2-support/model-card.html). Release November 5; current license field **Tinker Terms of Use**. 48-layer hybrid local/global attention decoder, 8 of 384 experts/token; image dimensions recommended 40–4096px, model context up to 1M, text output only. MXFP8/NVFP4 numerics. Training includes video data, not a promise of an audio/video input API.

### harness-results

Model-card eval table includes Terminal Bench 2.1: 85.1% Pi versus 81.3% Terminus, and v4.0 13.1%. They are different reported conditions/benchmark versions, not interchangeable measures. ScreenSpot Pro downscales images longer than 4096px and rescales answers. Full benchmark expansion is preserved; results were not reproduced.

### release-policy

[A Safe Path to Open Weights](thinking-machines--inkling-2-support/safe-open-weights.md). Capability, accessibility, removable safeguards and ecosystem readiness inform staged access. Hosted fine-tuning is between inference and downloadable weights; stages are not an automatic promise to publish. Concrete thresholds/stop criteria remain future work. Earlier Inkling/Inkling-Small risk evaluations must not be relabeled as the full new model's evidence.

### financial-labels

[Learning to Replicate Expert Judgment in Financial Tasks](thinking-machines--inkling-2-support/expert-financial-judgment.md), **Sarah Su, Kevin Zhu, Emily Xiao, Rohan Alur, Daniel Kang / Bridgewater AIA Labs**, June 2026 citation, hosted by Thinking Machines. Six information-triage tasks, proprietary expert preferences, Qwen3-235B base. Non-expert label errors were routed to experts through model/training-label disagreement; final eval held out. Disagreement is a triage signal, not proof the model was right, and agreement can hide shared mistakes.

### financial-recipe

Same Bridgewater study: task-wise round-robin batches, CISPO/asymmetric clipping, on-policy distillation; promote teacher every 20 steps only on a new validation best. Reports 84.7% accuracy versus 78.2% best tested frontier prompt baseline and 13.8× lower inference cost per task. Leave-one-out ablations are not additive gains; this is information relevance/segmentation, not investment-return prediction or generalized financial correctness.

### stable-reinforce

[StableReinforce alpha docs](thinking-machines--inkling-2-support/stable-reinforce.md). Sampler records stability info; datums carry provenance. Same-session sequences are initially trainable for one day; each training use renews that day. KL compares sampler q to learner p, **not** a reference teacher. k1/k3 estimators differ; k1's gradient does not depend on supplied sampling logprobs, while k3's does. Stability is a vendor-reported property, not proven here for arbitrary lag/numerics.

### datum-provenance

[Datum](thinking-machines--inkling-2-support/datum.md). Input/target shift, variable-length batches handled by service; prompt/sampled provenance spans must tile both fields and remain in the same session. Docs say the server checks ranges and exact whole-sequence/prompt tokens. StableReinforce requires complete sampled target spans and recorded stability data for nonzero-advantage tokens. Metadata correctness is not a cryptographic proof of honest task completion.

### pricing

[Pricing docs](thinking-machines--inkling-2-support/models-and-pricing.md), [models JSON](thinking-machines--inkling-2-support/models.json), [serverless JSON](thinking-machines--inkling-2-support/serverless.json). Per-million-token capture: Inkling 2 Small prefill $0.30/$0.03 cached, sample $1.00, train $1.50 at 64K or $3.00 at 256K. Storage $0.10/GB-month; forward-only training-client calls bill at training rate. Serverless beta: 256K, input $0.30/$0.03 cached, output $1.00; production waitlist described. Exact IDs/limits belong to each surface, not the general model-card maximum. Prices are dated inputs, not lasting recommendations.

### async-source

Captured [rl/train.py](thinking-machines--inkling-2-support/rl-train.py), pinned to [4a3a2829190b45999021e423bc90b7523108edf4](https://github.com/thinking-machines-lab/tinker-cookbook/blob/4a3a2829190b45999021e423bc90b7523108edf4/tinker_cookbook/rl/train.py#L421-L480). Read `_check_provenance` (281–299), `AsyncConfig` (421–480), slot allocation (1280–1335), oldest-completed grouping (1377–1410), staleness/slot release (1518–1532). Work-in-flight cap is groups × (max_steps_off_policy + 1), not a hard maximum age: slow completed groups are retained. Unfinished rollouts can hold slots; timeout policy is required where environments hang. Streaming can fail on a later bad datum after earlier minibatches were sent. [Apache-2.0 license retained](thinking-machines--inkling-2-support/cookbook-LICENSE). This single-file inspection does not validate Tinker's backend or the entire training recipe.

### incomplete-context

[PMPP title-only attempt](thinking-machines--inkling-2-support/pmpp-hard-attempt.md). No benchmark-author methodology was recovered. Announcement, linked background paper names and external leaderboard claims remain separately attributed; not every citation was independently followed.

## Why we cite this

Adds contract-level qualifications and source-level async scheduling detail to [[artifacts/projects/inkling-2-small]], without treating model release plans or reward curves as deployment guarantees.

## Related sources

- [[sources/thinking-machines--inkling-2-small]] — requested announcement.
