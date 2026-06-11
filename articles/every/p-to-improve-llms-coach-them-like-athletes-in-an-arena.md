---
title: "To Improve LLMs, Coach Them Like Athletes in an Arena"
author: "Alex Duffy"
date: 2025-08-15
url: https://every.to/p/to-improve-llms-coach-them-like-athletes-in-an-arena
words: 697
---

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

This week I and several colleagues __published our findings__ about how, with a little elbow grease and creativity, anyone can dramatically increase performance of any LLM.

The secret is in coaching. Allow me to explain.

The reason an athlete can credibly claim to be “best in the world” is because arenas and structured competition—games—exist. There are rules, clocks, standings, and tape you can study. The AI world has benchmarks—but benchmarks only check facts. Games reveal a model’s behavior, which can be recorded and studied to help models get better. That is what we did with AI Diplomacy, a project in which we turned the classic strategy game Diplomacy into a competitive arena for language models.

AI Diplomacy works because it has clear goals—try to outfox your opponents and take over Europe—and room to improvise. But subtlety and guile are key parts of the game, which centers on tactical negotiations (check out our complete list of rules). When we first set up the game environment, the LLMs were lost. After we got past a bunch of thorny technical problems, we realized that we could learn a ton about the models’ strengths and weaknesses from how they play against each other—and that we could coach them to be better. For example, prompting models to act more aggressively turned __GPT-5__ from a patsy into a formidable contender. __Claude Sonnet 4__, meanwhile, was a strong, speedy player even without specialized prompting.

These are useful differences. One model is highly steerable, the other is fast and consistent. That improvement tells you how the model will respond to a real-world task. If you have more time to craft a great prompt and need the best result, GPT-5 would be great. In a rush? Try Claude 4.

The industry is starting to realize that games can help evaluate models and push them to new levels of performance. Google has launched Google Arena, for instance, because the company __says__ games are “[the] perfect testbed for evaluating models & agents.”

We agree. In fact, we think there’s so much potential here that we’re putting up $1,000 in prize money to see who can prompt their agent to victory in AI Diplomacy in our __Battle of the Bots__ in September.

In the meantime, let’s break down our findings so far.

## What AI Diplomacy taught us about models

Diplomacy is one of the hardest games language models can play today. Our coaching setup took a long time to optimize, but now even small models can finish full games. The key is to provide all the information needed, and nothing more—easier said than done. For us that was a text version of the board that conveys what matters to the LLMs: who controls which locations on the map, where each unit is allowed to move, nearby threats, and the current phase of the game. We set simple rules for how models negotiate and submit orders, but left room for creativity.

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

Love this whole project so much! So much learning there and you share it so well. I just checked and the diplomacy repo (thankfully OS) has been forked 64x. Did you see/hear anything interesting that people did with those forks?

For c4-1m vs. c4-1m-agressive it seems like the top score and average looks better for aggressive but the variance is huge compared to the non-agressive. Now, if you join the AI Diplomacy tournament, and without giving too much away, which of the models with prompts as shown in this article would you bet on? Say the prize money is $1M? Why would you select that model and that prompt from the data set of this article?
