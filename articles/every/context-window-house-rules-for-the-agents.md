---
title: "House Rules for the Agents"
author: "Every Staff"
date: 2026-04-05
url: https://every.to/context-window/house-rules-for-the-agents
words: 2559
---

# House Rules for the Agents

Plus: We Vibe Checked a reimagined Cursor

April 5, 2026 Updated April 28, 2026

*Hello, and happy Sunday! Was this newsletter forwarded to you? Sign up to get it in your inbox.*

## Fine tuning

**Anthropic’s OpenClaw problem**

When Anthropic’s new Claude Max restrictions started circulating, the company named one tool specifically: OpenClaw. “Wtf,” wrote CEO **Dan Shipper** in the Every Slack. The policy seemed to say: If you access Claude through OpenClaw, your subscription no longer covers it the same way. “They disallow specifically OpenClaw from subs,” head of tech consulting **Mike Taylor** wrote. “You have to pay for extra usage. Pretty lame.”

Mike’s best explanation for why Anthropic drew the line where it did centers on prompt caching, a cost-control mechanism that works by reusing previously processed conversation text. When it works, it keeps inference costs low. When a third-party tool changes even a single token in the prior conversation, that reuse breaks, and Anthropic has to reprocess the entire conversation from scratch. “Prompt caching keeps cost down by saving the previous tokens that have already loaded,” Mike explained. “If a provider breaks the cache by changing even one token of the previous saved conversation, you have to reprocess the entire old conversation.” He also noted that Claude Code co-creator **Boris Cherny** had already opened pull requests to improve OpenClaw’s cache efficiency, suggesting the problem was technically solvable. Anthropic enacted restrictions instead.

What the team disputes is not that Anthropic has a reason—it’s that singling out one app by name is the wrong response to it. The consistent argument across the Every Slack was that if cache-breaking usage costs more to serve, make those users pay more: Meter the consumption rather than ban the interface. “A better middle ground is not to ban OpenClaw users,” head of platform **Willie Williams** argued, “it’s to give me a certain amount of tokens I can use as part of my subscription, and then charge me overages if I go over.” Dan framed the same principle from the user side—“I think of AI subscriptions like Claude and ChatGPT as being like cell phone plans that give me a certain amount of data”—and Mike extended it to the infrastructure side, invoking net neutrality: Verizon shouldn’t get to slow down Netflix because Netflix uses a lot of bandwidth. The argument, in every form it took, was the same: Charge for what costs you money, not for which app someone uses to spend it.

There is also a business problem that goes beyond annoyed subscribers. Restrictions like this do the opposite of building loyalty—they create churn. Anthropic may have a legitimate business reason for drawing a line somewhere. But drawing it in a way that feels confusing and selective is not the way to win the platform war between model providers and the tools built on top of them.—*Kate Lee*

##### AI video analysis just got way cheaper

AI video analysis is rarely discussed in AI hype circles today. Only one frontier model—Google’s __Gemini__—can natively watch and understand what’s happening in a video. It’s more like rocket flight than air travel: not an established industry getting cheaper, but a new capability on the verge of becoming practical. And something just shifted that could blow the door open.

When GPT-4V (vision) launched at the end of 2023, I used video processing to identify what strategies were being used in video games at a cost of roughly $6 per hour—and that was after a lot of complex engineering to split videos into frames at 0.5 frames per second (FPS) and feed them through as images. Google’s recently released open-source __Gemma 4 model__ does this much more efficiently: I estimate the same task now costs about $0.14 per hour at 2 FPS—capturing four times as much detail, with none of the hacky engineering workarounds that used to be necessary.

The math: At current token pricing ($0.14 per million input, $0.40 per million output), one hour of video at 1 FPS with 70 tokens per frame runs about 252,000 input tokens, or roughly $0.04. Bump to 2 FPS with richer frames (140 tokens each) and you hit ~$0.14 per hour—still a 97 percent cost reduction from 18 months ago.

The cost of understanding what happens in a video has dropped by a factor of roughly 40, while the quality of that understanding has improved dramatically. That is the kind of price collapse that creates entirely new categories of application. Imagine live video streaming commentary of your kid’s soccer game, a Ring doorbell that tells you who’s at the door, or an automated review of thousands of hours of security footage to find a missing person.—*Mike Taylor*

## Knowledge base

__“Vibe Check: Cursor 3.0 Bets Big on Agent Orchestration”__*by Dan Shipper, Katie Parrott, and Mike Taylor/Vibe Check:* Cursor totally rebuilt its product around agent orchestration rather than code editing, and we came away feeling that the new Cursor still has maturing to do. The desktop app is fast, the local-to-cloud workflow is impressive, and its new model, Composer 2, is concise and snappy. But missing basics like file navigation and branch management left even power users like ** Cora** general manager

**struggling. Read this for the breakdown of where Cursor 3.0 stands against Claude Code and Codex.**

__Kieran Klaassen____“Seven Things I’ve Learned Getting Companies to Use AI”__*by Mike Taylor/Also True for Humans:* Most companies mandate AI adoption and wonder why it doesn’t stick. Every’s head of tech consulting argues you should do the opposite: Find the people who are already bought in, get them IT access and budget approval, and let their results pull everyone else forward. His other lessons include building on the model providers directly instead of buying third-party tools, setting stretch goals that force people to think about where AI can save them time, and training every individual contributor to be a manager of agents. Read this for the whole playbook from his consulting engagements.

__“What I Learned Onboarding Our AI Project Manager”__*by Nityesh Agarwal*: Every’s consulting team built an AI project manager named Claudie that saves them 15 hours a week tracking client work across email, documents, and meeting transcripts. Getting her there meant rebuilding her multiple times, figuring out why she kept dropping key details, and writing her an employee handbook she reads on every startup. Read this for the full architecture and the management lessons that apply to your next agent hire.

🎧 __“If SaaS Is Dead, Linear Didn’t Get the Memo”__*by Context Window/Laura Entis:* Agents can now create tasks and manage workflows inside Linear just like human users, and companies like OpenAI and Coinbase run their agents on it. In this week’s * AI & I*, Linear CEO

**Karri Saarinen**tells Dan how his company reinvented itself for the agent era without abandoning its mission of helping teams build great software. Also, read Every creative lead

**’s thoughts on why tools like Google Stitch can make any app look polished, but you still need a human designer to make something**

__Lucas Crespo__*memorable*. 🎧 🖥 Listen on

__Spotify__or

__Apple Podcasts__, or watch on

__X__or

__YouTube__.

__“How to Design for Human-agent Interaction”__*by Karri Saarinen/Thesis*: When your agent sends out an email before you’ve had the chance to review it, the model did its job—it’s the interface that failed. Karri** **argues that AI’s unreliability is a design problem, not a model problem, and shares the six principles Linear developed so that agent actions are as legible and controllable as human ones. Read this to understand why the answer isn’t approving every agent action—it’s designing the system so the agent already has the constraints it needs before it starts.

## Thesis extra: Designing toward the immeasurable

From Saarinen’s home office in San Francisco, he spoke to us about the design goal he cares about most—which also happens to be one he can’t measure: quality.

Saarinen describes quality as a near-sensory reflex. If he touches—or even looks at—something that doesn’t “feel” thoughtfully crafted, it sets off a niggling itch in the back of his mind. “It’s a belief,” he says, “or I could say, it’s like a faith.”

It’s an unusual stance for a tech founder—given the industry’s penchant to quantify all it possibly can—but Saarinen has made the pursuit of quality central to how the company operates. He sees it as inseparable from Linear’s ambition to be the best in its space.

### Create conditions that make quality inevitable

If quality has to be felt to be understood, scaling it across a growing company isn’t straightforward. Saarinen’s approach mirrors an activity he does far, far away from his laptop screen: growing potatoes every summer at his home in Finland. “You didn’t directly make those plants grow,” he says, “but they grew because you created the conditions for them to grow.” When something goes wrong—say, strange spots appearing on the vegetable’s skin—you have to evaluate the conditions you created. Were the soil conditions right? Perhaps it was too acidic? You adjust, and you learn.

Similarly, a leader can define a standard of quality, but they can’t manufacture it themselves. Their role is to create an environment where quality is likely to take root. At Linear, that means hiring people who genuinely care about their craft, telling them openly—and often—that quality is valued, and building rituals that reinforce it. One of those rituals is __“Quality Wednesday,”__ where the engineering team works on fixing small issues that degrade a user’s experience. The ritual trains the team to notice things that most people would scroll past, and carry that instinct into everything they ship.

### What shapes a seasoned eye

When Saarinen talks about his influences, he’s drawn mostly in the direction of hardware. Saarinen points to Opal—the webcam he used during this interview—or the distinctive aesthetic of Swedish electronics company Teenage Engineering. In particular, he likes the latter’s audio mixers, where tactile grids of knobs and keys—and the small icons etched into their surfaces—attempt to give sound a visual form.

At the same time, Saarinen has never been a fan of skeuomorphism—which styles digital interfaces to mimic physical textures. “If you’re designing a new house and you like Roman columns, so you put columns like that in the house,” he says, “well, it’s still not a Roman house.” Those columns came to exist in Rome from constraints and traditions that were specific to a certain time and place—and grafting them onto a modern house is borrowing from that aesthetic, even though the context that produced it has little to do with what you’re building.

Software, he argues, should be approached the same way. It’s a new medium, and it deserves a native design language instead of hand-me-down forms from the physical world. (And now that apps are becoming __agent-native__, these interactions call for their own __design patterns__.)

### Felt, not measured

Beyond design, Saarinen’s taste gravitates toward science fiction and fantasy—*Dune*, the *Alien* franchise, Stephen King’s *Dark Tower* saga—drawn to the new ideas, the unfamiliar worlds, the visual imagination these stories demand. There are even small nods to these influences hidden in Linear, a detail tucked into a homepage here, a reference in a feature launch video there.

Across all of it, the through line is the same: work that exudes intention and care. The kind of quality you can’t measure, only feel.—__Rhea Purohit__

## Log on

We host __camps and workshops__ on topics like __compound engineering__ and __writing with AI__ to share the knowledge we’ve acquired from training teams at companies like the __New York Times____ and leading hedge funds__, and by learning and playing with AI every day ourselves.

**Upcoming camps**

-
__Claude Code for Absolute Beginners__(April 14): This beginner-friendly, live workshop led by(head of tech consulting at Every) is designed to get you from zero to a working project with Claude Code.__Mike Taylor__

## Alignment

**Dropshipping GLP-1s. **The *New York Times* published __a story__ this week about what might be the first $1 billion one-person company. It’s a GLP-1 telehealth startup called Medvi, built by **Matthew Gallagher** in two months with $20,000 and a suite of AI tools. In its first full year it did $401 million in revenue and is on course for $1.8 billion this year. He has one employee, his brother.

A lot of people are calling the numbers fake, but having spent two and a half years working inside this industry, I don’t think they are. The demand for these medications has been the most ferocious thing I have witnessed in my working life, and the hardest parts of running a telehealth company, like finding doctors and fulfilling prescriptions, can be entirely outsourced to platforms like CareValidate and OpenLoop. All you need is the audacity to do blitz marketing like you’re holding an AK-47 with unlimited bullets, and that’s exactly what Gallagher did.

His affiliates, armed with AI, built fake doctor profiles in Meta ads and made unscrupulous claims about weight loss using fake testimonials. The liability sits with both the affiliates and the company for these types of advertisements, but enforcement has been so slow that it hasn’t mattered.

Of course these black hat marketing tactics worked because regulators are slow and enforcement has been lax. But with acquisition costs rising and retention becoming harder as consumers chase the cheapest option, the unit economics of this model will become increasingly unattractive. These types of businesses exist for a moment until they capitulate because it no longer becomes economically viable.

Gallagher will come away from it a much richer man, so maybe that validates the business model. There’s also a discussion about whether it’s truly a one-man, billion-dollar business: Dan** **__rightly points out__ that Gallagher is outsourcing a large amount of human labor. The part I’m concerned about is that it’s being celebrated as a milestone in AI use when it’s really a better example of someone exploiting an unregulated space.

Some untold number of unknowing people clicked on a fake doctor’s profile, filled out a one-minute consultation, and got a GLP-1 shipped to their door. This is exploitation on an enormous scale! It works for GLP-1s because the demand is extraordinary and the side effect profile is manageable for most people, but the same funnel could be pointed at antidepressants, or hormone therapy, or opioids. This type of business is now being copied because of the publicity this story has received, and that should scare us.

**Evan Armstrong** __predicted__ the one-person billion-dollar company would arrive because AI would compress human intelligence. This feels like something different.—__Ashwin Sharma__

*That’s all for this week! Be sure to follow Every on X at @every and on LinkedIn.*

*We build AI tools for readers like you. Write brilliantly with *


__Spiral__*. Organize files automatically with*


__Sparkle__*. Deliver yourself from email with*

__Cora__. Dictate effortlessly with

__Monologue__*. Work on documents with AI agents using*


__Proof__*.*

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
