---
title: "The Culture of AI Engineering"
author: "Noah Brier"
date: 2026-05-08
url: https://every.to/thesis/the-culture-of-ai-engineering
words: 1258
---

*Noah Brier** cofounded Percolate in 2011 and learned the CEO’s hardest job: keeping a whole company pointed in the same direction. Now, at his AI consultancy* __Alephic__—and in his own work, where he uses Claude Code as a__second brain__—he’s facing that same problem with agents in the mix. AI was supposed to make coordination easier. Instead, Noah argues, it has created new coordination problems of its own. In this piece, he pushes back on the “software factory” metaphor and offers a framework, drawn from *Stewart Brand**’s pace layers, for getting carbon and silicon to build the same thing.— Kate Lee*

Strong DM is a software company whose three-person AI team calls their system for autonomous code generation a __“Software Factory.”__ Entrepreneur **Dan Shapiro’**s __widely circulated framework for AI coding__ culminates in “the Dark Factory,” named after a Japanese robotics plant that __runs with the lights off__. __Factory.ai__, which has raised millions from Sequoia and Khosla Ventures, has built an entire business around the metaphor—its autonomous coding agents are called Droids.

I’ve been incorporating many of StrongDM’s concepts about agentic software development into our work at __Alephic__, the consulting company I co-founded—but I have one fundamental disagreement: I think factory is the wrong metaphor.

If the hardest problem is making something people want, then the process of building software looks a lot more like **Andy Warhol**’s factory than **Henry Ford**’s. Both are focused on throughput, but Ford’s is focused on mechanization and stamping out identical cars with as little variance as possible. Warhol, on the other hand, was concerned with ensuring all work aligned with a single creative vision.

Ford’s factory—or more specifically, the assembly lines inside it—was designed to eliminate imperfections. __Six Sigma__, the quality methodology made famous by General Electric and beloved of manufacturers, is literally a measure of the defect rate. Quality starts with deciding what to build. This is why __product-market fit__ is the lingua franca of startups: If you haven’t built something the market needs, nothing else—including the quality of your code—matters.

Too much of the industry treats software as a problem to be optimized and solved. That may be true for code writing and testing, but the better metaphor is staring us in the face: It’s a software *company*, not a software *factory*.

Just as in the days before AI, the hardest problem for a business is still creating this vision and alignment around it—how to keep an entire team of humans, and now humans and agents (and humans with agents), building toward the same vision, from the system architecture down to the individual lines of code. As I’ve learned long before agents existed, achieving this is much more akin to building a startup than assembling a car. What follows is my attempt at a framework for keeping an entire system of humans and agents building the same thing.

## The alignment problem isn’t new—and AI didn’t solve it

I ran into this alignment problem years ago, when I cofounded the company Percolate, a content marketing platform, in 2011. As we grew the business from zero to 100 people in less than three years, my job as CEO shifted from building the product to building a company capable of building the product. My agents were people, and my job was to design the system they worked within. Culture, I concluded, was one of the strongest levers I had.

As __Ben Horowitz____ put it__, culture is “how your company makes decisions when you’re not there.” This was exactly what I needed: documents, tools, and rituals that helped each individual make the best possible decision without having to run every decision up the chain. I probably spent half my time on this, building a living culture document, running onboarding sessions for every new hire, and developing internal tools that automatically routed knowledge to the right people.

Every new technology promises to solve these coordination problems. But of course, nothing is that simple. What they do in reality is reshape the landscape around them and, in the process, create new problems that didn’t exist before. AI is no different.

Open-source software offers an early glimpse of the kind of unexpected problems that AI can create: Whereas the primary challenge a few years ago was finding maintainers willing to contribute code on goodwill alone, today’s challenge is sifting through hundreds of crappy __AI-generated pull requests flooding GitHub__.

Now, 15 years later, my audience at __Alephic__ is not just the humans who work with me. Those humans are often paired with agents, and, increasingly, the agents themselves are delivering work independently. Yet the core problem is identical.

If you’ve used a coding agent for more than a week, you’ve already experienced this: The code works, but it often feels written by someone most definitely not you—ignoring obvious abstractions and stylistic norms that are present in the codebase. It looks, in other words, like a new engineer on the team who hasn’t been properly onboarded. We write onboarding documents and do training for our human colleagues, but most people don’t do this for agents. Yet.

## Pace layers of AI engineering

I still have an onboarding document and set of activities every new hire goes through during their first week, including building a module in our homegrown learning system as their first coding task (a few recent editions were GPUs, __quantization__, and __agentic commerce protocols__).

But I am also building tools that go further and ensuring our code is maintainable, consistent, and built the way we’d want it built.

I think about our tooling as a kind of cultural stack, where standards inform architectures, which in turn inform specs, plans, and code. The layers are inspired by counterculture systems thinker __Stewart Brand____’s pace layers framework__. It’s a model for how society changes at different speeds, from nature, which shifts over millennia, to fashion, which can change by the day. The lower layers move slowly; the upper ones move fast.

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

Great article. Awesome thoughts. Thanks Noah.

I love the concept of pace layers, Noah. Esp if you think about it 3 dimensionally as a solar system and the gravitational force of the foundational standards are keeping everything held together rather than flying off into outer space. :) Great thoughts here.

I have many MD files with various documented requirements (like what to not do, preferences, writing style guide, brand guide, priorities, etc.) ~ But they’ve even become a headache to maintain. I recently spent a good deal of time cleaning up all the various MD files but worry it’s just a matter of time before I must do it again.. And then there’s the challenge of having to constantly remind my agent of these standards, due to memory drift and the abundance of documentation. My main memory/agents file has this all stated and routed, but it’s still not great yet. I even have a script I copy/paste to recalibrate, and I use it more frequently than I like. Any advice on how to reliably have agents refer to these “pace layer” standards so it’s committed to memory? Excellent article ~ thank you!
