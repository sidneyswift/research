---
title: "How Resilient is the Internet?"
author: "Nikhil Mulani"
date: 2021-12-08
url: https://every.to/p/how-resilient-is-the-internet
words: 3273
---

# How Resilient is the Internet?

Recent outages test the limits of a centralized internet

December 8, 2021 Updated May 11, 2026

#### Sponsored By: Yem

If you have a paid newsletter, definitely check out Yem. We here at Every are working with them and love it! In a nutshell, Yem helps paid newsletters grow by providing effective personalized messaging. They send targeted messages with the goal of growing your email list, converting free subs to paid, and preventing cancels—which consistently drives a 5% to 15% lift in subscription revenue.

If you’re operating a paid newsletter and are interested in lifecycle email automations, send Yem a note and tell them we sent you, or sign up for a 1-month free trial here.

On October 4th, 2021, Facebook—including its subsidiaries Instagram and Whatsapp, and its authentication system used by many other companies, including Spotify and Doordash—was unavailable for hours. This system outage provided us with a glimpse of vulnerabilities that have been developing in the internet’s ever-shifting architecture over the past few decades. The phrase “the move to the cloud” is often used to refer to how the Internet has changed in recent years, but this pleasingly vague metaphor papers over a worrisome reality.

Systems as large as Facebook’s shutting down should make us concerned about the resiliency of the internet in general. When Whatsapp goes down, so does access to the only means of communication for many people in many countries. When Instagram goes down, so does the primary channel for sales and marketing for many small businesses across the world.

Between its internet access programs in developing countries and its platforms that span social, business, and community needs, the scale and scope of services offered by Facebook is now similar in functionality and criticality to those offered by the major cloud service providers, including Amazon Web Services, Microsoft Azure, and Google Cloud. The way in which so much of our online interaction now depends on a few centralized platforms has made all of us vulnerable to organizational, political, or infrastructure deficiencies that each of the companies in this small set will likely come to face, sooner or later.

This state of affairs, in which most of us depend on a layer cake of centralized service providers, is a far cry from the original design intentions of the internet’s first form as the Arpanet project, funded by the U.S. Advanced Research Projects Agency and Department of Defense in the late 1960s.

According to computer scientist David Clark, who has been involved with internet design and governance since the days of Arpanet, the following principles existed for the system’s architecture from the outset:

- Internet communication must continue despite loss of networks or gateways.
- The Internet must support multiple types of communications service.
- The Internet architecture must accommodate a variety of networks.
- The Internet architecture must permit distributed management of its resources.
- The Internet architecture must be cost effective.
- The Internet architecture must permit host attachment with a low level of effort.
- The resources used in the internet architecture must be accountable.

*From **The Design Philosophy of the DARPA Protocols** *

In the internet’s current state, point number five from David’s list seems to have superseded all other considerations for the internet’s functionality. To support increased demand for large-scale online services and high processing loads, the internet’s underlying architecture has been consolidating among a few large platform companies that can provide economies of scale and unbeatable low prices through their services.

The internet’s overall structure has turned into one where most users require a small set of the large platform companies to serve as intermediaries for communicating and connecting with other users. This compression does away with “a variety of networks” or “distributed management” and instead increases the chances that one company or country will become a point of failure in—and have unprecedented control over—our experience of the internet.

Although it seems difficult to imagine a way out of our current moment, centralization does not have to be a necessary evil in order for us to enjoy all that the internet has to offer. Governments are realizing that cloud services and application platforms are of comparable public value to national utilities, and are trying to spur domestic investments in alternative offerings to encourage more choices for consumers. At an architectural level, the growing popularity of Web3 and blockchain-based applications and platforms hints at a longer-term path towards a more resilient internet.

**The Facebook Outage**

People across the world depend on Facebook for the same reason they used to depend on town squares or malls: that’s where network effects have moved. Facebook, Instagram, WhatsApp, and Messenger have a user population of over 3.5 billion people—more than half the world’s total population.

For businesses, this is an unparalleled opportunity to advertise and sell to a global audience and hope that some small part of that audience will use the social visibility and viral effects of the platform to bring in even more potential customers. These same compounding effects have pressured individuals to adopt these services to communicate with their personal connections across the world.

The scale of the world’s growing dependence on Facebook becomes even more stunning taking into account a key part of the company’s growth strategy: bringing internet connectivity to populations that were previously without any access to it. Under initiatives such as Facebook Connectivity and Free Basics, Facebook takes on the cost of setting up wi-fi or cellular access to the internet in the hopes that newly onboarded communities will become recurring users of their products.

The result is that, for many people, Facebook has become their main access point into the internet. In fact, since Facebook moved WhatsApp onto its own private cloud in 2017 and the app became the dominant means of communication in many developing countries, it may be fair to characterize the company as something similar to a cloud services provider for the developing world.

About a third of Facebook’s user-base is now located across Asia, Africa, and South America. When Facebook experienced an outage, many people in these countries believed the entire internet had experienced a failure. In India and Brazil, small businesses which use WhatsApp as their main front of business were completely unable to operate. In conflict zones such as Afghanistan and Syria, aid workers were unable to alert each other about ongoing bombings and family members were unable to let each other know about their whereabouts.

Facebook has published a thorough post-mortem of the recent incident, but the short explanation is that employees were attempting to run a set of commands to monitor and update the configurations that define connections between internal data centers and external hubs of the corporate networks. These configurations likely contained some errors. When Facebook’s internal auditing systems detected these issues, the systems reacted by running an automated set of rules that included taking down all the connections that make up the service backbone.

The world could no longer access Facebook services—but neither could the company’s employees, whose network triage and troubleshooting tools were built to use the IP addresses and domain names that were now unavailable. It took seven long hours for Facebook engineers to visit the company’s data-centers in-person, physically reset the hardware, and debug the configuration files to once again allow their networks to become accessible.

**The Cloud**

Facebook’s disproportionate importance as an access gateway to the internet for developing countries is just one small piece of a larger pattern of the internet’s centralization. In the case of a failure for any of the major cloud services companies, like AWS or Azure, many businesses’ commercial operations would be disrupted and users would face a series of subsequent outages for each of the online services that rely on those servers.

One of the major AWS outages in 2017, which was only four hours in duration, was estimated to have cost $150M in combined revenue for the S&P 500 alone. If the operational cost to governments and small businesses were included, the number is likely much larger. Insurance marketplace Lloyd’s of London estimates that if a single major cloud service provider experienced an outage of less than a week, it would cause economic losses up to $15B. Businesses in the wholesale, retail and manufacturing sectors would be particularly hard hit and have to temporarily stop operations.

This massive liability is a result of “cascading effects,” the chain reaction of having so many intertwined online services trace their core dependencies to one of the dominant cloud service providers: Amazon Web Services, Google Cloud, Microsoft Azure, IBM and Alibaba Cloud. As of April 2021, analysts estimate that over half of all global spending on cloud services goes towards the first three companies on that list.

During the COVID-19 pandemic, people and businesses have only increased their dependence on this small set of cloud services. Microsoft estimated that we experienced two years’ worth of organizations and individuals shifting towards cloud services in the space of the first two months of the pandemic in the United States.

Each of the major application and cloud companies have become scaffolding that other organizations have to build on top of to offer their own capabilities to a meaningful audience. The result is that the internet is no longer the distributed “network of networks” it once was. Now, it is perhaps better conceived of as a teetering set of platforms orbited by smaller individual and corporate networks, which require the platforms to serve as intermediaries in any digital interaction.

* Decentralized “network-of-networks” *


*Centralized platforms*

This more centralized architecture involves a serious tradeoff in favor of convenience over resilience.

On the one hand, we can comfortably rely on the resources and expertise offered by the nearly infinite resources of these large platform companies. They are capable of developing robust server infrastructure, ensuring networks stay secure against cyber attacks, and consistently monitoring usage and maintaining scalability. If these companies did not exist, it would be a massive undertaking and a large barrier to market entry for smaller players to enter the online services sector and reach the same size of audience.

On the other hand, each of these platform companies now exerts unprecedented control over global speech and interactions—with predictably unpleasant results. And in parallel, the potential costs of a simple human error at only one application or cloud service provider have metastasized.

The seemingly innocuous cause of the Facebook outage—a configuration file containing errors—and the ensuing cost to businesses around the world, prompts one to wonder what damage an intentional cyber attack on a single cloud platform could cause. There have been very close calls in the past. The hardest part of quantifying cyber security risk is that the full extent of damage is not knowable until such a disaster actually happens.

**Balancing the Map**

As the architecture of the internet’s backbone has centralized, geographic risks surrounding internet control and usage have intensified. As of 2020, mapping out the concentration of cloud service provider data center footprints among larger scale providers (Google, AWS, Microsoft, IBM, Alibaba) shows only a few major hubs of fifteen or more data centers supporting the backbone of the internet: the eastern and western coasts of the United States, the eastern coast of China, southeast Asia and Australia.

The global spread of cloud data centers matters because internet access and company activities are largely regulated on the basis of the server infrastructure housed within a given country. A lack of regionally-located data centers implies a lack of ability for any one country to fully control how information and digital capabilities are used or transferred within its borders.Europe, Africa, the Middle East, South Asia and South America are all noticeably absent from the points on the map above. Although numerous individual data centers are scattered throughout the countries in each of these regions, none can claim to harbor a domestic cloud capability they can regulate or monitor to the extent they may desire.

To overcome this, Germany is pursuing a plan they call “cloud sovereignty” to build up a domestic cloud hub for critical sectors such as government, healthcare and auto manufacturing—but is still depending on Google to provide scalable infrastructure. In an attempt to create a similar offer for the German government, Microsoft put together a proposal that included potentially creating an entirely new operating company headquartered in Germany—but under Microsoft’s purview—to administer the new German “sovereign” cloud hub.

Meanwhile, China has been successful in fostering fully local technical capabilities to support “cloud sovereignty” within their own borders. Alibaba Cloud makes the list of globally dominant cloud service providers in part because of an intentionally restrictive regulatory environment for foreign entrants hoping to build cloud capabilities in China. Foreign companies such as Amazon or Google are not allowed to fully own and operate data centers in China, which means they must contract locally to set up a cloud capability.

If foreign cloud providers do set up service in China, their service is compromised by all traffic having to traverse the national firewall used to censor communications. Azure’s handbook for cloud service customers calls this out, noting that “network latency between China and the rest of the world is inevitable, because of the intermediary technologies that regulate cross-border internet traffic.” China’s strategy of walling off their national network has resulted in greater than half of the country’s public cloud spend going towards domestic businesses like Alibaba Cloud.

Countries and regions can be strategic about fostering internet infrastructure capabilities within their borders, but often still find themselves reliant on the globally dominant providers. It is very difficult to create scaled capabilities without talent and knowledge that comes from employees at those companies. China and the United States are the only two countries where most of the cloud services offered in-country are coming from companies also headquartered in that same country.

**“Redistributing” the Internet**

The internet’s increasingly centralized architecture and inequitable global spread of infrastructure begs the question: how do we get back to the original goal of “distributed management” of the internet’s architecture? Each country building its own domestic cloud capabilities might mitigate but does not fully solve the problem of decentralizing, since users will still depend on centralized applications that use the large-scale cloud platforms.

The problem of decentralization can not be solved at the policy or software levels alone. It will have to involve a rewiring of the internet’s architecture: a willful, society-wide detachment from the large centralized platforms. We already see signs that popular sentiment is shifting away from these platforms and towards alternatives. The full shift will likely only happen if the market can offer a greater variety of applications and infrastructure services that are easy, pleasing to use, and offer a path towards avoiding the problems of over-centralization.

Web3 capabilities hint at one such architectural solution. While the internet has evolved towards a set of core centralized services provided by large corporations, Web3 imagines replacing these with decentralized and peer-to-peer networks built on top of the blockchain. If we attempt to summarize a list of Web3 principles, like David Clark did for the original “Web1” of Arpanet, it might look something like this:

- Distributed ownership, through token/currency systems or democratization of creating network infrastructure.
- Distributed governance, through architectural decisions can be voted on by all who build, use, or own pieces of the network.
- Stakeholder transparency, through open-source architectures and more accessible and participatory forms of organizational decision-making (such as DAOs).

If the principles of Web3 are extended to the internet as a whole, it would mean that no single organization or server should necessarily be required as an intermediary for exchanges of bits and bytes. But if blockchain capabilities do find their way to core internet architecture, it will be a long journey. Most users of distributed networks like Bitcoin and Ethereum still access them by way of websites, apps, and devices that rely on the major application and cloud platforms.

Although still in its early days, the Web3 ethos looks to be centered around aligning incentives between each of the participants on the network—users, builders, and investors—with hopes of creating a freer, more reliable, and more trustworthy architectural backbone for the internet.

Web3 principles still have a long way to go to prove their robustness. It will be a tricky endeavor to create global-scale systems that meet the spirit of the above principles but do not end up either restricted by government regulation or dominated by wealthy individuals and organizations who could corner ownership stakes.

If we take a look at the distribution of nodes underpinning the Bitcoin and Ethereum networks, we see some of the same challenges of inequitable distribution but also much more room to hope for change. As of December 4th, Ethereum is running on 2,273 nodes—but about 75% of those are located in the U.S., Germany, Canada, and the United Kingdom. Bitcoin is running on 14,868 nodes—the U.S. and Germany still lead in node count, but there is a more names of European and Asian countries appearing in the trailing count than for Ethereum (with the caveat that the location of a little over half of the Bitcoin nodes is indeterminate).

*Map above shows concentration of reachable Bitcoin nodes found in countries around the world as of Dec. 4, from*

*Bitnodes.io*

Bitcoin has been around since 2009, so the network has had much longer than Ethereum’s to gain popularity. It is a promising sign for DeFi that the trend for growth in such decentralized networks looks to be towards greater spread rather than greater concentration. The barrier to entry for setting up a node or mining rig is much lower for individuals and organizations than it would be to build a cloud data center.

Some groups are starting to rebuild many base layer cloud infrastructure capabilities to be based on Web3 principles. Solutions such as Storj and Filecoin aim at decentralizing cloud storage (competing with Amazon S3), while protocols like IPFS and Handshake aim at decentralizing the domain name system and the methods by which we access online content. At the application layer, projects like Mastodon and urbit offer social and personal computing capabilities in a more decentralized form. Each of these platforms aims to build entirely new networks consisting of the nodes that participants will set up. However, the reality is that many of these platforms will likely depend on gatekeepers and server hosts like AWS in order to run their own infrastructure for some time to come.

Just as it took decades for us to reach a place where a few large companies dominate the architecture of the internet, it will likely take decades to reach a place where they no longer have the hold they now exert. Web3 will very likely not be the final form of the constantly mutating internet, but it will hopefully be a large step in a more resilient direction. Eventually, perhaps, we can truthfully say we have once again managed to “permit distributed management of resources,” “accommodate a variety of networks,” “support multiple types of communications services”—and have come full circle in meeting the original design principles of the internet.

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
