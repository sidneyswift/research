---
title: "The Next Big Programming Language Is English"
author: "Dan Shipper"
date: 2024-05-02
url: https://every.to/chain-of-thought/i-spent-24-hours-with-github-copilot-workspaces
words: 1006
---

*Was this newsletter forwarded to you? **Sign up** to get it in your inbox.*

GitHub Copilot is like autocomplete for programmers.

As you type, it guesses what you’re trying to accomplish and suggests the block of code it *thinks* you’re going to write. If it’s right—and very often it is—you press Tab and it’ll fill in the rest for you. Launched in 2021, a year or so before ChatGPT’s arrival, Copilot was the first breakthrough generative AI use case for programming that really took off.

If GitHub Copilot is like autocomplete, GitHub Copilot Workspace—currently in limited technical preview—is like an extremely capable pair programmer who never asks for coffee breaks or RSUs.

It’s a tool that lets you code in plain English from start to finish without leaving your browser. If you give it a task to complete, Copilot Workspace will read your existing codebase, construct a step-by-step plan to build it, and then—once you give the green light—it’ll implement the code while you watch.

Put another way, it’s an agent. It’s similar to Devin, the AI agent for programming whose launch announcement went viral a few months ago, and which was reportedly seeking a $2 billion valuation in a new fundraising effort. I haven’t gotten access to that yet (shakes fist in Devin’s general direction!), but I do have access to Copilot Workspace.

Over the past 24 hours, I’ve put Copilot Workspace through some of its paces. I tried to have it build a large, complex feature on its own, but I also asked it to do smaller, better-defined tasks. My goal was to see what I could ask of it, what kinds of tasks it could handle, and when I might choose to use this instead of ChatGPT.

The short answer is: This kind of product is the future of programming. The long answer is below.

## How Copilot Workspace works

I’ve been working on an internal tool that we use at Every called Spiral. It allows users to build and share prompts for common AI tasks—but more on that in a future essay. I fashioned an ugly tribal tattoo-looking logo, and I wanted to replace it with a new one created by Keshav, one of our talented designers.

This is one of those changes that isn’t very hard to code, but it’s a little annoying. You have to make sure the logo looks right in context and doesn’t break any of the styles of the elements around it. It’s one of those all-too-simple tasks that I also usually procrastinate doing until I really need to.

So, I figured it was perfect for an AI. I decided to try Copilot Workspace—from here, simply referred to as CW—to see how it would do.

**Create a task**

First, I opened up CW and created a task. A task is a natural language description of what you want CW to build:

*Source: Screenshots courtesy of the author.*

You’ll notice that the task description I gave it has details such as the file I want it to modify, where I want the logo to appear, and the file name of the logo image. I experimented with different prompts (and looked through the GitHub documentation) and learned that giving it more detail should lead to better results.

Once I inputted the task, CW processed it and created a specification: a map of the current state of the codebase, and a set of criteria for what success looks like.

**Specifying out your idea of success**

CW creates a specification through a process that is sort of like what I do before I leave the house to grab coffee: I tap both of my pants pockets to make sure I have my phone, AirPods, wallet, and keys. In a sense, I am asking my pants, “Do you contain all of the essentials I need in order to leave the house, purchase a coffee, and make sure I don’t get locked out?”

Depending on how they reply—bear with me—I know whether each item is either present or missing. This helps me to create a plan to gather the things I need to find in order to successfully complete my mission. (Note to self: Your wallet is always wedged in some physics-defying configuration between the couch and the wall. Look there. Not there? Look again.)

In a sense, CW does this, too. Given the task you assigned it, it attempts to figure out the current state of your codebase (to put it in pants terms, it taps the codebase and finds the wallet and keys are missing). Then it proposes a set of tests for what your codebase *should* look like when the task has been completed properly (the wallet and keys are now safely slotted in their proper pockets).

To make it even easier, it does this in normal English:

Plus, you can edit each step of this process and, if you want to, add your own ideas in natural language. Basically, you can give CW your own test criteria for what success should look like so that it will check against it as it writes code.Once you’re satisfied with the specification, you move on to the plan.

**Creating your plan**

If the specification stage is about figuring out *what* needs to be done in your codebase, the planning step is *how* it will be done. At this stage, CW gets into the nitty-gritty details of your codebase and writes out the changes it will make to each file:

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

Great... Now you can stop bugging me about "Every" bug and let me "Sparkle" 🤪
