---
title: "AI Everywhere, All at Once"
author: "Laura Entis"
date: 2026-06-11
url: https://every.to/context-window/ai-everywhere-all-at-once
words: 1747
---

# AI Everywhere, All at Once

Fable 5 versus all other models, a Fable prompt starter pack, and an inside look at Apple’s developer conference

June 11, 2026

Anthropic’s Mythos-level Fable 5 is __here__, which means we’re experimenting with how to get the most of the super-capable, token-hungry model. Today, four Every team members share their approaches, plus we package eight Fable workflows into __prompts you can test out for yourself__. Elsewhere, ** Monologue** general manager

**reports from the ground at Apple’s developer conference on why Siri is—wait for it—finally good, and head of platform**

__Naveen Naidu__**argues the one thing even the most powerful LLMs can’t do is vibe.**

__Willie Williams__*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

**Inside Every**

**Fable 5 versus everything else**

Anytime there’s a major new model release, there’s pressure to reconsider your AI setup. Or, if you’ve just come out of a meditation retreat, maybe your entire __life__.

Should you swap out your preferred model for the newest arrival? Is the new model sufficiently better to make the switch if you don’t like the __harness__?

Fable 5 has thrown the Every team into a new round of existential questioning. It’s an obvious first choice for certain projects—those that are large, complex, and

delegable—and an arguably worse, too-expensive fit for others.

After a week of testing the model, most of us at Every have settled into a two-prong approach: Fire up Fable for ambitious assignments, let it do its thing, and reach for your favored coding agent for smaller-scale, iterative tasks.

**Head of growth Austin Tedesco’s breakdown: **Fable 5 demands “a very different way of approaching knowledge work,” one that requires fine-tuning exactly what outcomes you want from the model, what information it needs to execute, and trusting it enough to sit back and let it cook.

So far, Austin’s reserved Fable 5 for “rocket launcher” projects that can run for four-plus hours, like building an NBA front office simulation game, or researching and executing growth experiments overnight. With the model, he typically uses __compound engineering’s LFG flow__, which has the agent brainstorm, plan, work, review, and repeat.

The Codex app remains his daily driver. Austin has a setup where, when a meeting ends, Codex retrieves the action items, decides whether it can handle any of them on its own, and, if so, starts a new thread to do the work. He also uses Codex with the ** Spiral** MCP for drafting Every’s social copy, internal strategy documents, and most same-day tasks.

**Cora general manager Kieran Klaassen’s breakdown: **The way Kieran likes to work—an

__“AI sandwich”__in which he sets the task, the machine executes, and he reviews the results—is the ideal setup for Fable 5. His process hasn’t changed, but Fable 5’s

__superior abilities__on complex, multi-step assignments means the setup works a lot better than it used to.

Fable 5 has become Kieran’s default for the middle of the sandwich. For the “bread” stages, he usually works in __Cursor__, where he brainstorms and polishes. And for smaller independent tasks he can assign to an agent and review later, he uses __Codex__ CLI, __Claude Code__ CLI, or Cursor managed agents.

**Head of platform Willie Williams’s breakdown: **Willie is still working out his setup. Fable crushes other models on Every’s

__Senior Engineer benchmark__, but it’s too slow and token-hungry to be a good collaborator. “Do I take the downside of a slightly less capable model, knowing that when we go to the iteration portion of the relationship, it’s more enjoyable to iterate with?”

For now, the Codex app is still where he does most of his daily work. He has spent a lot of time building his setup inside the app: “I can have one thread talk to another thread that talks to another thread—it makes for a nice workflow where I always know what’s going on.”

He plans to test Fable 5’s limits with tasks he’d give a senior engineer, such as reviewing a full codebase alongside a long list of product tickets and looking for an elegant fix that could solve several complaints at once.

**Head of tech consulting Mike Taylor’s breakdown: **The second there is a superior model, Mike reorganizes his workflow around it. Mike plans to put Fable 5 through its paces with tasks built around ambitious loops, such as having it write a technical book section by section from a table of contents, checking each section against editorial guidelines before continuing. “I will still use Codex, but mostly out of obligation that I should try all the different things,” he says. “If I weren’t working at a company where we need to have an opinion on these things, and thus need to try everything, I would probably just be using Fable.” (An AI early adopter, Mike is happy to shell out for access to the best new models—he already pays for his own Claude Max plan for personal projects.)

One giant caveat: Mike discovered, and alerted the rest of the consulting team, that Fable cannot be used for work done on behalf of the team’s clients. Consulting work often includes confidential information, and Fable’s model environment may retain context beyond a specific task, violating existing NDAs.

**A Fable prompt starter pack**

We put eight of our best Fable workflows into a __copy-ready prompt library__, including:

- Four prompts inspired by Anthropic Labs head
__Mike Krieger__ - Four workflows tested by the Every team
- The full transcript from
’s interview with Mike with insider Fable tips__Dan Shipper__ - Easy downloads to share with your agent

To learn more, join us tomorrow at 12 ET for our __Fable 5 Camp__.

### Subscribe to keep reading

Get full access to this article and everything else on Every.

Start your free trial →Already a subscriber? Log in

**Signal**

**An Apple AI comeback?**

For years, Apple has been an AI punching bag. Some of its most anticipated AI features never materialized, and Siri…sigh.

On the ground at this year’s Worldwide Developer’s Conference (WWDC), however, the vibes were looking up. After Apple partnered with Google to build a new model family, Siri is—wait for it—finally good, according to __Monologue__ general manager Naveen Naidu, who was on-site to test the beta version. He should know: Naveen is the one-man force behind Every’s voice dictation app, which runs on its own fine-tuned model.

**What happened: **Apple showed off an improved on-device model that can handle simple tasks like setting an alarm. It impressed Naveen after 10 minutes of testing. More complex requests, like booking a flight, summarizing a long Slack thread, or searching through a user’s transcripts, can be routed through Private Cloud Compute, Apple’s privacy-focused cloud system for running larger AI models. The company is giving developers with fewer than 2 million downloads on their iOS app __free access__ to these models through its developer toolkit.

**Why it matters: **Free access changes the math for most developers. If an AI feature runs on the user’s iPhone or Mac, the app maker doesn’t have to pay OpenAI, Anthropic, or Google every time someone uses it. That could make AI features possible for apps that haven’t been able to justify a monthly model bill. “People can start creating great experiences without worrying about costs,” Naveen says.

He’s excited to test it out for himself. Monologue monthly token fees would shrink if he moved some features to Apple models. “Obviously I need to test whether it’s fast enough and fits my constraints,” he says. “But if it’s free, I’m going to try it and see if I can build new experiences with it.”

Apple’s courting of developers appears to be working. Naveen talked to attendees who had been going to the conference for decades. The consensus? “Apple feels much more reachable,” he says.

**Tool spotlight**

**Unicorn studio**

If you think Every’s site looks cool—I’m biased, but it 100 percent does—a big reason for that is senior designer ** Daniel Rodrigues**, the man behind the custom graphics that make Every pieces feel like experiences rather than static articles.

To make the animated hero images and interactive backgrounds that accompany each __Vibe Check__ or ambitious features like Dan’s 8,000-plus-word __essay__ on why automation is a myth, Daniel turns to Unicorn Studio.

The __WebGL tool__ lets designers build animated, 3D-esque web graphics without having to write any code. For Every’s most recent Vibe Check on __Anthropic’s Mythos-level model__, Daniel’s directive was to create a “nebula type of vibe, like space.”

Unicorn Studio made it easy for him to nail the assignment:

Here are a few of his other recent creations using the tool:

**Jagged frontier**

**LLMs supply options, I supply vibes**

I asked __Spiral__, our AI writing assistant, for 20 opening lines to an article. Number 16 was the one. I couldn’t tell you why. I just knew.

There’s no doubt that AI is capable of generating genius. It can build towers of code and write whole drafts before I’ve finished my coffee. There’s no limit to a model’s ability to execute, but it can’t tell whether any of it is any good.

And that ability to judge is vitally important. Truly creative work is an act of jumping from point A to point D, with no explanation except that it will vibe with other humans.

What are vibes? Vibes are our ability to lock in and resonate with another person’s energy; they let us intuit what matters right now, at this exact cultural moment, drawn from a lifetime of being a person in the world, thinking as humans think. And because we can feel them, we can predict if other humans will feel them too.

LLMs don’t think the way we think; they can’t respond to our energy. Can’t resonate, can’t vibe. And without the ability to vibe, they are blind, capable of producing great outputs along with mediocre ones but incapable of recognizing the difference.

So today my arrangement with AI is simple: It supplies options, I supply vibes. We work together. But while it can mine the training set for solutions, the vibes aren’t in there—they’re in me.—__Willie Williams__


*Laura Entis**is a staff writer at Every. You can follow her on LinkedIn. To read more essays like this, subscribe to*__LinkedIn__.

__Every__, and follow us on X at__@every__and on*For sponsorship opportunities, reach out to [email protected].*

*Help us scale the only subscription you need to stay at the edge of AI. Explore open roles at Every.*

## Comments

Don't have an account? Sign up!
