---
title: "The Tool That Lets You Switch Models Without Losing Your Place"
author: "Katie Parrott"
date: 2025-11-04
url: https://every.to/source-code/the-tool-that-lets-you-switch-models-without-losing-your-place
words: 1188
---

# The Tool That Lets You Switch Models Without Losing Your Place

Everything we learned at Droid Camp about switching between GPT and Claude while staying in flow

November 4, 2025 Updated May 25, 2026

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

**Kieran Klaassen** is not an easy man to convert. As general manager of Every’s AI email assistant ** Cora**, Kieran has become a steadfast Claude Code devotee—including building an entirely new

__engineering system__around the tool. So no one at Every was surprised when he first tried Droid,

**the agentic coding product from Factory, and proclaimed himself “unimpressed.”**

But he kept trying because he discovered Droid had subagents—specialized AI workers configured for specific tasks. He could replicate the engineering process he designed in Claude Code in Droid without learning a different system. Once he realized Droid could do that—and that it would let him pick which model to use for which task—he used it to ship a feature in Every’s AI writing partner ** Spiral** (an app he’d never worked on before) in less than two hours.

That’s what Droid offers: an AI agent that lets you switch between GPT and Claude mid-task, picking the best model for each phase of work. Unlike Claude Code (Anthropic only) or __Codex__’s command line interface (OpenAI only), Droid works with multiple models from different providers. __GPT-5__ and __Claude Sonnet 4.5__ each have distinct strengths. Until now, in order to switch between those models, you had to switch tools.

If there was one person who wasn’t surprised by Kieran’s conversion, it was **Danny Aziz**, general manager of Spiral and Droid’s biggest evangelist at Every. Danny __canceled both his Claude and ChatGPT Max plans for Droid__, became Factory’s top early-access user, and built nearly all of the newest version of Spiral using its multi-model workflows.

If Danny and Kieran represent the developer side of Droid, Factory’s head of developer relations **Ben Tossell **represents proof that you don’t need to code to get value from AI agents like Droid. He can’t write a single line of code, but uses Droid as his default interface for everything from analyzing monthly financials to downloading YouTube transcripts. Where Danny and Kieran use Droid to build features faster, Ben uses it to automate tasks he’d otherwise do manually.

Danny, Kieran, and Ben joined Every CEO **Dan Shipper** last week in Every’s __Droid Camp__ to share how they use Droid in production, answer subscriber questions, and demonstrate workflows you can start using today. The event was for paid subscribers, but there was so much useful discussion and knowledge sharing that we’re posting the key takeaways for anyone who missed it. You’ll learn how to orchestrate multiple AI models in production—plus see real examples of developers and non-coders doing exactly that.

**Key takeaways**

Here’s what makes Droid worth your attention:

-
**Switch models mid-task to match the work.**Use GPT for long research and planning, then switch to Claude for implementation—all in the same terminal session. -
**Start with one model, scale up.**Ben runs most tasks in a single conversation thread. Danny orchestrates multiple models across separate terminal panes. -
**It’s great at non-technical use cases.**Droid handles data analysis, file management, and automation tasks just as well as code. -
**Context moves between models.**When you switch from GPT to Claude, Droid compresses your conversation history and carries it forward so the new model understands what you’ve been working on.

**What makes Droid different?**

Droid is a command line AI agent—software that can read files, write code, run commands, and complete tasks on your behalf. You might also hear it referred to as a harness: the software layer that packages an AI model into a usable tool. The harness determines how the model interacts with your code, what tools it can access, and how it presents information back to you. A good harness can make the same model perform better by giving it better context and more effective tools to work with.

Unlike most similar products, which are made by the companies that build the AI models (like Anthropic’s Claude Code or OpenAI’s Codex CLI), Droid works with multiple models from different providers and lets you switch between them with a single command. When he was building Spiral’s latest version, Danny got into the habit of running most of his workflow across multiple terminal panes that play to models’ different strengths: GPT-4 handles research and planning, __Claude Haiku__ implements the bulk of the code, and Claude Sonnet refines the details. Danny never has to leave his terminal or copy files between tools—he simply picks the best model for each phase of work.

Droid consistently ranks near the top of __SWE-bench__, a benchmark that measures how well AI agents solve software engineering tasks. According to Ben, the Factory engineering team attributes this to several design choices: reliable error handling that doesn’t fill your context window with repeated failures, built-in system reminders that keep models on track, the ability to pair smaller models for planning with larger ones for execution, and files where you can save notes that Droid will read to keep track of your preferences (a feature Claude Code also has).

Dan, Every’s CEO, captured the general experience: Droid consistently produces better results than you’d expect from using the same models elsewhere, even if the reasons why aren’t fully clear yet.

**Workflows from the Every team**

Here’s how our engineers use Droid in production, with specific examples from the session.

**Ben Tossell: Non-technical automation**

Ben runs Droid the way most people use ChatGPT, but with access to his file system. His terminal typically has six tabs running simultaneously: one analyzing Factory’s monthly finances, another helping him write documentation, a third working through tutorial scripts, and a fourth teaching him technical concepts he doesn’t understand yet.

When he notices himself doing something manually that could be automated, he asks Droid to handle it, then saves the commands it used as a reusable workflow. Take downloading YouTube videos, for example. In ChatGPT, extracting a transcript requires multiple copy-paste steps. In Droid, he typed one instruction: “download the *My First Million* episode about Grindr, extract the transcript, save it to a folder.” Droid found the right command line tools, ran them in sequence, and confirmed completion.

Afterward, Ben reviews the commands Droid executed in order to understand the sequence, and converts the pattern into a sub-agent or slash command (a reusable shortcut) he can trigger with a single word next time.

**Danny Aziz: Multi-model orchestration**

Danny showed the most sophisticated setup of the session. He had multiple terminal panes open, each running a different model on the same codebase:

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
