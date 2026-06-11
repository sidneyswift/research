---
title: "I Created a Hacker News Simulator to Reverse-engineer Virality"
author: "Mike Taylor"
date: 2025-02-25
url: https://every.to/also-true-for-humans/i-created-a-hacker-news-simulator-to-reverse-engineer-what-goes-viral
words: 1413
---

# I Created a Hacker News Simulator to Reverse-engineer Virality

AI agents cosplaying as online commenters have a lot to teach us

February 25, 2025 Updated January 28, 2026

#### Sponsored by: Every

**Every is hiring!**

If you're interested in any of these positions, email Brandon Gell at [email protected] with a link to your LinkedIn and/or X profile and a paragraph about why you're the right fit.

- A full-stack
**growth marketing lead**to help grow Every and all of our products. If you live to drive top of funnel, this is a dream job. - A
**full-stack AI****engineer for****Cora**. We're building a calm inbox and need an engineer to help us. Launched less than a month ago, Cora has over 1,000 daily active users and 10,000 on the waitlist, and product leaders like Andrew Wilkinson and Mike Krieger love it. - A
**full-stack designer**who can work across our website, products, courses, and other initiatives. You should move fast, be scrappy, and be fluent with AI tools. - An
**operations lead**to help us function more smoothly and efficiently, develop and implement systems and processes, and provide top-notch customer support.

💡Want to learn more about us? Check out this piece by Spaces about our team and approach.

*In **Michael Taylor**’s latest piece for **Also True for Humans**, his column about managing AIs like you'd manage people, he delves into using AI agents for synthetic market research—specifically, he generates AI personas for multiple Hacker News users based on the comments in their profiles. Michael applies the wisdom of the crowd concept to working with AI to determine how agent-based simulations can help us make better business decisions. If you want to try our Hacker News simulator to test your own headlines, join the waitlist at **askrally.com**.—**Kate Lee*

*Was this newsletter forwarded to you? **Sign up** to get it in your inbox.*

Imagine walking into that sales meeting for the 50th time (the first 49 were virtual), ready to handle every objection. Or sending that marketing email to 100 AIs first, to catch any mistakes before you roll it out to your 100,000-person email list.

Whether it’s your advertising, website copy, or social posts, there are real-world consequences to getting your messaging wrong. Why not practice on an AI audience first?

Large language models are unusually good at roleplaying, and if you string enough of them together, you can simulate how the market would react to your business idea, potentially mitigating some of the risk. Instead of talking solely to ChatGPT, you can chat with many GPTs at once, each with a different persona that matches the target audience you’re trying to reach. Pitch your startup to this virtual crowd, and get hundreds or thousands of responses that simulate what would happen in the real world. Since AIs never get tired of you asking, you can run every question by your AI audience and keep iterating on your idea until you’re sure you’ve got something good. Then, you can roll it out to the real world.

I recently explored this idea as a prompting technique I call "personas of thought," but I wanted to see how far we could take this concept to simulate a real-world scenario: testing link headlines on Hacker News. I’ll share how I tested different ideas while building Rally, a synthetic market research tool, going head-to-head with AI agents roleplaying as Hacker News users. And I'll show you a technique for getting AI to stop being polite—and start giving you the brutal feedback that makes your ideas better.

## ChatGPT versus multiple GPTs

ChatGPT responses are the average of all the internet, because that’s what the underlying AI models were trained on. After training, engineers fine-tuned the models to make them prioritize helpful responses as judged by human feedback. This is what makes ChatGPT such a useful assistant, but it can be hard to get out of it a real, honest opinion like you might from a human colleague.

*Source: ChatGPT. Courtesy of the author.*

In this screenshot of ChatGPT, I asked it to compare the (controversial) new slogan for iconic British luxury car company Jaguar, “Copy Nothing,” against its traditional tagline, “Grace, Pace, Space.” The response is a perfect example of how ChatGPT defaults to writing like a marketing textbook instead of responding with a human opinion.

Because ChatGPT has ingested much of the internet in its training data, it has seen how a wide variety of individual people speak, and it can roleplay them with remarkable accuracy. Even with a small amount of direction, you can elicit noticeable differences in the responses.

*Source: ChatGPT. Courtesy of the author.*

Given a more detailed persona based on a two-hour interview with a human, ChatGPT can replicate their answers on surveys with as much as 85 percent accuracy. The recent introduction of so-called reasoning models like OpenAI’s o1 and Deepseek’s R1 (baking the chain of thought prompting technique directly within) showed how powerful it can be to get the model to think through a problem before answering. Much like how chain of thought decision-making helps a model answer logical problems with LLMs, personas of thought are key to solving creative problems with LLMs. It’s a leap from step-by-step thinking to person-by-person thinking.

## Market research with synthetic people

I started building Rally at the beginning of the year to give myself an interface for running these "personas of thought"-type of queries. Normally I would need to copy and paste the question “Which ad is best?” between ChatGPT sessions for each individual AI persona. With Rally, I can send a prompt to more than 100 AI agents at once, and it aggregates their responses. When I ask for feedback on the Jaguar advertising copy, I get a diversity of opinions from different personas instead of the average, fairly dull ChatGPT response. When I’m testing headlines, I can see which one my audience picked most often, learn why, and decide whether I need to further refine what I’ve written.

*Source:*

*Rally*

*. Courtesy of the author.*

And by digging into individual responses, I can see which personas voted for which copy and skim the reasons why. About 40 people are currently testing the tool, and the most common feedback is that seeing the responses from individual AI personas often changes their minds about what their audience would like in real life. It’s like an A/B test, but faster and cheap enough to run every idea past your audience—ideas that you wouldn’t spend the time and money testing in real-life market research, because the cost and time commitments necessitate only bringing your best and most polished ideas to human beings.

*Source:*

*Rally*

*. Courtesy of the author.*

In my own work as a prompt engineer, AIs make excellent judges, even when their own AI-generated ideas aren’t that creative. It makes sense: It’s easier to be a critic than to create. Theodore Roosevelt may have said, “It’s not the critic who counts,” but it’s helpful as the man (or robot) in the arena to seek feedback on how you can improve. The results only need to be directionally correct to be useful, because reading the reasons for which the agents said they liked (or hated) an idea helped me make up my own mind.

## ‘I want a Hacker News simulator’

Every CEO **Dan Shipper** is one of the 40 people beta-testing Rally, with the most common use cases being gauging effective article headlines, gathering feedback on pieces before they’re published, and even serving as the tie-breaker between team members when they disagree on creative direction. Trending on Hacker News can bring tens of thousands of people to Every’s website, so Dan had the idea of using Rally to A/B test Every headlines on an audience that mimics the real Hacker News audience.

*Source: Every’s Discord.*

**Become a ****paid subscriber to Every**** to unlock this piece and learn about:**

- How Rally tests headlines against real Hacker News posts
- Which model delivers the most human-like feedback
- The art of getting AI to roast your ideas

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
