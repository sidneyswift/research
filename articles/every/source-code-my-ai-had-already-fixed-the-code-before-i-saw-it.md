---
title: "My AI Had Already Fixed the Code Before I Saw It"
author: "Kieran Klaassen"
date: 2025-08-18
url: https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it
words: 1238
---

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

Before I opened my laptop, the code had reviewed itself.

I launched GitHub expecting to dive into my usual routine—flag poorly named variables, trim excessive tests, and suggest simpler ways to handle errors. Instead, I found a few strong comments from __Claude Code__, the AI that writes and edits in my terminal:

"Changed variable naming to match pattern from PR [pull request] #234, removed excessive test coverage per feedback on PR #219, added error handling similar to approved approach in PR #241."

In other words, Claude had learned from three prior months of code reviews and applied those lessons without being asked. It had picked up my tastes thoroughly, the way a sharp new teammate would—and with receipts.

It __felt like cheating__, but it wasn't—it was compounding. Every time we fix something, the system learns. Every time we review something, the system learns. Every time we fail in an avoidable way, the system learns. That's how we build ** Cora**, Every’s AI-enabled email assistant, now: Create systems that create systems, then get out of the way.

I call this **compounding engineering**: building self-improving development systems where each iteration makes the next one faster, safer, and better.

Typical AI engineering is about short-term gains. You prompt, it codes, you ship. Then you start over. Compounding engineering is about building systems with memory, where every pull request teaches the system, every bug becomes a permanent lesson, and every code review updates the defaults. AI engineering makes you faster today. Compounding engineering makes you faster tomorrow, and each day after.

Three months of compounding engineering on Cora have completely changed the way I think about code. I can't write a function anymore without thinking about whether I'm teaching the system or just solving today's problem. Every bug fix feels half-done if it doesn't prevent its entire category going forward, and code reviews without extractable lessons seem like wasted time.

When you're done reading this, you'll have the same affliction.

**The 10-minute investment that pays dividends forever**

Compounding engineering asks for an upfront investment: You have to teach your tools before they can teach themselves.

Here’s an example of how this works in practice: I’m building a “frustration detector” for Cora; the goal is for our AI assistant to notice when users get annoyed with the app’s behavior and automatically file improvement reports. A traditional approach would be to write the detector, test it manually, tweak, and repeat. This takes significant expertise and time, a lot of which is spent context-switching between thinking like a user and thinking like a developer. It’d be better if the system could teach itself.

So I start with a sample conversation where I express frustration—like repeatedly asking the same question with increasingly terse language. Then I hand it off to Claude with a simple prompt: "This conversation shows frustration. Write a test that checks if our tool catches it."

Claude writes the test. The test fails—the natural first step in __test-driven development (TDD)__. Next, I tell Claude to write the actual detection logic. Once written, it still doesn't work perfectly, which is also to be expected. Now here's the beautiful part: I can tell Claude to *iterate on the frustration detection prompt *until the test passes.

Not only that—it can keep iterating. Claude adjusts the prompt and runs the test again. It reads the logs, sees why it missed a frustration signal, and adjusts again. After a few rounds, the test passes.

But AI outputs aren't deterministic—a prompt that works once might fail the next time.

So I have Claude run the test 10 times. When it only identifies frustration in four out of 10 passes, Claude analyzes why it failed the other six times. It studies the __chain of thought__ (the step-by-step thinking Claude showed when deciding whether someone was frustrated) from each failed run and discovers a pattern: It's missing hedged language a user might use, like, "Hmm, not quite," which actually signals frustration when paired with repeated requests. Claude then updates the original frustration-detection prompt to specifically look for this polite-but-frustrated language.

On the next iteration, it’s able to identify a frustrated user nine times out of 10. Good enough to ship.

We codify this entire workflow—from identifying frustration patterns to iterating prompts to validation—in CLAUDE.md, the special file Claude pulls in for context before each conversation. The next time we need to detect a user's emotion or behavior, we don’t start from scratch. We say: "Use the prompt workflow from the frustration detector." The system already knows what to do.

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

Excellent idea on compounding, thank you. As a non-developer, I am able to share your article with Claude Code, discuss how it applies to our project, and (hopefully) implement it correctly.

@rkilburn I should try this with the project I'm buidling Thanks

The synergy between this piece and programming as advoced with Solve.it (https://www.youtube.com/results?search_query=solve.it+howard) is amazing. I'm anxious to set up three agents. The TDD cycle here is on a different level than TDD in Smalltalk 20 years ago, but the spirit is the same. In modest coding efforts with claude over the past 2 months, I've seen glimpses of the cycle you describe, but I had not realized the power of an extreme cycle that leverages an agentic model. This post was worth my subscription as it pulled so much practce and history together,

As a product designer who recently started coding more, this is so insightful. I particularly feel more at peace because of step 5. My worry has always been on having a baseline level of fundamental knowledge, even as I use AI tools to assist the building process.

I feel two ways about this: it's a good way to show structure and progression to those coming from a non-technical direction. On the other hand, it is just a list of well-known (does not mean always practiced) good engineering practices for engineers.

Of course, replacing humans with machines may speed up the feedback cycle.

Enjoyed this article. It would be great to see a follow piece that talks more about recruiting/hiring/onboarding a first engineer in a "compounding engineering" environment. How to find the best candidates to thrive in this type of environment would be an interesting discussion. I don't think the challenge is limited to converting an existing team.

You mention a lot of stuff in here, and it would be really cool to get more examples of this stuff and references. I don't know what llms.txt is. I'm also very curious how you get claude to add review comments to its own memories.

@nysu.gfx https://llmstxt.org/

Brilliant piece, and should we share this with Dwarkesh, if continual learning , at least in the embryonic stage is solved 😀!

Great read. I shared with GPT 5.0, explained my existing report writing process - and it came back with a tailored approach I can use to continuously improve it.
