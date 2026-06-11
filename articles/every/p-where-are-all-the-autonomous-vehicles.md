---
title: "Where Are All the Autonomous Vehicles?"
author: "Dimi Kellari"
date: 2024-05-12
url: https://every.to/p/where-are-all-the-autonomous-vehicles
words: 1478
---

*I love publishing views that strongly disagree with my own. The Every team **thinks** **that** autonomous cars are much closer to working than most people realize, but there are very smart and informed people who feel differently. As such, I’m proud to publish this original piece by **Dimi Kellari**, in which he argues the bear case to my personally held bull. It made me reexamine my views, and I encourage you to read it with an open mind.*—*Evan Armstrong*

It was easy to spot Waymo’s employees. Their hoodies and T-shirts were adorned with an unmistakable blue-and-green “W.” I was working as a strategist at X, Alphabet’s self-styled moonshot factory, which shared an office with Waymo. We built potentially world-changing products, such as novel sensors, wildfire prediction models, and learning robots. While the work was fulfilling, some of our products never saw the light of day, let alone hit the market.

In the cafeteria, I struck up conversation with Waymo employees, peppering them with questions: When will driverless cars be everywhere? Are they actually safe? How safe do they need to be? How will they ever make money? Waymo’s cars seemed futuristic, just like the products we worked on at X, but they were already deployed for testing in the real world.

But I needed to know more. After a year at X, I found myself obsessed with the driverless future, mulling over philosophical questions about human risk and practical questions about the kind of infrastructure needed to make this a reality. Each year, more than 40,000 people die on the roads in the U.S., and many more people suffer debilitating injuries. I was drawn to the possibility of bringing something straight from science fiction into the real world—and making our roads safer for everyone.

By the end of 2019, I departed X to incubate a startup called Cavnue, which builds infrastructure, like dedicated lanes and road sensor technologies, for automated vehicles. (Until recently, I was the company’s head of systems and technology, and am still an advisor.) In the process, I spoke to nearly every autonomous vehicle (AV) startup and large automaker about their obstacles to success.

In the course of these conversations, I noticed something strange. Many companies had roadmaps that showed them, as they put it, achieving scale—running cost-effective operations in multiple locales—within the next few years. And many were struggling to operate commercially in even a single metropolitan area. It didn’t quite add up.

Five years later, I don’t believe that AV makers were disingenuous with their projections. Getting autonomous vehicles to scale isn’t as straightforward as one might think. Many misunderstood the bar of what it takes to be—and be seen as—“safe enough,” as well as the financial difficulties that come with rapidly growing these complex systems.

In the past two years, Ford has shut down the self-driving car venture Argo.ai. Meanwhile, the autonomous trucking company TuSimple exited the U.S. market, its peer Embark Trucks dropped from a $5 billion valuation and got acquired for $70 million, and General Motors’s autonomous subsidiary Cruise temporarily pulled all of its vehicles off the street. That’s not to mention the fires: Teslas have burst into flames, and a group of people in San Francisco set a Waymo vehicle on fire.

When the original investments were made in companies like Cruise, Argo, Zoox, Waymo, and others nearly a decade ago, the AV industry believed it would have been further ahead commercially by now. But the markets for these products have not yet materialized, in part because the products are not ready. For all the hoopla, autonomous cars are far from operating with true autonomy—humans are still very much involved.

What is holding us back from our driverless future? What problems still need to be solved? And when will we—as humans—feel like these cars are safe enough to drive us around?

## Three reasons why driverless cars are so delayed

Self-driving technologies were supposed to usher in an era where anyone, anywhere, had access to reliable, affordable, safe, and low-emission transportation. An era with the experience of concierge cars, convenience of ride-hailing, affordability of public transit, and far fewer fatalities on the road. That may sound like a utopian vision, but that’s what we were promised by bright-eyed evangelists in Silicon Valley and Detroit.

Companies are building out autonomous vehicles in one of two ways. Either they’re building driver-out from the get-go—they’ll launch their vehicles with high levels of autonomy—or they’re building incrementally toward self-driving. Startups such as Aurora, Cruise, Kodiak, and Waymo are in the former camp while incumbent automakers and Tesla are in the latter.

While we’re a long way from autonomous vehicle ubiquity, you can experience self-driving in the fleets of autonomous taxis, or robotaxis, deployed by companies like Waymo in select cities. If you’re lucky enough to get off the waitlist to use its app to hail one, you’ll find yourself paying a similar price to an Uber or Lyft ride. When you are in the vehicle it can feel like magic, but it typically takes far longer to get to your destination than alternatives. There are three reasons why AVs are not yet widespread:

1. The bar for safety is higher than we thought.

2. Scaling driverless cars is harder than we thought.

3. The economics of driverless cars are shaky.

Understanding these three obstacles is the key to understanding why we’re still a ways away from autonomous vehicles being a part of everyday life.

## The bar for safety is higher than we thought

Fully driverless vehicles need to pass safety cases if they are to drive in the real world. In the AV world, a safety case is self-regulated by the AV company—it’s how a company gains its own conviction about safety so as to not face liability issues with an unsafe vehicle.

Traditionally, safety evaluations have focused on identifying and fixing design faults associated with vehicle components and overall structure—airbags, brakes, and seat belts—while human drivers have been responsible for the safety of operations. This division of labor has kept the scope of safety manageable.

However, as driving tasks start becoming automated, the number of things that can go wrong is no longer bound by these design faults. There are nearly infinite scenarios to test for, many of which are uncommon but important for safety, otherwise known as edge cases. The countless nature of these events is often referred to as "the long tail" problem of autonomy.

One way to reduce the number of possible scenarios is to introduce constraints on the operational design domain (ODD)—basically, the context in which the vehicle can safely operate—and only allow it to function under certain conditions, like on certain roads, at certain times, under certain weather conditions. Within this narrow space, you can test the probability, severity, and controllability of events.

Unfortunately, the complexity of getting a vehicle to drive itself in this narrower ODD remains high. Let’s illustrate this with some simple math: Assume there is a particular event that can result in an injury or fatality, say, someone in a wheelchair chased a dog across a road. You cannot estimate how often this event happens without data: It could be once every 10,000 miles, giving it a 0.0001 percent chance of occurring on any given mile. In order to gather whether that is a fair estimate, you’ll have to travel at least 10,000 miles. For the sake of this example, let’s say you do encounter the case within 10,000 miles. If a vehicle drives eight hours a day at an average of 30 miles an hour, it would take about 42 days to encounter this edge case. Once you encounter it, you build and implement an algorithm that can safely navigate this situation. You test it in simulation and on the test track. The next step is to try it out in the real world. Statistically, it might take another 42 days to encounter the situation. It could also take less time or much, much more.

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

Excellent piece. I was expecting something a bit more optimistic - seems the best argument is that human drivers are much less safe, but that is not enough.

As a person who lives in a rust belt city with wildly variable road infrastructure, I can’t imagine how autonomous happens beyond very limited applications - no snow, quality roadways and logical traffic patterns. This is a long way away.
