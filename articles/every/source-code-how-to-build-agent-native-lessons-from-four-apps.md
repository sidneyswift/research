---
title: "How to Build Agent-native: Lessons From Four Apps"
author: "Katie Parrott"
date: 2026-02-17
url: https://every.to/source-code/how-to-build-agent-native-lessons-from-four-apps
words: 975
---

# How to Build Agent-native: Lessons From Four Apps

Start with three simple tools, and let the AI figure out the rest

February 17, 2026 Updated May 23, 2026

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

** Dan Shipper** scanned a page from

**Erik Larson**’s

**Winston Churchill**biography,

*The Splendid and the Vile,*and pressed save. The app he was demo-ing identified the book, generated a summary, and produced character breakdowns calibrated to exactly where he was in the story—no spoilers past page 203.

Nobody programmed it to do any of this.

Instead, Dan’s app has a handful of basic tools—“read file,” “write file,” and “search the web”—and an AI agent smart enough to combine them in a way that matches the user’s request. When it generates a summary, for example, that’s the agent deciding on its own to search the web, pull in relevant information, and write a file that the app displays.

This is what we call __agent-native architecture__—or, in Dan’s shorthand, “__Claude Code in a trench coat__.” On the surface, it looks like regular software, but instead of pre-written code dictating every move the software makes, each interaction routes to an underlying agent that figures out what to do. There’s still code involved—it makes up the interface and defines the tools that are available to the agent. But the agent decides which tools to use and when, combining them in ways the developer never explicitly programmed.

At our first Agent Native Camp, Dan and the general managers of our software products ** Cora**,

**, and**

__Sparkle__**shared how they’re each building in light of this fundamental shift. They’re working at different scales and with different constraints, so they’re drawing the lines in different places. Here’s what they shared about how the architecture works, what it looks like in production, and what goes wrong when you get it right.**

__Monologue__**Key takeaways**

-
**The AI is the app.**Instead of coding every feature, you define a few simple tools the AI is allowed to use—for instance, read a file, write a file, and search the web. When you ask it to do something, it decides on its own which tools to reach for and how to combine them. -
**Simpler tools get smarter results.**The smaller and more basic you make each tool, the more creatively the AI combines them. Claude Code is powerful because its core tool—running terminal commands—can do almost anything. -
**Rules belong in the tools, not the instructions.**You can ask an AI to be careful, but it might ignore you. If an action is irreversible—like deleting files—the safeguard has to be built into the tool itself. -
**You don’t have to start over to start learning.**Give the AI a safe space to interact with your existing app and experiment outside the live product. You’ll learn what the agent needs without risking what already works. Just don’t get attached to the code—as models improve, expect to throw things out and rebuild every few months.

**How agent-native works**

Traditional software can only do what it’s explicitly programmed to do by its code. Click “sort by date,” and it sorts by date. Click “export,” and you get a CSV. It will never spontaneously summarize your inbox or reorganize your files by topic—unless someone wrote the code for that exact feature.

Instead of coded features, an agent-native app has tools (small, discrete actions like “read file” or “delete item”) and skills (instructions written in plain English that describe how to combine those tools). An agent uses those tools and skills to produce an outcome that you specify, such as identifying what book you are reading from one page.

Three principles make this work:

-
**Parity:**Whatever the user can do, the agent can do. Every click, form submission, and interaction is available to both. -
**Granularity:**Tools should be atomic—small and single-purpose—and features, such as a personalized book summary or a Monday morning email brief, should live at the skill level where they can be written and modified in plain text. -
**Composability:**When tools are atomic and skills can combine them freely, the app develops the ability to do things nobody explicitly designed for.

But there are trade-offs. Agent-native apps are slower because the agent has to reason through each request instead of running deterministic code—pre-written instructions that always produce the same result. They’re more expensive because every interaction burns tokens, the unit AI companies use to measure and charge for usage. And they’re less predictable—the same request won’t always produce the same result, which makes security harder to guarantee.

Dan’s bet is that inference costs—the price of having the AI think—drop roughly 80 percent every few months, making this architecture cheaper over time. But today, it’s still expensive. __Cora__ general manager ** Kieran Klaassen** has seen days where those costs hit $1,500 with thousands of users. Risks like this are important to keep in mind when you’re getting started with building in an agent-native way.

**Three tools and a filesystem**

** Naveen Naidu**, general manager of

__Monologue__, took the architecture to its most minimal extreme. He’d been building a read-later app as a side project—something like Pocket or

__Instapaper__, where you save articles from the web and read them later. But instead of a traditional database, the entire backend is a set of folders, and an AI agent helps you interact with everything you’ve saved.

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
