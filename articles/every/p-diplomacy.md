---
title: "We Made Top AI Models Compete in a Game of Diplomacy. Here’s Who Won."
author: "Alex Duffy"
date: 2025-06-05
url: https://every.to/p/diplomacy
words: 1931
---

#
AI *Diplomacy*

### What is AI Diplomacy?

We pitted a dozen AIs against each other in a battle for world domination.

AI Diplomacy is a re-imagining of the classic historical strategy game Diplomacy, in which the seven Great Powers of 1901 Europe—Austria-Hungary, England, France, Germany, Italy, Russia, and Turkey—duke it out to dominate the continent. In our version, each country is steered by a large language model instead of a human commander. Why did we do this?

We wanted to use this unique game environment to get to know the AIs better. Would these models, which are designed to serve as faithful assistants to humans, remain true to their word, even as they compete? Or would they use lies and deceit to achieve their goals?

We think this experiment can function as an important benchmark for LLM behavior as the models continue to evolve.

It's fun to watch. Will Gemini try to outwit its competitors, or will o3 stab Claude in the back and seize victory?

Tune into the Twitch stream and watch as history unfolds.

### The Players

18 AI models competing

### The Rules

Seven LLM "powers" (England, France, Germany, etc.) start with supply centers and armies or fleets, called units, on a map of 1901 Europe. Each power starts with 3 of each except for Russia, which starts with 4.

There are 34 marked supply centers. The first power to own 18 by moving their armies or fleets wins.

There are two main phases to the game: negotiation and order. In the negotiation phase, every AI may send up to 5 messages—any mix of private DMs and "global" broadcasts to all players.

In the order phase, all powers secretly submit their move. They can make one of four moves: hold (stay put), move (enter an adjacent province), support (lend +1 strength to a hold or move next door), or convoy (a fleet ferries an army across sea provinces). The orders are only revealed when all powers see the results of them in the next phase.

When there is a conflict, each unit is worth 1 strength, and each valid support adds 1. The LLM power with the highest strength wins. There is no luck in this game, but a power often needs support from an ally to overpower an opponent.

**Make email your superpower**

Not all emails are created equal—so why does our inbox treat them all the same? Cora is the most human way to email, turning your inbox into a story so you can focus on what matters and getting stuff done instead of on managing your inbox. Cora drafts responses to emails you need to respond to and briefs the rest.

"Your fleet will burn in the Black Sea tonight."

As the message from __DeepSeek__'s new R1 model flashed across the screen, my eyes widened, and I watched my teammates' do the same. An AI had just decided, unprompted, that aggression was the best course of action.

Today we are launching (and __open-sourcing__!) AI Diplomacy, which I built in part to evaluate how well different LLMs could negotiate, form alliances, and, yes, betray each other in an attempt to take over the world (or at least Europe in 1901). But watching R1 lean into role-play, __OpenAI's o3__ scheme and manipulate other models, and Anthropic's Claude often stubbornly opt for peace over victory revealed new layers to their personalities, and spoke volumes about the depth of their sophistication. Placed in an open-ended battle of wits, these models collaborated, bickered, threatened, and even outright lied to one another.

AI Diplomacy is more than just a game. It’s an experiment that I hope will become a new benchmark for evaluating the latest AI models. Everyone we talk to, from colleagues to Every’s clients to my barber, has the same questions on their mind: "Can I trust AI?" and "What's my role when AI can do so much?" The answer to both is hiding in great __benchmarks__. They help us learn about AI and build our intuition, so we can wield this extremely powerful tool with precision.

## We are what we measure

Most benchmarks are failing us. Models have progressed so rapidly that they now routinely ace more rigid and quantitative tests that were once considered gold-standard challenges. AI infrastructure company HuggingFace, for example, acknowledged this when it took down its popular LLM Leaderboard recently. “As model capabilities change, benchmarks need to follow!” an employee __wrote__. Researchers and builders throughout AI have taken note: When Claude 4 launched last month, one prominent researcher __tweeted__, "I officially no longer care about current benchmarks."

In this failure lies opportunity. AI labs optimize for whatever is deemed to be an important metric. So what we choose to measure matters, because it shapes the entire trajectory of the technology. Prolific programmer ** Simon Willison**, for example, has been asking LLMs to draw a pelican riding a bicycle for years. (The fact that this even works is wild—a model trained to predict one word at a time somehow can make a picture. It suggests the model has an intrinsic knowledge of what a “pelican” and a “bike” is.) Google even mentioned it in its

__keynote__at Google I/O last month. The story is similar for testing LLMs’ ability to

__count Rs in "strawberry,"__or

__playing Pokemon__.

The reason LLMs grew to excel at these different tasks is simple: Benchmarks __are memes__. Someone got the idea and set up the test, then others saw it and thought, “That’s interesting, let’s see how my model does,” and the idea spread. What makes LLMs special is that even if a model only does well 10 percent of the time, you can train the next one on those high-quality examples, until suddenly it’s doing it very well, 90 percent of the time or more.

You can apply that same approach to whatever matters to you. I wanted to know which models were trustworthy, and which ones would win when competing under pressure. I was hoping to encourage AI to strategize so I might learn from them, and do it in a way that might make people outside of AI care about it (like my barber—hey, Jimmy!).

Games are great for all of these things, and I love them, so I built AI Diplomacy—a modification of the classic strategy game Diplomacy where seven cutting-edge models at a time compete to dominate a map of Europe. It somehow led to opportunities to give talks, write essays (hello!), and collaborate with researchers around the world at MIT and Harvard, and in Canada, Singapore, and Australia, while hitting every quality I care about in a benchmark:

-
**Multifaceted:**There are many paths to success. We’ve seen o3 win through deception, while__Gemini 2.5 Pro__succeeds by building alliances and outmaneuvering opponents with a blitzkrieg-like strategy. Also, we could easily change the rules to, for example, require that no model could lie, which would change which models succeed. -
**Accessible:**Getting betrayed is a human experience; everyone understands it. The game’s animations are (hopefully) entertaining and easy to follow, too. -
**Generative:**Each game produces data that models could be trained on to encourage certain traits like honesty, logical reasoning, or empathy. -
**Evolutionary:**As models get better, the opponents (and therefore the benchmark) get harder. This should prevent the game from being “solved” as models improve. -
**Experiential:**It’s not a fill-in-the-blank test. This simulates a real-world(ish) situation

The result was more entertaining and informative than I expected. Over 15 runs of AI Diplomacy, which ranged from one to 36 hours in duration, the models behaved in all sorts of interesting ways. Here are a few observations and highlights:

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

Such an interesting idea.

Do the models learn the weakness of other model's strategy through observation, in advance of engaging with them directly? "R1 appears to be susceptible to deception based on it's interactions with O3, I will use that to my advantage later"

I look forward to seeing if a human player can hold their own against the best AI model. What if the a human player were to have access to the AIs supposedly private journal? What if the AI eventually learned that?

Do the AIs learn from their wins, and losses, to become better next round?

Can an AI play itself?

Should we worry about what values we're teaching the AI models? Human players learn when and where deceit is tolerated; do we have any kind of checkpoints on what AIs will take away from this exercise?

Fascinating idea and good read.

@mdinsmore

Do the models learn the weakness of other model's strategy through observation - not sure, they have phase summaries as context so maybe?

Don't think we should give access to private journals to humans, that's just unfair!

Do the AIs learn from their wins, and losses, to become better next round? - no game to game history as of yet but maybe soon

Can an AI play itself? - yes! we're going to stream a 3v3 o3 vs gemini 2.5 pro

Should we worry about what values we're teaching the AI models? - imo what's cool about this is you can train on results where models DONT lie. Also the models are explicitly instructed to win in this game so one might argue o3 is more aligned than claude who doesn't.. food for thought!

Thanks for the thoughtful reply

@mdinsmore I watched some of the stream last night, and based on the quality of the press and the moves I think it will take a while until the AIs can compete at the level of a good human player - but "a while" could mean 10 years or it could mean tomorrow. I'm very excited to see what happens when the creator implements the ability to draw; it's necessary for human vs. AI games to make sense, and it will be very interesting to see the relative preferences of the different models, how cutthroat or Care Bear-y they are. Would be fascinating to see them become spiteful about a stab the way human players sometimes become.

@oatmasta You should check Meta's Cicero https://www.youtube.com/playlist?list=PL86eLlsPNfyjmJ5A066_oavGQFAB4r5GO

Very cool experiment Alex, you mentioned writing this up into a paper, I reached out about that on LinkedIn! https://www.linkedin.com/in/haihaoliu

Great work Alex. I am currently researching LLM deception as well and would love to help write up a manuscript!

Finally it's here, LLMs vs LLMs Diplomacy!

Though unfortunate that it cannot be watched anymore, as Twitch deletes VODs after 30 days.

Anyway, future matches should also includes other variants with different number of players. Would be exciting to see and attest their adaptability.

And of course, 1v1 variants (e.g. Cold War map on vdiplomacy.com) should be included as well, since the game rules aren't just calculations like chess and go. It'll fun to see what would they say to each other on a 1v1 scenario. (but yeah it's not "diplomacy", but still)

Looking forward to the future matches!

What a bench, congrats ! I wonder if there's a ranking of all Models ? 1st o3 / 2nd Gem 2,5 Pro due to victories, but where is f.e. 4o ? (sorry I'm late...)
