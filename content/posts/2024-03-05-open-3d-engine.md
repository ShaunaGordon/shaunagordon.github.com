---
title: "Open 3D Engine"
description: "First Impressions, Thoughts, and Diving Into The Deep End"
date: 2024-03-05
categories: [tech]
tags: [o3de, dev dive, gaming, game dev]
draft: true
---

Starting a new gig is very often described as "drinking from the fire hose," and for good reason -- the primary job for a new person for the first few months is simply taking in everything about the job, the work, the people, etc.

I have proceeded to jack that up to eleven.

Why get just a new job, when I can get a new job, in an industry I've never worked in, working in a language I've never touched?!

![](https://media1.tenor.com/m/QijA5AcVhuYAAAAC/bert-kreischer-lets-do-it.gif)

## Hello, O3DE

After getting laid off, several of my once-teammates-now-friends and I were chatting and someone asked "if you could make a radical change to your career, what would you do?" I had responded that I'd love to get into gaming, namely game writing (though I know my experience as an engineer would more likely get my foot in the door that way). To which one replied with "allow me to introduce you to a friend of mine..."

A few conversations and several hours of game engine research later, and I've now become the principal engineer for an upstart game studio, and a contributor to a particular open source game engine called [Open 3D Engine, or O3DE](https://o3de.org/). We settled on it, thanks to Unity fucking with their pricing, and Unreal preparing to use their own engine-specific language for game programming, instead of the standard C# they had been using.

As an engineer, I was attracted to the modular nature of it. Everything is what they call a "Gem." Each Gem is a particular feature, so the editor is a Gem, the rendering engine is a Gem, the physics engine is a Gem, the script graph, and so on and so forth. Combined with its open nature, it makes it perfect for the goal the studio has -- in addition to making games, also making a framework that makes it *easier* to make games.

For better or worse, the codebase is relatively mature, especially in comparison to the just couple of years it's been out in the wild, thanks to it being the successor to Amazon's Lumberyard, which itself was a fork of Cry Engine. (While the Cry Engine parts have been almost entirely replaced at this point, there are still numerous references to it in the source.) The whole thing is a [Ship of Theseus](https://philosophyterms.com/ship-of-theseus/) that's really quite fascinating to explore. That lineage also means that while it's nowhere near the polish of Unreal or Unity, it's actually got most of the foundation we need, and the open source nature of it means anything it's lacking, I can (at least theoretically) include or fix.

## The ~~Deep~~ Diving Board End

I'm no stranger to jumping into the proverbial deep end in my career. I've changed industries -- going from ecommerce to health tech to insur-tech to logistics tech to academia and more -- as well as languages -- picking up most of the dozen or so programming languages (and more frameworks) on the fly. For the most part, my career has consisteded of fundamentally the same kinds of problems to solve: taking data from one source, massaging it to fit a destination source, sending it to that destination, listening for responses, outputting it in some fashion. That makes the industry largely irrelevant, really, beyond providing the broader context for understanding the system, and I can focus on learning the tech if I need to and the industry knowledge kind of comes along for the ride.

That's...not the case here. The industry matters here, because the software is...kind of fundamentally different. There's still a certain amount of "take input, do stuff, output," but
