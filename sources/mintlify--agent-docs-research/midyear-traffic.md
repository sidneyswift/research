# Capture: midyear-traffic

Canonical URL: https://www.mintlify.com/blog/state-of-docs-traffic
Resolved URL: https://www.mintlify.com/blog/state-of-docs-traffic
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

# The state of docs traffic: a 2026 midyear report

> [llms.txt](https://www.mintlify.com/llms.txt)

Agents now account for 66% of measured web-traffic across docs powered by Mintlify, with July logging over 213 million agent web requests and 105 million human page loads as the month comes to a close.

- URL: https://www.mintlify.com/blog/state-of-docs-traffic
- Published: July 29, 2026
- Category: AI Trends
- Authors: kyan-yang

Agents now account for 66% of measured web-traffic across [docs powered by Mintlify](https://www.mintlify.com/data), with July logging over 213 million agent web requests and 105 million human page loads as the month comes to a close. This measures an increase of 52 percentage points compared to the start of 2026, where agent activity comprised of only 15.2% of docs traffic.

If the current trajectory continues, the agent share of web-traffic will reach nearly 90% by year-end.

To understand what this implies for the future of knowledge interaction, we examine site analytics to understand the behaviors, trends, and preferences of agents.

![Monthly agent requests and human visits from January through July 2026, ending at 213 million agent requests and 105 million human visits](/images/blog/state-of-docs-traffic/agents-vs-human-traffic.webp)

## Machine-readable routes are more important than ever

Human visitors read the rendered site, logging a request during each client-side page load. On the other hand, due to the lack of standardization, agent activity can come in a wide variety of forms. Agents can request direct [Markdown](https://www.mintlify.com/blog/context-for-agents) files (the current most efficient method), negotiate a text response, navigate through [`llms.txt`](https://www.mintlify.com/docs/ai/llmstxt), or use the barebones plain page text.

In July so far, 83.7% of agent web-request events arrived through an explicit machine route rather than an ordinary page requested by a known agent client, which accounted for the remaining 16.3%.

Within explicit machine routes, direct `.md` requests grew from 25.1% of volume in February to 54.4% in July so far. Requests negotiating `text/markdown` fell from 25.2% to 8.3%, while plain text visits moved from 47.2% to 34.5%.

![The share of explicit machine-route requests by response type from February through July 2026, with direct Markdown requests growing to 54.4%](/images/blog/state-of-docs-traffic/direct-information.webp)

## Where MCPs come into play

MCP clients connect to hosted documentation servers, where they call search, filesystem, or feedback tools. Because those calls travel through a different channel from direct agent web requests, we track them as a separate event stream outside our web-traffic totals. Most MCP activity comes from either site visitors querying the docs assistant or developer teams retrieving information from their internal Mintlify powered knowledge base.

Across our hosted docs sites in July so far, docs assistants have returned 1.18 million responses, while our hosted MCP servers have handled 1.42 million tool calls across the three exposed types. Additionally, calls per active server were 46% higher than in January.

Search accounted for 56.57% of those calls, used when agents have a question but do not yet know the relevant page path. When the path is known, agents use filesystem retrieval to read the page directly, accounting for another 43.30% of total MCP calls. Feedback submissions, sent by the agent when it runs into errors, made up the remaining 0.13%.

One unfortunate limitation of MCP clients, though, is that they do not expose a persistent conversation identifier to remote docs servers. This means calls arrive as stateless requests, preventing us from reliably grouping calls into specific tasks.

## Visitor attribution

| Measure            | What we count                                                                    | What remains unknown                                             |
| ------------------ | -------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Human visits       | Client-side docs page loads                                                      | Unique people and activity that never executes the browser event |
| Agent web requests | Explicit machine routes and requests matching known AI IP or user-agent patterns | Tasks, outcomes, and unidentified or intermediated clients       |
| MCP activity       | Search and filesystem tool calls, plus active servers                            | Conversations, completed tasks, and cross-channel journeys       |

Visitor attribution depends on the signature that reaches the publisher. Known client signatures can identify GPTBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Google-Extended, and other declared sources, while services presenting a browser user agent can fall into human traffic. Though even a known signature cannot prove whether a request originated in a product’s built-in search, an intermediary such as Parallel or Exa, or another browsing agent.

Route choice can also change the measurement because a Markdown request identifies itself as machine traffic, while an unrecognized client fetching HTML may not. A client switching routes can therefore raise measured agent share even if its task volume stays flat.

Client signatures also reveal quite a few interesting statistics, such as Claude-User traffic dropping by almost 60% on weekends, giving us an insight to how much of the industry works on the weekend.

## Wasted work in agents

In a [2,400-run benchmark](https://www.mintlify.com/blog/llms-txt-agent-benchmark) across 20 docs sites, we asked coding agents (Claude Code, Codex) the same knowledge based questions under four docs conditions:

1. HTML
2. Plain Markdown
3. Markdown linked to `llms.txt`
4. Markdown with the full `llms.txt` inlined.

Across plain retrieval conditions (HTML and plain Markdown), agents consistently guessed dead URLs, read irrelevant pages, and went back-and-forth through search before recovering the correct source.

However, displaying an `llms.txt` in the docs reduced error rate by almost **90%**, enabling the agent to answer with fewer fetches and tokens, keeping its context window cleaner as well as saving the developer both time and money.

![Average 404 errors per retrieval request across HTML, Markdown, and Markdown with llms.txt linked or inlined, falling from 2.23 to 1.42 to 0.11](/images/blog/state-of-docs-traffic/url-errors-benchmark.webp)

An important corollary to note, though, is that since every wrong URL and irrelevant page logs another request, improving agent accuracy would actually _lower_ total request volume from agents, even without a corresponding decline in agent use. Therefore, the most useful measure which a company can track is not total request volume, but rather the frequency of wasted work when visiting agents attempt to find relevant docs.

## One system to serve and measure every path

With agents now making up 66% of measured docs traffic, publishers need one unified publishing system that keeps the human-readable site and every source of machine-readable context in sync.

At Mintlify, every docs update, whether manual or automated, reaches the rendered site, direct Markdown routes, `llms.txt`, and the hosted MCP server all at once. [Mintlify Analytics](https://www.mintlify.com/docs/optimize/analytics) then tracks interactions across these surfaces, feeding the resulting events into your internal systems alongside support and product data to reveal what customers need and where the docs fall short.

## Where to start

- See your own human and agent split in [traffic analytics](https://www.mintlify.com/docs/analytics/traffic).
- Give agents a map with [llms.txt](https://www.mintlify.com/docs/ai/llmstxt) and a [hosted MCP server](https://www.mintlify.com/docs/ai/model-context-protocol).

To see how humans and agents are interacting with your docs, and to prepare your docs for the agentic future, [schedule a chat with us today](https://www.mintlify.com/contact/sales).
