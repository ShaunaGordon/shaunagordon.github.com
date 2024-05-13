---
title: "Open 3D Engine"
description: "First Impressions, Thoughts, and Diving Into The Deep End"
date: 2024-05-13
categories: [tech]
tags: [o3de, dev dive, gaming, game dev]
---

Starting a new gig is very often described as "drinking from the fire hose," and for good reason -- the primary job for a new person for the first few months is simply taking in everything about the job, the work, the people, etc.

I have proceeded to jack that up to eleven.

Why get just a new job, when I can get a new job, in an industry I've never worked in, working in a language I've never touched?!

![](https://media1.tenor.com/m/QijA5AcVhuYAAAAC/bert-kreischer-lets-do-it.gif)

## Hello, O3DE

After getting laid off, several of my once-teammates-now-friends and I were chatting and someone asked "if you could make a radical change to your career, what would you do?" I had responded that I'd love to get into gaming, namely game writing (though I know my experience as an engineer would more likely get my foot in the door in an engineering position). To which one replied with "allow me to introduce you to a friend of mine..."

A few conversations and several hours of game engine research later, and I've now become the principal engineer for an upstart game studio, and a contributor to a particular open source game engine called [Open 3D Engine, or O3DE](https://o3de.org/). We settled on it, thanks to Unity fucking with their pricing, and Unreal preparing to use their own engine-specific language for game programming, instead of the standard C# they had been using (both of which were no-gos for us).

As an engineer, I was attracted to the modular nature of it. Everything is what they call a "Gem." Each Gem is a particular feature, so the editor is a Gem, the rendering engine is a Gem, the physics engine is a Gem, the script graph, and so on and so forth. Combined with its open nature, it makes it perfect for the goal the studio has -- in addition to making games, also making a framework that makes it *easier* to make games.

For better or worse, the codebase is relatively mature, especially in comparison to the just couple of years it's been out in the wild, thanks to it being the successor to Amazon's Lumberyard, which itself was a fork of Cry Engine. (While the Cry Engine parts have been almost entirely replaced at this point, there are still numerous references to it in the source.) The whole thing is a [Ship of Theseus](https://philosophyterms.com/ship-of-theseus/) that's really quite fascinating to explore. That lineage also means that while it's nowhere near the polish of Unreal or Unity (because a bunch of parts did get completely rebuilt), it's actually got nearly all of the foundation we need, and the open source nature of it means anything it's lacking, I can (at least theoretically) include or fix, or talk to other developers to advocate for it getting fixed by others.

## The Deep ~~Sea~~ End

I'm no stranger to jumping into the proverbial deep end in my career. I've changed industries -- going from ecommerce to health tech to insur-tech to logistics tech to academia and more -- as well as languages -- picking up most of the dozen or so programming languages (and more frameworks) on the fly. For the most part, my career has consisted of fundamentally the same kinds of problems to solve: taking data from one source, massaging it to fit a destination source, sending it to that destination, listening for responses, outputting it in some fashion. That makes the industry largely irrelevant, really, beyond providing the broader context for understanding the system, and I can focus on learning the tech if I need to, while the industry knowledge kind of comes along for the ride.

That's...not the case here. The industry matters here, because the software is...kind of fundamentally different. There's still a certain amount of "take input, do stuff, output," but it takes *understanding* that input on a deeper level in order to even do *that* -- because you kind of have to know things like what the hell "frustum" and "lerp" are, or how field of view affects how a game *feels* (pro tip: if you've ever gotten sick from playing *Darksiders 2*, you've experienced this one), not to mention how these things actually translate into data and formats the computer understands. It's math *and* cinematography *and* 3D modeling *and* programming. It's really not just one industry, but like...six.

Let's just take a swan dive into the Mariana Trench, shall we?

(To be fair, this isn't by any means unique to O3DE, though I get a bit more hands-on on stuff that I might not otherwise even have access to, because I'm doing a lot of work on the engine, itself.)

## So...How's The Engine?

Overall, I love it. Maybe my lack of experience with other engines leaves me naive to how things "could" be -- and certainly, I've run into its rough edges and shortfalls enough to see where it still needs work -- but I still enjoy working with, in, and on it. So let's get into the specifics.

### Good: The Community

Like all open source projects, O3DE lives or dies by its community. A lot of people are critical about its lineage of having been owned and open-sourced by Amazon after they sunsetted Lumberyard. While a fair concern, it's largely unfounded, in my opinion. I'm by no means a fan of Amazon as a company, but they did this one right and gave it over to the Linux Foundation. This means that, while Amazon does pour a lot of resources into it, they don't control it. If they were to halt all contributions tomorrow, O3DE could still live on and Amazon couldn't suddenly [change the license](https://www.gamesradar.com/dandds-licensing-controversy-explained-heres-why-you-should-care/) or [fee structure](https://www.polygon.com/23870247/unity-engine-pricing-model-install-fee) and leave the community in the lurch.

The community members themselves, are also great. A lot of the core team worked on Lumberyard and the transition to O3DE, and then others from both big names -- including Red Hat, Meta, PopcornFX, and even Pixar(!!) -- and smaller shops and individuals have contributed and have a lot of great knowledge to share.

### Good: The Documentation

There used to be a dedicated docs team, and it really shows. Docs are always a weak point for any project, regardless of licensing, so there's always room for improvement, but the docs themselves can really get a newbie quite far, especially if they already have experience with other engines (my game developer had a bunch of "prototype" stuff going within about an hour).

For me, solid docs can make or break a complex application. So saying that I live in O3DE's documentation is quite high praise, because it means I find it a useful and valuable resource.

### Good: The Modular Architecture

Like I mentioned before, the modular architecture is what attracted me to O3DE to begin with. Everything is a Gem, even the core of the application and the rendering engine itself. This makes it very easy to swap out parts as needed (this doesn't usually happen with core parts, of course, but it can happen with the extra things quite often).

From an engineering standpoint, it also makes navigating the code *super* easy. Just find the Gem's folder in the source and edit as needed. This has made it easy (and pretty safe, since coupling between Gems is very loose) to start making code contributions.

This modularity even extends to the various parts of the editor. While there aren't really any alternative Gems for the editor right now, the possibility *is* there to build alternative editor UIs, add editor features, and more.

### Help Wanted: Realtime Particle Effects

This is a known issue. PopcornFX is officially available and O3DE is supported by them, but it is a paid solution, making for a bit of a barrier for newcomers and studios just getting started. Their licensing is quite generous, though, with a perpetual license after the first year, so it can still be an affordable option, if the potential user can swing it.

Ideally, though, there should be an open source option for particle effects, which the project doesn't yet have and has put out a call for anyone interested in taking it up.

### Needs Improvement: User Experience

Credit where it's due -- game engine editors are complex as hell, so with that in mind, it's quite solid, and when you're using the parts with the most attention paid to user experience and usability, it's quite easy to use.

Where it runs into trouble is particularly in the auxiliary tooling and self-recovery parts, forcing the user to go to the command line or edit config files in some instances. Now, *these* are pretty straightforward -- the commands are well-documented and not too complex, and the config files are simple JSON files -- but arguably, a regular user shouldn't have to resort to them to begin with. The Asset Processor could also use some UX love. Likewise, it's not uncommon to see newer users run into friction points with the interface.

Improving user experience is the Foundation's main goal for 2024, though, so major improvements in this area can be expected over the course of this year.

### Needs Improvement: Stability

Again, complex system. Even more, a complex *cross-platform* system, written in the old-school cross-platform system of C++ and a Python/Qt UI. No Electron here, thank goodness, but it also means the maintainers are responsible for juggling stability across the board, which is a difficult thing to do. Dealing with graphics cards and the low-level things games and game engines tend to do with them also adds to the juggling act.

As a result, stability can be a little hit or miss. For some, it's rock solid (and it's certainly more stable on Windows and Ubuntu, the officially-supported operating systems). For others, it might crash on startup. My game developer seems to have a knack for finding all sorts of hidden crash triggers.

## Conclusions

If it's not evident, I very much like O3DE. It has a lot of potential and has a lot of great people working on it. It's definitely not for people who want a polished, super-easy-to-use engine yet, but for anyone with some patience and willing to do some trailblazing, it has a lot going for it. With all the work being done on it, I look forward to seeing where it goes in the future. I genuinely think it has the potential to become a solid contender with Unity and Unreal and be to the game engine arena what Blender is to 3D modeling.
