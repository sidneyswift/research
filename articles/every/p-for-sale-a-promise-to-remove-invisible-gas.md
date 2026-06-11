---
title: "For Sale: A Promise to Remove Invisible Gas"
author: "Jamie Wong"
date: 2023-06-25
url: https://every.to/p/for-sale-a-promise-to-remove-invisible-gas
words: 6943
---

# For Sale: A Promise to Remove Invisible Gas

A primer on the carbon dioxide removal market in 2023

June 25, 2023 Updated June 6, 2026

#### Sponsored By: The Information

This essay is brought to you by The Information, the biggest dedicated newsroom in tech and business journalism.

The Information offers access to exclusive insights from the industry's top journalists. For a limited time, subscribe and save 25% on your first year.

*Editor’s Note: Climate change is one of the world’s most pressing issues, and it’s becoming fertile ground for technology innovation and investment. Today’s post, from Jamie Wong, is a starter guide for anyone new to the byzantine world of carbon dioxide removal (CDR). *

*Many tech companies (Stripe, Alphabet, and Microsoft, and more) are funding CDR efforts, VC firms are backing CDR providers, and mission-driven founders are developing software tools to support the process. Jamie has spent the last several months mapping the space, and this primer is the result of his efforts. It’s an excellent resource for anyone in tech looking to go deeper on the subject.*

In a select few corn fields after a harvest, the unwanted stalks, leaves, and cobs are fed into a storage container on the back of a long-haul truck. These agricultural wastes won’t be hitting the road in their loose, fluffy state though.

The storage container doesn’t start empty. It contains a complex chemical machine fine-tuned to efficiently convert the corn detritus into three chemical compounds: biochar, bio-oil, and syngas. The biochar, a solid, is scattered back onto the farm fields to improve field fertility. The syngas is, in part, used as fuel to keep the high temperature reaction going. The bio-oil is destined to be injected deep underground. Bizarrely, people will pay for it to be put there, not to save for later use, but with the promise that it will stay there forever.

This whole operation happens under the purview of Charm Industrial, a leading participant in a growing market of players with a shared goal: suck carbon dioxide directly out of the air and store it away for good. This is carbon dioxide removal, or CDR for short.

The machinery acting as this conceptual vacuum cleaner for the sky is about as diverse as you can imagine for an industrial process. Charm’s bio-oil production is just one of many. Another method starts with trays of powdered rock and ends with cement production. A third involves growing kelp in the open ocean and encouraging it to eventually sink to the bottom.

The Information offers access to exclusive insights from the industry's top journalists. Founded in 2013, The Information has built the biggest dedicated newsroom in tech journalism and count many of the world’s most powerful business and tech executives as subscribers. Their reporters focus on reporting the people, trends, and forces that are defining the future of technology and business.

As a subscriber, you'll get access to award-winning reporting, exclusive interviews, community conversations, and subscriber events and more, so you can make informed decisions anywhere, anytime. For a limited time, subscribe and save 25% on your first year.

The market is small for now, but ambitious. To meet the scale of needs for carbon dioxide removal outlined in the Intergovernmental Panel on Climate Change’s (IPCC) 2021 report, our rate of global removal will need to double roughly every 21 months for the next 27 years (1). IPCC wants us to reach net zero carbon dioxide emissions by 2050, and carbon removal plays a big role in that.

We’ll need a market with hundreds of billions of dollars in transactions per year. We’ll need an entirely new global industry on the scale of steel or cement.

This is the rate we need assuming we*succeed*in dramatically reducing emissions

*and*dramatically scaling up natural climate solutions.

*So we’ve got some challenges ahead.*

*Caption: The most optimistic emission reduction pathway from the IPCC's 2021 Assessment Report. Original **via Zeke Hausfather**. Edits in red are my own.*

Since leaving my job as a software engineer at Figma at the end of 2021, I’ve been learning about unsolved problems in the climate change space, and seeing where software can play a role. My exploration was perilously broad at first. Climate tech encapsulates everything from predicting the cost of connecting new solar to the grid, to chemically transforming refrigerants, to improved cow feed to reduce methane from their burps, to novel steel manufacturing strategies. Each entails a totally different market, with different stakeholders, and different problems.

Without choosing a specific problem domain, I found myself forever skimming across the surface: learning small details here and there, but never enough to evaluate real hypotheses about where I, personally, could apply leverage.

So lately I’ve been focusing on a narrow but important slice: carbon dioxide removal. I’d like to share what I’ve learned about the CDR market through reading and a couple dozen conversations with founders, investors, engineers, and scientists. This article is for anyone curious about CDR, but has a slight emphasis on areas where software is playing a role.

This post is a whopper, so here’s a preview of the path we’ll take:

- Orienting ourselves in the broader context
- Suppliers: the companies doing the main thing
- Capital: show me the money
- Building trust: where, exactly, did my money go?
- Let’s recap
- Where to go from here
- Further reading & acknowledgements

## Orienting ourselves in the broader context

Talking about carbon dioxide removal is a bit of a mess.

I’m afraid readers might leave with misguided perspectives like “new technology is *the solution* to climate change,” or worse “carbon dioxide removal is *the solution* to climate change.” New technology broadly, and carbon dioxide removal specifically, are squarely in the camp of “necessary, but not sufficient on their own.”

We’ll be exploring a sub-branch of a sub-branch of what’s needed to stabilize our climate. But remember, we need the whole conceptual tree to win this fight, and watchful arborists to tend to each branch and ensure its growth.

As for *real* trees, they will not be our focus today. Nor will filters placed atop smoke stacks. We’ll be focused on permanent removal.

### Three crucial jobs

*The most optimistic emission reduction pathway from the IPCC's 2021 Assessment Report. Original **via Zeke Hausfather*

If you examine the graph above describing an optimistic path to net-zero emissions, the three colors (gray, green, blue) indicate three crucial jobs needed to reach a stable climate over the coming decades:

-
*Reduce new emissions (shrink the gray).*This is where the vast majority of the work lies in fighting climate change. This job requires transitioning our electrical grid to renewable energy, electrifying our transportation and heating, and decarbonizing industrial processes like cement and steel production. This is also where technology like filters on smoke stacks, or filters placed on the exhaust system of semi-trucks, belong. Some of these solutions, like replacing a coal power plant with a solar farm plus storage, might be permanent in the sense that the emissions are permanently reduced. But solutions in this camp can’t remove emissions from the atmosphere that happened long ago. So things in this camp are not necessarily removal. -
*Use nature to remove carbon from the atmosphere (grow the green).*This is where high-quality tree planting initiatives play a role, for example TIST and Terraformation. These do remove carbon dioxide directly from the atmosphere, even if it was emitted long ago. But we can’t be confident about how long carbon held in trees will stay there. Forest fires, lumber production, and disease can all result in the carbon returning to the atmosphere. It is*removal*, but it’s not confidently permanent. -
*Artificially remove carbon from the atmosphere (grow the blue).*There are a few reasons we need to do this on top of the other two jobs. First, we*don’t*have credible plans for avoiding certain kinds of emissions, like the partial evaporation of fertilizer from agricultural fields (2). That’s why you never see the gray section go away completely. Second, we want to return our atmosphere to pre-industrial levels of CO2 concentration, not just stop concentrations from rising. That requires removing more carbon-dioxide than we’re emitting, which is why you see the black line representing net emissions eventually going into the negative.

Today we’ll only be discussing the third job—referred to as “Carbon Dioxide Removal” or CDR. I didn’t choose to focus on CDR because it’s the *only* important job of these three, or even *the most important* of these three. We need all three. But if you’re an entrepreneur, engineer, investor, or anyone else who wants to contribute meaningfully to the space, it’s helpful to choose a specific part of the problem.

### The lens of the day

There are many lenses to use when trying to understand CO2 removal. We could ask how we developed consensus for how much we need by 2050, or what spurred the initial research identifying strategies for CO2 removal, or compare different methods by their energy and land area requirements. Those all fascinating angles! But they’re not the focus of this article.

Here, our goal is to build intuition for what the CO2 removal industry looks like in 2023. In terms of big buckets, we’ll be focusing on three:

We’ll build up the following map, but do so gradually, so don’t worry about imbibing its contents in a single gulp. We’ll use concrete examples of organizations playing these various roles, and aim to be illustrative, rather than exhaustive.*Caption: A market map I created showing the flow of money through the CDR ecosystem*

With boundaries drawn around the subject of the day, we can start to examine what’s inside those boundaries. Let’s start with the suppliers.

## Suppliers: the companies doing the main thing

To be a supplier of permanent CDR, you have two crucial jobs:

-
**Capture**: how do you pull CO2 from the atmosphere? -
**Sequestration**: where do you put the captured CO2, and how do you ensure it stays there for 1000+ years?

There’s a lot of different approaches to pulling CO2 from the air and then figuring out how to store it long-term so it doesn’t escape. Let’s see how some leading suppliers answer these two questions:

The problems these companies are facing in scaling removal are varied, but I heard a few problems repeated. One was a problem I never needed to think about for software: permitting.

### Permitting: for anything that touches air, water, or dirt

To deploy at scale, removal suppliers need to build industrial infrastructure. Whenever you want to build a big physical *anything,* permitting law comes into play. Discovering which permits you need, applying for them, and engaging in back-and-forth with their regulating body can be a massive time sink for suppliers.

When I visited Charm Industrial, CEO Peter Reinhardt explained that they don’t deploy industrial infrastructure in California, despite the company HQ being in San Francisco. Getting permits in California can take years. By contrast, in some more politically right-leaning states, it takes weeks. They’d love to deploy in California, but the timelines make it prohibitive.

When I asked Heirloom’s CEO Shashank Samala about the problems that keep him up at night, permitting was on his list:

Different jurisdictions have varying rules and requirements for permits such as grading, electrical, building, construction, environmental and other permits. It would be immensely beneficial to have a comprehensive and up-to-date database containing all the necessary information for each permit, in every jurisdiction including contact information and where exceptions can be made.

Oftentimes, the challenge lies in the fact that permitting teams are understaffed. We had issues with staff turnover / lost knowledge midway through given how long these permitting timelines are. It is astonishing how outdated some of these procedures can be. For instance, in California, physical signatures on laminated drawings are still required for civil drawing approvals.

A few early-stage startups have begun working in this space. Blumen Systems and Paces are both working on automating discovery of permits for climate tech companies.The permitting problem is painful enough that CDR suppliers may design their deployment strategy around it. For some companies, this means deploying in states or countries with less arduous permitting processes. Ironically, another strategy is to woo the right industrial partners

### Industrial partners: piggy-back on a massive industry

Many Carbon Dioxide Removal (CDR) providers form symbiotic relationships with industry interests. The industrial partners—organizations like agriculture companies or desalination plants—allow the CDR suppliers to operate on their land and use their permits, which makes it easier for CDR suppliers to scale their efforts. In return, the CDR companies can save their partners money by turning their partners’ waste products into tools for CDR.

For example:

- Charm Industrial has agricultural and forestry partners to turn waste streams (corn stover and mechanical forest thinning respectively) into feedstock for its pyrolyzers. The agricultural partners get biochar, a soil-health enhancing material, distributed onto their fields in the process.
- Ebb Carbon partners with desalination plants, helping them turn the waste hyper-saline solution extracted from sea water into a chemical input for Ebb. By installing on-site, Ebb gains access to a system for returning large volumes of water to the ocean.
- Lithos has mining and agricultural partners. They turn basalt (a waste product of the mining industry) into soil health enhancing minerals for their agricultural partners. The agricultural partners provide them the large land area they need for spreading the basalt to maximize its reactivity.

With lab-tested CDR methodologies and industrial partners in hand, suppliers can build out a plan to scale. To put that plan into action, they need cash, and lots of it.

## Capital: show me the money

The CDR suppliers have bills to pay, things to buy, and employees who need to eat. CDR suppliers’ capital comes predominantly from selling carbon removal credits, venture capital, and research grants. Here’s how each of these avenues work.

### Carbon removal credits

Suppliers want to sell the removal of CO2 as a service. To make this a purchasable quantity, they parcel up tons of CO2 removed into units sometimes called “carbon removal credits.” The credit will show, at a minimum, how much CO2 was removed, who did the removal, and when the removal happened. Buyers of these credits can use this information as evidence of fulfilling public facing climate commitments.

In other words, companies that want to help fight climate change or offset their own carbon emissions will buy these “credits” to indicate how much carbon they helped remove from the atmosphere. It’s a good PR move, among other things.

So who are these buyers? Currently, nobody has a regulatory requirement to buy carbon removal (3), so anyone doing so is doing it voluntarily.

The industry is targeting $100/ton of CO2 removed, and 3.8 billion tons/year by 2050, which would make for a $380 billion/year market. At that scale, private-sector voluntary markets are going to be woefully inadequate, but we need to bootstrap a market to get there. This requires some buyers to act in economically irrational ways.

### The corporate buyers

Surprisingly, there are a number of companies willing to do it anyway. Some are driven by a sense of moral obligation to build a better future. Some may expect this market to happen with or without them, so they’d like a seat at the table to shape future legislation. Whatever the motive, it’s been enough to kickstart a sizable market. According to cdr.fyi, over 3 million tons in sales have been made as of May 2023, for a total transaction volume of $365 million USD since the industry’s inception.

One of the earliest buyers was Stripe (4), who announced in 2019 that they’d spend at least $1 million USD/year on carbon removal. In 2020, they fulfilled that promise by making purchases from Climeworks, Project Vesta, Charm Industrial, and Carbon Cure (5). For three of these companies, Stripe was their first customer.

Nan Ransohoff, Stripe’s current Head of Climate, now also leads Frontier, a coalition of Stripe, Alphabet, Shopify, Meta, and McKinsey which have collectively committed $1 billion towards purchasing carbon removal between 2022 and 2030 (6). This kind of advanced market commitment is crucial for building financial security for suppliers, which in turn provides security for investors knowing that these companies will have revenue to bolster their growth.

On May 23, 2023, JPMorgan Chase signed contracts to purchase $200 million in carbon removal via Climeworks, Charm Industrial, and a contribution to Frontier.

Microsoft explicitly committed to carbon negativity, which requires the purchase of carbon removal. They have a live dashboard of the removals they’ve purchased contracts for, including which vendors provided it.

### The curators

Early in this process, all purchases were made by bilateral agreements between climate-conscious companies and carbon removal providers, with no market curators in the middle. This meant that buyers had to do due diligence from scratch, and providers had to spend a ton of time on sales. This is one of the inefficiencies that companies like Watershed and Patch are addressing.

The equivalent for individuals instead of corporations also exists: Wren and Commons provide subscriptions to individuals who want to offset their carbon footprint, and they buy carbon offsets and removals on your behalf. If you’re looking for a tax-deductible option, check out Terraset.

### Pre-sale of credits for fledgling companies

The money available to carbon removal suppliers once they can deliver removal is encouraging!

But the market, as it stands today, is heavily supply constrained. While 3 million tons have been purchased, only ~2% of those tons have actually been delivered. Many suppliers are sold out of commitments for the next several years.

So at the moment, we need ways of accelerating our suppliers, and need ways of creating more suppliers. AirMiners is trying to accelerate the creation of CDR companies by helping them secure early funding through pre-sale of credits, discounted heavily based on the risk of credits never being delivered. Frontier also offers pre-purchase for fledgling CDR suppliers.

The more traditional route for pre-revenue companies to get funding is venture capital.

### Venture capital

Venture capitalist funds raise money from wealthy individuals and funds-of-funds to invest in portfolios of high-risk companies. They assume that the majority of their portfolio companies fail, but that a few of them yield outsized returns. Making many bets in pure software is relatively cheap, because the cost to evaluate product-market fit is usually the salary of a few software engineers for a year or two.

CDR companies, by contrast, typically need millions of dollars just to buy equipment, even for lab-scale prototypes. Because CDR is fundamentally about scaling physical processes, both the cost and speed of scaling is much worse than software, making it less appealing to most venture capitalists.

There are a few firms, however, with enough conviction in the space to invest in multiple providers (7):

- Lowercarbon Capital invested in Charm Industrial, Heirloom, Running Tide, Verdox, Undo, and Noya. Lowercarbon has a $350 million fund dedicated to carbon removal.
- MCJ Collective invested in Charm Industrial, Heirloom, and Noya.
- Prime Impact Fund invested in Charm Industrial, Verdox, and Project Vesta.
- Breakthrough Energy Ventures invested in Heirloom, and Verdox.

Here’s what Yin Lu from MCJ Collective (a purely climate fund) said about how they think about investments into companies with physical assets as part of their portfolio:

Roughly half of our investments historically have been in pure software companies and we expect that trend to continue.

Roughly half of our investments have some sort of real-world component to them. […] Most of our physically oriented companies have created some form of new process such as carbon removal, chemical synthesis, food production, or the like.

What you need to believe for this category is that the industries they are in will be undergoing fundamental change over the next decade due to the move toward decarbonization. This is a once in a lifetime transition that will see new companies emerge to capture large shares of existing markets and achieve scale that was otherwise not possible in previous innovation cycles.

Each time you raise venture capital, you sell part of the company. Founders looking for additional funding but wary of losing ownership will search for other sources of capital. The most common for early climate tech companies is grants.

### Grants

For novel technology aligned with societal need, there are billions of dollars available in research grants. The government offers a variety of grants that are applicable to some subset of CDR companies:

- The Office of Clean Air Demonstrations has $3.5 billion available in grants to establish direct air capture hubs.
- The Advanced Research Projects Agency-Energy (ARPA-E) announced $45 million in funding for companies working on validation of ocean-based carbon dioxide removal and also provided funding for research into Direct Air Capture (DAC) technology, including a grant to Heirloom for $476,811.

Private organizations also offer grants:

- The Musk Foundation partnered with XPRIZE to offer a $100 million milestone-based prize for carbon dioxide removal providers.
- Additional Ventures created a $10 million research award to further research into ocean alkalinity enhancement.

Unlike venture capital, the money for grants is not exchanged for equity in the company receiving the grant. The granting agency gets nothing financial in return. This makes grants, in a sense, “free money.” But the application process can be time consuming, and grants commonly constrain how the money can be used. Even after grants are issued, they create additional work reporting progress back to the granting agency.

It’s common for CDR companies to have full-time on-staff grant writers or to hire consulting firms to help them fill grants to manage the paperwork load. Some companies skip grants altogether because of their time intensity. To help ease this process, companies like Streamline and Pioneer are leveraging modern AI (e.g. GPT-4) to gather requirements and fill in grant applications.

Even after grant approval, the time for the money to hit the company’s bank account can sometimes be upwards of a year. This is one place where loans can help.

### Loans

If you’re quite confident you’ll have money in the future, but you need it now in order to help your company grow faster, you want some kind of loan. Enduring Planet builds financial infrastructure to handle two cases of this situation, specifically for climate entrepreneurs.

The first is when you’ve demonstrated a steady stream of revenue. This is unsurprisingly called “Revenue Based Financing.” The second, a “Climate Grant Advance,” provides money to climate companies who’ve already been approved for a grant, but haven’t received the money yet.

As the market matures and the revenue streams for CDR companies becomes less risky, traditional finance organizations will play a larger role here.

We’ve outlined two crucial blocks of the market: suppliers to remove carbon, and sources of money to make it happen. This system only works, however, if the folks with the money trust that their money has the intended effect.

## Building trust: where, exactly, did my money go?

If you owned a grocery store and needed to source some tomatoes, you’d try a few suppliers, and evaluate them based on the price, quality, and reliable delivery. If the tomatoes taste like feet or always show up late, you’d switch suppliers. In the CDR market, customers are buying a promise that an invisible gas is moved from one place to another, where the destination is far out of sight from the customer. So not only is it hard for the customer to “taste” the quality of the product, it’s hard to even know when it’s arrived!

To make the system work, we need a group of third parties where their primary function is to facilitate trust between suppliers and sources of capital.

This starts with building a shared understanding of the core mechanism of removal.

### Fundamental research: does the process remove carbon at all?

The discovery and evaluation of methods for carbon dioxide removal originate in fundamental research within universities and government labs. Through peer review and challenges from subsequent papers, we develop increasing confidence in the fundamental principle behind each method.

For example, the paper CO2 extraction from seawater using bipolar membrane electrodialysis (2012) was peer-reviewed and published in the journal of the Royal Society of Chemistry in their Energy & Environmental Science journal. The first author of the paper, Matthew Eisaman, went on to found Ebb Carbon to implement and scale the practice described in the paper.

Ambient weathering of magnesium oxide for CO2 removal from air (2020) was peer-reviewed and published in Nature Communications. The first author, Noah McQueen, is now co-founder of Heirloom, which is scaling this methodology.

This kind of research can serve as the catalyst to convince venture capitalists that a company concept isn’t totally nuts. As part of their investment memo for Heirloom, MCJ Collective cited this underlying science as a source of confidence:

[T]he basis of Heirloom’s technology stems from research led, in part, by Dr. Jennifer Wilcox who now serves at the U.S. Department of Energy. While there inevitably will be a need to bridge the gap between research performed at the lab bench and commercializing the technology in market, we are confident this risk is managed by the encouraging findings of the research and Heirloom’s iterative prototyping. – “Our Investment in Heirloom”, MCJ Collective

These papers describe fundamental mechanisms and estimation protocols, but typically describe isolated steps at small scale. To understand climate impact, we need to look at the process holistically.

### LCA: is it carbon negative?

As human history has shown, sometimes we inadvertently make things worse when we try to fix a problem. In the CDR world, having a mechanism which removes carbon dioxide from the atmosphere is useless if you emit more carbon than you remove in the process. Emissions can come from a range of things—e.g. energy used in manufacturing industrial equipment, operation of that equipment, and transportation.

Determining the *net* removal is the domain of a process called Life Cycle Analysis (LCA).

*From*

*“Bio-oil Sequestration: Prototype Protocol for Measurement, Reporting, & Verification”*

Absent relevant regulation, the process for establishing consensus on an LCA for a given company’s removal methodology is still up in the air, but typically involves peer review from industry interests rather than academics. These LCAs are made publically available for scrutiny.

The framework Charm Industrial uses to evaluate its net emissions was written by Carbon Direct and EcoEngineers, and then reviewed by Charm Industrial, Lowercarbon Capital, Frontier, and others.

The framework Running Tide uses was written by Running Tide, then reviewed by Lowercarbon Capital, Stripe, Patch, and others.

### MRV: what did my money, specifically, do?

Once the fundamental removal mechanism is confirmed, the carbon negativity of the entire process is quantified via LCA, and the supplier can run the process outside the lab, the last crucial step is providing an auditing chain for each action in the removal. This is the domain of Measurement, Reporting, and Verification (MRV).

To see what MRV looks like in practice, it’s instructive to look at Charm Industrial’s registry. On September 24, 2021, Block purchased 55 tons of CO2 removal from Charm Industrial via Watershed:

To present this information to buyers, you need:

- Sensors deployed in the field (in this case, probably a scale for bio-oil)
- A data collection pipeline to record this data reliably and accurately
- Software to convert those raw sensor values into emission and removal numbers using the appropriate method’s LCA process
- A way to build out a many-to-many relationship between deliveries and purchases and durably record those purchases to avoid double-counting

Most steps in Charm’s process lend themselves well to direct measurement. If we trust Charm is telling the truth about the scale reading leading up to the bio-oil being injected deep underground, then we can trust the amount of removal being performed. This is also the case for direct air capture systems like Heirloom, where the pure CO2 stream captured can be directly measured.

There are still some sources of uncertainty in these processes, however. Using its CDR Verification Framework, CarbonPlan is working on mapping out the sources of uncertainty in calculating net emissions, and assigning “Verification Confidence Levels (VCLs)” ranging from 1 to 5 for different pathways.

CarbonPlan assigns “Biomass Carbon Removal and Storage”, the pathway used by Charm, a VCL of 3-5. To examine what the remaining sources of uncertainty are, check out the CarbonPlan website.

For CDR methods using the ocean or soil to sequester carbon, measurement is more difficult, which yields higher uncertainty. For example, for ocean-based methods to accurately estimate their net removal, they need:

- Access to third party meteorological and oceanographic data like weather predictions, ocean currents, seabed topography, and satellite imagery
- A much richer variety of sensors deployed into the ocean on buoys: humidity, barometric pressure, temperature, etc.
- More resilient systems for sensor data collection, since the sensors will need to be left unattended for long spans of time
- Computationally intensive ocean simulations to estimate the timeline and quantity of the removal

Unlike Charm or Heirloom’s processes, it’s infeasible to directly measure the amount of CO2 removed from the atmosphere. The removal takes place over a massive surface area of water, as the ocean itself absorbs CO2 from the atmosphere. Even if we all agree on all the sensor inputs, there’s a lot to debate about the methodology for turning those sensor inputs into the number of tons of CO2 removed.

These are the kinds of challenges that Running Tide and Ebb Carbon face. CarbonPlan assigns Running Tide’s original method, “Ocean Biomass Sinking (No Harvest)”, a VCL of 1-2, and Ebb Carbon’s method, “Ocean Alkalinity Enhancement (Electrochemical)”, a VCL of 3. We can raise these confidence levels over time by developing better measurement strategies through research and experimentation. This is presumably why, as noted in the grants section above, ARPA-E announced USD$45 million in funding to validate marine CDR methods.

If we can control uncertainty, ocean and soil-based systems hold a lot of promise. By piggy-backing off of natural processes already happening at massive scale, they tend to be easier to scale quickly with lower energy requirements and require less novel machinery (8).

At the moment, this MRV process is done in-house by the CDR suppliers. This both creates duplication of effort (e.g. every supplier building their own web interface to expose to buyers), and a perverse incentive to overestimate removal. For now, the market is small enough (and difficult enough to enter as a supplier) that trusting companies to act in good faith is reasonable. As the market scales, however, this will become decreasingly true. So we’ll eventually need MRV-specific companies.

### MRV service companies

A tiny minority of funding (especially venture capital) has gone to companies focused on MRV for CDR. But there are a few players emerging.

Isometric is building a multi-pathway registry and verification service. To minimize perverse incentives to fill their registry with as many credits as possible, they charge a per-ton verification fee to the buyers of carbon removal rather than accept per ton registration fees from suppliers. The registry portion of the platform would be similar to Charm Industrial’s registry, but supporting many companies and CDR processes, rather than just one.

In order to do estimation and verification of ocean-based carbon removal, both CDR suppliers and verifiers will need infrastructure to run earth systems models. The models themselves come from academia. ⟦C⟧worthy is a non-profit working on improving these models for CDR purposes.

Submarine is adapting these models to support the MRV process and building the data infrastructure needed to run them at scale for use by both CDR suppliers and verification services.

**Let’s recap**

Okay! That was a lot of information to swallow! Let’s do a quick recap.

To stabilize our climate, we need to dramatically reduce our emissions. But even with optimistic estimates for our rate of reduction, we’ll still need technology to remove CO2 directly from the atmosphere. To reach the scale of removal needed, we need to double the rate of global CO2 removal every 21 months for the next 27 years.

To make this happen, we need to accelerate a variety of market players and processes.

** Suppliers—**Suppliers have two main jobs: capturing carbon dioxide directly from the atmosphere, and storing it away forever in a way that doesn’t leak back into the atmosphere.

-
**Permitting:**To build industrial infrastructure, suppliers need permits. This process is long and painful right now. Companies like Blumen and Paces want to make this less painful. -
**Industry Partners:**To gain access to land and permits, CDR suppliers partner with massive industries like agriculture, mining, steel manufacturing, and desalination plants. In exchange, the partners get decreased cost of waste removal, or co-benefits like improved soil quality.

** Capital—**To fund operations, suppliers have a few key sources of capital:

-
**Sale of carbon removal credits:**Corporations and individuals voluntarily buy carbon removal credits. Companies like Watershed and Patch provide curated market access to enterprise customers. Companies like Wren and Commons provide access for individuals. Later, there may be regulatory requirements to buy these, or possibly direct procurement by governments. -
**Venture capital:**Investment funds like Lowercarbon Capital, and MCJ Collective buy partial ownership of suppliers’ companies. -
**Grants:**Organizations (mostly government agencies like the DOE or ARPA-E) provide money for research, which suppliers can apply for. To make this process easier, companies like Streamline and Pioneer are helping write and manage grant applications. -
**Loans:**If suppliers can demonstrate that they will have money available to them down the road either from revenue or grant approvals, financial institutions like Enduring Planet will give them an advance on that capital.

** Trust—**For the market to work, everyone involved must have consensus on how money is turning into permanently removed carbon dioxide.

-
**Research:**Academic, governmental, and industry research organizations publish papers on the fundamentals of a given CO2 removal method. These papers are peer reviewed and distributed by journals. -
**Life cycle analysis (LCA):**Suppliers, usually in conjunction with a third party consultancy, publish a methodology showing the CO2 emissions and removal at every step in the process, demonstrating that the method creates net negative emissions. -
**Measurement, reporting, and verification (MRV):**As suppliers run their process for removal in the real world, they carefully record measurements along the way. This can include things like the weight of bio-oil being injected, or the ocean salinity reading from a buoy where a fluid was released into the ocean. The LCA is then applied to determine the net removal from the actions of the company, which is entered into a registry so carbon credit buyers can see what their money was used for. Companies like Isometric and Submarine are working on improving these processes, alongside non-profit organizations like ⟦C⟧worthy.

Now then, what should you do with all this information?

## Where to go from here

When asked to give advice to software engineers interested in contributing to the climate fight, the founder of Spark Climate Solutions said:

If you’re interested in path (a) and find yourself intrigued by carbon dioxide removal, many of the companies referenced in this article are hiring! Here are some job openings (dated June 2023):

- Full Stack Developer @ Running Tide (Remote USA): Running Tide does CDR via marine biomass cultivation.
- Full Stack Software Engineer @ Ebb Carbon (San Carlos, California): Ebb Carbon does CDR via electrochemical ocean alkalinity enhancement.
- Lead Modeling and Simulation Engineer @ Heirloom (Brisbane, California): Heirloom does CDR via direct air capture.
- Technical Lead @ Undo (London, UK): Undo does CDR via enhanced rock weathering.
- Platform & SRE Engineering Roles @ Isometric (London, UK): Isometric is building a verification and multi-pathway registration service for carbon removal.
- Founding Engineer @ Streamline (San Francisco, California): Streamline helps climate companies apply for grants much faster.
- Founding Engineer @ Blumen (San Francisco, California): Blumen provides siting intelligence tools for geothermal, hydrogen, carbon sequestration, and minerals project developers.
- Multiple Software Engineering Positions @ Watershed (San Francisco, NYC, London, Remote): Watershed, among many other things, provides a curated marketplace for carbon removal purchases.
- Software Engineer @ Patch (San Francisco): Patch also does many things, but one is to provide a curated marketplace for carbon removal purchases.
- Full Stack Engineer, Climate @ Stripe. (Remote): Stripe helped catalyze the start of the permanent CDR market with early purchases.

If you’re interested in path (b), here’s the consistent advice I’ve gotten from people that have walked this path (9):

- Talk to a bunch of people in a specific industry. If the problems are too diverse, narrow down the company category or job role until they become consistent.
- Choose a specific problem. Ask people about the problem to understand if it’s a mild annoyance, or the source of a constant living hell. If you want to build a big venture capital-backed business, make sure solving this problem has a path to building a $1 billion company.
- Propose a specific solution.
- Try to rapidly figure out why your solution is, in fact, a bad idea. If you fail to find evidence it’s a bad idea, try to implement it. If you find strong evidence, return to step 2.

In the course of researching and writing this article, I’ve mostly been doing steps 1 and 2. Here are the problems I’m considering exploring for steps 3 and 4:

- MRV for ocean based CDR
- MRV for soil based CDR
- Removing duplication of effort for sensor data aggregation for new CDR companies

If you’re also interested in path (b), the good news is finding the frontier problems in the space doesn’t take that long, and people will be happy to see you when you get there:

##
**Further reading **

This article comes in a short lineage of folks building their understanding of CDR from the ground up, and sharing what they learned:

- “We Need To Take CO2 Out Of The Sky” by Ryan Orbuch. Ryan is now a Partner at Lowercarbon Capital leading their $350 million carbon removal fund. If you want to stay on top of the space, following him on Twitter is a good bet.
- “Scaling CDR” by Neil Hacker. Neil is now a Researcher at Isometric, helping to build their verification and registry service for carbon removal.

If you enjoyed reading this, here are some other resources you might like:

- For an alternate take on the current state of CDR, see The State of Carbon Dioxide Removal.
- For a crash course in CDR, see AirMiners’ free 6 week cohort-based course called Boot Up.
- For a video series on the ongoing evolution of industry, see OpenAir’s THIS IS CDR.
- For writing on how to shape the growing CDR market, see The Great Unwind.

*Footnotes:*

- This assumes 100,000 tons will be removed in 2023, and that we need the capability to remove 3,800,000,000 tons/year by 2050.
- See https://cdrprimer.org/read/chapter-1#sec-1-4
- At time of writing, SB308 is under debate in the California legislature, which
*would*create a regulatory requirement to buy carbon removal. - Many members of the climate team at Stripe eventually scattered to build critical infrastructure to support CDR: Taylor Francis, Avi Itskovich, and Christian Anderson left to start Watershed which, among other things, provides climate-conscious corporations curated access to buying carbon removal. Ryan Orbuch left to join Lowercarbon Capital, now the leading venture capital fund in carbon removal.
- In the process, they open sourced all of the applications and purchase agreements, which serve as a great summary of core methodologies used by all the applying suppliers, free from marketing fluff. You can see them here on GitHub.
- Similar to Stripe’s internal process, Frontier also maintains open source applications and purchase agreements on GitHub.
- Occasionally, folks worry that carbon-dioxide removal is overallocated. But even within climate tech, CDR represents a relatively small portion of VC dollars. <2% of climate sector venture capital went to carbon removal as of 2022. See ”$40B and 1,000+ deals in 2022 market downtick” from CTVC for details.
- For more about the risks of biasing too far towards the easily observed processes, see “Leveling the Playing Field for Open-System Carbon Removal”.
- The most highly recommended guide for holding conversations in this phase of the process is “The Mom Test”. It’s about how to ask questions in a way that even your own mother wouldn’t lie to you to protect your ego. Many friends have informed me that your mother lying you to protect your ego is a decidedly culturally-specific phenomenon.

*Author bio: Jamie Wong was an early software engineer at Figma, and is now exploring climate tech at **South Park Commons** and co-hosting the emotional communication podcast **Vulnerability Junkies**. He published an earlier version of this post on **his blog**. If you’re building at the frontier of CDR (and especially if you’re working on MRV for mCDR), please reach out. You can **subscribe to Jamie’s writing by email**, **follow him on Twitter**, take a look at **other blog posts by him**, or if you'd like to chat in a non-recruiting capacity, DM him on Twitter.*

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
