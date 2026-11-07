# Capture: early-index-traffic

Canonical URL: https://www.mintlify.com/blog/how-often-do-llms-visit-llms-txt
Resolved URL: https://www.mintlify.com/blog/how-often-do-llms-visit-llms-txt
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

# How often do LLMs visit llms.txt?

> [llms.txt](https://www.mintlify.com/llms.txt)

Last month, we explored signals for the emerging standard of llms.txt, which is a Markdown file that makes websites easier for LLMs to index.

- URL: https://www.mintlify.com/blog/how-often-do-llms-visit-llms-txt
- Published: June 27, 2025
- Category: AI Trends
- Authors: tiffany-chen

Last month, we explored [signals for the emerging standard of llms.txt](https://www.mintlify.com/blog/the-value-of-llms-txt-hype-or-real), which is a Markdown file that makes websites easier for LLMs to index.

Some indicators of its rising importance:

- **Google** including an [llms.txt](https://github.com/google/A2A/blob/6351e4c45abaf2f0a6817d66540660af277e7772/llms.txt#L4) file in their new Agents to Agents (A2A) protocol
- **Windsurf** reporting that llms.txt helps reduce token usage by pointing agents directly to relevant endpoints, saving both time and cost
- **Anthropic**, creators of Claude, asking Mintlify to implement both llms.txt and llms-full.txt for their docs, a clear signal of where the industry is headed

That last point raised an important question: between the two formats, which one are LLMs actually using more?

The qualitative evidence is strong, but we wanted to understand how the data matches the hype.

To answer that, we partnered with [**Profound**](https://www.tryprofound.com?utm_source=blog&utm_medium=referral&utm_campaign=mintlify_llmstxt_blog), a platform that tracks how LLMs discover and interact with websites. Our goal wasn't just to validate adoption—we wanted to quantify the actual behavior of AI agents in the wild.

## A quick refresher on llms.txt vs. llms-full.txt

Before we get into the data, here's an overview of [what is llms.txt and llms-full.txt](https://www.mintlify.com/blog/what-is-llms-txt).

llms.txt is a Markdown file served at /llms.txt on your website or documentation. It acts similar to a sitemap, but structured in a way that's optimized for LLMs. With Markdown, LLMs can bypass the clutter of HTML, Javascript, and advertisements.

llms-full.txt is a standard Mintlify pioneered with Anthropic to go beyond the high-level links in llms.txt. Instead of listing just key pages, llms-full.txt includes the full content of your documentation in a single, structured file—giving LLMs a much richer indexable surface to work with.

## How we measured the data

Profound collects data at the infrastructure level via CDN logs—before caching and bot filtering—which gives a more complete picture of how LLMs crawl content. Their crawler detection models distinguish AI agents from traditional search bots, and their system supports real-time analysis across billions of requests.

For this analysis, we looked at:

- **Sample**: 25 companies that have llms.txt on either their marketing or docs domain
- **Segment:** Roughly even distribution from startups to enterprises
- **Duration**: 7 days of traffic
- **Focus**: Comparing total visits to llms.txt vs. llms-full.txt

And as a bonus, we'll share a deeper look into Mintlify's own site traffic.

## Results: llms-full.txt is visited more frequently than llms.txt

Across the dataset, llms-full.txt was visited much more frequently than llms.txt.

- llms.txt:
  - Median: **14 visits**
  - Mean: **62 visits**

- llms-full.txt:
  - Median: **79 visits**
  - Mean: **248 visits**

ChatGPT accounted for the majority of llms-full.txt traffic, reinforcing that it's actively used by leading LLMs to gather structured knowledge.

And we saw the same pattern on Mintlify's own site:

- llms.txt: **436 visits**
- llms-full.txt: **967 visits**

## Why llms-full.txt is easier for LLMs to index

The heavier traffic to llms-full.txt that LLMs prefer embedding the full content surface up front rather than relying on retrieval-augmented generation (RAG) via llms.txt.

While RAG can be efficient in theory—fetching only what's needed at query time—it introduces practical issues: retrieval latency, inconsistent formatting across linked pages, and the risk of missing or outdated content.

By contrast, llms-full.txt offers one complete, structured file that can be processed in a single pass. In Mintlify's case, llms-full.txt contains roughly 25 times more content than llms.txt: about 58,000 words versus 1,600.

This format plays well with models like ChatGPT, which are optimized for large context windows. GPT-4-turbo, for example, supports up to 128K tokens and performs best when given a dense, high-signal input. Rather than piecing together multiple documents, it can embed everything upfront—reducing fragmentation and increasing retrieval accuracy later.

While llms-full.txt may seem more expensive to embed initially, that cost happens only once. After indexing, LLMs can serve faster, more consistent answers from cached embeddings, without re-fetching content or resolving links on the fly.

## What this means for you

This data suggests that llms-full.txt is doing what it was designed to do: give LLMs a complete, structured snapshot of your product surface.

While llms.txt is a useful starting point, llms-full.txt is quickly proving to be the real workhorse for discoverability.

If your documentation isn't LLM-ready yet, now's the time to get ahead. Mintlify auto-generates llms.txt and llms-full.txt for all documentation, so your docs are AI-ready out-of-the-box.

[Get in touch with our team to learn more.](https://www.mintlify.com/contact/sales)

‍
