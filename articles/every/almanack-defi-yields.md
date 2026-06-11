---
title: "150% APR? How Are DeFi Yields So High? - DeFriday #6"
author: "Nat Eliason"
date: 2021-06-24
url: https://every.to/almanack/defi-yields
words: 2514
---

# 150% APR? How Are DeFi Yields So High? - DeFriday #6

Is this the real life? Is this just fantasy?

June 24, 2021 Updated January 20, 2026

When you first step into the DeFi world, you're presented with investing options that might break your brain. Sure, we all know about the “to the moon” stories where the value of a coin might unpredictably surge 10,000x and then go to zero days later—but that’s not the only source of yield in crypto.

For example, check out Yearn which I wrote about earlier. They're currently offering 3.3% APR on Tether, a stablecoin pegged to the US Dollar. How is that possible?

Savings accounts in the TradFi world pay 0.35% if you're lucky. So how is the APR on everything in DeFi around 3 - 7% minimum, and often into the tens, hundreds, or thousands of percent?

It's easy to see those rates and say "that's a scam" or "that's too good to be true," and you'd be right sometimes. But some of this yield can be explained without using the word ponzi. And in this piece, I'm going to try to explain where it's coming from, and what yields are robust, vs what yields are closer to unstable ponzi schemes.

Let's dive in!

## The Foundations of Yield in DeFi

Not all yield is created equal. Some are extremely robust, some are an outright fabrication.

There are four types of yield that make up the foundation of all robust earnings in DeFi:

-
**Staking Rewards**: compensation for helping secure the blockchain -
**Lending Rates**: interest earned for providing funds other people can borrow -
**Exchange Rewards**: fees earned for helped decentralized exchanges fill trades -
**Fee Distributions**: fees charged by platforms that are distributed to their token holders

And then there’s the high risk, high reward one that drives most of the really insane interest rates: Incentivized Liquidity Pools, where you’re paid extra tokens in exchange for helping a newer platform launch.

Let’s take a tour of each!

### 1. Staking Rewards

Bitcoin and Ethereum currently operate on a Proof of Work consensus model, which requires "mining" in order to secure the blockchain. Ethereum is in the process of switching to a Proof of Stake consensus model, which will use 99.5% less energy, and which will allow anyone to use their Ethereum to help secure the network.

Miners earn reward fees for securing the blockchain, and once Ethereum switches to Proof of Stake, those rewards will go to stakers instead. So you'll be able to stake your Ethereum and earn some of the transaction fees and block rewards that come from securing the network.

The interest rate depends on how much Ethereum is staked. Currently, that rate is around 6%. But the floor is closer to 5% if a significant percentage of outstanding Ethereum gets staked:

*Source: **Staking Rewards*

This yield is extremely robust and does not rely on inflation or other creative financial incentives. Stake your Etheruem, and you can collect your 5-6% per year in return.

If you wanted to do a "light" version of DeFi, you could simply take your Ethereum and stake it on Lido. They're currently paying 5.8% APR on staked Ethereum, and they handle all of the technical aspects of staking for you. It's slightly less secure than figuring out staking on your own, but you need 32 ETH to setup your own node, so Lido makes it quite a bit easier and cheaper.

The nice thing with Lido too is they give you a "stETH" token in exchange for your staked ETH (get it?) which you can then go do other things with. More on that in a bit.

### 2. Lending Rates

The next type of robust yield is the returns you can earn by depositing your funds on a lending and borrowing platform like Compound or AAVE.

This is certainly the easiest kind of yield to understand. You deposit some DAI into Compound. They let someone else borrow that DAI at 5%. They pay you 4 of that 5% for providing the liquidity. Boom, interest!

It's the same thing TradFi banks do when you deposit money into a savings account, there are just significantly fewer middlemen who need a paycheck along the way.

This is also where we see another difference between DeFi and TradFi: people are typically willing to tolerate paying higher interest rates in DeFi, which is why you're also able to earn higher interest rates. If other investors weren't willing to borrow at 5-10%, you wouldn't be able to earn 4-9%.

What makes these rates interesting is it's possible we'd see the same thing in TradFi if the Federal Reserve didn't effectively control the floor with the fed funds rate. Since there is no central bank in DeFi, the lending rates respond more to market demand than in TradFi.

### 3. Exchange Rewards

The third source of robust yield is from exchange fee rewards. If you provide funds to a decentralized exchange like Sushi, which allows DeFi users to swap between thousands of different tokens, you earn a cut of all trades that are done with those funds.

So if you deposit USDC and DAI liquidity, whenever someone trades between USDC and DAI you'll earn a percentage of the 0.3% fee charged on that trade. It's like owning part of the foreign currency exchange booth at the airport.

Return rates vary depending on which assets you deposit, but most exchanges will have a page where you can see the ROI of supplying liquidity to different trading pairs they offer.

### 4. Platform Fee Distribution

When you deposit funds into a Sushi liquidity pool, you're earning some of the fees, but Sushi is collecting some of them as well. Those collected funds partially go to the Sushi team, but they're also redistributed to people who have "staked" their Sushi tokens on what they call the "SushiBar"

Staking your Sushi tokens represents some degree of commitment to the Sushi platform since while your tokens are staked there, you can't sell them or do anything else with them. And you're showing you own part of Sushi, so you're earning some of the platform fees based on the percentage you own.

It's worth noting that "staking" in this context is very different from "staking" in the Ethereum context above. These staked Sushi tokens aren't validating some Sushi blockchain. They're just earning interest from the Sushi platform, which Sushi is paying as a way to reward Sushi holders for keeping their tokens instead of immediately selling them. The staked tokens don’t “do” anything, besides signal to Sushi that you’re committed to the platform.

Other platforms have more creative rewards structures in place for staking tokens. Curve, for example, keeps a higher percentage of the exchange fees than other platforms. But it then distributes those fees to Curve token stakers similar to Sushi, with one twist: the longer you lock up your Curve for, the higher your interest rate:

The current interest rate on veCRV (the locked CRV token, similar to stETH) is about 20%. But you have to lock up one CRV token for four years to get one veCRV token. If you only lock it for one year, you only get 0.25 veCRV, or effectively a 5% interest rate.

Where things get more interesting is that on Curve, if you stake your CRV tokens you not only earn interest on your staked tokens, you also get a higher interest rate on all the other pools. This comes in the form of "boosts" where your rewards for staking tokens in other pools, like their USDC - DAI - USDT pool, are increased based on how many veCRV tokens you have.

This creates a natural incentive structure to do all of your liquidity pooling possible on Curve, assuming you're bullish on the platform. The more CRV you lock up, the higher your rewards for staking, and the more platform fees you earn.

Those are the big four: staking rewards, lending rates, exchange rewards, and platform fees. And if we just look at those four, you'll rarely see interest rates above 10%. Almost never above 20%.

So what about the crazy interest rates? Where do those come from?

## 5. Crazy Interest Rates from Incentivized Liquidity Pools

It's tough to feel content with your 6% for staking Ethereum when you see the 100% or even 1,000% interest rates you can earn elsewhere.

And you'll notice that none of the big four foundational yield sources offer rates that high. So where are they coming from?

In almost all cases, they're coming from "incentivized liquidity pools." A method of launching new tokens that can be done with a conservative long-term plan, or with a "live fast and die young" hyper-aggressive schedule where they're praying the demand outpaces their insane inflation rate.

Here's how they work.

When you deposit tokens into a liquidity pool like on Sushi as we described above, you earn a share of all the trading fees for that pool.

For established tokens like USDC or ETH, people will naturally supply liquidity to these pools for the trading fees and for a modest return.

But what if you're a brand new DeFi protocol or application? How do you get people to purchase your token, then supply it as liquidity to a decentralized exchange?

Well, you pay them! Let's use Alchemix (which I wrote about here) as an example.

When they launched the platform, they had some ALCX tokens, but no one else could buy them unless there was enough ALCX - ETH liquidity on decentralized exchanges like Sushi.

So, to incentivize people to add liquidity to that pool, Alchemix rewards liquidity providers with additional ALCX tokens. Those rewards are how new ALCX tokens are minted, and they'll be minting ALCX for these rewards over a 3-year period.

If we look at the ALCX - ETH pool on Sushi, you can see that the APR is 138%!

Some of that is coming from trading fees, but most of it is coming from the ALCX incentive Alchemix is paying people for providing liquidity to this pool.

If you're bullish on Alchemix long term, this is a great deal because it means you can earn a huge APR, paid in ALCX tokens, for helping more people buy ALCX tokens. But if people just sell their ALCX tokens as soon as they earn them, that will drive down the ALCX price over time, and could result in the APR you're earning going lower and lower.

Alchemix is an example of a platform doing a good job of this. But you'll also see platforms do significantly more aggressive versions, which is what IRON Finance did and is part of how they blew up. They were paying a massive APR of about 1,825% to people providing TITAN-IRON liquidity, which they paid by distributing new TITAN tokens. That worked great while the price was increasing, but as soon as a big sell-off started, the house of cards collapsed and now TITAN is worthless.

Incentivized liquidity pools are a fantastic way to bootstrap adoption of a new token when they're done well and without too aggressive of a token distribution schedule. But when platforms try to attract tons of hype by dishing out insane APRs by minting tons of their tokens, the APR can't keep pace with inflation and they end up devaluing themselves.

So if you see a platform offering APRs that seem too good to be true, they are. They're printing tons of their own tokens to pay you for providing liquidity, and the value of their token will almost certainly drop precipitously once the weight of people selling their rewards overtakes the demand to jump into the hot new token.

There's one last source of yield I want to mention, since it relates to both legitimate foundational ones as well as the insane inflationary ones.

## 6. Auto-Compounding Protocols

Compound interest is great, but to take advantage of it in DeFi, you usually have to manually compound your rewards from different sources.

For example, if you deposit liquidity on Sushi to earn SUSHI token rewards, those rewards are not automatically being re-invested into the liquidity pool. You have to collect and re-invest them yourself.

But doing that requires making a few transactions, which based on gas fees can be pretty expensive. I actually built a calculator for people in DeFi to use so they could figure out how often they should collect and re-invest their earnings.

If you don't want to do that though, or if your investment isn't big enough to justify compounding it yourself, you can use auto-compounding protocols like Pickle which compound your liquidity pool earnings for you.

If you joined the Sushi ALCX - ETH pool mentioned earlier, you could stake your liquidity pool position on Pickle instead of Sushi, and then your APY would be between 208% and 216%:

That return is the result of Pickle continuously harvesting the Sushi rewards for the pool, and then selling those rewards to re-invest in the liquidity pool and compound your earnings for you.

These auto-compounders are where you start to see some really insane numbers. Check out these auto-compounding farms on Beefy Finance on Polygon:

Put in $1 today, and in one year, you'll have $6,000,000! Nothing concerning about that, right?

Well, just remember that whenever you see an "APY" instead of an "APR" they're getting that number by continuously compounding the current APR for a year. It's not a real rate. The daily rate is accurate, but remember what happened with IRON. When it seems too good to be true, it probably is.

## So Where's the Yield?

When you're evaluating DeFi projects offering you attractive APRs, try to get a sense of where that yield is coming from.

Is it coming from platform fees being redistributed to token holders? Or is it from the platform inflating their currency in the hope that people will keep buying it and pumping it up?

Getting a good read on where the yield is coming from will help make sure you're participating in projects that will last, instead of funding the next runaway crypto ponzi.

## Wrap Up

That's all for this week, be sure to subscribe to get future editions!

If you sign up for the paid membership, you'll also get access to a private Discord with me and the other members of the bundle to talk about all things Crypto, Finance, Productivity, Business, and more.

Aside from there if you have any questions or want to say hi, you can reach me on Twitter.

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
