---
title: "The Folder Is the Agent"
author: "Kieran Klaassen"
date: 2026-04-13
url: https://every.to/source-code/the-folder-is-the-agent
words: 888
---

# The Folder Is the Agent

I'm running 44 AI agents across multiple projects. Each one is just a model pointed at a folder.

April 13, 2026 Updated June 5, 2026

*On Friday, April 17, *__Cora__* general manager *__Kieran Klaassen__* will lead a camp for Every paid subscribers on compound engineering, the AI-native engineering philosophy that he built and that has more than 14,000 stars on GitHub. Since the last camp, Kieran and product leader **Trevin Chow** have built out product-focused workflows to make the methodology as valuable for product managers and founders as it is for engineers. In this camp, they’ll walk you through what’s new, go deeper on the brainstorm and ideate steps, and share examples of using compound engineering beyond engineering work. Read the full compound engineering guide, install the plugin, and join us for the camp.—Kate Lee *

I spent three months trying to make __agent swarms__ work.

The idea of multiplying myself by coordinating multiple agents at the same time was a compelling pitch as the sole engineer building Every’s AI email assistant, ** Cora**. If I could summon a fleet of

__AI agents__, let them coordinate, and watch them produce work no single agent could match, it would relieve some of my overwhelm.

I tried everything to make it work—__Claude Code__ teams, agents dispatching tasks to other agents, __orchestration setups__ where a lead agent managed a pool of workers. Many iterations, many burned tokens.

But more agents didn’t make me faster. I’ve __run parallel Claude Code sessions__ for months, which works when each agent has a clear task, and I’m directing the work. The swarm experiment was different: agents coordinating with each other, deciding what to work on, producing output I hadn’t shaped. When 10 of them finished simultaneously, I had 10 __results to evaluate__ without enough context to know which ones I could trust. AI agents don’t have a speed limit, but the person managing them still does.

I kept looking for a smarter orchestration layer—a better protocol or a tighter framework that would filter the output and tell me which result to trust. Then I stopped and looked at what was really doing the work.

It was something I already had—a folder.

A project folder with a CLAUDE.md/AGENT.md (the file that tells an AI how to work in your project), some __skill__ definitions, and context accumulated through months of __compound engineering__—that’s an agent. The context that this folder gives an AI model makes the generalized model a specialist in whatever task or field you want it to excel in.

I’m running 44 of these folders-as-agents across multiple projects now. Each one runs inside a specialized folder I’ve built and tested over months, and a dispatch layer I built on top does the routing between them. Here’s how it works.

**The agents hiding on your hard drive**

People hear “agent” and picture a __Rube Goldberg machine__—dozens of comically complex moving parts, each one triggering the next. But an agent is much simpler: a model with enough context so you don’t have to re-explain everything each time you open the chat.

Here’s an example: All of Cora’s code lives in a project folder in the Every organization on GitHub. When I open that folder with Claude, Claude can see the code and the structure. But it doesn’t know my way of working or what I care about, which is why the folder also includes a __CLAUDE.md__ file. The file tells Claude how I name things and how I structure tests. That’s an agent—not a fancy one, but an agent nonetheless. Just by pointing the model at this folder, which contains some of my personality, knowledge, and __taste__, the model can be a specialist in my codebase.

Claude Skills—files that give the model specific capabilities—are an example of this “folder as agent” structure. Before anyone called them “skills,” people were already writing markdown files full of instructions and dropping them into project directories.

My ~/cora/ folder goes further:

-
**Conventions and standards:**The CLAUDE.md covers Rails conventions, deploy workflows, and database patterns. -
**Institutional knowledge:**The docs/developer-docs/ directory holds accumulated knowledge that any new agent inherits automatically, including architecture reports, the email processing pipeline, and the__assistant system design__. -
**Operational memory:**The docs/runbooks/ and docs/investigations/ capture operational patterns built from real incidents. -
**Specialized agents:**.claude/agents/ holds specialists I’ve refined over months: reviewers, planners, and the assistant-component-creator.

When I point a model at this folder, it starts working with everything Cora knows about itself.

The reading order I give to every new agent that touches Cora is the following: Read CLAUDE.md first, then the architecture document, then the assistant system report, then the assistant’s prompt, then the component creator agent.

~/cora-agent/, another folder, is a completely different agent, though it runs on the same model. (I mostly use __Opus 4.6__, but also like __GPT 5.4__ and __Gemini Pro__ 3.1.)

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
