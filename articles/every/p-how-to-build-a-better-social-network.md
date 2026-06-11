---
title: "How to Build a Better Social Network"
author: "Nir Zicherman"
date: 2023-11-26
url: https://every.to/p/how-to-build-a-better-social-network
words: 3979
---

*The problem with most writing about technology is that it points out problems without proposing solutions. One of the easiest things to bellyache about is how social media works: it prioritizes shallow engagement bait by creators who already have large followings. In social media, the rich get richer, and the audience gets more stupid. *

*I recently came across an article about the problem of social media that points out this problem and attempts to solve it. It’s by Nir Zicherman, the co-founder of podcasting company Anchor and the former VP and Global Head of Audiobooks at Spotify. He proposes a solution: create a market economy where users spend points in order to govern which posts get seen, and rapidly redistribute those points such that no one can accumulate an ongoing advantage. In this world, he hopes, the best content gets promoted—rather than just content from large accounts or shallow engagement bait.*

*Read the article and then see my commentary at the end.* *—**Dan*

I believe it’s possible to build an ideal social network that has all the benefits of social media while addressing the fundamental issues with today’s platforms.

Here’s how it works: every new user is given 1,000 points when they join. When they see content they like, they allocate some or all of their points to the post’s creator. The more points a creator has at any given time, the more distribution their content gets.

But the points decay over time in a predictable and transparent way. Gradually, points get reallocated across the user base. The more points you have, the faster you lose them. If you have less than 1,000, you’re incrementally brought back up. The network perpetually tries to return itself to equilibrium, and it’s the innovation of the community and proliferation of high-quality content that prevents that from happening.

For the purposes of this article, I’ll refer to the network as DK (a phonic play on “decay”). And for the record, as the former vice president of audiobooks at Spotify and cofounder of Anchor, I’m not interested in building DK myself, but if you are, reach out and let’s chat.

## The social networks of today

We often hear about what’s wrong with today’s social networks: they’re echo chambers, the comments are toxic, clickbait proliferates, and the algorithms support extremism. Social media skews elections, spreads false information, and leads to mental health problems. The list goes on.

And yet, the core concept—technology that brings us together by enabling seamless content distribution across the world—continues to attract people.

Why, then, do our existing social media networks have so many flaws? Because social networks are economies. Self-serving agents interact in a public market, exchanging ideas and content instead of goods and services. They offer wealth in the form of distribution. They have winners and losers.

But economies work when they are governed by supply and demand. Whatever is wanted spreads; whatever is low quality is weeded out. The invisible hand of the market functions when there are efficient correction mechanisms that reallocate money as needed.

The social networks of today don’t have those correction mechanisms. There is no “free market” social network that exists at scale. Instead, we have one of two models. Most social networks lean heavily in one direction, but are in fact hybrids of the two.

### The follower model

The traditional follower model—popularized by Facebook, Instagram, and Twitter/X—allows people to grow their distribution channels and retain them for future distribution. We’re all familiar with these. They come with five problems:

-
**Follower-based distribution:**It is easier for people with large followings to distribute new content. -
**Accumulated advantage:**It is easier for people with large followings to get bigger. For example, an account can more easily go from 20,000 to 50,000 than from 10,000 to 30,000. -
**Diminishing returns:**As the network grows, feeds become crowded by incumbents, making it harder for new creators to succeed. -
**Echo chambers:**Social connections are disproportionately made between people who think, look, and sound alike. -
**Decreasing quality:**Followers are easier to retain than grow. As a creator with a large following grows bigger, they have little incentive to invest in content quality. New posts do not need to work as hard as early ones to derive the same benefit for the creator.

Over time, these social networks feel stale, tend toward extremism, and discourage content innovation. This is akin to an oligarchy. Some creators come in early, win big, and hoard their channels of distribution.

Real economies have correction mechanisms. Two examples are depreciation and inflation, economic phenomena that incentivize innovation and capital investments. If a company does not continually strive for improvement, growth, and efficiency, its assets would depreciate and its prices would inflate. It would be driven out of business in the long term.

An ideal social network will need to have similar counter-forces, so that content creators are incentivized to regularly improve and meet the needs of their audience.

#### The algorithmic model

The other type of social network, popularized by TikTok, follows the algorithmic model. Content spreads based on user signals around engagement. This algorithm is the primary decider of the type of content that succeeds.

Algorithmic models fail to be efficient markets for two reasons. First, they prioritize engagement over quality, which creates a self-fulfilling flywheel. Creators are incentivized to create content the algorithm prefers, which only strengthens the algorithm with more engagement-maximizing content.

The second reason these models fail to be efficient is because the black box distribution algorithm is akin to an economic command economy, where the government controls market dynamics. There is little transparency and community control over the dominant algorithm, a structure that—according to most economists, at least—always results in long-term inefficiency.

Both network models have structures that create problematic incentives for users. And neither model has sufficient correction mechanisms to ensure that the harmful aspects of social media don’t propagate. Which leads me to…

#### Introducing a new social network: DK

DK is my concept of the “ideal” social network. Users will flock to this platform because of high-quality content. DK can be iterated on in a number of ways. I’ll keep it simple for the purposes of this article.

*A bad mockup of DK. Notice the feed is sorted by each creator’s current points.*

**Points: **When a user joins a platform, they are given 1,000 points. Points are a store of distribution value. The more points you have, the higher you rank in the feed.

**The feed: **The feed is global. It shows a stack ranked list of posts based on how many points each creator has. Creators who have created high-quality content are given points by others, ranking them higher in the feed and making their new content more likely to be seen. This is similar to the traditional follower model, except that there is an equalizing force, described below.

**Posts: **Users can post content as often as they’d like. But only their most recent post shows up in the feed at any given time.

**Equalizing force:** Every 10 minutes, the system slightly reallocates points. Think of it as a tax on users with high points that get reallocated to users with fewer points. The algorithm’s goal is to eventually return users to their starting condition—an equilibrium state of 1,000 points each. This is similar to the “correction mechanism” that markets have.

Here’s what the math of the equalizing force looks like:

Every 10 minutes, an adjustment happens to all users’ points. This adjustment depends on the number of points a user has. This formula brings a user’s points back to equilibrium (1,000) at a rate of half every six hours. Think of it as a six-hour half-life. If the user is below 1,000, the process gives them some points, and it takes those from the users who are above 1,000.

(This function is asymptotic, meaning it approaches the equilibrium of 1,000 but never quite gets there. For simplicity, let’s assume that when a user is within 10 points of 1,000, they just return to 1,000.)

For example, a user starts with 1,000 points, posts decent content, and is given points by others. They now have 1,200 points.

- In 10 minutes, they’ll have 1,196 points (four points taken away and given to other users on the platform).
- After 1 hour, they’ll have 1,178.
- After 6 hours, they’ll have 1,100 (half of the difference from 1,000 they started at).
- After 24 hours, they’ll have 1,012.
- At 26 hours, they’ll be back to 1,000 (because that’s when the delta to equilibrium is less than 10).

Let’s look at an example where a user has 500 points (below 1,000, because they’ve given out points to content they like):

- At 6 hours, they’ll be at 750.
- At 12 hours, they’ll be at 875.
- At 34 hours, they’ll be back to 1,000.

Here are four users trending back toward equilibrium over a 24-hour period:

And here’s a slightly more complicated version of this, where Users 2, 3, and 4 all give User 1 their points throughout the course of a day.

Every time User 1 jumps up in points, it happens at the expense of another user who has given away their points—and despite accumulating points, User 1 always trends toward 1,000 over time. Despite User 1 continually accumulating points, they trend toward 1,000 over time. The more points they’re given, the faster that trend occurs. The total number of points on the platform is always 1,000 multiplied by the number of users.

## Addressing today’s social media problems

This new model would not be interesting if it didn’t address the issues with today’s social platforms. Here’s why DK addresses them:

-
**Follower-based distribution:**Unlike the traditional follower model, distribution is based on the short-term perception of the quality of a user’s content. -
**Accumulated advantage:**No one is able to sustain their distribution benefit for long without continuing to create high-quality content. -
**Diminishing returns:**Feeds are ranked by the quality of the content within them, rather than by engagement likelihood or past accumulation of followers. If errors or inefficiencies are made in DK’s economy, they quickly correct themselves as the platform returns to equilibrium. -
**Echo chambers:**Because of the finite number of points in the system, people can only give a*finite*advantage to those they agree with. In other words, there is no way for a particular group/party/ideology/perspective to gain global advantage over any other. -
**Black-box algorithms:**Unlike today’s algorithmic platforms, DK’s logic for distribution is transparent. There is no way to game the system long term, nor can creators gain a long-term advantage without consistently creating high quality content.

## DK is just the start

There are many things one can do to enrich the DK experience—here are just two:

- Encourage users to give out their points so that users with substantial distribution boost smaller creators.
- Allow users to “follow” creators and be notified of new posts. The following mechanism will be left out of global distribution or feed ranking.

The flaws with social media today are symptoms of decisions made in their implementations. If we return to the core question of why we’re building—and if we do it in a way that is inspired by actual economies and markets—we can build something better, more positive, and more meaningful than what we have today.

*I love solutions like this, and it’s worth pondering whether you think it might work. There is something useful about an enhanced decay function for any creator’s distribution, and a shift from engagement to points as a way of disincentivizing shallowness and hype. But I have a few concerns:*

*I’d guess that engagement and point-giving are going to be highly correlated. In other words, a user is likely to give points to any content they engage with. There might be some edge cases, especially if point-giving is public, where, for example, I might not distribute my points to gossipy content—but I might spend a lot of time looking at it. But there are many real-world instances where people spend inordinate amounts of actual money on shallow things instead of “quality.” I think that dynamic will persist in this system.**Accumulated advantages exist because of the way our brains work, and a decay function doesn’t solve for this. We have a limited amount of attention and can only fit a few creators at a time into our brains. We are also social creatures who look to others to help us filter for what we consume. These combined forces create accumulating advantages over time to a small set of creators. I don’t think a strong decay function solves this problem—in fact, it might incentivize people to race even faster to produce shallow content before their distribution runs out. It’s similar to the dynamic among news organizations to cover breaking stories as quickly as possible before the information’s value decays.*

*I love this article because it got me thinking. My two cents is that the best way to solve this problem is to try to put high-quality content out into the world—in other words, be the change you want to see. That’s what Nir is doing with this article, and what we do at Every.*

*For more on this topic from Every, read Nathan Baschez’s classic, **“Why Content Is King.”* *—**Dan*

*Nir Zicherman is a writer and entrepreneur. He was the co-founder of Anchor and, until recently, the vice president of audiobooks at Spotify. He also writes the free weekly newsletter*

*Z-Axis*

*, in which this article was*

*originally published*

*.*

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

Uh oh. I wrote a comment and then the Every log in again message popped up. You might want to fix that to HOLD the comment instead of losing it. Maybe you can fix it to recognize the subscriber needs to log in again before accepting any keystrokes in comments? Glad to see Dan and Nir teamwork on this piece.

@[email protected] oh no!! we will add something to our backlog. sorry about that. thanks for reading and commenting!

"Proposing solutions" Nice JOB Every.

@goldsdk w00t!!

Every week, in the NFL, the poorest team and the least effective team has to perform live against other teams. That performance may be recorded, but on game day the only thing that matters is taht day's performance. Two or three days later that performance is obviously over but also in most respects "gone". The attention to last week's performance, whether it was good or bad, is dissipated. But at the end of the season, the NFL draft explicitly conducts an enormous correction in the probable distribution of future opportunity to perform and recapture attention. The worst teams get the best future-facing choices for renewal and improvement. What's different about this is that it is disconnected from Social Preference. The League and the Media are a networked platform and people who are consumer/users literally invest time and money into being participants for hyper-personalized benefit yet still become "cheeseheads" or join Raider Nation.

The problem with Social Networks is not that they are darwinian, it's that the networking part does not shy away from the social part. The difference between a "social" network, a "news" network, a "knowledge" network, and so on, is a profound difference. No "social" network should be forced to satisfy the requirements of a different kind of network. What is "quality" in social terms? Mainly, the problem to solve is to not conflate different kinds of networks. Not to get argumentative, but DK is not a model of a social network. It's a different kind of network.

@malcolmryder this is an interesting point. is your idea that, essentially, social networks should map social preferences—which don't follow the simple Darwinian performance measurements as NFL teams? therefore, DK would work simply as a media site like Digg but not as a traditional social network?

@danshipper Hi there. In my NFL analogy, Raider Nation is the social network; the league is not a social network, and the game audience isn't either.. But I want to be careful and not arbitrary in saying that. I'm not so much concluding as I am hunting.

A la DK, since a poster watches the audience gradually file out of the arena a while after the posting, the poster has no recourse but to prep and come back and perform again if they want the audience to come back. But even with poor attendance and/or shoddy performance, an NFL team has a baseline support system called "League" -- the league makes sure they come back to perform again, and it maintains the opportunity to improve as well. In effect, there's a subsidy in place for league members.

In comparison, where does the subsidy come from that puts a sustained floor under members of a social network? Mostly, it's in marketing one member to another. Social is way different from "free to the public". Yes, I do think that the conceptual distinction of a social network is that it "maps TO" social preferences, without externally judging those preferences.

But I think social networks were just allowed to become containers of any kind of attractor individual persons wanted them to contain, and there's no incentive to have another "equal opportunity" mechanism for the individuals who show up with an attraction.

I've always wondered if charging a dollar a day to use a "social network" would almost immediately verticalize that network into a special interest network, wherein suddenly the quality of the content supercedes the cheap thrill of getting and giving attention that is already "good enough" for a "general" social network. Looking at LinkedIn, what do we think the answer to that question is? The behavior shows enormous pressure to market popular and trendy ideas, and most of the rest of it mimics remote socializing -- i.e., turning a special interest network into a social network. I assume you already looked at this more closely than I; it's interesting to me that (in my view) DK's mechanism of artificially producing supply-side scarcity in an open source environment does not imply that the demand side will get more choosey... and I do get that the algorithms that turn suppliers into a power curve do a lot of what we're now wanting to call "hallucinating"...

@malcolmryder kind of agree... this is the old model with [poorly] tweaked tools. Everybody forgot what a free market looks like... A decentralized social platform with P2P ad space and minimal barriers to monetize and a star is born. I call it the social 'homestead act'...

That recalc done every 10 minutes for every account across the userbase - is that realistic at millions of users?

@ernieoporto almost certainly, yes. something similar has to happen for algorithmic feeds

Amazing posts. During 2020 I made a trademark for ppleport. This "idea" was similar to your description for a social media site where users on the network get points and give points from their passport. The more stamps on your passport the better. The global feed resets every 24hrs. You get more points if you go to different countries. I even pitched this to 1 small VCs. Never developed it though. Would like to work on this with ya!

Nir's approach seems to encourage _quantity_ rather than quality: Unless creators post every hour or so, they fall off the leader board and are never seen again. Just getting onto the leader board would involve an enormous release of content.

@jimhull agreed, that was my feeling on it as well. it's an interesting idea—but lots of potential unintended consequences

Still designed in the fragile control model... So much of modern business punishes. You create 'quality' or you will be punished in this manner... Points/rewards/earning should merely be a barrier free option.. Someone may just want to log in and see their grandkids in another state, at their local sporting events... Having a centralized 'point' system will maintain the fragility... In order to create an antifragile system, it needs to be a free market. Also, too much focus on the algo's instead of the king [content creators of any quality and scale; antifragile]

Not being a good academic, I couldn't write out the solution well so I built the prototype instead; i love being in the game anyway. If i demo it (because the new tooling needs to be understood) and you cannot poke holes in its ecosystem/functionality, will you write an article...?

I don’t see how DK won’t just reward popularity exactly like the existing SoMes? A scientist posting the cure for cancer will still get drowned out by Taylor Swift’s photo of her breakfast.

Also, what about bots? You could just buy points the same way you can buy followers.

My concern is that this assumes good faith actors -- this would most certainly be gamed with bots to keep some particular content artificially 'present' which would be self-reenforcing: people would see the 'boosted' content first and as other studies show, people tend to favour what's popular vs what's good. Additionally, those who can afford to buy a bot army will have a massive advantage as they are 'buying' the sustaining points from bots that will remain dormant (and would reduce the 'value' of a point). It's a super interesting concept but the bigger issue is: how do we get people to act in good faith? If you have that then even the most rudimentary system could produce quality results.

This is a very good idea. It’s entertaining, logical, appealing by its seemed justice, but it not gonna work :-)

Reddit Canvas is simple example of how fanboys will crack the algorithm — coordinate, create multiple accounts, find proper timing, arrange shifts, and boost their nonsense to the top.

I think it’s a very cool idea, but I’m not sure the points system is fundamentally different than distributing likes on Twitter (which Twitter slowly devalues over time as well)

im more interested in solutions that change the sharing mechanic itself so that posting ≠ broadcasting (eg https://plexus.earth)

My ever-growing cynicism suggests that the current stars of social media and a majority of users are uninterested in self-balancing systems, preferring the momentous advantage of incumbents and the feeling of domination that accrues to their various factions.

The ideal network described here is attractive to the minority of users who are actually interested in high quality content vs affirmation of their current mind-set or click-bait titalation.

While I and many readers here would be delighted with a network where attention must be continuously earned, the current social media denizens are unlikely to support it.

An alternative concept is to allocate a portion of the financial reward of posting to the value voter. So if the post had a value of $1 (say through ads) then the platform gets $0.25, the poster gets $0.50 and the $0.25 gets distributed to voters.

This distribution is based on the consensus value. So if I rate the post an 8/10 and then the average rating is 8/10 I get a bigger share of the $0.25. If I voted a 4/10 I'd get little to nothing based on how many people voted the post to be an 8/10.

There's more to it but that's the crux of identifying true value through small financial returns that are paired with reputational factors on a social network.

I'm working on a professional network for health and it is something we're going to trial
