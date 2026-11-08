Jev is a new model built to evaluate questions with predefined possible answers. It returns answers in a few hundred milliseconds, in a structured format, with a probability for each possible answer.

Practically, Jev helps you make a decision. You provide it context, questions, and possible answers, and it answers each question using probabilities, which you can then use to make a decision.

We spent the past two weeks building with Jev’s API. In this post, we’ll show practical examples of what you can build with it.

## [What can you ask Jev?](https://rubriclabs.com/blog/what-can-you-build-with-jev#what-can-you-ask-jev)

You can ask Jev three kinds of questions. Every figure in this post calls the Jev API live, and the time and cost in each corner come from your request.

Choice picks the best option from a list you provide, and returns a probability for every option.

Which emoji best represents “Q4 revenue report”?

Live

Using Choice to find the emoji that best represents the title
Score rates something on a scale you define, like 1 to 5. The score can land between levels, like 4.7.

How well does the “📊” emoji represent the title “Q4 revenue report”?

Live

Using Score to rate how well an emoji represents the title
Bool (Jev calls it [Noul](https://docs.typesafe.ai/primitives/noul), and OpenAI calls it [Predicate](https://developers.openai.com/api/docs/guides/decisions)) returns the probability that a statement is true. Your code decides how sure is sure enough.

The “📅” emoji is a suitable match for the title “Office lunch menu”.

Live

Using Bool to test whether an emoji represents the title

## [Examples](https://rubriclabs.com/blog/what-can-you-build-with-jev#examples)

### [Prioritizing notifications](https://rubriclabs.com/blog/what-can-you-build-with-jev#prioritizing-notifications)

We all get tons of notifications every day from different products, whether natively on your device or via email.

Knowing which ones need your attention now and which can wait is really critical.

So instead of doing it manually yourself or passing this on to a reasoning model, which can take many seconds and has real cost per notification, we asked Jev two questions: Does this notification need the recipient to act? And is it time-sensitive?

80%

Live0/8 requests0 priority

Prioritizing incoming notifications with Jev
A notification is marked priority when both answers come back at 80% or higher. That threshold is our choice. Change it in the figure’s top-left corner, then replay the inbox to sort it against the new cutoff.

[Click the priority pill on any notification to see Jev's answers.](https://rubriclabs.com/blog/what-can-you-build-with-jev#jev-notification-pill)
This example isn't perfect: we're not passing any context about the user.

Take the first notification, for example, Maya's message in #team about lunch at noon. Our two questions are written for work, so they treat lunch plans as something that can wait. So it's really important how you specify the criteria to the model, because your criteria determine how the model answers your questions.

Secondly, the model is only going to make a decision as good as the state or context you provide, which is true for any language model. So in another situation, if we provided more context about the user, perhaps its decisions would have been different.

### [Searching by meaning](https://rubriclabs.com/blog/what-can-you-build-with-jev#searching-by-meaning)

When you search a web page in your browser, it runs a literal search: it only finds the exact characters you typed.

Semantic search matches what you mean instead, so it can find an answer that shares none of your words.

Jev can do semantic search. In the figure below, we ingested every sentence from [Wikipedia’s article about platypuses](https://en.wikipedia.org/w/index.php?title=Platypus&oldid=1376973599) and made it searchable.

[Ask anything about the platypus, or click refresh for another question.](https://rubriclabs.com/blog/what-can-you-build-with-jev#jev-search-refresh)
LiveShowing 0 of 211 results

Searching an article on the platypus with Jev
In this demo, we first split Wikipedia’s article on the platypus into 211 sentences. During each search request, we ask two questions:

- A Choice question ranks all 211 sentences, using their IDs as the options. Choice accepts up to 255 options, so the whole article fits in one request.

- A Bool (Noul) question asks whether any sentence answers the question, where true means at least one sentence states or directly implies the answer.

We need both because Choice always ranks some sentence first, even when none answers. Ask "How fast can a platypus swim?" and Choice picks a swimming sentence at 85%, but the article never gives a speed. The Bool returns 5%, below our 35% cutoff, so the figure dims the matches.

One question rarely covers everything you need to know, so it often pays to ask several in one request: here, Choice finds where the answer is, and Bool tells you whether there is one.

Each search takes about 250 ms and costs 0.05¢. If you want to dig further into this use case, check out [this guide](https://docs.typesafe.ai/cookbooks/semantic_find).

NewsletterThe Grid
What we’re learning about building with AI. Two short emails a month.

### [Checking spelling](https://rubriclabs.com/blog/what-can-you-build-with-jev#checking-spelling)

Think of a Grammarly-style editor that checks your spelling as you type. Each time you finish a word and press space, we send Jev that word and the text around it. Once you type the next word, we check it again, since some mistakes only show up in what comes after.

The request sends two Bool questions in one call, the same pattern as the semantic search example above:

- Non-word: "Is this word, as written, a misspelled non-word?" This catches recieved and publsh. Names, jargon, and regional spellings count as correct.

- Wrong word: "Is this word spelled correctly but wrong for this sentence?" This catches form for from and loose for lose.

A typo gets a red squiggly line, and a wrong word gets a blue one.

LiveTotal cost: 0¢

Checking spelling as you type
We underline a typo when Jev is at least 80% sure, and a wrong word at 50%. The wrong-word bar is lower on purpose: in our tests, correct words never scored above 37%, so 50% still leaves a safe margin. Lowering it from 80% to 50% caught 8 of 12 wrong words instead of 5.

It still misses some easily confused pairs, like then and than or your and you’re. Those scored between 20% and 46%, below our bar.

If you fix a word yourself, its underline disappears, and Jev checks it again once you pause or press space.

Because the rules are written in plain language, you could also make the spellcheck programmable: tell it what to ignore, like startup names, acronyms, or slang, and it skips those words.

### [Finding settings](https://rubriclabs.com/blog/what-can-you-build-with-jev#finding-settings)

So far, each example asks Jev one round of questions. Here, Jev walks down the menus of iPhone Settings one level at a time, and each answer decides which question we ask next. Sorting something into a tree like this is called hierarchical classification.

[Search the phone for a setting you want to change, or click refresh for another one.](https://rubriclabs.com/blog/what-can-you-build-with-jev#jev-settings-phone-refresh)
9:41

Live

Finding a setting in iPhone Settings
The walk stops at a setting, or earlier if Jev is less than 60% sure of any option, leaving you on that menu page instead of guessing or going down the wrong path.

### [Rewriting emails](https://rubriclabs.com/blog/what-can-you-build-with-jev#rewriting-emails)

Jev also works well next to a larger model. Here, each email comes with a few things its writer cares about. Jev scores the draft on each one, and a language model, in this case gpt-6-luna, rewrites it until every score reaches 4 out of 5, or until it has tried three times.

[Click play to improve the draft, or refresh for another email and its criteria.](https://rubriclabs.com/blog/what-can-you-build-with-jev#jev-rewrite-refresh)
Sam,

The launch deck was due yesterday and I still don't have it. This is the second time this month this has happened, and honestly I'm tired of chasing you for it.

The whole team is waiting on your slides before we can do the dry run, and now we're going to have to push it. I need the deck today, no excuses.

Jordan

- Sounds friendly
- Makes one clear ask
- Doesn't blame anyone
- Explains why it matters

Live

Rewriting an email until it meets the writer's criteria

## [How does Jev compare?](https://rubriclabs.com/blog/what-can-you-build-with-jev#how-does-jev-compare)

While we were writing this post, new decision models kept coming out, from OpenAI's [Decisions API](https://developers.openai.com/api/docs/guides/decisions) (GPT-6 Luna Decisions) to Cloudflare's [Clef 27B](https://www.cloudflare.com/resource/clef-rl-interest), an open-weight model.

We were curious how they compare, so we ran a quick vibe-comparison by creating 101 hand-labeled scenarios based on the examples discussed in this post and running them against each decision model three times.

Overall, we found that Jev was the most accurate, fastest, and cheapest, but slightly less consistent. The gaps between Jev and GPT-6 Luna Decisions were small, except on price, where GPT-6 Luna Decisions was nearly twice as expensive. Clef was noticeably slower and about six times as expensive as Jev. See the full results below.

Jev 1.13GPT-6 Luna DecisionsClef 27B
Accuracy96%91%86%
Spelling (36 scenarios)86%69%81%
Notifications (20 scenarios)100%95%95%
Search (25 scenarios)100%100%100%
Settings (20 scenarios)98%100%70%
Latency
Fastest 10%182ms191ms321ms
Median211ms239ms471ms
Slowest 10%298ms339ms1850ms
Cost per 1,000 requests$0.13$0.23$0.73
Consistency (same answer each run)99%100%100%

Three decision models on 101 hand-labeled examples
It's important to note that we wrote these prompts for Jev and revised a few labels after our first run, so read this as a rough comparison rather than a benchmark.

## [What’s next](https://rubriclabs.com/blog/what-can-you-build-with-jev#whats-next)

To recap, all of these use cases could have been done with structured outputs from previous LLMs. None of this is fundamentally new.

What's different about Jev is that it's incredibly fast, cheap, and consistent. TypeSafe [measures it](https://typesafe.ai/blog/introducing-system-one-models-and-jev) at 40–200x faster than frontier models, and 445x cheaper. You've probably noticed this yourself using the figures in this post.

It's faster because it doesn't write. An LLM produces its answer one token at a time, and your code then parses it. Jev reads your question once and puts a probability on every possible answer at the same time, so it can't return an answer you didn't allow.

But overall, decision models like Jev open up use cases that used to be too slow, too expensive, or too hard to personalize and fine-tune. And since Jev-like models can run on smaller weights, many of them could even be done on device.

The field of decision models is moving fast. Try OpenAI’s [Decisions API](https://developers.openai.com/api/docs/guides/decisions), [Together’s model](https://www.together.ai/blog/how-to-train-your-own-jev), [Kev](https://openrouter.ai/jaredpalmer/kev-4b), [d1](https://www.liquid.ai/blog/d1-decision-model), [pplx-decider](https://huggingface.co/perplexity-ai/***.1-27b), or whatever comes next. We'll dig into how decision models work in a future post.
