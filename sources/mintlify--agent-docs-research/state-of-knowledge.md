# Capture: state-of-knowledge

Canonical URL: https://www.mintlify.com/state-of-knowledge/2026
Resolved URL: https://www.mintlify.com/state-of-knowledge/2026
Retrieved: 2026-11-05
Representation: server-provided textual representation
Content-Type: text/markdown; charset=utf-8

---

# The 2026 State of Knowledge Report

> [llms.txt](https://www.mintlify.com/llms.txt)

Agents are taking over as knowledge consumers, but few organizations are ready. Read the full 2026 State of Knowledge Report: platform data, a controlled benchmark, and a survey of 329 professionals.

URL: https://www.mintlify.com/state-of-knowledge/2026

Agents are taking over as knowledge consumers, but few organizations are ready

[Download PDF](/new/knowledge-report/state-of-knowledge-report-2026.pdf)

## Your number-one knowledge consumer is no longer human.

2026 marks the first year on record that AI agent readership of Mintlify-powered sites crossed the
majority line.

August alone saw 257 million agent web requests and 131 million human page loads. This means agents
now account for over half of total traffic. And the numbers keep compounding.

There are still people behind every one of these requests, they've just stopped doing the reading
themselves. Agents skip your images, your design, and your catchy headline. They want structure, yet
even the most forward-thinking companies have made only one knowledge surface ready: docs. And it's
not as ready as many think.

## Agent vs. Human traffic in August 2026

- Agent requests: 257,000,000
- Human page loads: 131,000,000
- Agent share: 66%

Chart: agent share of traffic per month, February to August 2026, rising from 20.8% to 66%.

## Docs vs. Knowledge

- **Documentation** is what you publish for people building with your product: guides, tutorials,
  API references, etc.
- **Knowledge** is all of that plus everything else that explains your product, your company, and
  how it all works: the help center, the community forum, the changelog, support tickets, sales
  enablement, premium customer portals behind auth, and more.

As agents begin moving from reading documentation to writing it, knowledge stops being a static
destination one team publishes and becomes living infrastructure the entire business runs on.

The data insights from this year's report show how quickly this transition is happening, what it costs
companies that aren't ready, and what it takes to go beyond docs and turn company-wide knowledge into
a system that keeps up.

## Part 1: Agents: The Readers You Didn't Write For

### Who they are

The instinct to write agent traffic off as "bot traffic" is strong, but the difference is
measurable. "Agents are a new kind of user," explains Chris Riley, Sr. Manager, Developer Relations
at HubSpot. "What's good for the humans is good for the agents, but you can't treat them the same
way, and treating non-human traffic as something to filter out means you're now filtering out your
customers."

Our survey results show this opinion is now the consensus among most companies, yet a surprising 24%
of respondents still don't see the distinction.

**Figure 1. Do you consider "bot traffic" to be the same as "agent traffic"?** (Base: all
329 respondents)

- 76% — No, they are different
- 24% — Yes, the same thing

While bots crawl indiscriminately, agents work with purpose. Most agents eschew HTML rendered pages.
In August, 83% of agent traffic arrived through machine-friendly routes: the .md version of a page,
/llms.txt files, or agent skills. Agents only request these resources when they know they exist.

And Model Context Protocol (MCP) tool calls exceeded 2 million the same month, roughly 3x growth
since February. MCP requires a client that speaks the protocol and calls tools by name—a crawler
can't produce a single one.

> **A Third Channel.** Web traffic isn't the full picture. Docs assistants operate as a separate
> channel that's tracked outside human and agent requests entirely. This channel returned nearly 1.3
> million responses in August alone.

This is real readership, and it's grown 9.3x since February this year, compared to just 1.2x for
human readership. While part of this can be attributed to more agents, the rest reflects the
differences between how agents and humans read.

### How they're different

A developer with a question used to open the documentation and read, generating a single visit.
That same developer now asks an agent, and the agent pulls the map, checks three pages, follows a
reference, and verifies a parameter before answering. The question and person are identical, but
the traffic is an order of magnitude higher.

Agents don't browse—what they come for is structure. Case in point: /llms.txt was fetched roughly
10.8 million times in August: a file humans rarely type into browsers. MCP calls split 53% search /
47% filesystem retrieval, depending on whether the agent already knows the page path. Either way, it
orients before it acts, which makes your information architecture the interface, not your prose.

> "Agents are the new audience for your knowledge, and that comes with real product requirements:
> for how it's shaped, what it contains, and how retrievable it is, so the agent can perform
> meaningful tasks end-to-end for users." — David Hou, Product Education Lead, Decagon

## Part 2: The Price of Persistence

### All roads lead to readership

The question is no longer if agents will try to read your docs, it's what happens when they do. And
the data shows they keep trying.

We noticed agents repeatedly requesting pages that didn't exist: 404ing, backing up, guessing a new
path, trying again. So we ran
[2,400 controlled tests](https://www.mintlify.com/blog/llms-txt-agent-benchmark) across 20
documentation sites, asking each the same set of questions, served four ways, with every request an
agent made observed and counted.

The agents rarely failed to answer. Accuracy remained between 94-99%, regardless of format. Reading
was never the problem—navigation was.

### Markdown vs. maps

The cause was structural, and counterintuitive. Serving pages as stripped-down markdown, the
standard move for making content machine-readable, removes the navigation along with the HTML,
leaving agents to infer URLs that aren't real.

**Figure 3. 404s by docs format** (Average # of 404 errors per task; Claude & Codex; 2,400 controlled
tests across 20 documentation sites)

- Markdown + llms.txt — 0.11
- Markdown — 1.42
- HTML — 2.23

Documentation served as HTML produced 2.23 failed requests per task. Clean
markdown brought that down to 1.42, and adding a single link to a map dropped it to 0.11. That's a
20x improvement over HTML, with markdown accounting for roughly a third of the gain and the map
delivering the rest. The pattern held across every model tested, on 19 or 20 of the 20 sites in
each case.

In our testing across five different models, we saw a 26% to 60% savings in tokens consumed when the
agents fetched pages as Markdown + llms.txt compared to HTML alone. This showcases that optimizing
your documentation for agents helps reduce cost for your customers in addition to speeding up the
path to better and more accurate results.

> **Test your own docs.** We made our benchmark tool open source. Point it at your own docs to find
> out how many failed requests agents are hitting trying to navigate your content.
> [See your results](https://github.com/mintlify/url-discovery-bench)

### Who pays?

The cost of failed navigation lands on your customers first. Their agents go in circles inside your
documentation, burning their tokens and time. But it doesn't stay there. Every wasted call and
information gap shapes your user experience and the impression your product makes.

"For coding agents, docs are an essential part of choosing which software to implement," says Ethan
Finkel, Founding Product Manager at [Gauge](https://www.withgauge.com/), a platform that runs coding
agents in real repositories to measure which tools they choose. "They may start with a list of tools
that they would commonly use, but selection and implementation success are highly coupled to the
quality of your documentation."

> "In prompts focused on choosing a tool with a hard limit on building, Gauge found that agents were
> more likely to read documentation than they were to read marketing materials." — Ethan Finkel,
> Founding Product Manager, Gauge

We asked Mintlify customers whether improving documentation discoverability and structure has
positively influenced their growth metrics. While many note increases in signups, website traffic,
demo requests, and free trial starts, almost half have yet to measure the impact. This indicates a
major opportunity to improve understanding of the relationship between content discoverability and
business outcomes.

**Figure 4. Since improving your documentation's discoverability and structure with Mintlify, have
you seen measurable changes in any of the following?** (216 Mintlify customers)

- 28% — Developer adoption
- 28% — Web traffic
- 12% — Demo requests
- 8% — Free trial starts
- 17% — No measurable change
- 47% — Haven't measured

Unfortunately, nothing on your dashboard shows an agent wasting twenty fetches to answer a question
that should have taken one. And what happens if what they eventually find isn't accurate?

## Part 3: Inside the New Docs Ecosystem

### Skepticism doesn't scale

Ask any technical writer or developer: keeping documentation current has always been the hardest
part of the job. "GitHub recently published
[an article](https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/)
that says the number of pull requests merged has increased by 3.6x since 2023," shares Sarah Deaton,
Anthropic's Technical Content Engineer for Claude Code. "Nobody is manually documenting 3.6x more.
Keeping up with this volume requires a new approach."

Just 24% of survey respondents say product changes are reflected in docs the same day. About 54%
cite a one-week lag, while 22% have to wait a month or longer, clearly illustrating the challenge
most teams face keeping up with the constant rate of new features.

**Figure 5. How long does a product change typically take to reach your documentation?** (All 329
respondents)

- 24% — Same day
- 54% — Within a week
- 13% — Within a month
- 5% — Longer than a month
- 4% — It often never does

Human skepticism has quietly absorbed decades of documentation debt. A developer who hits a stale
page and notices the version doesn't match will try something else, ask a colleague, or check the
changelog. But an agent that reaches your documentation doesn't then evaluate whether it's right. It
acts on it, writing the wrong parameter into a codebase without hesitating.

> "The same page that misled one developer now misleads an unknowable number of agents, which then
> propagate that misunderstanding to downstream users." — Sarah Deaton, Technical Content Engineer,
> Claude Code, Anthropic

Documentation accuracy has stopped being an editorial problem and become a systemic issue, requiring
a solution that scales just as fast.

### Reader to writer

Leading companies aren't just structuring their documentation for agents to read—they're now
leveraging them to update it with every code push, too. From February to August 2026, users directed
the Mintlify agent to update their documentation nearly 367,000 times.

In August alone, 95% of that volume was triggered by automation, either a webhook or a scheduled cron
job. More than 61% of resulting pull requests were merged. And now teams have started pointing the
same agents at resolved support tickets, turning the questions documentation failed to answer into
patches.

Our survey findings confirm this trend. A whopping 83% of respondents say AI agents now draft
documentation updates for their team. However, only 9% let those agents publish without a human in
the loop.

**Figure 6. Do AI agents draft documentation updates for your team?** (All 329 respondents)

- 74% — Yes. With human reviews before publishing
- 9% — Yes. With automated publishing
- 14% — No
- 3% — Not sure

> **How Anthropic closes the loop.** Sarah Deaton is the only person running documentation for
> Claude Code at Anthropic—a setup made possible by agents that surface knowledge gaps and draft the
> fixes for her review.
>
> Scheduled jobs pull new feedback every few hours through the Mintlify
> analytics API: broken code-sample reports, written comments, and more. An agent triages that
> stream alongside Slack mentions and GitHub issues, sorting each signal into user error, support
> issue, or a real documentation gap.
>
> From a dashboard she built with Claude Code, an autofix button
> turns the ones that matter into pull requests. And when feedback points to friction in the
> product, she can submit a PR to fix that instead, so the issue gets solved rather than documented
> around. [Read the full story](/customers/anthropic)

Documentation is transitioning from a static surface teams publish into a system that reads itself
and drafts its own improvements—with people deciding what's true and what ships. And it isn't going
to stop there.

## Part 4: From Documentation to Knowledge Infrastructure

### Spread across surfaces

Agents answer from whatever they can reach, and a lot of what a company knows isn't in the docs. It
lives in a help center article, support ticket, or community post. More than half of survey
respondents say their company knowledge lives across 5+ knowledge surfaces.

**Figure 7. Across approximately how many surfaces does your company knowledge live?** (All 329
respondents)

- 1 (docs only) — 6%
- 2–4 — 41%
- 5–7 — 36%
- 8–10 — 8%
- More than 10 — 9%

Respondents also reveal that few of these surfaces have been optimized for AI discovery and
consumption, let alone self-improvement. Less than a third classify "most" or "all" of their
knowledge as AI-ready.

**Figure 8. How many of these knowledge surfaces have been optimized for AI agents to access and
read?** (All 329 respondents)

- All of them — 7%
- Most of them — 24%
- Some of them — 39%
- Only our documentation — 16%
- None — 9%
- Not sure — 9%

### Why it often stops at docs

As Mintlify Co-founder and CEO, Han Wang, explains, "Making a surface agent-ready is a massive
engineering lift, from clean markdown and a queryable interface to a way to report what's missing
and a path back to the source. Once it's 'done,' the target has already moved."

llms.txt was proposed in September 2024. MCP followed that November, and by late 2025 had been
donated to a foundation with more than 10,000 public servers running on it. A company that made its
knowledge base agent-ready in early 2025 built against a landscape that has already changed several
times since.

Then there's ownership. Docs sit with DevRel or engineering, the help center with support, community
with marketing, and the changelog with product. That means four teams, four tools, and four versions
of "truth."

Some 35% of survey respondents say their companies use four or more tools to publish knowledge. This
group is also 5x more likely to rate their companies' AI-readiness as "behind" compared to those with
just one knowledge publishing platform.

**Figure 9. How many separate tools or platforms does your company use to publish and manage its
knowledge?** (All 329 respondents)

- 1 — 6%
- 2–3 — 54%
- 4–5 — 27%
- 6 or more — 8%
- Not sure — 5%

"Knowledge and the ability to make it agent-accessible often don't sit in the same place," says
Wang. "The people typically closest to what customers actually ask—like sales and support—are the
least equipped to make those answers reachable, and the people who could make them machine-readable
aren't the ones holding that knowledge."

Less than half of respondents have a specific team that's responsible for ensuring non-docs surfaces
are AI-ready. The majority, 57%, has no clear owner.

**Figure 10. If your company wanted to make knowledge other than docs readable by AI agents, such as
its help center or community site, who would be responsible for that work?** (Base: 328 valid
responses. 1 unclassifiable answer excluded)

- A specific team, and it's clear who — 43%
- It would need to be assigned — 38%
- Nobody obvious — 12%
- Not sure — 7%

> **Enter the knowledge engineer.** Today, teams struggle with a lack of ownership for making
> knowledge AI-ready. To solve this, more companies are hiring designated "knowledge engineers" to
> build and maintain systems that keep knowledge synchronized across the company. Rather than
> manually choosing and writing every word, this role focuses on designing the prompts, context,
> automations, and agents that produce and maintain content. A successful knowledge engineer sets
> the standards and processes for their entire team to capture and use information.
> [Learn more about knowledge engineering](/blog/knowledge-engineer)

Top companies are recognizing these issues and that knowledge doesn't stop at docs. They've stopped
treating it as a collection of static, siloed repositories and started running it as operational
infrastructure the whole business depends on. Documentation, changelog, community, and everything
else live on a single system that's agent-accessible by default and designed to maintain itself at
scale.

"This layer is what actually unlocks a future where an agent can take action and run long-horizon
tasks for your company and your customers," says Hou. "These outputs are what drive actual business
outcomes, so getting the foundation right matters more than most teams realize."

### Knowledge infrastructure in practice

One company already doing this is Microsoft Foundry. As Microsoft's unified platform for building,
grounding, and governing AI apps and agents, Foundry needed more than a docs site. But its existing
solution constrained design, left roughly 40% of API docs with missing or inaccurate return values,
and offered no llms.txt or Markdown hosting.

The team decided to create an entirely new developer experience: a knowledge center embedded
directly in the Foundry portal. Documentation and API reference, roadmap and labs pages, a model
showcase, an auto-generated changelog, and a community hub—all in one place, inside the product.

Every page can be copied or viewed as Markdown. An auto-generated llms.txt indexes the content for
LLMs. Semantic HTML maps to typed MDX components, so the pages are structured for machines as much
as rendered for people.

> "Docs alone just don't cut it anymore. As agentic AI keeps advancing and doing more work for
> people, we'll see more companies join the ranks of leaders like Microsoft Foundry, Decagon,
> Coinbase, and Anaconda by putting knowledge infrastructure in place that makes content accessible
> to both humans and agents." — Han Wang, CEO, Mintlify

## Conclusion

On the one surface companies have made ready, documentation, agents went from reading to writing in
a single year. It's quickly becoming a system that maintains itself, with people deciding what
ships.

But everywhere else a company's knowledge lives—the community, sales enablement, the release
notes—hasn't followed. So the depth races ahead on one part of company knowledge while everything
else sits stagnant, written for an audience that's now in the minority. That gap is the work of the
next few years, and it isn't only technical.

Ironically, most companies don't yet realize this applies to them. Some 79% rate their own knowledge
as "about average" or "ahead of most other companies." Yet just 7% have made every surface they own
readable by an agent, illustrating that AI confidence is running well ahead of readiness.

**Figure 11. How would you rate the AI-readiness of your company's knowledge?** (All 329
respondents. Percentages do not sum to 100 due to rounding)

- Ahead of most companies — 39%
- About average — 40%
- Behind — 19%
- Not sure — 3%

"Building the knowledge layer takes more than technical infrastructure," concludes Decagon's Hou. "It
takes people and operating infrastructure too—the whole organization has to buy in, or a real source
of truth never happens. That's the operational problem: getting a company to actually treat
knowledge as one shared asset, and building a system where this knowledge can grow and self-heal
over time."

In the meantime, agents aren't waiting for any of this to get sorted. They're already reading
everything they can reach, and answering from whatever they find. This raises an uncomfortable
question: How much are you investing in knowledge that's becoming increasingly invisible?

Documentation is where the work starts. It can't be where it ends. To learn more, visit
[www.mintlify.com](https://www.mintlify.com).

## Methodology

This report combines server-side traffic data from Mintlify-hosted documentation sites, Mintlify
product telemetry, a controlled open-source benchmark, external sources, and survey findings.
Traffic analysis covers February 1 through August 31, 2026.

Human traffic is captured through client-side analytics—page loads and events recorded in the
browser. Agent traffic is measured through server-side requests for machine-readable versions of
pages, agent-friendly assets like llms.txt, and HTML page fetches by recognized AI user-agents.
Because these two collection methods differ, direct comparisons are estimates.

## About Mintlify

Mintlify is the AI-native knowledge infrastructure company that makes knowledge accessible to humans
and agents.

As AI agents become the primary consumers of documentation, we're building the layer that makes it
easy for them to understand, use, and discover every product.

Mintlify powers documentation for over 20,000 companies, including Anthropic, Microsoft, Coinbase,
Spotify, and HubSpot. Knowledge on Mintlify reaches over 50M people a month.

## Documentation is where the work starts. It can't be where it ends.

Get your copy of the 2026 State of Knowledge Report.

[Download PDF](/new/knowledge-report/state-of-knowledge-report-2026.pdf) · [Visit our homepage](/)
