---
title: "The Button Problem of AI"
author: "Evan Armstrong"
date: 2024-09-12
url: https://every.to/napkin-math/the-button-problem-of-ai
words: 2641
---

*Before our regular programming, I wanted to tell you I am teaching a course on **How to Write With AI**. It’ll show you how you can use AI tools to create higher quality writing significantly faster. Registration closes on September 15, so act quickly to secure your spot.*

When GPT-4 came out 548 days ago, the world was supposed to change. Our computers would get an IQ upgrade, ushering in an age of productivity for humankind.

None of that has happened. Instead, we’ve gotten a mixed bag.

For the AI bulls, there are stories of staggering growth: ChatGPT has 200 million weekly active users—twice as many as nine months ago. Meta AI’s chatbot has 40 million daily active users, with 400 million logging in per month. Nvidia is the hottest stock of the last few years, and ServiceNow, an enterprise software company that automates workflows, has seen material revenue gain from adding AI to its platform, fueling a 37.5 percent increase in its stock price over the last 12 months.

For the AI bears, we have earnings calls where Nvidia’s CEO struggles to articulate what kind of revenue benefit his customers are seeing from purchasing his chips, and launches into a discussion about "first principles." Microsoft, the company that most astutely forecasted the power of LLMs with its $13 billion dollar investment in OpenAI, can’t get more than 1 percent of its customers to purchase its Office 365 AI-powered software. At Microsoft’s scale, even 1 percent represents hundreds of millions of dollars in revenue, but it’s notable how relatively small the adoption has been.

On the startup side, AI-focused ventures comprise half of the 28 firms that have reached the coveted $1 billion valuation mark this year. Yet there were 69 unicorns last year, and 502 in 2021. If AI was such a boon to technology companies, surely there should be more amazing startups appearing?

It is tempting to blame these poor results on slow-moving customers or the financial markets. But while those things certainly played a part, I believe there is a more innocuous explanation for why the AI revolution has fallen short of our expectations: Almost all of AI’s progress can be delivered with a button.

**Button it up**

Because AI is currently incapable of building and following complex plans as an independent agent—at least as far as the current generation of large language models is concerned—productivity software tends to buttonify it into small, discrete tasks.

For example, I like to set aside some time every evening to send emails with the productivity app Superhuman. Let’s say I’m not coming home for Christmas, and I need to send my mom an email to let her know. (I’m too scared to call her, for obvious reasons.) I could spend an hour writing this terrifying message. Or, I could just hit a hotkey to bring up the AI module and type in the gist of what I want to write.

*Source: All images courtesy of author’s screenshots.*

Superhuman will do a remarkable job of writing a short, friendly email letting my mom know the bad news. And if I want to edit it, I can hit an AI button that will edit the message for me:

Because most fixes follow similar patterns across users’ workflows, all I need to do is select from a set of predetermined options like “shorten” or “simplify.” This is both the beauty of existing AI tools and the rub: The majesty of LLMs, the tens of billions being spent building more and more advanced systems, gets boiled down to a single click allowing me to do a task I would do while writing anyway.

Do you know what this makes Superhuman? An email app. That’s it! AI just makes it do email better.

The reduction of AI’s ambition applies to most LLM-based products in software today. Because the models are unable to handle knowledge-labor workflows in their totality, product builders are forced to bind LLMs to tasks that are small and easily definable. And what is the best way for a user to deploy a small, discrete task? You guessed it: a button.

To be fair, these are tasks that word processing software wasn’t capable of before; users just did them manually. Now, instead of writing the scary email or relying on an editor to perfectly place commas in a text, you can have the model do it.

But simply replacing small portions of a workflow with an AI button isn’t enough to meaningfully change the work itself. To materially increase a worker’s productivity (and give a startup going after a market the chance to replace existing tooling), it has to be an experience that is 10 times better than previous options—and, more importantly, done in a way other platforms can’t replicate.

## What about chatbots?

Clever reader that you are, you may have noticed that Superhuman offers me another option while editing: “Describe how to edit the text.” Does this mean that my thesis is incorrect? That LLMs are too powerful to be contained by the lowly button? No. As I see it, even the integration of a chat interface solidifies power in existing ways of working.

I write my essays in Lex, a Google Docs competitor incubated here at Every. If I want the AI to rewrite something, I can highlight the passage in question and hit the “rewrite” button.

Over time, the Lex team will make that button more useful by improving its ability to produce rewrites that adhere to my tone and voice. However, if I want more control, I can hit the head emoji below the rewrite button and pull up a chat window. Presto, the chatbot will help me take my essay to the next level—like nail a joke I am trying to write from the perspective of a pirate.If I find myself asking the same question of the chatbot over and over again, I can turn a custom prompt into a button. For example, I built one called “What would evan say” that helps me write conclusions based on those I’ve written in the past. (If you are interested in learning how to do this, I am teaching a course on How to Write With AI that starts next week. Registration ends in four days, so act quickly.)

Lex even lets me pick which AI model I want to use, saving me the time I would normally spend pulling up the chatbot of my favorite writing model maker, Anthropic.

Just as spellcheck started as a standalone tool before getting bundled in the word processor, developers can easily integrate chat into any type of productivity application, either as part of a workflow or in a window next to where the work is done. This means that incumbents will be naturally advantaged—LLMs’ functionality is simple enough to be contained in a button, or is similar enough to existing types of knowledge labor that it can get bundled in. Software will mostly struggle to differentiate on the basis of AI capabilities.

The principle I’m trying to drive home is this: Every incremental innovation in technology starts off as a differentiated skill but ends up as a button. When a new, hard-to-grok tool hits the market, a craftsman can command a higher wage by learning to use it. However, over time, most tools become easier to use, and their capabilities become commoditized. They are buttonified, bundled, and obfuscated into a machine, sometimes with the result of downgrading the craftsman to a lineworker.

As I see it, the only way that a startup can build a materially superior business is by making the previous tool’s capabilities a commodity component in their machine, then adding adjacent workflows that were previously within the purview of other applications. In writing, this could mean evolving the writing workflow to completely automate monetization and distribution, tasks that Google Docs would be incredibly challenged to replicate. In my case, you could write the essay, and the LLM could automatically translate it into a format for Twitter or LinkedIn, write and place the paywall, and publish it to an email list.

## Death to drudgery

Programming environments are another area that illustrate the limitations of buttons. For a variety of reasons that we won’t get into today, writing code has turned out to be one of the tasks that LLMs are best at. The first iteration of AI in coding included buttons that a programmer could hit while writing a line of code, and the LLM would finish it. While this is an amazing invention that allows programmers to write more code, it does not suddenly open up the market for startups. It is easier to integrate a “AI write code” button rather than creating an entire developer environment from scratch.

Replit is a great example of a tool that started off as a type of standard development environment to write code in and used LLMs to go much further. Amjad Masad, the company’s founder, described its agent product like this: “AI is incredible at writing code. But that’s not enough to create software. You need to set up a dev environment, install packages, configure DB [a database], and, if lucky, deploy. It’s time to automate all this.”

Replit Agent neatly bundles the workflows of an integrated development environment into an AI agent that also allows you to write and deploy code. All you have to do is prompt a chat window with what you want to build. Two nights ago, while watching the presidential debate and feeling pretty depressed, I felt an urge to create something that would bring more joy into the world. So I prompted Replit Agent to make a website with a button that would fill the screen with smiley faces.

From there, the app did the rest. I could even prompt it through the chat interface to check in on its progress. Before I knew it, the app was up and running. All it does is make smiley faces, but that’s enough for me. You can try it! It took maybe five minutes to create, and tied together tasks that used to require multiple different skill sets and tools.## The triumph and tragedy of LLMs

The button-ification of AI isn't just a design choice—it's a stark reminder that we're still in the “training wheels” phase of this supposed revolution.

That doesn’t mean that what has happened isn’t useful. AI tools—including the buttons—have made it possible for me to produce quality writing a lot faster. When it does work, I experience a quantitative lift in productivity. However, the “when it does work” stipulation doesn’t cover as much of our current knowledge work as we hoped when this class of models hit the market.

We've created a technology with the potential to redefine human creativity and productivity—and reduced it to a feature in our email apps. We're so focused on making AI fit into our existing workflows that we've forgotten to ask whether those workflows even make sense anymore.

I don’t want to do email faster; I want to never do email ever again. And the only way AI startups will be able to compete with existing technology giants is if they dream big enough to make our current knowledge work software pointless. They have to automate the labor of email entirely—or eradicate the need for it altogether. Until then, we'll be stuck in a world where the most advanced technology in human history is reduced to a button that writes emails to our moms.

*If you want to learn how to use AI in your writing like I’ve discussed today, I’m teaching a course all about it, starting on September 19. Registration closes this Sunday and spots are limited, so act quickly to secure your seat.*


*Find out more**.*

*Large language models are a gift. They are not replacements for creativity or skill, as some have feared—they’re amplifiers of ambition that allow you to create better work, faster. *

*Four years ago, I had 25 subscribers to my name (most of whom were blood relatives), but decided to become a writer anyway. Now, I’m publishing two full essays a week to an audience of more than 78,000 people. Since I started publishing online, I’ve reached number one on Hacker News multiple times, written cover articles for magazines, and been read by my heroes. *

*Going from no experience and no skills to this outcome has only been possible with one thing: AI. *


*Evan Armstrong**is the lead writer for Every, where he writes the*

*Napkin Math*

*column. You can follow him on X at*

*@itsurboyevan*

*and on*

*, and Every on X at*

*@every*

*and on*

*.*

*Was this newsletter forwarded to you? **Sign up** to get it in your inbox.*

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

This is an interesting take. But I think it is scoped too narrowly. The question of why AI hasn't yet revolutionized anything and - more importantly - whether it actually will is quite interesting. At present the element of time simply must be acknowledged: the pace of adoption has been meteoric compared to almost any other general technology example one could care to name. So the fact that this adoption may be "shallow" at present seems like a lot less of a prediction of its longer-term potential.

Perhaps more importantly most - if not all - big change is as much about culture and the momentum of the world we already exist in as it is about the actual utility of a given technological or scientific achievement. There may be arguable exceptions to this: it's fair to suggest that perhaps when the technology is the "right" one for the moment, or is delivered in the exact right way, then monumental change can happen relatively quickly (see: iPhone). And it's hard to imagine that possibility before it occurs, at least for most people (myself included).

Having acknowledged that, I still have to say I find it extremely unlikely (to my dismay!) that AI could "get rid of" email, at least not very quickly (which takes a lot of the air out of the "it's a revolution!" balloon). My skepticism is not so much about technological limitations as cultural ones. Slack promised to do this, for a while it looked like a huge revolution, and now it just exists alongside email and arguably only *added* to the channels of communication we have to deal with, in which case it actually just made the problem worse. 😅

I think people trusting AI at a deep level is what will be needed for the kind of adoption required to weaken email's grip. There are signs that this kind of trust is already developing more rapidly than with many other technologies, so we'll see. I'll be as happy as anyone if we can stop having to check email regularly!

good piece but who reinvents the issues ....like never wanting to do emails again.....I don't think AI with LLM models has the ability to do that...it still takes human oversight especially if the reality cha get around you fast...i.e. you aren't coming hime of xmas cause a fire burnt down you house.....agents need a new approach to do stuff by itself

If we all have Neuralink implanted we could avoid email altogether by transfering thoughts by thinking where to send them. I'm not sure mom would always appreciate the 'not home for Xmas' message.
