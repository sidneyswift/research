---
title: "When Your Vibe Coded App Goes Viral—And Then Goes Down"
author: "Dan Shipper"
date: 2026-03-20
url: https://every.to/chain-of-thought/when-your-vibe-coded-app-goes-viral-and-then-goes-down
words: 1403
---

# When Your Vibe Coded App Goes Viral—And Then Goes Down

Lessons learned when vibe code meets high load

March 20, 2026 Updated May 22, 2026

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

At 4 a.m. on the day after we launched our __agent-native__ document editor, ** Proof**, I watched yet another

__Codex__agent try to revive our server.

Over 4,000 documents had been created since launch, but the app had been mysteriously crashing all day. This left users with crucial documents that they couldn’t access, and me with egg on my face.

I hadn’t slept for almost 24 hours, and all I could do was nervously munch trail mix as Codex investigated yet another bug buried deep in a codebase that I didn’t understand. It felt less like programming and more like being the dumbest participant at a math Olympiad. Needless to say, I was reconsidering my life choices.

Today, almost a week later, Proof is more or less stable. And I’ve learned a lot about both building and launching a purely vibe coded app. Perhaps more importantly, I’ve also learned what happens once that app goes live—and then goes down.

My current opinion is this: If you can vibe code it, you can vibe fix it. You just might not be able to fix it quickly.

Software engineering is changing rapidly as a discipline. The days of typing code into a computer manually seem to be over, and the current conversation on X is around “zero-human startups.” My experience with Proof, though, is a good reality check.

It demonstrates both what is truly possible with vibe coded apps, and where human engineers will continue to be critical now and in the future.

#### Auto-scale AI workloads with ease

Traditional databases struggle with unstructured data, slowing AI workflows. MongoDB natively handles JSON-like, unstructured data, giving you freedom to store, query, and scale diverse datasets—whether text, images, or sensor data—easily and flexibly, without rigid schemas.

## What’s possible at the edge

I’ve been writing about how AI is changing programming __for a few years now__, and my experience with Proof confirms a lot of my thoughts:

**You can vibe code and launch a complex app extremely quickly**

I built Proof on the side while running a company of about two dozen employees.

I first committed code to Proof’s Github repository in early January. Back then, it was a MacOS app. Two and a half weeks ago, I pivoted it to be web-only. The final form that we launched was about 10 days old, and in that time, I’d built a version that was stable enough that it had become a critical internal tool at Every, and was being used by a small cohort of enthusiastic subscribers, too.

The repository now has 1,600 commits—the vast majority from me—over 600 pull requests, and about 140,000 lines of code. To give you a point of comparison, between 2020 and 2024, the median *full-time* developer committed code __417 times per __* year*.

Vibe coding is a new superpower for everyone—but people still underappreciated its importance for CEOs.

**Codex is a powerhouse**

I primarily used OpenAI’s __Codex desktop app__ and __GPT-5.4__ to build Proof. I find GPT-5.4 to be faster, more personable than previous Codex models, and extremely smart. Where other models like Anthropic’s __Opus__ started to fail as my codebase grew, Codex hummed along nicely.

As of this week, Codex also has __subagents__, which lets you hand off work to specialized agents that run in the background. Subagents dramatically accelerated my work. As I was trying to keep our server from going down, I’d have one subagent pushing the latest fixes live, another watching for new errors, and another coding up a solution to the highest-priority issue, all while an orchestrator was managing them for me.

I also used Every’s __compound engineering__ plugin extensively as the project got further along. Its ability to make deep, well-researched plans and its comprehensiveness in reviewing code only further extend Codex’s power.

## The new bottlenecks at the edge

In launching Proof, it also became obvious to me where coding models still fall short—and what new bottlenecks show up now that we don’t have to type code character by character into our computers anymore. Here’s a list:

**Coding models make a mess when they try to fix issues in isolation**

Coding models often prefer to fix the local issue instead of stepping back first to identify the root cause. Without your guidance, the codebase risks becoming a patchwork of hot fixes that cause more problems than they solve.

**Coding models don’t always know best practices**

Proof is built on __Yjs__ and __Hocus Pocus__, two open-source libraries for building live, collaborative document editors. A week into the latest version of the app, I realized that the best practices around Yjs aren’t in GPT-5.4’s training data. This meant it wasn’t catching some obvious architectural deficiencies, and was pursuing suboptimal solutions to certain problems.

Asking the model to do significant web research *before* building seemed to mostly fix the issue. But this relies on the best practices being on the web, which is not always the case—especially if you’re working in enterprise software and using private company libraries.

**Coding models will figure out the right answer—eventually**

Even with the above problems, I do think Codex would have *eventually* solved most issues. But coming to the right answer requires a feedback loop.

Once Codex, or any coding model, writes a fix, it needs to review the code, test the fix locally, test the fix in a staging environment, get the code into the production app, and then monitor to see if the fix is working. On a small codebase, this loop is fast. On a large, complex one, it can take hours.

**Why human engineers aren’t going away**

Every bug fix is a scientific experiment. A coding model has no way to shortcut the cycle—of hypothesizing a fix, coding it up, deploying, monitoring, and, if the fix doesn’t work, forming a new hypothesis. It can only run the experiment and wait. The cost, in time and tokens, grows with the complexity of your app.

An experienced engineer using a model runs fewer experiments. They look at a broken system and, based on years of their own failed experiments, quickly narrow the possibilities—*this is probably X*. These hunches aren’t always right, but they are right often enough to make the difference between an immediately stable app and one that’s broken for a few days while your agent hunts down the issues.

This is the whole point of the __allocation economy__. The scarce resource is knowing where to direct intelligence. Expertise increasingly means being able to ask the right first questions, narrow the hypotheses, and waste fewer cycles.

And faster model progress doesn’t get rid of this. Because the frontier of expertise is moving even as new models are being trained. The best practices for using AI on complex production systems are being worked out right now, by engineers doing it, and those practices won’t show up in training data for months or years—if at all.

So yes, we are now living in a world where if you can vibe code, you can vibe fix it. But without human expertise, it might take a while.

*Dan Shipper**is the cofounder and CEO of Every, where he writes the* *Chain of Thought* *column and hosts the podcast* AI & I. *You can follow him on X at* *@danshipper* *and on* *LinkedIn. *

*To read more essays like this, subscribe to Every, and follow us on X at @every and on LinkedIn.*

*We build AI tools for readers like you. Write brilliantly with **Spiral**. Organize files automatically with **Sparkle**. Deliver yourself from email with **Cora**. Dictate effortlessly with **Monologue**.*

*We also do AI training, adoption, and innovation for companies. Work with us to bring AI into your organization.*

*For sponsorship opportunities, reach out to [email protected].*

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
