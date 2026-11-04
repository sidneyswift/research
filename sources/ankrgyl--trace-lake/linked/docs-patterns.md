> ## Documentation Index
> Fetch the complete documentation index at: https://docs.braintrust.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Patterns

> Let Loop investigate your traces on a schedule and record recurring problems and trends as patterns, each with supporting evidence and a suggested fix.

Once you're [capturing traces in Braintrust](https://docs.braintrust.dev/tracing-quickstart.md), [** Patterns**](https://www.braintrust.dev/app/~/patterns) uses [Loop](https://docs.braintrust.dev/loop.md) to find recurring problems and trends, including behavior your scorers don't measure.

A pattern is a saved finding with supporting evidence, an explanation, and a suggested next step. A severity level helps you prioritize findings and filter the list by impact, and a category describes the kind of finding.

> [!WARNING]
>
> Patterns is in [public preview](https://docs.braintrust.dev/feature-lifecycle.md) and can change before reaching general availability.

![Patterns](https://mintcdn.com/braintrust/Mpah3XDvMklMcbs-/images/observe/patterns.png?fit=max\&auto=format\&n=Mpah3XDvMklMcbs-\&q=85\&s=6f229a579369b58a877bcbe6d6edb33a)

Use Patterns to:

* Find recurring failures and regressions.
* Track cost and latency drift in recurring LLM calls.
* Discover recurring successes and emerging use cases.
* Give a coding agent the evidence it needs to implement a fix.

> [!TIP]
>
> To learn how to use Patterns to find recurring problems in your team's coding-agent sessions, read [Improving coding agents with coding agent insights](https://docs.braintrust.dev/cookbook/recipes/CodingAgentInsights.md).

## How discovery works

Patterns runs as a scheduled [Loop automation](https://docs.braintrust.dev/loop/automations.md). You can also ask Loop to [find patterns](https://docs.braintrust.dev/loop/capabilities.md#find-patterns) in an interactive thread. They appear in the same list.

### Goals

Each run has three goals:

* **Discover new patterns.** Following your instructions, Loop samples traces randomly from the start, middle, and end of the query range, and examines each tool's output separately to catch rarely used tools. It also looks for failures that tools return in their output without setting `error`. Loop investigates candidates and saves findings with supporting evidence. A run can find nothing new.
* **Refresh existing patterns.** Loop updates evidence and [affected-trace measurements](https://docs.braintrust.dev/observe/patterns/review.md#affected-traces) and rechecks unmeasured patterns against recent similar traces. It updates wording when the finding changes or rewrites it once to follow revised writing guidance, preserving the finding's meaning and stored evidence.
* **Close patterns that have stopped.** Loop closes an active pattern when the behavior hasn't occurred in the previous two weekdays, including in similar traces its filter might miss. The [quality and reasons](https://docs.braintrust.dev/observe/patterns/review.md#close-or-reopen) you give when closing a pattern guide later findings.

At the end of a run, Loop reports which patterns it checked, which it couldn't check, and which were out of scope.

### Verification

Before saving or closing a pattern, Loop checks its work:

* **Explanatory factors:** Loop compares groups of traces by attributes such as model, agent settings, integrations, or experiment variant, and reports the comparison in the pattern's summary. A difference doesn't prove a cause.
* **Source code and requirements:** Before saving a new pattern, Loop reviews the finding against the relevant code in a [connected repository](https://docs.braintrust.dev/loop/github.md) and checks requirements from an [external MCP server](https://docs.braintrust.dev/loop/mcp.md). The review can confirm, reword, or drop the finding, and Loop saves cited code as the pattern's [Sources](https://docs.braintrust.dev/observe/patterns/review.md#sources). Without source access, the finding labels unconfirmed causes as hypotheses.
* **Uncertain results:** Missing data or a failed query isn't evidence. When Loop can't confirm something, it keeps the pattern's status and reports what it couldn't check.

## Requirements

* **Traces.** [Traces logged to your project](https://docs.braintrust.dev/tracing-quickstart.md).
* **Model access.** Braintrust's [built-in models](https://docs.braintrust.dev/admin/ai-providers.md#available-models) use your monthly [model credits](https://docs.braintrust.dev/plans-and-limits.md#model-credits) and need no setup if you meet the [requirements](https://docs.braintrust.dev/admin/ai-providers.md#requirements). To use your own key or continue after credits run out, configure a compatible [AI provider](https://docs.braintrust.dev/loop/manage.md#models-and-providers).
* **Project permissions.** Enabling Patterns requires permission to create project automations, included in the **Owners** and **Engineers** [permission groups](https://docs.braintrust.dev/admin/access-control.md#built-in-permission-groups). Anyone who can read the project's logs can read patterns. Closing and reopening a pattern, correcting its severity or categories, and backfilling missing severity also require the project's [`Update` permission](https://docs.braintrust.dev/admin/access-control#object-permissions).
* **Self-hosted deployments.** Data plane v2.13 or later and an enabled [Loop runtime](https://docs.braintrust.dev/admin/self-hosting/configure/loop-runtime.md), which is available only on AWS.

## Patterns and Topics

[Topics](https://docs.braintrust.dev/observe/topics.md) classifies and clusters traces so you can filter and chart them by user intent, sentiment, or issue. Patterns investigates findings in depth. Neither requires the other.

| | Topics | Patterns |
| - | - | - |
| Question it answers | What themes occur most often? | What keeps happening, why does it matter, and what should we do next? |
| Output | A classification on every trace | A focused set of findings, each with evidence and a suggested fix |
| Scope | Broad, across all your traces | Scans your traces, then investigates a subset of them in depth |
| Models | Braintrust built-in models, drawing on your [model credits](https://docs.braintrust.dev/plans-and-limits.md#model-credits) | The same built-in models by default, or your own configured AI provider |
| Cadence | Daily pipeline | Scheduled Loop automation |

Topics runs as a separate, low-cost pipeline on Braintrust-served models, regardless of your Loop model selection.

Loop can use topic classifications, scores, and human feedback in its investigations. It can also turn a pattern into a facet, scorer, classifier, or monitor to measure the behavior continuously at lower cost. See [Act on a pattern](https://docs.braintrust.dev/observe/patterns/review.md#act-on-a-pattern).

## Next steps

* [Enable Patterns](https://docs.braintrust.dev/observe/patterns/enable.md) and configure how often Loop looks for them.
* [Review and act on patterns](https://docs.braintrust.dev/observe/patterns/review.md) once the first run finishes.
* [Discover insights with Topics](https://docs.braintrust.dev/observe/topics.md) to classify your traces at a broader scale.
* [Run Loop on a schedule](https://docs.braintrust.dev/loop/automations.md) for recurring analysis beyond pattern discovery.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.