---
title: "🎧 Inside OpenAI’s Agentic Browser, Atlas"
author: "Rhea Purohit"
date: 2026-02-11
url: https://every.to/podcast/inside-openai-s-agentic-browser-atlas
words: 1650
---

# Inside OpenAI’s Agentic Browser, Atlas

Ben Goodger and Darin Fisher on building a browser that does the chores—and what that means for the web

February 11, 2026 Updated June 10, 2026

*TL;DR: Today, we’re releasing a new episode of our podcast *__AI & I__, *where *__Dan Shipper__* sits down with two members of the team building OpenAI’s agentic browser Atlas, **Ben Goodger**, head of engineering,** **and **Darin Fisher**, member of technical staff. **Watch on X or YouTube, or listen on Spotify or Apple Podcasts. *

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

The AI labs __fighting for attention__ __during the Super Bowl__ call to mind another iconic Super Bowl moment: Apple’s __1984 ad for the Macintosh__, which promised that the personal computer would be a source of unbound wonder, freedom, and delight.

They were right, but over time, the personal computer has also become cluttered with errands.

These “computer errands”—downloading a W-2 when tax season rolls around, hunting for the right coupon code before checkout, or navigating the unholy labyrinth of the Amazon Web Services dashboard just to change one permission setting—have taken over our digital lives. __Atlas__, OpenAI’s __agentic browser__, sprang from the idea that AI should handle this tedium for you.

In this week’s episode of * AI & I*,

**sat down with two members of the Atlas team,**

__Dan Shipper__**and**

__Ben Goodger__**. Goodger is Atlas’s head of engineering, and Fisher is a member of the technical staff. Both are legends of the browser world. They’ve spent decades building the modern web, working together on Netscape, Firefox, and Chrome before arriving at Atlas. From that vantage point, they told Dan how they think browsing is about to change, why building a browser is harder than it looks, and what it’s like to create a new one with AI coding tools like**

__Darin Fisher____Codex__.

Here is a link to the episode transcript.

You can check out their full conversation:

Here are some of the themes they touch on:

### How browsing the web will evolve

As agentic browsers become mainstream, they raise fundamental questions about the future of the web, and how we’ll interact with it going forward.

#### The web will survive—with less drudgery

One of the big questions hanging over agentic browsers is whether they eventually make the web obsolete. If you can stay inside ChatGPT and have agents do all the browsing for you—maybe even spin up custom pages on demand—do traditional websites cease to matter?

Goodger doesn’t buy that future. Yes, people will increasingly hand off tedious or mechanical work to agents. But he believes there is a category of activities, like shopping and travel planning, where people still want to be directly involved. The web’s abundance, in these cases, is part of its appeal; it’s a place to wander rather than a resource to extract.

Fisher offered an analogy: He loves taking Waymos, but he also loves driving his stick shift. Sometimes you want the convenience of being chauffeured; other times, you want tactility and control—and the future involves moving between the two modes depending on the task. While AI might synthesize information for you, what to ignore and what to act on is still up to you. You might ask a model to prepare a shopping cart, but you’re still going to want to look at what’s in it before you buy. You’ll probably incorporate the two modes, says Fisher, very naturally in your life.

#### A browser as a guide, not just a doorway

For most of the web’s history, browsers have been an empty door frame between you and whatever site you’re trying to reach. If they work well, you barely notice they exist. But an agentic browser introduces a new possibility: a browser that also helps you decide where to go. Dan likens this to the difference between a utilitarian taxi and a more-involved tour guide. He wonders if this new vision of the browser conflicts with what people have come to expect from the old vision.

Goodger argues Atlas is built to balance this duality. The interface is deliberately minimal, keeping the browsing experience familiar and unobtrusive—but ChatGPT sits at the heart of the product, ready when you want it. You choose how much to engage with the AI. The web is full of moments where you don’t know what to do next in order to achieve an objective. Atlas, they suggest, is designed for those situations.

### An inside look at building an agentic browser

Goodger estimates that more than half the code behind Atlas was written by __Codex__, OpenAI’s coding agent. The browser is as much built *by* AI as it is built for AI.

#### How the Atlas team uses Codex

Goodger and Fisher have been manually coding browsers together for decades, and they both say that building Atlas with AI feels fundamentally different.

For Fisher, the value lies in navigating complexity. For years they’ve worked in the Chromium codebase—the foundational code that underlies Google Chrome and other browsers including Microsoft Edge, Opera, Brave, and Atlas. That codebase has grown enormous over time, so being able to ask Codex questions about it is, Fisher says, “unbelievably useful.” The same goes for learning new techniques like how to set up a particular animation, or knowing what the right strategy is for a UI effect. “A lot of our code is able to be created by Codex because there’s a lot of straightforward aspects to what we’re doing, but there’s also very delicate aspects,” he says. “These tools can be tremendous companions as we’re trying to figure out what’s the right strategy to explore the solution space.”

#### How AI changes the experience of coding

For engineers who’ve spent decades writing software by hand, using AI coding tools can feel like __a kind of loss__: The work gets faster, but perhaps less personal. Fisher doesn’t deny that tension. He describes writing code as “almost therapeutic,” like “art, ”and views Codex as a tool that accelerates the tedious parts while leaving the satisfying ones intact. He describes spending hours on a refactor that spanned the code base—updating the same kind of code, with slight variations, in dozens of places across the project. When a similar task came up later, he handed it to Codex, and it finished in an hour by following the patterns he’d already established.

Goodger sees a similar division of labor. AI coding tools are often surprisingly good at finding elegant solutions, but they don’t always understand the context behind a decision—the reasons that aren’t written in the code. There’s still a need for the kind of judgment that comes from experience. But once you’ve made that call, AI can execute far quicker than you could yourself. “I don’t feel precious about typing that code,” he says.

Another upshot of coding with AI is that the Atlas codebase is better-tested than it otherwise would be. Writing unit tests—small pieces of code that check whether a specific part of your software works correctly—is important but tedious. Fisher notes that the team can now just ask Codex to generate them, and it often catches edge cases they didn’t think to specify. “In that regard,” Fisher says, “it’s been a fabulous friend.”

What do you use AI for? Have you found any interesting or surprising use cases? We want to hear from you—and we might even interview you.

##### Timestamps

- Introduction: 00:01:57
- Designing an AI browser that’s intuitive to use: 00:11:51
- How the web changes if agents do most of the browsing: 00:15:24
- Why traditional websites will not become obsolete: 00:25:06
- A browser that stays out of the way versus one that shows you around:00:29:00
- How the team uses Codex to build Atlas: 00:39:51
- The craft of coding with AI tools:00:44:47
- Why Goodger and Fisher care so much about browsers: 00:52:33

You can check out the episode on X, Spotify, Apple Podcasts, or YouTube. Links are below:

- Watch on X
- Watch on YouTube
- Listen on Spotify (make sure to follow to help us rank!)
- Listen on Apple Podcasts

Miss an episode? Catch up on Dan’s recent conversations with founding executive editor of *Wired* ** Kevin Kelly**, star podcaster

**, LinkedIn cofounder**

__Dwarkesh Patel__**, ChatPRD founder**

__Reid Hoffman__**, economist**

__Claire Vo__**, writer and entrepreneur**

__Tyler Cowen__**, founder and newsletter operator**

__David Perell__**, and others, and learn how**

__Ben Tossell__*they*use AI to think, create, and relate.

If you’re enjoying the podcast, here are a few things I recommend:

-
__Subscribe__to Every -
Follow
__Dan__on X -
Subscribe to Every’s
__YouTube channel__

*Rhea Purohit **is a contributing writer for Every focused on research-driven storytelling in tech. You can follow her on X at* *@RheaPurohit1* *and on* *LinkedIn. *

*To read more essays like this, subscribe to Every, and follow us on X at @every and on LinkedIn.*

*We build AI tools for readers like you. Write brilliantly with *


__Spiral__*. Organize files automatically with*


__Sparkle__*. Deliver yourself from email with*


__Cora__*. Dictate effortlessly with*


__Monologue__*.*

*We also do AI training, adoption, and innovation for companies. Work with us to bring AI into your organization.*

*Get paid for sharing Every with your friends. Join our referral program.*

*For sponsorship opportunities, reach out to [email protected].*

*Help us scale the only subscription you need to stay at the edge of AI. Explore open roles at Every.*

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
