> ## Documentation Index
> Fetch the complete documentation index at: https://docs.braintrust.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Topics

> Automatically classify logs by user intent, sentiment, and issues, then turn what you find into evaluation datasets, scorers, and review queues.

[** Topics**](https://www.braintrust.dev/app/~/topics) automatically analyze and classify your logs to surface the failures, edge cases, and recurring problems hiding across your traces. Use Topics for:

* **Blind-spot detection**: Surface user request types and system gaps you didn't know to look for.
* **Silent failure detection**: Catch quality issues that don't trip explicit checks.
* **Product roadmap signals**: Cluster real user requests into themes to inform what to build.
* **Targeted evaluation datasets**: Filter classified logs to build datasets for focused evals.

> [!TIP]
>
> Topics classifies every trace, which tells you what your logs are about. To have Loop investigate a smaller set of traces in depth and recommend what to do next, see [Patterns](https://docs.braintrust.dev/observe/patterns.md). Neither requires the other. [Patterns and Topics](https://docs.braintrust.dev/observe/patterns.md#patterns-and-topics) compares them side by side.

> [!NOTE]
>
> For self-hosted deployments, Topics requires data plane v2.x or later and access granted by your account team. See the [v2.x upgrade guide](https://docs.braintrust.dev/admin/self-hosting/upgrade/v2.md#enable-topics) for setup and eligibility requirements.

## How it works

Topics runs a daily pipeline on your logs:

1. **Preprocessing** — Each trace is formatted into readable text. Messages, tool calls, and nested spans become a narrative.
2. **Facets** — For each facet (Task, Sentiment, Issues), an LLM analyzes the preprocessed trace and extracts a short summary describing the trace through that lens.
3. **Topics** — Once at least 100 facet summaries are collected, a clustering algorithm groups similar summaries into topics. For example, "User wants a refund," "Requesting a chargeback," and "Asking for money back" might all become the topic "Refund requests."
4. **Classification** — For each facet, the trace is matched to its closest topic. These classifications appear in your logs table, where you can filter, query with SQL, and build evaluation datasets.

The pipeline runs on a set cadence:

* **Initially**: Existing logs are optionally backfilled with facet summaries.
* **Continuously**: New logs are processed as they arrive.
* **Daily**: Topics are regenerated from collected facet summaries. Generation requires at least 100 summaries.

### Group traces into conversations

Topics classifies one trace at a time by default. When a session or conversation spans multiple traces (for example, one trace per turn with [auto-instrumentation](https://docs.braintrust.dev/instrument.md)), classifications can fragment across the conversation. Configure a [grouping key](https://docs.braintrust.dev/observe/topics/manage.md#group-traces-into-conversations) so Topics classifies the group as a unit and sentiment, task, and issues reflect the full interaction.

> [!NOTE]
>
> The same grouping is available for [online scoring](https://docs.braintrust.dev/evaluate/score-online.md#configuration-parameters), which runs a scorer over the group rather than classifying it.

## Built-in facets

Topics ships with three built-in facets that classify your logs automatically:

* **Task**: Extracts the user's intent or goal (e.g., "Creating a dataset," "Debugging an API error").
* **Sentiment**: Extracts the user's emotional tone (e.g., "POSITIVE," "FRUSTRATED," "NEUTRAL").
* **Issues**: Identifies problems with agent behavior or responses (e.g., "Tool call failed," "Incomplete answer").

[Custom facets](https://docs.braintrust.dev/observe/topics/custom-facets.md) extend this set with domain-specific patterns.

## Models and data handling

Topics runs three model calls during the daily pipeline. Braintrust serves all three, not third-party LLM providers, and runs them with Zero Data Retention.

### Models

* **Facet summarization** (`brain-facet-*`): Reads each preprocessed trace or configured group of traces and writes a short summary through the lens of each facet (Task, Sentiment, Issues, or your custom facet). Choose the model in the automation's [Advanced settings](https://docs.braintrust.dev/observe/topics/manage.md#adjust-automation).
* **Embedding** (`brain-embedding-*`): Turns each summary into a vector so similar summaries can be grouped together.
* **Cluster naming** (`brain-agent-*`): Reads a sample of summaries from each cluster and picks a short, human-readable name like "Refund requests."

Braintrust serves these models on [Baseten](https://www.baseten.co/), which is included in the Braintrust [DPA](https://www.braintrust.dev/legal/dpa) as a subprocessor.

### Data retention and personal information

Every deployment, whether Braintrust-hosted (SaaS), [BYOC](https://docs.braintrust.dev/admin/deployment/byoc.md), or self-hosted, calls the same Braintrust-hosted endpoints, so Zero Data Retention (ZDR) applies to every organization. ZDR is on by default and requires no configuration. The model host doesn't store the trace text sent for inference or the summaries and topic names returned.

Facet summaries and topic names handle personal information differently:

* **Facet summaries**: Describe a trace or configured group of traces and can include names already present in those traces, such as names of people, companies, products, and features. The facet model is instructed to replace secrets, such as credentials and API keys, with a generic description like "an API key."
* **Topic names and descriptions**: Summarize patterns across traces and may be shared more broadly than the underlying trace details. The cluster naming model is instructed to omit personally identifiable information, such as people's names, email addresses, phone numbers, street addresses, and usernames, and describe the person's role instead, for example "a recurring contact." Company, product, and feature names can still appear.

### Requirements and usage

* **Built-in models required**: [Disabling built-in models](https://docs.braintrust.dev/admin/ai-providers.md#manage-built-in-models) automatically pauses your topic automations. Re-enabling them doesn't resume the automations, so [resume each one manually](https://docs.braintrust.dev/observe/topics/manage.md#pause-resume-automation).
* **Self-hosted**: Built-in models are disabled by default. [Enable them](https://docs.braintrust.dev/admin/ai-providers.md#manage-built-in-models) before using Topics.
* **Starter and Pro plans**: Topics usage draws down your [model credits](https://docs.braintrust.dev/plans-and-limits.md#usage-limits), shared with the built-in models, and continues at the [on-demand token rates](https://docs.braintrust.dev/plans-and-limits.md#model-credits) once your credits are exhausted.

## Next steps

* [Enable Topics](https://docs.braintrust.dev/observe/topics/enable.md) by checking that your traces work with the Thread preprocessor and turning on the daily pipeline.
* [Review insights](https://docs.braintrust.dev/observe/topics/review-insights.md) by viewing topic distributions, examining traces, clustering filtered subsets, and tracking trends.
* [Act on findings](https://docs.braintrust.dev/observe/topics/act-on-findings.md) by building evaluation datasets, scoring logs by classification, and assigning topics for human review.
* [Manage Topics](https://docs.braintrust.dev/observe/topics/manage.md) by checking pipeline status, re-generating topics, adjusting sampling, and rewinding history.
* [Create custom facets](https://docs.braintrust.dev/observe/topics/custom-facets.md) for domain-specific patterns beyond the built-in Task, Sentiment, and Issues.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.