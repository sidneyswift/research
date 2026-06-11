---
title: "We Gave GPT-4.5 a Myers-Briggs Test. It’s an Extrovert."
author: "Alex Duffy"
date: 2025-03-07
url: https://every.to/context-window/we-gave-gpt-4-5-a-myers-briggs-test-it-s-an-extrovert
words: 2498
---

*Hello, and happy Sunday! I’ve been writing for Context Window for a a couple of months, and I'm happy to report I am now at the helm. (I also help lead Every’s **consulting business**.) I’m obsessed with how AI tools are developing and, more importantly, what they can do for you. Every week you'll get my analysis of the latest news and trends in AI, along with everything we published last week and updates from **Every Studio**.—**Alex Duffy*

*Was this newsletter forwarded to you? **Sign up** to get it in your inbox.*

##

Release notes

### Allow us to re-introduce GPT-4.5

When GPT-4.5 arrived last week, expectations were stratospheric. For two years, people had been imagining a leap forward from GPT-4—an AI so brilliant it would feel superhuman in all regards. It was an impossible standard, and unsurprisingly, GPT-4.5 didn’t meet it. As we wrote last week, GPT-4.5 might not totally blow your mind, but might befriend you instead.

Having spent more time with the model, we can confidently say it’s lived up to that promise: We at Every are officially friends with GPT-4.5.

### Beyond benchmarks: Subtlety and nuance

Initially, GPT-4.5’s benchmark scores didn't amaze us, aside from its standout improvement on SimpleQA, a benchmark meant to test factual accuracy—on which it nearly doubled GPT-4’s performance and dramatically reduced hallucinations.

*Source:*

*OpenAI*.

Benchmarks, however, can be misleading. Different tasks require fundamentally different strengths. Code needs to be factually correct; evocative writing and humor often do not. To truly grasp GPT-4.5 or any of these models’ capabilities, getting specific with how you want to measure them is key. Getting creative, like Anthropic—which has its model playing Pokemon live—is encouraged as well. We tested GPT-4.5 with personality assessments like Myers-Briggs.

*Comparison of GPT-4.5 with other models on the Myers-Briggs test. Source: Python and Plotly via Alex Duffy*.

It emerged notably extroverted, with an ENTP designation of “The Visionary,” compared to earlier GPT models. (The idea of giving AI a personality test is admittedly strange, but it captures something real: how we perceive its communication style.) Interestingly, the previous Claude 3.5 also ranked extroverted and was known for a certain "magic." In Claude 3.7, priorities toward factual and coding accuracy were evident, so it performs much better there.

Expect to hear more from us at Every on benchmarks. Measuring the progress of these tools—and grasping why it matters—requires us to pay attention in new ways.

### The deeper linguistic layers

Regardless of benchmarks, how exactly does GPT-4.5 feel subtly better? Part of the answer lies in a richer understanding of the intricacies of language.

**Terra Blevins**, a researcher at the University of Washington, explored this exact phenomenon. She found that large models implicitly grasp linguistic structures—like how words form sentences (syntax) and how meaning emerges in context (semantics)—even without explicit instruction. The bigger the models, with more neurons and therefore more connections, the more of the subtleties of language they grasped. Our colleague **Evan Armstrong** calls this capability "vibe compute"—the ability of newer models to intuitively sense and respond to not just explicit instructions, but our underlying intent, tone, and emotional context.

Language models began by mimicking prose, capturing superficial patterns like sentence flow and punctuation—something **Andrej Karpathy** famously demonstrated back in 2015 in his landmark essay, ”The Unreasonable Effectiveness of Recurrent Neural Networks.” But as models have grown, they’ve developed better internal representations, enabling a deeper understanding of each word and its relationship with others.

GPT-4.5, thanks to its unprecedented size, navigates these layers effortlessly, making interactions richer, funnier, and more human-like.

### Your new writing companion

At Every, we write—a lot. GPT-4.5 is the first model that we have used that is at times legitimately a great writer. It hits a sweet spot Evan described as “not too hot, not too cold.”

Previous models struggled with style: Too cold meant repeating rigid patterns typical of LLMs, overusing the same bland constructions like, “It's not X, it's Y.” Too hot meant slavishly mimicking provided examples without generalizing.

GPT-4.5 strikes an impressive balance. “It feels like editing a writer who has a lot of talent but doesn’t necessarily know how to think through things,” says Evan. “GPT-4.5 has a sense of what's right—even if you couldn't articulate exactly why.”

That subtle intuition makes GPT-4.5 feel more like a true creative partner. And it's actually funny.

A surprising benchmark that has gained popularity, as it illustrates GPT-4.5’s subtle humor and creative capabilities, is “green text”—a concise storytelling style that originated on the social network 4chan. By asking GPT-4.5 to “finish the green text,” users can get a sense of what GPT-4.5 might think about a certain situation, encouraged to channel the absurdist humor typically associated with the 4chan style.

*Source: ChatGPT courtesy of Alex Duffy*.

### Why size—and cost—matter

This quality comes at a cost. Not only is training a bigger model more expensive, but every query you run on it is, too. GPT-4.5 initially debuted on OpenAI’s Pro subscription tier ($200 per month) likely due to its enormous computational demands. Now, it has been rolled out (with some limits) to Plus ($20 per month) users, opening it to a wider audience.

Costs will continue to fall though through a process called distillation. Conversations with large models like GPT-4.5 can be used as “synthetic data” that smaller models can learn from, replicating much of their performance at significantly lower costs. Eventually, this results in more accessible, affordable, high-quality AI.

It also means that the cost of recreating performance is orders of magnitude less than developing it for the first time, which makes pricing these models particularly difficult.

Despite the cost challenges, the incentives to train better models are enormous: Existing users and tools based on the latest models immediately become more powerful. **Simon Willison** noted that Code Interpreter, which gives ChatGPT the ability to run code, has barely changed since its release two years ago. Yet when paired with GPT-4.5, it clearly demonstrated improved real-world data analysis and problem-solving.

As the costs continue to balloon for larger and larger models, we might soon see nation-states developing their own models that reflect their biases, priorities, and goals.

Meanwhile, different AI companies are clearly picking lanes that they feel will help them better cater to specific customer needs.

-
**Anthropic (Claude 3.7 Sonnet):**After seeing that over one-third of all requests were about math and coding, Anthropic has focused on code. Claude 3.7 Sonnet is excellent at it, likely the best model available via API for software development. -
**xAI (Grok 3):**Built by a team that stood up the largest cluster of GPUs in the world in record time and is launching a game studio, it is no surprise Grok 3 is exceptional at math, gaming, and infrastructure. -
**Google (Gemini 2.0)**: Google’s mission statement is "to organize the world's information and make it universally accessible and useful." That extends beyond just text. Gemini 2.0 models excel at understanding rich multimedia data, like pictures and video—understandable given that the company owns YouTube. -
**OpenAI (GPT-4.5):**OpenAI has increasingly built products for mass appeal. Prioritizing nuanced communication, emotional intelligence, and everyday usability makes sense in this context. Consider the demo in the GPT-4.5 launch announcement, during which they asked AI for help sending an emotionally charged text. Unlike o1, GPT-4.5 deviated slightly from the instructions and rephrased the message in an apparent attempt to preserve the friendship.

### Subtle improvements, real impact

GPT-4.5’s strength is the quiet accumulation of deeper understanding, subtle humor, and genuine creative skill. It's harder than ever to discern just how good these models have become because they've reached levels of nuance many of us can't quickly put our finger on. Yet when you experience GPT-4.5 personally, you feel it. It's a meaningful advancement that quietly reshapes our relationship with AI, making it more like a collaborator and less like a mere tool.

## Knowledge base

🔏 **"How to Build Your AI Therapy Bot"** *by Mathias Maul:* Ever wish you had a therapist available at 3:00 a.m. when your thoughts spiral out of control? Good news—you can build one yourself. **Mathias Maul**, a therapist who's been using AI for personal development for years and works with tech companies, walks us through creating a customized AI therapy companion using LLMs. He shows how AI can create a judgment-free space where people can work through their thoughts. Read this for a practical, step-by-step guide to building your own AI therapist that matches your style, knows when to push you, and helps you break out of established thought patterns.

**"A Dynamic Framework for Making Product Decisions"** *by Edmar Ferreira/Source Code*: After a decade of building products, Every entrepreneur in residence **Edmar** got fed up with rigid frameworks like RICE (Reach, Impact, Confidence, Effort) that reduce complex decisions to arbitrary numbers. His solution? VICE, replacing Reach with “Vibe,” a dynamic framework that uses pairwise comparisons and the Elo rating system (yes, like chess rankings) to pit features against each other in a product-decision thunderdome. Read this if you want a more intuitive, flexible way to decide what to build next.

**"AI Has Learned How to Capture Our Emotional Metadata"** *by Evan Armstrong/Napkin Math*: What if the most interesting thing about AI isn't its ability to follow instructions, but its uncanny talent for reading your mind? **Evan** argues we're entering an era of “vibe compute,” where AI systems don't merely execute tasks—they intuit our preferences and feelings. This shift is already happening in coding assistants that understand “make this less clunky,” writing tools that grasp “make it punchier,” and voice AI that feels eerily human. Read this to understand the profound implications of machines that might soon understand your vibes better than you do.

🎧 **"You Don’t Need More Money—Just A Better AI Strategy"** *by Dan Shipper/AI & I:* If you’re worried your AI startup can't compete with OpenAI's coffers, investor Mike Maples (who wrote early checks to Twitter, Twitch, and Lyft) says you're thinking about it all wrong. The secret isn't building a better model—it's building a better strategy. In this episode of *AI & I*, Mike explains how “sea changes” in technology create asymmetric advantages for nimble startups, why business model innovation trumps product innovation, and how to find niches that AI giants can't or won't touch. Watch or listen to this if you want to understand how the economics of startups are fundamentally changing in the AI era—and how to position yourself to win. 🖥 🎧 Watch **on X** or **YouTube**, or listen on **Spotify** or **Apple Podcasts**.

**“How Knowledge Work Will Evolve in the AI Era”** *by Rhea Purohit/Learning Curve: *History is filled with people freaking out about new technology destroying cherished human skills (think: the printing press). AI is triggering the same fears today, especially for knowledge workers whose thinking abilities seem threatened. But research shows our cognitive skills won't disappear—they'll evolve from gathering information to verifying it, from solving problems to integrating AI output, and from executing tasks to overseeing them. Read this if you want to understand how your thinking will adapt in the AI era, and why that's not necessarily a bad thing.

## From Every Studio

**Toggle, customize, conquer: **Stop drowning in multi-inbox chaos. Now you can corral all of your personal, team, and work emails into briefs. With **Cora**'s new multi-account feature, you can easily add and toggle between inboxes—staying up to date on customer inquiries, meetings, and dinner reservations, all streamlined through briefs. Even better, invite users to view specific briefs—perfect for managing team inboxes, keeping your partner in the loop, or coordinating logistics with your assistant.

And whether you're an early bird, a night owl, or something in between, Cora now lets you customize the days and times you receive your briefs. Your inbox(es), your way!

**Turn your taste into content, anywhere on the web: **See an article you like? Use **Spiral**’s new Chrome extension to transform content directly from the tab you’re browsing into your format of choice—no need to switch tabs or copy and paste.

**Create mesh gradients with just a few clicks:**Experience Every creative lead

**Lucas Crespo**’s new mesh gradient shader app, which lets you craft beautiful animated textures (think lava lamps) with ease. What sets it apart? You can instantly copy the component code for any shader you create and drop it into your projects as a background or design element—making these gorgeous effects accessible to everyone. If you need a static version, download your creation as a PNG with one click.

**Auto-generate your Cursor rules:** Tired of manually coming up with Cursor rules to wrangle your code? Now you don’t have to. **Kieran Klaassen**, the general manager of Cora, has a go-to prompt that does the heavy lifting, generating rules that adapt to existing conventions in your codebase. Pro tip: Disable the "mdc editor" for the best results. Less friction, more shipping.—*Vivian Meng*

## Alignment

**Friction that teaches.** In her thought-provoking piece about AI therapy, psychologist **Maytal Eyal** warns that frictionless AI companions might erode our patience for human complexity. Her fear that we'll grow impatient with real relationships after tasting “algorithmic perfection” misses what history repeatedly shows us: Technological simulation heightens our appreciation for friction. Just like digital photography sparked a renaissance in grainy old films for which you had the satisfaction of holding a negative in your hand, AI's perfection will heighten our appreciation for what makes human connection real: its unpredictability and risk. The algorithm can't misunderstand you. It won't judge. It never rejects. And I think that's precisely its limitation. Real connection thrives on this inalienable friction because each exchange becomes an act of courage. What Eyal sees as a threat, I see as an awakening to the fact that we don't want perfect mirrors. We want the messy, challenging alchemy of minds that don't quite align, and the growth that comes from collision.—*Ashwin Sharma*

##

Hallucination

What if Spotify built hardware? An exploration:

*Source:*

*X/Lucas Crespo*

*.*

*That’s all for this week! Be sure to follow Every on X at** @every** and on** LinkedIn**. *

*We **build AI tools** for readers like you. Automate repeat writing with **Spiral**. Organize files automatically with **Sparkle**. Write something great with **Lex**. Deliver yourself from email with **Cora**.*

*We also do AI training, adoption, and innovation for companies. **Work with us** to bring AI into your organization.*

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

Love Spiral’s new Chrome extension! What if... I could use it to adjust content on the page though like an ARC boost?
