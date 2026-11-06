A Datum is a single training example: the tokens the model reads, plus the tensors its [loss function](https://tinker-docs.thinkingmachines.ai/tinker/losses/) needs.

- model_input — the input token sequence, of length N.

- loss_fn_inputs — a dict of per-token tensors, each with one row per input position: shape (N,), or (N, K) for inputs that carry K values per position. It always holds target_tokens, plus whatever else the loss takes (weights for cross-entropy; logprobs and advantages for RL losses).

The sequence length N can differ between Datums in the same batch. [TrainingClient.forward](https://tinker-docs.thinkingmachines.ai/tinker/api-reference/trainingclient/#forward), [forward_backward](https://tinker-docs.thinkingmachines.ai/tinker/api-reference/trainingclient/#forward_backward), and [forward_backward_custom](https://tinker-docs.thinkingmachines.ai/tinker/api-reference/trainingclient/#forward_backward_custom) accept a list of individual Datums with different lengths. You don't need to pad examples to a common length or pack them into a single sequence; Tinker handles batching and packing internally.

Position i of the input predicts token i + 1, so both are built from the full sequence, shifted by one:

https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-0-1full_sequence = prompt_tokens + completion_tokens
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-0-2
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-0-3datum = types.Datum(
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-0-4 model_input=types.ModelInput.from_ints(full_sequence[:-1]),
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-0-5 loss_fn_inputs={
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-0-6 "target_tokens": full_sequence[1:],
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-0-7 "weights": [0.0] * (len(prompt_tokens) - 1) + [1.0] * len(completion_tokens),
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-0-8 },
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-0-9)

Everything the loss needs is in the datum, so each datum is self-contained.

Pass your examples as a list:

https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-1-1# Each Datum can have a different sequence length.
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-1-2future = training_client.forward_backward(
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-1-3 [short_datum, long_datum],
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-1-4 loss_fn="cross_entropy",
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-1-5)
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-1-6result = await future

## Provenance

Some features need information captured when tokens were sampled. To use it at training time, the datum has to identify the sampled sequence behind each of its tokens. That annotation is the datum's provenance.

Provenance works only within one session

A training request can only name sequences sampled in its own session. Sample and train in the same session.

Every sequence a sampling request returns carries a sequence_id. Provenance is a list of runs naming those IDs:

- PromptProvenanceSpan(sequence_id, offset, length) — tokens [offset, offset + length) of the sequence's prompt.

- SampledProvenanceSpan(sequence_id, offset, length) — tokens [offset, offset + length) of the sequence's sampled tokens.

Datum.with_provenance attaches two lists of runs: one for model_input and one for target_tokens. Each list tiles its field: runs cover consecutive positions, and their lengths sum to the field's length. For a prompt and one sampled sequence, the input covers the prompt and all but the last sampled token, and the targets cover the same tokens shifted by one:

https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-1from tinker import types
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-2
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-3prompt_tokens = prompt.to_ints()
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-4sampled_tokens = sequence.tokens
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-5sid = sequence.sequence_id
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-6n_prompt, n_sampled = len(prompt_tokens), len(sampled_tokens)
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-7
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-8datum = types.Datum(
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-9 model_input=types.ModelInput.from_ints(prompt_tokens + sampled_tokens[:-1]),
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-10 loss_fn_inputs={
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-11 "target_tokens": prompt_tokens[1:] + sampled_tokens,
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-12 "logprobs": [0.0] * (n_prompt - 1) + sequence.logprobs,
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-13 "advantages": [0.0] * (n_prompt - 1) + [advantage] * n_sampled,
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-14 },
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-15).with_provenance(
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-16 model_input=[
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-17 types.PromptProvenanceSpan(sequence_id=sid, length=n_prompt),
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-18 # A one-token completion has no sampled token in the input; omit this run then.
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-19 types.SampledProvenanceSpan(sequence_id=sid, length=n_sampled - 1),
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-20 ],
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-21 loss_fn_inputs=[
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-22 types.PromptProvenanceSpan(sequence_id=sid, offset=1, length=n_prompt - 1),
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-23 types.SampledProvenanceSpan(sequence_id=sid, length=n_sampled),
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-24 ],
https://tinker-docs.thinkingmachines.ai/tinker/datum/#__codelineno-2-25)

Any loss accepts provenance, and the server checks it on every request. Each run must fit inside the sequence it names, and a run covering a whole sampled sequence must carry exactly that sequence's tokens, as must a model input run covering a whole prompt.

Features that require provenance:

- [StableReinforce](https://tinker-docs.thinkingmachines.ai/tinker/losses/stable-reinforce/)
