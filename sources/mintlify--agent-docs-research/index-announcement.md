# Capture: index-announcement

Canonical URL: https://www.mintlify.com/blog/mintlify-index
Resolved URL: https://www.mintlify.com/blog/mintlify-index
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

# Introducing Mintlify Index

> [llms.txt](https://www.mintlify.com/llms.txt)

Mintlify Index aggregates the docs of 9000 Mintlify-powered documentation sites into a natural language retrieval layer for coding agents.

- URL: https://www.mintlify.com/blog/mintlify-index
- Published: August 6, 2026
- Category: Announcements
- Authors: kyan-yang

<video
  width="100%"
  controls
  className="w-full rounded-3xl"
  poster="/images/featured/mintlify-index.webp"
>
  <source src="/videos/mintlify-index-launch-video-compressed.mp4" type="video/mp4" />
</video>

> **Update:** Mintlify Index has been discontinued. This post is kept for reference.

Mintlify Index aggregates the docs of 9000 Mintlify-powered documentation sites into a natural language retrieval layer for coding agents.

The architecture begins by filtering agent queries into two categories:

1. Queries that reference docs in the Mintlify-powered ecosystem, which then undergo an internally optimized retrieval process.
2. All other queries, which are routed to a standard external provider.

```text
Developer gives an agent an implementation task
      ↓
Agent calls search or context
      ↓
Mintlify Index routes each query
      ├─ product in Mintlify's hosted corpus → all public Mintlify-powered docs
      └─ other query                         → web search
      ↓
Index returns ranked sources or token-budgeted context
      ↓
Agent can call contents to inspect a selected source
      ↓
Agent uses the evidence to answer or plan the change
```

Each search or context request routes the query to a retrieval source. Queries about products in Mintlify’s hosted corpus use eligible public documentation when those docs are likely to answer the request. Other queries route to a leading third party web search tool. If the selected source fails or returns no results, Index will also fall back to the other.

An agent can retrieve evidence in two ways. Context returns an assembled, token-budgeted bundle of ranked excerpts and source URLs. For more control, search returns ranked source metadata and optional matching text. The agent can then pass a Mintlify URL or document ID to contents to retrieve the selected page. With a follow-up query and length limit, contents can return the most relevant section. Index supplies the evidence, afterwhich the agent remains responsible for producing and validating the answer or implementation.

We then ran an experiment comparing Mintlify Index with Context7, a popular docs-retrieval service for coding agents. Across 150 implementation-planning tasks on 50 products hosted on Mintlify, a blinded pairwise judge preferred the plans produced with Mintlify Index in 96 tasks, nearly two-thirds.

Not only did the Mintlify Index group produce higher-quality results, but they also completed tasks 48% faster end-to-end, with 10% higher factual correctness, 10% better citation support, and 17% fewer critical errors.

![Mintlify Index generated plans 48% faster and won 96 of 150 blinded comparisons](/images/blog/mintlify-index/benchmark.webp)

In pursuit of our mission to optimize the interaction between agents and knowledge, this experiment showed us the potential benefits of a customized retrieval system only made possible by the ecosystem of Mintlify docs.

We’re launching a beta version of Mintlify Index today, free to use for everyone.
