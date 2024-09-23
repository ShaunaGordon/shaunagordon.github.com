---
title: "Adventures in Modernizing React"
description: "Something, something, new paradigms"
date: 2024-09-08
categories: [tech]
tags: [react, legacy code]
draft: true
---

I spent the better part of my first year at Custom Ink upgrading an Electron and React application. That was an adventure unto itself, let me tell you. It also resulted in a list of "things I need to do when my priority isn't just get this thing working again to unblock the other team." Among that list was updating the code to modern standards -- something I got to make a bunch of headway on in the second half of my second year.

I got really good at converting class-based React components to functional ones. And now, I want to document how I did it, because there are always legacy apps to update.

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



## Return the Template

## Convert The Inner Functions 

Now that we've done the easy part, the next step is to convert all the functions to either hooks or constants. This is where it gets a bit time consuming, because it requires more understanding of the code the than simply a syntax conversion.

### Functions To Constants

Converting functions to constants is primarily for functions that aren't used for reactivity. 

### Functions to Hooks

## Convert or Remove Variables

Class-based components often use a lot of `this` and `this.props` type references when referencing class variables. These are no longer needed, because of how function based components work. The context usually communicated with `this` is inferred using standard Javascript context blocking, and using arrow functions for function declarations retains the component's context and bindings.

## Split Out Other Components

## Delete Any Now-Defunct Things