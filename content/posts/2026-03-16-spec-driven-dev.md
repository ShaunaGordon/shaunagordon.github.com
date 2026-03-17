---
title: "Spec-Driven Development"
# subtitle: ""
description: "Guiding the amnesiac intern"
date: 2026-03-16
categories: [tech]
tags: [ai]
---

I've recently (well..."recently," as in, three months ago at this point, but whatever) encountered Microsoft/Github's new AI development toolkit, [Spec Kit](https://speckit.org/), and the associated "Spec-Driven Development." When I first read about it, it struck me as very Waterfall-esque. Frankly, it still seems heavily so. I guess that's to be expected of something coming out of an "old guard" software company like Microsoft, really.

*However*, in this age of AI-based workflows, I think it has potential. If we're stuck with these things anyway, might as well make the best of them, right? And something I've noticed, too, is that many of these emerging "best practices" for getting beyond vibe coding toy projects...tend to be the very things many of us have been fighting tooth and nail for, for years, because as it so happens, the things needed to give AI context on something *are the same things needed to give humans context on it.* Who'da thunk it?

That human factor is honestly one of the things I appreciate the most about all of this. Even if the bubble bursts and the entire thing collapses tomorrow, if we keep workflows like "Spec-Driven Development" and the just overall better emphasis on good documentation, because we've realized it's good for the humans, too, then I call that a win.

In the meantime, I will continue to be amused at the lengths people are going to make a fundamentally non-deterministic technology more deterministic, while also seeing what I can get out of...any of this. (Because much as I dislike this whole fad for reasons I've already gone into, I'm a pragmatic person, and at the end of the day, I'm an engineer. I will forever find ways to make use of damn near anything I'm given to work with.)

## Honestly? I Like the Concept

Like I said, it has potential. I'll be entirely honest, part of it was to try to find *something* that might end up allowing me to actually get something working that's AI-driven, just to see if I can and what it would take. I have a *really* hard time believing people have actually made anything functional with little more than a handful of lines of vague instruction, unless that thing was something that had been done a million times already, giving the model a mountain of things from which to glue together its solution. I did actually try that route, just to see what would come of it, and while it works for little scripts or mini utility apps, it's very clearly not going to work for production applications, at least not without blowing through five figures worth of tokens in the process as it tries to work out what exactly to do. So far, my experience even with Claude hasn't changed that. Even with spec-driven development, I have to babysit it a lot.

And frankly? I wouldn't expect anything else. People really underestimate the sheer amount of context most production applications require. Tech debt is a thing in no small part for precisely this reason, because it's pretty much impossible to hold the entire application in one's head at once. The ceiling may or may not be higher for a computer, but it still exists. And the thing is, "context" in this scenario isn't just the code itself, it's all the decisions that went into the code and its architecture, it's all the quirks and known bugs, it's the business needs for things that haven't even been implemented yet, but which guide current planning and implementation, and so much more that a machine doesn't even really have access to (at least not unless we write a ton of -- surprise, surprise -- documentation, and it *still* pales in comparison to what the humans gather largely subconsciously).

Spec-Driven Development helps retain some of that extra context. It still can't get the longer vision stuff, but it *does* encourage better feature breakdown and description, and creates a trail of artifacts not unlike Architecture Decision Records. What I like most is the record of features that's created that not only explains *what* is made, but *why* -- and that's the crux of it all right there, why a feature is added. The Spec Kit template breaks each feature into a series of user stories that define:

- The what, in an "As a ____, I want to ____, so that I can ____" format
- Why the user story is a priority
- Independent tests, in plain words
- Acceptance scenarios for that story
- An overall Acceptance Criteria checklist that must be completed to be considered "done"

I've seen some specs go as far as describing the specific code changes, which...seems redundant, though admittedly makes for a super detailed historical record. Ironically, with the way Spec Kit works, it doesn't really matter whether it's in the spec or straight to the code, because the model is writing it all the same.

## I Am Going My Own Way, Though

Spec Kit is *verbose*. Like...kind of ridiculously so. It's super easy to tell that it was created by people who don't have to worry about usage or context limits (and for whom [AI usage is itself a KPI](https://www.windowscentral.com/microsoft/using-ai-is-no-longer-optional-did-microsoft-makes-copilot-mandatory-for-staff)), and indeed, some of the first-party tutorials talk about even using multiple models. Sorry, but not all of us can or are willing to do that (nor do I believe we should be expected to, because...holy shit, let's just burn down all the forests at once). If your employer pays for and expects exactly that, far be it from me to stop you, though. That, naturally, means doing it with local LMs is going to be inherently more challenging.

It's also *super* opinionated. You have to go through particular steps in a particular order. No doubt this works well for its creators, but it makes it quite unintuitive to add to an existing project, *especially* if you're not using the frontier models. And frankly, if you're using frontier models, you're probably using frontier model tooling, and Claude Code, at least, does a lot of it automatically at this point. All the scripts and boilerplate stuff do add some solid guardrails, though, I'll grant them that. That goes back to the lengths they're going to shore up fundamental flaws in the system, though, I think.

*So...* I did what any good engineer does -- I took the parts I liked, and I left the rest.

### Tooling Matters... Boy Howdy, Does It Matter

Surprisingly, the issue I ran into wasn't at the model level so much as at the wrapping tool level. I've found GitHub Copilot to be *super* annoying about insisting on using GPT...whatever version it sets to default, even when I've told it time and time again to *not use that one* and, instead, use my Ollama setup. Then, it burns through whatever allotment GitHub has set for the free tier, and then bitches because I've exceeded it and *still* doesn't just use my local models...despite claiming it "automatically switches to the best available model" or whatever.

No. No, it doesn't.

*Anyway...* so I for a while settled on Kilo Code for actual "agentic" stuff. Much as I like the idea of Continue, which was what I'd settled on for a time before that, it's proven to be too finicky and just plain nonfunctional in the cases I've been wanting to use it (nothing like getting told that perfectly tools-capable models...aren't). Kilo Code has its share of problems (namely with settings actually sticking), but for the most part, it works pretty well and the actual *agentic* part is pretty slick.

*Except...* there was, last I used it, a bug in Kilo Code where it doesn't run workflows except for the very first one in a new session, and only if that workflow is the very first thing. That...makes running Spec Kit...a little challenging. And by "a little challenging," I mean "basically impossible." Without functioning workflows, the model just goes completely off the rails about what it's supposed to do, and for once, it's not really the model's fault. 

Then, came Claude. I got a Claude Code subscription from work at the beginning of the year, and it has proven better on that front, but honestly? I've been underwhelmed by the workflow of Spec Kit, itself. I've fallen into my own workflow that works well for me, and has allowed me to create an application that is so far, pretty robust.

### Spec Kit Kinda Chokes on Established Repositories

Simply put, as of the time I tried it, Spec Kit works *best* when there isn't any code yet at all. Like...make the directory, init Spec Kit, open it in VSCode, write your specs out, *then* start doing code work, however that looks for you.

Trying to put it into an existing code base is a fast track to analysis paralysis as the model tries to grok how to do things. This *might* work better with frontier models, or other setups where the model can take advantage of its full context window, but I get the feeling that doing so would burn through usage tokens, so...yeah...

It's really, really, best for brand-new applications right now. The people behind it seem keen on changing that, so we'll see as time goes on.

## The Great Irony Of Spec Kit

While I like the concept of Spec-Driven Development, I *have* to laugh at the irony of what Spec Kit, itself, *is*. The real brains behind it is a collection of templates, scripts, and workflows that tell it in great and explicit detail what to do. That's...basically it. The LLM part of it is really just to fill in the templates with something that isn't *quite* so rote as regular old programmatic insertion and string interpolation. And... I mean... it does work... strictly speaking. It's just... so very much *not* what the public has been led to believe about... all of this.

Furthermore, to really make use of Spec Kit, and spec-driven development, you return to the old front-loaded project workflows like Waterfall. Everything old is new again, I guess.

I've been working on that bit, specing out one feature at a time, in detail, in an effort to keep the lessons learned from years of Agile (and Agile-adjacent) development, and avoid the pitfalls of classic Waterfall. Thats worked pretty well, all things considered.

## Anatomy of a Spec-Driven Project

Okay, so what's my method look like in practice? Well, so far...not a whole heck of a lot different from my human-only workflow, just with some artifacts that machines can read.

One of the biggest hurdles, though, is that everyone does everything differently, because we're still in that "Wild West" era of this stuff. It's the "this site is built for Internet Explorer" of the 21st century. 

Everything old is new again...again.

Thankfully, I've found some patterns that they all seem to generally follow, which helps to minimize duplication. Skills (or commands or whatever they're called today) are still something that needs tool-specific setup for now, since they all look into their own `.{AGENT}` folder for them. I might eventually figure something out.

### AGENTS.md

AGENT.md, AGENTS.md, CLAUDE.md, copilot-instructions.md, whatever the fuck you want to call it (because who needs standards in our return to the Wild West? Thankfully, they will all read AGENTS.md, or at worst can be told to read it), it's README for the machines. Now, this isn't really part of Spec Kit, as it's an independent thing that's emerged. However, it makes for a *great* entry point for the machines. I've found it works best when serving as a sort of table of contents and brief introduction. Give it an outline of the goals of the project and what tech it's using, then toss in a list of the key resources, and you're good to go. For the key resources, I include the Constitution, the `docs` or `memory` folder (naming things is hard) that I keep all such artifacts in, and the main source folder(s), so the agent can easily look up where to go for what things.

Keeping it light like this means it remains evergreen and isn't yet another thing to keep updated.

### The Constitution

I *really* like the Constitution. This is the primary governing document of the whole project, and it works for humans and machines alike. The Constitution is what sets forth the quality expectations, coding standards, best practices, performance requirements, expected workflow and contribution requirements, and other similar expectations.

The Constitution can be super involved or super concise, as long as it conveys the immutable laws of the project. Like some human Constitutions, it can be a living document, which you (not the agent, this is important) update periodically to refine the project expectations. The Constitution is meant to be updated only by humans, because it's one of the authoritative documents for the machine to follow. It is, basically, your rules for the machine. If the agent can edit it, then it loses that authority.

#### Why Not Put The Constitution in AGENTS.md?

I've seen a couple articles whose recommendations for AGENTS.md is essentially the Constitution. That's certainly a viable way of doing it, but I like the separation better. The Constitution can really be used by anyone, and arguably should be. AGENTS.md is for...well...the agents. Making AGENTS.md more like a table of contents allows the agent to decide whether it needs to review the Constitution, or any of the other documents, leveraging progressive discovery, which keeps token count and context size lean.

### Docs or Memory Folder

It's well-known by now that LLMs don't have a memory to speak of (hence the "amnesiac intern" moniker), which means it needs a way to "remember" important things. Kind of like Lucy from _50 First Dates_.

![It's Lucy's daily morning tape in "50 First Dates"](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExY21jY3Rjbm5tNnFjY2U2ZmI4bW1jeGdmNXpnam1maGJrNzFiYjg1cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S5JOaLz8Aw3s3yJRaH/giphy.gif)

That's where the memory folder comes in. I'm still working on the specific name, because some of the files are useful for humans and are arguably documentation, and when I first started it, it had the specs in it, too (more on that later), but the main purpose is for maintaining agent memory.

In practice, this folder ends up containing important notes for the agent, and any human controller, about quirks of the system (or integrations it connects to), documenting findings for otherwise undocumented code, and outlining processes that have organically emerged, but haven't yet been codified into skills or formal documentation.

This is also one of those challenging locations where every agent tool has its own idea about where to put these things. Kilo Code is nice enough to actively seek out a memory folder and use it, but Claude Code has proven...a bit more erratic. It's a case of too many options -- it keeps its own memory folders (both in the user-level `.claude` folder, and in the project level `.claude` folder), plus tools like [Serena](https://oraios.github.io/serena/01-about/000_intro.html) have their own locations in their dot folders, plus whatever you might try to set. This has happened to me even when I instruct it in the `AGENTS.md` file. I might have to try making a skill for it to more firmly reinforce it.

### The Specs

Specs are the bread and butter of the workflow, obviously. It's kind of hard to have *Spec*-Driven Development without specs.

But... if we look at [Spec Kit's spec template](https://github.com/github/spec-kit/blob/main/templates/spec-template.md) we start seeing it get super verbose. Each spec is segmented into user stories, requirements, and success criteria, but where it gets weird is that the user stories have acceptance criteria, *and* the requirements section itself is largely a list of acceptance criteria, too.

"But the agent writes that!" Sure, the agent writes it, based on the user running the `/specify` command, which means it first works through the rather vague description created from `/specify`, asks any clarifying questions it has, then writes a doc where it writes basically the same thing in triplicate. Then, it has to go back through the spec for any future passes. So if you want to further clarify it, it has to load all that up again, and again when you get to implementation (if it's been pushed out of context or a new session has been started). That all costs precious tokens and context space.

Now, maybe this works well in a bureaucracy-heavy environment, where everything is linked to KPIs or other metrics that six layers of management want to see -- in which case, this triplicate production makes a fair bit more sense -- I've found a much more concise spec, which I write myself, works just as well for the actual development.

In other words, the verbosity benefits the humans far more than it does the machines (especially when you consider that every character in those documents adds to the context and token count for the machines, *and* that [agents truncate large documents](https://dacharycarey.com/2026/02/19/agent-web-fetch-spelunking/)). The human aspect's not necessarily a *bad* thing, mind you, though one does have to wonder what humans actually *read* specs with that level of repetitive detail. My guess? Very few.

#### Enter The Issue Tracker

Another thing SDD does is put the specs into the repository. This *seems* like a good idea at first, but it very quickly becomes unwieldy. Besides, what do you do with the bugs your PM or QA person finds? Or the feature requests from users? Or anything else from any other source that isn't engineers? The specs are also supposed to be numbered, so what happens if more than one person is writing specs? What about comments from others on the expectations?

This is starting to sound an awful lot like an issue tracker to me.

So that's exactly what I did -- I set up an issue template for Gitlab (where we host our repositories at work), and whenever I create a spec, I use that template, which in turn adds the `spec` label. When I get to the implementation phase, I have a skill that instructs Claude to fetch the spec by the supplied issue number using Gitlab's CLI tool, and it can immediately start implementing.

No more numbering collisions, no more question of how to do comments or non-engineer contributions, no more split between what's in the repository and what's in the issue tracker. Even better, other issues can be refined and turned into specs without losing their internal context. *And*, it separates out those more ad-hoc agent notes from formalized process docs.

### Skills

Skills are fun. They're what help make sure the agent does certain things the same way each time. I mentioned my `/implement` skill previously. It's a pretty easy one that tells Claude to fetch the numbered skill, read it, ask clarifying questions, then implement it. It's like a process checklist for a junior engineer.

I also found myself needing Claude to create its own issues and plans. These are distinct from specs, in that Claude is making them, as opposed to a human writing them, and they're tagged with `agent-plan` accordingly. This allows me to see and refine what Claude has written, versus what I've personally crafted. This skill instructs Claude to not make issues blindly, but rather follow a process to try to ensure there isn't already an existing issue, and if there is, edit or comment as appropriate.

## Conclusion

I'm still evolving my process, but I'm finding it to be a useful tool in this new agent-based working world...even if I do still find it funny that we need to add such processes to begin with, to make it not go off the rails.
