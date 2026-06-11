---
title: "Where Copilots Work"
author: "Dan Shipper"
date: 2023-03-09
url: https://every.to/chain-of-thought/where-copilots-work
words: 776
---

#### Sponsored By: Lever

Hire smarter with Lever—the only complete hiring solution that provides modern talent acquisition leaders with complete ATS and robust CRM capabilities in one product: LeverTRM

Luke Skywalker had R2-D2’s whistles and beeps. Maverick had Goose. Bertie had his butler Jeeves, who shimmered in and out of the room to perform tasks well before he’d even been asked to.

These stories are popular because everyone wants a copilot—a partner who makes you better, and who (sometimes) becomes a friend you can lean on when things get hard.

This sort of thing is exactly what a lot of people in AI are building right now.

GitHub CoPilot is the first large-scale AI use case that has significant traction—reportedly writing 40% of the code for developers who use it. Reid Hoffman thinks there will be a copilot for every profession. Microsoft is building an AI copilot into Office. Diagram is building a copilot for designers. The list goes on.

These systems work like a superpowered autocomplete. They predict what you’re about to do, and then offer that to you before you have a chance to do it yourself. It saves time and effort.

If you’re a builder hacking away on side projects, you’re probably thinking about building a copilot too. GPT-3 makes this kind of thing pretty easy to pull together over a weekend. I know because I’ve been doing it too:

I built a little copilot for my mind. I want it to help make me smarter: to make connections between ideas, bring up pieces of supporting evidence for points I’m making, and suggest quotes to use as I’m writing.

It takes in any chunk of text, and then attempts to complete the chunk using quotes it finds in my Readwise database.

It’s a cool demo, but it isn’t anywhere close to being a usable product yet. It doesn’t always pull great quotes for me, and it doesn’t always complete them in a way that actually supports the point I’m trying to make. It also doesn’t demonstrate sufficient understanding of my writing, or the writing of the authors it’s pulling from to be useful.

As I wrote in the End of Organizing, I’m quite optimistic about the future of technologies like this. I find myself reading fewer and fewer physical books and taking fewer physical notes. I’m increasingly confident that every digital highlight I make will be made 10x more useful by these tools in the next year or so.

The question for me and other builders like me, is this: Where can these kinds of copilot experiences *actually *deliver* *value with the technology that’s available *today*? And what are the bottlenecks that need to be resolved to make these useful for more use cases?

Let’s take these one at a time.

## Where copilots can be built today

AI-based copilots are quite useful with out-of-the-box technology in situations where small pieces of lightly transformed boilerplate text provide a lot of value.

This is particularly true in areas where:

- Text can be checked for accuracy quickly with little user effort
- The cost of inaccuracies is low
- Relevant text can be found reliably with embeddings search

GitHub CoPilot is a great example of this. But other examples are things like grant writing, contract writing, tax prep, many types of email replies, RFP responses, medical recommendations to doctors, and more.

If you’re building a copilot (or thinking of building one), I’ve put together a little checklist for you to go through in order to figure out whether it will be possible to get good results with today’s technology.

## Can you build a copilot for it? A checklist.

If you want to build a copilot for a specific domain using today’s technology here’s the list of things you need to check off:

- Is there a corpus of relevant text completions to be used by this copilot?
- Can relevant text for completions be found reliably with embeddings search over this text corpus?
- Can those pieces of text, without more context needed, be lightly transformed and inserted as an accurate completion?
- Can completions be checked for accuracy with little to no user effort?

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
