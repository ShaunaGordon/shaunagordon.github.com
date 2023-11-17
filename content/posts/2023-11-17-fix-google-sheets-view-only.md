---
title: "Fixing The Google Sheets View Only Bug"
description: "I finally f*ing found it"
date: 2023-11-17
categories: [tech]
tags: [bugs]
---

Have you ever been using Google Sheets on your Android or iPhone, then suddenly find a sheet that you own stuck in read only mode? Or maybe you opened it to find a message that says "this document has changed significantly. Reload to sync," and then it goes read only?

I have. It's annoying as hell, and made yet more annoying by the fact that not a single help forum seems to acknowledge this is even an issue! I have found some half a dozen posts dating back to 2019 with the same symptoms and the same brain-dead "answers" and *none* of them actually fix the problem!

It's infuriating!

![Obligatory xkcd - Wisdom of the Ancients] (https://imgs.xkcd.com/comics/wisdom_of_the_ancients.png)

All the responses are the same (if there are responses and it's not just locked without any), I shit you not.

- You must be logged into the wrong account (...except when I know for a fact that I'm using the right account and can open other sheets on that same account)
- Ask the owner to give you edit permission (*I'm the owner!*)
- Make a copy (this technically works, but it defeats half the purpose of using Google Sheets; also, these are my D&D sheets that I load into Avrae, so it's not a tenable solution)
- Wait for it to fix itself (again, technically, but that's seemingly random and who knows how long it'll take)
- Edit it on a computer (again...sure? not helpful when I'm on the road though)

## The Stupidly Simple Solution - Clear App Data

I had this happen to me for the umpteenth time today. In the middle of editing, I get the "this has changed significantly, reload to sync" message. Pay no mind to the fact that *I'm the only person with edit permission* and I've been editing on the same device all day. Where is this message even coming from?

Now, it had been a while since I ran into it, so I tried searching to see if any solution was ever posted. Nope. Still the same old useless garbage.

But! I'm a software engineer! It's literally my job to track down stupid shit like this and figure out fixes, even when nothing is documented. And I'm angry. It's been a long day, and I just wanted to give my Ranger his feat after a hard-won fight that at multiple different points nearly saw him kidnapped or killed. I earned that edit, dammit!

So...I started poking around and playing the "what's this button do?" game. There's nothing in the app itself, since the app...you know...(rightly) assumes the owner has edit access.

However... device settings has some things: clear cache and clear app data.

And it makes sense. Randomly breaking, and more importantly, randomly _fixing_ issues tend to point to caching issues of some sort. So, I cleared the cache and restarted the app.

...except that didn't work.

Okay, fine. I didn't actually know what clearing app data would do to my Google Drive stuff, since I've never had to do it. Who knows what tedium awaited me down that path. But, I was at the point of wanting to solve this out of spite. It had been a rough day, and damnit, I wanted *something*.

So I hit the button and cleared the data.

Then, I opened Drive back up, half expecting to need to re-authenticate or something.

Lo and behold, it worked! It actually fucking worked! After two years of running into this problem just intermittently enough to piss me off, I finally found the (user-accessible) solution!

Hopefully, this will help the next poor sap who runs into this issue, and finds themselves scouring the Internet for how to solve this problem that shouldn't even be a problem to begin with.

Even if that next poor sap is future me.