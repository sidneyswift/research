# Capture: agent-score-announcement

Canonical URL: https://www.mintlify.com/blog/agent-score
Resolved URL: https://www.mintlify.com/blog/agent-score
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

# Is your documentation agent-ready?

> [llms.txt](https://www.mintlify.com/llms.txt)

An AI agent is reading your documentation right now. How well is it doing? We built a free tool to check how agent-ready your content is based on the agent-friendly documentation spec.

- URL: https://www.mintlify.com/blog/agent-score
- Published: April 27, 2026
- Category: Announcements
- Authors: ethan-palm

Agents are reading your documentation. Whether it's Cursor pulling context for a developer, Claude answering a support question, or an autonomous agent evaluating your API, your [docs have a new audience](/blog/ai-traffic) that never tells you if it got what it needed from your site.

To be agent-ready, your documentation must be structured so agents can find it, understand it, and use it. That means clear entry points, well-formed content, consistent terminology, and the right signals in the right places.

[Agent score](https://mintlify.com/score) tests your documentation against 29 checks and tells you exactly how ready it is for agents.

> Coding agents are rapidly becoming the primary surface for developer experience. To tackle anything meaningfully complex, agents require detailed, trustworthy context. For APIs and SDKs, that means documentation. When docs are accurate, well-structured, and agent-accessible, devs can pull off nearly hands-free integrations, saving huge amounts of time and effort. It's early days, but in customer conversations we're already seeing this emerge as a competitive differentiator.

— Mo King, Lead DX Engineer at Together AI

## Try it

Enter your documentation site URL at [mintlify.com/score](https://mintlify.com/score). You'll get a score and an explanation of each category in seconds.

![Agent score dashboard showing checks and scores](/images/agent-score.png)

You'll see what your site does well and where you can improve.

Keep in mind, it's a snapshot. Your score reflects the current state of your documentation. It changes as your docs change.

A low score isn't a failure. Most documentation wasn't written with agents in mind, because agents weren't a primary audience until recently. Use your score to guide where you take your documentation rather than judge it's current state. Documentation maintenance will always be an ongoing process.

## What it means to be agent-ready

Agent score is built on the [Agent-Friendly Documentation Spec](https://agentdocsspec.com), an open standard that defines what good documentation looks like for agents. It runs checks across seven categories:

- **Content Discoverability** — Can agents find your docs?
- **Markdown Availability** — Can agents get clean Markdown?
- **Page Size** — Are pages a reasonable size or will agents truncate them?
- **Content Structure** — Is the content well-formed for agents?
- **URL Stability** — Are URLs going to help or hinder agents?
- **Observability** — Do resources stay accurate over time?
- **Authentication** — Can agents reach your docs?

The spec covers the foundations very well. We added checks on top based on how we observe agents using documentation:

- **Full content discoverability** — Can long-context agents find and retrieve a corpus without repeated crawling?
- **Agent skill discoverability** — Can agents find and use your agent skills?
- **MCP server discoverability** — Can agents find and call tools on your site programmatically?

These additions reflect what we're seeing matter most right now, and how we expect agent-mediated documentation use to evolve.

## This work should be open

We built an internal tool with proprietary scoring. It worked well, but building on top of a closed standard didn't make sense.

Agent-readiness isn't a problem anyone will solve alone. Standards like [llms.txt](https://www.mintlify.com/blog/what-is-llms-txt) only work when they're widely adopted. The signals agents rely on only matter when they're consistent. The ecosystem only improves when the whole documentation environment iterates together.

The Agent-Friendly Documentation Spec is an open standard, with a [companion open source library](https://github.com/agent-ecosystem/afdocs) that implements all the checks.

We're building with the community and want to encourage others to contribute to the standard and the tooling.

Agent score is built on the spec. The checks are transparent. We're highlighting additional patterns we believe will improve documentation for all of our users.

## Join the conversation

Writing documentation for agents is a new discipline. We're all learning, and everyone improves with collaboration. More voices will help the standards and best practices develop faster.

If you think we're missing something, we want to hear from you. If you disagree with how we've implemented a check, let us know. If you've found something in your own docs that correlates with good or bad agent behavior, that's exactly the kind of signal that can help everyone who maintains documentation.

Score your docs at [mintlify.com/score](https://www.mintlify.com/score).
