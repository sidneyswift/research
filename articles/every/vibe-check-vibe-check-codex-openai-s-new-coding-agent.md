---
title: "Vibe Check: Codex—OpenAI’s New Coding Agent"
author: "Dan Shipper"
date: 2025-05-16
url: https://every.to/vibe-check/vibe-check-codex-openai-s-new-coding-agent
words: 1913
---

# Vibe Check: Codex—OpenAI’s New Coding Agent

Our hands-on day-0 review of the new autonomous software engineer

May 16, 2025 Updated January 28, 2026

🎧 🖥 *Bonus: A special episode of *__AI & I____ __with OpenAI product team member *Alexander Embiricos **is now live. Watch on X or YouTube, or listen on Spotify or Apple Podcasts.*

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

Last night I shipped a new feature for __Cora__, Every’s AI-enabled email assistant. Cora is not a __vibe-coded__ product: Its codebase is a 5,500-plus commit cathedral of Rails craftsmanship mostly from ** Kieran Klaassen**, Cora’s general manager, our resident

__DHH__. Needless to say, exactly zero previous commits are mine.

Undaunted (or somewhat daunted, but holding my shit together), I pressed “merge” on a pull request for a little quality-of-life UI update, and what had previously been just a twinkle in my eye appeared on production in less than an hour. How?

I used Codex—OpenAI’s new coding agent, launching publicly as a research preview today. Like __Devin__, Codex is designed as a software engineer that can build features and fix bugs autonomously. OpenAI has tried to incorporate the taste of a senior software engineer into how Codex writes code: It’s familiar with how large codebases work, and writes clean code and commit messages. It’s designed for you to run many sessions in parallel, so you can manage a team of agents without touching a single line of code.

In OpenAI’s storied tradition, Codex is confusingly named. The company has previously used the same name for both a model and a command-line tool. (Here’s an __o3 summary__ of the full history of OpenAI’s use of this name.) It’s a little rough around the edges and balkanized into a product separate from ChatGPT (more on this later). Even so, it’s useful.

We’ve been testing it for the last few days at Every. What follows is our day-zero vibe check. I invited Kieran to help me write this review because Codex, unlike many other AI coding agents, is clearly built for senior engineers like himself, and I think his perspective is important.

I also had a chance to speak to the member of the OpenAI team responsible for Codex, **Alexander Embiricos**. You can check out our full conversation here:

Let's go through what it is, how it works, what to use it for, and what it means. But first: the Reach Test.

**Public is making your ideas an investable reality with AI**

Multi-asset investing platform Public has just launched **Generated Assets**, enabling you to turn your ideas into investable assets with AI. Just enter your prompt into the chat-based interface in as much or as little detail as you like. In seconds, the AI builds a Generated Asset tailored to your vision. You can analyze its past performance, compare it to the S&P 500, and fine-tune the holdings to your liking. Then, share your Generated Asset with the world—and see how it stacks up against the rest.

**The Reach Test: Do we use it every day?**

The best leading indicator for long-term usefulness of an AI product is what I’m calling the Reach Test: Do I find myself automatically turning to this tool to do certain tasks? Or do I just leave it on the shelf and forget it’s there?

Here are the results of our Reach Test on Codex:

-
**Kieran (agent-pilled tech lead archetype):**Yes, he’s thinking about how to use it all day and night. -
**Dan (technical tinkerer CEO, weekend vibe coder archetype):**No, but because I’m normally coding on net new ideas rather than existing products.

**Overall:** It’s a tool you’ll reach for if you’re a tech lead adding features or fixing bugs on an existing codebase. If you’re trying to vibe code a new __one-person billion-dollar SaaS company__, look elsewhere.

**A Codex tour**

Codex presents you with a simple text box that asks you to describe the programming task you want it to perform, followed by two buttons: “Ask” and “Code”:

This is a telling user interface. It’s not a chat box, like ChatGPT, where you can casually go back and forth. Instead, it’s a text box for you to type in your well-specified coding task for it to complete.

When you press “Code,” this screen doesn’t disappear. Most other agent products open up a new window for you to watch the agent do its work. Instead, Codex slides your piping-hot new job into its task queue and blinks status updates as it gets going.

If you click into the task as it’s running, you can see a detailed log of what it’s thinking as it’s working:

For each new task, it spins up your codebase in its own sandboxed environment in which it can run tests and linters—aka spell check for programmers—so it can catch errors itself. Unlike Devin, it *does not* yet have access to a browser where it can use the code it’s written to see if it does what it’s supposed to do.

When it’s finished, it’ll give you a concise summary of what it did along with a code diff so you can see exactly what changes it made. It also has a button for you to easily submit its changes as a pull request on Github:

**What makes Codex different**

Codex is OpenAI’s attempt to turn __o3__ into a senior software engineer. The company used reinforcement learning to fine-tune Codex on the kinds of skills that professional software engineers have: how to write good pull request titles and descriptions, work with large messy codebases, how and when to run tests, and more.

The training team showed Codex large codebases—both clean and messy—so it would feel like it had more real-world experience and, crucially, a better sense of taste than other coding models. It shows: Codex produces terse, minimal code with concise, focused summaries.

Another thing that makes Codex different is its user interface. When you press “Code” on a new task, it doesn’t take you into the task execution screen so you can watch what it’s doing. Instead, you stay on the same screen on which you initiated the task to encourage you to start many tasks simultaneously without caring about the details of their execution.

Codex encourages a particular style of coding agent use: It emphasizes the creation of small, self-contained tasks that turn into small, easy-to-review pull requests. This makes it a good fit for use by professional software engineers working on production deployments because it makes it easier to track and understand what’s going into your codebase.

Codex is built to turn you from __programmer to manager__. It felt like the next evolution of what I experienced when __I first reviewed Devin__—like playing online poker in college, where you can be running 3-4 tables simultaneously.

And, somewhat surprisingly, it’s pretty good. It confidently __one-shotted__ a styling fix for one of our internal apps, called Paradigm. It also one-shotted the new feature for Cora I mentioned earlier. There is a piece of the UI that you can expand and collapse. I asked it to figure out how to save that state between user sessions. and it did it quickly and well.

Codex isn’t a vibe coding tool. You can tell it’s built not to replace senior software engineers, but as a tool for them.

**What doesn’t work well**

Codex is not a chat product. It sits in a separate interface from ChatGPT, and it is clearly built around a specific workflow: Give it a coding task, get a finished outcome. That’s why it’s good at what it’s designed for, but it’s a trade-off with flexibility.

For example, Codex is currently not very good at follow-up requests. If you ask it to build a feature and realize afterward that you want to add to or modify what it’s built, it’s a gamble whether your follow-up will work.

As a result, it’s a little unfriendly for less senior engineers and is much better optimized for small, self-contained tasks. If you know how the whole system works in your head and exactly what you want to build—like a senior engineer does—you can type your request into the task box and move on with your day. If, like me, you prefer to chat back and forth for a while to figure out what you want to build and how it should be done, Codex is not going to work very well. Instead, you need to refine your task in ChatGPT and flip to Codex when you’re ready to build.

It also doesn’t yet have full integrations with most of the surfaces where engineering happens, like Github and Slack. While it can post a pull request to Github, it can’t respond to a comment on the pull request telling it what to change. This will happen in time, but it adds friction for now.

**Codex: The next step in autonomous programming**

Codex is an exciting new release for OpenAI, but it’ll take a while for us to know if it’s exactly the right product to manifest the future of programming.

On the one hand, OpenAI has made a programming tool for senior engineers and succeeded at it. A senior developer gets a nice productivity boost by being able to fire off multiple well-constructed tasks simultaneously.

It also changes what it’s like to code: I spent about an hour pair-coding with Kieran last night, and we chatted while firing off tasks to Codex and testing them as they came back. It was a more social model for programming, because when you’re coding with Codex you can do it with divided attention.

But something about Codex also reminds me of __Operator__, OpenAI’s computer use agent. It’s split out into its own tool, so I have to remember to use it. And because it’s more specialized, it’s inherently less flexible.

I haven’t seen any major update to Operator since it was launched five months ago. I wonder, given OpenAI’s __reported acquisition__ of AI coding agent Windsurf, whether the same thing will happen to Codex.

It seems like OpenAI is attacking programming from two angles. Once Windsurf is fully integrated into its ecosystem, it will provide a tight, collaborative programming experience between programmers and AI. Codex, on the other hand, is built for autonomous delegation.

Ultimately, you’ll want to be able to switch back and forth between them for different tasks in different parts of your day.

*Dan Shipper** is the cofounder and CEO of Every, where he writes the Chain of Thought column and hosts the podcast*

__AI & I__.

*You can follow him on X at*__LinkedIn__, and Every on X at__LinkedIn__.

__@danshipper__and on__@every__and on*We build AI tools for readers like you. Automate repeat writing with *


__Spiral__*. Organize files automatically with*


__Sparkle__*. Write something great with*


__Lex__*. Deliver yourself from email with*


__Cora__*.*

*We also do AI training, adoption, and innovation for companies. Work with us to bring AI into your organization.*

*Get paid for sharing Every with your friends. Join our referral program.*

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
