---
title: "What I Saw at OpenAI’s Developer Day"
author: "Dan Shipper"
date: 2023-11-06
url: https://every.to/chain-of-thought/what-i-saw-at-openai-s-developer-day
words: 1847
---

#### Sponsored By: LiveFlow

This essay is brought to you by LiveFlow, North America’s #1 Financial Analysis Software.

Planning your 2024 Budget but don’t know where to start? LiveFlow has already made the financial models and templates. Budget vs Actuals by Department, 13-week Cash Flow Forecasting, Consolidation… All you have to do is plug and play. Just connect your QuickBooks Online to their models and it’ll be fully set up in minutes. Say goodbye to manually entering financial data. Say hi to automatic updates of your custom models and fully streamlined financial management. Get 20% off for 3 months with promo code EVERY.

LiveFlow, the ideal choice for automation and efficiency. #1 Easiest to use software for Financial Planning & Analysis by G2.

I like to watch what people do when they think no one's looking.

That's the incredible thing about going to events like OpenAI's Dev Day: you get to see the things that the cameras don't pick up, and hear the things that don't get said on stage.

It was all crowds, concrete, fast wifi, and LED lights. A magic show for AI nerds like me.

I waded through the crowd doing my patented FCO: Furtive Conference Ogle. I would see someone maybe-famous—Roon, say, or Karpathy, or Kevin Roose—and quickly glance down at their badge and back up at their face before they could give me a look like, "Hey, my eyes are up here, buddy!"

I usually sit near the back at events, but at Dev Day I made sure to get a seat at the front. I wanted to see the magic up close.

Sam Altman walked on stage and greeted the crowd. I could see the taut, contained, nervous energy in his face and body as he performed. I could feel the hours of practice in his delivery. After a short opening monologue, Sam introduced a video of creative professionals, developers, and regular people talking about how they use ChatGPT. The lights dimmed, he stepped off to the side, and the video started. Everyone was watching the video, but I was watching Sam.

He was standing alone in the shadows on the corner of the stage. He was wearing dark jeans and Adidas x LEGO collab sneakers in primary colors. His hands were folded in front of him, and he stared intently at the floor. Sam is intense and always “on.” But on the side of the stage, listening to the video being played, he was unpracticed and unstudied. I felt like I had caught a magician’s left hand as he maneuvered a hidden coin, while the audience watched his right hand waving.

Seeing a magician's secret temporarily breaks their spell. But it also creates a new kind of magic: you see the magician as a human being. Eating, breathing, putting their pants on one leg at a time, and making magic all the same.

Sam is on his way to becoming a legendary figure in tech. But in that moment on the stage, he was also a human being. He looked like he was enjoying himself, observing and anticipating the thing he's made, and watching it play out on the biggest stage in the world. He was living the dream of anyone who’s ever built something and hoped the world would like it.

Watching him in that moment was worth the price of admission. I won’t soon forget it.

Here’s what he had to tell us:

Bigger, smarter, faster, cheaper, easier.

That’s the summary of the changes that OpenAI announced yesterday. Let’s go through the updates one by one and discuss why they’re important.

## A new model: GPT-4 Turbo

### Bigger

OpenAI launched a new model, GPT-4 Turbo, that sports a 128K token context window. That means that each prompt you send to GPT-4 Turbo can be up to the equivalent of 300 pages of text. Here are a few things that can fit into 300 pages:

- 100% of
*The Lean Startup*by Eric Ries - Three copies of
*The Little Prince*by Antoine de Saint Exupery - At least half of my collection of moody journal entries from middle school

This is a 16x increase from the context window length of the most widely available version of GPT-4 prior to today. It significantly enhances the complexity and power of the queries developers can run with GPT-4. Previously, developers had to spend time and energy deciding what pieces of information to put into their prompts, which I’ve previously argued is one of the most important bottlenecks for LLM performance.

A 128K context window makes this task far easier, but it doesn’t solve every problem. Long context windows are hard to manage, and LLMs are more likely to forget or miss context the longer the inputted context gets. We don’t know if GPT-4 Turbo suffers from these problems yet, but I’ll let you know as I start to build things with it.

### Smarter

GPT-4 Turbo is smarter than previous generations of OpenAI models, in a few ways.

**It can use multiple tools at a time.** The previous version of GPT-4 introduced tool use, which I covered. Tool use allows GPT-4 to call out to developer-defined tools—like web browsing, calculators, or APIs—in order to complete queries. Previously, GPT-4 could only use one tool at a time. Now it can use many.

**Updated knowledge cutoff.** Previous versions of GPT-4 only knew about events up to September of 2021. This version is current up to April 2023, making it far more reliable.

**GPT-4 speaks JSON.** JSON is text that’s easily readable by non-AI applications. GPT-4 Turbo can return results reliably in this format—making it far easier to integrate into other pieces of software. Previously, developers had to cajole GPT to format its output correctly by, for example, telling GPT they would be fired if it messed up. No more cajoling necessary.

**GPT-4 can write and run code.** For a while, ChatGPT Plus users have been able to use Code Interpreter (later renamed Advanced Data Analysis), a ChatGPT plugin that can write and run Python code for you. It’s like a data scientist in your pocket—and now it’s available for developers to use and integrate into their own programs via the GPT-4 API.

**Multimodal.** The GPT-4 API can accept images at input: developers can send it any image and GPT-4 can tell them what it sees. It can also do text-to-speech, meaning it can reply with human-like voices to text input. And it can do image creation with DALL-E.

### Faster

As far as I can tell there are no publicly available speed benchmarks, but Sam said it was faster. Based on my very scientific testing of playing with it in my PJs last night, he’s right. It’s really fast. It leaves GPT-4 in the dust and seems at least as fast as, if not slightly faster than, GPT 3.5 Turbo—the fastest previous model..

### Cheaper

GPT-4 Turbo is **3x** **cheaper** than GPT-4. I can’t remember a company that’s been able to so aggressively improve performance while also slashing the price.

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

great piece Dan ...am using it in my Understanding AI classes and interesting to see how it stacks up against Gemini from Google when we hear more about it. One item I keep mentioning in class which I never here anyone talk about is how Open AI has maxed out potential return for investors like Microsoft at certain levels (I think 100 billion for MSFT) so that it isn't ruled by making money for investors if it reaches valuation goals such as APPLE or GOOGLE. I think that is a huge change in what it might become and say in class but no one seems to talk about it. Any thoughts? Keep up the great work; will be contacting your new editor early next year to see if we can set up a farm team of journalist for your company. best, Craig

So far the best I’ve read so far about the event. Kudos Dan. Lots if strategizing to do for devs that use OpenAI’s suite for their own product. The so called “wrappers are dead” companies.

I don’t think it’s as simple as “wrappers are dead”, especially if they are adding a store.

Interesting anecdote. Microsoft Azure team pinged us unsolicited with the pitch “you should be on Azure store because…”. We did a call it’s interesting.

Maybe apps have three channels. Normal old way B2B SaaS, the OpenAI store, and the Azure store.

As a thought experiment, how many apps are in the Salesforce App Store?

Best,

Drew

Thanks for the update Dan. I really appreciate your articles. You've made a very complicated, technical and foreboding topic feel approachable for a simple, non-technical and easily intimidated average person. I don't think I'd have gone anywhere near Chat GPT without having stumbled across your writing in another newsletter. It's now a tool I use regularly to help with 'life admin' and work...

Have a personal connection to anyone at OpenAI? I'm a professional namer (one half of a micro-agency that specializes in naming and brand architecture) and I'd LOVE to get my hands on their naming system. It's so confusing now, and it's only going to get worse as they develop more products. Plus I can't tell you the number of people I've heard say "Chat GTP"...

And (unrelated to the naming) - does any of what was announced change your plans for the upcoming Chatbot course? I'm signed up, but I find myself wondering if the syllabus was just rendered semi-obsolete. Still super interested in learning, but I'm hoping maybe there will be adjustments or supplementary lessons?

So what if someone put the muscle into making all those personas and then created a marketplace of those personas that you could just grab when you needed them? Students want to practice their debating? - the debater. Trying to hold the boundaries with a toddler and ran out of steam with your four lines? - The toddler diffuser. They keep saying they’re fine but you can see they’re not fine? - “The Fine reaponder”. Does this “persona marketplace exist?” Is that what the openAI App Store intended to be but the problem is that it’s not so much an app as it is a bot? Can’t anyone build the “persona marketplace”? Wouldn’t you be able to load the negotiator somewhere and anyone could use it once off for say $5 for the hour or lifetime for $58. Does this all make sense? Would it work?

That Watching Sam on the corner of the stage in the shadows part , Maaan that's a movie opening right there.
