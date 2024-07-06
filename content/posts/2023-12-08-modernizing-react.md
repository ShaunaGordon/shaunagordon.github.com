---
title: "Adventures in Modernizing React"
description: "Something, something, new paradigms"
date: 2023-12-08
categories: [tech]
tags: [react, legacy code]
draft: true
---

I spent the better part of my first year at Custom Ink upgrading an Electron and React application. That was an adventure unto itself, let me tell you. It also resulted in a list of "things I need to do when my priority isn't just get this thing working again to unblock the other team." Among that list was updating the code to modern standards -- something I got to make a bunch of headway on in the second half of my second year.

I got really good at converting class-based React components to functional ones. And now, I want to document how I did it.

## Convert The Class To A Function

It sounds a bit like a tautology, but the first step in converting a class based component to a functional one is, indeed, to make the conversion.

Where we have

```js
class Foo {
```

we need to make it

```js
const Foo = () => {
```

This, of course, will promptly throw a bunch of IDE error syntax errors. That's okay, we'll fix those in the following steps. Just make sure the function is wrapping properly.

## Convert The Inner Functions 

Now that we've done the easy part, the next step is to convert all the functions to either hooks or constants. This is where it gets a bit time consuming, because it requires more understanding of the code the than simply a syntax conversion.