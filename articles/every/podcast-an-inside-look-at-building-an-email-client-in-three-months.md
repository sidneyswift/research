---
title: "🎧 An Inside Look at Building an Email Client in Three Months"
author: "Rhea Purohit"
date: 2025-01-15
url: https://every.to/podcast/an-inside-look-at-building-an-email-client-in-three-months
words: 1934
---

# An Inside Look at Building an Email Client in Three Months

With one engineer—and AI

January 15, 2025 Updated April 22, 2026

*TL;DR: Today we’re releasing a new episode of our podcast *AI & I*. **Dan Shipper** goes in depth with **Kieran Klaassen**, the general manager of Cora—our latest product incubation that lets you manage your inbox with AI—and **Brandon Gell**, Every’s head of Studio and consulting. We get into the inside story of how a one-person engineering team built and launched Cora in three months. **Watch **on X** or **YouTube**, or listen on **Spotify** or **Apple Podcasts**. *

On a summer evening last year, Every entrepreneur in residence **Kieran Klaassen** hotfooted it home from his coworking space. To passersby, Kieran may have looked a little…weird. For one, he appeared to be talking to himself. He walked in short, fast bursts, stopping to think for a moment, before resuming the janky monologue. Those within earshot would’ve heard snatches of “email,” “dread,” “Cora,” “delightful,” and “magic.” Oh, and there was a giant grin on his face the whole time.

Before leaving the office, Kieran had a call with Every Studio head **Brandon Gel**l about a new project—reimagining email in the age of generative AI—and his mind was *buzzing*. After putting his daughters to bed that night, he sat down at his desk, pulled up a transcript of the voice memo he’d just recorded, and started coding.

When Brandon and **Dan Shipper **woke up the next morning, they had a message from Kieran: the MVP of Cora—a whole new way to do email—was ready.

That was the beginning of the exciting, exhausting, *emotional* journey of building a product we’re proud of at Every, and Dan invited Kieran and Brandon on the show to talk about it. They go behind the scenes on how they went from idea to execution on Cora—meandering, occasionally chaotic, and unvarnished (we have the voice memos to prove it). Here's a link to the episode transcript.

Cora, Every’s latest product incubation, is a way to manage your email with AI. It frees you from your inbox by turning all your emails into a sleek, scannable story—a “brief”—twice a day. A month after launch, there are almost 8,000 people on the waitlist. If you want to try Cora, sign up. The team is onboarding new people every day and prioritizing Every paid subscribers. If you want to jump the waitlist, make sure you subscribe if you haven’t already:

**Watch ****on X**** or ****YouTube****, or listen on ****Spotify**** or ****Apple Podcasts****. **

If you want a quick summary, here’s a taste for paying subscribers:

#### Sponsored by: Every

**Tools for a new generation of builders**

When you write a lot about AI like we do, it’s hard not to see opportunities. We build tools for our team to become faster and better. When they work well, we bring them to our readers, too. We have a hunch: If you like reading Every, you’ll like what we’ve made.

## Act I: Finding the right problem to solve

The team intuitively thought that the problem with email was the burden of responding, so they built Cora, an AI email assistant that drafted email in your voice and style. That was the primary function of the MVP that Kieran shipped overnight. Cora was tested internally until the product was really good at drafting email in the user’s voice, but they still weren’t satisfied—the drafts often missed important details.

“[W]e realized that it doesn't matter how good an LLM can mimic your voice,” Brandon recalls. “If it's not in your brain, if it doesn't have the context that you have, it just can't write a good email for you.”

At this point the team had been thinking deeply about email for a while—in Kieran’s words, “we were feeling this idea already for months…it was in the air”—and they realized that responding to email wasn’t actually a problem. As Brandon adds, “[It’s] kind of the pleasurable part of emailing because it means you're maybe progressing something forward.”

They believe that the stress that we feel about email goes beyond that, flowing from the cognitive load of reading, archiving, and organizing emails. That’s the arc of why Cora is centered around briefs, so that you don’t have to worry about cleaning your inbox—it’s neatly delivered to you twice a day. “Cora does draft emails for you, but it only drafts emails that it thinks that it can do a great job drafting, where you're going to have to edit a very small amount,” Brandon says.

Cora’s journey—from ideas to drafts to briefs in three months, owned by a one-person engineering team—reminds Dan that software development is forever changed. Building software isn’t expensive anymore. AI has made it possible to build a product, at least a rough version, in a couple of days, and that makes the question of *what* you’re building even more important. The hard thing isn’t writing code; it’s running experiments and developing the taste to know when you’ve found something valuable.

## Act II: Searching for the soul in software

After nailing down the problem they wanted to solve, the next phase of the team’s journey was building a delightful solution.

### Build products with a point of view

As AI democratizes the process of building software, what counts is building products with soul, ones that reflect a clear point of view. “[A] lot of the most successful businesses that are being built using AI…come from people or organizations that have really strong perspectives,” Brandon says.

Cora is a good example of this philosophy, because telling users to look at their email just twice a day—through the brief at 8 a.m. and 3 p.m.—is a bold position. Kieran explains, “We hear people say, ‘There’s no one else like this, it’s different’—and that can be good, that can be bad, but we're very proud of it.”

Building products that reflect an opinion, or a feeling, comes naturally to Kieran. “I’m a musician, he explains. “I did film music for eight years, conducting orchestras and scoring, and for me, software is very similar…you score a film…to make you feel a certain way…in a similar way with software, you create an experience where it makes you feel or experience something, or tell a story.”

Creating something that makes someone *feel* is a quality that’s hard to define, Dan explains, and one we aspire toward at Every, both in writing and in software. He says that the lines between the two are blurring—software is beginning to resemble content—and in a world where building products is faster and more inexpensive than ever, the ones that make users feel great will win.

### How Kieran used AI to build Cora

Kieran’s philosophy about building a product as complex as Cora in three months is: “Really drilling down to understand what the problem is you're trying to solve, and at the same time being super free and just doing shit.”

Whether he’s building the MVP of an email consumer product or a personal app just for himself, Kieran has the same process. He goes for a walk and records himself talking about his vision for the product, letting his thoughts wander and adding as many details as he can. He transfers the transcript to an LLM of his choice and converts it into a PRD (a product requirement document is an overview of what a new product should do, how it should look, and what features it needs to have).

When it comes to actually writing code, Kieran prefers to work inside AI code editor Cursor. He estimates that 80-90 percent of the underlying code in Cora has been written by AI, a valuable “collaborator just enabling [him] to do things faster.” When Cursor has written subpar code, it’s usually because he hasn’t been clear while defining the problem for the AI. “If I don't understand all the aspects [of the problem], it's very hard for Cursor to do the right thing,” he explains. “It will fill in the details…sometimes it goes rogue, in different directions that are contrary…so you need to be very clear on a direction.” He gives Cursor the right context by proactively editing Cursor rules, which are custom instructions that he’s written for a project.

Other than for coding, Kieran’s model of choice is OpenAI’s o1 Pro model, accessible through the $200 tier. o1 Pro is infamously slow because it uses more compute to “think” harder about the prompt, a quality he sees as an added benefit: “It also makes me chill a little bit because working with AI can be very energizing, but also a little bit stressful because it goes so quickly…and it's kind of refreshing to have to just sit on a chair and do nothing for three to five minutes once in a while.” He uses the model as a thought partner, bouncing off ideas and thinking through strategies with the AI.

## Act III: The future of Cora—biggest wins and challenges

A month after Cora’s launch, we’re proud to have more than 8,000 people on the waitlist. As the team onboards new users, they’ve been getting more and more feedback. One of their biggest challenges is being able to recognize real problems in Cora, given their familiarity with a product that they’ve made.

The current goal for Cora is to make one part of email—managing your inbox through briefs—as delightful for users as possible. As the team continues on the journey of building a product they love, they’re alternately energized and drained. “The reality is that completion state doesn't exist. It exists when you're writing code and you're building a feature, but for building a company—building a product—it's really enjoying the journey and embracing the suck of it and embracing the messiness,” says Brandon.

You can check out the episode on X, Spotify, Apple Podcasts, or YouTube. Links and timestamps are below:

- Watch on X
- Watch on YouTube
- Listen on Spotify (make sure to follow to help us rank!)
- Listen on Apple Podcasts

**Timestamps:**

What do you use AI for? Have you found any interesting or surprising use cases? We want to hear from you—and we might even interview you. Reply here to talk to me!

Miss an episode? Catch up on my recent conversations with star podcaster Dwarkesh Patel, LinkedIn cofounder Reid Hoffman, *a16z Podcast* host Steph Smith, economist Tyler Cowen, writer and entrepreneur David Perell, founder and newsletter operator Ben Tossell, and others, and learn how *they* use AI to think, create, and relate.

If you’re enjoying my work, here are a few things I recommend:

- Subscribe to Every
- Follow me on X
- Subscribe to Every’s YouTube channel


*Rhea Purohit**is a contributing writer for Every focused on research-driven storytelling in tech. You can follow her on X at*

*@RheaPurohit1*

*and on*

*, and Every on X at*

*@every*

*and on*

*.*

*We also **build AI tools** for readers like you. Automate repeat writing with **Spiral**. Organize files automatically with **Sparkle**. Write something great with **Lex**.*

*Get paid for sharing Every with your friends. Join our **referral program**.*

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
