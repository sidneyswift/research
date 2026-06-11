---
title: "Inside the AI Workflows of Every’s Six Engineers"
author: "Rhea Purohit"
date: 2025-10-27
url: https://every.to/source-code/inside-the-ai-workflows-of-every-s-six-engineers
words: 934
---

# Inside the AI Workflows of Every’s Six Engineers

Each person on the team has tailored their stack to their individual tastes

October 27, 2025 Updated May 25, 2026

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

Working alongside the engineers at Every, I sometimes wonder: What do they actually do all day? Building software, just like writing, is a creative act, and by definition, that means the process is messy. When I write, I go between Google Docs and whichever LLM I’m leaning on at the moment (currently, __GPT-5__). But what does that look like for the people building software?

Sure, I hear about the products they’re shipping in standup, and I get snippets of their workflows when we run __Vibe Checks__. But those moments are always in isolation, scattered whispers of a bigger conversation.

So I asked: What does the workflow of each of our engineers really look like? What stack have they built that makes it possible for six people to run four AI products, a consulting business, and a daily newsletter read by more than 100,000 people?

### Experimenting at the edge: Yash Poojary, general manager of Sparkle

**Yash Poojary** used to be the kind of developer who insisted on doing everything from one lone laptop. A few weeks ago, he caved and added a __Mac Studio__—Apple’s high-performance desktop—to his setup. “I wanted to use my laptop for everything,” he admits, “but I felt bottleneck[ed] for testing things faster.”

The upgrade has paid off. Now he runs __Claude Code__ on one machine and __Codex__ on the other, feeding them the same prompt and codebase to see how they respond. He’s finding that the two models have distinct personalities. Claude Code is the “friendly developer,” great at breaking things down and explaining its reasoning, while Codex is the “technical developer,” more literal, more precise, and often able to land the right solution on the first try.

Yash also __recently launched__ a new version of ** Sparkle**, our AI file organizer, complete with a redesigned interface that he worked on in Figma. Back in the dark ages (aka five months ago), Yash would take screenshots of the design and paste them into Claude so it could write the code. Now, with a

__Figma MCP__integration, Claude can plug directly into the Figma file so it can read the design system itself—the colors, spacing, components—and translate that into working code. It saves steps and keeps Claude working from the real source of truth.

Outside of agents, Yash leans on __Warp__—a modern version of the developer’s command line, the text-based interface developers use to control their computers. Every time he pushes code, he jots down two lines about what he learned in a “learnings doc” and stores them in the cloud. After a few days, he has a rolling memory of recent context to feed back into his AI tools.

Even with all this experimentation, Yash emphasizes the importance of guardrails. He structures his day around one big task and a handful of smaller background ones, and he’s careful not to let AI-generated suggestions derail him. As he puts it: “The problem with CLIs [command line interfaces] is it’s easy to get derailed and lose focus on what you’re actually trying to build… so building guardrails into the system is essential.”

One way he’s doing that is with __AgentWatch__, an app he built that pings him when a Claude Code session finishes, letting him run multiple sessions simultaneously without losing track of them. Yash—and a __smattering of others__—have been using it of late; if you give it a try, __DM__ him.

He’s also split his day into two modes: Mornings are for focused execution—just Codex and Claude Code, no new tools allowed—so shipping doesn’t stall. Afternoons are for exploration, when he experiments with new agents, apps, and features. That separation between “build” and “discover” has removed the productivity drag he used to feel when testing new tools.

### Orchestrating the loop: Kieran Klaassen, general manager of Cora

For Kieran, everything with **Cora** starts with a plan__ generated__ __in Claude Code__ with a set of custom agents and workflows. He scopes programming plans at three levels, depending on the feature:

- Small features: simple enough to one-shot
- Medium features: span a few files and go through a review step (usually by Kieran)
- Large features: complex builds that require manual typing, deeper research, and lots of back-and-forth

The point of planning, he says, is to ground the work in truth—best practices, known solutions online, and reliable context pulled in through __Context 7 MCP__, a tool that pulls up-to-date, version-specific documentation and code examples straight from the official source and places them directly into your prompt.

Once the plan is set, it gets sent to GitHub. From there, he uses a work command—a prompt that takes the plan and turns it into coding tasks for the AI agent. For most projects, Claude Code is his go-to, because it gives him more control and autonomy. But he’ll sometimes turn to Codex or the agentic coding tool __Amp__ for more traditional or “nerdier” features.

##
The Only Subscription

You Need to

Stay at the

Edge of AI

The essential toolkit for those shaping the future

"This might be the best value you

can get from an AI subscription."

- Jay S.

Join 100,000+ leaders, builders, and innovators

Email address

Already have an account? Sign in

### What is included in a subscription?

Daily insights from AI pioneers + early access to powerful AI tools

## Comments

Don't have an account? Sign up!
