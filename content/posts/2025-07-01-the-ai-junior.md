---
title: "My New, Amnesiac Intern"
subtitle: "Or, Adventures in Agentic AI"
description: "Hey bot, come up with a catchy title for me"
date: 2025-06-29
categories: [tech]
tags: [ai]
draft: false
---

As a software engineer, I've basically been forced into the forefront of all this AI stuff, whether I like it or not. Naturally, I've had...uh...[quite a bit to say about it](/tags/ai/) already. Still, regardless of my opinions on the matter, the fact remains that I'm compelled to stay on top of this particular technology. And, to be honest, I do actually *want* to find that magic tool that does the stuff so many others tout it doing. So far, I've been...rather underwhelmed, but the recent addition of {{% abbrev MCP "Model Context Protocol" %}} and so-called "Agentic AI" have finally brought this stuff out of the chat window and into more practical use...in theory. I'm still unimpressed, but I've found, like some [others I've seen,](https://www.eric-fritz.com/articles/my-ai-junior-dev-still-needs-an-adult-in-the-room/) that it works best when I treat it like an amnesiac intern, fresh on the job, now that I've finally nailed down the models that work best for my purposes and goals (for now).

## Llama Llama Llama
 
I've already written at length [about my disdain for OpenAI/Anthropic](/2025/06/29/the-hate-of-my-love/hate-of-ai/), and where I think this is all going. So naturally, I wanted to put my proverbial money where my mouth is. Besides, I wanted to see if I *could* get a viable local setup for more than just little trivial things.

When I first started my foray into local language models, I was using [Jan.ai](https://jan.ai/). It's actually a pretty solid tool for something more sandboxy. If you want a desktop version of ChatGPT and the easy ability to try out some models, Jan's not a bad choice. It's got a great community, too.

As is my general wont with...basically any tool that tries to make things easy, though, I quickly found myself bumping against its limits. This first came about when I wanted to use it to replace Github Copilot in my VS Code setup. On the VS Code side, I quickly settled into [Continue.dev](https://www.continue.dev/), thanks to how much it can be customized with text-based configs. Jan, however, proved to be too limited. Between being cumbersome to switch between models, lack of support for the models I was most interested in, and lack of some of the more cutting-edge features, it just wasn't working for me.

[Ollama](https://ollama.com/) to the rescue. It balances ease of use (getting new models is as simple as `ollama pull`), with powerful capabilities (tools, multi-model usage, etc).

Of course, because things change so rapidly now (cue Weird Al's [It's All About the Pentiums](https://music.apple.com/us/album/its-all-about-the-pentiums-an-adaptation-of-its/250502752?i=250502849)), I soon ran into problems with Continue (it was great for general conversation and autocomplete, but was falling short for me for actually being an agent), and so I added [Kilocode](https://github.com/Kilo-Org/kilocode) to my toolkit, which proved to be better at being an agent and doing the agenty things people talk about, but with local models.

## Eeny, meeny, miny, model...

The next problem, of course, was...what model(s) should I use? Hugging Face has...many options. Even Ollama's curated list is pretty long.

I started with some of the usuals -- Mistral, Devstral, gemma, qwen, and even Phi. Sadly, Mistral had to be nixed pretty quickly, due to licensing (they only allow research/non-commercial use, and I need one that can I can potentially use on commercial work). Then, I happened across a couple others -- Cohere's Command-R, and DeepCogito's Cogito. For a time, these were my favorites. They were solid, well-trained, and came up with some good responses to what I was using them for at the time (brainstorming and asking questions about things).

It wasn't long, though, that I started pushing up against their limits, primarily when tool use became more of a thing and the tooling evolved to rely on it more. I still want to play around with Command-R for {{% abbrev RAG "Retrieval Augmented Generation" %}} purposes, but I haven't gotten that far yet. So, I started experimenting with a bunch of different models, and I found a few things:

- Qwen models are *super* naval-gazey. Even with a larger context window, they seem to easily get into "overthinking" loops and basically end up in analysis paralysis (because I don't have to deal with that enough from the *people* in my life... 🙄 ).
- gpt-oss is a solid model and I hate that I like it (because of the whole OpenAI of it all).
- Granite4 is aptly named, given that it's about as smart as a rock. It *really* doesn't live up to the description put out for it.
- Devstral works super well with Kilocode for code-based tasks, for the most part. It does sometimes get into fail-retry loops. Something, something definition of insanity...
- Continue's Instinct model is so far my favorite autocomplete model.
- All of this ☝️ might be wholly invalid even 6 weeks from now. Or tomorrow. It's the Pentium race all over again.
- I can jack up the context size pretty far on several models before I start running into my vRAM limits. 32k context size go brr.