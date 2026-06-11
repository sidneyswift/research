---
title: "Stop Coding and Start Planning"
author: "Kieran Klaassen"
date: 2025-11-06
url: https://every.to/source-code/stop-coding-and-start-planning
words: 841
---

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

AI made us sloppy because it made us forget how to plan.

Planning used to be a non-negotiable part of the work: sketching screens, prototyping flows, and writing problem statements. You had to define the scope—what’s in, what’s out, what’s too ambitious, and what solves the problem. Good planning required good thinking, good writing, and collaboration between stakeholders. It was slow, but it prevented expensive mistakes.

When __vibe coding__ emerged, planning went out the window—at first. Why spend an hour planning when you could spend five minutes building the feature? I did it, too. “Make this feature work” was my entire instruction. Sometimes it worked. Often it didn’t. When it didn’t, I’d spend three hours debugging an error that a 10-minute session—asking AI to create a clear outline of the problem and the research needed to build a solution—would have prevented. And I’d be starting from zero with each feature I shipped, instead of the AI improving with each request.

When you vibe code, you prompt, “Add email validation to the signup form,” and hope the AI takes the right route. When you plan with AI, you write: “Research how we handle validation elsewhere in the codebase, check if our email library has built-in validation, look up best practices for user-friendly error messages, then create a plan showing three approaches with tradeoffs.”

One approach ships a feature. The other ships a feature *and* teaches the system how you think for next time. Get this right, and the system learns from every plan. Let me show you how.

## Plans teach the system—code just solves problems

I had five screens of Figma designs staring at me, and a weekend to turn these pixels into a product.

We were preparing for the launch of ** Cora**'s email bankruptcy feature—a free service that clears users’ inbox for them without deleting anything important.

**and**

__Lucas Crespo__**Daniel Rodrigues**, Every’s designers, had turned my ugly-but-functional flow into those beautiful Figma designs: something people would want to use, with clean layouts, thoughtful interactions, and the kind of polish that sets

__software that delights__apart from software that works. Now I had to build it.

As recently as early 2025, that would have meant: Hook up the Figma MCP plugin (a tool that connects design files to code), watch it produce something vaguely related to the design but mostly ugly, then spend the weekend manually fixing it—squinting at measurements, guessing at spacing, writing HTML, refreshing the browser, noticing it’s wrong, adjusting, repeating. Days of work and frustration.

This time, instead of coding all weekend, I spent one hour that saved me days.

I created an AI agent with one job: Take a Figma design screenshot, analyze how to implement it, and output a detailed plan grounded in our patterns, components, and way of building.

Once the plan was complete, I added a second agent to review the work: Compare the Figma screenshot to what got built using Puppeteer (a tool that automatically captures screenshots of web interfaces), note every difference, and keep iterating until they match. Because the plan was clear and detailed, the review agent could focus entirely on execution, instead of trying to figure out what we were even building.

I got five screens, pixel-perfect, including mobile layouts that were never even designed for. The plan guided the work step, and pixel perfection came out the other side.

The next time we need to implement a complex interface, I won’t start from scratch. I’ll use the same system and the same planning workflow, and it will be faster because the system learned from this round.

This is __compounding engineering__: building systems where every unit of work makes the next one easier because you’re teaching the AI what to do. And the fastest way to teach is not through code you write, but through plans you review.

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

Thank you for this great content. How can I reach to the 8 strategies for effective planning text, couldn't find it.

@fcesitler I think it is here in the next article (https://every.to/source-code/teach-your-ai-to-think-like-a-senior-engineer). I haven't read it but I looking forward of to follow from this good introduction.

Wow, a great article. The line that really resonated with me was "Coding teaches, “Here’s how to solve this problem.” Planning teaches, “Here’s how to think about problems like this.”

Do you have a good guide, to something that, showcase how to actually do this. I was hoping for something like a good, guide/walkthrough for how to vide-code and use the planning concept.
