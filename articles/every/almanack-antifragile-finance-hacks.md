---
title: "Antifragile Finance: How Hacks Make DeFi Stronger - DeFriday #9"
author: "Nat Eliason"
date: 2021-07-16
url: https://every.to/almanack/antifragile-finance-hacks
words: 1726
---

# Antifragile Finance: How Hacks Make DeFi Stronger - DeFriday #9

We're all in this together.

July 16, 2021 Updated May 15, 2026

This week, THORChain, a newer blockchain working to improve cross-chain transfers, was hacked for 14,000 ETH or $28,000,000.

To anyone outside of the crypto world, that probably sounds like a catastrophic failure that should scare people off of using THOR, or maybe off of crypto entirely. After all, when was the last time your bank was hacked for $28,000,000?

But to people in the crypto world, these hacks are perceived very differently. In a strange way, they usually end up being a good thing, because they uncover some underlying issue with the protocol that once fixed can make it stronger.

The etiquette around managing hacks and exploits is a crucially important, and impressive, part of crypto and DeFi culture. It blends extreme ownership, radical transparency, accountability, and remote collaboration into a completely different way of handling catastrophic failures than we’re used to seeing in the traditional financial or business worlds.

Let’s explore how exploits happen in crypto, and how they make the ecosystem stronger.

## DeFi Hacks vs. Web2 Hacks

You’ll occasionally hear stories in the traditional finance or business world of a company getting hacked. If Crypto and DeFi are “Web3,” these are “Web2” hacks.

Usually, the hacks involve someone getting access to the company’s database and getting a huge list of customer email addresses and passwords or credit cards.

In many cases, these hacks are done through elaborate phishing scams or social engineering. If you haven’t seen this DEFCON video of a hacker taking over the reporter’s cell phone account, it’s pretty incredible.

Because data and access to data is more centrally controlled in the Web2 world, individuals are often the point of failure. If you can hack the right individual inside of an organization, you can use them to get you access to data, control, or whatever else you need.

In the crypto world, things work a little differently. All transactions are public, so there’s really no value in trying to hack a customer list. It’s public anyway. And while having someone’s credit card info might let you spend their money, having someone’s public wallet address doesn’t let you do anything.

What’s worth going after though are the funds stored in the applications themselves. All of these DeFi protocols I’ve written about like Compound, Yearn, and Alchemix, have hundreds of millions or billions of dollars stored in their code.

If you can figure out how to exploit the logic of that code, you can drain some or all of those funds.

That’s why you’ll often hear these hacks referred to, more accurately, as exploits: the system wasn’t technically broken into, there was an underlying issue with it that someone figured out how to take advantage of.

Hacks definitely do happen, but in most of the big stories you hear about a smart contract or set of contracts was exploited through some vulnerability in the code.

These vulnerabilities usually come in a few forms:

### Sloppy Security

Sloppy security would include any mistake with managing your private keys that could result in someone getting access to your crypto accounts. This is a mistake that can happen to anyone. I made a mistake with my security once, and a hacker was able to steal $30,000 from me. Ouch.

But sometimes protocols make security mistakes too. EasyFi currently holds the #1 spot for top DeFi exploit, because a hacker was able to get access to a computer that had the admin keys to the entire protocol, and steal $59,000,000.

Thankfully, most crypto projects will advertise what type of security they have in place to prevent this from happening. One common tool is a multisig wallet that requires multiple people to sign off on transactions to protect treasury funds.

Mitigating against sloppy security is essential, but it's kind of like exercise. Everyone knows they should do it all the time, but that doesn't mean it actually happens as often as it should.

The more interesting exploits come from things like code mistakes.

### Code Mistakes

Code mistakes are what caused the THOR exploit. You can read more of the details on Rekt, but the short version is they were supposed to change part of their code and apparently forgot to do it before pushing to production.

Code mistakes are one of the reasons audits are so important in the DeFi world. There are companies like Certik or Haechi who will review the smart contract code behind platforms and publish any concerns they have or errors they catch.

Many platforms will include links to their audits on their homepage as a way of building trust and demonstrating they’ve done their best to make sure their code isn’t hackable. Unfortunately, an audit doesn’t always catch everything, and you can actually see which companies audited past exploited companies on the Rekt Leaderboard.

But even if your code doesn’t contain any obvious bugs, you could still be vulnerable to another common type of exploit called a “flash loan exploit.”

### Flash Loan Exploits

This is where the exploits start to get more interesting. Most flash loan exploits don’t take advantage of a mistake in the code, rather a vulnerability in the logic or tokenomics that can be attacked with a sufficiently large pool of funds.

A Flash Loan is a DeFi product where you borrow a large amount of funds, use them to execute a trade, and return those funds all in the same transaction. They’re often used to arbitrage price differences on various crypto exchanges.

Let’s say you were browsing Uniswap and Sushiswap, and you realized the stablecoin DAI was priced at $1.005 on Uni, but only $0.995 on Sushi.

You could write some code where you borrow $10,000,000 of ETH from AAVE, use that $10,000,000 to buy $10,050,251 DAI from Sushi, then sell it on Uniswap for $10,100,502, then return the $10,000,000 of ETH plus a 0.09% fee of $9,000.

In one transaction, you just made $91,502, and you never put your own capital at risk. Cool right?

What you just did in that case was flash loan arbitrage, and it’s generally considered an important part of the DeFi ecosystem since it helps keep prices the same across exchanges.

But flash loans can also get used to exploit protocols when a weakness is discovered.

In the Harvest Finance exploit, a $50,000,000 flash loan was used to manipulate the relative prices of two stable coins on Curve, in order to take advantage of the deposit and withdrawal math on Harvest, allowing the exploiter to make ~$500,000 each time they ran the cycle. They then did that 32 times over the course of 7 minutes, and made off with $24,000,000.

The crazy thing is they could have kept going and drained $400,000,000 for themselves. But they didn’t, for some reason.

These flash loan exploits are among the most common, and they often reveal unknown vulnerabilities in other projects as well.

This is where we start to see how exploits help the DeFi community grow.

## Learning from the Exploits

In the Web2 world, we often hear about hacks months after they happen, and with limited information on how they happened or how they’ll be prevented in the future.

In the crypto world, it’s impossible to hide any of these big exploits since everyone can see all the money moving around. As soon as a big exploit happens, people will know.

The community is also generally understanding when these things happen, so long as the communication about it is clear and there’s a plan to address the situation.

THOR gave a masterclass in this yesterday.

First, they acknowledged the hack and immediately made it clear they would donate funds from their treasury to everyone who was a victim of the exploit:

Then a few hours later, they figured out how the exploit happened and shared their quick notes:

A few hours after that, they found the bug and submitted a pull request for it, and that patch was merged a few hours later:

And though it’s coming a tad late, they shared the security audit that they’re working on to make sure something like this doesn’t happen again in the future.

So within 24 hours, THOR:

- Was exploited for ~$5m
- Acknowledged the exploit and paused chain activity
- Committed to paying everyone back for their losses
- Found the issue
- Patched the issue
- Deployed their new, more secure network

That is **incredible**.

While it obviously sucks to lose $5m the THOR treasury has over $244m in it so they’ll be fine. Plus they gained a more secure network, along with a ton of customer trust.

And because they’ve shared all of these details publicly, including all their code, this exploit is now in the growing library of “risks to look out for” when other people are writing smart contracts or auditing their own security. They’ve made the entire DeFi ecosystem more secure.

This is what I mean when I say it’s not always bad to see exploits like this happen. Whenever possible, the protocol that gets exploited repays anyone who suffers losses. And they end up creating a more secure product because of it.

By being able to learn from everyone else’s mistakes and see what’s gone wrong before, the whole ecosystem can develop extremely quickly compared to the traditional financial world where information might be more siloed.

And as strange as it might seem, sometimes a protocol having been exploited once already is a sign using it is *less* risky. It means hackers have already done their best to attack them, found the vulnerability, and now they’ve hopefully fixed it.

This is still the wild west. And while we can’t prevent hacks and exploits entirely, we can at least work together to decrease them over time.

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
