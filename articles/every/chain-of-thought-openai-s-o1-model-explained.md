---
title: "OpenAI’s o1 Model, Explained"
author: "Dan Shipper"
date: 2024-09-13
url: https://every.to/chain-of-thought/openai-s-o1-model-explained
words: 535
---

*Was this newsletter forwarded to you? **Sign up** to get it in your inbox.*

OpenAI launched a new model, o1 (previously code-named Strawberry), yesterday. It’s significantly better at reasoning tasks, scoring in the 89th percentile in competitive programming, and exceeding Ph.D.-level smarts on physics, biology, and chemistry questions.

It’s been taught to use chain of thought reasoning to answer each question it’s given rather than just blurting out a response.

Chain of thought, of course, has been around for a long time. It’s the practice of asking a language model to solve problems by thinking out loud. You’re probably better at doing long division if you write out the steps one by one than you are at doing it in your head. Language models are the same way: Chain of thought creates a tunnel of reason that keeps the AI on track.

Chain of thought used to be just a prompting technique that would improve outputs in the original GPT models.

o1 is different because it’s been trained via reinforcement learning to *always* use chain of thought in its responses without any extra prompting required. Now, when you ask ChatGPT with o1 enabled a question, up pops an expandable thinking indicator that lets you see its thought process:

## A new paradigm in AI: Test-time compute

Well, I’m glad I named this column Chain of Thought because it turns out Chain of Thought is probably the next big paradigm in AI progress. (Better to be lucky and partial to polysemy than good, as the saying goes.)

As I mentioned in my article on Strawberry, the key ingredients for AI progress so far has been: more data and more compute during training.

The interesting update from Strawberry is that OpenAI has found a way to add a new dimension on which to improve performance: compute during inference. The company has found that when Strawberry takes longer to respond to a prompt—in other words, when it’s given more time to think—it generally responds more accurately.

This wasn’t *necessarily* the case with previous models. The longer GPT-4 was left to run in an autonomous loop, the more likely it was to go off the rails or get stuck in a meaningless rabbit hole. Because o1 has been trained to perform better on chain of thought reasoning, it seems to be able to better stay on track.

The success of o1 gives OpenAI a new way to approach performance improvements. Instead of doing a training run for GPT-7 that requires the entire energy output of the sun, it can do something with a shorter feedback loop: giving o1 more time to think before it responds to a prompt.

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

Thank you.

Appreciated the timeliness and the 1500 / 1700 /1900 thought experiment
