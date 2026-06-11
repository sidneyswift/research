---
title: "Spiral 4.0 Goes Agent-native"
author: "Marcus Moretti"
date: 2026-06-04
url: https://every.to/on-every/spiral-4-0-goes-agent-native
words: 1540
---

*TL;DR: **Spiral** v4 just shipped with four major updates: a style engine that generates writing indistinguishable from your own 87 percent of the time, agent-native access via MCP, CLI, and API, team workspaces for writing in a shared voice, and a $10 price drop, bringing personal plans to start at $15 a month. Spiral will continue to be free for paid Every subscribers along with access to all our tools and content.*

Today we’re announcing a number of updates to Spiral, the writing partner for you and your agent. Spiral is built by writers for writers, to help you from idea to line edit, matching your writing style throughout.

##### The highlights:

- With
__stylometry__(or the study of writing styles), Spiral now sounds more like you. We’ve built a new Style Engine from the ground up, so Spiral computes your writing fingerprint and picks relevant samples for new drafts. - Use Spiral wherever you do work. With a new MCP, plus our existing CLI and API, Spiral can step in if you’re underwhelmed by your agent’s writing output, or need good writing in any workflow.
- For teams, use Spiral to speak with one voice. Team workspaces let you share styles, prompts, knowledge, and now chats and drafts.
- And finally, we’ve given Spiral a new coat of paint and logo, designed by
. The primary brand font is now Edgar, from Frere-Jones Type.__Daniel Rodrigues__

Since __re-launching__ at the end of last year, Spiral has:

- Created 5,524 style guides from 168,464 writing samples
- Generated 113,165 drafts
- Made 350,078 revisions

It also now averages a 4.9/5 conversation score on our internal LLM-as-judge eval.

We built Spiral to help people who write for work write better. Just as Cursor is a coding harness, Spiral is a writing harness, supporting you at every stage of the writing process. Here’s how:

-
**Before you start writing**, Spiral vets the clarity of your idea and materials to substantiate it. From basic writing prompts to the hard-won insights from Every’s editorial and social media teams, multiple 12,000-word system prompts govern Spiral’s workflow. (To get the style and substance just right, we’ve iterated on these system prompts 131 times so far.) -
**When it’s time to draft**, Spiral uses stylometry to reproduce your voice, working in Every’s know-how where appropriate. For example, if you ask Spiral for tweets, it will incorporate best practices from X’s latest algorithm update. -
**When you need help polishing a draft,**Spiral is your editor. Along with a built-in guardrails against AI-speak, you can set custom writing rules that Spiral applies in a “top edit,” the final expert-level edit on a piece—a term I learned working at Every.

We’ve written about __the challenges of getting LLMs to write like you__. It’s difficult to prompt an LLM to write like you, let alone get it to stop using common AI phrasing and punctuation. Spiral’s Style Engine is the best solution to this problem we’re aware of. An eval runs on every draft Spiral produces, challenging an LLM-as-judge to spot the generated draft among real samples in a blind lineup. Today we’re at 87 percent on this eval, meaning Spiral’s generated draft blends in with users’ samples almost nine times out of 10. When a draft is spotted, the judge explains why, creating a feedback loop to refine the Style Engine further.

## Spiral goes agent-native

As ** Dan Shipper** has

__pointed out__, Claude and Codex are increasingly becoming the central interface for all computer work. So we’ve made Spiral available to agents via MCP, CLI, and API.

To try it out, copy and paste this command in your agent:

Help me set up Spiral, my AI writing tool, so you can write in my voice. Read https://writewithspiral.com/agents.md and follow the steps. In short: add Spiral’s remote MCP server at https://api.writewithspiral.com/mcp/ (Streamable HTTP). The first connection opens a browser to sign in to Spiral and authorize access (OAuth, no API key to paste). Then help me write something.

The CLI, or command-line interface, is personally how I use Spiral the most. After I merge a pull request, a cleanup command runs in Claude Code, which calls Spiral to generate tweets about the new feature for the __Spiral X__ account. Spiral markets itself. This technique is now bundled into the __compound engineering plugin__ in the form of the `ce-promote` command.

In addition to the main `spiral write` command, the CLI and MCP, or model context protocol, expose “personalize” and “humanize” functions. “Personalize” takes a given piece of text and rewrites it in your voice. “Humanize” does a pass to remove common AI tells, including the dreaded __em-dash__ (which Every’s house style uses, hence its appearance in this piece).

Over 500 agents have been connected to Spiral since we launched the integration last month. Those agents are revising blog posts, generating marketing copy, drafting email replies, and more—automatically, and in the user’s voice. On some days, API sessions outnumber web sessions. And as agent-native usage of Spiral picked up, we realized we needed to adjust our pricing model. As a result, we’re adopting a new token-based pricing model, which is more in line with AI apps like Claude, Codex, and Cursor.

## From session limits to token limits

In May alone, Spiral generated billions of LLM tokens, or units of text. While drafts typically range from 500 to 1,000 words, a lot of tokens are processed under the hood to make those drafts great. I’m reminded of the line attributed to French mathematician **Blaise Pascal**: “If I had more time, I would have written a shorter letter.” It takes a lot of tokens to generate a few good ones.

Before this release, Spiral limited the number of sessions, or unique chats, users could start per month. This approach had two problems. First, some users sent hundreds of messages within a single chat, consuming tens of millions of tokens, while using only 2 percent of their session allotment. Second, API users hit their session limit quickly, because the shape of API usage tends to be many single-turn sessions.

We’re moving to a token-based model, which is in line with how billing works in AI products like Claude and Codex. The personal and team plans come with millions of tokens each month. Once those tokens are consumed, it’s pay-as-you-go for extra token usage. Customers can disable extra usage and set their spend cap.

The good news is that the base prices of the personal and team plans are both dropping by $10. Personal plans now start at $15 per month (down from $25), and team plans start at $25 per user per month (down from $35).

The __Every bundle__ remains the best value: For $30 per month you get Spiral but also all of our coverage of AI and four other products: ** Cora**,

**,**

__Monologue__**, and**

__Proof__**. Once you’ve subscribed to the Every bundle, sign into Spiral with the same email address and start writing.**

__Sparkle__## Tell your stories, express your ideas

Technology is at its best when it augments our skill sets—amplifying what we’re good at, assisting with what we’re not. Figma and Canva help designers do better work, and allow people without a design background to manifest what they imagine. Claude Code and Codex help engineers ship more software, and allow people without engineering backgrounds to create the software they always wanted to exist. Our hope is that Spiral helps writers sharpen their work, and allows people without a strong writing background to put their stories and ideas into words.

One Spiral user is a retired musician in Australia. He’s accumulated a lifetime of stories in the studio and on tour. He’d never written them down, because he didn’t quite know how to tell them. Since signing up for Spiral, he’s recorded many chapters of his life stories with the tool’s help. He told me that Spiral has taught him how to be a better storyteller.

That’s what we’re building toward: a writing partner that helps people say what they mean and get better at saying it. Spiral produces good writing fast, but it also explains its writing and editing decisions along the way: the rationale behind rhythm, structure, rhetoric, and more. As my colleague ** Natalia Quintero** observed, the best AI tools teach you things as you use them.

If any of this sounds useful, __try Spiral__. Share your feedback on X (@tryspiral) or get in touch: __[email protected]__.

*Marcus Moretti** is the general manager of Spiral ( @tryspiral).*

*To read more essays like this, subscribe to Every, and follow us on X at @every and on LinkedIn.*

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

Spiral desperately needs some step-by-step tutorial videos and lots more examples on how to actually use the product.
