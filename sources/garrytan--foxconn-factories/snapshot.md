<!--
VERBATIM SNAPSHOT — immutable evidence. Do not edit.
Source: Garry Tan (@garrytan), essay "Stop building Foxconn factories for your agents"
Captured: 2026-06-01 (pasted by Sidney Swift; canonical URL + publication date not yet confirmed — TODO)
Citation page: sources/garrytan--foxconn-factories.md
Text reproduced as provided, including the author's original typos (it is evidence, not a clean copy).
-->

# Stop building Foxconn factories for your agents

**Garry Tan** · @garrytan

In January I got back into coding and I built Garry's List. Over five hundred thousand lines of Rails and the tests to police it.

I was proud of it. I shouldn't have been. The thing worth being proud of wasn't the app. It was the setup that came out of building it. GStack, the way I code with agents, grew out of the work of building Garry's List, and I gave it away. It's one of the hundred most-starred open source projects in GitHub history, about 105,000 stars in under three months. The half-million lines were the product. The setup was the byproduct. The byproduct is the part that mattered.

Here is what 540,000 lines of code wrapped around an LLM actually is.

It is a Foxconn factory. Built for an hyper-intelligent AI worker who doesn't need hyper-vigilance. We built it anyway.

Little booties at the door. Up at 6am. Calisthenics. A life so hard you have to erect netting around high floors of every building, because... well, it's not a life you want to live. The same line of the assembly belt forever. Every test, every guardrail, every retry loop, an inch of cage bolted onto a worker who can already do the job and a thousand things you didn't ask for.

Humans and agents both contain multitudes but Foxconn factories are built to squeeze intelligence and work out of beautiful beings that could do all that work and 1000x more if we let them.

I built the factory. Everyone builds these today. I'm telling you not to.

## The time traveler

What I actually did with my 539k LOC written was prove I could perfectly impersonate a time traveler. A 2013 Web 2.0 engineer (me, the last time I was a true software engineer) dropped into 2026 with modern tools, building the only way he knew how. More code. Always more code. The tools had changed. My instincts hadn't.

The 2013 engineer believes one thing in his bones: capability equals lines of code. That belief was correct for decades, until now. Hand me Codex or Claude Code and I'll do the work of 100 to 1000 engineers. Same map, faster engine, fastest possible route to the what is now the wrong place.

This is where almost everyone building with AI is right now. They upgraded the tool and kept the 2013 mental model. The trap doesn't feel like a trap, because the code works. Garry's List shipped. It felt like the most productive month of my life.

It was productivity in the service of an obsolete idea.

## LLMs were expensive so we had to harness them

The old economics for many years through 2025: LLM calls were expensive and code was cheap. So you wrote code to ration the model, to harness it, to call it carefully and sparingly. The architecture was lots of software wrapped protectively around a few precious model calls.

Both halves of that equation have flipped.

The model is now becoming cheap and getting cheaper every quarter, and it's so smart that the value-cost ratio flipped. And the model can write usable code. So you stop writing code to babysit the model. You can now instruct the model in plain language, and you let it write the minimal code actually needed.

This is just-in-time-software, and we're entering the golden age of it.

The artifact changes shape entirely. The Rails app was 540,000 lines I wrote and own, code plus the tests built to police it. The replacement is an agent built on markdown and code, a fraction of that. Same capability. Easier to read. Easier to maintain. Far more flexible, because the behavior lives in instructions you can edit in plain language instead of logic frozen in code the day you wrote it.

We were writing code to babysit a thing that is now smarter than the code.

## Inside the Foxconn factory, netting and all

If you've been coding lately, you probably are building this kind of factory without knowing it. Walk your own codebase and count the lines that exist only because you didn't trust the model to do its job.

Mine: about 262,000 lines of application code, and about 276,000 lines of tests bolted on to police it. The audit committee was bigger than the company. Sanitizers checking inputs the model would have handled. Validators checking outputs the model would have caught. Retry loops wrapping calls the model recovers from on its own. Every one of those lines is a bet that the worker will fail. You wrote the same bets. We all did.

127 background jobs, 33 of them on cron. That is not capability. That is 33 alarms set for an LLM worker who usually these days shows up on time.

In my Foxconn factory building days, Claude and I wrote a 1,778-line file whose only job is to second-guess the model's facts. It takes every claim the model makes, fans each one out to five separate sources in parallel, and grades them. A triage gate so the easy claims skip the full blast. A retry if the first pass comes back empty. Fallbacks for the fallbacks.

There's an episode of Rick and Morty where Rick builds a little robot at the breakfast table. It powers on, looks up, and asks what its purpose is. Rick says, "You pass butter." The robot slides the butter dish across the table, looks down at its own hands, and says, "Oh my god." Then it just sits there. That robot contains multitudes. It was built to pass butter. My 276,000 lines of tests were the butter dish.

When you build this kind of software, in the 2023 Foxconn factory way, you built a cage, and if you're not careful, you'll be the jailer maintaining the prison for your AI agents.

## Markdown is the program now

When I say markdown, I do not mean prompting. Prompting is ephemeral. You type something, you get something, it evaporates.

This is building. Versioned, tested, reusable.

The markdown is the instruction layer: the intent, the skill, the judgment about how the work should be done. The TypeScript is the thin deterministic layer. The few things that genuinely have to be code, the I/O, the parts that must never hallucinate.

And critically, you test the markdown the way you'd test code. In my setup the loop is one word. I build something with the agent until it works, then I say "skillify it." The agent then writes:

the markdown skill
the minimal code it needs
a unit test for the code
an LLM eval for the skill
an integration test across both
a resolver so the agent invokes the skill automatically when it's relevant
and an eval for the resolver

That bundle is a skill pack. A unit of reusable capability that compounds. The tests are the magic: coverage on the skill is what lets it change without breaking. This is what separates it from vibe coding. Vibe coding is a vibe. A skill pack has tests.

We are only now figuring out the systems primitives for agentic engineering in real time, the way the early CPU era invented the stack, the heap, the registers, the von Neumann machine. I think a skill pack is one of those primitives. A harness is another. Most people haven't noticed, because they're still measuring software in lines.

## The crazy shit you can actually build

This is not a toy argument. The agent does more than the five-hundred-thousand-line Rails app did, with a fraction of the new code. Concretely:

The hackathon judge. Two Saturdays ago we ran a GStack/GBrain hackathon. 85 submissions. I uploaded the Google Drive of submissions and said go. The agent analyzed every repo's code quality, did deep research on every single person who attended, watched and screenshotted each demo video, rated the screens, and rank-ordered all 85 teams. Then it told me the five apps from the batch worth paying attention to. Judging a hackathon went from a multi-day slog to about thirty minutes.

I didn't write the code. I had OpenClaw do the task, and I guided it. Then once it was done, I said skillify it, and now it's a tarball anyone can run against any hackathon spreadsheet, forever. I say "skillify" all the time now and I have more than 350 skillpacks. Almost every kind of personal and work task I need to do, now my agent can do.

That is the inversion in one example. A capability that would have been a real software project, with scrapers, a scoring pipeline, video processing, a research module, a ranking system, instead became markdown plus a little code, built by the agent, in an afternoon, reusable by everyone.

As an aside: The winner of the hackathon actually built code I ended up polishing up and landing on main! GStack can now test iOS apps both in simulator and on real devices, and that complete feature was made in less than 8 hours at a hackathon by a single person!

## Tokenmaxxing

There's a price of admission, and almost nobody is paying it: you have to be willing to spend on tokens.

Peter Steinberger built OpenClaw, my favorite harness. He has said he's willing to spend on the order of a million dollars a year in tokens to do it. Most people hear that and flinch, but they shouldn't because that's the gold: you can live in 2028 if you can this, and it will be years before people catch up.

This is why OpenAI decided to offer $2M to every YC company as an uncapped SAFE in the form of token credits. There's something magical that happens when you can turn raw intelligence into tokens and then output that is actually usable by users and solves real needs for users that they'll pay for. If you're a founder you need to be maxxing out this capability. (This is why I keep harping on skillify because it's a real way to achieve these good outcomes.)

We spent the last era treating LLM calls like they were too expensive to make. We rationed them. That instinct is now the thing holding people back. If you are willing to tokenmax, to let the agent burn tokens freely and run constantly, you get a 1994 head start on the internet, paid for in tokens. It prices out the >99.99% of organizations still counting pennies on a resource that is collapsing in price, and hands the head start to the few who get it.

For a few hundred thousand dollars a year, for some far less, you can run today the way the rest of the world will be forced to run in a few years.

You can live in 2028 but in 2026, and that is worth the trade in paying more now since, those same tokes that cost $100K today will be $10K next year and $1K the year after that, and maybe $100 by end of 2028. If you could tell any founder in the history of the world that you could invest 6 figures in capital into living 2 to 3 years in the future and hold that advantage for years, 100 out of 100 founders worth their salt would take that deal.

The only thing in the way is the 2013 instinct that says the model calls are too expensive to make freely. They aren't. That was the old economics. The inversion already happened.

## Esalen, not Foxconn

If 540,000 lines of control code builds a Foxconn factory for the worker, the cure is to build the opposite.

There is a place on the cliffs at Big Sur called Esalen. People go there to be unmade and rebuilt, to drop the armor and come back more themselves. No assembly line, no foreman, no 6am whistle. Freedom, not control. Build that. Build a YC, where we try to help you build companies that solve real problems and reach product market fit.

Build places where the workers, both human and AI, are free and not enslaved.

That is the whole ethos. Make things where agents can be free. Make companies where humans can bounce their ball. In knowledge work, the factory is the failure mode. The institution that frees people is the goal, just now pointed at agents too.

OpenClaw is a Ferrari you have to bring a wrench for. The model is the engine, not the car. We're at the Apple I moment still, soldering breadboards. It ships rough. You have to finish it yourself still. GBrain, the retrieval engine and skillpacks I give away open source are not yet batteries included.

They say OpenClaw is unsafe. They don't understand the freedom is also how it is so powerful. You don't bolt safety rails onto a thing you trust before you know you hit the problem. The wrench in your hand is the sign nobody caged it.

A control system is polished because control needs total control, a Foxconn factory. A free system is rough because it trusts you to finish it. Pick which one you're building. Then look at how much code you wrote.

## What it actually means

540,000 lines of Rails was me proving I could still play the old game at the highest level, but that level was from Web 2.0, a decade ago.

I could play as well as I ever could, 1000x engineer in building Foxconn factories. Old code.

But the new game isn't played in lines of code at all. My haters, it turned out, were right. I tip my hat to you if you're reading, anons.

When you can turn intent directly into working, tested, reusable systems, the bottleneck stops being how much you can build and starts being what you actually want and whether it's worth building. The scarce resource becomes clarity, taste, and judgment. The engineer who writes the least code is often the one building the most.

I wrote 540,000 lines to learn that. You don't have to.
