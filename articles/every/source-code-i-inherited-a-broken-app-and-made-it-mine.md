---
title: "I Inherited a Broken App—And Made It Mine"
author: "Yash Poojary"
date: 2025-10-02
url: https://every.to/source-code/i-inherited-a-broken-app-and-made-it-mine
words: 867
---

# I Inherited a Broken App—And Made It Mine

How rebuilding someone else's vision taught me that ownership is the only moat

October 2, 2025 Updated May 25, 2026

*TLDR: Today we’re releasing an early beta of *__Sparkle Search, __*the next step in Sparkle’s evolution from your file organizer to the AI command center for your Mac. The app is designed to keep you in the flow: You can search for your files in natural language, do quick math or unit conversions right from the search bar, and run system actions like quitting distracting apps with a single command. Read on for**Yash Poojary**'s account of how he made it—and made it his own.— Kate Lee*

Most founders start with an idea they can’t stop thinking about. I started with someone else’s.

I’m the general manager of ** Sparkle**, the AI file organizer I’ve spent most of 2025 rebuilding. I

__rewrote the entire codebase__, gave it a fresh look, and shipped new features—including a new version we’re announcing today. But the original vision wasn’t mine. Sparkle was conceived by Every CEO

**Dan Shipper**back in

__2020__, and by the time it reached me, it had already been through four different engineers, passed around like a hot potato because the logic in the app’s original codebase was a tangled mess.

This is very different from the usual founder story: Fall in love with an idea, and then do everything you can to bring it into the world. It’s a story of what happens when you inherit an idea, try to keep it going, and eventually realize the only way forward is to make it your own.

### What it’s like to go all in on something that you didn’t start

I came to Sparkle after building a Mac app called __NightClub 9__, which, in its heyday, ranked in the top 10 on the Mac App Store. It’s an app that displays a live leaderboard of people in your network who are working late, tucked into the menu bar at the top of your Mac.

While it is, in some sense, a productivity app, it skews more toward social media. But I’ve always wanted to go deeper on productivity software as a niche. Ask any of my friends how much it genuinely bothers me when I see them stuck in endless scroll loops on their phones; it makes me feel we’re wasting away our potential. Even my side projects were about helping people focus: __Agent Watch__ to let you know when your AI agents have finished running, __Terminally Online__ to tweet from the terminal so you don’t have to open X. I’ve always chased that rare, electric feeling of being fully focused—a __looped clip of __** Jesse Eisenberg** hammering out code from

*The*

*Social Network*plays in the background while I work—and I want to help others find it too.

So when the opportunity to lead Sparkle came up, I jumped at it. Sparkle helps you stay productive by quietly taking care of one of the most boring knowledge work tasks—organizing your files—freeing you to focus on what you want. It felt like a chance to channel my passion into something real.

### I didn’t invent Sparkle—but I had to make it mine

My first challenge was already laid out for me: Sparkle’s janky codebase that was built in Electron, an open-source framework that made even simple things like adding a paywall painful. __I used AI to rebuild it__ in Swift, Apple’s native language for Mac apps; that also happens to be the language that made me fall in love with coding. A friend and I redesigned Sparkle’s interface over bowls of ramen one night, staying up late and obsessing over every screen until I felt like the app started to, literally, *sparkle*. I listened to users and pulled from their feedback, adding requested features like catching duplicate files in downloads. And without fully realizing it, I was leaving little pieces of myself in the app—my preferences, sense of design, and taste. For a while, it felt like I was breathing life back into Sparkle. I was completely energized.

Until I wasn’t.

As time went on, I started to feel boxed in by Sparkle’s vision of productivity through file organization. I kept trying to make the app more robust—running Sparkle on a local model (instead of remotely like the app currently works), and more smartly sorting files based on their content—but I kept hitting roadblocks. For example, most consumer Macs don’t have enough compute to run a local model capable of organizing a large number of files. And when it came to sorting—which we only felt comfortable running locally—the models tended to hallucinate more than average, making the results too unpredictable to rely on.

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
