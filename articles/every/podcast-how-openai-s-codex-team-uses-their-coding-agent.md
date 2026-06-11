---
title: "🎧 How OpenAI’s Codex Team Uses Their Coding Agent"
author: "Rhea Purohit"
date: 2026-02-18
url: https://every.to/podcast/how-openai-s-codex-team-uses-their-coding-agent
words: 2330
---

# How OpenAI’s Codex Team Uses Their Coding Agent

Thibault Sottiaux and Andrew Ambrosino on product strategy, the workflows they rely on, and why speed creates a new bottleneck

February 18, 2026 Updated May 30, 2026

*TL;DR: Today, we’re releasing a new episode of our podcast *__AI & I__, *where *__Dan Shipper__* sits down with two members of the team building OpenAI’s coding agent, Codex, *__Thibault Sottiaux__*, head of Codex,** **and *__Andrew Ambrosino__*, member of technical staff on the Codex app. **Watch on X or YouTube, or listen on Spotify or Apple Podcasts. *

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

A little after 4 p.m. PT on Super Bowl Sunday, a wave of people took their eyes off the game to download a coding agent. It wasn’t the wings, the beer, or Bad Bunny that inspired them. It was one of the many AI ads that aired—specifically, OpenAI’s plug for its coding agent, Codex.

** Thibault Sottiaux**, head of Codex, and

**, a member of technical staff on the Codex app, say their systems came under heavy load almost immediately after the spot aired. Even better, a lot of people also reached out to tell them that the ad inspired them to build, they told**

__Andrew Ambrosino__**on**

__Dan Shipper__*this week.*

__AI & I__The conversation caps off a few busy weeks for the Codex team: Since the start of February, they’ve shipped a __desktop app__, __GPT-5.3 Codex—a new flagship model__—and a __research preview of a model that’s almost too fast to follow__. The momentum is showing up in the numbers, too. Usage has grown fivefold since the start of the year, and more than a million people now use Codex each week. Dan talks to the pair about the strategy decisions behind what they’ve built, the workflows they rely on inside Codex, and how a lightning-fast model potentially solves the next bottleneck for coding agents.

Here is a link to the episode transcript.

You can check out their full conversation:

Here are some of the themes they touch on:

## A look inside OpenAI’s strategy to ship new products

Sottiaux and Ambrosino talk Dan through the decisions and tradeoffs that went into their new launches.

#### A warmer coding agent that’s still for builders

As we’ve written, GPT-5.3 Codex feels more user-friendly than its predecessors—warmer and more creative—while still maintaining its technical prowess. That shift was echoed in OpenAI’s decision to run a Super Bowl ad for Codex rather than ChatGPT, signaling a bet that coding agents are ready for a mainstream audience.

Still, OpenAI views Codex as its most powerful coding tool, one that requires a certain level of technical fluency. Sottiaux describes the target user as “technical” or “technical adjacent”—someone with familiarity in areas like data science, for example—and says that to get the most out of it, you should be able to read code. For the wider, less technical audience, he adds, OpenAI plans to eventually bring a similar experience into ChatGPT, which will not assume engineering literacy of its users.

Even so, the team is adamant that professional developers deserve a “dedicated experience.” Ambrosino notes that while the Codex app shares clear DNA with ChatGPT—features such as the central chat-style interface and the auto-named conversations—it was purpose-built to “showcase the power of the models and the way [they] could change the [software] development lifecycle.”

#### OpenAI believes your coding agent doesn’t belong in a terminal or the IDE

The decision to build a dedicated graphical user interface (GUI)—a visual, point-and-click interface rather than a text-only terminal approach—for the Codex app was, by the team’s own admission, a break from trending design choices. Ambrosino describes the app as a “daily driver,” with the terminal and the integrated development environment (IDE)—an all-in-one environment for writing code where many developers have traditionally worked—reserved for the occasional specialized task.

According to them, a terminal works well for firing off quick tasks, but starts to feel limiting once agents become multimodal—drawing diagrams, generating images, and responding to voice instructions—or once you’re running several in parallel and need to keep track of them all.

OpenAI designed Codex to dynamically show only the tools and views you need at that moment. “We came to the conclusion that…these models are great at knowing what’s needed…for what type of task,” Ambrosino says. Sottiaux adds that the AI is already acting on far more than just code—like filing tickets in project management software Linear and posting to Slack—and cramming all of that into an IDE “would feel very odd.”

#### How the Codex team teaches AI to read between the lines

Achieving a balance between the model being good at following instructions and intuiting user intent is something the team obsesses over. Codex has historically excelled at the former, but when they optimize too hard in that direction, the model starts to overindex on literal wording and miss intent in ways a human never would. Sottiaux takes the example of a typo in a prompt that ends up verbatim in the code, rather than the model inferring what you obviously meant.

The team is also investing in what they call “personalities”—essentially, a measure of how supportive or blunt the model should be. While the previous default leaned heavily terse and direct, now there’s a friendlier, more supportive option, and users can toggle between the two. Both Sottiaux and Ambrosino still use the pragmatic “personality.” “You should feel like you have your own little personal Codex,” Sottiaux says, “that works in exactly the way that you want it to work.”

## How the Codex team uses its own AI

Two features make the Codex app especially powerful: “automations,” which let you schedule prompts to run hourly, daily, or at whatever cadence you set, and “skills,” which bundle instructions so that Codex can connect to external tools and run workflows that go beyond code generation, including research, reporting, and writing. These are a few automations and skills that Sottiaux and Ambrosino find useful:

-
**Keeping code changes ready to ship.**When multiple people are working on the same codebase, their changes can collide—one person’s update breaks another’s, creating “merge conflicts” that have to be manually untangled. Ambrosino runs an automation every hour or two that scans for these conflicts and quietly resolves them, so that when a change is ready to ship, it can go live immediately. -
**Daily team digest.**Every morning at 9 a.m., Ambrosino gets an automated report summarizing everything that was merged into the Codex app over the previous day, including who contributed what, grouped by theme. It’s a quick way to stay on top of a fast-moving codebase without having to manually track every change—especially useful in the chaos leading up to a launch. -
**Random bug hunter.**Sottiaux runs an automation multiple times a day that picks a random file from the codebase and looks for bugs. It uses a random number generator to choose where to start, so each run explores a different corner of the code. The automation usually picks up on non-critical bugs that nobody would’ve gone looking for and are trivial to fix. -
**Silent bug fixer.**Another team favorite: an automation that reviews the pull requests you’ve done over the past day, scans for signs that anything is breaking. It pushes a fix before anyone notices you shipped a bug. -
**Daily marketing intel.**Sottiaux runs a daily automation—tuned with a custom skill to do deep research—that searches the web for how users are perceiving and talking about Codex, and compiles what it finds into a short report. -
**One-click publish.**After writing code, a developer still has to save it with an explanation (called a “commit”), open a pull request for teammates to review it, and write a clear title and summary describing what changed and why. Ambrosino built a “yeet” skill that does all of that automatically. -
**Custom book for his kids.**Ambrosino used the Codex app’s image generation skill to create a personalized book for his kids. He started by prompting Codex to write a script based on his daughters’ ages, the cities they’ve lived in, and the arc of their lives so far. Once he approved the script, Codex generated an image for every page, then stitched everything together into a printable PDF.

## Speed is a dimension of intelligence

We said GPT-5.3-Codex-Spark, the smaller, speed-optimized version of OpenAI’s GPT-5.3 Codex, is __fast enough to blow your hair back__—and it is. “We do slow it down ever so slightly, just so you can see the words come in a little bit smoother,” Ambrosino says. The team sees speed unlocking different ways of working

-
**Staying in the flow.**The first is simply staying in the flow. Sottiaux describes using the new model as “sculpting code” in real time. At first, the speed is almost disorienting, but within minutes, you adjust—and once you do, going back to anything slower is hard to imagine. -
**Replacing brittle tools with intelligent ones.**Programmers rely on Git, a version control system for tracking code changes, to save and share changes to their code, and while it’s powerful, it’s also notoriously finicky. If the code is in even a slightly unusual state, simple actions like “publish this change” can trigger confusing errors that require manual cleanup. That’s why many apps struggle to make Git feel smooth or intuitive: There are too many edge cases to account for with rigid, pre-programmed buttons. Ambrosino suggests that a fast enough AI model can potentially change this. Instead of relying on brittle scripts that only work when everything is perfectly set up, the AI can look at the situation in real time and figure out what needs to happen. -
**Redirecting the model while it works.**Mid-turn steering is the ability to send a new instruction while the model is still working, and have it adapt without stopping its thinking process. Codex already supports this, but paired with the new model, the experience would feel more and more like a fluid conversation. Sottiaux is especially excited about combining this with voice—talking to the model in natural language, redirecting it as you go, watching the implementation happen almost instantly.

## Code review is the next bottleneck

With speed close to being solved, the next bottleneck is review. Models can generate code faster than ever. But will it be bug-free? Will the button in the settings panel do what it’s supposed to? That still requires a human to click through the app and check for consistency.

The OpenAI team is exploring what that process looks like with AI involved. The Codex app already has a review mode that annotates diffs (side-by-side comparisons showing exactly which lines of code were added, removed, or changed). Speed helps here, too, Sottiaux adds. A faster model that helps you understand the code you’re reviewing offsets some of the pressure created by the sheer volume now being produced.

Ambrosino hints at a more ambitious direction: If a model can prove a bug fix works by retracing the exact click path a user would take, code review, as we know it, might matter less—you’d verify the outcome directly rather than reading the code as a proxy. The team already has skills in the Codex app that click around the app, screenshot the results, and attach them to a pull request to show what changed (and why it works).

What do you use AI for? Have you found any interesting or surprising use cases? We want to hear from you—and we might even interview you.

##### Timestamps

- Introduction: 00:01:27
- OpenAI’s evolving bet on its coding agent: 00:05:27
- The choice to invest in a GUI (over a terminal): 00:09:42
- The AI workflows that the Codex team relies on to ship: 00:20:38
- Teaching Codex how to read between the lines: 00:26:45
- Building affordances for a lightning-fast model: 00:28:45
- Why speed is a dimension of intelligence: 00:33:15
- Code review is the next bottleneck for coding agents: 00:36:30
- How the Codex team positions itself against the competition: 00:41:24

You can check out the episode on X, Spotify, Apple Podcasts, or YouTube. Links are below:

- Watch on X
- Watch on YouTube
- Listen on Spotify (make sure to follow to help us rank!)
- Listen on Apple Podcasts

Miss an episode? Catch up on Dan’s recent conversations with LinkedIn cofounder ** Reid Hoffman**; the team that built Claude Code,


__Cat Wu and__

**; Vercel cofounder**

__Boris Cherny__**; podcaster**

__Guillermo Rauch__**; and others, and learn how**

__Dwarkesh Patel__*they*use AI to think, create, and relate.

If you’re enjoying the podcast, here are a few things I recommend:

-
__Subscribe__to Every -
Follow
__Dan__on X -
Subscribe to Every’s
__YouTube channel__

*Rhea Purohit** is a contributing writer for Every focused on research-driven storytelling in tech. You can follow her on X at @RheaPurohit1 and on LinkedIn.*

*To read more essays like this, subscribe to Every, and follow us on X at @every and on LinkedIn.*

*We build AI tools for readers like you. Write brilliantly with *


__Spiral__*. Organize files automatically with*


__Sparkle__*. Deliver yourself from email with*


__Cora__*. Dictate effortlessly with*


__Monologue__*.*

*We also do AI training, adoption, and innovation for companies. Work with us to bring AI into your organization.*

*Get paid for sharing Every with your friends. Join our referral program.*

*For sponsorship opportunities, reach out to [email protected].*

*Help us scale the only subscription you need to stay at the edge of AI. Explore open roles at Every.*

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
