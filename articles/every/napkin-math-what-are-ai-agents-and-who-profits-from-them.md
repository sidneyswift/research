---
title: "What Are AI Agents—And Who Profits From Them?"
author: "Evan Armstrong"
date: 2024-03-28
url: https://every.to/napkin-math/what-are-ai-agents-and-who-profits-from-them
words: 1830
---

Most races have a prize pool. The New York City marathon winner gets $100,000. 2023’s F1 winner took home a $140 million pot.

The winner of the race I’m going to describe will earn billions. Maybe tens of billions. They’ll bend the arc of the universe. They’ll materially increase GDP.

This is the race toward the AI agent. Agents are the next step in the AI race and the focus of every major tech company, research lab, and leading AI startup.

I’ve spent months talking with founders, investors, and scientists, trying to understand what this technology is and who the players are. Today, I’m going to share my findings. I’ll cover:

- What an AI agent is
- The major players
- The technical bets
- The future

Let’s get into it.

## What is an agentic workflow?

An AI agent is a type of model architecture that enables a new kind of workflow.

The AI we started with formulates an answer and returns it. Ask it something simple, like “Does an umbrella block the rain?” and GPT-4 returns the answer, “Of course it does, you dumbass.” The large language model is able to answer the question without relying on external data by using internal data and executes on the prompt without a plan. It's a straightforward line connecting input and output. And every time you want a new output, you have to provide a prompt.

Agentic workflows are *loops*—they can run many times in a row without needing a human involved for each step in the task. A language model will make a plan based on your prompt, utilize tools like a web browser to execute on that plan, ask itself if that answer is right, and close the loop by getting back to you with that answer. If you ask, “What is the weather in Boston for the next seven days, and will I need to pack an umbrella?” the agentic workflow would form a plan, use a web browsing tool to check the weather, and use its existing corpus of knowledge to know that if it is raining, you would need an umbrella. Then, it would check if its answers are right and, finally, say, “It’ll be raining (like it always does in Boston, you dumbass) so yes, pack an umbrella.”

What makes agentic workflows so powerful is that because there are multiple steps to accomplish the task, you can optimize each step to be more performative. Perhaps it is faster and/or cheaper to have one model do the planning, while smaller, more specialized models do each sub-task contained within the plan—or maybe you can build specialized tools to incorporate into the workflow. You get the idea.

But agentic workflows are an architecture, not a product. It gets even more complicated when you incorporate agents into products that customers will buy.

## Solving users problems > flashy demos

The only thing that matters in startups is solving customers’ problems. Agentic workflows are only useful as a product if they solve problems better than existing models. The tricky thing is that no one knows how to make AI agents a consistently better product right now. The pieces are all there, but no one has figured out how to put them all together.

This moment is strongly reminiscent of the early 1980s of personal computing, when Apple, Hewlett-Packard, and IBM were duking it out. They all had similar ideas about the user interface (the use of a mouse, the need to display applications, etc.), but the details of implementation were closely guarded secrets. These companies competed on the quality of their technical components and how each of those components fit together to solve customer problems.

Companies that make AI agents are also competing on both individual component quality and how these components are combined. In broad strokes, think of these arenas of competitive intensity scattered across five components:

*Every illustration.*

-
**Data inputs**: The agent needs access to unique data sets or be better able to parse public data sets (such as scraping the web). Where does the agent draw its data from? Can it access internal data repositories—note-taking systems for individuals or corporate knowledge bases for enterprise use cases—to make answers better? -
**Models:**For the past year, when you heard “AI” it typically meant this component—the large language models (LLMs) like GPT-4. Within the model companies like OpenAI, there are a variety of approaches that I’ll cover in a minute. -
**Tools:**Think of these like giving the handyman (an LLM) a new set of screwdrivers. This is an area I’m excited about. In 2023, I used a tool from OpenAI called Code Interpreter that has been able to replace many finance workflows. Code Interpreter provides the LLM with a coding environment that allows the LLM to modify spreadsheets. -
**Interface**: Knowing how to integrate these capabilities into a user’s workflow is just as important as—if not more than—what the agent can actually do. Is the agent nestled within a typical LLM chatbot? Is it operating behind the scenes as part of an application's code? Does the AI need to be in its own separate UI and app? Or should it be integrated into an existing workflow app like Salesforce or Excel? -
**AI glue:**This is my own term (you can tell because it sounds dumber than the rest), but in my interviews with founders building AI agent companies, the most common thing I heard was that “AI agents are an engineering problem, not an AI problem.” There is a sense that while each of the previous components is important, what matters is figuring out how to stick them all together. Glue is traditional, deterministic software that programs a set of logical steps.

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

I work in an industry (integrity/enhanced due diligence) which is absolutely ripe for this type of AI agent takeover. I think the first company that manages to nail the "ai glue" element will basically kill off our entire industry (or at least 90% + of it) immediately. There are two types of main EDD/IDD work currently being done; the base, KYC/compliance work that is a regulatory requirement in a lot of jurisdictions and sectors, and the more reputational DD, which is usually more complex and is in support of some sort of transaction and investment, therefore going beyond just fulfilling a regulatory requirement.

LLMs are already adept at learning to mimic writing styles and at canvassing large amounts of information. Every firm in our sector keeps every past EDD/IDD report on file (for our small firm it's thousands and thousands of reports, a bigger firm like Kroll will have many more), so the model would have a huge amount of existing internal data to pick through, learning the house style, structure of reports etc. I don't think it will take too long before you have an AI that can go through large amounts of data online (google results, database search results either manually or through APIs, etc) and use its training on identifying relevant results, conducting "fuzzy searches", and analysing the results. Once you have that, having another AI agent which would write the report based off the existing internal repository of reports (most companies have a house style and structure of report) is also likely not very far away.

So basically "all you need" is that ai glue. To give you an idea, reports have at minimum a 2-3 working day TAT and the cheapest reports that have human analyst input cost thousands of dollars. An AI would write this in minutes, with commensurate savings in costs. Almost all EDD/IDD reports are a pure cost to the client and they are currently used to these TATs and costs... If you were the first firm on the market and your product actually worked, you would basically be unassailable on efficiency and cost (because the marginal gain of minutes, or a couple hundred dollars on an EDD report, is irrelevant to all but the absolute largest global bank's compliance team), and it would not be entirely clear whether the additional investment from competitors on making a tool that would provide marginally "better" (more detailed, even more accurate) reports would be worth it.

In fact, it would be interesting to see just how nuts the disruption around professional services firms would be. Already the largest corporate law firms are experimenting with AI to conduct doc review, which alone is like millions of billable hours a year.

@pierre.lejeune Yea this seems like a perfect use case. A lot of it will also depend on context window size (Dan has written about that if you're interested) and RAG. Basically how does the model train and access internal data. But for the use case you're describing—sounds like most of that is doable by AI right now. If you're fast you just invented a nice multi-million dollar business for yourself :)

Great article. Just like the term "AI", "AI agent" is overloaded and everyone seems to have a slightly different definition for it. Yours is as accurate as it can be as of today, in my opinion.

One comment on "Last year Anthropic told its investors it was preparing to create a model 10 times better than GPT-4". I can't recall exactly when they made this claim (about a year ago?) but am pretty sure they've already missed the mark on it. Claude 3 is arguably better, but not by much. We're seeing diminishing returns on "mega" LLMs (1T+ parameters) and scaling itself won't continue to yield proportional gains. Just as the auto industry started scaling down engine sizes in the 70s (while boosting efficiency), we now need to come up with smaller and "smarter" model architectures. That, or something akin of nuclear fusion 😬

@leo_5051 Maybe! If you include time for training, red-teaming, and prepping for product launch, Claude 3 would've been timed around then. This Claude-Next should be created now.

Your sentiment isn't wrong (and is I think a popular one) but I'm not willing dismiss the benefits of scale quite yet.

Good point. I'm not saying there are no gains to be made with additional scaling or that LLMs won't get bigger. I guess I'm hoping the trend reverses soon so the AI rush (which I'm very excited about) doesn't become an environmental catastrophe.

Sorry for the naive question...are the agents you are referring to the same as GPTs? I don't hear much about GPTs since the initial announcement, so I am curious as I continue to learn AI and applications.
