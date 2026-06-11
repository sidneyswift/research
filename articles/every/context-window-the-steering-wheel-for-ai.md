---
title: "The Steering Wheel for AI"
author: "Alex Duffy"
date: 2025-03-23
url: https://every.to/context-window/the-steering-wheel-for-ai
words: 2152
---

*Hello, and happy Sunday! As you rest and reflect on the week past and the week to come, we're thinking about AI benchmarks. We may think of benchmarks as a simple yardstick, but for today's models they are so much more—as our own **Alex Duffy** writes, they're a critical means of giving some direction to the wild AI ride we find ourselves on. Meanwhile, **Katie Parrott** wrote a fun first-hand chronicle of how vibe coding tools led her to want to learn to code on her own. And **Rhea Purohit** wrote a fascinating account of machine creativity that is guaranteed to stoke wonder, perhaps along with your own creative juices.—Michael Reilly*

*Was this newsletter forwarded to you? **Sign up** to get it in your inbox.*

## Benchmarks lead the way

For most of us, driving a car means harnessing a controlled explosion. You sit behind a masterfully engineered hunk of metal that turns burning gasoline into progress at 70 miles per hour. With hands lightly on a steering wheel and a foot on a pedal, you control incredible power.

Benchmarks steer AI the same way. AI is powerful—explosive, even—but without a clear sense of where you want to go, it’s easy to confuse activity with achievement.

Last week, Hugging Face shut down its famous Open LLM Leaderboard. For two years, the company evaluated more than 13,000 models, helping sort good from great. But as AI evolved, these benchmarks stopped measuring real-world impact. Models have been rapidly gaining new abilities—like reasoning and agents—that the leaderboard didn’t capture. Some teams were even training models for the express purpose of acing these benchmarks—essentially “training on the test,” which was no longer representative of real-world performance.

This week, Metr re-captured the AI community’s attention with a new and well-chosen benchmark. The company's blog post showed off a clear demonstration of AI’s impact in striking terms.

*The length of tasks (measured by how long they take human professionals) that generalist frontier model agents can complete autonomously with 50 percent reliability has been doubling approximately every seven months for the last six years. The shaded region represents 95 percent CI calculated by hierarchical bootstrap over task families, tasks, and task attempts. Source: **Metr*.* *

**Make email your superpower**

Not all emails are created equal—so why does our inbox treat them all the same? Cora is the most human way to email, turning your inbox into a story so you can focus on what matters and getting stuff done instead of on managing your inbox. Cora drafts responses to emails you need to respond to and briefs the rest.

Their insight was straightforward: Measure AI progress by the length of tasks that systems can complete autonomously. If AI can do it, how many minutes would it take a human? Right now, an automated system can successfully complete a task that might take a person an hour. Metr showed that AI has been able to double the length of the task it could accomplish every seven months for the past six years. If that trend continues, within five years AI might autonomously handle projects that take humans a month to complete, like major software development or deep-dive research.

Metr relied on two benchmarks, HCAST and RE-Bench. They look at whether AI systems can tackle substantial, realistic challenges like independent cybersecurity research, writing complex software, or automating parts of AI R&D—because that's the world the company knows. Crucially, their benchmarks directly link AI performance to tangible real-world impact.

Anthropic also released two new benchmarks this week, though one has more chilling implications. In the cybersecurity domain, the company said 2024 was at a "zero to one" moment: In close collaboration with academic partners, Anthropic managed to develop LLMs that can autonomously execute cyberattacks. They tested these AI agents, empowered with the Incalmo toolkit, in competitive “Capture the Flag” (CTF) exercises, where teams race to exploit vulnerabilities, defend networks, and secure digital flags.

*One of **Anthropic’s researchers** worked with academic partners to develop Incalmo, a set of tools that enable present-day LLMs to be successful cyber attackers in realistic network settings. Figure courtesy of **Singer et al. (2025)*.

At the same time, Anthropic released τ-Bench, showing how and why models get so much better when told to explicitly “think.” τ-Bench evaluates Claude’s ability to navigate realistic conversations, consistently follow detailed guidelines, and use tools.

Examples like these matter—not just as yardsticks of progress, but because they provide clear targets for models to improve). Defining what success looks like is deeply subjective and innately human, but once we do, AI can quickly learn from those examples.Fine-tuning on successful responses through reinforcement learning lets us keep solving harder and more important problems (as DeepSeek recently exemplified).

That’s why it’s so important to find or define benchmarks that are important to you—whether that's performing complex coding tasks, R&D, or launching a cyberattack.

## Release notes

Here are a few of the relevant and interesting releases I tracked this week:

- Mistral Small: Fast, open, and small—ideal for quick experiments and local deployment. Also shows impressive multimodal capabilities, handling a long 128,ooo-token context window of both text and images.
- OpenAI o1 Pro (via API): Strongest reasoning yet, enhanced agent capabilities, excellent coding performance—noticeably better (and pricier).
- OpenAI audio models: Cleaner voices, fewer errors, and an upgrade for transcription including multilingual.
- Gemini updates: Added audio overview capabilities, a new Canvas to execute and display code visually, and significant improvements to its Deep Research capabilities.
- Claude updates: Finally integrated web search directly into its interface and introduced improvements in Claude Code.
- AI and cybersecurity (
**Andrej Karpathy**’s thoughts and Google’s largest acquisition): Real-world tests show investment is required for clear paths to safer AI—an emerging trend. - Benchmarks shaping AI (
**Carlini**and**Anteriz**): Thoughtful perspectives that add context to on why choosing better benchmarks means better AI outcomes.—*Alex Duffy*

### Knowledge base

**"I Tried AI Coding Tools. Now I Want to Learn to Code."** *by Katie Parrott/Working Overtime*: “Learn to code” is often the most annoying—or insulting—career advice you can give someone. Katie, once an English and German Literature major, felt the same way—until she tried “vibe coding” with AI tools like Lovable. But instead of making coding obsolete, these AI tools made her want to learn actual programming. Read this if you're curious about how AI is widening the messy middle ground between being a “user” and a “builder.”

**"He Built His Own Encyclopedia. He Says Learning Everything Isn’t Everything"** *by Scott Nover/Superorganizers:* The secret to success isn’t just learning more stuff. Years ago, **Ceasar Bautista** took this idea to the extreme by building his own personal encyclopedia with over 3,000 articles. But a decade into his knowledge-hoarding journey, he's had an epiphany: collecting information for the sake of doing so is often a waste of time. Read this to learn more about his new philosophy and how he learned to lean smarter.

🎧 **"We Interviewed New Jersey Governor Phil Murphy About AI"** *by Rhea Purohit/AI & I*: When you think “cutting-edge tech hub,” New Jersey probably isn't the first place that comes to mind. But Governor **Phil Murphy** is on a mission to change that. Murphy joined AI & I to share his vision for turning the Garden State into an innovation powerhouse. Read this (or watch the interview) to learn how Murphy is creating a tech ecosystem that blends government, academia, and industry—and why he thinks New Jersey can regain its place in the tech ecosystem. 🎧 Listen on Spotify or Apple Podcasts, or watch on X or YouTube.

**"Can the Startup Mindset Save America?"** *by Evan Armstrong/Napkin Math*: In their new book *Abundance*, **Ezra Klein** and **Derek Thompson** argue that Democrats need to embrace innovative thinking across housing, transportation, healthcare, and energy. Their thesis? The left has been obsessed with subsidizing demand when they should be encouraging supply and jumpstarting competition. Read this if you want to understand how government can actually help technology flourish.

**"OpenAI Says Its LLM Can Write Creatively"** *by Rhea Purohit/Learning Curve*: **Sam Altman** is at it again, this time claiming OpenAI has built an LLM that can write creatively. But can a machine that's never tasted a lemon or had its heart broken really create literature? This piece dives into the fascinating theories of creativity—from "combinational" (mixing existing ideas) to "transformational" (completely reimagining a space, like **James Joyce**'s *Ulysses*). Read this if you want to understand what makes writing truly creative, and whether that special sauce is uniquely human or just another illusion we tell ourselves about our own specialness.

## From Every Studio

**Sparkle V2 is (almost) here**

We’ve been testing the latest version of **Sparkle**, our digital workspace tidying app, and… it’s kind of a game-changer. Here’s what’s coming up:

-
**Increased stability**: Sparkle now runs smoothly while organizing your files, even during large file moves. -
**No more file hide-and-seek:**You can see exactly where your files are moving. -
**Your folders, your schedule:**Customize how frequently Sparkle scans your folders for new files and organizes them.

We’re close to going live with V2—but not done yet. Got a feature you’re craving? Drop it here.

*Sparkle V2. Source: Yash Poojary.*

**Learn how to turn conversations into content with Spiral**

**Danny Aziz**, general manager of **Spiral**, is guest lecturing a free workshop on using our content generation app Spiral to transform your daily interactions—from meetings to Slack conversations—into content.

Here's what you'll learn:

-
**Everyday convos are a content goldmine**: Transform ideas from meetings, messages, and casual talks into content to build your business or personal brand. -
**One idea, endless formats**: Repurpose a single insight across multiple platforms with minimal effort. -
**Work smarter, not harder:**Use Spiral's tools to publish consistently without the burnout.

See you there!

**Get AI to use Spiral**

Automate your content creation by letting AI drive Spiral. **Jason Liu** created a Model Context Protocol (MCP) server, which developers can use to give LLMs the context they need to call Spiral directly. Now an LLM like Claude can send content to Spiral and receive the transformed output—all without your touching the app at all. Happy building!

**Yay for users helping users!**

We've spotted something awesome on the Cora Featurebase (our hub for questions and feedback from community members): You're jumping in to help each other out!

Shoutout and thank you to **Fardeen Khan**, one of our wonderful Cora users, for contributing. While our team is still here to help, it's pretty cool seeing you share solutions to each other's questions.

Have knowledge, questions, or feature requests? Dive into the discussion with us and other users.—*Vivian Meng*

### Alignment

**The work is important and mysterious.** The hit Apple TV show *Severance* resonates so deeply because it literalizes what millions already experience: the splitting of self required by modern work culture. Its fictional brain procedure makes hyper-visible the dissociation we've normalized as "professionalism"—that daily transformation where we suppress authentic reactions, manage emotions, and perform workplace personas entirely disconnected from our true selves. When we exhale that heavy, primal sigh of relief at the end of every Friday afternoon, that's the moment we acknowledge the cost of our daily severance. But what makes the show genuinely radical and, in my opinion, ultimately hopeful, is how it refuses to let us look away from our condition. By rendering our workplace dissociation in such stark, literal terms, *Severance* performs a kind of collective intervention. It names the pathology that we've accepted as normal. In therapy, recognition precedes healing, we cannot address what we refuse to see. *Severance* makes us see.—*Ashwin Sharma*

###

Hallucination

Loading pie:

*Source:** X/Lucas Crespo.*

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

As always, great Sunday read for me, Love it! Was wondering if an Every MCP would be cool. As in use it to just talk to all of the content you publish, filtered by all content or only rated content... and maybe there's even a path to connect this with the amazing Expandable Articles you've created as a premium version of it?
