---
title: "What Actually Matters (And What Doesn’t) For DeepSeek"
author: "Evan Armstrong; Alex Duffy; Edmar Ferreira"
date: 2025-01-28
url: https://every.to/context-window/what-actually-matters-and-what-doesn-t-for-deepseek
words: 2238
---

*Was this newsletter forwarded to you? **Sign up** to get it in your inbox.*

News of DeepSeek’s R1 model, released last week, has sent shockwaves through the tech world. Like many of you, we at Every have been captivated by the Chinese startup’s inexpensive, high-performing model, and the innovations that were necessary to achieve it.

As for the implications? There’s a lot to reckon with, and we’re still only just figuring out what this new model can do. Investors mostly felt R1’s arrival on the scene wasn’t positive news for AI’s U.S.-based incumbents, and shares of Nvidia and other chip makers were hit particularly hard. Builders, meanwhile—including some of us here at Every—are pretty excited.

Because there’s so much to unpack, we’ve pulled together three of our writers to each tackle one aspect of the news that struck them, and where they see things going. **Alex Duffy** breaks down the innovations that led to R1 achieving a 90 percent cost reduction in performance compared with OpenAI’s o1 model. Entrepreneur in residence **Edmar Ferreira** discusses the immediate implications for people looking to build AI-based applications. Finally, **Evan Armstrong** talks about the markets’ (over-re)reactions.

Let’s dive in.*—Michael Reilly, managing editor*

## DeepSeek R1 is a shift from ‘sounding good’ to ‘thinking better’

Most large language models (LLMs) rely on reinforcement learning (RL) to refine how “helpful and harmless” they sound. Notoriously, OpenAI has used cheap labor in Kenya to label and filter toxic outputs, fine-tuning its models to produce more acceptable language.

DeepSeek R1 took a different path: Instead of focusing on *sounding* right, it zeroes in on *being* right—especially in math, coding, and logic. Rather than learning from subjective human preferences, R1 follows reasoning-oriented RL that rewards the model only if its code compiles and passes tests or if its math solutions are indisputably correct. Because “correctness” is easier to define for these tasks, R1 can scale its training without needing armies of human data labelers. Surprisingly, even for tasks that are more subjective—like creative writing—this emphasis on logical consistency tends to deliver better results, too.

R1’s leap in capability and efficiency wouldn’t be possible without its foundation model, DeepSeek-V3, which was released in December 2024. V3 itself is big—671 billion parameters (by comparison, GPT4-o is rumored to be 1.8 trillion, or three times as big)—yet it’s surprisingly cost-effective to run. That’s because V3 uses a mixture of experts (MoE) approach, where the model is divided into specialized sections, each of which functions as an “expert” in a certain domain. When a query comes in, only the expert section “lights up”—around 5 percent of the model, or 37 billion parameters. This significantly reduces the compute power needed. MoE gained traction in 2024 thanks to teams at companies like Mistral, xAI, and Databricks, which showed it can be easily integrated, scales well, and brings major efficiency gains.

On top of that, V3 embraced multi-token prediction (MTP). Rather than predicting text one word at a time and inspired by Meta’s FAIR (Fundamental AI Research) team’s ideas toward building "Better & Faster Large Language Models via Multi-token Prediction," it predicts multiple words simultaneously. Finally, a trick called FP8 training helps V3 run even faster and cheaper by using “rounded” (lower-precision) numbers. This approach slashes compute costs, memory usage, and reliance on huge GPU clusters—an especially big deal in an era of hardware export controls.

Crucially, thanks to R1's new distillation approach to maintaining performance with models of smaller sizes, these advanced reasoning skills don’t require a Google-sized infrastructure. DeepSeek’s distillation techniques let R1’s capabilities trickle down into smaller, more budget-friendly versions of the model. You can even run a distilled variant locally on your MacBook Pro with just one line of code. In conjunction with its open-source license, this efficiency has led many cloud providers, like Groq, to provide access to their own hosted version of the R1 model. Having options gives consumers more choices taking factors like speed, reliability, price, and privacy into account.

Perhaps R1’s biggest breakthrough is the confirmation that you no longer need enormous data centers or thousands of labelers to push the limits of LLMs. **If you can define what “correctness” means in your domain**—whether it’s coding, finance, medical diagnostics, or creative writing—**you can apply reasoning-oriented RL to train or fine-tune your own model**. You pick the benchmarks; you control the objective “good.” Meanwhile, V3’s underlying architecture and cost-saving optimizations ensure you won’t break the bank. By decoupling “performance” from raw scale and shifting it toward well-defined standards of correctness, and being willing to share its innovations, DeepSeek R1 hands more power to researchers, entrepreneurs, and even hobbyists—anyone willing to experiment on how we train and evaluate AI.—*Alex Duffy*

#### Sponsored by: Every

**Tools for a new generation of builders**

When you write a lot about AI like we do, it’s hard not to see opportunities. We build tools for our team to become faster and better. When they work well, we bring them to our readers, too. We have a hunch: If you like reading Every, you’ll like what we’ve made.

## Welcome to the post-training era for startups

Training LLMs can be divided into two major phases: pre-training and post-training. The pre-training phase is an extremely expensive process that involves training a general model from a large corpus of data. Even in the case of DeepSeek, a single run of training costs $6 million, while it’s estimated that Meta’s Llama 3 model costs $120 million to train. DeepSeek’s decreased costs are a huge breakthrough, but they’re still too expensive for most organizations.

Most companies outside of the big labs focus on post-training: We work on top of a "pre-trained” model like Llama to train it to be good at our desired tasks. There has been a widely held belief that post-training language models just surface data from pre-training, which means that language models can only interpolate plans or reasoning patterns seen in pre-training. I think that is clearly debunked now. DeepSeek R1 shows that LLMs can learn new things directly from post-training with reinforcement learning (RL).

DeepSeek R1 introduces revolutionary post-training techniques that can be applied across various open-source LLMs like LLama, making AI development more accessible and efficient, particularly for smaller organizations. Using reinforcement learning is like training a dog: You give it a reward every time it does the right thing. If you can automatically generate the reward, you can train the AI to do the task, even without providing it with many examples. The AI can learn from its own experience instead of only from human examples.

Traditional LLM fine-tuning requires extensive labeled datasets, creating barriers for smaller teams. DeepSeek R1 RL techniques address this by enabling models to fine-tune on smaller, specialized datasets, which are easier for smaller teams to collect. This is especially valuable in domains like math, where outcomes can be automatically verified against known solutions or specifications.

Organizations with deep domain expertise can leverage these RL techniques by creating customized evaluation sets and training environments. For example, healthcare startups can design scenarios mimicking clinical decision-making, while financial institutions can develop reward functions based on risk-management outcomes.

A key advantage of these RL advancements is their universal applicability across any open-source model. This flexibility allows organizations to future-proof their AI investments by using the best current models, and reusing the data and workflow to retrain when a better model comes up. For instance, a customer support AI could adopt newer foundational models while preserving its established reward systems for response quality.

However, DeepSeek R1 has several limitations:

- It underperforms compared to DeepSeek-V3 in complex tasks like using tools, complex dialogue, and roleplaying as characters.
- Its multilingual support is limited primarily to English and Chinese, with inconsistent performance in other languages.
- It shows sensitivity to prompting, with performance degrading when a small number of examples are used in the prompt (often called few-shot prompting).

Despite these challenges, DeepSeek R1 post-training RL techniques represent a significant advancement in AI development. By enhancing adaptability, emphasizing domain expertise, and ensuring universal applicability, they empower organizations to create more specialized and effective AI systems.

The technology particularly benefits startups and smaller teams, who can now compete more effectively in the AI space by focusing on their unique expertise rather than on data acquisition. Instead of collecting thousands of perfect examples, you just need to define what "good" looks like for your specific use case. As with training a dog, you don't need examples of every possible trick—you only need to reward the right behaviors. Startups can focus on their unique domain expertise and building great products, rather than spending months collecting and labeling training data. If you can automatically evaluate whether your AI is doing a good job at your specific task, you can train it to get better through trial and error, just like a human would learn.—*Edmar Ferreira*

## The view from the markets

Assume you believe in artificial general intelligence (AGI). Also assume that you believe that DeepSeek’s technical innovations make it possible to get there. With those beliefs in mind, ask yourself: How many years and how many dollars until we achieve AGI?

The implications for R1 are less to do with the present usefulness of DeepSeek's work—which is on par with other models—and more to do with whether these techniques can be used to make AGI happen on our existing infrastructure.

Big tech stocks were punished yesterday not because it proved their models weren’t useful, but because the inflated AI revenue expectations—and the data centers built to support those beliefs—were simply too aggressive in a world where DeepSeek-style models can offer inference at one-tenth the cost.

There is a world in which, with more intelligence more cheaply available, developers start clamoring for even more compute. This could very well be the case! However, the timing of data center utilization matters. Meta alone forecast spending roughly $65 billion on data centers *just this year. *Cloud hyperscalers like Microsoft or Amazon Web Services are forecasting similar levels of data center spend, while AI companies like OpenAI are setting up $100 billion data centers—and inference needs for these centers was just cut by 90 percent! Someday, somehow, these centers will hit 100 percent utilization rate, but the forecasted growth in training and inference costs on which these infrastructure projects were based has just been wildly upended.

In our previous work on bubbles, we happily noted that the infrastructure built out during a bubble eventually resulted in consumers benefiting in the long run. In the face of the DeepSeek news, similar arguments are being trotted out for big tech’s spendy ways. However, there are three reasons to cast doubt on that narrative:

- The dot-com bubble didn’t really pay off until Google and Meta took advantage of it, nearly a decade after fiber cables were laid.
- Data centers filled with GPUs have, at best, four years of shelf life before they rapidly lose value. Chips get worn out just like any other equipment, and newer models allow for more powerful use cases.
- So far, there is likely far less than $50 billion in AI application revenue globally. ChatGPT, by far the world’s best monetized pure-play AI application, only did $4 billion in revenue globally in 2024.

R1 does not spell the end of big tech. It speeds up timelines and likely forces some companies to reduce their data center build-outs (or at least justify them more thoroughly than they have up to this point).

Whether yesterday’s market reaction of Nvidia’s 17 percent stock plunge is justified is unclear. Our team is still debating the implications and will undertake further experiments in which we employ some of these training models ourselves. Some of us are shorting Nvidia; others are buying. Sign up to receive the results of our tests.—*Evan Armstrong*


*Evan Armstrong**is the lead writer for Every, where he writes the*

*Napkin Math*

*column. You can follow him on X at*

*@itsurboyevan*

*and on*

*, and Every on X at*

*@every*

*and on*

*.*

*Alex Duffy** is the consulting lead and a staff writer at Every, where he writes about empowering people with AI tools and technology in **Context Window**. You can follow him on X at **@theheroshep** and on **LinkedIn**.*

*Edmar Ferriera** is an entrepreneur-in-residence at Every. Previously he founded and sold Rock Content, a leading content marketing platform. You can follow him on X at **@edmarferreira** and on **LinkedIn**.*

*We also **build AI tools** for readers like you. Automate repeat writing with **Spiral**. Organize files automatically with **Sparkle**. Write something great with **Lex**. Deliver yourself from email with **Cora**.*

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

Terrific analysis, thank you. The DS ‘event’ has hastened the AI value pool accretion tilt towards the application layer. While their 6M training cost is suspect, their reasoning and architectural approach, which you have so beautifully highlighted, will hopefully lower the cost of intelligence for vertical-specific use cases.
