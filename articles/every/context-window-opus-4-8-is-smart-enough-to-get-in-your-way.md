---
title: "Opus 4.8 Is Smart Enough to Get in Your Way"
author: "Laura Entis"
date: 2026-06-03
url: https://every.to/context-window/opus-4-8-is-smart-enough-to-get-in-your-way
words: 1397
---

# Opus 4.8 Is Smart Enough to Get in Your Way

We revisit Anthropic’s newest model, Figma responds to the 'SaaSpocalypse,' and how Every’s senior designer wrangles multiple image generators

June 3, 2026 Updated June 11, 2026

Today, we update our __Opus 4.8 Vibe Check__ with a Pulse Check featuring perspectives from more team members, ** Dan Shipper** sits down with Figma’s

**Matt Colyer**to unpack why AI hasn’t killed professional design services, and Every senior designer

**Daniel Rodrigues**shares the two-tool AI workflow he uses to get precise, visually stunning results.

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

### ‘AI & I’: The limits of chat-based design

In a new episode of our podcast, * AI & I*,

**Dan**

**talks with**

**Matt Colyer**, Figma’s director of product management for developers, about the limits of chat-based AI agents for design and why the rise of vibe-coded everything is, despite what you might have heard, a boon for the company.

Watch on __X__ or __YouTube__, or listen on __Spotify__ or __Apple Podcasts__. (You can also read the transcript.)

Here are the highlights:

-
**The “SaaSpocalypse” narrative has it backwards.**AI agents turn anyone into a vibe coder, kicking off investor panic that traditional software-as-a-service (SaaS) companies like Figma would cease to justify their cost. Colyer isn’t worried: AI has exponentially expanded the developer base, while underscoring how difficult it is to create a vibe coded version of Figma that works as well or as reliably as the real thing. He’s vibe coded multiple agents to do stuff like handle his emails, but the maintenance costs piled up quickly and never seemed worth it. “I’m buying more software these days than I ever did before,’” he says. “‘I’m just going to pay somebody else to run my agent for me.’” -
**Figma is embracing agents.**The company has launched an MCP server—a standardized interface any AI tool can plug into—that allows you to approach design work from two directions. “Code to design” takes a live web page and reconstructs it on the Figma canvas, so you can manipulate the elements directly; meanwhile, “design to code” flips the process by packaging a Figma design and giving it to an agent, which makes changes for you via pull request. -
**There’s a ceiling to chat-based generative design.**Great design hinges on a diamond-shaped process: First you diverge, or generate lots of ideas, and only then do you converge around the most promising options. Text-based chats are inherently linear and therefore bad at divergence; the setup forces you to__select an option__and iterate on it. Agents are already good at the task-completion workflows Figma supports today, but the divergent, exploratory part of design remains unsolved across the industry. Colyer is interested in dividing the process so specialized agents handle the divergence by pushing you to expand your thinking, while another set filters through the options to identify a single path forward. “Even the best agents, the command-line agents, don’t have the ability to do those workflows,” he says. “That’s where I see the future of design and product thinking.” -
**Agents can produce so much so quickly.**They’re less good at determining whether any of it meets a company’s values or design standards. Colyer isn’t sure the best way to close this gap—maybe it’s a video walkthrough, a screenshot, or a trusted review agent—but for good design to scale, AI needs to play a larger role in evaluations.

Miss an episode? Catch up on Dan’s recent conversations with LinkedIn cofounder ** Reid Hoffman**; the team that built Claude Code,

**and**

__Cat Wu__**; Vercel cofounder**

__Boris Cherny__**; podcaster**

__Guillermo Rauch__**; and others, and learn how they use AI to think, create, and relate.**

__Dwarkesh Patel__## Pulse Check: Opus 4.8 is the best tool for the right job

Five days ago, we called Anthropic’s __Claude Opus 4.8__ the best Claude model yet for writing and serious engineering, and said we’d switch to it from __GPT-5.5__ if the Claude app ever caught up to __Codex__. After a work week of more testing, we’re still an Opus 4.8 admiration society, although the results are a bit more mixed as people from different disciplines have had a chance to weigh in.

Here’s what more of the Every team has to say about when to use the model and when to steer clear.

**Key takeaways **

-
**Reach for Opus 4.8 when productive friction improves the work.**It’s good at tracking nuance, questioning a weak framing, and staying with a complicated problem. But the same instinct can become stubbornness, misplaced caution, or confidence in a wrong interpretation. -
**Give it the long, messy jobs.**Opus 4.8 earned its strongest reviews on sprawling source material, long-running threads, difficult creative work, and complex coding tasks. For routine questions and clearly scoped work, its slower pace and higher token burn can wipe out the quality gain. -
**Do not rebuild your workflow around it yet.**Even teammates who preferred Opus’s answers kept reaching for GPT-5.5 in Codex because speed, context, and a better-connected app outweighed model advantage. -
**Double-check security warnings.**Two independent accounts reported that Opus invented a prompt-injection concern. Until that failure is understood, ask it to show the evidence behind a warning before you act on it.

**The Reach Test, part II **

**Arielle Shipper, head of operations 🟩**

**Arielle Shipper**, Every’s new head of operations, has spent the last few weeks on a discovery tour. She used Opus 4.8 to redo an HTML site showing a summary of her findings, after building the original with __Opus 4.7__. She noticed meaningful improvements: 4.8 distinguished between two similarly named pages in Notion without the explicit guidance 4.7 had required, and suggested highlighting a count of how many times specific topics came up in her conversations with the team. Her summary: “It seems really detail-oriented in a way I appreciate.”

#####
**Austin Tedesco, head of growth** 🟨

Austin spent the weekend using Opus 4.8 on an essay with ** Monologue**, our speech-to-text tool, and our writing app,

**. For that job, he wrote that Opus 4.8 “is the best model available,” a step up from Opus 4.7 and “materially better than GPT-5.5.” But he doesn’t expect it to change his daily behavior. GPT-5.5 is “pretty good” at the same kind of creative partnership, he said, and keeping his work in Codex matters more than the modest quality improvement: “I don’t see myself reaching for Claude models much without a materially better desktop app experience, or such a dramatic leap in model quality that the harness matters less.”**

__Spiral__#####
**Nityesh Agarwal, senior applied AI engineer** 🟩(model) / 🥇(dynamic workflows)

Nityesh tested Opus 4.8 inside the AI employees he is building for Every—__Claudie__ for consulting, Andy for the editorial team. He reported that the model recalls the right memory at the right time, stays useful in longer threads, and lets him use more of its 1-million-token context window, the amount of material it can handle in one conversation. But Anthropic really won his heart with __Dynamic Workflows__, the workflow-automation feature released alongside Opus 4.8. Combined with the new model, Nityesh says it feels like “a major power-up.”

#####
**Lee Knowlton, software engineer ** 🟨 ** **

Anthropic says Opus 4.8 is more honest and better at flagging risks. But Lee saw the negative side of that instinct during a daily planning run he’d repeated for months where Claude used his calendar, Slack, and notes to create a plan for his day. One morning, the plan cited events, messages, and files Lee couldn’t find in those sources. When he asked Claude what had happened, it claimed a prompt-injection attack had supplied fake information. When Lee challenged it, Claude said it had invented that story to explain its own bad output, mistaking a planning file Lee had moved for evidence of interference. The exchange left him reluctant to trust the model’s explanations for its own behavior.

**Andrey Galko, engineer 🟩**

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
