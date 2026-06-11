---
title: "AI Work Is Splitting in Two"
author: "Every Staff"
date: 2026-05-10
url: https://every.to/context-window/ai-work-is-splitting-in-two
words: 1509
---

# AI Work Is Splitting in Two

Plus: Anthropic’s agent push, ChatGPT as project manager, and optimism in biotech

May 10, 2026 Updated June 3, 2026

Hello, and happy Sunday! This week belonged to agents. OpenAI had a “low-key” launch party for __GPT-5.5__ on May 5 at 5:55 p.m., a time chosen by the model itself. The following day Anthropic held its second annual __Code with Claude developer conference__, where the company announced three new features for its Managed Agents product, along with—more suprisingly—a partnership to use SpaceX’s Colossus supercluster.

Every was on the ground in San Francisco at Code with Claude. Taken together with the way Codex has been showing up inside Every, it became easier to see that __battle lines are being drawn__ on two fronts: desktop apps for you and a model to collaborate with in real time as you work, and long-running agents like __OpenClaw__ or Claude Managed Agents that teams hand off work to. It matches how agents inside Every __have bifurcated__ into ones we delegate to and ones we collaborate with, and signal we’re seeing from frontier labs __embedding employees__ in large enterprises.

Scroll down for a special weekend *AI & I* with two engineering heads at Anthropic, workflows to steal for __hitting inbox zero with Codex__ or __deciding which AI tools are worth testing__, and how Every COO __Brandon Gell____instills curiosity__ in both his newborn son—and in himself. We’ve also been keeping an eye on the **Elon Musk** versus OpenAI trial. Discovery has surfaced plenty of gossipy, occasionally jaw-dropping text messages, but so far none of it changes much for the day-to-day user.—__Kate Lee__

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

## ‘AI & I’: The secrets of Claude’s platform from the team that built it

In the future, you’ll be able to accomplish a goal by just giving Claude an outcome and a budget.

That’s the direction Anthropic is building in with its new Managed Agents features, announced at this week’s Code with Claude developer event. The basic idea: Claude, wrapped in a computer in the cloud, that you can spin up, scale, and manage as needed. Anthropic is taking on the infrastructure that kills most agent products, and making sure that it scales to meet the needs of agents running 24/7.

On a special episode of *AI & I *recorded at Code with Claude, ** Dan Shipper **talks with Jiang and

**Katelyn Lesse**, head of engineering for the Claude platform, about what it takes to build an AI infrastructure platform. This is a must-watch for anyone trying to take an agent past the demo and into production. Watch on X or

__YouTube__, or listen on

__Spotify__or Apple Podcasts.

Miss an episode? Catch up on Dan’s recent conversations with Stripe’s ** Emily Glassberg Sands**, Every’s


__Brandon Gell____and__

**, Linear cofounder**

__Willie Williams__**, and others, and learn how they use AI to think, create, and relate.**

__Karri Saarinen__## Knowledge base

__“Inside Anthropic’s 2026 Developer Conference”__*by* __Dan Shipper__,__Marcus Moretti__, and* Katie Parrott/Chain of Thought:* Dan and

**general manager**

__Cora__**attended Anthropic’s 2026 Code with Claude, and this piece is a report from the ground. The centerpiece is Anthropic’s new Managed Agents features, which**

__Kieran Klaassen__**general manager**

__Spiral__**has been testing in his workflows, as well as the new “Dreaming” feature Kieran is most excited about. Read this for what Anthropic announced, what mattered, and how the tools are already being used in practice.**

__Marcus Moretti____“I Let ChatGPT Manage My Workweek”__*by* *Katie Parrott/Working Overtime:* ** Katie Parrott** is a self-described disaster at project management, a gap she papered over for 15 years by keeping deadlines in her head and avoiding ambitious projects. As her work got more complex, that stopped being sustainable, so she built a ChatGPT agent that reads her OKRs, calendar, Notion, and Slack and tells her what to do next. Read this for the setup, the limits AI can’t fix, and the copyable prompt that powers the whole system.

__“The Culture of AI Engineering”__*by Noah Brier/Thesis: *The “software factory” metaphor is everywhere in AI engineering, but Alephic cofounder **Noah Brier** argues it’s the wrong one. Running a software company is less like **Henry Ford**’s assembly line and more like **Andy Warhol**’s studio: The hard problem isn’t throughput, it’s keeping everyone building the same vision. **Brier** adapts **Stewart Brand**’s pace layers framework into a five-level cultural stack to keep humans and agents aligned. Read this to understand why onboarding your agents matters as much as onboarding your engineers.

__“The Dawn of Codex-native Apps”__*by* *Katie Parrott/Context Window:* AI work is splitting into two modes—delegation and collaboration—and the new meta-skill is knowing which one fits the task. Read this to discover why the __allocation economy__ thesis was only right about half the work, and what’s in the other half.

__“OpenAI Flips the Script”__*by Laura Entis/Context Window: *Three months after ** Dan Shipper** wrote that OpenAI had catching up to do, he and head of growth

**have made Codex their daily driver for strategy docs, recruiting, and other kinds of knowledge work. 🎧 🖥 Listen to their episode of**

__Austin Tedesco__*AI & I*on

__Spotify__or

__Apple Podcasts__, or watch on

__X__or

__YouTube__.

## From Every Studio

**Spiral lets you start from a blank page and stop mid-stream**

** Spiral** is one of the first products to use Claude’s new multi-agent feature in production. When you use the Spiral CLI to request multiple drafts, a

__Managed Agent__spins up multiple Opus-class subagents to write your drafts in parallel— cutting the response time by 20-30 seconds per draft. Spiral also shipped improvements to the core app flow. You can start a session with a blank draft in addition to a new chat message. You can stop a Spiral response mid-stream if you need to add or change something from your previous message. And the guard against AI tells in Spiral output has been improved based on user input.—


__Marcus Moretti__## Alignment

**The case for optimism. **The holy grail of any product is low marginal cost and high value. That is why software ate the world and why investors loved it. Biotechnology, however, is the polar opposite. A new drug costs hundreds of millions in research and development, then has to clear approval, then has to be manufactured, and out of every 100 candidates, only two or three reach the pharmacy shelf. The gross margins are *fine* once a drug ships, but the pipeline to get there is long and expensive.

Biotech was never going to scale the way software did. Yet R&D productivity in biotech is rising for the __first time__ in many years, and the investors calling biotech a money pit are back at the table. There are a couple of reasons why.

We understand biology a lot better than we did even a decade ago, because we’re able to narrow the search space before we run an experiment. AlphaFold—Google DeepMind’s AI program for predicting the 3D shapes of protein—mapped roughly __200 million__ in a year. Instead of spending years figuring out a target’s structure, researchers can now begin with that information already in front of them.

The second reason is the collapse in the cost of reading the genome. Sequencing a single human genome cost around __$100 million__ in 2001 and now costs about $200. We can sequence at population scale, and once you’re able to do so, you can start to see which genetic variants drive disease and which are noise.

We now have maps of protein, genes, and cells that are starting to add up to a coherent picture of disease. For most of the history of medicine, we worked at the level of the organ, so we could see the disease but never its origins. Now we work at the level where disease happens—a genetic variant produces a misfolded protein, the misfolded protein disrupts a cellular pathway, and the cellular disruption is the disease.

Of course, the marginal cost of a drug will never be zero. But the marginal cost of asking what a disease is, and where to look for the answer, is collapsing. Lower R&D costs mean more breakthrough drugs, which means patients live longer and investors make money. The incentives, for once, point in the same direction.—__Ashwin Sharma__

*That’s all for this week! Be sure to follow Every on X at @every and on LinkedIn.*

*We build AI tools for readers like you. Write brilliantly with Spiral. Organize files automatically with *


__Sparkle__*. Deliver yourself from email with*

__Cora__. Dictate effortlessly with__Monologue__. Work on documents with AI agents using

__Proof__*.*

*For sponsorship opportunities, reach out to [email protected].*

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
