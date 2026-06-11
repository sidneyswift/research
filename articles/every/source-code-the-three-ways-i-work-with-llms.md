---
title: "How I 10x My Engineering With AI"
author: "Kieran Klaassen"
date: 2025-06-03
url: https://every.to/source-code/the-three-ways-i-work-with-llms
words: 1128
---

I spent three hours on X last week watching prompt gurus peddle their latest silver bullets:

"This one ChatGPT prompt will replace your entire engineering team."

"Claude with this secret system prompt outperforms every developer."

"My $497 prompt library will make you a 10x coder."

Meanwhile, I shipped five features for __Cora__, our AI-powered email assistant, using models from all three providers—Anthropic, Google, and OpenAI— and zero magic prompts. I didn't find one perfect prompt or tool to do all of my work. In fact, I stopped looking for one. Instead, I used different tools based on what I was trying to do.

This approach has changed how I ship code. I set the goal and define the rules, and then 100 percent of my pull requests are opened by AI tools like Claude Code. Every research task runs through ChatGPT and Claude. AI handles 30 percent of my code reviews and debugs half of the bugs I encounter. What used to take me a full week of coding now happens in hours.

The contradiction isn't lost on me: I’m criticizing one-size-fits-all AI solutions while building an AI-powered product myself. But Cora doesn't promise to do all your email work—it helps you spend less time on the parts that don't matter. My work with AI follows the same principle: Clear away the mechanical coding tasks to focus on what requires actual thought.

After years of building with LLMs—most recently the systems that let Cora triage emails by importance and draft replies intelligently—I've distilled my coding approach to three core patterns, each optimized for a different kind of cognitive load. These three workflows got me from grumbling about AI gurus on X to shipping features before lunch.

**Everyday coding with Windsurf and Cursor: The flow state companion**

When I'm in that programmer's groove—I’m clear on what needs building and ready to just code—I reach for Windsurf and Cursor paired with thinking models like Claude Sonnet 4 or __Gemini 2.5 Pro__. This setup works for:

- Building incrementally on existing code
- Solving well-understood problems
- Maintaining focus and flow while coding

What makes this workflow special is its lightweight, responsive nature. I speak coding instructions in plain English—"add a function to validate email addresses"—and the AI translates them into code. The AI editor doesn't break my concentration; it reduces the friction between my intention and implementation. In this setup, I am the thinker, and the AI is purely the executor. I drive all the decisions, while the AI handles the mechanical aspects of coding. I maintain complete control of the architectural and design choices.

Here’s an example: I needed to add a new filter option to Cora, similar to the "all emails" view but to show just important messages. It’s trivial work—I could have done this manually in 20 minutes. But that’s 20 minutes that I wanted to spend shaping the next feature. Instead, I stayed in my editor, described what I wanted in natural language—show only the important emails, write the query efficiently, check for indexes, and make sure it plugged into the existing context cleanly—and watched the AI implement it across the codebase. Twenty minutes of coding, or two minutes of talking to my editor—the math is obvious.

This might sound like __vibe coding__ on the surface, but there’s an important distinction in terms of intention. Vibe coding works from the outside in: You tell the AI what you want the software to do and let it figure out __how to get there__. My approach is inside-out: I already know both the destination and the route. I've decided on the architecture, the patterns, and the specific implementation details. I'm just delegating the mechanical act of translating those decisions into syntax. The AI is my hands, not my brain.

The key advantage is speed without sacrificing quality or accuracy. I speak, and the AI translates my intentions into code. It feels like pair programming with a skilled partner who never gets tired.

This mode works best when the stakes are low and the direction is clear. I'm not relying on the AI for big architectural decisions—I'm using it to implement solutions I could code myself but prefer to delegate.

**I reach for this workflow when:**

- I know exactly what “done” looks like.
- I'm working on a single, focused task.
- I need to build efficiently without breaking flow.

This is the mode I default to when I'm already mid-sprint or almost done and just need to keep moving.

**Big-picture thinking with search and reasoning models: The architect's approach**

When facing a blank canvas—starting a project from scratch, designing a new system architecture, or untangling complex legacy code—I need a different approach. This is where my research-focused workflow for discovery and exploration comes in, using:

-
ChatGPT with
__o3__and tools -
RepoPrompt or
__Claude Code__agentic search (a tool that gives AI the full picture of your codebase instead of working blindly) -
Multiple models in parallel (
__Claude 4 Opus__, Gemini 2.5 Pro, o3)

Unlike everyday coding where I direct every detail, here I embrace the AI as a true thought partner. I start with an open mind and deliberately avoid pushing too hard in any direction. The goal is to be surprised—to discover approaches and solutions I wouldn't have considered on my own.

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

Best article I've read so far regarding the development landscape with AI. I was getting bogged down with so many AI tools popping up every week: Cursor, Devin, Claude Code etc.

You articulated a great framework for when to use what. It helped me validate my thinking. Very helpful, thanks.

Love the clarity on mental models and practical examples of how you apply it all. You clearly are at the stage where the new technology has changed the way you work which is much further ahead than most that pull the new technology into how they work.

Are you using OpenAI's deep research on GitHub repos much or just o3? What are your mental modelas and preferred AI models in Cursor/Windsurf and why? What's your view on Cursor vs. Windsurf and all the others? What about Claude Code vs Codex vs Cline etc? It's too much to try it all I think and it changes so fast so was curious where your head is at.
