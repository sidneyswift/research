---
title: "Meet Your New Finance Intern: GPT-4"
author: "Evan Armstrong"
date: 2023-05-17
url: https://every.to/napkin-math/meet-your-new-finance-intern-gpt-4
words: 847
---

The finance intern—a tale as old as time. They work 100 hours a week, snort Adderall in the bathroom, and wear boat shoes in December. For this, they demand $160K a year. Now there is a new breed of intern that'll get you the numbers you need without the snarky attitude.

In fact, it's really friendly, it never sleeps, and it costs 20 bucks a month. It's still mind-bendingly stupid every once in a while though. I’m talking about GPT-4.

I think that with existing AI tools, a finance professional can *increase* *their individual output by 50%*. Workflows that require entire teams will collapse into one dude’s afternoons. It means we need far less entry-level or outsourced staff at banks, consulting firms, and investment funds. The software programs that are so dominant in finance today may be reduced to mere data storage programs.

Today I would like to show the results of two of my experiments that have taken my thinking here:

-
**Analysis:**How you can use ChatGPT to build models, analyze P&L statements, and then build visualizations -
**Synthesis:**How you can use Anthropic’s Claude to quickly parse through 10-K documents

Don't get too excited about GPT making you a ton of money via stock picking. Instead, its first job will be automating the tedium of analysts’ lives with improved workflows. While this is distinctly less sexy than stock picks, it has far bigger implications. By changing the types of labor that a finance professional does, it dramatically changes the skills sets of those who succeed in the industry. You need to be paying attention, the world is changing fast.

### Analysis

As my colleague Dan argues, GPT-4 is a reasoning engine*. *Think of it as the world’s smartest and dumbest intern: It can do more than you think but tends to make up stuff if your directions are unclear.

We will guide our intern with an OpenAI tool called code interpreter. For the unfamiliar, the code interpreter is a “Python interpreter in a sandboxed, firewalled execution environment.” To translate: You can upload a spreadsheet and then the software can write code that will interpret, analyze, and visualize the data in the file.

So let’s say, entirely hypothetically, that I had a bank’s financial model for Meta. I won’t say which bank (because obviously I don’t have this), but let’s say it rhymed with Schmolden Schmacks. I would just upload the bank’s financial model and let it start to analyze the content:

It then goes on to analyze and categorize all 14 tabs in the model for things like the income statement or valuation. It does so in 10 seconds, which is faster than I could do it.

*Note: I’ll have a few screenshots in here; you can read or ignore them, they are supplemental. *

From there it is pretty simple. I ask some questions in plain old English. The AI will interpret my questions and then solve them with Python. Let’s pretend I’m not super familiar with the P&L of the company, so let’s start with the basics. I ask if it can “tell me how the company is doing.”

ChatGPT then goes on and writes Python code to analyze the contents of the relevant sheets. Notice how it selected the important tabs *without my telling it which ones matter. *Its reasoning capabilities are good enough that it knows the value and relationships between the tabs, like the income statement and the cash flow statement. To do this, it runs little snippets of Python picking apart the spreadsheet. If you want to double check its work, you can always open the code—by default it is hidden.

By doing so, it is able to totally analyze the company's performance in <30 seconds. It would take at least 30 minutes for me to do a similar task. Ultimately, a company’s performance is a rather subjective question. I was testing whether the program, which is connected to the internet, would be able to find what matters. It does it beautifully, immediately identifying the “Family of Apps” category that Facebook uses. This is the most important lens by which to view the company because it separates the ad business from the VR business. That Code Interpreter was able to find the correct row in this 14 spreadsheet model and tell me why it mattered in less than 30 seconds is pretty wild.

This is pretty amazing! But we can go further.

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

It isn't a reasoning engine. The human is the reasoning engine, and the human is using GPT-4 to have a dialectical thinking process. Why do y'all get this so wrong?
