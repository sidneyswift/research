---
title: "🎧 This AI Makes a Video Game World in 40 Milliseconds"
author: "Rhea Purohit"
date: 2025-09-03
url: https://every.to/podcast/this-ai-makes-a-video-game-world-in-40-milliseconds
words: 1741
---

# This AI Makes a Video Game World in 40 Milliseconds

Decart cofounder Dean Leitersdorf built a model that edits live video as it streams—here’s what he learned building it

September 3, 2025 Updated May 2, 2026

*TL;DR: Today we’re releasing a new episode of our podcast *__AI & I__*. **Dan Shipper** sits down with **Dean Leitersdorf, **cofounder and CEO of Decart, the creator of the only real-time video-to-video model in the world. **Watch on X or YouTube, or listen on Spotify or Apple Podcasts. **Here’s a link to the **episode transcript**.*

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

At first glance ** Dean Leitersdorf** looks like every other startup founder on a Zoom call: wavy hair, spectacles, a plain black t-shirt.

Then mid-sentence he’s transformed into a wizard conjuring light from his hands. A few seconds later, he’s a Lego figurine, spectacles now molded in yellow plastic. Each avatar looks just like him, mirroring his expressions and movements in real time, from adjusting his glasses to the exact sync of his lips as he speaks.

This shape-shifting—which Leitersdorf showed off in the video recording of this week’s *AI & I* with **Dan Shipper**—was made possible by __Mirage__, the only real-time video-to-video model in the world. Mirage can take a live video feed (like Leitersdorf speaking on Zoom) and instantly re-render every frame in a new style, without breaking flow. It’s editing reality as it happens.

Leitersdorf is the co-founder and CEO of __Decart__, a startup that makes Mirage. Decart recently __raised__ $100 million at a $3.1 billion valuation as part of its push to usher in a new era of real-time generative experiences like this.

Mirage has obvious potential for how we play and design video games: Imagine creating endless variations on existing titles, like a *Barbie*-skinned *Minecraft*, or a brand-new game, taking a bare-bones vibe-coded prototype and instantly layering it with immersive textures and themes. But Leitersdorf also sees the beginnings of a new medium, a new experience created by AI.

Dan and Leitersdorf take a look at how Mirage works under the hood, and what the Decart team learned about the future of software while wrestling with its toughest research problems. They also debate __AGI__—how close it really is, what counts as progress, and what kind of society it might create.

You can check out their full conversation here:

If you want a quick summary, here are some of the themes they touch on:

## The skeleton and muscle of modern software

Leitersdorf sees a fundamental divide in what traditional software and AI each do best. Classical code is best at handling problems that are discrete, exact, and brittle, where getting something almost right is the same as getting it totally wrong.

AI, on the other hand, is good at problems where approximate solutions are acceptable, and sometimes even preferred. Leitersdorf takes drawing an image of Dan as an example. “It’s fine if I'm missing a few things,” he says. “If your shirt's a bit off, if the wall behind you is slightly different, if your glasses are slightly bigger.”

This division suggests a hybrid future for software architecture, one that Mirage is built on. The traditional game engine handles the rigid logic, like remembering “you have exactly 71 gold coins in your pouch,” or that “you took this pickaxe and put it in that chest.” AI takes care of the flexible, creative parts, like giving *Grand Theft Auto V* a convincingly frigid winter filter.

Dan likens this to our own bodies, with traditional software like a skeleton that gives us structure and the ability to “stand up.” AI, meanwhile, is like muscles and tendons that add flexibility and movement. For the longest time, we could only build software that resembled “bones,” and AI has now enabled systems to bend and respond in fluid ways.

## The breakthroughs that make Mirage work

#### Videos come alive with speed

To make real-time video possible, Mirage had to process video fast, blazingly so. The way to do this, Leitersdorf explains, is “writ[ing] lots of very optimized GPU code.” Most developers who work with NVIDIA GPUs use something called __CUDA__, a programming toolkit that makes it easier to tell the GPU what to do. But the Decart team went a level deeper. Instead of going through CUDA, they wrote code directly in __PTX__, the GPU’s assembly language. That’s the computer’s native tongue: harder for humans to write, but much faster for the hardware to understand. This decision let them squeeze every ounce of performance out of the hardware. It’s how Mirage can process video with only a 40-millisecond delay today—with plans to shrink that to just 16 milliseconds.

#### How Mirage thinks like an LLM

The second problem Decart had to tackle was creating a new kind of model altogether. When you use AI video tools like Google Veo, for example, you prompt them, and they process it and generate a short video. Mirage generates videos frame by frame, almost like an __LLM predicting the next word in a sentence__. To do that, it looks at two things at the same time: the live video it’s supposed to transform (say, a Zoom feed of Leitersdorf), and the video it has already generated up to that point (the running output). “You feed it in two video streams…and it needs to predict the next frame,” Leitersdorf says.

#### The error accumulation problem

Beyond speed and model architecture, the real test for the Decart team was stability. As Leitersdorf explains, early versions of Mirage were like GPT-2 or GPT-3.5: impressive for the first few back-and-forths, but eventually getting caught in a loop where they would repeat the same thing over and over again.

“We could easily get Mirage to be great for two to three seconds but then it slowly started to degrade and it got stuck in this loop… in a single color and your entire screen just became red or blue or green,” he says. Solving this __"error accumulation"__ problem—called such because with every frame, tiny mistakes pile up, gradually pushing the model further away from the patterns it was trained to follow—took six months and thousands of experiments.

## What will a world with AGI look like?

Questions about that small, uncontroversial topic—AGI—sparks a friendly back-and-forth between Dan and Leitersdorf. Leitersdorf argues that economic AGI—when machines “are able to do any economic job better than all of us, or better than the vast majority of humanity”—is just 12 to 18 months away. When asked what a world like that might look like, he draws an analogy to how democracy came to be in ancient Greece: As technology improved, it lightened the burden of farming, giving people time to think—and their minds turned toward philosophy and governance.

Skeptical of Leitersdorf's timeline, Dan pushes back. He agrees that AI can outperform humans in specific tasks if properly prompted, but stresses that “given the right prompt” is the crux of the problem. AI still can’t reliably direct itself. To him, a __better definition of AGI__ is “when it is economically profitable to leave your AI on all the time.” Getting there, he argues, will require AI systems capable of continuous learning—being able to update their own weights, adapt to new information, and refine themselves over time—rather than just relying on better prompting. Without that ability, AGI remains years away.

When pressed on this point, Leitersdorf reframes his position: “So I think that maybe a different way to phrase it is there's a chance in 12 to 18 months, AI lets us be so productive that we're able to create companies that are just way bigger than anything we saw so far.” He takes the example of the first trillion-dollar company ever, Apple, in 2017, to the 10 that exist today, predicting that AI could create so much value that the stock market might double.

Dan ties this back to Athens: Democracy flourished in Athens because it was a society of __generalists__, where citizens had to wear many hats—statesman, lawyer, prosecutor, juror, warrior—all at once. That balance broke down when Athens grew into an empire, the equivalent of a trillion-dollar corporation, where specialization became necessary to manage scale. Specialization enabled progress but diminished the generalist ethos, a pattern that has carried through Western society ever since. He argues that AI could change this: With “a thousand specialists in your pocket,” individuals and small teams can stay generalists for longer, blurring roles and doing more across domains.

What do you use AI for? Have you found any interesting or surprising use cases? We want to hear from you—and we might even interview you.

Here’s a link to the episode transcript.

You can check out the episode on X, Spotify, Apple Podcasts, or YouTube. Links are below:

- Watch on X
- Watch on YouTube
- Listen on Spotify (make sure to follow to help us rank!)
- Listen on Apple Podcasts

Miss an episode? Catch up on Dan’s recent conversations with founding executive editor of *Wired* ** Kevin Kelly**, star podcaster

**, LinkedIn cofounder**

__Dwarkesh Patel__**, ChatPRD founder**

__Reid Hoffman__**, economist**

__Claire Vo__**, writer and entrepreneur**

__Tyler Cowen__**, founder and newsletter operator**

__David Perell__**, and others, and learn how**

__Ben Tossell__*they*use AI to think, create, and relate.

If you’re enjoying the podcast, here are a few things I recommend:

-
__Subscribe__to Every -
Follow
__Dan__on X -
Subscribe to Every’s
__YouTube channel__

*Rhea Purohit** is a contributing writer for Every focused on research-driven storytelling in tech. You can follow her on X at @RheaPurohit1 and on LinkedIn, and Every on X at @every and on LinkedIn.*

*We build AI tools for readers like you. Write brilliantly with *


__Spiral__*. Organize files automatically with*


__Sparkle__*. Deliver yourself from email with*


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
