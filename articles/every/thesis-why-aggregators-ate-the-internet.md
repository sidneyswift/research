---
title: "Why Aggregators Ate the Internet"
author: "Alex Komoroske"
date: 2025-07-14
url: https://every.to/thesis/why-aggregators-ate-the-internet
words: 1626
---

*In the most recent episode of *AI & I

*, former Stripe and Google executive*


*Alex Koromoske**referenced the “same-origin paradigm”—a security decision made by Netscape engineers in the 1990s that has inadvertently shaped our digital landscape. In today’s*

__Thesis__, Alex explains how this choice created the conditions for big tech monopolies by forcing our data into silos, making it nearly impossible to move information between apps without friction. The good news: AI has reached an inflection point such that new technologies could finally break this cycle. Imagine a personal research assistant that understands your note-taking system, a financial tracker customized to your budgeting approach, or a task manager that adapts to your changing work style—read on to learn more.—__Kate Lee__*Was this newsletter forwarded to you? Sign up to get it in your inbox.*

There's a bug in the operating system of the internet. It's why your photos are trapped in Apple’s ecosystem, you can’t easily move your data between apps, and every new app starts from scratch, knowing nothing about you. Most importantly, it's why the AI revolution—for all its promise—risks making big tech companies even bigger instead of putting powerful tools in your hands.

The bug is called the __same origin paradigm__. It's a historical accident—a quick fix the Netscape browser team implemented one night in the 1990s that somehow became the invisible physics of modern software. Once you understand how it works, you can't unsee it. You start to notice how every frustration with modern technology traces back to this one architectural choice.

I've spent more than a decade as a product manager and strategist at companies like Stripe and Google. I've seen waves of technology promise to change everything—mobile, social, cloud. But there's a pattern: Each wave makes the biggest companies bigger. Every "revolution" reinforces the existing structures instead of empowering us to create new ones. And it all goes back to the same origin paradigm.

Now it's AI's turn.

The good news? For the first time in decades, we might be able to fix it. The tools to transcend the same origin paradigm are already here.

But first, we need to understand what we're dealing with.

**The hidden physics of software**

Here's how the same origin paradigm works: Every website, every app, is its own universe. The browser treats amazon.com and google.com as completely separate worlds that can never intersect. It’s the same with the Instagram app and the Uber app on your phone. The isolation is absolute—your data in one origin might as well be on Mars as far as other origins are concerned.

This creates what I call the iron triangle of modern software. It's a constraint that binds the hands of system designers—the architects of operating systems and browsers we all depend on. These designers face an impossible choice. They can build systems that support:

- Sensitive data (your emails, photos, documents)
- Network access (ability to communicate with servers)
- Untrusted code (software from developers you don't know)

But they can only enable two at once—never all three. If untrusted code can both access your sensitive data *and* communicate over the network, it could steal everything and send it anywhere.

So system designers picked safety through isolation. Each app becomes a fortress—secure but solitary. Want to use a cool new photo organization tool? The browser or operating system forces a stark choice: Either trust it completely with your data (sacrificing the "untrusted" part), or keep your data out of it entirely (sacrificing functionality).

Even when you grant an app or website permission only to look at your photos, you're not really saying, "You can use my photos for this specific purpose." You're saying, "I trust whoever controls this *origin*, now and forever, to do anything they want with my photos, including sending them anywhere." It's an all-or-nothing proposition.

**The aggregation ratchet**

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

I don't understand how your thesis that Same Origin is responsible for data silos can really be justified. APIs exist, they can have any rules the developers want them to, the auth can work in whatever way is desired/can be developed. People already trust many big companies with their data, with little or no assurance of genuine privacy or confidentiality of data. People tell secrets to AI every day without considering who has access to it and what they might do with it. People take nude pics all the time, put it up on the cloud, and get hacked. These problems aren't solved by Confidential Compute. And as far as permissions and sharing, some people like myself have photos in both Amazon and Google Clouds, our use of them is based on trust of those orgs, the lack of their ability to communicate with one another is *not* a trust issue. Google and Amazon simply have no incentive to provide data interchange in that context. The reason trusting Google with everything works is that they provide services that cover a wide range of common use cases, and they (generally) handle the integration between them internally. Again none of this has to do with Same Origin.

So the reason better data exchange systems haven't been developed before now is not, in my view, a technical one but simply an incentive one in the capitalist market. Companies could have put resources into creating open systems with good permissions models but they have no financial incentive to do so. They still don't, at least not significant ones. Maybe that will change with AI, but I don't see the case being laid out that clearly above.

Federated systems with granular permissions systems already exist, they prove that tech is not the underlying issue. No need for a fancy Confidential Compute implementation, which anyway relies on trust, i.e. I can send my data to a novel 3rd party for some unique service not provided by the larger trusted data silo I use, but I have to have reason to trust that 3rd party, and data security in processing is a small part of that concern at a practical level. As I noted above confidentiality of data at runtime is generally not a concern for the mass market, as evidenced by people's use of social media, and now AI tools. Blockchain implementations likewise exist to solve similar trust issues. Confidential Compute is a red herring for this problem domain, though it obviously solves some important issues for business customers, and others that could actually be important for the AI age as we as consumers have more and more incentive to share ever more sensitive information with AI companies. But again that's a separate issue from Same Origin *and* from data interchange. At least as far as I can see.

Have I misunderstood the entire argument here?

The problem is that with other parties (e.g. doctors, insurance companies, tech companies, the government) having my personal information is that once they have it they have it forever. I can't unshare it.

Is this some sort of Inspector Gadget type of encryption where I can send a piece of data (or some sort of blockchain address to avoid having to maintain the files myself) and only grant the recipient access to the data for a certain period of time? When the period ends then the data is no longer decrypted and they cannot access it. Enabled by Confidential Compute? If so, cool!

My understanding is that once something is decrypted the cat is out of the bag and it can't be put back in. If something like this was possible it would do more for user privacy than any number of well-intentioned laws.

🚧 The Bug Beneath the Browser

Reading Alex Komoroske’s sharp post on the same-origin paradigm had me nodding—until the pivot to AMD’s secure enclaves. A solid feature, sure. But a narrow fix to a systemic problem.

The flaw isn’t in the chip. It’s in the model.

What’s broken is how we authorize, move, and trust data online.

Here’s why hardware-bound solutions won’t solve the deeper architecture problem:

🌱 Too Local: CPU fixes assume data lives in one secure zone. But like people, data needs to move, combine, and adapt.

🌾 Weeds in the Garden: Healthy systems allow messy overlap. Ecosystem diversity—not lockdown—is what drives innovation.

🌊 The River Always Wins: A rock can block flow. But real resilience comes from trees, soil, and balance. Nature distributes control—and software should too.

Komoroske nails the true villain: the same-origin paradigm. It traps your data in silos, makes permission binary, and rewards companies that aggregate context at scale. The result? Big gets bigger.

🧩 What we need isn’t tighter perimeters—it’s a system where trust, access, and privacy aren’t locked in a zero-sum game.

That’s why I’m following researchers like Geoffrey Litt, who’s pushing decomposable documents and malleable software. Instead of rigid apps, we get fluid tools that operate on user-owned, user-governed data. You bring the tool to the context, not the other way around.

🔑 The future of AI isn’t in the model or the chip. It’s in the architecture of agency.

@backofthenapkin this seems very AI generated

@danshipper What magic decoder ring are you using? I write with a partner to sharpen for clarity and brevity. Feels like common sense, not a conspiracy. Like your business, clarity is currency. I don’t mind splitting the check with AI.
