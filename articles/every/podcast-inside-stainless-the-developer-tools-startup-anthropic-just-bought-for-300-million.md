---
title: "Inside Stainless, The Developer Tools Startup Anthropic Just Bought for $300 Million"
author: "Dan Shipper"
date: 2026-05-20
url: https://every.to/podcast/inside-stainless-the-developer-tools-startup-anthropic-just-bought-for-300-million
words: 7167
---

# Inside Stainless, The Developer Tools Startup Anthropic Just Bought for $300 Million

'AI & I' with CEO Alex Rattray

May 20, 2026 Updated June 10, 2026

**The transcript of AI & I with Stainless CEO Alex Rattray is below. Watch on X or YouTube, or listen on Spotify or Apple Podcasts. [Disclosure: I’m a small investor in Stainless.]**

**Timestamps**

- Introduction: 00:01:15
- APIs and MCP, the connectors of the new internet: 00:05:09
- Why MCP exists: 00:11:00
- Why MCP servers are hard to get right: 00:17:15
- Design principles for reliable MCP servers: 00:20:24
- Using MCP for business ops at Stainless: 00:25:06
- Alex’s take on the security model for MCP: 00:40:57
- How one-off AI actions become permanent production software: 00:44:42

**Dan Shipper**

The internet runs on computers talking to each other, but its entire architecture was built for a pre-AI world. Now we’re trying to hook AI up to the internet with MCP—Model Context Protocol—which turns any website or web service into a set of tools that an AI can use natively to get work done. And the software companies that learn how to do MCP well are going to win over the next decade.

That’s why I brought Alex Rattray, the founder and CEO of Stainless, onto the show. Stainless’s job is to help computers talk to each other. They make the APIs and SDKs for all the big companies you know about, like OpenAI and Anthropic, and they’re starting to build MCP servers too. Alex and I get into the nitty-gritty of what the future of MCP looks like, how to design good MCPs, why MCPs are actually really hard to scale and possibly insecure, and we try to figure out together what a better model for allowing AIs to use the internet might look like.

This is a great episode. Alex is a good friend of mine. Let’s dive in.

Alex, welcome to the show.

**Alex Rattray**

Thanks, Dan. It’s really exciting to be here.

**Dan Shipper**

It’s good to have you. For people who don’t know, you are the founder and CEO of Stainless, which is the API company. You make APIs for companies like OpenAI and Anthropic—just name your big company that you might use their API, and Stainless is probably behind it. Before that you worked at Stripe doing their API, which makes total sense. And before that, most importantly, we were very good friends in college and have remained good friends. We were both starting companies in college. I’m a tiny investor in Stainless. It’s been really fun to watch your journey and get to hang out together so much over the years, and I’m just very excited to bring you on to talk about AI and what you’re doing at Stainless.

**Alex Rattray**

Thanks, Dan. It’s been really fun over the years. When we were in college, I was working on a startup and you were working on a startup. You had a conference room at a venture capitalist office as your office, and you let me crash there with my co-founder and team. We were just on the other side of the conference table hacking away into the evening. Very fond memories of those days. And these days it’s not every evening, but on the weekends, whatever—the same thing is still happening. You don’t see that every day, and it’s a really nice feeling. It’s been great to see everything happening with Every along the way.

**Dan Shipper**

Thank you. As I say, I started from the bottom, now we’re here.

The thing I always say when I run into people and they ask me about you—in order to embarrass you—is that you’re the only person I know of who has consistently run barefoot through the streets of Philadelphia. When we first met, you were not a fan of shoes and you were a fan of running. You want to talk about that?

**Alex Rattray**

It wasn’t that I didn’t like the concept of shoes—it’s that I couldn’t find a good pair. At a certain point, I was running through Nikes and they would bust open every few months. I think what was actually going on is that I had really wide feet and was probably buying narrow shoes. Shoes would constantly get ruined, and on a college budget it’s just like, “This is no good.” Eventually I decided, okay, the longer you wear your shoes, the more worn out they get, but the longer you just wear your feet, the tougher they get.

**Dan Shipper**

“The longer you wear your feet.”

**Alex Rattray**

Try it out. Try this at home. What could go wrong? I actually currently have a really annoying splinter in one of my feet—so don’t actually try this at home. But—

**Dan Shipper**

Are you still running barefoot?

**Alex Rattray**

No, no. This is just from around the house.

**Dan Shipper**

Dangerous.

**Alex Rattray**

Yeah. But see, that’s the thing. If I had been going around on the asphalt without socks on, my feet would’ve been tougher and I’d have no splinter.

**Dan Shipper**

So when you’re not running barefoot, you’re running Stainless. You’re around 50 people now, right?

**Alex Rattray**

Just about, yeah.

**Dan Shipper**

That’s pretty wild. You started Stainless in a pre-AI world, and now we’re in an AI world, and I think you have some ideas for what the future of AI is going to be and how APIs fit into that, how MCPs fit into that. Do you want to paint a little picture for us about where we’re going?

**Alex Rattray**

I would love to. To start—what’s an API? Not everybody’s familiar with that. It stands for application programming interface. There will not be a quiz, right, Dan?

**Dan Shipper**

No quizzes.

**Alex Rattray**

Great. Basically, it’s how one computer program talks to another computer program. It’s how computers talk to computers, how apps talk to apps. APIs are the dendrites of the internet. Dendrites are where your neurons connect and actually exchange information with each other. If you have two neurons in your brain but they’re not talking to each other, you’re actually not thinking. There is no thought happening in a brain without connections between neurons.

And if you think about the internet—if all these servers in the cloud weren’t talking to each other, you wouldn’t have internet. Programs, internet software, does nothing without APIs, without connections to other programs. It’s really fundamental to the mesh of pretty much all modern software. Everything we think of when we think about technology—APIs are at the heart and center of that, just like dendrites are the center of the mesh of the brain and how we think.

Stainless’s mission from day one was to make it easier for computers to talk to computers. The long-running trend of technology is toward more automation. APIs are how most business-to-business interactions, in some format or another, become real, become automated.

What we see with the rise of AI is that a new computer has entered the chat. There’s a new kind of system that can talk to other systems—or at least we’d like it to be able to. You used to have either humans interacting with a computer through a user interface, or a computer interacting with a computer through an API. Now we have LLMs interacting with computers. What’s that through?

Anyone familiar with Every and who’s a regular listener will know MCP—Model Context Protocol—which is a system for connecting LLMs to computers broadly speaking. It’s an area we’re investing in at Stainless. It’s really part of our core mission of making it easy for computers to talk to computers.

The core product we first brought to market is software development kits, SDKs. These are ways of saying, “Okay, Stripe has this great REST API. You can send JSON over HTTP and get back JSON over HTTP. And if you want that to be really convenient, you’re going to use the Stripe Python library, the Stripe Python SDK.” If you’re a Python developer, you’ll go pip install stripe, and then in your application code you’ll write stripe.customers.create, and all of a sudden you have a nice new customer object in your Stripe database and you’re off to the races. Or stripe.charges.create in the old days, to charge a credit card.

SDKs give developers that easy way to interface with an API. What’s the thing that gives LLMs an easy way to interface with an API? You might say MCP, and in a sense you’d be right. But what we’re seeing so far as MCP rolls out into the world and people experiment with it is that it’s not working so great. It’s difficult to deliver on what I see as the core vision of what’s so exciting about MCP.

A dashboard and a user interface lets you click around, see a bunch of stuff, fill out forms, click buttons, do things—anything you’d do while interacting with software, you do through the UI. But LLMs interacting through MCP tend to be much more restricted. You can only do a few little things. There’s usually not a ton of tools you’re going to be exposing to the models.

**(00:10:00)**

**Dan Shipper**

Just to stop you there—what I’m hearing you say is that just like a website is built for humans to use, MCP is sort of the equivalent for models. You can think of it as exposing a set of tools the model can use to perform certain functions. Just like you might click a button on a website, MCP gives the model a bunch of things it can click on or use to get work done.

An example might be a Gmail MCP that has a send mail tool, a compose mail tool, a read inbox tool—that kind of thing. And instead of a human going on the Gmail website and doing it, the LLM is essentially logging in and using it itself. It’s a native interface for language models. But you’re saying that’s not working that well. Can you tell me more?

**Alex Rattray**

Let’s start with what I see as the big vision of MCP and, in some sense, the big vision of agentic AI in the first place. I’ll start with the most pedestrian example you can imagine.

Let’s say Dan walks into my store and buys a pair of stripey socks and maybe a few other things. The next day I hear back from Dan that there’s something wrong. It happens, you know? I turn to someone on my team and say, “Hey, can we refund Dan for those stripey socks he bought yesterday and send him a discount code for next time with a little thank-you note, because we like to take care of our customers?”

This is the most normal thing to do in software—some little task like this. What the member of my team would be doing is opening up their internal admin and looking around. They might go to the Stripe dashboard and look through the list of payments or transactions or orders to find one that has someone named Dan. Which Dan? There might be a bunch. Look through the list of products in the order to see whether there were stripey socks in there. That might be a few clicks. Find the right one, then go to the screen where you can create a refund, create the refund, make sure it’s the right amount, then go and create the discount, then take that discount code and send it over to some other SaaS app to send the mail automatically.

Of course, in a business-to-business context, you might be going into Salesforce and sending a Slack message to an account manager, so on and so forth. In the normal course of work, it’s just the most normal thing in the world—having one task involve going through five different apps, each time 15 different clicks and scrolls and loading spinners, just to do one simple thing.

The promise of agentic AI is to take that same prompt and type it into ChatGPT or Claude or whatever, say, “Hey, can you help refund my friend Dan?” and just have the AI go off and do that—go through these five different apps and the 15 different screens and the various button presses to complete the task and then come back and say, “Great, it’s done.”

In order to do that—and there are only so many tool calls you have to make as an AI model to perform that exact linear chain of events, so it’s somewhat tractable—but if you think about this in the general case, you want your agentic AI to be able to do anything that human operator would have done, without having to wait for a bunch of JavaScript to load on a website or anything like that.

That means you need not only the Stripe create refund tool and the Stripe list transactions tool and the Stripe list products and lookup customer and create discount tool—you need not only those tools, but you need everything you can do in the Stripe dashboard, which is basically everything you can do in the Stripe API. And that’s actually a lot. There are hundreds of different endpoints in the Stripe API. The Stripe dashboard is massive. It’s a huge application.

If you were to take that list of tools today and go to an LLM and say, “Hey, here’s our MCP definition for all of this. Here’s a create refund tool, here’s a create transactions tool,” so on and so forth, and tell it all about those tools—all the descriptions, all the different request properties, the response properties, all the documentation—everyone listening already knows: you’ve just burned through your entire context budget. That’s hundreds of thousands of tokens just in pretty much translating the Stripe OpenAPI spec directly over to MCP tools. Today’s models not only can’t handle that amount of context, it’s a poor use of context because you have a lot else going on. But it’s also just confusing to the model. It’s too much to hold in your brain at one time.

And that’s just the Stripe part of it. What you’re really trying to do is enable your operators to do anything they would normally do. And that spans many, many different SaaS tools. In the course of one interaction, it might be five. In the next interaction, it might be a different five. If you think about every single SaaS tool your business uses on a daily basis to get work done—ideally you’d want every single one of those tools exposed to your operators in their AI chat, with every single tool available, with every nook and cranny and corner case available, so you can do anything through AI. That’s the vision.

There are a lot of problems with that. The biggest is this context window limit. But you also have all sorts of security and permissions problems, because you don’t want the AI to color outside the lines and say, “In addition to refunding Dan’s socks, I also refunded every customer for all transactions ever. And then I sent a bunch of money to my own AI bank account.” There’s more to the challenge, but that’s the vision.

**Dan Shipper**

I think the place we started was you saying it’s not working. But I don’t think that’s the reason it’s not working today. Is that the reason why it’s not working today?

**Alex Rattray**

What people do with MCP today is sometimes try to expose all parts of their API. The way people generally build MCP tools is they have an underlying API—usually a REST API—and they wrap different parts of it, different endpoints, different operations, in MCP tools. You can do that in a one-to-one mapping, or you can kind of handcraft things for the MCP. Today, in order to succeed, people are finding you really have to handcraft it to the MCP, to the LLMs. You have to say, “Okay, I’m making one specialized tool to look up a customer and refund their transaction based on a description.”

**Dan Shipper**

So there are all these decisions you have to make where you need to have the ergonomics of the model in mind—how the model thinks—in order to make sure the model does the right thing more often than not.

**Alex Rattray**

Yeah, it’s hard. I use this SDK analogy sometimes. It took a long time for humanity to get to the point where we could make a really good Python SDK for a developer wrapping an API. I think we’ve cracked that nut. Stainless offers really great Python libraries, but we’re building on the shoulders of giants here. We haven’t figured out how to expose an API ergonomically to an LLM in the same way we’ve figured out how to expose it ergonomically to a Python developer. That’s a new research problem in a sense.

And it’s harder because I can go learn how to be a Python developer if I want. I can’t really learn how to think or see like an LLM. That makes it tricky.

We do have at Stainless some things we’re cooking up to address some of these problems. LLMs have a really hard time with a repeated, sustained chain of actions. Even if you get an API response back for “list all the transactions,” there’s so much data, and you might have to go through the next page and the next page to find the one that has Dan with the stripey socks. That’s again a ton of context with one or two small needles in the haystack. LLMs are pretty good at that, but not perfect—and with too much hay, we all end up throwing up our hands. That’s true for LLMs too.

**Dan Shipper**

When you’re building MCP servers for people—and when you see people doing it well today—what are the principles? How do you think about making an MCP server that one, people use, which is actually a big one, and two, when it is used, actually does the right job?

**(00:20:00)**

**Alex Rattray**

There have been relatively few times I’ve seen it done well. I have seen it done well. We’re cooking something up that I’m really excited about. But with today’s technology, you really have to do a good job of product management. You have to go out into the market, talk to your customers, see what their actual needs are, look over their shoulders as they use and operate your software, and think about what you could unlock through AI where people would be doing things they can’t really do with your software today—because it just got so much easier. Then you have to do a lot of engineering work to wrap it up in a bow that works for the models.

You have to set up a really good system for evals, and if you’re doing MCP, you have to think about the different clients people might be using. Are they using Cursor? Are they using Claude Code? Something else? And the different models underlying all that. You end up with a pretty crazy matrix of things to optimize for and ways to evaluate whether what you’re offering is working well.

It’s also kind of a black box to get that feedback back to your servers so you can find out: we gave a tool call response here, was it actually any good? Did the user like it? Was the LLM able to use it? That’s a problem I haven’t seen a lot of people solve yet. Thinking about that as a first-class thing—maybe you have a send feedback tool, which is something we’ve been thinking about—so that if a user says out loud in the chat, “Oh man, that was useless garbage,” at least the MCP server finds out about that.

**Dan Shipper**

Is there anything more concrete you’ve learned about how to design a good MCP server—beyond the obvious stuff about talking to customers and thinking about use cases?

**Alex Rattray**

You want to keep the number of tools relatively small. You want the tool name and the description to be really precise and specific.

**Dan Shipper**

Aren’t those two things at odds?

**Alex Rattray**

Yes. Good writing is hard. You can make a great tool that looks up a person by name and product description and then refunds them. You also want a small number of properties in the input schema—a small number of parameters, concisely described but sufficiently described. This is also hard. You want the response data to come back with very little data—only exactly what the model will need. That’s also very hard because you may not know a priori which things the model is really looking for.

We have a technique we use in our MCP servers today where we give the model a JQ filter, which is a way of filtering out JSON, and that can work pretty well. But that’s kind of a special trick.

**Dan Shipper**

Doesn’t this mean that MCP just needs another level like a search tool—search, like, find a list of relevant tools given my task?

**Alex Rattray**

The tool browsing problem is definitely a serious one, and that is one approach. We actually do this at Stainless today, where you can get an MCP server for your API that just has, like I was saying earlier, the very simple thing of every endpoint exposed as a tool. If you have a small API, that works great. You can also filter it, so you expose an MCP server with only a small subset of your endpoints. That works great.

You can also use what we call dynamic mode, where there are three tools no matter how big your API is. One is list endpoints, another is get endpoint and learn about it, and the last one is execute endpoint. That enables the context thing to scale really well, but it means three turns of the model just to do one thing. So that gets slower. It’s more expensive in another sense, and there’s some lossiness. It performs pretty well usually, but not quite as well because the tools aren’t loaded up in quite the same way.

Are you using MCP servers yourself?

**Dan Shipper**

Yeah.

**Alex Rattray**

Funnily enough, not so much on the coding side—I use it on the business side. I’ll use the Notion, HubSpot, and Gong MCP servers and an MCP server for our database—a read-only copy—and say, “Hey, what are the interesting customers that signed up for Stainless last week?” It’ll go off and make a great query of our Postgres database, cross-reference those things in HubSpot, look up our notes in Notion, maybe even look at transcripts in Gong, and tell me all about it. It’s incredible.

**(00:30:00)**

**Dan Shipper**

And so that’s one of your big use cases. How often are you doing that? I’m now interested—not even from an MCP perspective, but for anyone running a business with some complexity who wants to know what’s going on. What are you actually doing, what is the report that comes out, and how often? Tell me so I can steal it.

**Alex Rattray**

For me it’s still usually in kind of playing-around mode. One of the things is the MCP servers disconnect, and then I get annoyed. You have to reconnect, which is not a huge deal, but there are a lot of little paper cuts still in technology this new that can hold back some amount of usage.

One thing I found really helpful at the meta level—and I’m sure you’ve had other guests talk about this—is the practice of just collecting notes for the AI by the AI, then edited and curated by yourself. I have a notes folder, a research folder, something like that in a special Git repo that I use just for this sort of internal stuff. I tell the AI: “When you find interesting customer quotes, put them in this folder and give the full citation,” so that the next time I start asking interesting questions, it doesn’t have to go searching through the MCP servers again. It has them cached in markdown files on disk.

**Dan Shipper**

Wait, that’s crazy. What are you using to write into that Git repo? Is it Claude Code? ChatGPT? How does it get in there?

**Alex Rattray**

I use Claude Code these days for that kind of thing.

**Dan Shipper**

So you just have Claude Code open and running, and then a new customer testimonial comes in and you’re like, “Hey, can you throw this into my master company Git knowledge repository?” And then whenever you need anything later you’re like, “Claude, go search through my master repository to figure out where the best customer quote is for this.”

**Alex Rattray**

Totally.

**Dan Shipper**

That’s so cool. What kind—can we see it?

**Alex Rattray**

No, it’s too messy and probably has a lot of confidential information—the latter being more important.

**Dan Shipper**

When you say it’s messy, are you having Claude organize it at all? How is it structured?

**Alex Rattray**

There’s a lot that I want to do here that we haven’t had the chance to do yet. There’s some lower-hanging fruit that our business team is working through right now, just on the basics of your CRM systems and so on. It’s not well-structured now, but I think that’s fine. I’m not going to prioritize structuring it super well until we’re using it more broadly. I use it some of the time. One of the business people on the team uses it a fair amount. One or two of our customer support engineers use it a lot. But it’s not yet broader than that, and I’d like it to get there. Once we see how everything’s evolving, that’s when we’ll start bringing in more structure. As it is, Claude Code can handle unstructured stuff really well. You don’t have to think about it too hard in advance. You can move things around later.

**Dan Shipper**

What else do you have in there other than customer quotes?

**Alex Rattray**

SQL queries. I’m a software developer—I don’t write a lot of code these days, but I spend a lot of time doing that. When I say, “Hey, how is our month-on-month growth of XYZ metric over the last three months?”—I did this recently for my last board prep—it came out with a pretty good answer right away, and I was like, “Wow, this is awesome.” Then I looked a little deeper and realized I actually wanted to exclude certain users from the analysis and filter it this way and that way. I imbued more business context into that SQL query and iterated with Claude Code to get it better and better for the specific metric and the specific story I was trying to tell. Then I got it to a good place and said, “Great, let’s dump this into an analytics folder for future use.”

**Dan Shipper**

So next time you’re doing board prep, you can be like, “Hey, what was that query we did last time?” and it’ll go get it.

**Alex Rattray**

Yeah. That’s really cool.

**Dan Shipper**

What else?

**Alex Rattray**

As any software team is doing these days—we’re using this for, “Hey, a customer comes in with a question. Can Claude Code just fix it?” In some cases, a Linear ticket gets filed, and our support engineers are really very technical. They may not have the wall clock time to chase down the fix themselves on an incoming bug. They have the technical skill, but another customer writes in two minutes later and they want to jump on that. They don’t want to be knee-deep in a debugger.

So sometimes what we do is file the ticket—intending to do it later, or for another engineer to do it later—but say, “Hey, can we see if Claude Code can just take a crack at it?” Is that going to work out 100% of the time? Definitely not. Is that going to work out 50% of the time? Still no, to be honest. But can that improve the overall efficiency? Yeah, maybe. We’re still experimental there, but we’re seeing a lot of promise.

**Dan Shipper**

In our pre-production call, you were talking about having a big vision for the future of AI. Do you want to walk me through that?

**Alex Rattray**

I would love to. We talked earlier about how agentic AI can make operators’ lives a lot easier by taking certain pedestrian tasks and running with them independently. That’s something I think as an industry we’re almost on the cusp of.

A big part of the way I see things unfolding from here—I like to say the future of AI is cyborgs. Which is already sort of ridiculous because what is a cyborg other than a robot? But cyborg, as I understand it, is a term that means you’re part person and part machine. In this case, when you go and talk to an agent, what you’re going to be getting is part LLM neural net and part code—where the machine I’m talking about is traditional CPU software, not GPU software.

I think this will play out in two main ways. One is your kind of one-off operational use cases like we were talking about a minute ago, and then the other is production software.

In the use case where someone needs to perform some tricky one-off action with a bunch of points and clicks, and now we want an AI to just make a bunch of tool calls—the way I actually see that happening and what we’re building toward is code execution. Rather than the model having a bajillion tools, the model has two tools. One to execute code—where it just has a text box of “put in some TypeScript, and you’re going to use this API’s TypeScript SDK, and you’re going to write stripe.charges.list, stripe.customers.retrieve, stripe.refunds.create.” This is really easy for models. They’re really good at writing code.

**(00:40:00)**

If you give that tool a little bit of a README—“here’s an example request, here are some other API calls you can make”—it’s really good at extrapolating from patterns when the SDK and the API are well-formed and predictable. Then you give it an additional tool to search the docs and ask questions of the docs. Anything it’s not sure about or gets wrong on the first try, you give it the documentation.

What this does for the scenario we were talking about earlier is you have very limited impact on the context window up front—we’re talking about 1,000 tokens or something like that. And the context impact of doing a whole bunch of paginated list requests? Zero. The model will go look for somebody named Dan and double-check that the purchase was stripey socks. You might write three nested for loops, but then only at the end when it found the right thing it’ll console.log “found Dan, customer ID, blah blah, transaction ID, blah blah.” Then create refund—refund ID one, two, three.

The context hit coming back from all of this is going to be like 10 lines of text. It’s really minimal. And all of this will run really quickly too, so you don’t have a round trip to the model every time you’re doing something like this. It’s just CPU code, and it runs in a server in the cloud right next to the Stripe API somewhere in AWS. It goes super fast.

**Dan Shipper**

What I’m understanding you to say is that the language model has a tool where it can write code and send that code to whatever API provider—Stripe, whoever’s MCP server you’re using—they’ll go and execute that code, that code is going to interact with their API, and then return the results. Rather than having 50 different possible tool calls and all that stuff, it’s just: model writes API code, API provider executes that code, runs it on their API, and returns the results.

Why wouldn’t my model just write the code that I then run myself instead of relying on an API provider to do it?

**Alex Rattray**

I expect that will happen a lot more. I expect the code execution tool is going to become the most widely used tool. The problem is that today the code execution tool doesn’t work so well with libraries. LLMs have a hard time knowing exactly what version of a library they’re using, using the right version—probably usually the latest version—and not hallucinating aspects of the API, and knowing how to iterate if they hallucinate wrong.

And if it can’t use any library off NPM or the Python Package Index really, really well, basically perfectly out of the box, then forget about using a library. At that point you just have to hit the raw HTTP API. And in order to figure out what’s in there, you need the whole OpenAPI spec, and you’re back at square one because that document is massive.

Furthermore, something that’s really scary about that is if you don’t have a typed library with static typing where the computer can say what you’re trying to do is wrong, then the LLM will try to make an API request that is wrong some percentage of the time. The code execution tool can run a type checker and say, “You’re asking about stripe.transactions.list, but that actually doesn’t exist. Stripe doesn’t have a transactions API. You might want payment intents, you might want orders, you might want balance transactions. Which one do you want?”

And if the API provider is doing a great job building this tool, it’ll return the documentation for all of these things inline. It might have its own AI look at what the model’s trying to do and come up with a suggestion. That sub-agent is well-trained, well-specified, always updating, and isn’t burdened with the context of the full conversation.

**Dan Shipper**

What do you think of the security model?

**Alex Rattray**

The security model is really, really interesting. This is another area where we’re really starting to think about things at Stainless, and I’m getting really excited about it—so if any listeners are really interested in this and have some ideas or want to talk, please do reach out.

At the end of the day, I think security has to take place at the API layer itself. Right now you see people trying to implement security by limiting what’s exposed through MCP, and that kind of makes sense—but at the end of the day, you could do anything that’s in the API under the hood.

What people should be doing is using OAuth with granular permissions, with proper scopes. At that point, the security happens in the right place, which is at the API layer. There are limitations to OAuth scopes and it’s pretty hard to build. It’d be nice if someone made that easy, but in my view, that direction is the right layer.

**Dan Shipper**

Going back to my earlier question—I’m thinking about the idea of having a model write code that the API provider then executes to interact with their API and returns the results. Would you ever consider just creating a code execution environment that developers use themselves? Because, for example, I’m thinking about Quora. It has all these tools. Maybe Gmail is going to build a code execution thing, but really I’d want something like what you’re talking about inside of Quora. What I’d need is a computer use tool where I control the environment, I can install different libraries in it, and it can call any API—it just needs to have network access basically.

You guys should build that.

**Alex Rattray**

We’re working on it.

**Dan Shipper**

Fuck yeah. You’re building it for developers who want to access MCP servers, or for people who are providing MCP servers?

**Alex Rattray**

We’re starting with people who are providing MCP servers, but ultimately I think we’re going to need this to work such that you can give the model a code execution environment where it can hit not only the Stripe integration but also the Salesforce integration and also anything else. But not too much anything else. One of the advantages of starting where we’re starting—just one API provider—is that you ensure there are no network connections allowed out of that sandbox where we’re running the code to anything other than, in this case, api.stripe.com. That’s really critical for security for something like this.

There are ways to expand that bit by bit and keep things secure. It’ll take some time.

The other thing to point out as you see some of these generalizations is it’s not just that you want this code execution sandbox to work really well for any API, for any library—which I think we really need. You also start to see that this is just a powerful model for AI doing stuff. Sometimes you realize that the thing the AI did this one time in this one-off case is actually enduringly useful. Maybe any time a customer writes into support and says, “My socks had holes in them,” they should automatically get a refund. Maybe you want that, maybe you don’t—but there’s a lot of stuff that people do once, then twice, then three times, and then they say, “Okay, we should automate this.” That’s what software teams do all day, every day.

**(00:50:00)**

I think we’re also going to be seeing that with AI—where the same code search tool we’re talking about, all the same prompting that will make an AI really, really good at interacting with an API in one of these code sandboxes, almost quote unquote “in its brain,” where it can write code in its head, run the code in its head, see the results, and then move forward with your task—it should be able to say, “Actually, this is enduringly useful code. Let me commit this to the repo.”

**Dan Shipper**

Yeah, yeah. Chat is a really good interface for exploring, but sometimes you just want a dashboard. I just want to log into my Stripe dashboard and see all the stuff without having to be like, “What is my MRR?” It should just show up because I do that every day.

But I want to push you as a hashtag value-add investor. I think there’s a thing that happens in AI where often the first attempt at something like this, people try to be really cautious—and I’m sure your enterprise customers care about that—but the things that get adopted are often the ones willing to take the risk to be YOLO very early.

An example is DALL-E was totally private for a long time, and people were posting some images but you couldn’t get in. Then Stable Diffusion was just like, “Forget it, anyone can use this.” And that really started the whole image generation wave. Obviously Stable Diffusion fumbled the bag, but they had a lead for a while.

Same thing for Claude Code. If you look at the difference between Codex CLI and Claude Code—Claude Code was just YOLO mode. It’s super industrious. It has a sandbox, but you can just do --dangerously-skip-permissions. Codex fell way behind because first it was in the browser, so the whole thing was locked down. Then it was in the CLI, but it was really built for pair programming, so it wasn’t particularly industrious. It wouldn’t go off and do a bunch of stuff. It would get locked out of doing certain things even in full auto mode.

And now they’ve caught up because you can just let it do whatever you want. So I would really push you: there might be a version you could do like today or tomorrow or very soon for individual developers that would let them set up this environment that, for example, I would use immediately. I care about security, but I care a lot less than some gigantic enterprise company. And I think the people like me who are building at this scale are eventually hopefully going to be the big companies, but we’re the ones really doing the AI-first adoption, not the big companies.

I would love to get this in your hands. What are some of the APIs your team uses the most?

**Dan Shipper**

Thinking about all our different products, I’m thinking right now about Cora, the email assistant. It has all the big APIs it’s using—mostly the Gmail API. You’re interacting with the assistant over chat, and it has a list of tools: archive email, draft email, send email, and so on. It categorizes your mail in certain ways.

I think we’d definitely try out something like this because if it ran the same way, it would make it much more flexible for us to make more tools and not break old ones. It’s really interesting.

**Alex Rattray**

In a sense, what I actually predict is that people who are quote unquote “building tools”—once we have a code execution super-tool like I’m talking about—is that the only way you really “build a tool” is with instructions, with prompts. The full power of everything you could possibly do in the Gmail API, for example—it’s all there in one tool. But sometimes you have specific tasks or specific categories of work you want to describe in a particular way, to help the LLM perform a sequence of actions as productively as possible. At that point, the only engineering work you have to do is prompt engineering.

We’ll see if it’s that “easy.” As we all know, prompt engineering can be really tricky. But I think that’s part of the vision.

That being said, we do have some pretty nifty ways with the MCP servers we generate today to help developers mix and match all the parts of the different tools underlying all the different parts of the API as they compose and write their own tools.

**Dan Shipper**

This is awesome. For people who are listening and want to know more from you or more from Stainless, where should they find you?

**Alex Rattray**

Stainless.com is our website. At least visit stainless.com.

**Dan Shipper**

Alex, great to have you on. I can’t wait to do more of this when you have some of these new things launched. This is really, really fun—great to chat.

**Alex Rattray**

Thanks, Dan. You too.

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
