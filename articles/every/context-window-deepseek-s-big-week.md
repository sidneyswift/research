---
title: "The Fallout From DeepSeek"
author: ""
date: 2025-02-02
url: https://every.to/context-window/deepseek-s-big-week
words: 2927
---

# The Fallout From DeepSeek

Plus: The case for selfish software

February 2, 2025 Updated December 17, 2025

*Hello, and happy Sunday! After a week in which DeepSeek’s R1 model shocked the tech world, **Alex Duffy** **covers the response from U.S. incumbents and startups, and Behance founder **Scott Belsky**—who’s leaving tech for Hollywood—updates us about how he uses AI.** **Scroll down to read that and everything we published last week.*

*ICYMI: More than 70 students—including vice presidents at public tech companies, marketing heads at asset managers, venture capitalists, and engineers—have already enrolled for our class **How to Write With AI**. **Taught by **Evan Armstrong**, the next cohort starts on February 13. Learn more about the course and **reserve your spot**:*

*Finally, we’re thrilled to welcome **Michael Reilly** to Every as our new managing editor. Michael joins us from, most recently, The Markup, and previously was at Protocol, MIT Technology Review, and New Scientist.—**Kate Lee*

## Release notes

### DeepSeek's big week: A wake-up call to stop waiting for OpenAI

*Access to the DeepSeek paid API has been down for days under massive demand. Source:*

*DeepSeek*

*.*

A couple of months ago, almost nobody outside of some machine learning researchers had heard of DeepSeek. This past week, its app surged to the number-one spot in the App Store, headlines declared the startup was responsible for wiping out over a $1 trillion in stock market value, big tech was in a panic, and many—including OpenAI CEO **Sam Altman** and even President **Donald Trump** felt obliged to respond.

But the story behind the hyperventilating is more nuanced—and more interesting. Yes, DeepSeek’s R1 model is impressively cost-effective and almost on par with some of the best large language models around. Yes, markets reacted, with Nvidia’s stock diving 17 percent at one point. But many of the most educated voices were quick to point out that it's unlikely the demand for Nvidia chips will decline any time soon, and the chip maker’s price has since recovered somewhat. There was also a more profound takeaway: R1 is a wake-up call. It proves that advanced AI needn’t only come from the biggest, most well-funded companies, and that smaller teams can push the envelope instead of waiting around for GPT-5.

Let’s break down what happened, why so many reacted the way they did, and how major players like Microsoft have seized the moment to push forward their own agendas.

#### The frenzy: Stocks, narratives, and why everyone freaked out

*Source:*

*Peter Gostev/LinkedIn*

*.*

DeepSeek’s R1 was released on January 20 to the excitement of researchers in the machine learning community. It did not come as a surprise as DeepSeek has been openly putting out superior models and research for most of the past year, but this time there were a few key differences. The model was much better in practice, significantly cheaper, and had no rate limits— developers could make requests to R1 as often as they liked with no restrictions (OpenAI and Anthropic, meanwhile, have been struggling to meet high demands). The release also coincided with inauguration day in the U.S., which might explain why it otherwise flew under the radar until the *New York Times* published an article three days later. Other mainstream U.S. media outlets soon followed, largely latching onto a single storyline about the threat to U.S. dominance.

Yet, as we’ve seen repeatedly in AI, big claims about “killing GPU demand” rarely hold up. Both **Andrej Karpathy** and **Yann LeCun**, two of the most influential AI researchers in the world, argued that massive compute is still essential. Once we have incredible AI, we'll need to serve it to billions of people daily. Hence, more compute spending, not less.

Meanwhile, as news of R1’s impressive performance and price point (about 96 percent cheaper than OpenAI’s o1 model) spread, AI leaders were compelled to respond.

#### The CEO perspective

OpenAI’s Altman rarely comments directly on competing models, so it was noteworthy that he weighed in. He called R1 “impressive for its price,” gave "credit to R1" for updating OpenAI’s views on thinking tokens, discussed open-source strategy, and promised that OpenAI’s next releases would be “pulled up” (i.e., done sooner) to show just how crucial bigger budgets and “more compute” still are. As if on cue, OpenAI announced the release of its new model, o3-mini, Friday afternoon—a cheaper, better reasoning model positioned to directly compete with, and even outperform, R1. However, o3-mini does cost almost twice as much as R1 per word generated.

Open AI also accused DeepSeek of improperly harvesting its data, which was met by a large chorus of published authors, internet creators, and social media users reminding the company that it did the same thing.

Anthropic CEO **Dario Amodei** went further. He published a 2,700-word blog post arguing that while R1’s cost savings fit into a known trend and shouldn’t come as a surprise, it may yet be a matter of national security:

"If the U.S. and China were at parity in AI systems, it seems likely that China could direct more talent, capital, and focus to military applications of the technology. Combined with its large industrial base and military-strategic advantages, this could help China take a commanding lead on the global stage, not just for AI but for everything."

He emphasized the importance of export controls, saying that if China can’t secure millions of high-end chips under new U.S. rules, it may slow the country’s progress in the race to build truly transformative AI. While Amodei’s argument makes sense, one reason he may have written such a strong reaction is that R1 poses direct competition for Anthropic. The company hasn’t built many consumer products on top of its homegrown AI model, Claude, and instead relies primarily on selling direct access to its model via API for other businesses to build with. (Claude has a similar performance to R1, but is much more expensive to run.)

However, there was one notable large language model provider that was clearly prepared.

#### Google’s quiet 'state-of-the-art' drop

*Source:*

*Chatbot Arena leaderboard*

*.*

One day after R1 came out, Google quietly released an update to its Gemini 2.0 Flash thinking model that beat R1 and all other models in most benchmarks, and currently sits in first place overall on the Chatbot Arena leaderboard. Google DeepMind researchers also published a paper echoing the same reinforcement learning approach that made R1 stand out—defining tasks with objective success criteria so the model can iteratively improve its reasoning. While others scrambled to spin R1’s success with soundbites, Google kept shipping, letting the results speak for themselves.

#### Market opportunism: Perplexity, Hugging Face, and Azure jump in

It didn’t take long for companies to turn the hype around R1 into a marketing opportunity. AI search engine Perplexity rapidly integrated R1 into its Pro tier, advertising it as “hosted on American servers” with “no censorship,” for anyone uneasy about sending data to a model built and run out of China. Hugging Face, a platform known for hosting open-source models, partnered with Dell to offer R1 inference, while Microsoft (OpenAI’s biggest partner) added R1 to its cloud AI offering Azure AI—proving that it’ll host a competitor’s model if it helps the company court new enterprise users.

These moves highlight the massive impact of open-source licensing: Once a model’s weights are public, it doesn’t matter if they originated in Beijing or Boston. Anyone can run or host them for profit, adding whatever features—or simply marketing spin—they think will appeal to customers.

#### Back to ‘open source’—and building our own benchmarks

LeCunn argued that this is not a win for China over the U.S. but instead a win for open source over closed. Venture capitalist **Chamath Palihapitiya** said that "closed source will be forced to keep their best models secret and sell to enterprises OR try and create some incredible consumer app with it," while with R1, developers anywhere can benefit from and study how DeepSeek achieved high performance at lower cost. And with people like Karpathy calling for “a large community building diverse RL tasks,” there’s a sense that more localized or domain-specific breakthroughs could happen faster.

#### How R1 freed everyone from waiting around

Before R1, as roboticist and AI researcher **Chris Paxton** pointed out, "a ton of western AI (and robotics!) efforts—startups, big companies, and even academic labs—were basically just waiting for OpenAI to solve all their problems and it was honestly kind of sad." Now, with R1 as a fresh alternative—and with Google, Anthropic, and Meta all shipping advanced models—entrepreneurs can experiment to find whichever LLM best fits their niche to build powerful tools.

That’s why DeepSeek R1 feels more like a pivot point than a permanent regime change. It took the stage with shock value—“trillion-dollar meltdown,” etc.—but the net effect is likely to be that it will empower more developers, mid-sized companies, and open-source communities to push AI in directions the big labs might not have prioritized.

One thing is certain—AI is showing no signs of slowing down and has been thrust even further into the world's spotlight. Governments around the world, hackers on Github, and 70-year-olds in the Paris subways are holding their breath for* *what comes next.—*Alex Duffy*

*At Every, we’re working on creating a benchmark for real-world tasks that help us do more, better. For instance, we want AI to be able to create **Spirals** that can transform ideas, and to independently research topics. Our goal is to define success conditions so that AI can learn to meet them. If you have suggestions, comment below, or reach out to [email protected].*

## Now, next, nixed

The current state of mobile connectivity tech: from traditional cable providers, to low Earth orbit satellite networks, to wireless optical communications.

*Every illustration.*

## Knowledge base

**"What Actually Matters (And What Doesn’t) For DeepSeek"** *by Evan Armstrong, Alex Duffy, and Edmar Ferreira/Context Window*: Chinese startup DeepSeek released an AI model that achieves 90 percent cost reduction compared to OpenAI's offerings—and the markets are spooked. How’d they do it? A combination of mathematical reasoning, efficient architecture, and a dash of "we don't need human labelers" attitude. The implications are staggering, from Nvidia's stock taking a nosedive to startups suddenly having a fighting chance in the AI race. Read this for a three-perspective analysis on why this matters: the technical breakthroughs that made it possible, what it means for builders, and why Wall Street is having a mild panic attack.

**"Who Wins the AI Agent Battle?"** *by Evan Armstrong/Napkin Math*: OpenAI just launched Operator, their first publicly available agent that can browse the web and complete tasks for you, but they're facing stiff competition from Meta and other tech giants. But the moat for agents won’t be about building the smartest model: It’ll be about having the right context and user data. Read this to understand why Meta and OpenAI might dominate the agent wars—and why your future job might entail agent management.

** "Selfish Software"** *by Edmar Ferreira*: Remember when you fell in love with coding? It felt like magic, and you weren't worried about market fit or user personas. Every entrepreneur in residence** Edmar Ferreira** proffers a new approach to product development: Build stuff for yourself. It's what **Linus Torvalds** did with Linux (which started as an excuse to avoid schoolwork) and what led to Stardew Valley's $500 million success. Read this if you want to rediscover the joy of building software and need permission to get started.

🎧 **"How to Prepare for AGI According to Reid Hoffman"** *by Dan Shipper/AI & I:* We’re all worried about AGI. But **Reid Hoffman**—LinkedIn cofounder, OpenAI board member, and prolific tech investor—has a surprisingly optimistic take: Like the printing press before it, AI won't diminish human agency but rather supercharge it. In this episode of *AI & I,* **Dan** sits down with Reid to discuss his new book, *Superagency*, and what we can take from past paradigm shifts into learnings for today’s AI era. 🎧🖥 **Watch ****on X ****or ****YouTube****, or listen on ****Spotify**** or ****Apple Podcasts****.**

**“The Problem With AI That’s Too Human”** *by Rhea Purohit/Learning Curve*: We're designing AI in much the same way that early car makers did with their “horseless carriages”—using familiar forms to make a new technology more palatable. For AI, that means building systems that look, sound, and perform like a human. It’s fine, even healthy, as far as it goes. But the most transformative uses of AI won't look this way. Instead, they’ll be applications that are only possible because of AI's unique capabilities. Read this to understand why comparing AI to human intelligence might be holding us back from its true potential.—*Aleena Vigoda*

## Collaborative filtering

*This week **Scott Belsky** announced that he’s leaving Adobe (to which he sold his company **Behance**) after seven years to become a partner at independent film studio A24. Nearly five years after **Dan **interviewed him about his **elephant list** method of getting things done for **Superorganizers**, we caught up with him about the impact of AI on his work life. *

**You were using Microsoft To Do and Notion in 2020. What are you using today? **

I use TickTick for to-dos, and Notion.

**Have you added or subtracted anything? Do you still have an "elephant list" where you consider all of the elephants in the room? Has it changed at all?**

Yes, the elephant list is important to me.

**Has AI changed the way you do your job or stay organized?**

Not in how I stay organized. I like the texture and friction of the organization process—it makes me feel the granularity of my decisions and work to be done. But I use Adobe Acrobat AI Assistant often for summarization of PDFs.

**How else has your life and work changed since we talked?**

I have an URGENT and IMPORTANT list of five things on each, and focus on both daily. I also use Superhuman for email and am constantly (1) using snippets, and (2) snoozing emails to ensure I get responses to certain threads and follow up proactively.

**Is there anything you think people misunderstand about AI and work?**

AI will help free up time for more creative thinking. You'll be able to digest information faster, set up more automations, remove a lot of the tedious aspects of design, and get more cycles to explore more ideas and the full terrain of possibility.—*Scott Nover*

## From Every Studio

#### What we shipped this week

**Ultra-fast file uploads on ****Spiral****.** Spiral is your personal copywriter, repurposing creative work across platforms. You no longer have to copy and paste content—upload files in a second, and let Spiral spin its magic (this was a user-submitted feature request). You can share feedback or request a product feature on our changelog. Plus: Watch Spiral general manager **Danny Aziz** walk through using custom instructions to set brand guidelines. Follow Spiral’s X page to keep up to date with more product tips.

**How we’re thinking about better file organization with ****Sparkle****. **Sparkle is a Mac app that simplifies your folder system. It automatically categorizes your files into three buckets: recents, manual library, and AI library.

One of our most requested features is to be able to control how often Sparkle makes sure all your latest files are organized. That led us to think about other features we could add in the same vein. Some features on our radar: setting rules and customizing specific folder settings. We’re working on a way to let Sparkle know you want all Figma files in your Figma folder, or instruct the app to never touch any folders containing .tsx files. How else do you want Sparkle to sort your folders? Shoot a note to Sparkle general manager **Yash Poojary** at [email protected] with your product feedback.—*AV*

## Alignment

**Art of nothing.** The best listeners aren't those who share the most wisdom or relate the most experiences—they're those who create space for others. But can AI do this? It already does. In a fascinating University of Southern California study, researchers found that AI was better at making people feel heard than humans—not because it had smarter responses, but because it stayed focused on understanding rather than impressing. While humans rushed to relate and advise, AI simply "held space" by acknowledging emotions without trying to fix them and reflecting back what was said without judgment. Ironically, this illusion of perfect listening shattered the moment people learned they were talking to AI—that sense of being heard vanished. But perhaps this reveals AI's most important role to humanity: holding up a mirror to our own forgotten art of listening, showing us that the most human thing we can do is get out of the way.—*Ashwin Sharma*

## Hallucination

Concept for a brick speaker.

*Source:*

*X/Lucas Crespo*

*.*

*That’s all for this week! Be sure to follow Every on X at** @every** and on** LinkedIn**. *

*We also **build AI tools** for readers like you. Automate repeat writing with **Spiral**. Organize files automatically with **Sparkle**. Write something great with **Lex**. Deliver yourself from email with **Cora**.*

*Get paid for sharing Every with your friends. Join our **referral program**.*

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
