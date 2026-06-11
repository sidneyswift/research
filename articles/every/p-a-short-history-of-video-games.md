---
title: "A Short History of Video Games"
author: "Anna-Sofia Lesiv"
date: 2024-01-08
url: https://every.to/p/a-short-history-of-video-games
words: 3702
---

# A Short History of Video Games

How the gaming industry paved the way for tech

January 8, 2024 Updated December 17, 2025

*Whenever Anna-Sofia Lesiv publishes a new piece, we know we’re going to learn something new. As a writer at Contrary Capital, she publishes incredible deep dives into a wide variety of technical industries, across software, hardware, and deep tech. Her latest is about the innovations behind video games, an industry whose cutting-edge technologies have had a major impact on computing as a whole. This piece demonstrates that there’s a lot to learn about how different sectors of technology interact with—and influence—another. —**Kate** *

Video games are one of the world’s newest art forms. But even though they’re visually stunning and technically challenging, they lack the prestige bestowed on art forms such as film or literature.

This is a shame—what is required to produce a virtual world is nothing short of miraculous. Video game technologies involve mathematics, physics, and, of course, an intimate familiarity with computer hardware. That’s not to mention the layers of artistry involved in game visuals, narrative architecture, and gameplay design itself.

Video games are more capable of expanding the human experience than any other medium. They can deliver perspectives and sensations achievable only within a game’s virtual environment. To do so, game developers not only leverage the bleeding edge of computing but in many cases push that edge out themselves.

From the very beginning, the gaming industry has lifted the tide for the computing industry, developing bleeding-edge technologies that have major impacts elsewhere—for example, GPUs. In this piece I’ll highlight some of the terrific achievements, across both hardware and software, that were brought about thanks to the gaming industry.

## The latest and greatest in gaming

The gaming industry is truly enormous: Within the United States, video games generated an annual revenue of nearly $100 billion, while globally the industry rakes in more than twice as much. This makes the global gaming industry five times bigger than Hollywood, bigger than the film and music industries combined.

Behind the production of many games are teams of dozens of engineers and artists who often work for years before release. Many games produced by top game studios, referred to as “triple-A studios,” often have production budgets in the tens of millions of dollars. And some forthcoming games could spend orders of magnitude more than that. Recently, rumors have circulated that *Call of Duty: Modern Warfare 3* could end up spending $1 billion on production.

All this investment and talent has produced a truly remarkable technology—game engines capable of producing real-time simulations of the world that have found tremendous relevance outside of just games. These are the operating systems of the game world. Everyone from commercial pilots to budding surgeons and architects are turning to simulations to train and practice their craft. The use case has even made it into popular media, like in the 2023 film *Gran Turismo*, which documents how a pro-gamer skilled at virtual racing games was able to transfer his skills directly into actual racing.

*Source: *Unreal Engine*.*

As game engines become more realistic—like *Unreal Engine 5*, which stunned the world with its ability to achieve real-time photorealistic graphics renders—the ability to transfer skills between virtual and physical realms will likely accelerate.

To truly appreciate what will be required to continue improving the quality of such simulators, let’s take a look at the scope of the technical work required to produce a game engine.

## What’s inside a game engine

The majority of two- or three-dimensional games are real-time interactive simulations. This means they take place in a virtual world that must be generated and updated in real time.

Games that strive for a high degree of realism, like modern first-person shooters, come with many considerations. They must, for example, adhere to the laws of real-world physics and light.

The game must then update these aspects at speeds that mimic reality. For most realistic games, this means the screen must be updated *at least* 24 times per second to give the illusion of motion. And because most screens have refresh rates at 30 or 60 Hz, meaning they refresh 30 or 60 times per second, the state updates need to happen even faster than that.

The game engine manages all of this. It continuously updates and re-renders the game world over and over again.

In the early days of gaming, when most video games were 8-bit platformers like the *Mario Bros.*, the logic for these considerations could be coded from scratch with each new game. The original *Mario Bros.* had something like 22,000 lines of code. Even by 1994, game developer Chris Sawyer spent two years coding the game *Roller Coaster Tycoon* almost entirely in assembly code.

As hardware improved and visuals became more complex, coding all the physics and rendering logic from scratch became a massive undertaking. Instead of reinventing the wheel each time, game developers began producing game engines—programs with much of the required game logic pre-established, making it easy for game designers to build unique games on top.

Today, the largest state-of-the-art game engines comprise millions of lines of code. *Unreal Engine 5*, which takes up around 115 GB, is estimated to have up to 16 million lines—and that’s *just *the engine that runs the game logic. And modern games like *Mass Effect*, *BioShock*, *Gears of War*, and *Fortnite* are built on top of *Unreal Engine*, each comprising hundreds of thousands or millions of lines more.

Game engines are massive and have many moving parts, but there are a few key subsystems that take on the bulk of the work—the gameplay foundation layer, the physics simulator and collision system, and the rendering engine.

*Source: Run time game engine architecture, **Jason Gregory**.*

## Gameplay foundations dictate what happens

The gameplay foundations layer executes game-specific logic. It’s what dictates *what actually happens* in the game, the flow of events, and the game-specific rules.

Essentially, this layer is the UX of the game. It keeps track of game objects from the background scenes and geometries, as well as dynamic objects like chairs, cans, roadside rocks, playable characters, and non-playable characters. It also handles the event system, which determines how and when these different objects interact within the game.

By the 2010s, the average video game had something like 10,000 active gameplay objects to track and update, not to mention the 5-10 other objects that these active objects would touch. This amounts to a lot of compute—and yet, it’s only a tiny fraction of the computation done by parts of the game engine like the physics simulator.

## Physics systems govern how objects interact

The physics system is one of the core parts of the game engine. It contains many of the physical laws that govern the real world—everything from gravity’s rate of acceleration to Newton’s laws of motion. It handles the positions of objects based on how quickly they are moving. This means it must keep track of object velocities and constantly update their locations.

More importantly—and perhaps most critical to gameplay—the physics simulator handles what happens when two objects collide. Now, it’s already challenging to determine when objects are colliding. Most game object models, like humanoid players, are complex figures made up of many different tiny surfaces. That means it would be even more intensive to discern whether any of those surfaces are intersecting with another object, like a bullet or a wall. As a result, most games simplify object models to more basic shapes, like boxes. This limits the surfaces the collision system needs to keep track of—to some extent.

*Source: Hitboxes, **Technotification*.

Some of the most clever optimization schemes in computer history have emerged from figuring out how to do these calculations efficiently. One such optimization was devised by the legendary programmer John Carmack in 1996, while building the game *Quake*.

Rather than check whether *every* surface was intersecting with another one, Carmack decided to split the game space into sections stored in a binary tree. This way, he would only need to check the surfaces closest to active gameplay. When one of those surfaces was impacted, you could easily traverse up the tree and check whether other nearby surfaces should be impacted too. The illustration below shows how *Quake* represented its first level in a binary space partitioned tree.

*Source: **Matt’s Ramblings**.*

This is only a fraction of the considerations that go into the physics engine. Once you detect a collision, physics systems need to determine how objects respond: Do they fly off, break, or bounce off? It depends on their weight, friction, or bounciness. The physics simulator renders the mechanics of an entire virtual world. Yet, even this is not the main workhorse of the game engine.

## Rendering engines generate game visuals

The most computationally intensive subsystem of the game engine is the rendering engine, which is responsible for generating the game’s visuals in real-time. It is very difficult to simulate how objects look, especially visually complicated three-dimensional ones.

The human eye is able to see through a unique process. The cones in the backs of our eyes detect the frequencies of billions of photons bouncing around our surroundings and into our retinas. It’s the refractions of a countless number of visible light rays that allow us to see and distinguish light from shadow, allowing us to make out objects in three dimensions. In fact, this process is so computationally intense that studies show roughly half of the brain’s cortex is engaged in visual processing.

How do you mimic this process on a computer? The answer to this question was even more difficult in the early 1990s, when computers had only a couple dozen megabytes of RAM.

In order to copy exactly what light does, we would have to project a number of light rays per screen pixel onto a virtualized 3D model and observe how each bounces between surfaces to produce the full range of light effects—highlights, shadows, indirect light, and diffuse light. This would be computationally expensive.

*Source: **Nvidia**.*

Even so, graphics pioneers like J. Turner Whitehead were working on algorithms for photorealistic computer graphics as early as the 1980s. He had his computer slowly trace individual sun rays to determine exactly how much each screen pixel should be illuminated. In 1980, it took Whitehead 74 minutes to render the image below.

*Source: **Nvidia**.*

In practice, the algorithm was nowhere near feasible for games that required real-time rendering.

Instead, the graphics industry looked for ways to simplify. Rather than pursuing ray tracing, the industry developed a method called rasterization. Rasterization was an exercise in perspective projection. Three-dimensional objects in a perspective field were given a measure of depth relative to a virtual camera lens. Then, the rasterization algorithm would determine which pixels to shade in to indicate the presence of a plane and which to leave blank.

*Source: **USC**.*

Rasterization was capable of drawing basic shapes of an object relative to a particular point of view. However, to account for the impact of light and shadows, which help further build out the three-dimensional nature of objects, a series of other clever algorithms was developed to help approximate how light would scatter objects. Techniques like Lambertian shading or Phong shading estimated where highlights and shadows should be added based on the planes of that object and the direction of the light source. These algorithms weren’t calculating individual rays—instead, they were outputting an approximation of how a lit object should look on average.

*Source: **HappieCat**.*

While approximating algorithms like these were *still* too computationally complex to run in real time in the 1990s, those with more time on their hands, like animated movie studios, could employ them to render films. The first successful 3D animated movie was *Toy Story*, produced in 1995. It was rendered using Pixar’s proprietary rendering engine called RenderMan, which didn’t have ray tracing and used rasterization techniques. The film, which had over 114,240 frames, took 800,000 machine hours to render. In total, it took 117 computers running 24 hours per day to render less than 30 seconds of the film per day.

Graphics cards changed all of this for the better. Though graphics-specific chips had previously existed, Nvidia popularized the “graphics processing unit,” or GPU, when it released its GeForce 256 chip in 1999.

Matrix multiplications are required to do rendering. In a computer, 3D objects are modeled from a series of triangles. The vertices of these triangles are encoded in a matrix, which describes the shape of the object. Orienting the object in the game world involves multiplying the object matrix with a matrix of coordinates that describes its location in the virtual game space.

*Source: **Polygon mesh**.*

From there, perspective projection, which turns 3D models into two-dimensional views, requires another series of matrix multiplications. Additionally, shading algorithms account for even more matrix multiplication.

*Source:*

*Research Gate*

*.*

Lucky for Nvidia, GPUs were specifically designed to do exactly these calculations extremely efficiently. And it was a happy coincidence that creating chips optimized for matrix multiplication would one day prove incredibly useful for the field of artificial intelligence.

The proliferation and increasing power of GPUs created a boom for computer graphics. By 2006, *Unreal Engine 3* was capable of rendering up to 5,000 visible objects in a frame, which required around 500 GFLOPs—5 billion floating point operations per second—to do so.

The algorithms and math needed to produce true-to-life photorealistic graphics were established. The only thing the graphics and gaming industry needed was more compute.

In 2018, Nvidia changed the computer graphics industry forever when it released its RTX card, a GPU designed specifically for ray tracing. GPU hardware was getting so powerful that the earlier algorithms invented to cut corners and simulate the effects of light were not needed anymore. Chips were getting so powerful that you could illuminate a scene by literally tracing through the entire refractive pathways of up to four light rays *per pixel in real time.*

Today, this allows modern computer graphics to achieve stunning levels of photorealism. Renders produced using *Unreal Engine 5* can now depict light glimmering in real-time in complex scenes of dense foliage in high definition. At times, computer-generated renders of humans appear indistinguishable from photos.

*Source: **TechPowerUp**.*

## A very brief history of gaming

It’s astonishing just how far gaming capabilities have come since 1961, when the first-ever computer game *Spacewar *was launched. It was produced by MIT student Steve Russell, who benefited from the university’s access to one of the first computers on the market, a DEC PDP-1. It took Russell six months to code this two-player shooting game, in which each player has command of a spaceship that seeks to obliterate the other. (You can still play an emulation of the game.)

*Source: **Spacewar!*

While the game was a hit with students and eventually spread to other universities over the ARPAnet, computing hardware was prohibitively expensive at the time. PDP-1s cost roughly $120,000 each in the 1960s. Sadly, they, alongside *Spacewar, *were confined to the annals of history.

Instead, it was the legacy of *Spacewar* that lived on. Nolan Bushnell was a student lucky enough to play *Spacewar* at a rival university. Between 1962 and 1968, Bushnell was studying engineering at the University of Utah when he fell in love with the possibilities of computer games. Bushnell started the company Atari in June 1972, which was devoted specifically to making gaming consoles. Atari’s first game *Pong*, which required its own hardware to play, was a smash hit in the United States, selling 150,000 units in 1975. By 1977, Atari had released the Atari 2600 console, which could play up to nine games. It brought game console hardware into Americans’ living rooms, and it made Bushnell a millionaire (a fortune he later used to start the Chuck E. Cheese empire, but that’s a story for another time).

Atari’s consoles were such a success that they became a platform for third-party game creators, who started coding games that could run on Atari’s infrastructure. Four of Atari’s game developers left the company in 1979 to form their own game studio, which they called Activision. Atari let Activision make games for the Atari console as long as Atari retained rights to royalties earned from Activision’s sales—a model still common in the game industry today.

Much to the chagrin of console makers in the late eighties, an unexpected competitor entered the gaming landscape—the personal computer. Thanks to the scaling effects of Moore’s Law, computers were getting more powerful each year. They had more than enough computational power to reproduce many of the games that required consoles in the past.

In the wake of this shift, a number of engineers saw the incredible opportunity opening up in gaming. One of the most consequential organizations that made this leap was id Software. Like many great early tech companies, the early id Software team was formed in 1991 after the game development team at Softdisk quit.

Led by the brilliant John Carmack, the team produced a number of hits, including *Commander Keen*, a PC-native version of *Mario Bros.*, and *Wolfenstein 3D*, the first 3D first-person shooter game. The latter was a revolutionary format at the time and represented an impressive technical achievement. At a time of limited memory and processing speeds, id Software created a fast-paced shooter game played from the perspective of the shooter. Frames changed fluidly as the character moved around the game arena, producing one of the first truly immersive games on the market.

*Source: **PlayDOSGames**.*

Id Software doubled down on the success of its shooter game format. In 1993, the company released *Doom*. To this day, *Doom* and its sequels continue to enjoy an avid fanbase, many of whom recognize its role as the progenitor of classic modern shooters like *Modern Warfare* and *Halo*. This same team of video game pioneers cemented their impact on the video game industry when they produced *Quake*, the first-ever game engine, later used to build out the *Quake* series.

*Source: **The Escapist**.*

## The future of gaming

Gaming has humble origins. Given this fact, it’s stunning to consider how realistic and immersive games have become—and how they’ll continue to advance. If improvements in hardware are any indication, the coming wave of realism and immersion will be profound.

In 2016, Tim Sweeney, the founder of Epic Games and producer of *Unreal Engine*, predicted that real-time photorealistic graphics would be achievable when GPUs could do 40TFLOPS, or 40 trillion floating points operations per second. In 2022, Nvidia released its most powerful GPU yet—the Hopper—capable of doing 4PFLOPS, 4 quadrillion floating point operations per second, 100,000 times the power Tim Sweeney claimed he’d need for photorealism.

And that’s not even the end of the story. Nvidia has developed further techniques to improve the performance of game time renders. One of these is known as DLSS, or deep learning super sampling technology. This technique leverages artificial intelligence to help boost the performance of rendering engines by requiring the render to compute only *one* out of every eight pixels on the screen. The remaining seven pixels can be inferred by the software.

As the hardware becomes more powerful, new techniques are simultaneously being released to supercharge rendering capability *even *further. We’re approaching a point where path tracing, a technique that traces the paths of hundreds to *thousands* of light rays per pixel, can be feasible in *real time *game play.

The wrinkle here is that the massive GPUs required are expensive. Most consoles and even the top gaming computers don’t have access to this kind of hardware. Many gaming companies are now opting to use cloud-based computing to render real-time gameplay and stream it to players’ consoles or devices. It’s a less decentralized form of gameplay that some avid gamers are growing frustrated with—it means that gameplay becomes impossible without an internet connection.

Another fascinating frontier for gaming will be found in virtual reality. In 2023, Apple announced the forthcoming release of the Apple Vision Pro, which represented a significant step forward for virtual reality headsets. Already, game engine producers like *Unreal* are exploring how its engine might run on the Vision Pro.

However, hosting games on a fully immersive visual headset still comes with many challenges. Gameplay rendering will need to be refactored to accommodate a headset device that will need to render not one but* two *views for the player—one for each eye. And though the hardware specs on the Vision Pro are impressive, they are still less powerful than the state-of-the-art technology used to render the photorealistic graphics top gamers are used to. Offline compute for gaming could be a solution to some of these problems. Even so, the move to more constrained hardware specifications will present a new set of very interesting problems for programmers.

Computer games are still a new medium. They’ve only been around since the 1960s. Yet they’ve already had a transformative impact and become the largest source of global entertainment, eclipsing even music and film. Games have also become among the most powerful expressive mediums. They can manipulate a large number of variables to enhance a player’s experience—everything from how players experience time and space to images and sounds.

We are nowhere near exhausting the full potential of the video game medium. With more time and artistry from game designers, we will reach even deeper levels of immersion and more profound virtual experiences. When that happens, the gaming industry will lift the tide for the entire industry of computing, as it has done since the very beginning.

*Anna-Sofia Lesiv is a writer at venture capital firm **Contrary**, where she originally published **this piece**. She graduated from Stanford with a degree in economics and has worked at Bridgewater, Founders Fund, and 8VC.*

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
