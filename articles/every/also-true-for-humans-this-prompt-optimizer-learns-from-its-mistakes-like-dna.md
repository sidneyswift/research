---
title: "This Prompt Optimizer Learns From Its Mistakes Like DNA"
author: "Mike Taylor"
date: 2025-12-05
url: https://every.to/also-true-for-humans/this-prompt-optimizer-learns-from-its-mistakes-like-dna
words: 634
---

# This Prompt Optimizer Learns From Its Mistakes Like DNA

A new tool that 'evolves' your prompts may be the next step in getting LLMs to do precisely what you want

December 5, 2025 Updated February 14, 2026

*Many of you wanted to learn more after the overwhelming response to Every columnist *__MikeTaylor__*‘s piece on prompt optimization framework DSPy. In this essay he goes deeper, breaking down GEPA, the specific optimizer inside DSPy that treats prompt engineering like natural selection—testing and evolving your prompts automatically. Even if you’re not technical enough to run GEPA yourself, his argument holds broader lessons for how anyone can work better with LLMs and what the future of prompt engineering holds.*

*Plus: We’re giving away 10 Monokeys—our limited-edition physical button for dictation—to the top 10 referrers on our leaderboard by December 7. Share your *


*Monologue**referral link with people who’d benefit, and every sign-up moves you up the leaderboard.—*

__Kate Lee__*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

Tech leaders at __Shopify__, __Databricks__, and __Dropbox__ have all become smitten with an obscure tool for enhancing how you prompt language models. It’s called GEPA, and it’s part of DSPy, the prompt optimization that is already so good it __could replace me and my job as a prompt engineer__.

GEPA works by iterating on your prompt in a way that resembles one of biology’s most powerful forces: genetic mutation and natural selection. It does this by creating multiple copies of your prompt, making changes to them (“mutating” them) and keeping track of the best ones. (GEPA is short for “Genetic Pareto,” in which the best-performing prompts define something called a __pareto frontier__.)

The __original paper on GEPA__, published on the open-access archive Arxiv in July, promised 25 percent better performance than other methods of optimizing prompts on a range of tasks. That may not sound like a huge improvement, but it did it fully automatically with 35 times fewer trials—so it’s smarter about what it tries. As a result, it’s cost-effective to run on any task that’s worth spending a few hundred bucks to improve—like the prompts that power Every’s AI writing assistant **Spiral**’s creative writing, which got a 44 percent quality improvement through GEPA optimization.

I keep getting questions about how GEPA works and whether people should be using it. Though there is a technical barrier, it’s coming down as no code tools like __LangWatch__ and __Opik__ integrate it into their products, as well as a number of others build __user interfaces__ for it. Even OpenAI is getting in on the __prompt optimization game__, with an interface for optimizing your prompts. I’m going to break my explanation down in accessible terms. I’ll also walk you through a case where GEPA doubled the accuracy of my prompt in 20 minutes, so you can see how GEPA can help you optimize daily workflows and, more broadly, how AI can help us use it better.

**Become a paid subscriber to Every to unlock this piece and learn about:**

- How a prompt Mike created went from giving the correct outputs 26 percent of the time to 71 percent of the time in half an hour—without him rewriting a word
- The hidden patterns in invoice data that GEPA spotted but its human operator missed
- Why the future of prompt engineering won’t involve writing prompts at all

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
