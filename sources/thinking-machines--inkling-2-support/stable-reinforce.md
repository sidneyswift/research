Alpha

StableReinforce is in alpha, and its API may change.

StableReinforce (stable_reinforce) is a REINFORCE variant that stays stable even when the sampling policy differs from the policy being trained, such as in async RL or when training and sampling use different numerics. In our internal post-training, this loss function has led to extremely stable training, even under highly off-policy async RL and low precision numerics. The objective uses minimal additional information captured at sampling time, so you need to sample with record_stability_info=True and annotate your training tokens with corresponding sequence_ids from sampling.

## Sampling with stability info

Create the sampling client with record_stability_info=True. Every sample from that client is recorded, and each returned sequence carries a sequence_id that training requests use to name it:

https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-0-1sampling_client = await training_client.save_weights_and_get_sampling_client(
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-0-2 record_stability_info=True
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-0-3)
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-0-4response = await sampling_client.sample(
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-0-5 prompt=prompt,
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-0-6 sampling_params=params,
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-0-7 num_samples=4,
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-0-8)
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-0-9sequence = response.sequences[0]
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-0-10sequence.sequence_id # names this sequence in a training request

ServiceClient.create_sampling_client and TrainingClient.create_sampling_client take the same argument.

Recorded sequences belong to the session that sampled them, and can be trained on for one day after sampling. Each training request that uses a sequence restarts that day.

## Training

StableReinforce is one of the features that need [provenance](https://tinker-docs.thinkingmachines.ai/tinker/datum/#provenance): every datum must identify the sampled sequence behind each of its tokens. Beyond the general provenance checks, it requires:

- Both span lists on every datum.

- At least one SampledProvenanceSpan in the loss_fn_inputs spans, each covering its whole sequence (offset=0 and the sequence's full length). Spans on the model input may cover part of a sequence.

- Every token with a nonzero advantage under a SampledProvenanceSpan whose sequence was sampled with record_stability_info=True.

With datums built as in the [provenance example](https://tinker-docs.thinkingmachines.ai/tinker/datum/#provenance):

https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-1-1future = training_client.forward_backward(
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-1-2 data, loss_fn="stable_reinforce", loss_fn_config={"kl_coeff": 0.01}
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-1-3)
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-1-4result = await future

Input tensors:

- target_tokens: array[(N,), int] — Target token IDs (from the sampler \(q\))

- logprobs: array[(N,), float] — sampling_logprobs for the tokens

- advantages: array[(N,), float] — Advantage values for RL

Output tensors:

- logprobs: array[(N,), float] — target_logprobs for the tokens

Output diagnostics:

- loss:sum (scalar) — Summed loss, for monitoring

## Sampler–learner KL

The loss includes a KL term between the sampler \(q\) and the learner \(p_\theta\). This is not a KL to a reference model; the loss uses no reference policy. It is estimated on each sampled token \(x_t\), the tokens under a SampledProvenanceSpan, with one of two estimators.

k1 (the default):

\[
\mathcal{L}_{\text{KL}}(\theta) = \beta \sum_t \left(\log q(x_t) - \log p_\theta(x_t)\right)
\]

Its gradient, \(-\beta \sum_t \nabla_\theta \log p_\theta(x_t)\), raises the learner's probability of every sampled token regardless of its advantage, keeping the learner close to the sampler. The gradient doesn't depend on the logprobs you send; they only shift the reported value.

k3, with \(r_t = p_\theta(x_t) / q(x_t)\):

\[
\mathcal{L}_{\text{KL}}(\theta) = \beta \sum_t \left(r_t - 1 - \log r_t\right)
\]

Every token's term is at least 0. Its gradient, \(\beta \sum_t (r_t - 1) \nabla_\theta \log p_\theta(x_t)\), lowers the learner's probability of tokens it favors more than the sampler did and raises it for tokens it favors less. Because \(r_t\) uses \(q\), the gradient depends on the logprobs you send, and it grows quickly on tokens where the learner's probability far exceeds the sampler's.

Both are sample estimates of \(\mathrm{KL}(q \,\|\, p_\theta)\) scaled by \(\beta\). Configure the term through loss_fn_config:

- kl_coeff — \(\beta\), a finite float ≥ 0 (default 0.01); 0 turns the term off

- kl_estimator — "k1" (default) or "k3"

https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-2-1future = training_client.forward_backward(
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-2-2 data,
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-2-3 loss_fn="stable_reinforce",
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-2-4 loss_fn_config={"kl_coeff": 0.01, "kl_estimator": "k3"},
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-2-5)
https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/#__codelineno-2-6result = await future
