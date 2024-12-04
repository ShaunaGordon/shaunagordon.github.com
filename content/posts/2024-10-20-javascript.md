---
title: "On Javascript"
description: ""
date: 2024-10-20
categories: [tech]
tags: [javascript]
draft: true
---

Not long ago, I got into a discussion with someone who vehemently and vocally dislikes Javascript. When they voiced their dislike for it, I made the mistake of asking why, then proceeded to dig myself further into the rabbit hole until we both grew tired of the conversation. I noticed, though, that a lot of their complaints seemed to (not unlike a lot of the common complaints about PHP) come largely from a place of misunderstanding the language, and it made me still want to put out there explanations for some of those complaints.

## The Floating Point "Bug"

Let's start with the most common thing used to criticize the language, which is most commonly illustrated as:

```js
0.1+0.2 == 0.3
> false
```

Contrary to popular belief, this isn't a bug at all, but a limitation in math itself that, in fact, *all* programming languages have. How Javascript handles it is actually (and ironically) the documented standard way [set forth by the IEEE](https://en.wikipedia.org/wiki/IEEE_754). Most other languages choose to be less compliant with the standard in favor of what they consider better development experience, and truncate or round the numbers to create results we'd normally expect (usually). Different languages handle this differently.

So what is this limitation? It's an incompatibility between base 10 (decimal) and base 2 (binary), combined with how computers do math, and the necessary limitations of dealing with infinitely repeating decimals.

How do you represent \({1 \over 3}\) in decimal format? In math class, it'd be \(0.\overline{3}\), or "zero point three, repeating." That's because decimal *can't* represent \({1 \over 3}\) or any other number from an equation that doesn't divide cleanly. This is the same reason your calculator will display \({2 \over 3}\) as \(0.66667\) (or however many decimal places it displays), because it picks a limit and rounds the next place accordingly. Converting between binary and decimal has the same issue, except with different (floating point) numbers. There's a whole bunch of math used to illustrate this, but I won't bore you with those details. [Wikipedia has a good explanation](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) if you're curious.