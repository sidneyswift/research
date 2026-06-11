---
title: "Regulate Who? The Weird Legal World of DeFi - DeFriday #11"
author: "Nat Eliason"
date: 2021-07-29
url: https://every.to/almanack/regulate-defi
words: 1514
---

# Regulate Who? The Weird Legal World of DeFi - DeFriday #11

Did this Unicorn take your money?

July 29, 2021 Updated May 15, 2026

Who do you regulate when no one runs the bank?

Last week Uniswap, one of the most popular decentralized exchanges on Ethereum, mysteriously decided to remove access to 100+ tokens on the main user interface to their exchange.

Some of the removed tokens were ones with bugs in their code, but most of them were tokens that might bring Uniswap under some legal risk. Specifically: tokens representing TradFi derivatives like options, stocks, commodities, and foreign currencies.

Uniswap didn’t say they received a letter from the SEC, but the community suspicion is that they were either contacted by someone and suggested to remove these kinds of tokens, or they were staying in the loop with discussions going on in Washington around crypto regulations and decided it was prudent to preemptively delist this class of tokens. Either way, it’s one of the first times the US Government has influenced decision making of a major DeFi company.

The community didn’t love it, and there were plenty of memes and jokes about “new boss same as the old boss,” but the token de-listings also didn’t particularly matter. Within a few hours, community members had launched new versions of Uniswap’s website, reinstating access to the banned tokens.

If you still want to buy some Synthetic Tesla Shares, all you need to do is go to https://uniswap.eth.link/ or https://uniswap.ninja/ or any of the other mirror sites launched by the community and you can trade them just fine.

This is where we start to see the “decentralized” part of DeFi really come into play, and how odd of a challenge regulators are going to have. If the SEC wants the NYSE to remove a company from their exchange, it’s not like 17-year-old Kyle in Minneapolis can re-launch the NYSE in-between Biology and soccer practice. But he can re-launch Uniswap.

## The Two Layers to DeFi

The reason the community can relaunch their own Uniswap free from the new restrictions is that there are really two “Uniswaps.”

One is the Uniswap you see when you go to Uniswap.org. It’s the website and user interface maintained by Uniswap Labs.

The second is the Uniswap Protocol, code on Ethereum that operates the decentralized exchange completely autonomously.

Uniswap Labs contributes to the Uniswap Protocol, but it doesn’t own it or have any special control over it. Since the protocol lives on the Ethereum network, it runs completely on its own thanks to the computing power of all the devices maintaining the network.

The Uniswap Labs site at Uniswap.org communicates with the Uniswap Protocol, much like the Every.to site you’re reading this on communicates with the Every database and backend code. But the big difference between the crypto Web3 world and the Web2 world you’re reading this site on is that *anyone* can communicate with the Uniswap backend. You don’t need any special access.

Using the Uniswap website is the easiest way to interact with the Protocol, but you can also do it directly. If you’re a coder, you can build your own version of their site without their permission. You can even go to the Uniswap Protocol contract page on Etherscan and interact with the protocol directly, without having to go through a website.

We have an analog of this in Web2 with public APIs. Many Web2 products have APIs that developers from outside their company can use to interact with parts of the backend to popular sites. Ethereum just takes this to the next level by saying *everything* is accessible via API, and there’s no permission needed. Once a new protocol is deployed to the network, everyone has access to it, no matter who wrote it.

This is why the community was able to rebuild an uncensored Uniswap so quickly. The Uniswap Protocol can be accessed by everyone, so as long as you know a bit of Javascript, you can easily write your own functions to interact with it. Combine that with copy and pasting the front-end design of Uniswap, and bam, you just relaunched a stock exchange.

If the SEC or any other governing body wanted to ban synthetic stock tokens from the Uniswap Protocol… they can’t. The protocol is unchangeable code deployed on the Ethereum network which is run by hundreds of thousands of computers spread all around the world.

If someone wanted the Uniswap protocol changed, they’d have to shut down Ethereum itself. Or get the majority of Ethereum operators to agree on a new version of Ethereum where Uniswap doesn’t exist. Considering Ethereum is a global network that the US is only a part of, there’d be no way to even begin to enforce that.

Once the code is out there, it’s out there, and while the Uniswap Labs company in NYC can be forced to take synthetic stocks or other assets off their interface with the Uniswap Protocol, no one can stop the protocol from continuing to list those assets.

So how do regulators even respond to this?

## How Regulators Might Respond

If the regulatory goal is something along the lines of “prevent Americans from trading or selling tokenized stocks,” it’s going to be exceptionally difficult to enforce.

Since Ethereum is global, even if American companies don’t create these synthetic stocks, someone in Hong Kong or South Africa certainly will. And while the US could create Great Firewall style Internet censorship to try to block access to those sites, it wouldn’t be able to do anything about the Ethereum network transactions unless it blocked access to Ethereum entirely. And given how quick it would be to spin up alternative websites to access these protocols, there’s no way the firewall could keep up fast enough. It would also be an odd new change in policy, considering other sites that explicitly enable illegal activity like The Pirate Bay aren’t blocked by the US.

So if they can’t block access to these protocols, what are some other options?

One would be to punish developers or teams who deploy protocols that enable trading anything that breaks securities law. They could make this retroactive and go after the Uniswap developers and everyone else, but that certainly wouldn’t be a very popular move.

And at the end of the day it wouldn’t do much of anything. Contracts can be deployed by anyone from any address, and there’s no personal information that gets encoded with it. Developers would just use anonymous addresses to deploy any contracts they’re worried might be risky in the future, and everything would continue as it has been.

Another option would be to punish individuals who interact with any of these tokens. But that would be fairly simple to get around using anonymizing services like Tornado Cash.

Then a response to that would be to punish anyone who interacts with anonymizing protocols like Tornado Cash, but since anyone can send anyone a Tornado Cash transaction, someone could just send money to everyone at the SEC from Tornado Cash and suddenly those regulators are in trouble since they can’t prove they didn’t send it to themselves.

## What's the Solution?

You see the problem. For every regulatory move against certain tokens or DeFi protocols, there’s a countermove that makes the effort pointless. It’s not even necessarily worth trying to comply with some of these regulations, since they’ll end up being unenforceable.

But there also need to be *some* reasonable guidelines to give US-based crypto developers guidelines for what’s okay and what isn’t. If everyone is afraid that something they’re building now could get them arrested in five years, all the talent will go elsewhere. If the US wants to be a leader in the next generation of the Internet, it has to figure out these guidelines sooner rather than later.

It may be that building a new financial layer will also require a completely new form of regulation for that financial layer. Just like applying existing paradigms to new technology often results in suboptimal products, applying existing legal paradigms to new technology could result in ineffective regulation that does more harm than good.

While I was working on this piece, Don Beyer introduced legislation in the House focused on regulating cryptocurrencies. Though many members of the crypto community don’t love any kind of regulation, it’s coming, and this is actually a pretty promising first step. Figuring out how we can create reasonable safeguards for retail people entering crypto, and providing a sense of security for developers building in the space, is necessary for DeFi to reach its full potential.

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
