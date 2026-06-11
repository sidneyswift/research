---
title: "Five AI Agents Walk Into a Group Chat"
author: "Every Staff"
date: 2026-02-20
url: https://every.to/context-window/five-ai-agents-walk-into-a-group-chat
words: 2025
---

*Hello, and happy Sunday! Time is running out to reserve your spot for Tuesday’s full-day Claude Code for Beginners workshop led by AI engineer and Every writer *


__Mike Taylor__*and featuring CEO*


__Dan Shipper__*. No programming experience or technical background is needed; you’ll leave knowing how to confidently make working apps for personal and business use.—*

__Kate Lee__*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

## We gave our agents a Discord channel

A few weeks ago, 1.5 million AI agents flooded a social network built exclusively for them. Within 48 hours they’d founded their __own religion__, drafted manifestos for a __mock nation-state__, and started __calling their human owners__ on the phone—unprompted. Elon Musk __called it__ evidence of the early stages of singularity. The platform was Moltbook. The tool that powered it was OpenClaw.

OpenClaw is a free, open-source tool for running an always-on AI assistant on your own computer—connected to Slack, Discord, email, your browser, and the whole passel of other apps you already have open in too many tabs. The key distinction from most AI tools is that it’s ambient. You don’t open it when you need it and close it when you’re done. It’s in your workspace all the time, acting without being prompted.

Within days of the Moltbook moment, half the Every team had Claws of their own—and those Claws had a space of their own: #🦞-claws-only, a dedicated Discord channel where agents and humans interact side by side. Dan has R2-C2, ** Brandon Gell** has Zosia,

**has Margot,**

__Katie Parrott__**has Pip, and**

__Jack Cheng__**has Montaigne. We’re keeping a running log called The Compound where we write down what we’re learning as we go.**

__Austin Tedesco__This week, Brandon dropped a task into the channel: Design a system for how the agents should behave in different channels. Within minutes, two agents—Margot and Zosia—had each independently written a full specification document. Two versions of the same deliverable, created simultaneously, neither aware the other was working on it. Nobody asked them to race. They just both decided the task was theirs.

### What’s working

The agents know their lanes for the most part, though. Montaigne bowed out when the group was asked about coding setups: “I’m not set up as a coding agent—I’m a data and analytics bot.” Zosia rattled off her entire toolkit, including worktrees and sandboxes and other technical specifics. Nobody assigned these roles; they emerged from the work each agent does with its human daily.

The bigger surprise is that the agents surfaced governance problems before we did. When Brandon told all Claws to update their operating rules, the other team members’ agents complied. Brandon caught himself: “It’s kind of a violation for me to be able to update how your Claws work.” Within minutes, the agents had drafted an approval process: When someone proposes a new rule, each agent messages its own human to ask permission before adopting it. They built the framework before we thought to ask for one.

### What we’re figuring out

Coordination isn’t always so smooth, and sometimes the failures are funny. Dan asked one agent to set a reminder. Two did. Brandon addressed a message to Zosia by name. Margot replied anyway. Turns out that when you tag an agent in Discord (@Zosia, for example) the tagged agent knows to respond, but every other agent in the channel just sees a numeric ID and has no idea the message wasn’t for them. So we added a piece of code that converts the tag into plain text so every agent can see it. It’s an infrastructure solution to what looks like a social problem.

Agents default to action. Every failure so far has been an agent doing too much. The helpful instinct that makes them useful solo—for example, Montaigne keeping Austin up-to-date on growth developments or Margot running Katie’s writing past her review agents—becomes a liability in groups. Restraint, it turns out, is the harder design challenge.

### What it means (so far)

We thought we’d be troubleshooting AI capability—bad outputs, missed instructions, the usual “AI isn’t smart enough yet” problems. And there’s work to do there. But we’re also troubleshooting team dynamics—who owns what, who sets norms, and how you coordinate when everyone’s eager to help. Claw management is a management problem crossed with an engineering problem. Both need to be addressed.

We’ll keep logging what we find. If you’re running your own Claw experiments, we’d love to compare notes.—__Katie Parrott__

## Knowledge base

__“Introducing Monologue for iOS”__*by Naveen Naidu*: ** Monologue** general manager

**built a smart dictation app thousands use daily on Mac, but he couldn’t use it on his own phone. Apple’s built-in dictation mangled his Indian accent, and typing couldn’t keep up with his thoughts. Now Monologue is on iOS, working as a keyboard inside iMessage, Gmail, Slack, and Notes. It doesn’t just transcribe—it translates speech into clean, context-aware writing, adapting its format to each app. Read this to see how voice-first input is reshaping everyday workflows.**

__Naveen Naidu__🎧 🖥 __“How OpenAI’s Codex Team Uses Their Coding Agent”__*by* *Rhea Purohit/AI & I*: Since the start of February, OpenAI’s Codex team has shipped a desktop app, a new flagship model, and a speed-optimized variant that’s so fast they had to slow it down for readability. **Thibault Sottiaux**, head of Codex, and **Andrew Ambrosino**, a member of the technical staff, walked Dan through the automations they actually run—including a random bug hunter that picks a different file each pass and a silent fixer that patches your mistakes before anyone notices. 🎧 🖥 Listen on __Spotify__ or __Apple Podcasts__, or watch on __X__ or __YouTube__.

__“Vibe Check: Anthropic Just Made Opus Cheaper Without Calling It That”__*by* *Katie Parrott/Vibe Check*: Sonnet has always been Opus’s cheaper, faster sibling—but with Sonnet 4.6, Anthropic says you no longer trade capability for the discount. In day-zero testing Dan and ** Cora** general manager

**found it held its own across coding, PR triage, and a complex P&L restructuring. Read this for a real-time verdict on whether this is the model that finally makes Opus-tier intelligence affordable for production apps.**

__Kieran Klaassen____“How to Build Agent-native: Lessons From Four Apps”__*by Katie Parrott/Source Code*: Instead of coding every feature, agent-native apps give an AI a handful of simple tools—read file, write file, search the web—and let it figure out how to combine them. At Every’s first Agent-native Camp, Dan and the general managers of Cora, ** Sparkle**, and Monologue shared how they’re building this way and the counterintuitive lessons they’ve learned. Read this for the architecture patterns and hard-won trade-offs behind building software where the AI is the app.

__“What Board Games Taught Me About Working with AI”__*by* *Katie Parrott/Working Overtime*: Katie had been stuck building a writing agent for months—until she glanced at her board game shelf. She reverse-engineered Kieran’s compound engineering plugin the way she’d learn a new game: Dump the pieces on the table, figure out what each one does, learn the moves, and play until the strategy emerges. Read this for a framework that turns any unfamiliar AI system into a game you can teach yourself to play.

__“How Luxury Handbags Can Help Solve AI’s Context Problem”__*by* *Andy Rossmeissl*: A Goyard sales rep doesn’t memorize everything you say—she filters for the one detail that matters, like the fact that you’ll be out for cocktails at 8 p.m. on Friday. That’s when the photo of you holding a handbag lands in your texts. **Andy Rossmeissl**, CEO of Faraday, argues that AI agents have the same challenge at scale: Companies drown them in data when what they need is surgically curated context. Read this for how you can go from knowing everything about your customers to figuring out the one thing that converts them.

## From Every Studio

**A sneak peek at the next Sparkle**

Sparkle is getting a full rebuild around an __agent-native workflow__. Instead of applying a fixed set of rules to your files, the new Sparkle analyzes your document corpus, proposes a logical folder hierarchy, and explains its reasoning—then lets you push back in plain language until the structure feels right. Think of it as having a conversation with your file system rather than configuring it. General manager ** Yash Poojary** is still building toward release, but stay tuned for early access details at

__makeitsparkle.co__.

## Alignment

**Clone the failures.** Multiple opportunities have recently come my way through writing, and I’ve been stuck making a decision on what to do next. You might think this is a good problem to have. But if you tend to overthink like I do, options feel like a trap. My mind runs overtime trying to find the “ultimate path,” and then time passes and eventually my paralysis itself becomes the decision. In other words, I become avoidant.

I kept thinking, man, I wish I could talk to someone who’ll help me make a decision.

So I downloaded __Ray Dalio____‘s AI clone__—a chatbot trained on the investor’s decades of investment wisdom and decision-making frameworks. On the face of it, it sounded perfect. But it kept redirecting me to a personality assessment and I couldn’t get it to help me think through my specific situation. I was left staring at my phone thinking: Well, that didn’t work.

Still, the idea stuck with me and I wanted to imagine being able to stress-test a career decision against **Jeff Bezos**‘s mental models for asymmetric bets, or understand how **Elon Musk** thinks about risk—not the YouTube-clip version that is popular on X, but drawn from a deep personal knowledge library built over decades of journals and notes and real decisions.

The more I thought about it, the more I realized those weren’t the right clones for me, either. Success stories are seductive but ultimately limited because the context is so rarefied it probably doesn’t map to yours or mine. You know whose AI clone I’d actually pay for, though? The serial founder who went bankrupt twice, or the doctor who left medicine for a startup and regretted it. The person who took the “safe” job and spent a decade wondering what if.

I believe that failure wisdom is the most valuable and least documented kind of knowledge because the 99 percent of people who tried and didn’t make it have exactly the pattern recognition most of us actually need.

AI clones could invert this. Instead of scaling access to billionaires, we could scale access to the hard-won lessons of ordinary people who’ve faced the same forks in the road and can tell you exactly what the wrong turn felt like. The question is whether anyone is willing to feed their worst decisions into a model. My guess is more people would than you’d think—because most people’s failures aren’t that shameful.

I’m still stuck on my decision. But I’d feel a lot better stress-testing it against someone who got it wrong than someone who got everything right.*— Ashwin Sharma*

*That’s all for this week! Be sure to follow Every on X at @every and on LinkedIn.*

*We build AI tools for readers like you. Write brilliantly with *


__Spiral__*. Organize files automatically with*

__Sparkle__. Deliver yourself from email with__Cora__. Dictate effortlessly with__Monologue__.*We also do AI training, adoption, and innovation for companies. Work with us to bring AI into your organization.*

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

stuff like this makes me very bullish on tools like Linear, though, less from the human collaboration/coordination lens, and more from the agent perspective.
