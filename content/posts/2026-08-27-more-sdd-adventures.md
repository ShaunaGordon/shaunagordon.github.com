---
title: "More Adventures In Spec-Driven Development"
# subtitle: ""
description: "Six Months Later"
date: 2026-08-27
categories: [tech]
tags: [ai]
---

It's been six months since I last wrote about my foray into Spec Driven Development, and eight since I started doing a lot of agentic development. I've refined my own workflow. I've tried it on a number of projects. I've even created some tooling to help bootstrap it. I also went ahead and tried Spec Kit again.

So, what have I learned?

## Let's Get Spec Kit Off My Chest

Let's start with my revisit of Spec Kit. The website claims you can build better software, faster with it.

Uh...sure...I guess. If "better" means "better than just blind prompting" and "faster" means...well, I'm not actually sure.

### It's *Heavy*

Like...holy hell is it heavy.

I feel like it's *worse* now than it was when I first tried it back at the beginning of the year, but maybe that's just a result of better understanding the intended Spec Kit process. Regardless, it's actually impressive with how heavy it is.

The heaviness starts from the moment you start using it, because you have to go through seven steps to spec out a feature, regardless of how large or small it is. You start with `/specify`, and explain what you want, which...okay. That's fine. It might ask you a few questions to refine things. Then you should run `/clarify`...because apparently the specify step doesn't fully clarify things? Then you run `/plan` and heaven forbid you don't remember anything for the clarify step at this point, because you're supposed to run it *before* plan. (Spec Kit happily runs them in either order, but I suspect it can cause all sorts of subtle issues.) Then, you run `/tasks`, which breaks the spec into tasks, which again, not too bad. I could see that being useful in some multi-agent workflows. 

Then, you're supposed to run `/analyze` which is supposed to fix any cross-document creep. This is where I found it *really* turned into a slog, because that task found a whole slew of issues that, for whatever reason, weren't enforced or were otherwise ignored in the earlier steps. Now, this can happen, but at this point, I wonder how much *Spec Kit, itself* is exacerbating this. Because now, by this point, we have most of the Markdown artifacts, which means we have some 20 thousand words in the context just for the feature, itself, and that doesn't count whatever the analyze step adds as it rewrites large swaths of the spec, uncovers more issues, rewrites more, and so on until you are either satisfied with it or so sick of it that you give up and move on to `/implement`.

Oh, and you're supposed to read all of it. Every time. Plus the report of running whatever step you're on.

Isn't tech supposed to make our lives *less* tedious?

#### Spec Kit + Big Models = Even Heavier

In my latest foray into Spec Kit, I experimented with the different models available in my Claude subscription. Spec Kit's significant ceremony and requirements to create a lot of artifacts to begin with is exacerbated by Fable and Opus's own penchant for overengineering. The result is a lot more detailed spec documents and multiple files of checklists, and a functional, but poorly engineered, minimal app.

One of the big problems with Spec Kit is that it creates a lot of spec documents, and those spec documents need to be in the context in order to work ideally. Even with Opus and Fable's mega-sized context windows, it still means a lot of information gets pushed to the top of the pile to be compacted when the context fills to capacity, and a lot of things the agent has to sift through. That means a lot of things still get dropped, most notably the foundation documents that dictate coding style and standards.

### It Ignores An Agent's Own Tooling

This is by design, but I think severely hurts what it could do. Spec Kit deliberately doesn't rely on agent-specific tooling in order to be as agnostic as possible. That's admirable, but it means tools like Claude Code have to always be in "automatic edit" mode for it to work "properly," missing out on the perks of Plan mode, and other features, like subagents. It also means plans don't show up in nice reports like what Claude can do. Instead, you get a thousand lines of Markdown across 10 or more files, all of which you're ostensibly supposed to read before approving the plan. Having gotten used to Claude's interactive plan interface, this is painful to say the least.

This is a side effect of being in the "wild west" phase of new tech. Things compete and everyone steps on everyone else's toes. Tech is obsolete almost as soon as it's in people's hands. It's the early 2000s all over again, except this time, we have factions fighting to make their own standards, even as they don't follow their own.

## So What Do I Do, Instead?

So, if I'm generally not impressed, do I have something better? Well, I have something better for me, at least. I'm still working out the kinks for multiple users (that's actually a semi-fatal flaw I've noticed with agentic development as a whole, thanks to its non-deterministic nature). Let's walk through what I've got so far.

### Foundation Docs

The Constitution is hands-down still one of the best things to come from Spec Kit. Combined with `AGENTS.md` for machines and `README.md` for humans, and sometimes a tech stack and architecture document, the Constitution forms what I call the "foundation documents." These contain the non-negotiable rules that all contributors -- agent and human alike -- must adhere to, as well as basic contextual information about the project overall. This helps the agent know what languages and other tech to use, instead of having to self-discover that information and thus, filling up its context finding out that information.

### Issues As Specs

I went into this in my [last post about SDD](2026-03-17-spec-driven-dev), and having been doing it for the past six months, I'm more convinced of its benefits, and my concerns from March haven't been assuaged. In fact, they've been reinforced. There's still no apparent remedy to spec number conflicts or my questions about collaboration (except maybe a lot of version control pushes that might trigger continuous integration). Furthermore, agents can use command-line tools, such as GitHub's `gh` CLI tool, or Gitlab's version, `glab`, so there's really no good reason not to (though I would love a way to create an identifying access token in these tools that automatically labels work done by the agent as the agent, while still linking the agent to a user, but Gitlab, at least, doesn't have that).

I've decided I prefer writing the specs, since it means I can control what goes into the spec, how detailed it is, and include any notes for specific requirements that aren't part of the feature, itself, but the agent needs to know anyway (such as style or standards reminders).

### Smaller Feature Specs

In every single project I've done, the less supervision I give the agent, the more quickly it grows fragile and falls apart, even with some kind of SDD structure. (Code quality matters, who'da thunk it?) Even before it falls apart, I start feeling like I've taken a back seat on my own project, and have a harder time controlling some of the implementation details that give an application polish. This has happened regardless of model I've used for such projects. 

Large feature specs are a *super* easy trap to fall into with something like Spec Kit, and in fact the heaviness of Spec Kit's process arguably *encourages* larger specs. Who wants to go through that process for a tiny feature? Besides, why break a feature down, when the agent can do it for you? ...Except the breaking down happens within the larger spec folder, in that situation, and the agent still implements it as all one spec. Claude Sonnet, at least, is reasonable enough to go "hey, this is a really big feature, so I'm going to stop at certain intervals for review." But it's still...not much of an improvement, at least not in the way taking time to break down features into smaller specs and handwriting the specs has been for me.

Instead, writing the specs myself naturally results in smaller, more concise documents than what agents spit out. It also means that I know *exactly* what's in the spec. Breaking them down manually requires me to get smaller with the features, making them more focused and thus, more easily reviewed. The smaller, tighter focus also gives the agent less chance of going off the rails, or overengineering things.

### Judicious Use of Skills

Nothing like automating the automation. I run a fairly lean collection of skills, but the one I use the most is my `/implement`, which is a small skill that lays out the expected process for implementing a spec issue. It allows me to simply do `/implement 123` and the skill handles the expected process.

### Work *With* the Agentic Ecosystem

Where I work, we thankfully only use one agent tooling (Claude Code), which allows us to assume availability of its features. I'll concede this might prove more challenging in a mixed agent scenario, but it works for me, at least, and it feels like I'm not fighting my tooling so much.

This means I make heavy use of Claude's "Plan" mode. For all the criticisms I have of Claude Code, I quite like its Plan mode in the VS Code plugin. Being able to highlight sections and pass that in for specific context is such a great feature, and one I immediately and greatly missed when tinkering with Spec Kit. Could it have been recreated? Possibly, but it's as much about the built-in developer/user experience of it being right there as it is about the feature itself.

I also leverage [Serena](https://oraios.github.io/serena/01-about/000_intro.html), and while Serena and Spec Kit technically co-exist side-by-side, Spec Kit's rigidity makes it hard for the agent to know when (or even that) it can use Serena.

Again, it comes back to a fundamental difference in the nuances of the problem being solved. The makers of Spec Kit are trying to create a universal solution that works for everyone, which means they can't account for everything outside their sandbox and therefore can't *allow* for anything outside their sandbox. GitHub/Microsoft are also a large enough behemoth that they can get away with expecting other tools to somehow play nice with *them* and not the other way around. As someone who prefers making tools that actively play nice with other tools (even when the tool itself is specific to a particular tool or use-case), suffice it to say, I'm not a fan of Spec Kit on this front.

### Review All Code

Small specs -> small changes -> reviewable code. It all comes back to those small specs, doesn't it?

But seriously, being able to revieew the code also means it's easier to check to make sure the code...y'know...makes sense and does what the agent claims it does. I am, after all, still responsible for the output, even if I'm not the one that typed it. Just like how I'm responsible for the output from the junior engineer I'm training.

Reviewing the output code is also a big key to keeping the system stable. It's no coincidence that my most stable agentic project is also the one I've babysat the most. Agents really love to write the same thing three different ways, and only about half the time notice when something needs to be extracted into a standalone function or class. This is especially the case when the duplicated items are in different files, especially if the other files aren't ones that the agent happened to pick up during its discovery phase. Even with foundation docs, the agent still often violates the rules of the project, and the review phase helps catch that.

## Conclusion

Agentic development clearly benefits from a structured framework, but I do believe there's a limit to the amount of structure that can be feasibly imposed, before diminishing returns set in. It's not 100% perfect (agents, like humans, sometimes just disregard some or all of the processes), but such is the nature of current agents.