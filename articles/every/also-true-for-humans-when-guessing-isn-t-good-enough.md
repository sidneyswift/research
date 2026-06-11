---
title: "When Guessing Isn’t Good Enough"
author: "Mike Taylor"
date: 2024-11-19
url: https://every.to/also-true-for-humans/when-guessing-isn-t-good-enough
words: 967
---

# When Guessing Isn’t Good Enough

Solving AI hallucination with retrieval augmented generation

November 19, 2024 Updated June 2, 2026

*In **Michael Taylor**’s work as a prompt engineer, he’s found that many of the issues he encounters in managing AI tools—such as their inconsistency, tendency to make things up, and lack of creativity—are ones he struggled with with people. It’s all about giving these tools the right context to do the job, just like with humans. In the latest piece in his series **Also True for Humans**, Michael explores retrieval-augmented generation (RAG), in which you first search your documents to pass relevant context to the LLM to generate a more accurate answer.—**Kate Lee*

*Was this newsletter forwarded to you? **Sign up** to get it in your inbox.*

In 2012, on a trip from London to Havana, Cuba, I got into a heated debate with friends: Who is the best-selling author of all time—well, at least of modern times? (Sorry, Shakespeare.)

I thought it was Stephenie Meyer, author of the vampire romance series *Twilight*, but my friends disagreed. One thought it was *Harry Potter* writer J.K. Rowling, and another was convinced it was Arthur Conan Doyle, the author of the Sherlock Holmes books. There was no mobile internet in Cuba at the time, so we couldn’t look up the answer. Instead, we made plausible-sounding arguments for hours.

When we got home to London, we looked up the answer on Wikipedia and learned the truth: While Meyer had been the best-selling author the past few years, first place belonged to the detective novelist Agatha Christie, with 2–4 billion copies sold. By contrast, Meyer has sold about 100 million. None of us were right, but our answers were within the realm of believability, if not possibility.

ChatGPT does the same thing: It gives plausible-sounding answers, or “hallucinations,” when it doesn’t have all the facts. In fact, everything ChatGPT tells you is made up. Large language models do not really *know* the answer to any question. They’re just giving you the answer that’s statistically most likely based on its training data. ChatGPT is often close enough, however, that many people feel comfortable using it without having to fact-check everything it says. (You should absolutely fact-check ChatGPT.)

But there’s a simple solution that artificial intelligence developers have built into their LLMs in order to solve the hallucination problem and ultimately make these systems more accurate: retrieval augmented generation, or RAG, where the LLM you’re using first does a vector search (more on that later) to find relevant information, which is then inserted into the prompt as context for the AI model to consider. If you can breathe better accuracy into AI, they can improve from complex probabilistic guesswork to something much more reliable and helpful.

In the AI gold rush, startups such as Pinecone, Glean, Chroma, Weaviate, and Qdrant raised hundreds of millions of dollars selling RAG technology to AI developers. It’s also being built directly into popular generative AI applications. OpenAI’s custom GPTs—the third-party versions of ChatGPT they host—can use RAG in order to make use of the documents that users upload, searching for relevant snippets to include as context in the prompt. Once paired with RAG, AI systems are essentially taking open-book exams when they communicate with you. The answer is somewhere in the book—on Google, in your PDFs, in your chatbot message history. They just have to look for it.

Unsurprisingly, LLMs are better at finding an answer in a long document than they are at guessing the answers without context. With a little help, they don’t need to make something up, and you can get accurate answers based on sources of data that you trust. I’ll show you how we can make AI more trustworthy by teaching it to look up answers instead of guessing using RAG.

*Source: Screenshot from ChatGPT.*

## What if every concept had a postal address?

AI models don’t really see words. They use numbers to represent them. Think of numbers as a postal address or map coordinates, with concepts that are the most similar clustered closer together on a graph. When you upload documents to a RAG-enabled AI system, it will search to find relevant “chunks” of information and hand them over so the application can answer more accurately. To find the most relevant “chunks” in a document, it effectively plots them on a graph and looks for the ones that are closest to your prompt.

Imagine a simple AI model that has three variables: age, gender, and royalty. The three-dimensional space of the graph is called latent space—every word, phrase, or concept you query will have a location in this space. In the 3D graph below, find the point where the word *woman* is located. If gender is a spectrum, as you change that number from 10 to 0, you’ll get to where the *man* point is located on the graph. Alternatively, if you move along the age spectrum from man, you’ll get to *boy*, because a boy is just a young man. Finally, if you increase the, er, royalness of the *boy*, you get to *prince*, which is a royal boy.

**Become a ****paid subscriber to Every**** to unlock this piece and learn about:**

- The mathematics of meaning in AI's vector space
- Why context chunks matter more than raw data volume
- The untapped potential of AI-powered organizational memory

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
