---
title: "How AI Image Models Work"
author: "Nir Zicherman"
date: 2025-09-04
url: https://every.to/p/how-ai-image-models-work-49b41bc0-2365-4157-a6d7-3f8adaac787f
words: 734
---

# How AI Image Models Work

An entirely non-technical explanation of image generators

September 4, 2025 Updated December 17, 2025

*To follow up on our latest podcast episode with Decart cofounder **Dean Leitersdorf—**about AI video generation—we're re-publishing **Nir Zicherman**'s piece about how AI image models work. (Nir is also an upcoming guest on *AI & I.) *Plus: Paid Every subscribers are invited to **Every Demo Day** on Friday (tomorrow), September 5 at 12 p.m. ET. Sign up to attend, or upgrade your subscription to register.—Kate Lee*

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

I can vividly recall the day I got access to the DALL-E beta. It was the summer of 2022. For months, I’d been on the waitlist, hearing about this magical new tool that could take *any* description and output a matching image.

One of the first images I created used the prompt “80s tv commercial showing a hippo fighting a pegasus.” This was the output:

Fast-forward to today, less than two years after the advent of that mind-blowing capability. The same prompt, in ChatGPT 4o, yields this:

Despite persistent flaws and hallucinations (that hippo has three legs!), it is mind-boggling how far we’ve come in such a short period of time. Dream up *anything*, with any text description, and a machine will create a matching image in seconds.

Yet despite the technology’s sudden ubiquity, few people who regularly use it understand how it works or how these improvements come about.

Several months ago, I published a primer that explained __how large language models (LLMs) work__ using no technical language. I’d like to do the same now for image generators. As with LLMs, I believe that the core concepts are straightforward. The fancy calculus and ground-breaking computing power used to train these models is simply the application of something we can explain with an analogy to a kids’ game.

**The story plot game**

Let's imagine inventing a new game intended to teach children how to unleash their creativity and come up with fictional stories. Left to their own devices, children will typically write about topics that interest them. But our intention is to broaden their horizons and encourage them to think outside the box, to be comfortable ideating and crafting stories about *any* topic.

We're going to teach this incrementally. We’ll begin with a skill that (at first glance) might seem unrelated: identifying *existing* story plots.

The children will be presented with a sentence containing a single typo. If they find the typo, they will uncover the plot of a well-known film. Here it goes:

*A princess with magical towers accidentally sets off an eternal winter in her kingdom.*

I imagine most children would successfully identify that the outlying word is *towers* and that the word with which it should be replaced is *powers*. (The film, of course, is *Frozen*.)

Let's make it a bit harder. This time, the error won't be a rhyming word but an entirely different word altogether. For instance:

*A clown fish gets separated from his banana and must find his way home.*

This time, a child familiar with *Finding Nemo *will hopefully recognize the word *banana* as a typo and replace it with the word *father* to decipher the correct plot. But here's an interesting implication that comes with this second example: Had the child replaced *banana *with *best friend*, the resulting sentence would be perfectly logical and the plot perfectly plausible, even if it did not accurately summarize any particular Pixar film.

**Getting noisier**

We may seem far removed from our eventual goal of mirroring generative image models, but there is more happening here than it might seem at first glance. We’re teaching the children to identify compelling story plots hidden somewhere in a summary rife with errors.

Let's give these errors another name: noise. And let's turn the difficulty up a notch and replace two words in a given plot:

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
