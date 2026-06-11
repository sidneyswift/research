---
title: "Five AI Products You Can Build With GPT-3 Today"
author: "Nathan Baschez"
date: 2023-02-21
url: https://every.to/divinations/five-ai-products-you-can-build-with-gpt-3-today
words: 976
---

#### Come hear Nathan speak

If you like this post, you’ll love getting to hear from Nathan live at our Thesis conference this Saturday. Only a few tickets remain—purchase them at the link below.

AI critics say that the technology is all hype. They are wrong. I’ll show five categories of products that are a) currently possible, and b) I am extremely excited to use, hopefully soon.

I’ve become familiar with what GPT-3 is capable of by building Lex. I spend a lot of time writing prompts, and seeing what it gets right and what its limits are. It reminds me of when the iPhone first came out: if you paid attention, it was easy to see that transformative new product experiences would inevitably emerge. It’s hard to see exactly what those will be. Still, it’s fun to guess :)

So here are some of the new products that I predict will emerge thanks to AI. None of the ideas are dependent on technical advances—they could all be built *today* using GPT-3.

## 1. The infinite article

How much of your time do you spend scrolling through feeds and scanning articles? If you’re like me, it represents a decent chunk of your time. What if you could hire someone to do this work for you and compile a daily briefing? What if you could ask them questions and prod them to go deeper on the topics that interest you, and skip over anything that isn’t worth your time?

I would love this! I can’t wait for someone to build it. I presented this idea initially in September of last year. At the time I thought it was something that was years in the future. Now, I’m convinced you could build it today.

When I first thought of the idea I assumed the best you could do is to build a personalized list of articles based on a user’s Twitter history, the email newsletters they subscribe to, or any other data you can gather about the user. And I thought the best the AI could do is offer a short summary. I didn’t think it was possible to allow users to ask questions and have the AI give accurate, interesting answers.

I was wrong. Since then, a few things have caused me to update my thinking.

First, I realized you don’t need to get much information from users to offer a compelling user experience quickly. You definitely don’t need to scrape their Twitter feed, browsing history, or email. How did I learn this? From a new product called Artifact, created by the Instagram founders. The basic idea is simple: you check a few boxes of topics you’re interested in (e.g., Formula 1, tech, interior design), and the app will start recommending articles to you. It doesn’t collect any data on you other than what you do inside the app.

When you first start using Artifact, the article suggestions are just okay. But it only takes a few days for the suggestions to get much better—proving that good personalized recommendations are not as hard to make as I thought, and don’t require a large existing user base.

The second big shift in my belief happened when I learned about embeddings, a technology that makes the “question answering” part of the idea easy to implement. Without diving too deeply into the technical weeds, embeddings make it possible to retrieve chunks of text from a document that are relevant to a user’s question. You can then stuff these chunks of text into a prompt and have GPT-3 use it to factually answer questions. My co-founder Dan has done a lot of cool stuff using embeddings to create chatbots that answer questions based on a specific corpus of text, like *Huberman Lab* transcripts or Lenny Rachitsky’s newsletter.

With these two pieces in place, I feel like someone could easily build a wonderful daily briefing tool. If you’re building it, please let me know on Twitter. I would love to try it.

## 2. Shopping assistant

I perform the following routine at least once a week:

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

Hi Nathan, thanks for your articles. Yes, I agree there is a tone that can be done. Here is one. I was looking at Upwork and a building inspector wanted to be able to write a list of observations (from inspecting different rooms) and then spill out automatically a summary of it in a certain style, with an example provided. In one afternoon, I built a little app on streamlit that uses one of OpenAI's model and the right prompt (using the example given) to output exactly what was needed. I am also thinking about other ways but every time I think of one, it seems I already find an app that does it :)

The shopping assistant idea is one I've been yearning for lately as well. Could save me a lot of time (and possibly money). And I do think it being independent and *not* being e.g. an Amazon service is pretty important to trust, at least for me. I'd easily pay $5-10/mo for it, personally. Especially if it could cover groceries, audit my various "Subscribe & Save" orders (which are often but not always the best deal), etc.

For the meeting search use case, Otter.ai does that today!

Hey Nathan, curious about the people finder idea. How are people and their skills captured by LLMs?
