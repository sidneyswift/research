---
title: "Freeform: A New Experiment From Every Studio"
author: "Cassius Kiani"
date: 2025-01-07
url: https://every.to/source-code/freeform-a-new-experiment-from-every-studio
words: 2085
---

*TLDR: Today we’re sharing the latest experiment from **Every Studio**: **Freeform**, an AI-powered tool for creating smarter, more adaptive forms built by entrepreneur in residence **Cassius Kiani**. Try it out yourself with a 2024 reflection and let us know what you think.—**Brandon Gell*

When I learned that Meta is going to launch AI avatars on its platforms for users to interact with, my first reaction was that it’s a bold idea (and I love bold ideas).

My second reaction was, “Why?”

Facebook grew into a trillion-dollar business because it tapped into a universal need for human connection. It wasn’t about deep technology—it was about bringing people together. Even features that faced backlash, like the News Feed, were designed to strengthen that sense of connection, making it easier to see what friends were up to in real time. Meta has some shiny new tools—AI avatars, the metaverse—but it feels like they’re searching for excuses to use them for their own sake, rather than to delight and connect real people.

An easy way to frame this situation is that they’re swapping problems for possibilities. It’s like designing a house that pushes boundaries in architecture but is only occupied by ghosts. And I say this as someone who has swapped problems for possibilities before.

I worked with the team that created the first-ever decentralized autonomous organization (DAO), because I was nerd-sniped by the blockchain’s promise for decentralized governance. It felt like the future—democratic systems tied to mutual upside. But what did I learn? People didn’t want governance; they wanted accountability. When things went wrong, they didn’t want to be in charge—they wanted someone to blame. The most common question we heard was, “Who’s running this?” When the answer was, “You, the DAO holders,” the excitement faded fast.

#### Sponsored by: Every

**Tools for a new generation of builders**

When you write a lot about AI like we do, it’s hard not to see opportunities. We build tools for our team to become faster and better. When they work well, we bring them to our readers, too. We have a hunch: If you like reading Every, you’ll like what we’ve made.

I made similar mistakes while building a new product in legal tech. I thought inefficient law firms were desperate for innovation. But lawyers weren’t looking for ways to save time; they were looking for ways to bill for more hours. Every time we found a clever way to save them a few million dollars by reducing labor costs or reducing how long certain tasks would take, we were met with, “...and how will we bill a client for this?”

I now realize there’s a gap between what people say, what they do, and what they want. And maybe this is where Meta’s AI avatars will prove me wrong—because quite often, you have to build before you really learn what people want.

I learned this lesson most clearly while working in healthcare. Patients, I discovered, often just want to feel heard. Sometimes, that feeling is more important than the treatment itself. When patients felt heard, they were more likely to stick to their treatment plans, which led to better outcomes.

One of the ways we worked to improve communication was by rethinking patient forms. Traditional forms frustrate everyone. Patients have no idea what they’re being asked or how the information is relevant to their treatments. Doctors often feel that patients don’t give enough information or misinterpret the intent behind the question. The result? Insufficient information, misaligned care, and less trust in treatment plans.

There was a tension that AI could help resolve—not by automating for the sake of it, but by improving the experience for both patients and doctors. Imagine forms that adapt in real time, asking smarter questions based on a patient’s answers. Patients would feel understood, doctors would get actionable insights, and both sides would win.

My hunch is that this communication gap exists across forms in general. In most contexts, forms are critical connection points between people and systems, yet they’re often static and impersonal. We design forms like we design crockery: We assume it’s fine for it all to be the same. But really, forms should be more like meaningful conversations, rather than watching a recorded lecture.

That’s why I’m working on Freeform, an AI-powered tool I’m building to experiment with creating adaptive, dynamic forms. No two Freeforms will ever be the same. The questions adapt in real time based on your answers, diving deeper into interesting insights or stepping back when engagement fades. It’s more like a great conversation—guided by structure but full of unexpected turns, where everyone comes out better for it.

Freeform is my attempt to focus on problems rather than possibilities. If it works, it could be a blueprint for better tools that help people better connect with systems (and each other). But as always, I’ll only know if I’ve found a real problem once it’s out into the real world.

If you’re curious, give Freeform a spin with our Every Archetype experiment, which will guide you through a reflection of 2024 to discover your archetype for the year. It’ll help me learn whether this is something other people actually want, or just another shiny distraction.

Parting wisdom? Solve problems rather than possibilities. Get that right, and tools will follow.

*Thanks to **Katie Parrott** for editorial support.*

*Cassius Kiani** is an entrepreneur in residence at Every. He cofounded the nonprofit Pledges and health tech company Mora Medical. *

*To read more essays like this, subscribe to **Every**, and follow us on X at **@every** and on **LinkedIn**.*

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

Powerful observation and an important insight about the ubiquity of forms. Possibility or problem? TBD!

What does this end up looking like on the "Results" & Analysis side of the form?

Do the questions follow any pattern or guidance or they just question 1 -> question 10 and each question + response are completely unique?

@John Wetzel you can get the model to assign how many questions to ask, and you can even adjust this down the line too (based on responses) in a semi-reliable manner. In this version, I hardcoded the question number so I could ship this a little faster (and reduce the total surface area too). All questions are unique based on answers, all I need to do is seed the model with a single question hardcoded question, and then the rest is LLM magic.

@cassius makes a lot of sense.

I'm also curious about how you're imagining it would work as an Admin viewing all responses. In a traditional form tool, it's a table with a column for each question and rows for responses.

@John Wetzel that's a good question and it's one I'm trying to answer rn

Interesting idea! I would love to hear what use-cases you have in mind because most of the examples you bring up quickly raise problems/concerns in my mind, e.g. consistency of data gathered when the questions are all different, biasing effects, etc, etc. It's obviously not an approach that's appropriate when gathering comparable data is the goal (which seems like is *often* the case). I know there are other scenarios where forms are needed and often used, but I'm not totally seeing the *value* here, much as the concept intrigues me.

The experience of testing it just now was interesting and actually insightful with this self-reflection prompt. It feels a bit like a formalized and directed AI chatbot experience, which is not a bad thing. Btw I got stuck at the "Save your answers?" part; nothing happened when I told it to Save. After Refreshing it then prompted me correctly for my name and email and I was able to save it. However "saving" just emailed me a link to my answers *on your site*, which is definitely not what I hoped for. I really think the answers should be in the body of the email, or at the least an attachment (text/.md). Just in case that was supposed to happen I clicked the link and tried again to send it to myself, this time it got stuck after I put in my name and email, not showing any confirmation or moving to the next screen. I pressed the button twice so got 2 emails. Refreshing again made it progress to the Summary/Archetype screen. I'm on Windows 10, Google Chrome, using uBlock Origin.

@Oshyan in my mind, it depends on your goal.

When you're doing user research, or learning about problems (from health to wealth) it seems like it’s quite hard to ask the right standardised questions to get the right informaiton. Even when you want comparable data, it’s not obvious to me that means that the questions (or even answers) need to be standardised at responder level el.g. the person who answers. I would agree that at some stage standardisation helps, however when this happens is an open question in my mind. My hunch is that there’s valuable signal which is lost in static, standardised questions. At least, that’s what I saw in healthcare.

Cognitive Task Analysis (CTA) from Gary Klein is another reasonable example here. In CTA, you ask unstructured questions to learn how experts make decisions. CTA has a structure e.g. the practitioners know what success looks like, however you need to ask the right questions, then double-click on the right spots in the answers to get any value. Standardised questions and answers here would seem to lead to noise, rather than signal.

My hunch is that in a few years, models will bet better at asking tailored questions than any static form (which is why I’m exploring Freeform).

Thanks for the feedback on this Freeform. Static links were a conscious decision, because it was faster for me to ship this. Also, that’s a strange issue re: getting stuck. I’ll try to resolve.

@cassius Thanks, interesting examples! Survey design is such a challenging topic even without variability between what is prompting each respondent, but it's true that absolute consistency or comparability is not always the goal. Another interesting angle to consider is that survey design might in part be so difficult because the same question (the same way it is posed) can elicit not only different *responses*, but even different *understandings* in different people. From that simple idea one can perhaps see the seed of a proof that surveys as a means of gathering consistent data is inherently limited. Getting from that to confidence that AI can do a better job of achieving comparability *via* customization per-respondent is another stretch, but not out of the question. I can imagine analysis of millions of survey question:answer pairs with demographic or even individualized (but anonymous) data on respondents that might help an AI optimize for consistency in question interpretation by all survey respondents, for instance. A simple example of that would be customizing the sophistication of the language for the reading level of the respondent, but it could get much more sophisticated than that. All very theoretical, but intriguing to ponder!

@Oshyan thanks for these thoughts, there's lots for me to muse on here. I appreciate this.

Fascinating experiment. I was wondering when it was going to end, so an indicator of how many more questions would be good. I see this used for problem-solving or negotiations where it can help walk through dynamic questions based on previous answers. This could also be used as a job applicant interview engine (I built a set of prompts for similar activities) for both the employer and job applicant.

@paul.carney thanks Paul, did you see the progress bar at the top? If you didn't, it sounds like there's an issue I'll need to fix. What device and browser were you using?

Also, I've mused on job applications as well. If you have any fun ideas here, I'd love to hear them.
