# The Trace Lake

Author: Ankur Goyal (@ankrgyl)

Published: 2026-11-03T19:13:52.000Z

Modified: 2026-11-03T19:33:51.000Z

Retrieved: 2026-11-04

Canonical post: https://x.com/ankrgyl/status/2117696780741771638

Article: https://x.com/i/article/2117682615494823936

Capture: ordered rich-text blocks from public FxTwitter JSON; embedded MARKDOWN SQL preserved, inline links restored. Raw JSON is authoritative for formatting. Cover is title art, inspected separately.

---

Tracing was originally conceived as a mechanism to understand the bottlenecks in complex, multi-service software. Engineering teams needed to keep the services supporting their applications working fast, cost-effectively, and reliably as usage grew. Tracing and APM products were built for a world of deterministic applications and data about those applications' performance.

But agents are different, and agent traces are different. An agent trace serves as the authoritative record for how an agent behaves as it undertakes long-running, complex, and probabilistic tasks. Each decision, output, and interaction with the outside world is recorded and indexed, so you can inspect an individual trace or understand patterns across many.

In addition to real time data about your agent, you also need to learn from your agent's history. You need to keep execution history searchable and queryable, so teams can investigate behavior across many runs and use what they find in evals and investigations.

Many teams use data lakes and data warehouses to support these workflows. But data lakes weren't built specifically for agent traces. Agent observability demands something new: a Trace Lake.

### How to build a Trace Lake

Traditional tracing products sample heavily, focus on opening individual traces, and discard traces fast. Once a trace is gone, you can't return to it when a new question comes up. Looking at traces in real time is still important, but improving agents requires learning from the sum of their traces.

For example, what behaviors consistently waste tokens as your agent goes about a long-horizon task? What activities are frustrating your users? If you find an example of a specific behavior, like an agent changing languages mid-sentence, can you find 20 more, and debug the issues based on what you see? When a user reports a bad experience, can you recover the trace and the application state needed to reproduce it? Can you turn that example into an eval without manually collecting context from several systems?

To answer these kinds of questions, a Trace Lake needs to support three things.

1. Fast ingest (<10s) and fast SQL (hundreds of ms)

Engineers now use agents to both build and debug their software, so agents are also sending their own queries. To support agent self-investigation, you need to run many fast queries, and newly ingested traces need to become queryable quickly. To debug agent failures, you need true [full-text search](https://braintrust.dev/docs/observe/filter) to find the exact traces that have the relevant prompts, responses, or tool results. You also need [SQL support](https://braintrust.dev/docs/observe/filter) to filter and compare executions using the fields in the data that agents produce and interact with.

2. Cheap and scalable storage that can stay in your cloud

Production systems can generate on the order of [100,000 spans per second](https://braintrust.dev/blog/brainstore-architecture). They contain entire prompts, responses, intermediate reasoning steps, tool calls, and whole conversation histories.

A typical span can be ~50 KB and a typical trace ~10 MB. At p90, that can jump to spans in the tens of MB and traces that reach tens of GB. At this scale, traces are two to three orders of magnitude larger than what many databases were designed for.

Keeping execution history available for future investigations needs to be affordable as that history grows. Object storage lets you retain that history without requiring every query server to hold a full copy on local disk. Some teams need that data to stay in their own cloud because the traces can contain proprietary or sensitive information.

3. Finding patterns and turning them into evals

A Trace Lake should make it easy to run evals over incoming traces to detect failures and collect useful examples to keep investigating. Once a pattern is understood, an agent should define a focused, inexpensive eval that measures the recurring issues across many executions. Teams should be able to do this ad hoc when a question arises, and also keep checking for repeatable behavior as their agents change.

Turning a production example into a useful test case also requires the context to reproduce it. Depending on the application, that could include the state before the agent acted, or versions of the resources it used. The examples you find in production become test cases you can run against future changes. The path from behavior worth investigating to reproducible evidence to lasting eval should be trivial.

### What's missing

Looking at these use cases and the infrastructure you'd need to support them, you can see the outline of a data warehouse. However, there are a few key differences.

First, traces are a relatively new, demanding mix of ingest and query workloads. Traditional warehouses are [too slow](https://braintrust.dev/blog/nitro) at both ingest and query performance for agent traces, which led us to build our custom database, Brainstore.

These queries find traces from the last seven days with a GPT-6 Luna call, tool errors, over 50,000 tokens, and an average Factuality score below 0.5. Braintrust uses trace summaries and ANY_SPAN() filters instead of explicit joins and aggregations.

Braintrust

```sql
SELECT root_span_id, input, output,
       metrics.total_tokens, metrics.llm_calls,
       metrics.tool_calls, metrics.tool_errors,
       scores.Factuality
FROM project_logs('<PROJECT_ID>', shape => 'summary')
WHERE ANY_SPAN(is_root AND created >= now() - INTERVAL 7 DAY)
  AND ANY_SPAN(span_attributes.type = 'llm' AND metadata.model = 'gpt-6-luna')
HAVING metrics.total_tokens > 50000
   AND metrics.tool_errors > 0
   AND scores.Factuality < 0.5
LIMIT 100

```

Traditional data warehouse

```sql
WITH recent_roots AS (
  SELECT project_id, root_span_id, input, output
  FROM spans
  WHERE project_id = '<PROJECT_ID>'
    AND is_root = TRUE
    AND created >= CURRENT_TIMESTAMP - INTERVAL '7 days'
),
trace_summaries AS (
  SELECT
    s.project_id,
    s.root_span_id,
    SUM(
      CASE WHEN s.span_purpose IS DISTINCT FROM 'scorer'
        THEN COALESCE(s.prompt_tokens, 0)
           + COALESCE(s.completion_tokens, 0)
        ELSE 0
      END
    ) AS total_tokens,
    COUNT(*) FILTER (WHERE s.span_type = 'llm') AS llm_calls,
    COUNT(*) FILTER (WHERE s.span_type = 'tool') AS tool_calls,
    COUNT(*) FILTER (
      WHERE s.span_type = 'tool' AND s.error IS NOT NULL
    ) AS tool_errors,
    AVG(s.factuality_score) AS factuality,
    BOOL_OR(
      s.span_type = 'llm' AND s.model = 'gpt-6-luna'
    ) AS used_gpt6_luna
  FROM spans s
  JOIN recent_roots r
    ON s.project_id = r.project_id
   AND s.root_span_id = r.root_span_id
  GROUP BY s.project_id, s.root_span_id
)
SELECT r.root_span_id, r.input, r.output,
       t.total_tokens, t.llm_calls,
       t.tool_calls, t.tool_errors, t.factuality
FROM recent_roots r
JOIN trace_summaries t
  ON r.project_id = t.project_id
 AND r.root_span_id = t.root_span_id
WHERE t.used_gpt6_luna
  AND t.total_tokens > 50000
  AND t.tool_errors > 0
  AND t.factuality < 0.5
LIMIT 100

```

Second, traces contain a mix of structured metadata, nested fields, and unstructured text, so writing SQL queries is overwhelmingly verbose. A Trace Lake should make it straightforward to query fields within spans and compare results across whole traces. It should also preserve familiar SQL semantics while optimizing the underlying schema and execution for agent workloads.

Third, a Trace Lake needs to support continuous analysis of the data you ingest. Without applying intelligence to your agent traces as they come in, you won't be able to continuously run the investigations that help you understand and improve your agents. A warehouse can provide storage and processing, but teams would still need to build and maintain agent-specific intelligent workflows.

### What the Trace Lake makes possible

The Trace Lake is a new concept, but it's what we've been building towards at Braintrust for the past few years. Brainstore's architecture was designed in response to the new problems that agents have created.

Customers are already using this foundation to investigate their agents. Notion's AI modeling team described [running searches in seconds that previously took hours](https://braintrust.dev/blog/brainstore#customer-testimonials).

Teams can use [Topics](https://braintrust.dev/docs/observe/topics) to classify traces, [Patterns](https://braintrust.dev/docs/observe/patterns) to investigate recurring issues, and [Loop automations](https://braintrust.dev/docs/loop/automations) to repeat investigations on a schedule. They can query the data inside spans without needing to flatten it into a fixed schema.

To support these investigations, Brainstore's asynchronous query execution engine, Nitro, separates waiting for storage from processing the data it returns. In a production A/B test covering more than one million queries, [full-text searches ran more than twice as fast with Nitro](https://blog-trace-lake.preview.braintrust.dev/blog/nitro) than with the previous iteration of Brainstore. Other queries were 15% faster.

A Trace Lake won't only support agent traces and "agent observability." The same foundation can bring together metrics, logs, and system traces as well.

We've taken steps to make that real, like supporting [application logs](https://braintrust.dev/blog/application-logs) alongside agent traces, now in public preview. Start by sending logs from one service, and tell us what context is still missing. Your feedback will help us get there.
