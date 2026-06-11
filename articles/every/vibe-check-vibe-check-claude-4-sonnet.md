---
title: "Vibe Check: Claude 4 Opus"
author: "Dan Shipper"
date: 2025-05-22
url: https://every.to/vibe-check/vibe-check-claude-4-sonnet
words: 988
---

# Vibe Check: Claude 4 Opus

Anthropic’s new model crushes pull requests, research deep dives, and honest editing—yet o3 keeps the daily-driver crown

May 22, 2025 Updated December 17, 2025

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

This week has been a doozy: I went to Microsoft Build and __interviewed the company's CTO __** Kevin Scott**, we

__announced our fundraise__in the

*, Google held its I/O event (more on that from*

__New York Times__**tomorrow), OpenAI**

__Alex Duffy____acqui-hired__Apple designer

**Jony Ive,**and today I’m at Anthropic’s Code With Claude event. Let me state for the record: I am tired of all of this progress. My fingers feel like they are about to fall off, and my brain is functioning at a comparable intelligence to GPT-2.

But there’s a new Claude model launching today, for which I had to uphold my promise of writing __day-o, hands-on vibe checks__. So here it is for the long-awaited Claude 4 Opus (which Anthropic had code-named Linen), the follow-up model to __Claude 3.7 Sonnet__. (Besides, who needs fingers when voice-to-text AI is this good?)

I tried Opus on a variety of tasks, from coding to writing to researching. My verdict: Anthropic cooked with this one. In fact, it does some things that no model I’ve ever tried has been able to do, including OpenAI’s __o3__ and Google’s __Gemini 2.5 Pro__.

Let’s get into benchmarks. We’ll start, as always, with the __Reach Test__.

## The Reach Test: Do we reach for Opus over other models?

#### For day-to-day tasks: **no**

I’m still an o3 boi. I think this has a lot to do with ChatGPT’s memory—it’s an incredibly sticky feature. Opus would have to be a lot smarter and faster to make the trade-off worth it.

#### For coding: **yes**

It’s a beast in Claude Code, Anthropic’s __command line interface__ for programmers. If you assign it a task, it will code for long periods of time on its own with no intervention. It __one-shotted__ a few complex pull requests better than OpenAI’s coding tool __Codex__. For example, I asked it to implement an infinite scroll feature in __Cora__, our AI email assistant—i.e., to keep scrolling to see your next unread email summary. It made a good infinite scroll experience. We couldn’t ship it as it was, but it was close.

Anthropic seems to have solved Claude 3.7 Sonnet’s famously overeager personality, too. No longer does the model try to build the Taj Mahal when you ask it to change a button color.

** Kieran Klaassen**—Cora general manager, resident Rails expert, and opinionated agent-ophile—is also loving it, and he’s a tough sell. Advantage Claude.

#### For writing and editing: **yes** and **no**

o3 is still a significantly better writer. But Opus is a great editor because it can do something no other model can: It edits honestly—no rubber-stamping.

One of the biggest problems with current AI models is they tell you your writing is good when it is obviously bad (ask me how I know). Earlier versions of Claude, when asked to edit a piece of writing, would __return a B+__ on the first response. If you edited the piece at all, you’d get upgraded to an A-. A third turn got you to an A.

As much as I wish my physics teacher graded me like this in high school, it’s not how I want my AI models to work. I want ** R. Lee Ermey** with a thesaurus and a red pen.

*ChatGPT’s version of R. Lee Ermey in the 1987 movie *Full Metal Jacket*. Source: ChatGPT-4o image generation/Dan Shipper.*

To my delight, Opus is a good judge of writing. To test it, I worked with __Spiral__ general manager ** Danny Aziz**, our resident expert on teaching LLMs to write. We gave it a set of writing principles that attempt to outline what good writing is. For example, good writing elicits genuine emotional and intellectual investment from the reader, and avoids predictable patterns and cliches.

We fed it both interesting and boring writing (the latter was probably mine), and it nailed which pieces were boring and why:

*Source: Opus/Dan Shipper.*

Not only does Opus not glaze you, it can keep multiple principles in mind at once even when they’re hidden in the middle of long prompts with lots of context. Other models often narrow in on one principle to the exclusion of the others (ask **Sam Bankman-Fried** if you want to know __how well that works out__).

Danny found that “other reasoning (3.7, o3, and o4-mini) models tend to lose sight of their writing principles when they’re dealing with lots of context, like a lot of source material or a long chat. Opus (with reasoning) does a great job of continually reminding itself what it needs to do so the principles don’t get lost.”

Opus can also notice subtle patterns across large blocks of text. which is useful if you, like me, are writing a book. I fed it 50,000 words of a book I’m writing and asked it to find themes and patterns that I hadn’t written about yet. Could it tell me what I’m trying to say better than I can? The answer is yes. It found a few ideas about my parents’ divorce and my relationship to work that run throughout the book. While I knew this already, in an unspoken way, Opus put its finger on it.

*Source: Opus/Dan Shipper.*

#### For longer research tasks: **yes**

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
