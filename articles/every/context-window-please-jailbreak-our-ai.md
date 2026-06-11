---
title: "Please Jailbreak Our AI"
author: ""
date: 2025-02-09
url: https://every.to/context-window/please-jailbreak-our-ai
words: 2753
---

# Please Jailbreak Our AI

Plus: OpenAI and Google go ‘deep’

February 9, 2025 Updated December 17, 2025

*Hello, and happy Sunday! This week, a major AI company is challenging hackers to jailbreak its model’s nifty new protections. **Alex Duffy** breaks down this and much more news in AI. *

*Also, it’s the last chance to register for our course **How to Write With AI**. Taught by Every lead writer **Evan Armstrong**, the next cohort starts on February 13. Join corporate leaders, venture capitalists, and software engineers and **reserve your spot**.—**Kate Lee*

*Was this newsletter forwarded to you?** Sign up** to get it in your inbox.*

## Release notes

### Research agents, model security, and cheaper AI

This jam-packed week in AI started on Sunday evening with the release of OpenAI’s new “deep research” tool—an agent that scours the web, cross-references documents, and spits out impressively detailed reports. Then, mid-week, Anthropic threw down a $30,000 jailbreak bounty for anyone who could crack its “Constitutional Classifiers” system designed to prevent harmful outputs, and Google expanded its Gemini 2 lineup with cheaper, large context-length models.

We’ll dig into why deep research is drawing so much buzz (and skepticism), how open-source alternatives have sprung up for those balking at the Pro price, and the latest updates on AI safety. Finally, we’ll check out Google’s ultra-budget approach to large language models, and share two deep-dive resources from masters** Andrej Karpathy** and the researchers at Google DeepMind if you want to roll up your sleeves and understand how these systems actually work.

#### OpenAI’s deep research: Is this the agentic future?

*Source:*

*X/Siqi Chen*

*.*

OpenAI unveiled what might be the best AI agent on the market: deep research (not to be confused by the Google product of the same name, which we’ll discuss in a moment). It’s a multi-step tool that crawls the web, plucks relevant data, and merges it all into a polished report. Think of it as a personal, virtual research team that can power through PDFs, articles, and references in minutes. In fact, according to Runway founder **Siqi Chen,** it can exceed the value of a $150,000 research team.

-
**Why it matters:**It’s a taste of where AI is heading—more autonomy, more long-term planning, more data, and more thorough results. AI is better at coalescing oceans of data into a useful report than humans. Some users feel it can even surpass professors on a subject. -
**Beware of hallucinations:**Deep research still slips up on accuracy at times, and it does not have access to all sources like paywalled academic journals that house new cutting edge research (though that might change, according to OpenAI CEO**Sam Altman**). And while it’s great at consolidating information, it’s not an expert at discovering something new (yet).

If you need to survey a complex topic fast, deep research is a game changer. Just remember to double-check citations—and brace for a hefty response to read.

#### Google's Deep Research and other alternatives

If you’re hesitant to spring for the $200 ChatGPT Pro subscription, multiple teams have alternatives or rushed to create agentic research tools of their own in response to deep research—some free, some open-source, and all more budget-friendly.

-
**The easiest alternative:**Using OpenAI’s new free model o3-mini (freshly updated with more transparent reasoning) with search on chatGPT.com or chat.deepseek.com, you can use a thinking model with search. With multi-step searching and summarizing your result will be good but not nearly as detailed as with deep research. But it’s great for quicker questions. -
**Google’s****"Deep Research"**: Google released its own Deep Research feature in December within Gemini Advanced—which comes with a one-month free trial. The performance is solid, though not nearly as in depth or eloquent as OpenAI’s, which provides Ph.D.-level reports. I wish Google’s Deep Research asked follow-up questions. -
**Roll your own:**Open-source developers have mashed up cheaper LLMs (like o3-mini) with search APIs, letting them loop through web queries, read docs, and build a final answer. It’s a DIY spin on the same concept. Efforts from two AI research teams at HuggingFace and Jina.ai are particularly full-featured, and the browser automation project Browser Use UI added a deep research feature.

Agentic research won’t stay exclusive for long. There’s a near-future where anyone can access an “AI research sidekick” for little to no cost—which will inevitably be used both for positive discoveries as well as nefarious purposes.

#### Security and jailbreak wars—Anthropic’s bounty, Pliny’s exploits

As research agents get stronger, the risks of them spouting harmful or private information increase. Leading labs are stress-testing models in public so they’re safer once widely deployed, but upstart competitors like DeepSeek are not prioritizing the same. This week both Anthropic and Google emphasized the following points:

*Source:*

*Claude’s Constitutional Classifier*

*.*

-
**Anthropic’s $30,000 challenge:**The company released a “Constitutional Classifier” for its Claude model and promised bounties for anyone who can truly break it. The aim? Crowdsource solutions to tricky jailbreak prompts before bad actors figure them out. -
**Pliny’s partial victory:**A prolific pseudonymous jailbreak tinkerer named Pliny the Liberator passed the first few levels (pictured above) by convincing the language model to divulge information it was instructed not to, before finding an exploit in the interface to skip the rest of them. Anthropic dismissed it as a minor hack and encouraged Pliny to try to legitimately solve the challenge, which was met by unmet demands to open-source the data gathered in this experiment in exchange. -
**Industry stance:**Google shared their findings attempts to misuse its Gemini models focusing on two big ones: -
**Advanced Persistent Threat (APT):**Government-backed hacking like cyber espionage and destructive computer network attacks. -
**Information Operations (IO):**Attempts to influence online audiences in a deceptive, coordinated manner like sock puppet accounts and comment brigading.

There has not been a major security incident in part because not many bad actors are using Gemini yet, but there are plenty of small cracks to patch. APT actors using Gemini to support their attacks with research, reconnaissance, and development. The cat-and-mouse continues.

The more powerful these models become, the bigger the ramifications of AI safety research. The push and pull between speed of progress with safety will be a recurring theme to track this upcoming year and into the future.

#### Google’s Gemini 2: Cheap, fast, and good enough

In addition to sharing information on adversarial misuse, Google expanded its Gemini 2 lineup—which powers its AI assistant app Gemini Advanced and its other AI tools—with the release of the extremely cost-effective Flash 2.0 and larger base model Gemini 2.0 Pro.

Flash 2.0 stole the show. It isn’t the absolute best in terms of the quality, but it's an impressive bang for the buck: It performs as well as GPT-4o at around 60 percent of the cost of GPT-4o mini. It also has a huge context window of *1 million tokens*: You can give Gemini Flash 2.0 all seven *Harry Potter* books (about 1 million words) as context before asking it to create a new adventure featuring your daughter as a bed-time story.

Gemini 2.0 Pro is more of a mixed bag. It is not topping the charts for any benchmarks, but there have been claims of great coding abilities, especially because it boasts an enormous *2 million-token*** **context window. While it is not setting the standard for performance among models and or a currently-in-vogue reasoning model, Google clearly believes “it’s [a] critical path to keep pushing the frontier of pre-trained models,” said Google AI Studio product lead **Logan Kilpatrick**.

This kind of cheap “good-enough” intelligence is a sweet spot for many real-world applications, like understanding PDFs (it can analyze 6,000 pages for $1), deciding if a user request can be answered or routed to a human, and analyzing data. Prices are dropping and capabilities are rising—with the result that more people can integrate AI into daily workflows.

#### What cheap AI means for businesses

The real revolution might be “AI for the masses at scale.” It’s increasingly clear that it seems to be worth building with the assumption that access to intelligence will continue to rapidly decline in cost, similar to that of computer memory and storage over the past 50 years. Each time the price of intelligence drops, it opens up a new opportunity for tools to be built. As AI makes smart work cheap, a solo entrepreneur can wield the cognitive firepower of an entire corporation, turning a modest venture into a high-margin powerhouse. If AI code editor Cursor is any indication as “the fastest-growing SaaS company of all time”—going from $1 million to $100 million in annual recurring revenue in roughly 12 months—there are massive opportunities across industries. With the cost of executing on ideas decreasing, the future belongs to people with great ideas who can just do things.

*Source:*

*Sacra.com*

*.*

#### Resources to level up how you use AI

Anyone can now tap into AI for specialized research, coding help, or analyzing huge datasets. The next wave of innovation will come from people outside the AI bubble—those who have real-world problems and see these tools as leverage to solve them.

Try deep research if you can; we wrote an in-depth piece on why you should. If that’s out of range for you, you can spin up a free trial of Gemini Advanced for an idea of the state of the art. Watch it pull together data you would’ve spent hours scouring for on your own.

#### Nerdcore media corner

If you’d like to go deep, here are two new pieces of content that’ll provide you with a deep understanding of the complexity behind advanced AI models:

- Andrej Karpathy’s LLM deep dive. Another brilliant, down-to-earth overview from one of the brightest minds in AI, this time explaining how large language models work. Karpathy covers data collection, attention mechanisms, and decoding. It’s perfect if you’ve ever wondered why GPT-4 seems to “think” the way it does.
- Google DeepMind’s scaling guide. This technical breakdown describes how big models are trained and deployed (think: splitting your model across hundreds of GPUs and TPUs, or tensor processing units). For those familiar with the basics of LLM training, it's a rare glimpse at the state-of-the-art engineering behind everyday AI tools.

These are fairly technical, but their clarity and real-world examples render them pretty accessible—and the more we understand these technologies, the better prepared we will be to use them wisely. As costs keep falling and capabilities keep rising, AI will continue creeping into more aspects of our lives—freeing your time and imagination for bigger, more creative pursuits.*—Alex Duffy*

## Now, next, nixed

The current state of refereeing: from human umpires, to technology-assisted reviews, to fully automated referees.

*Every illustration*.

## Knowledge base

**"We Tried OpenAI’s New Deep Research—Here’s What We Found"** *by Dan Shipper and Alex Duffy/Chain of Thought:* If you ever wished you had a team of researchers at your beck and call, OpenAI is your fairy godmother: Deep research can spend up to 30 minutes autonomously researching any question you throw at it, delivering detailed reports of up to 16,000 words. The Every team got early access and put it through its paces. Read this if you’ve wondered what an AI agent might have to say about planning capsule wardrobes. 🔏 Paid subscribers have access to the results of our deep research tests.

**"Is Founding a Startup Right for You?"** *by Stella Garber*: Five-time founder **Stella Garber** has taken her share of startup punches, and she's here to help you decide if you're truly ready for the founder ring. The fourth in Stella’s series on business frameworks, read this piece if you're contemplating trading your cushy job for the founder lifestyle.

**“How Yancey Strickler ‘Scrolls’ Offline”** *by Scott Nover/Superorganizers*: Kickstarter cofounder **Yancey Strickler** schedules regular "scroll time" with nothing but a 50-foot roll of butcher paper to work through his biggest ideas. It's how he built his new startup, Metalabel, and it might be the antidote to our AI-obsessed world… although he’s coming around to AI. Read this if you’re curious about old-school creativity in an automated reality.

🎧 “**Vercel’s Guillermo Rauch on What Comes After Coding”** *by Dan Shipper/AI & I*: **Guillermo Rauch**—the man behind the code of OpenAI’s website and many more—has a surprising take: Being a pure coder won't cut it anymore. In this episode of *AI & I*, the Vercel CEO talks to **Dan** about why the future belongs to ideators with taste and how specialized AI agents will transform product development. Listen to or watch this if you want to understand how users will become managers in the allocation economy. 🎧🖥 **Watch ****on X ****or ****YouTube****, or listen on ****Spotify**** or ****Apple Podcasts****.**

**"The Vatican Has Some Thoughts on AI"*** by Evan Armstrong/Napkin Math*: **Evan** breaks down the Vatican’s 13,000-word document (with 215 footnotes!) on AI and humanity. Here’s a summary: AI may be smart, but it can’t understand what it means to hold your newborn daughter. Read this for a theological, and thoughtful, take on the AI debate.

**“The Every Bundle Now Includes Cora”** *by Dan Shipper*: Our new email experience, **Cora**, has amassed a 10,000- person waitlist. Now, Every paid subscribers can get it as part of the subscription bundle$20 per month package—along with **Spiral**, **Sparkle**, and **Lex**. Read this for a behind-the-scenes look at how we made Cora affordable, and AI’s role in delivering you to inbox-human.—*Aleena Vigoda*

## From Every Studio

#### What we shipped this week

**Polish your Spirals. **Here’s a tip for our creative automation tool **Spiral**, which simplifies 80 percent of repetitive writing tasks. You can improve your Spirals over time by adding outputs you like to the examples you provide for training. If you *really* like an output, you can add to both examples *and* extraction patterns, which will spiral (pun intended) your favorite outputs back into inputs to keep your copy up to date.

**Get your friends off the Cora waitlist: **In addition to opening up access to our new email experience to all paid Every subscribers, we’re giving you five invitations to share. If you’re still on the fence, here’s what some **Cora** users have been saying:

*“Cora is a life changing product.”—**Avi Flombaum*

*“Email finally feels special.”—**Alex Banks*

*“I’ve tried all these new fangled AI email apps, and the winner, by far, is Cora.”—**Andrew Wilkinson*

*“Cora is the best thing to come to email in a long time, and I am a big email nerd…feels like as big of an email innovation as Mailbox [or] Superhuman.”—**Harris Osserman*

*“Cora gives me a clearer ‘Email Conscience.’”—**Benny Bowden*

*“Anyone have a referral code to Cora?”—**Ted Spare**—AV *

## Alignment

**Nature knows best.** In 1994, while I was still in diapers, **Kevin Kelly** was pretty much writing ChatGPT's blueprint. His book *Out of Control*, which maps out autonomous agents that would evolve and improve themselves like biological organisms, reads less like futurism and more like prophecy. It’s a vision that looks eerily familiar in the age of self-improving language models and AI agents that can (maybe very soon) spawn their own variants. What stood out to me was Kelly's insistence that nature will always be more efficient than our artificial attempts at control. Therefore, the real AI breakthrough won't come from tighter rules and restrictions—it will come when we learn to work with systems that can grow and adapt on their own, just like nature does. The inevitable conclusion: We need guardrails, not handcuffs, for AI development—and for someone who has always argued for tighter regulations for AI safety, this is something I never thought I would say. Thank you, Kevin Kelly, for changing my mind.—*Ashwin Sharma*

## Hallucination

When will we get Starlink for our phones?

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
