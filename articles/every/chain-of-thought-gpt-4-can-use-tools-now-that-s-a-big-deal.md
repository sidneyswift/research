---
title: "GPT-4 Can Use Tools Now—That’s a Big Deal"
author: "Dan Shipper"
date: 2023-06-15
url: https://every.to/chain-of-thought/gpt-4-can-use-tools-now-that-s-a-big-deal
words: 888
---

#### Sponsored By: Brilliant

This article is brought to you by Brilliant, the best way to future-proof your mind through interactive lessons on everything from logic and math to data science, programming, and beyond.

Human children come out of the womb totally helpless except in one important way: they know how to use their parents as tools.

Infant tool use is quite blunt at first: they cry loudly and incessantly whenever there’s a problem: “HUNGRY”, DIRTYY DIAPER!!!!”, “TIREEDDD!!!!”, and so on. They keep crying until their parent adequately diagnoses and resolves the issue through trial and error.

As they get older, however, children ditch these crude initial methods and instead use language to skillfully manipulate their parents in ever more targeted and precise ways. Rather than simply becoming totally unconsolable because they see someone eating a cookie and want one for themselves they can now specify in precise language exactly what they want: “Can I have a cookie?”. Parents can then use their unique capabilities—the ability to walk, their height differential, their manual dexterity, and strength—to walk to the cookie jar, open it, select a cookie, and appropriately offer it up as tribute. This kind of tool use is a powerful method for intelligent beings with significant limitations to accomplish goals in the world.

In contrast to human children, large language models like GPT-4 were not created knowing how to use tools to accomplish their aims. This limited their capabilities significantly. Third-party libraries tried to implement this functionality—but the results were often slow and inconsistent.

Earlier this week, OpenAI built tool use right into the GPT API with an update called *function calling. *It’s a little like a child’s ability to ask their parents to help them with a task that they know they can’t do on their own. Except in this case, instead of parents, GPT can call out to external code, databases, or other APIs when it needs to.

Each function in *function calling* represents a tool that a GPT model can use when necessary, and GPT gets to decide which ones it wants to use and when. This instantly upgrades GPT capabilities—not because it can now do every task perfectly—but because it now knows how to ask for what it wants and get it.

Function calling works like this:

When you query a GPT model you can now send along with it a set of tools that the model can use if it needs to. For each tool you can specify a description of its capabilities (do math, call a SQL database, launch nuclear bombs) and instructions for how GPT can properly call each one if it wants to. Depending on the query, GPT can choose to respond directly, or instead request to use a tool. If GPT sends back a request to use a tool your code calls the tool and sends back the results to GPT for further processing, if necessary.

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

Hey Dan, I'm really enjoying your AI posts, thanks for putting them together. I'm a copywriter, so particularly interested in how to get ahead of the game and understand how large language models are going to impact things. I'm not thinking about blogs and website copy though, as I think that sort of writing can clearly be handled by AI already to a degree. It's more for higher level brand copy, where nuance is everything - capturing a vision, positioning statement or key messages in a fistful of words. My experiments so far have just produced very generic stuff. Have you any thoughts on this, or know where this sort of thing is being discussed?

@jontysignup hey!! great question. have you used Claude from Anthropic? it's a bit better at writing. also, I'm planning to write about this next week but these models might not be very good yet at writing key messages but they are very good at taking lots of complex inputs and summarizing them. i think this is helpful for brand / copywriting because it can help you easily take a bunch of examples (say of other products or websites that a client likes) and put into words what they have in common. e.g. they're really good for helping to articulate a taste or a vibe—which is a great first step for the use case you're talking about. hope that helps!

@danshipper Not tried Claude but will give it a spin. Be really interested to hear your take on this topic and yeah, it feels like the summarising side of things, rather than finished-product writing, is perhaps where it’s at. A strategist I work with also has an interesting thought on this: taking the transcript from a client’s (often badly articulated) brief, running that through AI, and perhaps getting something clearer that could be mutually signed off as a direction. Avoiding some of the ‘that’s not what I asked for’ back-and-forth
