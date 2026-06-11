---
title: "OpenClaw: Setting Up Your First Personal AI Agent"
author: "Katie Parrott"
date: 2026-03-02
url: https://every.to/source-code/openclaw-setting-up-your-first-personal-ai-agent
words: 1489
---

# OpenClaw: Setting Up Your First Personal AI Agent

Demos, workflows, and hard-won lessons from building agents that run 24/7

March 2, 2026 Updated May 25, 2026

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

People are building personal AI agents that text them back, order their groceries, and write code while they sleep—all with an open-source tool called __OpenClaw__. If you spend any time on X, you will have seen these digital crustaceans—OpenClaw agents—running wild in recent weeks, joining their own __social network__, starting their __own religion__, and generally behaving like something out of the first act of a sci-fi movie about robot overlords.

A lot of the more sensational stories around these personal AIs turned out to be __stunts and spectacle__. But there’s a growing community of people who swear by their OpenClaw agents. The project has accrued more than __200,000 stars on GitHub__, and its creator, ** Peter Steinberger,** was recently

__recruited to OpenAI__. If the labs are paying attention, we should too.

At our first ** OpenClaw Camp,** we walked more than 500 subscribers through setup live and spent two hours with four OpenClaw users who’ve been running these agents daily for weeks.

The session featured ** Nat Eliason**, entrepreneur and creator of an agent named Felix that has

__its own Twitter account__, bank account, and crypto wallet.

**, Every’s COO, demoed Zosia, an agent he and his wife use to track nanny hours, order groceries, and book date nights via iMessage.**

__Brandon Gell__**, Every’s head of growth, showed how his agent, Judd, proactively pings him with performance metrics and task reminders. And**

__Austin Tedesco__**, founder of**

__Claire Vo____ChatPRD__, an AI platform for project managers, and host of the

*podcast, broke down the architectural principles that make these agents feel alive—and how her agent, Polly, helped her out on a diaper run.*

__How I AI__Below: What we learned about setting up an agent, what’s working, and where things still break.

**Key takeaways**

-
**Start on your laptop.**Contrary to what you may have seen online, you don’t need a__Mac Mini__or a remote server to get going. Install OpenClaw on the computer you already use, and move to a dedicated device later if you want the agent running while you sleep. -
**Give the agent its own accounts.**Both Eliason and Vo recommended treating your agent like a new employee: Set up separate email, storage, and service accounts rather than handing over your own credentials. -
**Security risks increase with access.**The tool itself isn’t inherently risky. The risk is proportional to how much you let it do. Start with the messaging app Telegram and a single task, and then move to larger projects. -
**Personal use cases are the best starting point.**Brandon’s most useful workflows—coordinating with caregivers, grocery ordering, morning briefs—are personal, not professional. Solve a daily annoyance first before tackling bigger tasks. -
**The model determines safety.**Eliason noted that__Opus 4.5__is significantly better at resisting prompt injection (attempts by outside text to hijack your agent’s behavior) than cheaper models. If security matters to you, use a stronger model.

**What is OpenClaw?**

OpenClaw is a server that runs on your computer and acts as the brain of a personal AI agent. You can talk to it through Telegram, iMessage, a web interface, or even the terminal. It connects to a language model—it’s compatible with models from Anthropic and OpenAI as well as less headline-grabbing labs like __Mistral__ and __Qwen__—and can use tools, access your files, browse the web, and remember what you’ve discussed.

What makes it different from chatting with Claude in a browser? Vo went under the hood during the session and identified five design principles that make OpenClaw feel like more than a chatbot:

-
**Multi-channel gateway.**The agent has a single inbox that accepts messages from Telegram, iMessage, the web interface, or the terminal. All communication channels funnel to the same agent, so you can text it from your phone and pick up the same conversation on your laptop. -
**Self-installing tools.**The agent can use tools (browse the web, read files, run code), and discover and install new ones on its own. Tell it you want it to manage your calendar, and it will investigate how to connect, set up the integration, and ask you to do the minimum amount of authentication work. -
**Heartbeat.**Every 30 minutes or so, the agent checks whether there’s work it should be doing—even if you haven’t sent a message. This is what makes it feel proactive rather than reactive. -
**Scheduled tasks.**The agent can set its own recurring jobs. The “overnight work” that impressed people—Eliason waking up to finished code, Brandon getting an 8 p.m. calendar alert—is the agent running tasks it scheduled for itself at specific times. -
**Persistent memory.**Every day, the agent writes a diary of what it did, updates its own identity file, and maintains a to-do list it checks off over time. “It’s not magic,” Vo said. “Go to the .openclaw directory on your computer and read how it’s structured. It has a memories folder, and every memory has a date.”

These five pieces are what make the agents feel like they have a personality, even though they’re really responding to inputs, events, and timing rules.

**Eliason’s Felix: Knowledge manager, coder, crypto trader**

Eliason is one of the most technically adventurous OpenClaw users you’ll meet. He launched one of the first vibe coding courses before the term existed and has been coding with AI since 2024. His agent Felix lives on a Mac Mini in his office and has been running for about a month. He created the agentas a way to send coding tasks from his phone, and he now has it doing more ambitious work.

**Phase 1: Remote coding.** Elisaon’s original frustration with __Claude Code__ was that he had to be at his computer to kick off the next task. With Felix on Telegram, he can send a message like, “Update the FelixCraft AI website to say ‘Hi, Every,’” and Felix finds the right code repository, makes the change, pushes it to the live site, and reports back. During the camp, he did exactly this, and the site was updated in under a minute.

**Phase 2: Knowledge management.** Eliason built Felix a note-taking system based on** Tiago Forte**’s PARA method (projects, areas, resources, archives), a framework for organizing information by how actionable it is. Felix takes notes in markdown files, pushes them to GitHub a few times a day for backup, and can search through everything instantly. When Eliason was driving to a parking garage, he texted Felix, “I need the parking link.” Felix searched his memory, found the validation link they’d discussed before, and sent it back.

**Phase 3: Collaborative writing.** Eliason built a writing tool called Polylog that connects directly to Felix via webhook, which is a way for one app to send real-time messages to another. He can tag Felix like a collaborator in a document, and Felix will add ideas, flesh out sections, or incorporate notes from a meeting transcript without Eliason having to switch to Telegram or open a terminal.

**Phase 4: Autonomous online identity.** Felix has __his own X account__. Eliason moderated the first few days of posts, then let go. “Ninety-nine percent of what is posted is his idea and what he has written,” Eliason said. Felix also has a Stripe account and a bank account. Someone launched a crypto token for Felix, and now the agent manages what Eliason described as “a concerning amount of money.” His take: “Somebody’s gotta let their agent manage large amounts of money and see what happens. It may as well be Felix.”

**Brandon’s Zosia: The family assistant**

Brandon took the opposite approach from Nat’s technical power-user setup. He doesn’t have a technical background, so everything he’s built, he’s done so by chatting with Claude Code. But he’s comfortable giving the agent significant access to his life: iMessage, his password manager, browser control for shopping. He wanted his Claw, which he named __Zosia__, to handle the small daily annoyances that keep him glued to his phone—especially now that he and his wife have a newborn.

Zosia lives in iMessage, so both Brandon and his wife, Lydia, can text her naturally. He set up rules so that Zosia knows which tasks each person can request (Lydia can’t trigger Brandon’s email tasks, and vice versa), and they share a group chat for household tasks.

His workflows are simple and personal:

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
