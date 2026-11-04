> ## Documentation Index
> Fetch the complete documentation index at: https://docs.braintrust.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Loop on a schedule

> Configure a Loop automation to investigate your project on a schedule, control what it's allowed to change, and send results to Slack, PagerDuty, or a webhook.

Use Loop automations to investigate project data on a schedule and optionally send results to Slack, PagerDuty, or a webhook. For example:

* Review cost or latency on a schedule.
* Check whether quality is degrading.
* Summarize recent errors.
* Review logs using the filters from a dashboard.
* Send a Slack or webhook digest after each run.

> [!TIP]
>
> [Enable Patterns](https://docs.braintrust.dev/observe/patterns/enable.md) to discover recurring problems and trends your scorers may miss, with supporting traces and suggested next steps. The discovery instruction and write permissions are preconfigured for you.

## Create a Loop automation

To create a Loop automation, go to ** Settings** > [** Loop**](https://www.braintrust.dev/app/~/configuration/automations/loop) and click  **Loop automation**.

You can also create or edit automations from [** Loop**](https://www.braintrust.dev/app/~/loop). Click ** Automations** in the page header, then select **Create Loop automation** or an existing automation to edit.

**1. Define the investigation**

Enter a **Name** to identify the automation in Settings and an optional **Description**, then configure:

* **Instruction:** Describe what to inspect, how deeply to investigate, what to return, and when to stop. Use these techniques to make runs more consistent:

  * **Pin the time range.** Use the automation's query window to keep consecutive runs comparable.
  * **Specify the output.** Define the format and columns so recurring digests are consistent.
  * **Define exclusions.** State what Loop should exclude or avoid inferring, such as guessing names or treating explicitly requested behavior as a failure.

  See [Loop automation recipes](#loop-automation-recipes) for complete examples you can adapt.

* **Agent configuration:** Choose the model, reasoning effort, and whether to use Braintrust's built-in models or your own [AI providers](https://docs.braintrust.dev/admin/ai-providers.md). See [Models and providers](https://docs.braintrust.dev/loop/manage.md#models-and-providers).

  * Built-in models use your monthly [model credits](https://docs.braintrust.dev/plans-and-limits.md#model-credits), and automations that use them [pause](#pause-an-automation) when credits run out. Other models bill to their providers. Runs that inspect more data cost more, so keep instructions focused on a narrow slice of traces.
  * New automations use **Auto**, which follows your organization's [default provider for Loop](https://docs.braintrust.dev/admin/organizations.md#set-a-default-provider-for-loop) and its recommended model and reasoning effort, including later changes to the default. To choose the model, provider, and effort yourself, turn off **Auto** in the model picker. If the default becomes unavailable, automations with **Auto** on [pause](#pause-an-automation).

**2. Set the schedule and query range**

* **Frequency:** Choose **Daily**, **Weekly**, **Interval**, or **Custom (cron)**. Daily and weekly schedules include a run time and show the next scheduled run. Custom cron uses five fields: minute, hour, day of month, month, and day of week. Select a timezone beside the cron expression. Schedule previews use the schedule's timezone.
* **Continuous:** Turn on to check for new traces between scheduled runs and analyze them in the current run's thread. It's off by default. Each scheduled run still starts a new thread.
* **Default query range:** Choose 3 hours, 6 hours, 12 hours, 1 day, 3 days, 7 days, or a custom range. Each run inspects the full range, not only traces created since the previous run.

> [accordion] How continuous checks work
>
> Between scheduled runs, Braintrust checks every 15 to 45 minutes. If more than 1,000 new traces have arrived since the last analysis, Loop analyzes them in the current run's thread and sends only significant new findings to your destinations, not a full report.
>
> Interval schedules of 1 hour or less skip these checks. Continuous isn't available for automations with a threshold condition.

**3. Set write permissions**

In an interactive thread, actions that change something pause for your approval. A scheduled run has nobody to ask, so it relies on its **Write tool permissions** instead.

* Read-only tools never require approval, so a run can always inspect project data such as traces, existing patterns, experiments, and datasets.
* Automations created from the [\*\* Patterns\*\*](https://www.braintrust.dev/app/~/patterns) page can create and update pattern records by default. A pattern record can include trace evidence, monitor chart configurations, and recommendations for measuring the pattern later. Creating scorers, facets, or other project objects requires the corresponding write tools.
* To let a run create or modify other project objects, add the corresponding tools. The dropdown lists what each one permits.
* Automation runs can read [connected GitHub repositories](https://docs.braintrust.dev/loop/github.md) but can't push branches or open pull requests, even when write access is on. GitHub writes require an interactive thread.

Enabling a tool lets scheduled runs make that kind of change without asking. Choose only the tools the automation needs.

> [!WARNING]
>
> The **Write tool permissions** selection applies to Braintrust tools. All tools from [connected project MCP servers](https://docs.braintrust.dev/loop/mcp.md) are available to scheduled runs without interactive approval, including Patterns automations. Restrict external access through the permissions of the shared API key or OAuth account.

> [!WARNING]
>
> Allowing a run to create or update online scoring rules can start work that continues after the run ends. Online scoring rules score production traffic continuously and keep costing money until you stop them.

Objects a run creates are not linked back to any pattern it recorded. If a pattern's monitor chart measures a scorer or facet the run created, deleting that object stops new data from reaching the chart.

**4. Choose destinations**

Destinations are optional. Every run's results are available in Braintrust on the automation's [**Past runs**](#review-past-runs) tab, and any patterns it records appear in the [\*\* Patterns\*\*](https://www.braintrust.dev/app/~/patterns) list. Add a destination when you also want each run pushed to your team.

Click **+ Destination** in the configuration panel, then choose one of the following:

* &#x20;**Send to Slack.** Select a channel in a [connected Slack workspace](https://docs.braintrust.dev/admin/organizations.md#enable-slack-integration). Patterns automations send [per-pattern alerts](https://docs.braintrust.dev/observe/patterns/enable.md#slack-notifications). Other Loop automations post a text digest, which you can customize with the destination's **Formatting prompt**.
* &#x20;**Send to PagerDuty.** Enter a 32-character **PagerDuty integration key** and choose **Critical**, **Error**, **Warning**, or **Info** severity. The default is **Critical**. Failed runs also trigger incidents, which resolve after the next successful run. PagerDuty destinations require data plane v2.17.0 or later for self-hosted deployments.
* &#x20;**Send to webhook.** Enter a URL to send run results to an external service. Use the **Formatting prompt** to describe the JSON payload Loop should produce.

If no Slack workspace is connected, the destination menu depends on your organization permissions:

* **[Owners](https://docs.braintrust.dev/admin/access-control.md) or a custom permission group with Manage settings:** Click **Connect to Slack** to connect a workspace in a new tab. When you return, the workspace list refreshes and the menu offers  **Send to Slack**.
* **Without those permissions:** The menu shows **Ask an org admin to connect Slack**.

Only automation runs send results to destinations. Interactive threads, including those created with **Fork to chat**, don't send results to destinations, even when they add patterns to the Patterns list. To send new results without waiting for the schedule, [run the automation manually](#run-an-automation-now).

Click **Create** to save the automation.

## Run an automation now

A manual run lets you test an instruction or get results without waiting for the schedule. The next scheduled run still happens at its usual time. You need project [**Update**](https://docs.braintrust.dev/admin/access-control/manage-permissions.md#set-project-permissions) permission, and you can't run a paused automation.

To run a saved automation, open it and click  **Run now**. What happens depends on whether the automation is continuous:

* **Without continuous mode:** Braintrust starts a one-off run in a new thread. The run covers the most recent query range, ending at the current time minus any evaluation delay.
* **With continuous mode:** If more than 1,000 traces have arrived since the current run's last analysis, Loop continues the current thread. Otherwise, or if there's no current run, Braintrust starts a full run in a new thread. If a run is already in progress, nothing new starts.

To open the run's thread once it starts, go to the automation's [**Past runs**](#review-past-runs) tab.

To start a full run in a new thread for a continuous automation, click  next to **Run now** and select **Run in new thread**. Later checks continue that new thread. This option appears only for continuous automations.

## Loop automation recipes

Adapt these recipes to review cost and quality, summarize errors, or discover patterns. Each includes a schedule, query range, write permissions, and an instruction you can customize for your project.

> [accordion] Weekly cost report
>
> Posts a cost breakdown to Slack every Monday morning.
>
> | Field | Value |
> | - | - |
> | **Frequency** | Weekly, Mondays at 9:00 AM |
> | **Default query range** | 7 days |
> | **Write tool permissions** | None. The run only reads and reports. |
> | **Destinations** | Send to Slack |
>
> ```text wrap Instruction theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> Create a weekly estimated-cost report for this project.
>
> Periods:
> - Use the automation's seven-day window as the current period.
> - Compare it with the immediately preceding seven days.
> - State both UTC date ranges in the report.
>
> Cost by user:
> - Query project logs separately for each period.
> - Group by `span_attributes.created_by_user_id` and sum `metrics.estimated_cost`.
> - Keep null creator IDs as `Unattributed`, and never guess a name.
>
> Return only:
> 1. A Markdown table with columns `User`, `Past 7 days`, `Prior 7 days`, `Change`.
> 2. One sentence summarizing the total week-over-week change.
> 3. A short paragraph on which work drove the spend, based on the highest-cost
>    traces in the window. Describe the tasks, not the people.
> ```

> [accordion] Daily quality review
>
> Compares existing quality scores with the previous day and investigates possible regressions. This example uses `scores.factuality`, with higher values indicating better quality. Replace it with a score your project already records and adjust the direction if lower values are better.
>
> | Field | Value |
> | - | - |
> | **Frequency** | Daily |
> | **Default query range** | 1 day |
> | **Write tool permissions** | None. The run only reads and reports. |
> | **Destinations** | Send to Slack |
>
> ```text wrap Instruction theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> Review factuality in this project's logs for signs of degrading quality.
>
> Compare:
> - Use the automation's one-day window and the immediately preceding day.
> - State both UTC date ranges. For each period, report the average of
>   `scores.factuality` and the number of scored rows. Higher scores are better.
> - Exclude missing scores from the average and report how many rows lack scores.
> - If either period has no scores, report that the comparison is unavailable.
>
> Investigate:
> - If the average falls, inspect up to 10 low-scoring traces from the current
>   period and up to 10 scored traces from the previous period.
> - Check whether the tasks or traffic mix changed. Distinguish observed score
>   changes from possible causes, and do not treat a small sample as proof.
> - Use existing scores only. Do not run scorers or create scoring rules.
>
> Return a comparison table, a short summary of the evidence and its limitations,
> and up to three representative trace links with suggested follow-up checks.
> ```

> [accordion] Recent error summary
>
> Summarizes errors in the same subset of logs you monitor on a [dashboard](https://docs.braintrust.dev/observe/dashboards.md). Replace `metadata.environment = 'production'` with the filter conditions from your dashboard. Include the conditions in the instruction so the run has the scope it needs.
>
> | Field | Value |
> | - | - |
> | **Frequency** | Daily |
> | **Default query range** | 1 day |
> | **Write tool permissions** | None. The run only reads and reports. |
> | **Destinations** | Send to Slack |
>
> ```text wrap Instruction theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> Summarize recent errors for the production environment in this project.
>
> Scope:
> - Use the automation's one-day window and state the UTC date range.
> - Select traces matching `metadata.environment = 'production'` and inspect
>   their spans for recorded errors. If the field is unavailable, report that
>   the scope cannot be applied instead of broadening the search.
>
> Investigate:
> - Group similar recorded errors and count distinct affected root traces in
>   each group. Do not count repeated errors in one trace as separate incidents.
> - Inspect up to three representative traces from each of the five largest
>   groups. Check whether the operation recovered later in the trace.
> - Distinguish recorded errors from confirmed failures visible to the end user.
>   If the outcome is unclear, say so. Do not guess a root cause.
>
> Return a table with each error group, its affected trace count, and a
> representative trace link, followed by suggested follow-up checks.
> If there are no recorded errors in scope, say so rather than inventing groups.
> ```

> [accordion] Focused pattern discovery
>
> Narrows pattern discovery to one concern, using an existing [facet](https://docs.braintrust.dev/observe/topics/custom-facets.md) to choose which traces to investigate. Run this alongside the default **Pattern discovery** automation when a specific area deserves its own cadence.
>
> | Field | Value |
> | - | - |
> | **Frequency** | Daily |
> | **Default query range** | 7 days |
> | **Write tool permissions** | Create and update patterns |
> | **Destinations** | Optional |
>
> ```text wrap Instruction theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> Analyze recent project traces to find recurring failures within the existing
> "Primary failure mode" facet's topic classifications.
>
> Use the facet and its topic classifications only to select candidates. They are
> noisy, and are not evidence by themselves.
>
> Workflow:
> 1. Use the automation window.
> 2. Collect a sample of 100-200 facet occurrences, spread across the available
>    topic classifications rather than only the newest or largest cluster.
> 3. Cap the sample at two occurrences per root trace, and deduplicate repeated
>    facet runs and copies of the same underlying conversation.
> 4. For each candidate, inspect the compact context around the occurrence: the
>    user request, agent actions, tool results, and outcome.
> 5. Validate every proposed pattern against raw trace evidence. Reject any
>    hypothesis explained by explicit user direction, a permission or environment
>    block, or intentional fail-fast behavior.
>
> Record a pattern only when it describes a specific recurring behavior, is
> supported by at least three independent conversations, has a meaningful impact
> and an actionable response, and includes short quotes and relevant span IDs.
> ```

## Review past runs

Open the automation, select **Past runs**, and select a run to review the work Loop did.

* **Run history:** Each run creates a read-only thread that stays with its automation. These threads don't appear in the [** Loop**](https://www.braintrust.dev/app/~/loop) page's thread list and can't be deleted like interactive threads.
* **Follow-up questions:** Select  **Fork to chat** to copy the transcript into a private, editable thread where you can investigate the run. The fork does not have access to the automation's Slack or webhook destinations.
* **Failed runs:** Select **Retry & continue** to resubmit the latest failed turn in the same thread. This action applies to a failed automation run, not a delivery request from an interactive fork. Retry requires project [**Update**](https://docs.braintrust.dev/admin/access-control/manage-permissions.md#set-project-permissions) permission and expires four days after the run. It uses the run's original settings and saved destinations, even if you've changed the automation.

## Pause an automation

Pause an automation to stop its scheduled runs while keeping its configuration and history. Do this when you're tuning an instruction, controlling spend, or investigating a run that behaved unexpectedly. Objects its runs already created stay in your project.

To pause, open the automation and turn off **Active**. The rule then shows as **Paused** in ** Settings** > [** Loop**](https://www.braintrust.dev/app/~/configuration/automations/loop). Turn **Active** back on to resume the schedule.

**Automatic pauses.** An automation that uses a built-in model, or has **Auto** on, pauses automatically when it can't run. The automation list marks it with a warning indicator, and opening it shows a banner with the reason:

* **Default provider unavailable:** The automation has **Auto** on and the default provider can't serve it. Click **Configure default** to update the default, or turn off **Auto** and choose another provider.
* **Credit limit reached:** Your model credits are depleted. The automation doesn't switch to your own AI providers on its own. Choose another provider or add a payment method.
* **Provider unavailable:** The selected built-in model is unavailable, or built-in models are disabled for your organization. Click **AI provider settings** to review your providers, or **Add provider** if your organization has no configured providers.

## Delete an automation

> [!WARNING]
>
> Deleting an automation is permanent. If you might want the automation again, pause it instead.

To delete an automation, delete the rule from ** Settings** > [** Loop**](https://www.braintrust.dev/app/~/configuration/automations/loop).

Deleting an automation doesn't affect the objects its runs already created. Patterns, scorers, facets, and other objects a run produced remain in your project, and any online scoring rules a run created keep running until you stop them separately.

## Next steps

* [Enable Patterns](https://docs.braintrust.dev/observe/patterns/enable.md) for scheduled pattern discovery.
* [Set up alerts](https://docs.braintrust.dev/observe/alerts.md) for conditions you can already define, without an agent run.
* [What Loop can do](https://docs.braintrust.dev/loop/capabilities.md) to decide what's worth automating.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.