---
title: "The Optimal Level of Optimization"
author: "Dan Shipper"
date: 2023-07-14
url: https://every.to/chain-of-thought/the-optimal-level-of-optimization
words: 939
---

# The Optimal Level of Optimization

Lessons on goal maximization from machine learning

July 14, 2023 Updated January 29, 2026

#### Sponsored By: Mindsera

This article is brought to you by Mindsera, an AI-powered journal that gives you personalized mentorship and feedback for improving your mindset, cognitive skills, mental health, and fitness.

How hard should I optimize? It’s a question I’ve often asked myself, and I bet you have too. If you’re optimizing for a goal—building a generational company, or finding the perfect life partner, or devising a flawless workout routine—the tendency is to try to go all the way.

Optimization is the pursuit of perfection—and we optimize for our goals because we don’t want to settle. But is it better to go all the way? In other words, how much optimizing is too much?

. . .

People have been trying to figure out how hard to optimize for a long time. You can put them on a spectrum.

On one side is John Mayer, who thinks less is more. In definitely-his-best-song, “Gravity,” he sings:

“Oh, twice as much ain't twice as good / And can't sustain like one half could / It's wanting more that's gonna send me to my knees.”

Dolly Parton, who seriously disagrees, is on the opposite side. She’s famous for saying, “Less is not more. More is more.”

Aristotle disagreed with both of them. He propounded the golden mean 2,000 years ago: when you’re optimizing against a goal, you want the middle between too much and too little.

Which one do we pick? Well, it’s 2023. We want to be a little more quantitative and a little less aphoristic about this. Ideally, we’d have some way to measure how well optimizing against a goal works out.

As is the case very often these days, we can turn to the machines for help. Goal optimization is one of the key things that machine learning and AI researchers study. In order to get a neural network to do anything useful, you have to give it a goal and try to make it better at achieving that goal. The answers that computer scientists have found in the context of neural networks can teach us a lot about optimizing in general.

I was particularly excited by a recent article by machine learning researcher Jascha Sohl-Dickstein who argues the following:

Machine learning teaches us that too much optimization against a goal makes things go horribly wrong—and you can see it in a quantitative way. When machine learning algorithms over-optimize for a goal, they tend to lose sight of the big picture, leading to what researchers call “overfitting.” In practical terms, when we overly focus on perfecting a certain process or task, we become excessively tailored to the task at hand, and unable to handle variations or new challenges effectively.

So, when it comes to optimization—more is not, in fact, more. Take that, Dolly Parton.

This piece is my attempt to summarize Jachsa’s article and explain his point in accessible language. To understand it, let’s examine how training a machine learning model works.

## Too much efficiency makes everything worse

Say you want to create a machine-learning model that’s excellent at classifying images of dogs. You want to give it a dog image and get back the breed of dog. But you don’t just want any old dog image classifier. You want *the best* machine learning classifier money, code, and coffee can buy. (We’re optimizing, after all.)

How do you do this? There are several approaches, but you’ll probably want to use supervised learning. Supervised learning is like having a tutor for your machine learning model: it involves quizzing the model with questions and correcting it when it makes mistakes. It’ll learn to get good at answering the types of questions it’s encountered during its training process.

First, you construct a data set of images that you use to train your model. You pre-label all of the images: “poodle,” “cockapoo,” “Dandie Dinmont Terrier.” You feed the images and their labels to the model, and the model begins to learn from them.

The model learns by a guess-and-check method. You feed it an image, and it guesses what the label is. If it gives the wrong answer, you change the model slightly so that it gives a better one. If you follow this process over time, the model will get better and better at predicting the labels to images in its training set:

Now that the model is getting good at predicting the labels for images in its training set, you set a new task for it. You ask the model to label new images of dogs that it hasn’t seen before in training.This is an important test: if you only ask the model about images it’s seen before, it’s sort of like letting it cheat on a test. So you go out and get some more dog images that you’re sure the model hasn’t seen.

At first, everything is very rock and roll. The more you train the model, the better it gets:

But if you keep training, the model will start to do the AI equivalent of shitting on the rug:##
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
