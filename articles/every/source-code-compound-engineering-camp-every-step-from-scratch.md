---
title: "Compound Engineering Camp: Every Step, From Scratch"
author: "Katie Parrott"
date: 2026-03-13
url: https://every.to/source-code/compound-engineering-camp-every-step-from-scratch
words: 911
---

# Compound Engineering Camp: Every Step, From Scratch

Kieran Klaassen turned a prompt into a working app in an hour and shows you how

March 13, 2026 Updated May 11, 2026

*TL;DR: *__Cora__* general manager *__Kieran Klaassen__* has written prolifically about compound engineering, his philosophy of software engineering for the AI age. In this piece, based on a camp he gave for paid subscribers a few weeks ago, we get an inside look at how exactly Kieran builds with the compound engineering plugin for the first time. He walks through, step by step, the process of going from a single prompt to a working app in under an hour. If you’ve been curious about how to build with compound engineering, this is the piece to read.—Kate Lee*

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

This time last year, any time **Kieran Klaassen** opened a new session in Claude Code, he started from scratch. The lessons from his past code reviews, the style preferences he’d painstakingly explained, and the bugs he’d already flagged—Kieran remembered them all, but from the machine’s perspective, it was like it had never happened.

He’d been building ** Cora**, Every’s AI email assistant, and getting tired of copy-pasting the same prompts, correcting the same overengineered tests, and flagging the same bugs. “A human would remember,” Kieran said. “The AI wouldn’t.”

So he decided to create a system that *would *remember—one that plans before it codes, reviews outputs to enforce his taste, and stores every lesson so the AI applies it next time. The result is what we now know as __compound engineering__, a signature approach to coding with AI where every bug, fix, and code review makes the system permanently smarter. The official __compound engineering plugin__ has more than 10,000 GitHub stars and is used by a growing community of builders, including engineers at Google and Amazon, who say it changed how they think about software.

At our first __Compound Engineering Camp__, Kieran walked subscribers through the full loop live, building an app from a one-line prompt to a working product in under an hour. Below is the workflow as Kieran demo-ed it, plus what it means for how software gets built from here.

**Key takeaways**

-
**Brainstorm before you plan.**The plugin has a brainstorm step that interviews you collaboratively and fills the gap between your vague idea and a detailed spec. -
**Planning should run without you.**Once the requirements of the project are clear, the plugin has a plan step that researches your codebase, checks for existing patterns, surfaces past learnings, and produces an implementation plan with zero additional input needed. -
**Use different models for different steps.**Kieran uses faster models—such as__Claude Haiku 4.5__or__Gemini 2.5 Flash__—for brainstorming,__Opus__for planning,__Codex__for implementation, and sometimes Gemini for code review. -
**Compound when the context is fresh.**The plugin’s compounding step stores lessons as artifacts that future agents can discover, the core of compound engineering. Run it right after something breaks or works—before the AI compacts your conversation and you lose the specifics of what you were talking about.

**The compound engineering loop**

A founder who does everything themselves hits a ceiling, Kieran says. The ones who scale are the ones who build systems—hiring, documenting, and training—so the work happens without them in the room.

Compound engineering applies that logic to coding with AI. “You remove yourself from as many places as you can,” Kieran said. “That forces you to extract things, automate things. And that’s where the compounding happens.”

The core idea is a four-step loop: Plan, work, review, compound. Each step has a specific input and a specific output. The output of one step becomes the input of the next.

**Plan** takes a problem and produces a detailed implementation plan—a markdown file (a simple text document with formatting) containing data models, file references, architectural decisions, and sources. The plan is specific enough that an AI agent or a human engineer could pick it up and execute it without asking questions.

**Work** takes that plan and produces a pull request (a proposed set of code changes ready for review). The code gets written, tests get generated, and documentation gets updated.

**Review** takes the pull request and produces findings—comments, suggestions, and flagged issues stored as to-do items in the file system. Different AI models can review the same code and surface different problems.

**Compound** captures whatever the system learned during planning, working, or reviewing—a new coding preference, a bug pattern to avoid, or an architectural decision worth preserving—and stores it in files that future sessions can reference. This is what makes the loop self-improving.

There’s also an optional upstream step—**brainstorming**—for when you have a vague idea rather than a clear requirement. “Brainstorming is when the idea isn’t super detailed yet,” Kieran said. “If you have a very clear requirement—like adding a new authentication provider—you skip brainstorming and go straight to planning. Planning is about the details and not making mistakes.”

**From a blank prompt to a working app**

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
