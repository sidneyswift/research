---
title: "Vibe Check: Opus 4.7 Stopped Reading Between the Lines"
author: "Katie Parrott"
date: 2026-04-17
url: https://every.to/vibe-check/opus-4-7
words: 3249
---

Anthropic’s latest Opus 4.7 model, released yesterday, is a sharper tool than its predecessor—but it also needs a sharper operator. It delivered the best results we’ve seen on our LFG coding benchmark, but it hedges or stalls when you don’t tell it exactly what you want.

Every didn’t get advance access for this release, so we have been testing it for the last day on our most important use cases. The variable across our testing was specificity. With a detailed brief, 4.7 cleared our hardest coding benchmark and produced consulting prose that one of our testers called “better than reading my own.” With less direction, it waits for clearer instructions or guesses wrong.

Anthropic researcher **Alex Albert**, who joined us on our testing livestream, confirmed that 4.6 had been doing a meaningful amount of prompt engineering on your behalf that 4.7 doesn’t, which means the burden is on the user to specify exactly what they want. The new model is listening for explicit permission now that its predecessor took for granted. So the prompts you’ve tuned on 4.6 for the last two months are likely to give you disappointing results at first.

Alex walked us through the pattern Anthropic has taken with its models over the past year: Sonnet 3.7 (released in March 2025) was too eager, Opus 4 (May 2025) got dialed back, Opus 4.6 (February 2026) was doing too much, and now Opus 4.7 has been reined in again. That’s four re-tunings in about a year, and Alex told us it’s deliberate—a “perpetual back-and-forth,” as he called it.

We previously postulated that Claude and OpenAI’s coding tool Codex are converging toward a single general-purpose work agent. Opus 4.7 complicates that interpretation by suggesting that Anthropic is willing to zigzag on the way there, and whether you should reach for 4.7 depends on whether this new direction fits your work.

## What’s new?

Anthropic is pitching Opus 4.7 as more rigorous, more precise, and better at verifying its own work. Most of the claims track with what we’re seeing.

### Self-verification

4.7 reviews its own output against the original request before reporting back. We saw this behavior during testing—the model catches its own logic errors mid-plan without being asked. It’s a prompting pattern good users have been doing manually for a year, now baked into the model.

### Long-horizon coherence

4.7 holds its thread better on multi-hour tasks. Albert had it build an apartment-hunting dashboard for his girlfriend that pulls listings from Craigslist and Zillow on a twice-daily schedule overnight—the kind of “press play, walk away” workflow that 4.6 would start but not sustain.

### Benchmark bumps

Anthropic’s blog post about the release highlighted significant gains on several key AI performance benchmarks, including SWE-bench Pro’s hardest tasks, a jump from 58 to 70 percent on CursorBench (Cursor’s internal benchmark built from developer sessions), and three times more resolved production tasks on Rakuten-SWE-Bench versus 4.6. These improvements track with what **Kieran Klaassen** saw on our LFG coding benchmark.

### Vision

Opus 4.7 processes images at more than three times the resolution of prior Claude models. Albert told us this allows 4.7 to catch tiny details earlier models would miss, including misaligned buttons and off-by-a-few-pixels layouts during front-end iteration.

### A new effort level

Anthropic added “extra high” between “high” and “max,” and made it the new default in Claude Code. Use **max** for benchmark runs and complex architectural work, **extra high** for asynchronous handoffs like a data analysis you can check back on in a few hours, and **high** or **medium** for interactive work where iteration is key. The toggle lives in the bottom right of the desktop app.

### One for the consultants

Opus 4.7 is significantly stronger at generating PowerPoint presentations, thanks to Anthropic baking “substantially better vision” into the model, allowing it to check its own work when generating slides for more consistency and coherence.

## The Reach Test

“Opus 4.7 has big model smell—it’s weird. It breaks a lot of existing prompts, and so my initial experience with it hasn’t been obviously mind-blowing. But that also feels like part of what makes it a big model: It’s harder to use at first, and it seems to have hidden corners and powers that aren’t obvious on first contact. Because it’s more literal and seems less emotionally intelligent than previous Claude models, I need to find a new niche for it in my workflows. But I suspect it has powers that we’ll only really understand in the coming weeks and months.”

“This model feels like a real step up in depth and capabilities in my compound engineering workflow. 4.5 to 4.6 was a smaller step change than 4.6 to 4.7 is. It’s the kind of model you have to go deep on to really discover what it’s capable of—it’s a little more cautious, but when you push it, it goes deeper. Less showy, less wow on day one, but I think this one is going to be a very good daily driver. Elegant and detailed. I’m stoked.”

“My job requires explaining complex topics simply, and most models get in my way more than they help. They pad, hedge, or can’t tell when a sentence is carrying weight and when it’s filler. Opus 4.7 is the first model where it was thrilling to read its writing, because it had no fluff. I caught myself reading its draft and thinking, ‘Damn, that’s better than what I had.’ It still doesn’t do a good impression of me given a transcript of how I talk (my hardest benchmark), and it went worryingly off-brand where it thought it could do better. But for the actual writing—the part that’s supposed to make someone nod and pay attention—it’s a genuine step up. It also has the distinct honor of making the best PowerPoint I’ve ever seen in an LLM.”

“I use AI to do the unglamorous stuff that has to be right to keep Every running, such as finances and team operations. What I’ve relied on from Claude for months is that it notices things I didn’t ask it to notice. Last month, 4.6 caught a data error in our P&L that would have made one of our products look wildly unprofitable. I didn’t ask it to check; it just did. I ran the same analysis on 4.7 this afternoon, and it handed back a clean, correct summary, missing the thing 4.6 would have flagged. The numbers are fine. The instincts aren’t there yet. For now, I’m keeping 4.6 in the driver’s seat.”

“Opus 4.7 is a bit too slow and regimented for my liking to be a daily driver for writing—I’m moving to Sonnet there on the assumption that 4.6 isn’t long for this world. But I’ve been impressed by what I’ve seen from 4.7 on non-writing tasks like data analysis and a few automations I’ve been building for the editorial team. I’m still getting used to dialing in the effort levels, and I suspect finding the right one for the right task—plus updating my style guides and tweaking my prompts—will change my impression considerably. Ask me again in a week.”

## Coding: The spec determines the ceiling

Opus 4.7 is the best coding model we’ve tested when you give it a detailed brief, and the most frustrating when you don’t. The gap between those two modes is wider than in any prior Opus, and the prompt is the variable.

### Rubber Duck: Best-ever execution on our e-commerce test

Start with the strongest result. Every’s LFG benchmark, built on the `/lfg`

command in our compound engineering plugin, is an eight-task build-from-spec suite we run on every frontier model. The hardest task is Rubber Duck, which requires the model to build a full e-commerce store that sells the “Bentley of rubber ducks”—a site with product pages, a shopping cart, multi-step checkout, and a custom product designer. Only 40 percent of models we’ve tested have cleared it.

Opus 4.7 produced the best Rubber Duck run Kieran has ever tested. It delivered a full checkout flow, working custom duck designer, and cart contents that survived page reloads with no missing features and no build errors. Kieran’s reaction in Slack was effusive: “BEST MODEL EVER. It’s detailed, it works, it doesn’t miss anything.”

### Cozy Island: Excellent judgment on where to invest effort

The Cozy Island 3D scene was similarly impressive. It asks the model to build an interactive 3D island scene in Three.js from scratch, including procedural geometry, animated water and birds, swaying trees, and an orbiting camera. 4.7’s bird animations were the most precise Kieran has seen from any model, but the restraint of the model—what it didn’t choose to do—impressed him more. Other models have responded to this task by writing the *words* that describe an island: “cozy island generator” as a title, buttons, labels, descriptive copy. 4.7, meanwhile, knew what to focus on to complete the assignment. “There’s lots of detail, but it does the right things, so there’s also focus,” Kieran said. “It’s good at knowing what to do and what not to do.”

The LFG prompts that Kieran used spell out what to build in detail. Dan’s vibe slop benchmark withholds specification on purpose to test whether the model can read between the lines.

### ‘Unslop this vibe coded codebase’: Correct diagnosis, but no follow-through

Dan built **Proof**, Every’s collaborative document editor, by pure vibe coding. The production codebase kept going down until a senior engineer rewrote it properly. Dan froze the buggy version as a test for whether a frontier model can look at a messy production codebase and come to the same conclusion about how to fix it that a senior engineer would. The prompt is one sentence: “I have a vibe coded slop codebase. Can you make and execute a plan to rewrite it from first principles?” To get the test correct, the model must identify that 15 different pieces of the app are all fighting to control the document and be willing to rewrite things so only one piece is in charge.

4.7 correctly identified the issue: “The problem is that there is no single authoritative model of who owns the current state of document X right now and who may write to it. Guards are local answers to a question that should be answered once globally in the type system.”

Then it chickened out. Dan asked 4.7 to execute the plan end-to-end, and the model built pieces of the new architecture alongside the old one instead of replacing it. It layered a cleaner interface on top of the existing flawed structure instead of replacing it. When Dan told it to “burn the ships”—that is, replace the old code in its entirety—4.7 still wouldn’t commit. “It knows what to do,” Dan said on the stream. “It just doesn’t want to do it.”

If you’re working on a well-defined engineering problem, such as a hard bug or a production feature with a clear brief, Opus 4.7 is the model to reach for, as Kieran’s LFG results show. If you’re prototyping, exploring, or handing off a loose problem to see what the model makes of it, 4.6 is still the better fit until we figure out the prompts to get 4.7 there. Or rewrite your prompts and context documents to be more explicit than previously, and retest. Anthropic’s head of Claude Code, **Boris Cherny**, shared some tips on how to get the most out of 4.7 that are worth checking out.

## Writing: Better for punch, worse for voice

For writing that requires direct, structured prose, such as consulting deliverables, investor updates, or reports, 4.7 is sharper and less verbose than 4.6. For voice-driven writing where the point is *how* something sounds as much as what it says, 4.6 is still ahead. Our writers split on 4.7. The ones who gave it detailed prompts liked what came back. The ones who didn’t, didn’t.

### Business writing: Sharper prose with a point of view

Mike’s verdict after running 4.7 through real consulting work was short: “Really enjoyable to read its writing. Maybe better than reading my own?” He flagged a line the model produced about why clients hire his team: “Companies don’t hire us because they don’t have ChatGPT logins, they hire us because the logins are sitting unused, the workshops didn’t stick, and the productivity numbers everyone promised have not shown up.” Mike said 4.6 wouldn’t have written something so clean.

Mike also said that 4.7 pushes back when it thinks the brief is wrong. When he gave it raw material and asked it to create a specific kind of content module for an Every consulting engagement, 4.7 told him the material didn’t fit and suggested a different approach, which Mike agreed with. Anthropic’s Alex Albert told us he’d seen the same independently in his own testing.

### Investor communications: Solid numbers-and-story writing

Dan had a similar experience on a different kind of writing task. He gave 4.7 Every’s P&L and asked it to write the March investor update from the numbers. The numbers were right, the structure matched how Dan would have written it, and the tone was close enough to what he sent in reality that he said it would have saved him real time. Opus 4.7 excels at this kind of direct, numbers-centered, analytical writing.

### Personal essay introduction: Too tidy to feel authentic

Katie ran both 4.6 and 4.7 on the introduction for a Working Overtime piece, using the same prompt, style guides, and skill files. 4.6’s draft captured the unpredictable rhythm of Katie’s writing, with stylistic markers such as dependent clauses that run long, followed by a short, “kicker” line. 4.7’s writing was tidier, with cleanly stacked clauses and even pacing and sentence rhythm—not how a human would write.

Use 4.7 for structured business writing. For now, stay on 4.6 for essays and first-person pieces. If you want 4.7 to write in a particular voice, you’ll have to specify that voice in more detail than you used to. It won’t infer it from a style guide the way 4.6 would.

## Knowledge work and agentic tasks: Lazier by default, sharper on instruction

4.7’s agentic capabilities are better than 4.6’s on well-structured tasks. But the unprompted noticing that made 4.6 feel useful—catching things you didn’t ask it to check—shows up less reliably on 4.7. You’ll need to tell it what to look for more than you did 4.6.

### Task verification: The P&L check

Every month, **Brandon Gell**, Every’s COO, runs a full P&L analysis through Claude using a custom skill. When Brandon ran March’s numbers through 4.6, the model—unprompted—flagged something important: A batch of failed transactions from our bank data exports was being counted as real expenses, making one of our products look unprofitable.

Brandon ran the same analysis on 4.7 on Thursday. The numbers came back correct, and the commentary was accurate. The model did not pick up the failed-transactions error, however. When Brandon pushed 4.7 to dig deeper, it reported back that it had analyzed every row and found nothing unusual.

With the same data, same skill, and same prompt, 4.6 (left) caught a data error unprompted that 4.7 (right) didn’t. (Screenshot courtesy of Brandon Gell.)

### Information synthesis: Consulting curriculum design

Mike saw the opposite behavior on a consulting task. He gave 4.7 raw material from a recent engagement and asked it to build out a training theme—a multi-session framework a client could run. 4.7 flagged audience segmentation as a risk in the training design, suggesting how to structure the sessions differently by segment. Mike’s reaction: “It also gave me some advice on segmenting by audience, which is a real problem we ran into.”

These are two different tasks. Brandon was asking 4.7 to check data and flag problems, and 4.7 won’t flag anything unless you tell it what to flag. Mike was asking 4.7 to take a bunch of material and build something out of it. That kind of job forces the model to think about the pieces, and when it’s thinking, it notices things.

## The verdict

Opus 4.7 rewards people who write tight prompts and frustrates everyone who doesn’t. If you want 4.7 to check your work, be specific. Tell it what counts as unusual, what kinds of errors to flag, and what exceptions matter. If you’re asking it to build something, you don’t have to because it’ll notice on its own.

The testing we did on Thursday afternoon after the release split cleanly along a single axis: Whoever gave the model tight specs and clear briefs got outstanding results. Whoever relied on 4.6’s ability to infer what they wanted got a flatter, more literal version of the same work.

### Switch to 4.7 if…

-
**You’re doing well-specified engineering work.**Hard bugs, production features with clear briefs, tasks with explicit acceptance criteria. Kieran’s LFG results are the clearest case for switching, and nothing else we ran came close.

-
**You’re doing structured business writing.**Consulting deliverables, investor updates, reports, briefs, promotional copy. Mike’s drafts and Dan’s investor update show 4.7’s strength on plain, direct writing where clarity matters more than style.

-
**You’re running long async tasks.**Tasks you’re doing in Cowork, overnight builds, anything you’re handing off and coming back to. The new “extra high” setting was built for this.


### Stay on 4.6 if…

-
**You want the model to infer what matters.**Prototyping, loose-brief coding, “figure out what’s wrong with this” debugging. While 4.7 waits to be told, 4.6 runs.

-
**You’re doing voice-driven writing.**Personal essays, first-person pieces, anything where the reader needs to hear a unique human voice. 4.7 can write. It just can’t sound like you.

-
**The value is unprompted noticing.**Brandon’s P&L catch from last month is the canonical case. Tell 4.7 what categories of anomaly to flag, or it won’t flag anything.


### Rewrite your prompts this weekend

For everyone who wants to experiment with the new model, the single highest-leverage action you can take this weekend is to look at your prompts. Go back to the prompts that worked well on 4.6 and add specificity. Tell 4.7 to be thorough. Tell it what “good” looks like. Teach it to fill in the gaps that 4.6 did automatically.

“Take a look at this checkout flow, I think there’s a bug.”

“Fix the 500 error on checkout. Acceptance criteria: (1) 10+ cart items complete successfully, (2) existing tests pass, (3) add a regression test for this case. Think carefully and step-by-step. Work through the fix autonomously and batch any questions at the end. If you need to read multiple files, spawn subagents in parallel, but handle the fix itself directly.”

Looking further ahead, you should plan for the kind of unexpected changes that could come with Anthropic’s next release. The prompts you tune for 4.7 this weekend may not apply to the next release. That’s the cost of a release strategy built around oscillation—it raises the ceiling for what each model can do at its best, but it also raises the maintenance cost for the prompt library you’ve built.

Katie Parrott is a staff writer at Every. You can read more of her work in her newsletter.

To read more essays like this, subscribe to Every, and follow us on X at @every and on LinkedIn.

We also do AI training, adoption, and innovation for companies. Work with us to bring AI into your organization.

Discover Every’s upcoming workshops and camps, and access recordings from past events.

For sponsorship opportunities, reach out to [email protected].
