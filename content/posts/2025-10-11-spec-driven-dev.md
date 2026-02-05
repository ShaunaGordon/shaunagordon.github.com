(Guiding the amnesiac intern)

I've recently (well..."recently," as in, three months ago at this point, but whatever) encountered Microsoft's new AI development toolkit, [Spec Kit](https://speckit.org/), and the associated "Spec-Driven Development." When I first read about it, it struck me as very Waterfall-esque. Frankly, it still seems heavily so, at least when using Spec Kit. I guess that's to be expected of something coming out of an "old guard" software company like Microsoft, really.

*However*, in this age of AI-based workflows, I think it has potential, at least on paper. If we're stuck with these things anyway, might as well make the best of them, right? And something I've noticed, too, is that many of these emerging "best practices" for getting beyond vibe coding toy projects...tend to be the very things many of us have been fighting tooth and nail for, for years, because as it so happens, the things needed to give AI context on something *are the same things needed to give humans context on it.* Who'da thunk it?

That human factor is honestly one of the things I appreciate the most about all of this. Even if the bubble bursts and the entire thing collapses tomorrow, if we keep workflows similar to "Spec-Driven Development" and the just overall better emphasis on good documentation, because we've realized it's good for the humans, too, then I call that a win.

In the meantime, I will laugh at the lengths people are going to make a fundamentally non-deterministic technology more deterministic, while also seeing what I can get out of...any of this. (Because much as I dislike this whole fad for reasons I've already gone into, I'm a pragmatic person, and at the end of the day, I'm an engineer. I will forever find ways to make use of damn near anything I have to work with.)

## Honestly? I Kind of Like The Concept

Like I said, it has potential on paper, so I've decided to give it a try. I'll be entirely honest, part of it was to try to find *something* that might end up allowing me to actually get something working that's AI-driven, just to see if I can and what it would take. I have a *really* hard time believing people have actually made anything functional with little more than a handful of lines of vague instruction, unless that thing was something that had been done a million times already, giving the model a mountain of things from which to glue together its solution. I did actually try that route, and while it works for little scripts or mini utility apps, it's very clearly not going to work for production applications, at least not without blowing through five figures worth of tokens in the process as it tries to work out what exactly to do.

And frankly? I wouldn't expect it to. People really underestimate the sheer amount of context most production applications require. Tech debt is a thing in no small part for precisely this reason, because it's pretty much impossible to hold the entire application in one's head at once. The ceiling might be higher for a computer, but it still exists. And the thing is, "context" in this scenario isn't just the code itself, it's all the decisions that went into the code and its architecture, it's all the quirks and known bugs, it's the business needs for things that haven't even been implemented yet, but which guide current planning and implementation, and so much more that a machine doesn't even really have access to (at least not unless we write a ton of -- surprise, surprise -- documentation, and it *still* pales in comparison to what the humans gather largely subconsciously).

Spec-Driven Development helps retain some of that extra context. It still can't get the longer vision stuff, but it *does* encourage better feature breakdown and description, and creates a trail of artifacts not unlike Architecture Decision Records.

## I Am Going My Own Way, Though

Spec Kit is *verbose*. Like...kind of ridiculously so. It's super easy to tell that it was created by people who don't have to worry about usage or context limits (and for whom [AI usage is itself a KPI](https://www.windowscentral.com/microsoft/using-ai-is-no-longer-optional-did-microsoft-makes-copilot-mandatory-for-staff)), and indeed, some of the first-party tutorials talk about even using multiple models. Sorry, but not all of us can or are willing to do that (nor do I believe we should be expected to, because...holy shit, let's just burn down all the forests at once). If your employer pays for and expects exactly that, far be it from me to stop you, though.

It's also *super* opinionated. You have to go through particular steps in a particular order. No doubt this works well for its creators, but it makes it quite unintuitive to add to an existing project, *especially* if you're not using the frontier models. And frankly, if you're using frontier models, you're probably using frontier model tooling, and Claude Code, at least, does a lot of it automatically at this point. All the scripts and boilerplate stuff do add some solid guardrails, though, I'll grant them that. That goes back to the lengths they're going to shore up fundamental flaws in the system, though, I think.

*So...* I did what any good engineer does -- I took the parts I liked, and I left the rest.

### First, A Quick Note on AGENTS.md

AGENT.md, AGENTS.md, CLAUDE.md, copilot.md, whatever the fuck you want to call it (because who needs standards in our return to the Wild West? Thankfully, they will all read AGENTS.md), it's README for the machines. Now, this isn't really part of Spec Kit, as it's an independent thing that's emerged. However, it makes for a *great* entry point for the machines. I've found it works best when serving as a sort of table of contents and brief introduction. Give it an outline of the goals of the project and what tech it's using, then toss in a list of the key resources, and you're good to go. For the key resources, I include the Constitution, the `docs` folder that I keep all such artifacts in, and the main source folder(s), so the agent can easily look up where to go for what things.

Keeping it light like this means it remains evergreen and isn't yet another thing to keep updated.

### The Constitution

I *really* like the Constitution. This is the primary governing document of the whole project, and it works for humans and machines alike. The Constitution is what sets forth the quality expectations, coding standards, best practices, performance requirements, expected workflow and contribution requirements, and other similar expectations.

The Constitution can be super involved or super concise, as long as it conveys the immutable laws of the project. Like some human Constitutions, it can be a living document, which you (not the agent, this is important) update periodically to refine the project expectations.

#### Why Not Put The Constitution in AGENTS.md?

I've seen a couple articles whose recommendations for AGENTS.md is essentially the Constitution. That's certainly a viable way of doing it, but I like the separation better. The Constitution can really be used by anyone, and arguably should be. AGENTS.md is for...well...the agents. Making AGENTS.md more like a table of contents allows the agent to decide whether it needs to review the Constitution, or any of the other documents.

### The Specs

Specs are the bread and butter of the workflow, obviously. It's kind of hard to have Spec-Driven Development without specs.

But... if we look at [Spec Kit's spec template](https://github.com/github/spec-kit/blob/main/templates/spec-template.md) we start seeing it get super verbose. Each spec is segmented into user stories, requirements, and success criteria, but where it gets weird is that the user stories have acceptance criteria, *and* the requirements section itself is largely a list of acceptance criteria, too.

"But the agent writes that!" Sure, the agent writes it, based on the user running the `/specify` command, which means it first works through the rather vague description created from `/specify`, asks any clarifying questions it has, then writes a doc where it writes basically the same thing in triplicate. Then, it has to go back through the spec for any future passes. So if you want to further clarify it, it has to load all that up again, and again when you get to implementation (if it's been pushed out of context or a new session has been started). That all costs precious tokens and context space.

Now, maybe this works well in a bureaucracy-heavy environment, where everything is linked to KPIs or other metrics that six layers of management want to see -- in which case, this triplicate production makes a fair bit more sense -- I've found a much more concise spec, which I write myself, works just as well for the actual development.

In other words, the verbosity benefits the humans far more than it does the machines (especially when you consider that every character in those documents adds to the context and token count for the machines). The human aspect's not necessarily a *bad* thing, mind you, though one does have to wonder what humans actually *read* specs with that level of repetitive detail. My guess? Very few.