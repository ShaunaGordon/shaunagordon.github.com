---
title: "On Javascript"
description: ""
date: 2024-10-20
categories: [tech]
tags: [javascript]
draft: true
---

Not long ago, I got into a discussion with someone who vehemently and vocally disliked Javascript. When they voiced their dislike for it, I made the mistake of asking why, then proceeded to dig myself further into the rabbit hole until we both grew tired of the conversation. I noticed, though, that a lot of their complaints seemed to (not unlike a lot of the common complaints about PHP) come largely from a place of misunderstanding the language, and it made me still want to write about what was behind those things they complained about.

## The Floating Point "Bug"

Let's start with the most common thing used to criticize the language, which is most commonly illustrated as:

```js
0.1+0.2 == 0.3
> false
```

Contrary to popular belief, this isn't a bug at all (at least not in the usual sense), but a limitation of digital calculating of math itself that, in fact, *all* programming languages have. How Javascript handles it is actually (and ironically) the documented standard way [set forth by the IEEE](https://en.wikipedia.org/wiki/IEEE_754). Most other languages choose to be less compliant with the standard in favor of what they consider better developer experience, and truncate or round the numbers to create results we'd normally expect (usually). Different languages handle the details of this differently, but the result is typically the same: `0.1+0.2 == 0.3 -> true`.

So what is this limitation? It's an incompatibility between base 10 (decimal) and base 2 (binary), combined with how computers do math, and the necessary limitations of dealing with infinitely repeating decimals.

How do you represent \({1 \over 3}\) in decimal format? In math class, it'd be \(0.\overline{3}\), or "zero point three, repeating." That's because decimal *can't* precisely represent \({1 \over 3}\) or any other number from an equation that doesn't divide cleanly. This is the same reason your calculator will display \({2 \over 3}\) as \(0.66667\) (or however many decimal places it displays), because it picks a limit and rounds the next place accordingly. Converting between binary and decimal has the same issue, except with different (floating point) numbers. There's a whole bunch of math used to illustrate this, but I won't bore you with those details. [Wikipedia has a good explanation](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) if you're curious.

## JavaScript Often Fails in Silent Ways Instead of Crashing

This is another one I've run into off and on, and was one the person I was talking to got particularly stuck on, since they worked primarily in server side and other controlled-runtime environments. This was also the underlying thing that led to basically all the rest of his criticisms of the language, particularly relating to math.

History time! Well, history and still current events, really.

### Array.sort "Can't" Sort Numbers Properly

(It can, just has a naive default that runs counter to numeric sorting -- it converts to strings and sorts alphabetically, because converting to strings preserves data. Also talk about how Python handles sorting.)

### `NaN % 2 !== 0` -> `true`

Also - `'abc' % 2 !== 0` -> `true` (basically, anything that isn't a number and can't be coerced into a number results in the same thing)

(He expected this to throw an exception (presumably type mismatch), but it's a case where JS fails gracefully rather than crashing. He claimed it was nonsensical, but...it actually isn't. `!==` is strong comparison and requires the left and right sides to also be the same type as well as equal. both `'abc' % 2` and `NaN % 2` return `NaN`, and `NaN`...is neither `0` nor the same data type...)

## The LeftPad Debacle

(Weakness of centralizd package repository, not language)
