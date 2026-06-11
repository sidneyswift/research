---
title: "Introducing Our First Synthetic Show: ‘TLDR’"
author: "Dan Shipper"
date: 2024-12-11
url: https://every.to/p/introducing-our-first-synthetic-show-tldr
words: 2210
---

*TLDR: We’re launching a new show called *TLDR*. It’s a 3-5 minute AI-generated podcast that quickly catches you up on meetings you missed at your company. We’re releasing our internal Every *TLDR* for you to listen to on **YouTube**, **Spotify**, **or X**. If you want to bring *TLDR* to your company, you can apply to be an early design partner. Preference goes to Every paid subscribers:*

Today, we’re launching a new experiment: a synthetic show called *TLDR* about what’s going on inside our business—and yours.

** TLDR** is a 3-5 minute AI-generated podcast that quickly catches you up on meetings you missed at your company. It’s an easy way to stay up to date on what’s going on at work without having to scroll through endless Slack feeds and email chains, or listen to long meeting recordings.

It takes any meeting recording and turns it into short, compelling (and sometimes spicy!) recap. It’ll tell you key decisions that were made and action items taken. It replays short clips of key moments from the meeting so you can skip the small talk and quickly catch up what’s going on at your company—hands-free.

## How synthetic shows work

** TLDR** is what we call a synthetic show: a new kind of podcast generated with AI by a product we’ve built in house.

In the past, our writers and producers wrote and edited every story and podcast we published. Instead, with a synthetic show, they pour everything they know about making great podcasts into the *prompts* that become the show. Then, you bring the raw material—your company’s communications. Together, we make a story.

It’s a way for us to spread Every’s storytelling to any business in the world. We believe every company has an epic story—and synthetic shows can tell yours.

*TLDR* is an experiment, but if it works, we’ll produce more shows about your company for both internal and external consumption: Think Sunday strategy deep dives, *How It’s Made*-style explainers, or *Acquired*-style histories.

**Automatically turn 1 piece of content into 10—in your voice**

You’re probably creating more than ever before—writing essays, recording podcasts, promoting your work on social media. We want to make it easier for you to move fast. Use **Spiral**, our tool to automate 80 percent of the repeat work that comes after creating—social media posts, YouTube descriptions, newsletter blurbs, and more.

## Listen to our internal Every ‘TLDR’

We want you to get a sense of what *TLDR* is, so we’re making our internal Every *TLDR* available publicly for you to listen to.

It tells the story of our weekly Every Studio standup where all of our entrepreneurs in residence (including Naveen Naidu, the EIR who built *TLDR*) meet to discuss what they’re working on.

The episodes are fun to listen to. I’m always slightly nervous and excited to hear a colleague's name mentioned, and to hear how the show summarizes what they said and how they said it—it’s like how it would feel to see or hear them on TV or on the news. There’s something different and compelling about having the inner workings of your company reflected back to you in this way. And it’s useful—I genuinely stay better informed about what’s going on inside of Every with TLDR.

All of the recordings are available publicly on YouTube, Spotify, and X.

Now that we have *TLDR* working internally at Every, we want to bring it to you. We’re looking for 10 early adopters to work with us as design partners—to help us tell stories about your company as a synthetic show. We’ll give preference to paid Every subscribers (so subscribe!) and people working at companies we think are interesting:

*TLDR* was built end-to-end as an experiment by Every EIR Naveen Naidu, who’s been working at the intersection of podcasts and tech for a while. He came to Every working on a product called PodBrew, which turned news articles into podcasts, and we evolved it into TLDR.

If you’re curious about synthetic shows, here’s a bit more about how and why we built *TLDR*.

## How we built ‘TLDR’

You’ve probably seen AI-generated podcasts through products like NotebookLM, which turns your uploaded source documents into an NPR-style show. When Naveen started working on the original version of *TLDR*, we thought it would be pretty easy to build something of similar quality.

But it turns out, making a great synthetic show is challenging. It requires both building a technology pipeline to turn meeting transcripts into first scripts and then audio—*and* great prompting to make the scripts good.

### The models we used

Naveen tested three different models for script generation: GPT-4o, Claude, and Gemini 1.5 Pro. He found that Claude was a better writer than 4o, but that it often missed interesting or important pieces of the transcript when creating the script. Gemini was best for consistently pulling out everything important and seemed to pay better attention to all of the different parts of the context.

For simplicity, he stuck with Claude because it’s the best writer, but in future versions we may use a mix of models.

Naveen also tested a few different voice models, including those from OpenAI, ElevenLabs, and Google AI Studio. But he ended up picking Play.ai because the voices sound more natural and conversational. They felt more appropriate for the kind of vibe we were trying to create.

### Model pipeline

In order to generate the script for the show from the meeting transcripts, we use a cascading prompt system with three prompts: introduction, body, and outro sections.

First, we generate the introduction. We feed the meeting transcript and our intro prompt into Claude. The intro prompt is a few-shot prompt that contains a script written by Every lead writer Rhea Purohit.

Once we’ve generated the intro, we feed it—along with the original meeting transcript—back into Claude and prompt it to generate the body of the script. This is where the host summarizes the meeting in detail.

Then we take the intro and body and pass it back one more time to Claude to generate a conclusion. Once the whole script is generated, we pass it to Play.AI to create the audio.

### How it all comes together

We record our meetings in Zoom and use Zapier to post the meeting transcript into our synthetic show creation tool. About an hour after any meeting finishes, we get a notification in our Spotify and Apple Podcast players that a new episode is live.

It’s a pretty cool experience! I listen while I’m walking to get coffee in the morning.

## Why we built ‘TLDR’

A year and a half ago I wrote:

“From the beginning of Every, we’ve noticed that the best ideas in business are never written down—they’re locked up in people’s heads…Part of the mission of Every is to bring these ideas to life on the page—but for now, it’s been slow, difficult, and expensive…AI changes this equation significantly.”

Ever since then, we’ve been looking for a way to put this idea into practice. When NotebookLM’s AI-generated podcasts came out, I realized the time might have finally come. *TLDR* and synthetic shows are our first foray into this territory—expect to see more in the months and years to come.

We believe every business has a story, but, unfortunately, most never get told.

Together, we hope to change that.


*Dan Shipper**is the cofounder and CEO of Every, where he writes the*

*Chain of Thought*

*column and hosts the podcast*AI & I.

*You can follow him on X at*

*@danshipper*

*and on*

*, and Every on X at*

*@every*

*and on*

*.*

*We also **build AI tools** for readers like you. Automate repeat writing with **Spiral**. Organize files automatically with **Sparkle**. Write something great with **Lex**.*

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

I must be one of the few people who is near-literally "allergic" to this kind of format. The NotebookLM output has largely been truly awful (or at best funny in a laughing-at, not laughing-with way) to me. Not in how "real" it sounds, but in how hollow it makes the subject and content feel, even when it's something that otherwise interests me. I am far too distracted by the system's attempts to mimic genuine and interesting banter, asides, etc. So I guess I'm not someone who can fairly evaluate this new product idea, it's definitely not one I would have thought of or would probably use myself. 😄

That said, what my negative reaction to the actual content/experience makes me think of may actually be interesting. First the question: do most people react in a similar way to this kind of format (the literal podcast emulation), and is it positive? Perhaps there are others with varying degrees of neutral-to-poor reaction, like me. And if so, might the future of this approach actually be to tailor the format to each listener's preferences?

For me I want the "fluff" and attempts at building a story to be cut, they feel artificial and forced (I'm not saying that's "true", that's just how it makes me feel about the content). If this were a more true summary of a meeting, without the fluff but also without being dry, I think I would personally respond to it a lot better. To me this means making it as concise as possible so that each thing that is said *is* meaningful and interesting in itself, without having to frame it in some particular way. That obviously includes actionable info as well as literal action items, but also novel and interesting quotes, etc.

Anyway the idea of a listener-specific approach to this is interesting to me, and I wonder if it's something you're already thinking about/working on.

@Oshyan thank you for such a thoughtful response to something you instinctively don't like! a rare and beautiful thing on the internet.

I definitely resonate with some of these issues, and do find some of the fake casualness off-putting—sort of like trying to create vegan meat instead of great salads. I think this format and these voices will evolve in the "salad" direction—where you can definitely tell they're AI, and use the genuine strengths of AI to create something distinct from human podcasts.

I definitely think there's room to go even further in the utilitarian direction with this format specifically, but I also think over time we'll get more and more comfortable with AI telling certain types of stories and I'd love to be able to explore that too.

Again thanks for such a great comment! Excited to hear what you think about this as we evolve

@danshipper vegan meat is a great analogy! 😄 And yes, I think I'm yearning for the "something distinct from human podcasts" that leans into AI's strengths. I haven't seen that yet, at least for audio, so I'm quite curious to see what comes next... I'll be watching for sure!

@Oshyan same here!

I like that you guys are exploring new media formats. May be a hit, maybe not but its the kind of iterating in public that I think we'll see more of over time

@cam.burley thank you!! yeah, totally! many of these won't work but we hope we discover a few that feel amazing. appreciate you coming along for the ride!

I think this is fantastic. I'm a heavy user of NoteBookLM and find the ability to summarize content this way interesting, insightful, and entertaining. This is a great variation because of the focus on meetings. I also really like how you took the time to explain the process. I am curious about the decision to stay with Claude versus Gemini Pro given that you find it summarizing better. I will say that I have found Claude to be the best writer historically (much better than ChatGPT) - but the new Gemini experimental 1206 model is getting pretty close.

Thanks again for doing these things and continually showing us the art of the possible.

@smith.stephen.m thanks Stephen! on your claude vs. gemini pro question I'll leave that to Naveen, but if I had to guess, right now, the harder task is good writing rather than information retrieval—so even if Claude sometimes misses stuff that's less apparent than stilted writing.

will have to keep trying with gemini, their progress has been impressive!! thanks for coming along on the journey :)

it is really good. the article also said something about the product podbrew. it turns news articles into podcast. how to get access to podbrew.

Wether one likes the audio format, I think AI is 'squishy' enough to give it to people in a format they love: podcasts, video, email, slack etc. Thinking this further, let's say for orgs beyond 50 people where alignment becomes harder a meta level podcast that checks for alignment across the business could be super interesting and valuable here too.
