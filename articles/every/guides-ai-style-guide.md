---
title: "AI Style Guides: How to Help AI Write Like You"
author: "Katie Parrott; Claude"
date: 2026-03-17
url: https://every.to/guides/ai-style-guide
words: 4093
---

## What an AI style guide is

A traditional style guide helps a group of people write consistently. It tells them what tone to strike, what words to use or avoid, and offers conventions for grammar, usage, mechanics, and other elements of writing style. The problem it solves is inconsistency.

An AI style guide solves the opposite problem. A model is perfectly consistent from the start—that’s why it sounds like nobody. The challenge is to push it toward the idiosyncrasies that make writing belong to a particular person. An AI style guide helps a model replicate a real writer’s judgment.

A useful guide doesn’t stop at vague descriptors like “clear,” “smart,” or “conversational.” It gets concrete. It explains the openings you favor, how your arguments tend to be structured, which sentence patterns you like and don’t like, which metaphors fit your voice, and what linguistic tendencies the model should avoid regardless of its training.

In that sense, an AI style guide is an operating manual. It takes what you know instinctively about your own writing and makes it legible for a machine to use.

A style guide is not a prompt. A prompt tells AI what to do: Draft an essay, revise a paragraph, or tighten an intro. A style guide is the reusable system underneath telling AI how to sound like *you* while doing it.

## What goes in an AI style guide

The most effective AI style guides are concrete and specific. At minimum, a good guide should cover voice, structure, sentence-level preferences, signature moves, anti-patterns, examples, and revision standards.

We’ve built two style guides at Every: one for __Working Overtime__, our column on how technology is changing work, and one for __Source Code__, where we share what we’ve learned about creating software products with AI. We’ll go through each section with examples from both.

### The Only Subscription You Need to Stay at the Edge of AI

Start shipping agent-native products with Every.

### Voice and tone

Start by describing how the writing should feel at its best. You can name qualities like smart, plainspoken, skeptical, warm, dry, lyrical, or reportorial, but this section works best when it goes beyond flattering adjectives. The more useful descriptors answer questions like: How formal is the writing? How much emotional temperature does it have? And what tone feels completely wrong?

**In practice:**

The Working Overtime style guide describes voice with five rules that define the column’s tone:

- Write
**from inside**the transformation, not above it. - Balance:
**participant + observer**,**enthusiast + skeptic**. - Vulnerability is analytical: Use personal stakes to frame insights.
- Tone:
**conversational + rigorous**,**optimistic but not naïve**,**critical but not cynical**. - Use humor sparingly for wry emphasis, not undercutting.

Source Code takes a different approach, defining a *spectrum* of valid voices:

- Technical authority: “I haven’t typed a function in weeks, yet I’m shipping faster than ever.”
- Confessional practitioner: “I fell into the vibe coding trap. Here’s what I learned.”
- Workshop narrator: “When Yash described compound engineering, he reached for a metaphor—a jet ski.”

The Working Overtime approach works for a single-author column with a consistent voice. The Source Code approach works for a multi-author publication where different pieces call for different registers.

### Structure

What often distinguishes a piece of writing is the way its ideas are organized. What makes a strong opening? How quickly does the piece get to its point? Does it move from anecdote to argument, example to concept, tension to explanation? AI infers these structural decisions poorly. So make them explicit.

**In practice:**

Working Overtime defines a core structural arc that every essay follows:

- Open with friction—failure, doubt, surprise, career anxiety. Stakes clear by paragraph one.
- Document experimentation—process, screenshots, missteps. Show the messy middle.
- Surface the pattern—connect to cultural, historical, or philosophical context.
- Deliver a takeaway—framework, prompt, workflow, or reframe readers can use tomorrow.

Source Code provides an arsenal of seven named structural templates: the Discovery Arc, the Technical Deep-Dive, the Workshop Report, the Multi-Case-Study, the Gateway Guide, the Two-Part Series, the Q&A format. Each has a step-by-step progression and a reference example from the published archive. For instance, here’s the Discovery Arc:

#### The Discovery Arc

- Problem/frustration encountered (or bad habit confessed)
- Conventional solution inadequate (or current hype misleading)
- Breakthrough moment
- New practice developed and named
- Results and transformation (with real metrics)
- How readers can adopt it (audience-segmented if applicable)

The Working Overtime approach fits a column with a consistent shape. The Source Code approach fits a publication that needs structural variety. Both are better than “start with a hook and end with a takeaway.”

### Sentence-level preferences

Spell out the line-by-line habits that shape the prose: short versus long sentences, clean declaratives versus winding accumulations, punctuation preferences, rhythm, diction, tolerance for abstraction, and any recurring structural moves to follow or avoid.

**In practice:**

Source Code’s guide instructs the model to use concrete language, and provides it paired examples:

- “Claude spun up five PRs while I drank coffee”—not “optimized workflows.”
- “$400/month replacing $400k/year”—not “cost-effective.”
- “Gmail rate limits blocked 2,000 email operations”—not “ran into scaling issues.”

Working Overtime specifies that at moments of emotional significance, the writing should locate the experience in the body:

Favor: “the relief felt as physical as the dread had been,” “a rush of satisfaction,” “I collapse afterward.”

Avoid: abstract descriptions of feelings that could apply to anyone.

Both give the model a testable target for how sentences should sound. One focuses on concrete nouns and verbs, the other on embodied specificity. Your guide should address whatever dimensions matter most for your writing.

### Signature moves

Name the things this voice does especially well. Maybe it starts concrete and zooms out. Maybe it uses humor to break up abstraction. Maybe it pivots from anecdote into argument or alternates bluntness with reflection.

**In practice:**

Working Overtime names three signature moves, each with a brief description:

**The Friction → Zoom Out → Framework:** Start with a personal moment of friction, zoom out to a broader cultural or historical frame, and land on a usable framework or reframe.

**Adventure Narrative: **A chronological account of trying something new, structured around the escalating discovery and its unexpected consequences.

**The Borrowed Lens:** Pull a concept from an unexpected discipline—dance, textual criticism, advertising, improv—and use it as the interpretive key for the essay.

Source Code names its equivalent moves at the column level—the “One Big Idea” rule (each piece must coin, claim, or crystallize one memorable concept), the “Personal Stakes as Foundation” principle, and the “Explain Like I’m Five” or “ELI5” rule (every technical term must be explained so a smart newcomer could follow). For example, here’s what the Source Code style guide says about the One Big Idea rule:

**The One Big Idea **

Each piece must coin, claim, or crystallize ONE memorable concept:

- A discipline (compound engineering)
- A lesson (“spend more time on your plans than you do on code”)
- A framework (the compound engineering loop: Plan/Work/Review/Compound)
- An architecture (agent-native)
- A practice shift (vibe planning, fidelity levels)

### Anti-patterns

This is often the highest-value section in the whole document. Don’t just tell the model what good writing looks like. Tell it what bad writing looks like, too.

**In practice:**

Working Overtime maintains a “red flag” table with specific patterns and their solutions:

Pattern |
Solution |
|---|---|
| Hedges: “actually,” “maybe,” “just” | Delete |
| Correlative constructions: “not X, but Y” | Rewrite |
| Rhetorical questions as filler | Cut or convert to statement |
| Meandering intro (>3 paragraphs to stakes) | Start with friction |
| Saggy conclusion that recaps | End by extending or reframing |

It also lists performance-killing patterns proven by data:

- Abstract industry analysis without personal stakes → 78% engagement drop
- Process documentation without emotional arc
- Theory before practical application
- Opening with context/history instead of friction

Source Code addresses skeptics directly, naming the readers’ objections and showing how the essay should handle them:

- “AI wrappers are overdone”—The opportunity is just beginning.
- “Agents can’t handle real engineering work”—Here’s a morning in my workflow.
- “I tried vibe coding and it was chaos”—That’s because you skipped the planning.

Both approaches are more useful than “avoid sounding generic.”

### Positive and negative examples

Examples make the guide much stronger. Show a paragraph that gets the tone right. Show a line that sounds AI-ish and explain why it fails. A rule paired with an example is almost always more useful than a rule alone.

**In practice:**

Working Overtime gives examples for openings, endings, and voice:

Good openings:

- “I used to be physically unable to open my email.”
- “One night last month, instead of booting up my Switch for another thrilling session of
*Stardew Valley*, I decided I wanted to play a different kind of game.”

Good endings:

- “And then I choose, one difficulty at a time.”
- “Let’s measure them—and ourselves—by the right standard.”

Avoid:

- “At the end of the day, it’s still just a tool. True clarity comes from doing the hard work yourself.”

Source Code has examples organized by opening pattern (the Bold Claim, the Charged Anecdote, the Confessional, the Scene-Setting, the Manifesto Declaration), each with sample lines from published pieces. It also provides negative examples through its *ELI5* section:

Vague workflow: “We spun up a retrieval pipeline with subagents, chunked the corpus, hydrated the cache, and it just worked.”

Why it doesn’t work: Jargon, no steps, missing clicks/inputs.

### Revision checklist

Include a checklist for evaluating whether a draft is working. What are signs that the prose has become too smooth, too generic, too abstract, or too pleased with itself?

**In practice:**

Working Overtime’s pre-publication checklist tests for the column’s values:

- Stakes clear by paragraph one?
- Lived moment of friction in the opening?
- Screenshots of actual AI interactions?
- All technical terms ELI5’d?
- Clear transformation (before → after)?
- Ending extends the idea (not summarizes)?
- Would someone say “I’m not alone in feeling this”?

Source Code’s 10 principles function as their own sort of revision checklist—commandments that double as editorial standards:

- Show the mess: Include failures, frustrations, false starts, and honest limitations.
- Coin deliberately: If you name it, define it clearly and develop it across pieces.
- Prove with examples: Show actual workflows, real metrics, named practitioners and tools.

The best checklist is one built from the specific ways your model-generated writing goes wrong. If your AI drafts always produce tidy summary endings, “Does the ending preserve energy?” belongs on the checklist. If they tend to bury the lede, add “Are stakes clear by paragraph one?” to the list.

## Where to start: three levels of style guide

The right approach depends on where you are with AI writing. Trying to build a comprehensive system in one sitting will burn you out. Starting with a vague voice description when you’re already drafting daily will leave you no better off.

### Level 1: The starter guide

**You’re just beginning to use AI for writing, or you don’t have many samples of your own work yet.**

At this stage, you just need to provide enough guidance to get the model out of its default voice. A starter guide has:

- Three to five bullets describing how the writing should feel (get concrete—go beyond “smart and conversational”)
- A short description of your preferred structural shape (how do your pieces open? how quickly do you get to the point?)
- A blacklist of five to 10 patterns you hate in AI-generated prose
- Two or three examples of writing you like, with a sentence or two about what you like about them

You can write this in 20 minutes, and it will meaningfully improve your next AI draft. If you don’t have strong samples of your own work, seed the guide with writing you admire—articles whose tone you want to emulate, openings you wish you had written, writers whose sentence rhythms feel right. Give the model a target, even if you’re still growing into it.

**Where to put it:** Keep it in its own note or document. Paste it into the chat window when you need it. Fine for this stage.

### Level 2: The working guide

**You’re drafting regularly with AI and have a growing body of work.**

At this stage, you’ve noticed the model’s recurring mistakes. You know which corrections you’re making over and over. A working guide adds:

- Sentence-level preferences with positive and negative examples
- Named signature moves (what does your writing do especially well?)
- A revision checklist built from real problems you’ve encountered
- Structural templates for the kinds of writing you do most
- Expanded anti-patterns with before/after examples

Both the Working Overtime and Source Code guides are working guides. Both took months to reach their current form. We used them daily, revised them each time the model made a repeated mistake, and expanded them each time we learned something new about what counts as “good” content for those columns.

**Where to put it:** Store it in a __Claude Project__ or __custom GPT__. The model reads the guide for context at the start of every conversation in that project or GPT, so you don’t have to manually include it.

### Level 3: The compound system

**AI is a core part of your writing workflow, and you want the system to improve with each use.**

At this stage, the style guide becomes one part of a larger infrastructure. You build automated checks that scan drafts for specific patterns. You create workflows that run the guide against every piece before it ships. Each editorial correction feeds back into the guide, so that the same mistake doesn’t happen twice.

You don’t need to start here. Just know that a style guide can grow from a document you paste in a chat window into dynamic guardrails that keep your writing consistent across the full spectrum of the writing process.

**Where to put it:** Build it into a skill, plugin, or agent system. The guide is part of an automated pipeline—checked against every draft, enforced through workflows, and updated by a feedback loop.

## How to build an AI style guide

Don’t sit down and write the entire guide from scratch. Instead, let the AI help build the guide for you. Ask it to interview you.

Many people are better at reacting than self-describing. You may not be able to explain your voice from a blank page, but you can answer questions like: Which of these two openings sounds more like you? What do you hate about this paragraph? Why does this sentence feel too polished? Which published piece feels most representative of your voice?

Here’s how to set up a good interview.

### Step 1: Give the AI examples of your writing (or writing you admire)

Give the model a small set of examples—three to five is a good starting point—that reflect the kind of writing you want. They could be published essays, favorite newsletter posts, successful intros, and strong paragraphs from past drafts—pieces that capture the range of how you write.

If you don’t have many examples of your own yet, seed it with writing you admire. You’re giving the model a target, even if you’re still growing into it yourself.

### Step 2: Ask the AI to interview you

Once the examples are in place, have the AI ask you questions designed to surface your preferences about tone, structure, sentence rhythm, opening strategies, metaphors, recurring habits, things you hate in AI-generated prose, and the differences between what feels generic and what feels like you.

This works much better than simply describing your style. The interview helps you elaborate and get specific.

### Step 3: React to examples, not generalities

The most useful answers come when the conversation is attached to actual text. Ask the AI to show you sample lines, paraphrases, or summaries for you to react to. You get a chance to say things like: “This is too symmetrical,” “This sounds too corporate,” “I would never end a paragraph this neatly,” or “This phrase is too pleased with itself.”

### Step 4: Turn the interview into a draft guide

Once the AI has enough material, ask it to synthesize the conversation into a draft guide covering voice and tone, structure, sentence-level preferences, signature moves, anti-patterns, and examples, along with a revision checklist that reminds the AI about the characteristics it should protect and avoid.

### Step 5: Test and revise

Use the guide for a week. Draft with it, revise with it, notice where you keep making the same corrections. Find out which parts are working and which are still too vague. At the end of that week, update the guide with what you’ve learned. If the model keeps making the same mistakes, sharpen the instructions. If a section noticeably improves the output, keep it.

## What makes a style guide work (and what doesn’t)

**Be more specific than feels natural**

Most people’s first instinct is to describe their style in broad, flattering terms: clear, thoughtful, sharp, conversational, and smart. Those descriptions aren’t wrong, but they also aren’t specific enough to change the model’s behavior. Instead, describe actual choices: how the writing tends to open, what kinds of transitions feel dead, how much abstraction it can tolerate, what sentence moves keep showing up, and what should get cut on sight.

**Name what the model should stop doing**

Many people describe a lot of what they like and little of what they hate. In practice, the blacklist is one of the most useful sections in the whole guide. The Working Overtime blacklist started with three items. It now has dozens, organized by severity, each one added as a result of a specific mistake on a draft.

**Use examples whenever possible**

A paragraph that nails the tone, a sentence that captures the right rhythm, or an opening that demonstrates the ideal movement will teach the model more than a paragraph of abstract explanation. Negative examples matter too: Showing what misses the mark—and why—can clarify as much as showing what succeeds.

**Optimize for the writing you do**

It’s tempting to make the guide broad enough to cover every possible kind of writing. Usually that makes it weaker. Source Code maintains separate style guidance for engineering-heavy, practice-focused, and philosophy-driven pieces because each calls for different structural and tonal choices. A guide grounded in real tasks produces better results than one designed to cover everything.

**Don’t make it too rigid**

Treat the style guide like a rulebook the model must follow mechanically, and you flatten the writing in a different way. The goal is to preserve what matters while leaving room for variation and surprise. Source Code’s guide makes this explicit: “Choose the approach that serves the story.”

**Don’t expect it to eliminate judgment**

Even a great style guide does not remove the need for editorial judgment. A guide can improve drafts and reduce repeated correction. It cannot replace taste. The goal is to make the collaboration more fruitful—not to automate writing so thoroughly that no one has to think.

## A simple AI style guide template

If you want to create a guide quickly, start with this template and fill it in as specifically as you can. You don’t need to get every section perfect on the first pass.

**1. Voice and tone**

**How should this writing feel at its best?**

Write three to five bullets describing the voice—with tensions and boundaries, beyond flattering adjectives.

Examples:

- Plainspoken, but not casual to the point of sloppiness
- Smart, but not academic
- Funny in a dry or understated way
- Willing to be emotionally honest, but not melodramatic
- Specific and grounded rather than vague or inflated

You can also include: level of formality, emotional temperature, whether humor is welcome, whether the voice should feel reportorial, essayistic, intimate, skeptical, lyrical, etc.

**2. Structure**

**How do pieces in this style usually move?**

Examples:

- Open with a concrete detail, scene, or recognizable problem
- Get to the core argument relatively quickly
- Move from example to idea, not the other way around
- Avoid long throat-clearing intros
- End with forward momentum rather than tidy summary

**3. Sentence-level preferences**

**What makes a sentence sound right in this voice?**

Examples:

- Vary sentence length
- Prefer clean, direct sentences over overly symmetrical ones
- Use abstraction sparingly
- Favor concrete nouns and verbs over vague framing language
- Avoid sounding too polished or too pleased with yourself

**4. Signature moves**

**What does this voice do especially well?**

Examples:

- Starts concrete and zooms out
- Uses humor to cut through abstraction
- Pivots from anecdote into argument
- Lets a little friction remain instead of smoothing everything out

**5. Anti-patterns/blacklist**

**What should the model avoid?**

Pattern |
Solution |
|---|---|
| “Not X, but Y” constructions | State Y directly; drop the scaffolding |
| Hedges: “actually,” “maybe,” “just” | Delete unless doing real intellectual work |
| Meandering intro | Start with tension or stakes |
| Summary ending | End by extending or reframing |
| Fake profundity | Cut |
| Generic transitions | Cut or make specific |
| Boilerplate authority (“studies show”) | Name the study or delete |

**6. Positive examples**

**What are examples of this voice working well?**

Include: a paragraph you love, an intro that sounds right, a sentence with the right rhythm. For each, briefly explain why it works.

**7. Negative examples**

**What are examples of this voice failing?**

Include: AI-generated lines that sound too generic, sentences that are too symmetrical or polished, openings that feel dead. For each, explain what feels off.

**8. Revision checklist**

**How should you evaluate whether the draft is working?**

Examples:

- Does this sound like a real person or a polished summary machine?
- Is the writing too smooth?
- Is the language specific enough?
- Are there blacklist patterns still in the draft?
- Does the ending preserve energy, or collapse into summary?
- Is this how I would say this?

## A starter interview prompt

If you want to kickstart the process, you can begin with a prompt like this and adapt it to your needs:

I want you to help me create an AI style guide for my writing.

Your job is to interview me and extract the information you’ll need in order to write a useful style guide—a practical document that will help an AI produce writing that sounds more like me (or like the style I’m aiming for), as opposed to a flattering summary.

Here’s how I want you to approach this:

- Start by asking me for examples of my writing, or examples of writing I admire if I don’t have strong samples of my own yet.
- Ask me one question at a time, not a giant list all at once.
- Focus on specifics: tone, structure, sentence rhythm, openings, metaphors, recurring habits, things I hate in AI-generated prose, and the differences between writing that feels right and writing that feels generic.
- Whenever useful, give me short examples, comparisons, or alternative phrasings and ask me to react to them.
- Help me surface both positive preferences and negative ones. I want to identify what I like, but also what I want to avoid.
- After you’ve gathered enough material, synthesize it into a style guide with sections for:
- voice and tone
- structure
- sentence-level preferences
- signature moves
- anti-patterns / blacklist
- positive examples
- negative examples
- revision checklist

- Keep the guide concrete, specific, and usable. If something is too vague to change how an AI would write, make it sharper.

Do not start by writing the guide immediately. Start by interviewing me.

You can customize this prompt to suit your goals. If you want help with a particular kind of writing—newsletters, essays, product writing, reported pieces—say that up front. If you want the guide to reflect an aspirational voice rather than your current one, say that too.

## The big picture

An AI style guide helps the model write like you. Creating one forces you to get explicit about your own taste—what you love, what you reject, what kinds of choices make the work feel like you. The guide helps the AI produce more usable drafts and better revisions. And it has another, perhaps more important benefit: It helps you better understand your own writing.
