> ## Documentation Index
> Fetch the complete documentation index at: https://docs.braintrust.dev/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter and search logs

> Narrow down to exactly the traces you need using metadata filters, SQL queries, or the API. Pull out specific production data for debugging, analysis, or dataset creation.

Narrow down to specific traces by applying a filter via the UI, CLI, or API. Paste ready-made patterns from [Common filters](#common-filters), or save a useful combination as a [shared table view](#save-and-share-filters). When you don't have an exact filter in mind, ask [Loop](#ask-questions-with-loop).

## Apply a filter

> [!NOTE]
>
> On hosted Braintrust, queries against logs and playground data enforce your plan's [data retention window](https://docs.braintrust.dev/plans-and-limits.md#usage-limits) (14-day retention on Starter, 30-day retention on Pro by default) across every query path: the UI, CLI, API, and MCP. Experiments have up to 365-day retention on all plans. Data older than the window is silently filtered out rather than returned as an error, so use a relative interval to stay within the window. On Enterprise, the window is the custom retention arranged with your account team.

> [tab] UI
>
> Click the search field in the toolbar to start filtering. When the field is empty, the dropdown shows **Suggestions** for filters and **Recent** text searches and SQL filters, when available. Start typing to get field and value completions, see recent SQL filters that start with your text, apply a SQL filter, or run a full-text search.
>
> For point-and-click filtering or a SQL editor, select  **Add a structured filter** from the dropdown:
>
> * **Basic**: Point-and-click filtering for common fields. The value picker lists the most common values for the selected field and includes a search box. To filter on a value that isn't in the list, type it into the search box and select the **Use “your value”** option that appears at the bottom of the list.
> * **SQL**: Write precise [SQL queries](https://docs.braintrust.dev/reference/sql.md) with operators, functions, and full-text search. The filter accepts a `WHERE` expression, not a full `SELECT` statement. Use the  **Generate** button to create queries from natural-language descriptions. See [How filtering works](https://docs.braintrust.dev/reference/sql/filtering.md) for matching behavior and [SQL best practices](https://docs.braintrust.dev/reference/sql/best-practices.md) for performance tips.
>
> If the search field is empty, **Add a structured filter** opens **Basic**. If you have entered text, it opens **SQL** with that text pre-filled. You can switch between the tabs in the editor.
>
> When Loop is enabled, type a description in the search field and select  **Generate SQL with Loop** to generate a filter from your description.
>
> Applied filters appear as chips in the filter bar. To edit a text search chip, click it to open an inline editor and select **Update**. To edit a structured filter chip, click it to reopen the filter editor:
>
> * A **Basic** filter that uses **equals** or **does not equal** on the span name or on a field in input, output, expected, or metadata reopens in **Basic** with its field, operator, and values filled in. Select **Update filter** to apply your changes. If you switch to **SQL** and edit the query, you can't return to **Basic**.
> * Other filters, including all **SQL** filters, reopen in **SQL** with **Basic** unavailable. Select **Update** to apply your changes.
>
> When the row type is **Traces** (the default), Basic filter conditions [match across spans](#match-traces-across-spans) automatically.
>
> > [!NOTE]
> >
> > When filtering by **Assigned to** in the **Basic** tab, the dropdown shows individual members and permission groups. Selecting a permission group matches any row assigned to at least one member of that group. If you select a permission group with more than 50 members, an error banner appears and the filter is not applied.

> [tab] CLI
>
> Use [`bt sql`](https://docs.braintrust.dev/reference/cli/sql) to run filtered SQL queries against your logs from the terminal. Pass a query inline or pipe one in from a file.
>
> > [!TIP]
> >
> > Most SQL data-source functions also accept an object name in place of its ID. See [Querying by name](https://docs.braintrust.dev/reference/sql/query-structure.md#querying-by-name).
>
> ```bash theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> bt sql "SELECT * FROM project_logs('my-project') WHERE scores.Factuality > 0.8 LIMIT 100"
> ```
>
> ```bash theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> cat analysis.sql | bt sql
> ```
>
> For automated workflows, pass `--non-interactive` to skip the interactive interface and `--json` to get machine-readable output.
>
> ```bash theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> bt sql --non-interactive "SELECT count(*) FROM project_logs('my-project') WHERE tags MATCH 'error'" --json
> ```

> [tab] API
>
> Query logs programmatically using the Braintrust API for automation, integrations, and custom tooling.
>
> **Basic filtering**: Use the [project logs endpoint](https://docs.braintrust.dev/api-reference/logs/fetch-project-logs-get-form.md) for simple filters and programmatic access:
>
> ```bash theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> curl -X GET "https://api.braintrust.dev/v1/project/<PROJECT_ID>/logs" \
>   -H "Authorization: Bearer <YOUR_API_KEY>" \
>   -H "Content-Type: application/json"
> ```
>
> **SQL queries**: For complex queries, POST a SQL query to the [`/btql` endpoint](https://docs.braintrust.dev/api-reference/query):
>
> ```bash theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> curl -X POST https://api.braintrust.dev/btql \
>   -H "Authorization: Bearer <YOUR_API_KEY>" \
>   -H "Content-Type: application/json" \
>   -d '{
>     "query": "SELECT * FROM project_logs('"'<PROJECT_ID>'"') WHERE scores.Factuality > 0.8 LIMIT 100"
>   }'
> ```
>
> The API accepts these parameters:
>
> * `query` (required): Your SQL query string.
> * `fmt`: Response format (`json` or `parquet`, defaults to `json`).
> * `tz_offset`: Timezone offset in minutes for correct day boundaries.
> * `audit_log`: Include audit log data.

## How filters match your data

Braintrust evaluates every filter against one span at a time, and the row type then decides which rows come back. That two-step behavior explains most unexpected results:

* On the **Traces** row type, a single matching span brings back its whole trace, including spans that don't match the filter.
* Fields aren't inherited from a trace's root span, so a condition on root-span metadata never matches a child LLM span.
* Conditions match the same span or different spans depending on how you combine them with `ANY_SPAN()`.

See [How filtering works](https://docs.braintrust.dev/reference/sql/filtering.md) for the full model, including `ANY_SPAN()` for matching conditions across spans and common pitfalls that return the wrong rows.

## Identify spans and traces

Every span carries three ID fields, each with a distinct role:

| Field | Identifies | Use it to |
| - | - | - |
| `id` | An individual span (one row in logs or an experiment). | Filter to or link to a single span. This is the span's identifier. |
| `root_span_id` | The entire trace the span belongs to. | Filter to or link to a full trace. |
| `span_id` | An internal field used with `span_parents` to construct the span tree. | Nothing. Treat it as an implementation detail. |

To fetch a known span or trace, filter on `id` or `root_span_id`. Both map directly to the index, so they are the fastest predicates. Avoid filtering on `span_id`. See [Fetch known traces or spans by ID](https://docs.braintrust.dev/reference/sql/best-practices.md#fetch-known-traces-or-spans-by-id) for details.

When you link to a trace in the Braintrust UI, the `r=` URL parameter is the `root_span_id`, not the `id`. Using the `root_span_id` is the efficient way to open a trace. See [Link to a trace or span](https://docs.braintrust.dev/observe/examine-traces.md#link-to-a-trace-or-span).

> [!NOTE]
>
> Some ingestion paths, such as OpenTelemetry collectors, set `span_id` to the same value as `id`, which is why the two are often conflated. Regardless, `id` is the field that identifies a span.

## Common filters

Ready-to-use filter expressions for the most common log queries. Paste them directly into the **SQL** filter tab in the UI, or use them as the WHERE clause in [`bt sql`](https://docs.braintrust.dev/reference/cli/sql) or [`/btql` API queries](https://docs.braintrust.dev/api-reference/query).

> [accordion] Filter by score
>
> ```sql Above threshold theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> scores.Factuality > 0.8
> ```
>
> ```sql Including missing theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> scores.Factuality IS NULL OR scores.Factuality < 0.5
> ```

> [accordion] Filter by tag
>
> Use `IN` for exact tag membership. `MATCH` is a fuzzy approximation, and `=` doesn't match the `tags` array at all.
>
> ```sql Has tag theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> tags IN ('error')
> ```
>
> ```sql Excludes tag theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> tags NOT IN ('internal')
> ```

> [accordion] Filter errored runs
>
> ```sql theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> error IS NOT NULL
> ```

> [accordion] Filter failed LLM calls
>
> Match the LLM span type and the error on the **same span** by combining both conditions inside one `ANY_SPAN()` call:
>
> ```sql theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> ANY_SPAN(span_attributes.type = 'llm' AND error IS NOT NULL)
> ```
>
> Splitting the conditions into two separate `ANY_SPAN()` clauses matches traces where any span errored and any span is an LLM span, even when they aren't the same span. See [Filter logs for failed LLM calls](https://docs.braintrust.dev/kb/filter-logs-for-failed-llm-calls) for span-shaped and summary-metric variants.

> [accordion] Filter by metadata
>
> ```sql Single field theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> metadata.user_id = "user-123"
> ```
>
> ```sql Combined theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> metadata.environment = "production" AND metadata.model = "gpt-5-mini"
> ```

> [accordion] Search text fields
>
> Use `search()` to match across all text fields, or `MATCH` to target a single field. See [Full-text search](https://docs.braintrust.dev/reference/sql/query-structure.md#full-text-search) for details.
>
> On the **Logs** page, full-text search filters hide the logs chart. See [Explore the logs chart](https://docs.braintrust.dev/observe/view-logs.md#explore-the-logs-chart) for an alternative filter that keeps the chart.
>
> ```sql All fields theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> search('timeout')
> ```
>
> ```sql Specific field theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> output MATCH 'timeout'
> ```

> [accordion] Filter by time
>
> Use a relative interval to stay within your plan's [data retention window](https://docs.braintrust.dev/plans-and-limits.md).
>
> ```sql Relative theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> created > now() - interval 1 day
> ```
>
> ```sql Range theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> created >= '2024-01-01' AND created < '2024-02-01'
> ```

> [accordion] Match traces across spans
>
> When filtering traces, you often want to match against any span in the trace, not just the root. Wrap conditions in `ANY_SPAN()`. For example, to find traces with both an LLM call and an error somewhere in the tree:
>
> ```sql theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
> ANY_SPAN(span_attributes.type = 'llm') AND ANY_SPAN(error IS NOT NULL)
> ```
>
> See [Single span filters](https://docs.braintrust.dev/reference/sql/query-structure.md#single-span-filters) for nesting rules and the `is_root` restriction.
>
> > [!NOTE]
> >
> > Braintrust applies `ANY_SPAN()` automatically in:
> >
> > * The **Basic** filter tab when the [row type](https://docs.braintrust.dev/observe/view-logs.md#browse-logs) is set to **Traces**.
> > * [Topics automation filters](https://docs.braintrust.dev/observe/topics/manage.md#adjust-automation).
> > * [Trace-scoped online scoring rule filters](https://docs.braintrust.dev/evaluate/score-online.md#configuration-parameters).

## Save and share filters

Save a frequently-used combination of filters, display settings, and columns as a [custom table view](https://docs.braintrust.dev/observe/view-logs.md#create-custom-table-views). Saved views appear in the  menu at the top of the table and are visible to all project members.

If you've built a useful view in one project, you can [duplicate it to another project](https://docs.braintrust.dev/observe/view-logs.md#duplicate-table-views-across-projects) via the API.

## Ask questions with Loop

Select  **Loop** on the  **Logs** page to ask natural language questions about your traces. Loop understands your data structure and can answer questions, identify patterns, and surface specific traces without writing any queries.

Example questions:

* "Show me traces where the user was confused"
* "Find requests that took longer than usual"
* "What are the most common error patterns?"

Loop is also available when viewing an individual trace. Ask questions like "Summarize this trace" or "Why did this request fail?" See [Analyze logs](https://docs.braintrust.dev/loop/capabilities.md#explore-your-data) and [Analyze individual traces](https://docs.braintrust.dev/loop/capabilities.md#analyze-traces) for more details.

> [accordion] Find similar traces
>
> Select one or more rows and use  **Find similar traces**. Loop identifies common traits across the selected traces and returns similar ones.

> [accordion] Save a query result as a dashboard chart
>
> You can save a chart from a Loop query result without leaving the Logs page:
>
> 1. Ask Loop to query the metric you want to chart.
> 2. Expand the **Queried** tool call and select the **Chart** tab to preview the result.
> 3. Click the  icon with the **Add to monitor** tooltip.
> 4. Enter a **Title**, choose a dashboard, and click **Add chart**. The chart appears on the selected dashboard.
>
> The chart action is available when the query result can be turned into a chart. See [Build charts](https://docs.braintrust.dev/observe/dashboards/build-charts.md) to refine and organize your charts.

## Speed up log filtering

If you frequently filter on the same custom fields, you can index them to reduce query latency. Braintrust offers a full-text index for broad search, subfield indexes for specific fields you filter on most, and a metric columnstore for trace-level metrics.

1. Go to ** Settings** > [** Query optimization**](https://www.braintrust.dev/app/~/configuration/query-performance).
2. Turn on **Enable log search optimization** to build a full-text index that speeds up text-based filter queries.
3. Turn on **Enable shingled search optimization** to also index multi-word phrases, which speeds up phrase and multi-word `search()` queries.
4. Turn on **Enable metric columnstore** to write trace-level metrics in a columnar format, which speeds up the trace queries behind the ** Logs** page on high-volume projects.
5. Under **Subfield indexing**, click **+ Add subfield index** for each field you filter on frequently.

   Braintrust auto-discovers candidate fields from your data (e.g., `metadata.session_id`). If a field doesn't appear, you can type it in directly. Subfield paths must start with `input`, `output`, `expected`, `metadata`, or `span_attributes`.
6. Click **Save and index**.
7. Enter how many days back to backfill (default: 3) and click **Save and backfill**.

The **Index status** section shows backfill progress as indexing runs in the background.

> [!TIP]
>
> Use [`search()`](https://docs.braintrust.dev/reference/sql/query-structure#full-text-search) in SQL filters to query all text fields at once. It gets automatic bloom filter acceleration when log search optimization is on.

## Next steps

* [Score online](https://docs.braintrust.dev/evaluate/score-online.md) to evaluate filtered traces
* [Create dashboards](https://docs.braintrust.dev/observe/dashboards.md) with filtered metrics
* Read the [SQL reference](https://docs.braintrust.dev/reference/sql.md) for complete query syntax


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.