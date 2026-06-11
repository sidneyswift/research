---
title: "Instagram's Cofounder on Why Great Products Are Still Hard to Build"
author: "Laura Entis"
date: 2026-03-25
url: https://every.to/context-window/instagram-s-cofounder-on-why-great-products-are-still-hard-to-build
words: 1554
---

# Instagram’s Cofounder on Why Great Products Are Still Hard to Build

Plus, how important are technical skills in the age of vibe coding?

March 25, 2026 Updated April 19, 2026

*We’re excited to welcome *__Laura Entis__* to Every as a staff writer. A former editor at *Fortune* and news editor at LinkedIn, Laura will cover Every as a beat—documenting how an AI-native media and software company works, our experiments, and our lessons. She writes today’s Context Window.— Eleanor Warnock*

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

## ‘AI & I’: How to build an agent-native product

Today, we’re releasing a new episode of our podcast * AI & I*.

**sits down with**

__Dan Shipper__**Mike Krieger**, cofounder of Instagram and co-lead of Anthropic Labs—the team working on experimental projects within the Claude developer—to discuss how the rules of professional product development are being rewritten in real time. Krieger brings a rare perspective as someone who has been at the frontier of two transformative technology waves, the mobile and social boom, and now agent-native software.

Watch on X or YouTube, or listen on Spotify or Apple Podcasts. You can also read the transcript.

Here are the highlights:

-
**A truly agent-native product can flex to meet user demand.**The best products today, like Claude Code, allow users to do things that their creators never intended. But that requires hard trade-offs between freedom and reliability for frontier products, an issue that Krieger’s team is learning how to solve. -
**Timelines are the difference between building now and building at Instagram.**At Instagram, it took months to hit dead ends and learn what to cut, Krieger says. Now, that cycle runs in hours. -
**Building too much, too fast with agents is a trap.**You can go from idea to a nearly-shipped product in a day, but that process doesn’t give you the incremental feedback that used to tell you what not to build. The models are great at adding features, but can create a product that lacks coherence. -
**Anthropic Labs structures product teams to be lean.**New product experiments are led by only two people, usually a product manager or designer paired with an engineer. Krieger says bigger teams tend to be too slow because of coordination complications. -
**You need to throw out your product and start over every three to six months.**AI progress means most of your software infrastructure will be outdated quickly. The best teams build this into their product strategy.

Miss an episode? Catch up on Dan’s recent conversations with LinkedIn cofounder ** Reid Hoffman**; the team that built Claude Code,


__Cat Wu____and__

**; Vercel cofounder**

__Boris Cherny__**; podcaster**

__Guillermo Rauch__**; and others, and learn how they use AI to think, create, and relate.**

__Dwarkesh Patel__**Don’t let infrastructure slow down your AI app**

Your fine-tuned model is ready, but your infrastructure isn’t. Sound familiar? Crusoe Managed Inference handles deployment and optimization so you can move from prototype to production with confidence. Their team helps you deploy, then get best-in-class performance. **Now, as a Day One launch partner for NVIDIA Nemotron 3 Super and Nemotron 3 VoiceChat, Crusoe gives you access to elite models, or bring your own, with 1M-token context windows.** Get reliable performance that stays high quality even with long prompts.

## Does persistence beat technical skills?

How important are technical skills in the age of vibe coding? We’ve been having this discussion at Every, and to some of us, the ability to build in plain English feels like the revenge of the liberal arts major.

But other skills are also needed. AI tools are now powerful enough that “the question of whether you can ship a product isn’t if you are technical or not—it’s whether you have the persistence,” says ** Mike Taylor**, head of tech consulting at Every.

This persistence often takes the form of asking the AI to explain itself again and again and again. “The core skill is to ask for help,” says ** Natalia Quintero**, Every’s head of consulting. “If you keep asking, you can become technical.”

** Austin Tedesco**, Every’s head of growth and a self-described “tech doofus,” built an agent using Claude Code that the entire team now uses to pull and analyze data about the company’s performance. Echoing Natalia’s comments, he says the key was having the doggedness to understand what was happening, the humility to ask Claude to explain it to him like he was an idiot whenever he didn’t follow, and the patience to refine the instructions when it didn’t give the right output or misinterpreted a command.

Persistence, clarity of vision, and curiosity can get you to a powerful prototype. But turning a prototype __into a reliable product__? For that, you need technical skills, or at least access to someone who has them, argues ** Naveen Naidu**, general manager of Every’s dictation app

**.**

__Monologue__An engineer, Naveen, never loses sight of a codebase’s overarching structure—something language models struggle to do. When Naveen builds a product, every decision ties back to one question: What can’t be allowed to fail? With Monologue, he knew that the vast majority of people would be using the app for dictation. If that feature failed, he’d immediately lose users’ trust. “I built my whole codebase in such a way that if my main server or database goes down, dictation doesn’t go down,” he says. “I made sure that it’s 100 percent reliable.”

Recently, the Monologue server did, indeed, go down. While new users couldn’t sign up, existing users could still dictate and didn’t notice any break in service.

Vibe coded apps often skip the information architecture step entirely. But when the code inevitably breaks, the non-technical user struggles to diagnose the problem, let alone fix it quickly. Having been the “technical” guy called upon to fix a vibe coded codebase, Naveen has found that rather than try to remedy existing structural issues, it’s sometimes easier to just start from scratch.—__Laura Entis__

## Log on

We host __camps and workshops__ on topics like __compound engineering__ and __writing with AI__ to share the knowledge we’ve acquired from training teams at companies like the__ ____New York Times____ and leading hedge funds__, and by learning and playing with AI every day ourselves.

**This week’s camp**

- Get a front-row seat to what we’re building at Every’s
, including a live walk-through of Plus One, our hosted AI agent that lives in Slack. The event takes place on Friday, March 27, at 11 a.m. ET.__Q2 Demo Day__

**Upcoming courses**

-
(April 3): Learn how to put custom agents to work inside your business with product designer__Every x Notion: Custom Agents Camp__**Brian Lovin**from Notion. -
(April 14): This beginner-friendly, live workshop led by__Claude Code for Absolute Beginners____Mike__**,**Every’s head of tech consulting, is designed to get you from zero to a working project with Claude Code.

**Recordings you may have missed**

-
**Compound Engineering Camp:**general manager__Cora__walks through, step by step, how to go from prompt to working app in under an hour using the__Kieran Klaassen____compound engineering__plugin.__Watch the recording__or__read the write-up__. -
**OpenClaw Camp:**The Every team walks through__OpenClaw__, showing how to set it up and our favorite use cases.__Watch the recording__or__read the write-up__.

## Straight from Slack

Prompts still form the backbone of AI workflows, but knowing whether your latest version is actually an improvement can be annoyingly difficult to track.

Our resident prompt expert, Mike, has a new favorite method to test and improve his prompts: __Langfuse__, an open-source tool for tracking AI model behavior that he calls “Google analytics for AI.”

Recently, when running a PowerPoint task, Mike noticed his agent was loading unnecessary skills, which cost him precious tokens. By using Langfuse to trace and label his Claude sessions, he was able to see, play by play, where the model made the wrong or right decision. “Otherwise, you have no idea if the changes you are making are helping or harming,” he says.

## One more thing

How many engineers do you need to ship a breakout product? Just two—provided they fill specific roles, argues __Dan__.

First, you need a pirate, or someone who has ambitious product ideas and moves as fast as possible to vibe code them into existence.

Once the pirate has established early product-market fit, the architect arrives to turn the prototype into something __that can reliably work at scale__.

We’ve already been using the pirate-architect model here at Every: ** Proof**, our new online editor built for agents and humans to collaborate, was built that way—as was

__Monologue__.

*Laura Entis** is a staff writer at Every. You can follow her on LinkedIn. To read more, subscribe to Every, and follow us on X at @every and on LinkedIn.*

*We also do AI training, adoption, and innovation for companies. Work with us to bring AI into your organization. For sponsorship opportunities, reach out to [email protected].*

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
