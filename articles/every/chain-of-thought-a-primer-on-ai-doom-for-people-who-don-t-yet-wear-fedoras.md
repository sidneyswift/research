---
title: "AI Doomsday For People Who Don’t Wear Fedoras"
author: "Dan Shipper"
date: 2023-04-06
url: https://every.to/chain-of-thought/a-primer-on-ai-doom-for-people-who-don-t-yet-wear-fedoras
words: 1817
---

#### Sponsored By: Reflect

This article is brought to you by Reflect, a frictionless note-taking app with a built-in AI assistant. Use it to generate summaries, list key takeaways or action items, or ask it anything you want.

Harry: “It’s just that I always try to imagine the worst thing that could happen.”

Professor McGonagall: “Why?”

Harry: “So I can stop it from happening!”

* — Eliezer Yudkowsky, Harry Potter and the Methods of Rationality*

I’ve been on a bit of an Eliezer Yudkowsky kick lately. Yudkowsky is, of course, the fedora-wearing AI researcher famous for saying repeatedly that AI will kill us all.

He’s also been on a media tour recently. He went on the podcast circuit (Lex Fridman podcast, the Bankless podcast, and the Lunar Society podcast.) He also wrote a widely circulated letter in Time advocating a multinational shutdown of current AI capabilities research, and the lawful destruction of “rogue datacenters by airstrike.”

I’m very excited about AI progress, and working with this technology has been one of the creative highlights of my life. Still, I feel like it’s important to understand the arguments he (and others) are making about its dangers.

I like him because he’s smart and earnest. He’s been in the field for a long time—he’s not some Johnny-come-lately trying to spread AI doom for clicks. He thinks very deeply about this stuff and seems to be open to being wrong.

But even as someone steeped in this stuff, I find many of his arguments—and a lot of the resulting discussion on AI alignment-focused sites like LessWrong difficult to parse. They tend to use words like “shoggoth”, “orthogonality”, and “instrumental convergence” that are frustrating for people who don’t speak Klingon.

So to parse his ideas, I read every article I could get my hands on. I listened to hours and hours of podcast episodes. I even read Eliezer’s 1,600-page Harry Potter fanfiction, Harry Potter and the Methods of Rationality, just for fun. And now, for better or for worse, I feel like I have a little Imaginary Eliezer on my shoulder to help balance out my AI excitement.

The question Eliezer forces us to confront is this: should we really stop all AI progress? If we don’t, will it really end the world?

Let’s put on our fedoras and examine.

## The crux of the doom argument

If you simplify the doom arguments, they all spring from one fundamental problem:

It’s dangerous to build something smarter than you without fully understanding how it thinks.

This is a real concern, and it reflects the current state of things in AI (in the sense that we don’t completely understand what we’re building).

We do know a lot: a vast amount of math and complicated tricks to make it work, and work better. But we don’t understand how it actually thinks. We haven’t built AI with a theory of how its intelligence works. Instead, it’s mostly linear algebra and trial and error stacked together.

This actually isn’t uncommon in the history of technology—we often understand things only after they work. An easy example is fire: we used flint to generate sparks for thousands of years before we understood anything about friction. Another example is steam engines. We had only a rudimentary understanding of the laws of thermodynamics when they were developed.

If you build something through trial and error, then the only way you can control it is through trial and error. This is the process of RLHF (reinforcement learning through human feedback) and related techniques. Basically, we try to get the model to do bad things—and if it does we change the model to make those bad things less likely to happen in the future.

The problem is, trial and error only work if you can afford to make an error. Researchers like Eliezer Yudkowsky argue one error with this alignment process leads to the end of humanity.

The rest of the doomer problems flow from this basic issue. If, through trial and error, you’ve built an AI that thinks you find:

- It’s hard to know if you’ve successfully aligned it because they “think” so differently than us
- They are not guaranteed to be nice
- Even it doesn’t explicitly intend to harm humans it could kill us all as a side effect of pursuing whatever goal it does have

In order to judge these arguments, I think it’s important to start from the beginning. How is it possible to build intelligence without understanding it? We built the software ourselves, shouldn’t we know how it works?

## How is it possible to build intelligence without understanding it?

We usually understand how our software works because we have to code every piece of it by hand.

Traditional software is a set of explicit instructions, like a recipe, written by a programmer to get the computer to do something.

An easy example is the software we use to check if you’ve entered your email correctly on a website. It’s simple to write this kind of software because it’s possible to come up with an explicit set of instructions to tell if someone has entered their email correctly:

- Does it contain one and only one “@” symbol?
- Does it end with a recognized TLD like .com, .net, or .edu?
- Does everything before the @ symbol contain only letters, numbers, or a few allowed special characters like “-”?

And so on. This “recipe” can grow to contain millions of lines of instructions for big pieces of software, but it is theoretically readable step by step.

This kind of programming is quite powerful—it’s responsible for almost all of the software you see in the world around you. For example, this very website is written in this way.

But, over time, we’ve found that certain types of problems are *very* difficult to code in this way.

For example, think about writing a program to recognize handwriting. Start with just one letter. How might you write a program that recognizes the letter “e” in an image? Recognizing handwriting is intuitive for humans, but it gets very slippery when you have to write out how to do it. The problem is there are *so* many different ways to write an “e”:

You can write it in capitals or lowercase. You could make the leg of the “e” short and stubby, or as long as an eel. You can write a bowl (the circular enclosed part of the “e”) that looks domed like a half-Sun rising over the morning sea or one that looks ovular like the eggish curve of Marc Andreeson’s forehead.

For this kind of problem, we need to write a different kind of software. And we’ve found a solution: we write code that writes the code for us.

Basically, we write an outline of what we think the final code should look like, but that doesn’t yet work. This outline is what we call a neural network. Then, we write another program that searches through all of the possible configurations of the neural network to find the one that works best for the task we’ve given it.

The process by which it adjusts or “tunes” the neural network, backpropagation through gradient descent, is a little like what a musician does when they tune a guitar: They play a string, and they can tell if the note is too high or too low. If it’s too high, they tune it down. If it’s too low, they tune it up. They repeat this process over and over again until they get the string in tune.

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

This was great.

I used some of the material to work through the topic with ChatGPT.

My final take-away is rather than shout "stop", and ruminate from the sidelines, people should get involved.

Has anyone posted an alternative letter or motion on something like Futurelife? Something like the below. I think the "pause AI" letter as written is harmful as written.

---

Subject: A Call to Action: Let's Shape the Future of AI Together

Dear [Community Members],

As we continue to witness rapid advancements in artificial intelligence, it is crucial for all of us to recognize our collective responsibility in shaping its development and ensuring its safety. Rather than advocating for a halt to AI progress, we encourage you to actively engage in the conversation and contribute to the development of responsible and ethical AI.

By joining forces and collaborating, we can create a future where AI is not only beneficial but also aligns with our shared human values. Researchers, organizations, policymakers, and individuals from diverse backgrounds must come together to develop guidelines and best practices that reflect the needs and values of our society.

Let us seize this opportunity to make a real difference in the trajectory of AI development. We urge you to:

Learn about AI, its capabilities, and the potential risks associated with its development.

Engage in discussions around AI safety, ethics, and best practices.

Advocate for responsible research and collaboration among AI developers and stakeholders.

Support initiatives that promote AI safety and responsible development.

By taking an active role in shaping the future of AI, we can ensure that its development is not only technologically advanced but also morally and ethically sound. Let's work together to create an AI-enabled future that serves the greater good and benefits all of humanity.

Sincerely,

[Your Name]

[Your Organization/Community]

ChatGPT Mar 23 Version. ChatGPT may produce inaccurate information about people, places, or facts

@mail_8115 glad you enjoyed it! I like this alternative version of the letter, haven’t seen anything like it

Found the Easter egg, erm, spelling mistake. “Tuneed” should be tuned. Keep up the fantastic work!

The problem is because the code wasn’t tuneed by humans, it's really hard to dig into it and understand how it thinks step-by-step.

@jbiggley fixed!! Thanks 😊

The whole AI alignment kerfluffle is kind of silly. AIs operate as designed. The problem isn't good under-aligned AIs that somehow turn misanthropic, it's good well-aligned AIs designed by bad people. One smart depressed teenager can set loose an autonomous reasoning system with SSH access that can wreak total havock across networks. We already have simple computer viruses that exist for no other reason than someone made them. Imagine the next generation of self-replicating destructor agents, capable of reasoning, observation, self-modification, self-protection, armed with the sum technical knowledge of humanity, and set loose with any number of nefarious goals...
