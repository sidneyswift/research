---
title: "Living Tax-Free off Magical Internet Money - DeFriday #14"
author: "Nat Eliason"
date: 2021-09-24
url: https://every.to/almanack/magical-internet-money
words: 1859
---

Larry Ellison is one of the richest, and the most indebted, people alive.

The term “debt” often sounds negative, but when used strategically, it can be a powerful tool for long term wealth creation or preservation.

Home mortgages are a classic example. A mortgage allows you to pay for your house over 30 years instead of having to pay for 100% its value in cash at closing. Right now, for this privilege, you’d be asked to pay only 4-20% down and a 3% interest rate which, when you factor in inflation, means you’re paying almost nothing for getting to spread out your payments over three decades.

Aside from buying a house, debt can also be helpful in other ways: like when it saves you from paying extra taxes, or from missing out on future asset appreciation.

So back to Larry Ellison. Why is he one of the most indebted people alive? He owns 22% of Oracle, and he's pledged 250 million of his shares (about $22.5b worth right now) as collateral to borrow against.

That essentially creates a credit card with a $22b spending limit that he can use for anything he wants, as long as the Oracle price share doesn't crash enough for him to get margin called.

$22b is an insane amount of credit to tap into, and it’s hard to imagine coming close to using it, so why does he have this massive credit line instead of just selling some Oracle shares?

There are two big benefits:

- He doesn't have to sell shares and reduce his ownership percentage.
- He doesn't have to sell shares and create a taxable event.

The latter is especially powerful. Imagine Larry wanted to live on $1m a year. If he sold shares to do it, he'd have to sell ~$1.25m worth assuming he has to pay 20% for long term capital gains.

But if he borrows $1m against his assets, he doesn’t pay any taxes on it. He hasn't sold any of his Oracle shares, so there’s no taxable event. He gets to live off some of the value of his stock without having to pay taxes or give up any ownership.

If he pushed it too much he could risk over-borrowing and getting liquidated, but assuming he only utilizes a responsible portion of his debt, he could live tax-free indefinitely.

This might seem like some secret tax loophole for the uber-rich, but it’s something anyone can take advantage of if they have some invested assets. Many online brokerages now will let you take out a “Portfolio Line of Credit,” where you can borrow up to a certain percentage of your portfolio at a reasonably low APR.

Just like in the Larry Ellison scenario, this is money that you can use tax-free, in case you needed to do something like make a down payment on a house. But it’s often not an ideal way to borrow money because if you borrow at the top of the market and the market drops, you could risk getting liquidated.

In my article on self-repaying loans, I talked about one alternative strategy in crypto where you can borrow against your principal, and have the yield earned by your principal pay down your debt.

And now there’s another interesting way you can use DeFi lending to live off the yield of your assets: with Magical Internet Money

## Magical Internet Money

Magical Internet Money (MIM) is an actual stablecoin that’s created by an actual protocol called Abracadabra. It sounds like a joke, but it’s not, and understanding it could help you earn more yield on your crypto or reduce your tax liability. In the simplest terms, MIM allows you to simultaneously borrow against and earn interest on your crypto assets. To understand why this is new and useful, it helps to understand DAI, one of the most popular stable coins on the market.

DAI is issued by MakerDAO, and in order to get DAI you need to stake crypto assets as collateral.

MakerDAO lets you deposit ETH, UNI, LINK, YFI, or other tokens, and then borrow against them. When you borrow against them, MakerDAO creates DAI as the borrowed asset, so 1 DAI is always redeemable for $1 of debt, which is how DAI is able to maintain its peg to the dollar.

MakerDAO and DAI were one of the first big DeFi products, and helped open up the whole world of crypto lending. But there’s one downside with using MakerDAO: your assets are locked up as collateral and are no longer able to earn the yield they could earn in other parts of the DeFi ecosystem. Considering you can stake your ETH in a number of places to earn 5-15% APR on it, locking it up as collateral where it earns 0% might not be a great deal.

This is where Abracabra comes in. Instead of using normal crypto assets as collateral, Abracadabra primarily uses “yield bearing tokens.”

A yield bearing token is essentially a receipt of a deposit in another protocol. When you deposit some of your crypto into Yearn, you receive special Yearn tokens that represent your deposit in that pool. For example if you deposit into the Yearn USDC pool, which currently earns 5.43% per year, you receive “yvUSDC” tokens that represent your deposit into that pool.

What's neat with these tokens is that they are your proof of deposit. If you want to transfer your Yearn deposit to a new wallet, you don't have to exit your position and recreate it on the new wallet. You just send your other wallet those yvUSDC tokens. Or if you want to pay someone in USDC, you could just send them the yvUSDC tokens and they'd be able to convert them to USDC on Yearn's site.

The way Yearn credits you the interest in your account is by steadily increasing how much USDC you can exchange the yvUSDC tokens for. So as long as you hold the yvUSDC tokens, their value is increasing as the Yearn USDC vault accumulates more interest.

So instead of locking up your USDC in MakerDAO to borrow DAI against it, where it won't earn any yield while it's locked up, you can first deposit your USDC into Yearn, then lock the yvUSDC into Abracadabra and borrow MIM against it.

If your Yearn tokens earn 7% on average, and your MIM interest is only 0.8%, then you're netting 6.2% interest while being able to unlock up to 90% of your original Yearn deposit. So now you can have the best of both worlds: you can still earn yield on your assets, but also borrow against them.

And with a deposit like yvUSDC, those tokens are based on interest earned on stablecoins, so they *shouldn’t* go down in value, unless something catastrophic happens to the stablecoin they're based on. That means that unlike borrowing against ETH or another volatile asset where you have to be more worried, you could theoretically push your borrowing amount much higher without having to worry as much. Borrowing 90% of your collateral value with a volatile asset is extremely risky. But doing that against something pegged to the dollar? It's not risk free of course, but it's quite a bit safer.

So you could hold a large chunk of money in yvUSDC, earn your 7% on it, and then if you need some money for something just borrow MIM against it instead of selling.

And unlike other ways to borrow against your assets in crypto, you're not giving up that topline yield, and you don't have to sell anything which would create a taxable event. Assuming your USDC amount grows faster than the additional amount you're borrowing against it, you could keep doing this indefinitely.

Or, of course, you could do some hilariously aggressive debt stacking to boost your return considerably higher.

## Debt Stacking for Extra Yield

Since you can deposit yield-bearing assets into Abracadabra, and since you can borrow up to 90% of the value for the stablecoin pegged ones, you can do some pretty crazy debt stacking if you want to maximize your return (with additional risk).

Here’s one example:

In this case, I’ve set up an initial deposit of 10,000 yvUSDC (about $10,000), and borrowed 85% of the value against it.

Then, I'm doing 10 “loops” with that borrowed MIM. For each loop, Abracabra:

- Borrows 85% of my collateral value in MIM
- Converts that MIM to more yvUSDC
- Deposits that yvUSDC back into Abracadabra
- Then repeats!

As you can see in the screenshot, that ends up borrowing a total of $48,212 MIM, with making the collateral amount earning interest around $56,720, creating an effective APY on my $10,000 of 29.7%. Quite a bit higher than the 5.4% it would normally earn right now!

The more you loop your debt like this, the easier it is to get liquidated, but since you're borrowing against something that should be based on a stablecoin, your risk of liquidation is much lower than it would be with other assets. And since you aren’t depositing anything other than your original principal, that’s the only thing that’s at stake. You can’t go into debt.

I’m not recommending you do this of course, and obviously nothing is risk free in crypto, but this kind of debt stacking does create a pretty interesting boost to your earnings rate for anyone who want to be adventurous.

## Using Abracadabra and MIM

Abracadabra creates a bonus layer of DeFi for anyone who has already explored Yearn from the “automatic asset allocation” article.

If you’re building up a large position in Yearn’s USDC vault, you’ll be passively increasing your USDC balance for whenever you need it.

Then, if you have some large expense come up where you need some of those funds, you can just take the Larry Ellison approach. Don’t sell, borrow!

Go to Abracadabra.money’s borrowing section, and check on the yvUSDC vault. Depending on demand, there might not be any MIM’s available at the time, in which case you can join their Discord and wait for an announcement that more are available.

Once there are some MIM’s available to borrow, you’ll be able to deposit your collateral and borrow however much MIM you need against it.

With the MIM in your wallet, you can use it like any other stablecoin you’d use in crypto. Or if you need it for something offline, you can convert your MIM to USDC on Curve:

Then cash it out to Fiat on Coinbase!

Congrats, you’re now living off your appreciating assets like a billionaire. Feels good, doesn’t it?

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

Hello, thank you for this info, can you explain the concept of liquidation?
