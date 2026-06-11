---
title: "A Few Things I Believe About AI"
author: "Dan Shipper"
date: 2023-04-21
url: https://every.to/chain-of-thought/a-few-things-i-believe-about-ai
words: 1097
---

#### CHATBOT COURSE EARLY BIRD PRICING ENDING SOON!

We are thrilled to announce we are relaunching our How to Build a Chatbot course! If you are interested in learning how to build with AI, join our upcoming Fall cohort taught by our very own Dan Shipper.

In the course you'll learn:

- How to aggregate sources of data for your chatbot
- How to manage your vector databases
- How to build a UI and bring your chatbot into production
- How to use Langchain and LlamaIndex to build a chatbot that can access private data, and use tools
- and so much more!

Learn how to build your own chatbot in less than 30 days. It will run once a week for five weeks starting September 5th and early bird pricing is available for $1,300 along with an Every membership. Last time we ran the course it sold out pretty quickly, so if you are interested, grab your seat now while early bird pricing still applies.

Early-bird pricing ends on July 31st, after that the price will be $2000.

Over the last 6 months I’ve been obsessively tinkering with, writing about, and investing in AI. It’s been a ride. I’ve talked to some of the most interesting thinkers in the space, I’ve stayed up late at night hacking zillions of little experiments, I’ve panicked about AI doom, I’ve imagined never organizing anything again, and I’ve basked in the warm glow of curiosity and delight I get from using these models.

Working in AI during this period has felt like having a SpaceX rocket strapped to my butt. I think everyone feels this way. You go very fast, but you constantly feel behind. Every once in a while your brain explodes with the possibilities in front of you. It’s easy to end up carried away with all caps tweets about how THE WORLD HAS CHANGED.

Today, I’d like to write something a little more nuanced and reflective. Even if you’ve got a rocket strapped to your butt, it’s important to look down every once in a while, and take stock of where you are. As such, here’s a short list of things I believe about AI that are shaping how I’m approaching my work at Every and beyond.

## Knowledge orchestration is the most important bottleneck for AI applications

There are two important components to intelligence: reasoning and knowledge. GPT-4 is quite good at reasoning, but its knowledge of the world is limited. As such, its performance is bottlenecked by our ability to give it the right knowledge at the right time for it to reason with.

This problem, which I’m calling *knowledge orchestration*, is the biggest unsolved problem for builders in AI outside of progress on foundational models. It touches how you store, index, and retrieve the knowledge you need to perform useful large language model tasks. There are many people trying to improve this at different layers of the stack:

OpenAI and other players are working to build this at the foundational model layer. They’re building bigger context window sizes: the more knowledge you can fit into your prompt, the better. GPT-4’s 32,000 token context window is 8x better than previous models, so improvement is happening quickly.

One layer up from that, LlamaIndex and Langchain are building at the developer tool / infrastructure layer. They’re making it easy for developers to chunk, store, and retrieve knowledge from various different kinds of databases with only a few lines of code.

Vector database providers are also working on this problem. Pinecone, Weaviate, and Chroma are all battling for supremacy here—with Pinecone in the lead.

Finally, various all-in-one solutions like Metal and Baseplate are bundling all of these layers of the stack together to make it easy for developers to get started. They’ve got slick web interfaces that make data observable, and easy for developers to get started quickly.

I suspect all of these players will start to leak out of their current layer of the stack, and try to grow into other areas. The right solution will figure out how to integrate layers in the right way to make it easy for builders to get started and to make iteration speeds faster.

Knowledge orchestration is the *process* around knowledge. But what about the knowledge itself? What *kind* of knowledge is most valuable?

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

don't you mean "vertically integrate"?

this is super insightful!!!

@vidy I went back and forth between vertically and horizontally. the definition i'm working off of is "vertically integrate" means anything that a company would normally pay a supplier or vendor for, and "horizontally integrates" means anything that a company's customers would normally pay someone else for.

but i could be wrong!

@danshipper oh that makes a lot of sense!!

@vidy @danshipper There might be various interpretations but I also thought it should be vertical integration. The way that I think of it is that in software consumers are often the one stitching together vendors and suppliers. If you buy an iPhone, Apple must figure out how to get all the physical components into the phone but if you use Midjourney, you have to figure out how to touch up, crop, and publish the image.

“”” “horizontally integrates" means anything that a company's customers would normally pay someone else for.”””

I interpreted that as being alternatives to the company itself since the customer might pay someone else to solve the same problem e.g. Airbnb expanding to operating hotels would be horizontal.

Anyway, great piece as always! I think being able to build with AI, speak to it as a writer and business thinker reveals truly unique insights.

This is insightful article. Read on 4/25/2023.

"Startups that are horizontally integrated over a process will be dominant"

"In other words, they started out as an API-only, but realized that the best way to improve performance was to integrate forward over more layers of the value chain so that they could get direct access to their customers' data."

Memo to myself: https://share.glasp.co/kei/?p=TolNDPEmLMj1NH2uJ554

Arrived here for the "first part" required to the "AI ChatBot Workshop" and stayed for the cookies.

@tomas.flores.art welcome!!
