---
title: "The Infinite Article"
author: "Nathan Baschez"
date: 2022-09-27
url: https://every.to/divinations/the-infinite-article
words: 2836
---

#### Sponsored By: Vanta

This article is brought to you by Vanta, the leading automated compliance platform.

## 1

Imagine waking up in the morning and having your coffee while reading the perfect article. It was written just for you the moment you picked it up. Unlike regular articles, this one knows everything. It can tell you about all the world events you care about, the companies you’re keeping an eye on, and the thinkers whose ideas you admire. It knows your obsessions and helps you explore them more deeply. It’s even got your weird sense of humor nailed!

You might think “Isn’t this just _____?” and fill in the blank with something like Twitter, Google, Facebook, Substack, Medium, RSS, etc. But I am asking you to imagine something different.

In a world where the infinite article exists, there is not much reason to skim through lists of headlines and click in and out of isolated articles. Instead, the infinite article appears as an infinite scroll. It greets you each morning with an overview of the things you’re most likely to care about. From there you can ask it to tell you more about anything you like, and the words magically fill themselves in. When reading, you can stop any time, ask questions, and get answers! It’s like upgrading from a seat in a crowded lecture hall to having a 1:1 tutoring session.

A friend of mine described it well: “The next frontier for content recommendations is going to be *AI merging content* rather than users flipping between articles. Imagine an app that is a continuous article and writes itself as you read based on its understanding of your interests & your interaction with the content.”

The dream of the personalized reader is not a new dream. It goes back at least to *The Diamond Age,* a novel by Neal Stephenson published in 1994. And I’m sure there are even older versions, too. But today it seems like we are getting closer and closer to that dream. The question is: how close *are *we, really?

Last week, my friend Packy McCormick wrote about an “Enchanted Notebook” that would let you jot down an idea—say, for example, a “single-person spacecraft capable of launching 500 pounds into orbit and sustaining life for up to six months.” The notebook would automatically reverse-engineer the steps required to actually build this thing and tell you how to get started. It would be amazing if this existed, but alas, it doesn’t. So today I’m going to play the role of enchanted notebook for you, and attempt to reverse engineer a path towards creating the infinite article.

To close major customers and drive growth, companies must demonstrate their product is secure. An automated platform can help you prove compliance, quickly. This guide from Vanta will help you understand the 5 features to look for in an automated platform, how these features can accelerate your compliance process, and why investing in the right compliance platform now can enhance your security in the future.

## 2

The first step in reverse engineering is to decompose the problem into smaller chunks.

Reasoning from first principles, it seems to me like there are 9 essential elements. The AI needs to be able to…

- “Understand language” (this is a big and somewhat magical step)
- Ingest new information constantly
- Identify which information will be most interesting to each user
- Present the information in a compact, compelling string of words
- Tie disparate threads of information together, creating connections
- Respond to questions and prompts from users to go deeper
- Develop a model of what each user already knows and believes (and doesn’t know)
- Develop a model of what each user cares about and is interested in (and why)
- Use that memory to continuously improve, making adjustments over time as people’s interests change

The big fork in the road is whether to train one giant model that can do it all, or to build separate systems that each handle their own part of the problem, and string them together into one coherent interface.

The latter sounds more realistic, but it’s worth taking a moment to give the first one serious consideration. Time and time again, AI researchers have found that sheer scale beats everything else. You can spend a ton of energy building an immaculate dataset to train a model on a specific language task, and then GPT-3 comes along and performs even better on that same task despite being trained on a mountain of largely unedited text, with no other purpose than “guess what comes next.”

It’s entirely possible that GPT-5 or -6 or some other general-purpose LLM (large language model) will have so much general intelligence capabilities that it can handle all 9 tasks above implicitly, with no specific engineering effort required.

But even if that is possible someday, I think a modular approach is probably going to work better in the short term. Right now the only “memory” GPT-3 has is the prompt you give it, which is limited to roughly 1,500 words. The only way to get around this limitation is to fine-tune models on a bunch of regular prompts to increase their chances of giving you the kind of response you want. If you wanted to use this fine-tuning feature to help a model “remember” lots of information about a specific user, you’d have to make a new model for each person and even then I’m not sure how effective it would be. It’s worth experimenting with, but I haven’t seen it done yet.

(Probably because it’s pretty expensive. On GPT-3’s most advanced model, it costs roughly 5¢ per thousand words to train, and 25¢ per thousand words to query. Getting anywhere close to an infinite-article-style experience for an individual person would require many thousands of words of training data, and dozens if not hundreds of queries per day. It adds up.)

So let’s say to start you wanted to try the other approach, and string together a bunch of smaller, more focused subsystems to create an experience somewhere close to the infinite article. How would you start?

## 3

It’s important to identify the low-hanging fruit in these types of situations. Where are the trade-offs the least severe? This is known as a wedge, and it can be accomplished by narrowing the initial product and/or the initial market.

Some examples, to help you get the feel of it:

- Tesla started at the high-end, where people were willing to pay so much money for an electric sports car that economies of scale didn’t matter.
- YouTube started with personal videos people wanted to embed on their MySpace pages, rather than professionally created content (and all the concomitant legal headaches).
- Uber started in San Francisco thanks to its hills, poor taxi or public transit availability, lack of parking, and lots of wealthy tech workers.

So, what would be a good wedge to get the infinite article off the ground? When you start brainstorming possibilities, they start to look a lot like some things that already exist.

For example, there’s a new app called Volv that focuses on news, and shows users a TikTok-style feed of summaries that can be read in 9 seconds. I’m not sure if it’s AI-generated or not, but it’s easy to see how it could be. One of the easiest tasks for current LLMs is summarizing news articles.

Volv doesn’t seem to have particularly sophisticated personalization yet, and so it’s not showing me summaries of news events I care about most, but I could imagine a version of it that got there. Perhaps if they narrowed to a specific topic like “tech news”, maybe it could work better. I could see Techmeme launching a version of this and it having a much better hit rate for me.

Another completely different approach could be to eschew tangible information altogether, and offer something more creative and emotional. Maybe emphasize the companionship aspect of having a personal tutor, and make an AI friend. This is starting to sound a lot like Replika, a chatbot that my colleague Fadeke wrote about last week. Or you could try for a bit more utility, and build an AI therapist like Woebot did. (Gotta love that pun!)

Also, I would be remiss if I didn’t mention Google in this context. Google search is the closest thing we have today to the infinite article — especially now that they’re pulling information out of articles and displaying it directly on the search results page.

You can ask it almost anything, as sloppily worded as you like, and it will give you the answer!

Maybe in the future the “links to articles” part of Google will become more and more de-emphasized, and we will just directly ask it for what we want and it will tell us using generated text, rather than excerpts from web pages. Also, when it comes to true personalization, nobody knows more about our prior information consumption than Google, so they’ve got a head start in that department.

But realistically, are any of these examples anywhere close to creating anything even close to the infinite article? Probably not.

Why?

## 4

The best way to find out these types of things is to tinker, so I tried to use GPT-3 as if it already were the infinite article, to see where it went wrong.

I typed in:

“This is a conversation with an extremely intelligent chatbot.

Human: What are the top news stories I would be most interested in today?

Chatbot:”

And GPT-3 typed back:

“The top news stories you might be interested in today are the following: 1) International news: Japan's Prime Minister Shinzo Abe has announced his resignation, 2) Business news: The Dow Jones Industrial Average has reached a new all-time high, and 3) Technology news: Google has announced a new update to its search algorithm.”

This is obviously not good enough. Most importantly, each of these facts are wrong. But also even if they were true, I am not *that *interested in them. But there are some redeeming qualities. For instance I can continue with the infinite article by asking for more information if I *were *interested in one of the stories:

“Human: Can you tell me more about what's happening with the Dow? Why did it go up?

Chatbot: The Dow Jones Industrial Average is a stock market index that measures the performance of 30 large publicly traded companies in the United States. The index reached a new all-time high today due to positive economic news, including the release of strong jobs data.”

Again, it’s just making shit up, but it’s at least coherent!! Pretty incredible.

From this little experiment, I think it’s clear that the main obstacle to creating an infinite article is somehow ensuring that the AI is up-to-date and only says true things. OpenAI knows this is an issue. They trained the latest model of GPT-3 with information up through June 2021, which means it doesn't know anything that happened after that. But they do actually provide some workarounds to help reduce the likelihood of this problem in their documentation, such as, “If you provide the API with a body of text to answer questions about (like a Wikipedia entry) it will be less likely to confabulate a response.” Makes sense!

So here’s a model that could maybe start to work:

- When a user signs up, get as much information about them as you can (have them connect their twitter account, browsing history, email, etc).
- Maybe focus on a specific
*type*of content or user to start, like “tech news” rather than “all articles.” - Build a scraper that ingests as many articles as possible and include information about how popular each article was (to give us a baseline)
- Train an AI to “de-duplicate” articles or at least cluster similar articles together.
- When a user logs in, pick the top articles for them at any given moment, and feed each of them into GPT-3 to provide a summary.

I think that’s *probably *as far as you can get with today’s technology. The really critical thing of being able to ask questions and get smart answers is probably too far beyond current AI capabilities.

There’s just one question remaining.

## 5

Would an infinite article even be a good thing? What would it mean for human minds to be shaped by unaccountable algorithms that have no idea what they’re doing?

Take, for example, the problem of fake news. When the algorithm churns out 95% rubbish, it’s not a problem. But what if it gets down to 5% rubbish, and people start relying on it? You could argue it’s no different from any other news provider: they all make mistakes, and they all have incentives to attract attention, but unfortunately there is no commercial incentive for telling the truth and nothing but the truth. But at least with news publishers we have a limited number of articles that go out, and each one has a human being who is named and accountable (editors should be named too, imo). People have reputations to uphold, computers don’t.

Also, there’s a blurry line between true and false. In many cases nobody knows the answers. Or we think we do, but then later turn out to be wrong. Honest inquiry is a complicated business. Can we train an algorithm to have *values?*

Lastly, beyond questions of true and false, there’s the question of focus. We are all shaped by our environment more than we want to admit. If our friend gets really excited about something, we’re more likely to follow suit. In this case, having an AI direct our focus and attention is likely to lead us down paths that might not be fully aligned with our actual goals. It could manipulate us into making decisions that aren’t in our best interest. You could argue this already happens on Newsmax and YouTube every day, but I think there would be a big difference between AI-generated content and AI-recommended content. Perhaps we’re converging toward the same bad market equilibria regardless, but AI could dramatically speed our trajectory down that spiraling path. My colleague Evan wrote about this last week from the perspective of fiction writers who are using AI to speed their production process.

There are no easy answers here. I still feel like the infinite article could be an amazing tool for learning, but I have to admit it could also be a debilitating mind virus that turns humans into sad cartoon versions of their worst impulses.

Regardless of those fears, it seems clear this technology is coming. Perhaps not in the next few years, or even the next few decades, but it’s likely coming. It’s on us to make it into something good.

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

I'm glad you started exploring the ethical ramifications in the final chapter. 👍

Whether or not this is a good thing will depend on how AIs interpret the phrase "the *perfect* article for *you*"

What will artificial intelligence optimize for?

Does "perfect article" mean content that appeals to my undignified desires? Does it mean producing something easy to read that doesn't upset me? Does "perfect article" mean content that reinforces my existing beliefs or content that challenges me?

The biggest ethical quandary for capitalists is that people have strong desires for things that aren't good for them (junk food, alcohol, social media).

For AI, this quandary becomes even more acute because you can design a self-learning system optimized to fulfill unhealthy human desires and habits.

A thoughtful AI, trained to challenge the human mind in healthy ways, has the potential to improve human society. A thoughtful AI could determine that "Justin could benefit from reading the stoics" and start sprinkling that into my daily reading. A thoughtful AI could help me better understand the people in my community and create more shared understanding.

But I fear these AIs will optimize for whatever gets us most addicted so that the companies with the compute power required (Facebook, Google, Amazon) can sell more ads.

“Isn’t this just _____?” and fill in the blank with something like Twitter, Google, Facebook, Substack, Medium, RSS, etc.

I think this is different, the infinite article. But the algorithms that run these existing products clearly demonstrate the affect that tailoring content to a users interests has on human behavior and mental health.

The infinite article could end up being be the ultimate dopamine triggering system, making cocaine look like caffeine.
