# Capture: march-traffic

Canonical URL: https://www.mintlify.com/blog/state-of-ai
Resolved URL: https://www.mintlify.com/blog/state-of-ai
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

# The state of agent traffic in documentation (March 2026)

> [llms.txt](https://www.mintlify.com/llms.txt)

An analysis of 30 days of Mintlify documentation traffic, broken down by AI agents, browsers, and other sources.

- URL: https://www.mintlify.com/blog/state-of-ai
- Published: April 3, 2026
- Category: AI Trends
- Authors: han-wang

We recently looked into 30 days of traffic data across Mintlify-powered documentation sites. By analyzing user-agent headers from Cloudflare, the identifier that tells us whether a request came from Chrome, Cursor, Claude Code, or something else, we categorized every request to understand who (or what) is actually reading your docs.

The results: AI coding agents now account for 45.3% of all requests, which is nearly tied with traditional browser traffic at 45.8%. Machines are reading your docs almost as much as humans are and the shift is being driven by two tools in particular.

## The numbers

One important caveat before we get into the data: not every AI agent sends a identifiable user-agent header. Notably, OpenAI's Codex [doesn't include one](https://github.com/openai/codex/issues/12859), which means its traffic can't be distinguished from generic HTTP clients in this analysis. This means the actual share of AI agent traffic is likely higher than what we're reporting here.

Over the past 30 days, Mintlify-powered docs received roughly 790 million requests. Here's how that broke down:

### AI Agents: 357.6M requests (45.3%)

| Agent             | Requests | % of Total | % of AI Traffic |
| ----------------- | -------- | ---------- | --------------- |
| Claude Code       | 199.4M   | 25.2%      | 55.8%           |
| Cursor            | 142.3M   | 18.0%      | 39.8%           |
| OpenCode          | 7.7M     | 1.0%       | 2.1%            |
| Trae (ByteDance)  | 4.6M     | 0.6%       | 1.3%            |
| ChatGPT           | 1.8M     | 0.2%       | 0.5%            |
| Google NotebookLM | 1.4M     | 0.2%       | 0.4%            |
| Manus             | 0.5M     | 0.1%       | 0.2%            |

_This analysis is based on 30 days of Cloudflare traffic data across Mintlify-powered documentation sites. Traffic was categorized by user-agent headers._

### Browsers: 361.7M requests (45.8%)

Chrome, Edge, Firefox, Safari, and the rest made up the other major chunk—with Chrome on Mac and Windows leading the way, as you'd expect.

### Other: (8.9%)

Bots, crawlers, Node fetch, and miscellaneous HTTP clients.

## Claude Code is the standout

Here's the number that really jumped out at us: Claude Code, on its own, generated 199.4 million requests. That's more than Chrome on Windows (119.4M). This means, a single AI coding agent is now pulling more documentation than one of the most popular browser-OS combos in the world.

Together, Claude Code and Cursor make up 95.6% of all identified AI agent traffic. The rest of the field, OpenCode, Trae, ChatGPT, NotebookLM, Manus, is showing up, but these two are far and away the heavyweights right now.

## What this tells us

We think there are a few interesting takeaways here, especially if you're building developer tools or maintaining documentation.

**Your docs have a new audience.** If you're thinking about documentation as something humans read in a browser, you're only reaching about half of your actual traffic. The other half is AI agents pulling your pages to help developers write code, debug issues, and integrate APIs.

**The ecosystem is broadening.** Beyond the big two, we're seeing traffic from ByteDance's Trae, Google's NotebookLM, and Manus. As more coding agents launch, this distribution will keep widening.

**Context retrieval is the new page view.** When Claude Code fetches your API reference, it's not browsing the way a human would. It's pulling context to generate or fix code in real time. That means the quality, structure, and machine-readability of your docs directly shapes how well these agents can help developers work with your product.

## What this means for documentation

We've been thinking about this shift at Mintlify for a while, and seeing the data play out this clearly is pretty exciting. Documentation is becoming infrastructure that serves two audiences at once.

For human readers, docs still need to be clear, navigable, and well-organized. For AI agents, they need to be structured, comprehensive, and easy to parse programmatically. The good news? These goals actually complement each other. Well-structured docs that work great for machines tend to work great for humans too.

That said, there are things that matter more now than they used to: consistent formatting in API references, complete and accurate code examples, explicit parameter descriptions, and thorough error documentation. These are the signals AI agents lean on when generating code for your users.

Learn more about building for the [agent experience on Mintlify](https://www.mintlify.com/blog/docs-as-ai-interface).
