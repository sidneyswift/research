---
title: "Mini-Vibe Check: Cursor Bets on Fast and Cheap With Composer 2"
author: "Every Staff"
date: 2026-03-21
url: https://every.to/context-window/mini-vibe-check-cursor-bets-on-fast-and-cheap
words: 1641
---

# Mini-Vibe Check: Cursor Bets on Fast and Cheap With Composer 2

Plus: Help your AI write more like you

March 21, 2026 Updated April 17, 2026

*Hello, and happy Sunday! Was this newsletter forwarded to you? Sign up to get it in your inbox.*

## Cursor’s new model is competitive but not quite frontier

*The benchmarks say Composer 2 competes with the best. Our testers say it’s built for a different kind of developer.*

Over the past year, OpenAI and Anthropic have converged on the same vision of AI coding. __Claude Code__ and __Codex__ both optimize for delegation: You describe the problem, the model goes away and solves it, you come back and review.

__Cursor__, on the other hand, wants the developer in the loop, inside a visual workspace, managing agents in real time. And if you’re running lots of tight cycles instead of delegating a 30-minute task, you need a model that’s fast, cheap, and smart *enough*.

Composer 2, which Cursor __released on Wednesday__, aspires to that vision. It comes in two flavors: a standard variant that’s one-tenth the cost of __Opus 4.6__ and one-fifth the cost of __GPT-5.4__, and a default “fast” version that’s faster than the fastest Opus model (and still a fraction of the cost).

Cursor says its benchmark scores put Composer 2 at frontier level. In our testing, the benchmarks hold up—but only within Cursor’s ideal workflow.

**What we found**

Speed is the standout feature here. ** Kieran Klaassen**, general manager of

**, called Composer 2 “**

__Cora____Gemini__fast.”

**, Every’s head of tech consulting, found that even the “slower” version completed some tasks in a third or a quarter of the time he’d expect from frontier models.**

__Mike Taylor__For a coding workflow built around tight cycles, that speed compounds quickly. As Mike put it: “When you’re in the loop, you need the loop to go fast. When you’re out of the loop, who cares—it’s running in the background overnight anyway.”

The model is also cautious. It undershoots rather than spiraling into overwrought solutions—a trade-off Kieran prefers. And on retrieval-heavy tasks, it performed well. Mike found that it comprehensively identified quoted material across a book manuscript, missing only a handful of quotes.

Composer 2’s weaknesses were what you’d expect from a model at this price point. Kieran found the design quality “way worse than Codex, Claude, Gemini” in his benchmark tests. An e-commerce site built in React was functional but missing features. A 3D island scene had “nothing wrong with it” but was “boring.” When writing Ruby code, the model didn’t lean into the language’s idioms. Mike ran into Composer 2’s literal-mindedness on non-coding tasks: In one case, it looked for the words “surprising” and “interesting” instead of reasoning about what in the data was noteworthy. He also found himself wanting subagent functionality—where a model divides up complex tasks among background agents—on more-involved research work.

**Who this is for**

To Kieran, Composer 2 feels six-to-eight months behind the frontier. For developers who have gone all-in on delegation—handing entire features to Claude Code or Codex and walking away—that gap is disqualifying.

But Cursor isn’t building for those developers, or at least not *only* for them, but instead for the ones still inside the IDE—the “integrated development environment,” where they pore over code changes and steer any AI work in real time. Here, Composer 2 is fast enough to keep the loop tight and cheap enough to run all day, and capable enough to handle the bounded tasks that make up most of the work.—__Katie Parrott__

## Knowledge base

__“How to Build an AI Style Guide____”__ *by Katie Parrott*: When you give a model a loose prompt, you get writing that sounds like nobody—coherent but generic. Every staff writer and AI editorial lead **Katie Parrott** explains how to fix that with an AI style guide, a reusable document that encodes your tone, structure, sentence habits, and deal-breakers so the model starts sounding more like you. Read this for __the full template__, a starter interview prompt, and lessons from the guides Every uses daily.

__“____Editing AI Writing____”__ *by Every staff/Context Window*: AI-generated prose can be so flimsy that it’s sometimes easier to start over and write it yourself. No amount of editing fixes text that was never grounded in real thinking, Eleanor writes. That thought leads nicely into this week’s podcast, where Every editor in chief ** Kate Lee** tells Dan how she uses AI daily, and the moment when the potential of AI tools finally clicked for her. 🎧 🖥 Listen on

__Spotify__or

__Apple Podcasts__, or watch on

__X__or

__YouTube__.

__“____When Your Vibe Coded App Goes Viral—And Then Goes Down____”__ *by Dan Shipper/Chain of Thought*: Every CEO ** Dan Shipper** vibe coded our new document editor,

**, in his spare time. But when it kept crashing on launch day, he spent 24 sleepless hours watching Codex agents hunt bugs in a codebase he didn’t fully understand. Dan’s takeaway is that if the AI can build it, it can also fix it—but it might take a while. Read this for an honest post-mortem on vibe coding at production scale.**

__Proof____“____What Comes After LinkedIn____”__ *by Eleanor Warnock*: AI is automating the routine work that many white-collar professionals built careers on, and a resume full of big-name employers no longer proves you have the judgment and taste that matter. Every managing editor ** Eleanor Warnock** writes that knowledge workers need portfolios—collections of artifacts that show how they solve problems. Read this for the emerging portfolio formats and examples worth stealing.

__“____I Hired an AI to Do My Chores. Now I Maintain the AI.____”__ *by Jack Cheng*: Every senior editor ** Jack Cheng** wanted his AI agent to handle the stuff nobody wants to do, like disputing bank charges, changing leaked passwords, clearing desktop clutter, etc. Instead, the agent kept breaking—and fixing it became another burden. The irony sent Jack down a rabbit hole about why we’re so bad at maintaining things, and what we lose when we stop doing it ourselves. Read this before you automate away your to-do list.

## Log on

We host __camps and workshops__ on topics like __compound engineering__ and __writing with AI__ to share the knowledge we’ve acquired from training teams at companies like the __New York Times____ and leading hedge funds__, and by learning and playing with AI every day ourselves.

**Upcoming camps**

-
__Claude Code for Absolute Beginners__(April 14): Early bird registration is open for this beginner-friendly, live workshop led by__Mike Taylor__(head of tech consulting at Every), designed to get you from zero to a working project with Claude Code.

## Alignment

**The n-of-1 problem. **This week, a __heartfelt story__ went viral about an Australian data analyst named **Paul Conyngham** who used ChatGPT, AlphaFold, and Grok to help design a personalized mRNA cancer vaccine for his dying dog, Rosie.

Rosie had advanced mast cell tumors that had beaten surgery, chemotherapy, and immunotherapy. Vets had given her months to live. So Conyngham, who has no background in biology, __used AI to sequence__ her tumor DNA, identify the mutations driving the cancer, and design a vaccine blueprint targeting those specific mutations. He handed that information to scientists at the University of New South Wales, who created a vaccine that a veterinary immunologist then injected around the tumors. Within a few weeks, the largest tumor shrank by about 75 percent, and Rosie is now happily chasing rabbits again.

I love this story, and it went viral for obvious reasons: A man’s love for his dog meets a bold act of individual agency meets a glimpse into medicine’s AI-enabled future—this is Tech Twitter’s dream!

But what Conyngham built was a treatment designed for one dog’s specific tumors, tested on that one dog, validated by a sample size of one—also known as an “n-of-1” trial (a play on notation from clinical experiments, where the variable *n *represents the number of participants).

Conyngham’s n-of-Rosie trial may have worked, which is wonderful. But her cancer isn’t cured, and it’s not known how much the response came from the vaccine or other simultaneous treatments. The entire infrastructure of modern medicine, from randomized controlled trials to regulatory bodies, exists precisely because we learned the hard way that anecdotes aren’t evidence.

Yet we’re drifting into n-of-1 territory everywhere. Some people are __injecting peptides__ sourced from Chinese manufacturers and self-reporting benefits that could easily be placebo, while others are going to Mexico and Colombia for __untested gene therapies__ that they believe will prevent aging.

What happens to evidence-based medicine when personalized treatments become trivially easy to design but remain extremely difficult to validate? Ethics committees, which approve and oversee lab experiments on humans and other animals, took Conyngham months to navigate and are not built for a world where thousands of people are desperate to use their own AI-generated blueprints.

Many people will understandably look at Conyngham’s example and be emboldened to take a similar approach to their own health. I also suspect that, because of Rosie’s story, bioethicists are losing quite a bit of sleep.—__Ashwin Sharma__

*That’s all for this week! Be sure to follow Every on X at @every and on LinkedIn.*

*We build AI tools for readers like you. Write brilliantly with *


__Spiral__*. Organize files automatically with*


__Sparkle__*. Deliver yourself from email with*

__Cora__. Dictate effortlessly with

__Monologue__*. Work on documents with AI agents using*

__Proof__.*For sponsorship opportunities, reach out to [email protected].*

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
