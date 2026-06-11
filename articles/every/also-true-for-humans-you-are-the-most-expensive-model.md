---
title: "You Are the Most Expensive Model"
author: "Mike Taylor"
date: 2026-04-27
url: https://every.to/also-true-for-humans/you-are-the-most-expensive-model
words: 946
---

*Not every step in an AI workflow needs the smartest AI. That may sound obvious, but it’s not how most people are working. The default is to route entire tasks through frontier models, which is expensive, slow, and usually unnecessary. Incremental determinism starts from a different question: How much intelligence does this task really need?? The answer is almost always less than you’d expect, and the savings add up.— Mike Taylor*

There is a reason McDonald’s would never ask its CEO to man the burger grill: It would cost the company __$9,230.77 an hour__. It’s the same as using frontier __AI models__ to do every task—you don’t need to pay __75 cents every half hour__ ($1,095 per month!) for Claude Opus to check your to-do list in __OpenClaw__.

This tension isn’t really about the pricing of AI models—it’s about the value of human attention. Now that you have a cheaper alternative for many tasks that used to require it, you need to figure out the optimal way to deploy AI in a way that frees up your most expensive model—you. Most businesses are getting this balance wrong in both directions: overpaying for AI on simple tasks and underusing it on ones that would free up their best people.

The solution is a process of optimization that I call incremental determinism. Every time you repeat a task, build it into a repeatable process by creating a __skill file__. Identify which parts of that process need the most expensive model, which can be delegated to cheaper, less powerful models, and which tasks repeat often enough to justify turning them into reusable code. And finally, get better at delegating so you can stay focused on the work that needs you.

I call it incremental determinism because the more you repeat a task, the more it pays to nail down exactly how it should be done. The first time, you figure the task out as you go, but after doing it a few times, you can document the best approach. “Deterministic” is a programming term for code that always produces the same output given the same input. The goal is to push as much of your workflow towards that end of the spectrum as possible, because deterministic steps are faster, cheaper, and more reliable. The tradeoff is the upfront investment needed to systematize the task.

There are four levels for achieving this balance and optimizing AI costs. Depending on your technical fluency, you don’t have to go to the final step, but understanding how they each support each other will help you manage how you can control AI costs across your entire organization.

##
**Level 1: Turn sessions into skills**

The first level is the easiest. Let’s say you are often asking AI to generate a PowerPoint pitch deck. The first step toward systematizing it is to make a __skill__. A skill can be as simple as a text file detailing how to do a task that the model follows each time it’s asked. It’s the McDonald’s handbook that tells every employee how to make the perfect burger, over and over again. Even less experienced cooks can get a good result.

Once you’re done with the normal back and forth of giving the AI the necessary data and context for the presentation, ask it, “What information would have been useful to know at the start of this task that would have eliminated several steps or mistakes?” Claude knows what it is capable of, so you can ask it to turn its response into a PowerPoint deck creation skill to use next time. Anthropic has been __releasing plugins__ (collections of skills) for various industries to serve as a starting point. They even provide a __“skill-creator” skill__ that teaches Claude how to guide you through making one when you ask.

Once you have a skill, test it. Ask Claude to test the efficacy of the skill with the following prompt: “Run the task using subagents, one with the skill, one without, and compare the results.”* *If the skill is doing its job, you should see an improvement in quality, cost, and speed. Now try running it with a cheaper model—“Run this test again with __Sonnet__/__Haiku__”*—*and compare the results. If you’re happy with the output, ask Claude to “Use a __subagent__ with Sonnet/Haiku when calling this skill.” You are using a subagent because you don’t want the model that you are using for your main session—the more expensive one—to be the model executing the task, so the separate, cheaper subagent does the work. You just decreased the cost of running that task by 10 to 100 times.

It doesn’t make sense to write skills for throwaway tasks you won’t do again. But if you find yourself doing something for the third time, it’s probably worth formalizing it. If you’re using it multiple times per week, try getting it working with a smaller model.

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

Are subagents (which can specify which model to use for Skills) exclusive to Claude Code or can I specify model with Cowork skills?

@antonacci.michael.d I just tested and it looks like cowork can create subagents but can't load them (you could drop the file in a session and use it that way).
