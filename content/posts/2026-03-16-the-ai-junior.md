---
title: "My New, Amnesiac Intern"
subtitle: "Or, Adventures in Agentic Tooling"
description: "Hey bot, come up with a catchy title for me"
date: 2025-06-29
categories: [tech]
tags: [ai]
---

As a software engineer, I've basically been forced into the forefront of all this "AI" stuff, whether I like it or not. Naturally, I've had...uh...[quite a bit to say about it](/tags/ai/) already. Still, regardless of my opinions on the matter, the fact remains that I'm compelled to stay on top of this particular technology. And, to be honest, I do actually *want* to find that magic tool that does the stuff so many others tout it doing. So far, I've been...rather underwhelmed, but the addition of {{% abbrev MCP "Model Context Protocol" %}} and so-called "Agentic AI" have finally brought this stuff out of the chat window and into more practical use...in theory. I'm still unimpressed, but I've found, like some [others I've seen,](https://www.eric-fritz.com/articles/my-ai-junior-dev-still-needs-an-adult-in-the-room/) that it works best when I treat it like an amnesiac, but enthusiastic intern, fresh on the job.

## Llama Llama Llama

I've already written at length [about my disdain for OpenAI/Anthropic](/2025/06/29/the-hate-of-my-love/hate-of-ai/), and where I think this is all going. So naturally, I wanted to put my proverbial money where my mouth is. Besides, I wanted to see if I *could* get a viable local setup for more than just little trivial things.

When I first started my foray into local language models, I was using [Jan.ai](https://jan.ai/). It's actually a pretty solid tool for something more sandboxy. If you want a desktop version of ChatGPT and the easy ability to try out some models, Jan's not a bad choice. It's got a great community, too.

As is my general wont with...basically any tool that tries to make things easy, though, I quickly found myself bumping against its limits. This first came about when I wanted to use it to replace Github Copilot in my VS Code setup. On the VS Code side, I quickly settled into [Continue.dev](https://www.continue.dev/), thanks to how much it can be customized with text-based configs. Jan, however, proved to be too limited to be a coding agent's model server. Between being cumbersome to switch between models, lack of support for the models I was most interested in, and lack of some of the more cutting-edge features, it just wasn't working for me.

[Ollama](https://ollama.com/) to the rescue. It balances ease of use (getting new models is as simple as `ollama pull`), with powerful capabilities (tools, multi-model usage, etc) quite well. There's a reason it's one of the top local model runners.

Of course, because things change so rapidly now (cue Weird Al's [It's All About the Pentiums](https://music.apple.com/us/album/its-all-about-the-pentiums-an-adaptation-of-its/250502752?i=250502849)), I soon ran into problems with Continue (it was great for general conversation and autocomplete, but was falling short for me for actually...being an agent), and so I added [Kilo Code](https://github.com/Kilo-Org/kilocode) to my toolkit, which proved to be better at being an agent and doing the agenty things people talk about, but with local models.

(Aside: At the start of the year, work gave me a Pro subscription to Claude Code, and it's definitely noticeably more capable than my local setup. I'll get into that later.)

## Eeny, meeny, miny, model...

The next problem, of course, was...what model(s) should I use? Hugging Face has...many options. Even Ollama's curated list is pretty long.

I started with some of the usuals -- Mistral, Devstral, gemma, qwen, and even Phi. Sadly, Mistral had to be nixed pretty quickly, due to licensing (they only allow research/non-commercial use, and I wanted one that can I can potentially use on commercial work). Then, I happened across a couple others -- Cohere's Command-R, and DeepCogito's Cogito. For a time, these were my favorites. They were solid, well-trained, and came up with some good responses to what I was using them for at the time (brainstorming and asking questions about things).

It wasn't long, though, that I started pushing up against their limits, primarily when tool use became more of a thing and the tooling evolved to rely on it more. I still want to play around with Command-R for {{% abbrev RAG "Retrieval Augmented Generation" %}} purposes, but I haven't gotten that far yet (RAG is actually way more of a pain in the ass than it really seems like it ought to be). So, I started experimenting with a bunch of different models, and I found a number of things:

- Qwen models are *super* naval-gazey. Even with a larger context window, they seem to easily get into "overthinking" loops and basically end up in analysis paralysis (because I don't have to deal with that enough from the *people* in my life... 🙄 ).
- gpt-oss is a solid model and I hate that I like it (because of the whole OpenAI of it all), though seems to be hit or miss with tool calling, because apparently it's nonstandard about it. It's like the IE6 of the language model world.
- Granite4 is aptly named, given that it's about as smart as a rock. It *really* doesn't live up to the description put out for it.
- Devstral works super well with Kilo Code for code-based tasks, for the most part. It does sometimes get into fail-retry loops, though. Something, something definition of insanity...
- Continue's Instinct model is so far my favorite autocomplete model. It's purpose-built for that, which makes sense.
- Deepcoder is *slick*. Comparable capability to Devstral, without getting into loops so much (knock on wood), and while using less vRAM (which means I can give it more context size and still have vRAM left over for concurrent embedding and autocomplete models to run).
- All of this ☝️ might be wholly invalid even 6 weeks from now. Or tomorrow. Or even right now, by the time I publish this. It's the Pentium race all over again.
- I can jack up the context size pretty far on several models before I start running into my vRAM limits. 32k context size go brr. (AMD's graphics cards actually win here, if you're only getting regular retail cards and not the ones specially built for language models, because vRAM is king, and AMD gives you more vRAM for your dollar. And just...more...period.)
- The new ARM-based Macs are surprisingly good model-running machines. The way they share RAM for graphics allows them to leverage basically the full system RAM with speeds on par with vRAM. And...at the rate things are going with hardware, this might weirdly be the affordable option.

The clear winner at the moment is Deepcoder, of all models. I literally just stumbled on this one one day when Devstral kept getting stuck in loops with no discernible way to get it out, and so far, I'm relatively impressed.

Here's what its Ollama entry has to say:

> Through a joint collaboration between the Agentica team and Together AI, DeepCoder-14B-Preview is a code reasoning model finetuned from Deepseek-R1-Distilled-Qwen-14B via distributed RL.

So...Qwen -- by far one of the best open source/local reasoning models -- distilled by Deepseek's famous process, then finetuned on code and compressed to run on consumer/edge hardware by one of the leading finetuning companies. Talk about hitting a sweet spot.

Oh, and as a 14B model, as opposed to qwen3-coder being 30B and devstral at 24B, it takes less vRAM by default to run. This means I can throw more context size at it, improving its working memory.

It's all about the ~~Pentiums~~ memories, baby.

## Hey ~~Intern~~ Agent, Go...Do Something...

The next natural question, then, is... wtf do I even *do* with this thing, exactly? I've tried letting it generate code and that's been... lackluster. Maybe I'm just too damned picky after honing my craft for a couple of decades, but even if it manages to generate good code once, the weaknesses so often mentioned (solving the same problem in slightly different ways, rarely making reusable code, etc) become glaringly obvious, *very* quickly.

I've found it to be *fantastic* at writing highly-structured things like documentation blocks and OpenAPI annotations. That's probably by far my favorite use for it. If I find no other purpose for this tooling, the fact that it can do *that* makes me immensely happy and objectively saves me a ton of time, and subjectively saves me a ton of brainpower that would be wasted on the tedium of OpenAPI annotation (seriously, that's some verbose stuff).

I'm also experimenting with helping me understand and document a large, complex, legacy code base. This task is proving more challenging, and already the cracks are showing (files are named differently and thus, some work is getting duplicated, for one), but it's also a task where I already plan to do a lot of cleanup and I just need to get past "blank page syndrome" and get *something* going, as well as a task that has to be repeated over and over for every piece. The hope here is that it cuts down on that tedium, even if it doesn't *technically* cut down on time.

## The Big Lesson: Tooling Makes All The Difference

Having a good model is definitely important, don't get me wrong, but what I've found matters at least as much is the tooling *around* the model. The model can be the most capable in the world, but if the tooling doesn't know how to talk to the model, you're still dead in the water.

These days, the table stakes for agentic tooling includes skills/commands, tool use, and automatically finding/adding context (particularly for coding agents; little is more frustrating than describing what you need, adding context, and referencing files, just for the model to come back with "great! What's the document you're referring to?"). This is where Jan, Continue, and Kilo Code have all fallen flat for me at one point or another, yet Kilo Code still stood head and shoulders above the others.

### Along Came A ~~Spider~~ Claude

Remember how I said work bought me a Claude subscription? It's about here that we see the difference it makes when the tooling developer *also* controls the models. Admittedly...it's quite nice. I really can't deny they've built something truly useful. Now...if only the frontier models and the companies running them were in any way sustainable.

I've ultimately resigned myself to the fact that local LMs aren't *quite* there yet, at least not without investing stupid amounts into massively overpriced hardware (seriously, did no one learn from the crypto thing? Wait...don't answer that. I already know that Venn diagram is basically a circle).

There is *some* hope, though. Anthropic recently updated Claude Code to (ostensibly) work with local language models. I gave it a try and was...disappointed in the results. Even tool-capable models and ones supposedly designed for this work just...didn't really work. (I really dislike this pre-standards phase of things.) *However*, this is evidence of the "bring your own model" trend I've been seeing lately. Github Copilot opened up similarly a few months ago (though it's still frustratingly hostile to other models in weird ways), and someone [made an open-source clone of Claude Code](https://opencode.ai/).

## Conclusion

I still really want to work local models into my workflow somehow, because I hate that the choice right now is between "barely usable for coding" and "torch the world". What would be really nice is if I could get Claude Code to shunt the gruntwork of actually updating files off to a local model, since I have to for the moment suck it up and deal with the fact that the Claude models are just objectively more capable (being able to run a trillion parameters and have context sizes in the hundreds of thousands is a tough act to beat, let's be honest). Unfortunately, that seems to be quite a ways off still. I guess I'm stuck waiting a little longer for the landscape change I'm expecting, before more resources get put into local models.
