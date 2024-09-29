---
title: "Adventures in Modernizing React"
description: "Something, something, new paradigms"
date: 2024-09-08
categories: [tech]
tags: [react, legacy code]
---

I spent the better part of my first year at Custom Ink upgrading an Electron and React application. That was an adventure unto itself, let me tell you. It also resulted in a list of "things I need to do when my priority isn't just get this thing working again to unblock the other team." Among that list was updating the code to modern standards -- something I got to make a bunch of headway on in the second half of my second year.

I got really good at converting class-based React components to functional ones. And now, I want to document how I did it, because there are always legacy apps to update.

## Convert The Class To A Function

It sounds a bit like a tautology, but the first step in converting a class based component to a functional one is, indeed, to make the conversion.

Where we have

```js
class Foo extends React.Component {
```

we need to make it

```js
const Foo = () => {
```

This, of course, will promptly throw a bunch of IDE syntax errors. That's okay, we'll fix those in the following steps. Just make sure the function is wrapping properly.

## Return the Template

The next most straightforward change to make is uwrapping the `render() {}` function to just a `return ()` statement.

So what starts as this:

```js
render() {
    return (
        <Foo>
            {{ this.text }}
        </Foo>
    )
}
```

becomes this:

```js
return (
    <Foo>
        {{ text }}
    </Foo>
)
```

## Convert The Inner Members

Now that we've done the easy part, the next step is to convert all the functions to either hooks or constants. This is where it gets a bit time consuming, because it requires more understanding of the code than simply a syntax conversion.

### Reactive Members to Hooks

I've found it easiest to start with picking out the variables and functions that are used for reactivity, because these are the things that will go into one or more `useEffect()` functions. This includes legacy lifecycle hooks like `componentDidMount()`, which have been deprecated.

For a simple example, let's say we have something like this:

```js
componentDidMount() {
    widgets = fetchWidgets();
}

onSelectedUpdateCountWidgets(widgets) {
    setCounter(seletectedWidgets.length);
}

handleSelectClick(event) {
    if(event.target.value == falise) {
        selectedWidgets.find(event.target).remove()
    }

    selectedWidgets.push(event.target)
}
```

That might become:

```js
const [widgets, setWidgets] = useState({});
const [widgetCount, setWidgetCount] = useState(0);

// Passing an empty array as the second parameter runs the body on load
// You don't want to set them in useState, because that's run on every repaint
useEffect(() => {
    setWidgets = fetchWidgets();
}, []);

useEffect(() => {
    const count = widgets.items().filter(widget => widget.selected).length;
    setWidgetCount(count);
}, [widgets]);
```

How `useEffect` and some of the other newer hooks work can take a little getting used to, but as you can see, it greatly cleans up the code, overall, thanks both to optimizing some parts of code (which might include updating code to leverage newer language features), and to switching to `useEvent()` hooks.

This is a very simple example, so the gains aren't as prominent, but I've reduced the size of some large components by as much as 60%, almost solely from this step. More importantly, though, is that I've greatly reduced the *complexity* of those components.

### Functions To Arrow Function Constants

 While there are some cases where the old function syntax is still needed, and this part isn't *strictuly* necessary, the vast majority of them can be converted to arrow functions.

 So this:

 ```js
 foo() {}
 ```

 becomes:

 ```js
 const foo = () => {}
 ```

 Switching the standalone functions to arrow function constants, in my opinion, helps keep function declarations uniform (since anonymous functions used both in the component declaration and in places like hooks are usually written this way), which in turn makes it easier to scan a source file. It also better leverages `const` versus `let` context, and gives the functions access to all of a component's variables, without having to pass them (and more crucially, `this`) around all the time.
 
 Yeah, yeah, developers coming from languages like Java or Elixir are probably cringing at the above paragraph, but trust me, it's okay. I'll explain more in the next section (and possibly in a lot more detail in another post).

### Convert or Remove Variables and Properties

Class-based components often use a lot of `this` and `this.props` type references when referencing class variables. These are no longer needed, because of how function based components work. The context usually communicated with `this` is inferred using standard Javascript context blocking, and using arrow functions for function declarations retains the component's context and bindings, eliminating the need to pass `this` around.

This conversion takes us from this:

```js
class Foo extends React.Component {
    constructor(props) {
        super(props);
    }
}
```

to this:

```js
const Foo = (props) => {

}
```

Much cleaner, right? In Javascript land, right.

While we're leveraging modern Javascript techniques, we can even take this a step further, making it easy to have required properties, in addition to ones this component doesn't care about, but a child component might, and do this:

```js
const Foo = (bar, baz, ...props) => {}
```

This allows us to explicitly require the ones this component cares about -- `bar` and `baz` -- then dump everything else into `props`, which we can later pass through to a child component.

> [!note] On Prop Drilling
> We do have to be mindful that passing through `props` like this can make it very easy to end up prop drilling -- passing properties through several components to reach a deeply nested component, where the prop is actually needed. While it's recommended to avoid any prop drilling in theory, in practice the alternatives can sometimes be more complex or harder to understand than simply drilling through one parent for a given use-case, especially if the "best" alternative isn't yet implemented in the project (I'm looking at you, Context API). Alternatively, some temporary prop drilling might be an intermediary step when converting from legacy to modern syntax.
>
> In short, just use your brain about it.

## Split Out Other Components

I can't tell you the number of times I've found a component in a legacy database that was housing *at least* one other component, if not two or three, and in some rare occasions, as many as half a dozen (and in a lot of cases, it's reusable components like dialog boxes). Even though the result is necessarily more files, the resulting components are usually so much simpler that it's more than worth the extra bit of mental overhead of having multiple files open. This is another place where I often greatly reduce the file size of any given component.

As a general rule of thumb, any time you see something like this (for anything but the most basic snippets):

```js
templateBlock() {
    return (
        <div>
            <p>Some stuff</p>
        </div>
    )
}
```

you can usually extract it out. Don't forget to pass in whatever properties you need, and take the members that actually belong to this new child component.

### Leverage useState and Properties

Is your code scattered with a bunch of `onChange` style event handlers that really only detect if a child component has changed in some way? Well, now you can clean that up, too, with the help of `useState`.

One of the cool things about React is that you can pass the state setter function to the child components. This allows them to handle their own change logic. So you go from something like this:

```js
onPropOneChange(data) {
    someValue += data;
}

onPropTwoChange(data) {
    someOtherValue += data;
}


<ChildComponent onPropOneChange={this.handlePropOneChange} onPropTwoChange={this.handlePropTwoChange} />
```

to doing something like this:

```js
const [propOne, setPropOne] = useState(0);
const [propTwo, setPropTwo] = useState('');

<ChildComponent setPropOne={setPropOne} setPropTwo={setPropTwo} />

// Or, if the child needs to know the current state of the prop

<ChildComponent propOne={propOne} setPropOne={setPropOne} propTwo={propTwo} setPropTwo={setPropTwo} />
```

The nice thing about this is that changes made even deep in the component tree, automatically propagate back up to where the state objects are created.

## Delete Any Now-Defunct Things

By now, you should have converted your entire component, or very nearly so.

...But what about all these other functions and variables that are still hanging out?

Over the course of the conversion, you might end up with orphan functions, or imports that are no longer used, or any number of leftover code. A code editor that changes the color of an unused function, variable, or import name can really come in handy here, because it makes them very easy to see, and thus remove. This brings us back to a simple step -- just delete those things! If you're concerned about "losing" code you might one day need, do a commit in your version control, before you go through and clean up the orphaned code. That way, you have a commit that is dedicated to code removal that you can go back to in the future. (Hint: you probably won't, to be honest.)

## Sit Back With A Cold One

And...you're done! Or should be *really* close to it. There might still be some little quirks that need worked out in the upgrade. 