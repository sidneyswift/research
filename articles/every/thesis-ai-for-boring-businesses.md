---
title: "How Main Street Companies Are Using AI"
author: "Sam Gerstenzang"
date: 2026-03-10
url: https://every.to/thesis/ai-for-boring-businesses
words: 1862
---

# How Main Street Companies Are Using AI

We run a funeral home and a medspa platform—not exactly Y Combinator darlings. Here's what we've learned about implementing AI in the real world.

March 10, 2026 Updated June 10, 2026

*The AI hype cycle has mostly rewarded software companies, but **Sam Gerstenzang** is betting on the opposite: operationally complex, real-world service businesses—funeral homes, a medical spa platform. Fresh off an appearance on our podcast *__AI & I__*, the Boulton and Watt partner and former Stripe product leader shares four hard-won lessons for injecting AI into Main Street businesses, including why humans remain stubbornly hard to replace. If you enjoy the piece, watch his episode on X or YouTube, or listen on Spotify or Apple Podcasts.—Kate Lee*

*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

I imagine it wasn’t easy being Costco’s management in the late 1990s. When dot-com darlings like Webvan, Amazon, Pets.com, Kazoo, and eBay—some still with us, others not—emerged, many doubted the warehouse retailer would survive the digital age. But Costco carried on.

I started an incubator called Boulton and Watt, where we start a new software-enabled business every year or two that looks nothing like a Y Combinator darling and a bit more like Costco. Our portfolio includes Meadow, a contemporary funeral home with no physical locations (we use wedding venues during the day), and Moxie, a platform for nurses starting aesthetic medicine clinics (which just raised a $25 million Series C funding round).

These are high-margin businesses in regulated industries—operationally complex, outside the San Francisco zeitgeist, and typically more likely to attract private equity than venture capital, which favors asset-light, high-growth tech businesses. For a while, the AI hype cycle made us look even more counter-trend.

But now, as software gets increasingly easy to build and public SaaS companies’ share prices are down more than 70 percent, entrepreneurs and investors are looking for companies that will continue to be resilient when anyone can build software.

Our thesis is that real-world service-based businesses are going to continue to flourish, and being on the cutting edge of AI will matter as much for the next Costco as it does for the next Lovable. We’ve had real successes, long journeys, and total flops as we bring AI to Main Street. Here are four lessons from bringing AI to a funeral home, a medical spa platform, and an incubator.

**A single database for your entire AI stack**

You don’t need three different systems to run one AI application. Most databases weren’t built for AI—so teams end up stitching together separate tools just to handle search and storage. MongoDB Atlas does both in one platform, scales automatically to handle traffic spikes, and runs across AWS, Azure, and Google Cloud in 125+ regions. Their latest release is faster, easier to scale, and costs less. If you’re building AI-powered apps, start here.

**1-From three months to three weeks: AI accelerates research**

We incubate new businesses with the same steps each time: Pick a market, interview people in that market, and test a solution. Each one of these steps is now AI-assisted, shaving days or weeks off of how we would have run this process previously.

In our most recent search for our third company, we used:

- ChatGPT to pull stats like how fragmented and large a new market was, pull data from public companies to understand margin profiles, and then suggest similar markets for the things we were looking for
- Data-enrichment platform
__Clay__to find relevant customers and kick off a series of targeted emails, which pointed to a landing page that Claude Code had spun up in an hour -
__Granola__to record all early lead calls, and Claude to extract ideas, sentiment, and open questions from the transcripts

When we had interest from potential customers, we’d screen-record the customers’ existing workflows, and use Claude to analyze how the time was spent and opportunities to build new products, and have those products ready to test the next day.

Each step could have taken weeks before. Using AI not only allowed us to move faster, it also reduced the cost of each tiny pivot required to find product-market fit.

**2-Reward outcomes, not AI usage **

We tried to implement “AI initiatives” in the companies we founded, but the first attempt often fell flat and became a “check the box” activity. We struggled with two challenges.

First, AI became an excuse for team members to outsource their judgment to the hallucinations of a madman. If you don’t hold people accountable for the result—not just the method—the critical thinking you hired them for goes out the window. Your team needs to understand that using AI to generate a bunch of bad copy isn’t a good thing. The use of AI itself is *not* the goal—using AI only matters if it can improve the quality and the speed of the work. Hallucinations are *your* problem, not the LLM’s.

And second, AI often requires re-thinking what the work can be, and real examples help show what is possible. Without practical examples of how AI tools could be implemented across the business, the use of AI was incremental rather than transformational. AI usage was limited to typing into ChatGPT and pasting the result into a spreadsheet.

Here’s one example: It was natural for analysts to use AI to clean up spreadsheets or write formulas. But the breakthrough came when a team member used Claude Code to create an entirely new, interactive map-based approach for looking at customer density data. Prominently highlighting this example allowed everyone else on the team to better understand AI’s possibilities and how it could help them solve their own problems.

Similarly, for our engineering team, the first incremental value of AI coding was simple: autocompleting code. But to drive change, we had to teach our engineers how to think differently. It used to be that a senior engineer would scope and break down a complex project into small chunks that a more junior engineer would take on. Now the junior engineers need to be trained to __think like senior engineers__ to build out a more detailed plan that AI agents build.

**3- Customer acquisition: The same story, but different this time**

But so far, it looks a lot like Google search did: people come with high-intent queries, and businesses play the same cat-and-mouse game trying to show up in results. . It’s not a new paradigm—it’s another channel.

For nearly two decades, this was the story of SEO: gaming Google’s algorithms to drive more traffic instead of paying for ads. Similarly, with “Generative Engine Optimization, ”companies are paying to fake interest on Reddit that will filter into ChatGPT.

But this opportunity will come to an end much faster: OpenAI has __started selling ads on ChatGPT__, and showing up in results will quickly become pay-to-play. Meanwhile, __Google’s search revenue is up 17 percent__ over last year. So much for the end of search!

AI-powered lead generation tools like Clay, using signal data from sources such as LinkedIn, are flooding inboxes—you’ve probably noticed a rise in email spam over the last year. We think this will be short-lived: Either you will get so many emails you’ll learn to ignore them, or email providers will get smarter and hide them for you.

The lesson for businesses like ours is to treat every new AI channel the way you’d treat any new channel, period. Test it, measure it, and don’t bet the farm on it just because it has “AI” in the name.

**4-Humans are harder to replace than you think**

Thirty years ago, I believed the internet and computers would eliminate manual paperwork. But it hasn’t happened yet, and the reasons why tell us a lot about AI adoption.

At Meadow, our software emails dozens of insurance claim PDF files a day to insurance companies. The data from these PDFs are then manually entered into their systems. It was an inefficient process even before LLMs arrived, but it’s the only way we can work with these insurance companies. The insurance partners aren’t dumb—the investment of creating, implementing, and moving over customers to an electronic system simply doesn’t outweigh the benefit for them, even though it makes my software engineering brain go crazy.

We’ve also worked with many small businesses that avoid automation for a different reason: They enjoy some of the repetitive work. And even if they saved time, it’s not obvious where they’d invest it.

Then there’s a third barrier: Humans are easier to forgive. Moxie operates a receptionist service for hundreds of aesthetic medicine clinics, powered by dozens of humans picking up the phone to book appointments. We thought it would be a perfect use case for AI—replace this service with voice and chat, and reduce the cost. But when we shared the AI-based service, we saw *greater* churn, even when the human offering was far more expensive. Both made the same number of errors, but customers were much more forgiving of the humans.

The pilot taught us a broader lesson: Getting AI to work in a test is easy. Getting it to work reliably inside your business is a different problem. Even though most of our code is now AI-generated and human-reviewed, the surrounding work—discovering edge cases, rolling out releases, and maintenance—still requires engineering time. And despite the headlines, good engineers are still expensive. So many tasks that seem like obvious AI candidates—like a landing page—only get done if the person who needs them can finish the whole thing without engineering help. The moment it requires integration into our real systems, it goes to the bottom of the queue.

**The bridge between AI and the real world **

Costco survived the dot-com boom by being relentlessly good at what it already did and what its customers needed. It adopted technology when it served its customers better, not because everyone else was doing it too.

That’s our stance with AI. The goal was never to use it—it was always to use the best tools to run great businesses that serve their customers.

*Learn more about how Gerstenzang builds businesses at Boulton and Watt on the *__AI & I__ *podcast. Watch on X or YouTube, or listen on Spotify or Apple Podcasts. *

*Sam Gerstenzang is a partner at Boulton and Watt. He can be found on Twitter and Substack. To read more essays like this, subscribe to Every, and follow us on X at @every and on LinkedIn.*

*We build AI tools for readers like you. Write brilliantly with *


__Spiral__*. Organize files automatically with*


__Sparkle__*. Deliver yourself from email with*


__Cora__*. Dictate effortlessly with*


__Monologue__*.*

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
