title: box-sizing: border-box and Changes in How We Use the Box Model
date: 2013-02-19 17:00
category: tech
tags: standards
slug: box-sizing-border-box-and-changes-in-how-we-use-the-box-model

Back in the days when Internet Explorer 6 reigned supreme, when Firefox was just getting its foothold and taking shares from IE, and Chrome was barely a Googler's pet project, the browsers followed different box models.

Firefox (as well as the then little-known browsers Opera and Safari) followed the W3C standard box model, what is now known as "content-box". Internet Explorer, on the other hand, followed its own box model, what we now call "border-box". As Firefox began to rise and threatened IE's market share, Web developers were singing the praises of the content-box style box model (which was one of the many W3C standards that IE ignored, and Firefox implemented), to the point that when Microsoft finally released Internet Explorer 7, it implemented the standard box model.
<!-- more -->
## Fast forward seven years

Now, it's 2013, not only are more browsers on the market, but the market share has tipped dramatically away from Internet Explorer, and had spread out among several browsers. Competition has forced IE to be more standards compliant (IE10 even has text shadow support!). And, to top it all off, a CSS technique is on the rise: `box-sizing: border-box`. Yes, the very same method that IE6 used.

### What changed?

I'm only speculating, but I think it's a fundamental shift in how developers write both HTML and CSS -- and perhaps a refinement of what they feel the standards should be -- based on what works and what makes sense in practice. There are two main paradigm "camps" regarding how HTML and CSS should be architected and written.

The first is the "positional" camp. The idea behind this one is that an element's style should be dictated by it's position in the document object model, or DOM. So, for example, all `<li>` elements within any `<nav>` element would have `display: inline-block` applied to them (making a horizontal navigation list), but if you moved that same set if `<li>` elements into an `<article>` element, it would become a vertical list.

The other is the "object oriented" camp. The idea here is that the `<ul>` (unordered list) which is the parent of the above-mentioned `<li>` elements, would have one or more classes on them, such as "horizontal" or "main-nav". This class, or set of classes, would dictate how the block of elements would look, regardless of where the block was placed. To use the same example, all `<li>` elements within the `<ul class="main-nav">` block woud have `display: inline-block` on them. This styling would stay the same regardless of whether the block was inside a `<nav>` or `<article>` element.

{% pullquote %}
In recent years, the trend has been shifting more toward this "object oriented CSS" camp, and for good reason - {" OOCSS creates modularity and allows for code reuse "}. This allows, for example, for me to reuse my [faux image frame effect](https://gist.github.com/4033366) on just about any element block on any website, simply by dropping in the required CSS and adding the "framed" class to whatever I want to have the frame.
{% endpullquote %}

One of the rules of object oriented design is that an object shouldn't care about any objects outside of itself. Each object handles itself and the initial creation of its children (the children then handle themselves). This isn't as rigid in CSS as it is in real programming languages, due to how CSS and document flow manipulation works, but the logic is still sound and works for the most part.

However, `box-sizing: content-box` (the default box-sizing for modern browsers) breaks this rule, by, in a sense, making objects lie about their true size.

For example, let's say I have a three-column layout, and I want each column to be equal width. Okay, that's easy, we do something like this:

<iframe width="100%" height="300" src="//jsfiddle.net/gordondev/yzfH2/embedded/html" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

<iframe width="100%" height="300" src="//jsfiddle.net/gordondev/yzfH2/embedded/css" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

This gives us a nice little three-column layout:

<iframe width="100%" height="300" src="//jsfiddle.net/gordondev/yzfH2/embedded/result" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Let's take a look now!

<iframe width="100%" height="300" src="//jsfiddle.net/gordondev/yzfH2/1/embedded/result,css/html" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Uh oh! That's not what we want. What happened? The boxes should only be 33% of the width!

You'd think that, wouldn't you? Remember what I said earlier about `box-sizing: content-box` making liars out of our elements? Well, this is it. You see, "33%" is only the width of the *content*. That doesn't include margins, padding, or borders. 

For most people (particularly the OOCSS-leaning people we mentioned earlier), this *really* doesn't make sense for padding. The purpose of padding is to add space from the outer edge, or border, of the container, in to the content. Basically the same way the margin lines on a piece of notebook paper work. Logically, this should reduce the space allotted to the content (likewise, the CSS margin would be roughly equivalent to the space between pages in an opened notebook - they exist outside the bounds of the edge of the container). Why, then, is the default behavior to make the box *bigger* when either margin or padding is added?

Now, in the days of fixed-width layouts, this meant recalculating the width of the internal boxes, so that they fit within their parent. This is one of the core reasons why 960px was used as the go-to content width of fixed layouts - 960 divides into both 2 and 3 evenly (1, 2, and 3 columns being the most common layouts). So, in the days of the fixed-width layout, we'd simply change the width of our boxes to accommodate things like margins, padding, and borders:

<iframe width="100%" height="300" src="//jsfiddle.net/gordondev/yzfH2/4/embedded/css" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

And look! Our layout works again!

<iframe width="100%" height="300" src="//jsfiddle.net/gordondev/yzfH2/4/embedded/result" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

But what happens when the width of the container is proportional, and scales based on the browser size, as with fluid layouts? Well, our layout breaks again, because it's dependent on a parent width of 960px. Once that parent width drops below 960px, our columns wrap again. Now, in some instances, this may be what we want (when a viewport gets too narrow, having columns drop underneath one another can help keep them wide enough to be readable), but we generally want some kind of give before that happens.

Okay, so we want the columns to scale with their parent (at least to certain breakpoints, but that's a discussion for a different time), *and* we want the fixed-sized padding, is there a way to do that? Well, before `box-sizing: border-box` gained support, there actually was, but it wasn't all that pretty, especially when dealing with pixel-perfectionists. You just used percentages for everything:

<iframe width="100%" height="300" src="//jsfiddle.net/gordondev/yzfH2/3/embedded/css" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

<iframe width="100%" height="300" src="//jsfiddle.net/gordondev/yzfH2/3/embedded/result" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

This works great...except for the fact that the padding also expands or contracts. If that's what you want, then great! If you're like me, and have to deal with people who expect those padding to stay the same, then you're <abbr title="Shit out of Luck">SoL</abbr> (or, at least, you used to be).

It's also possible to put the margins or padding on the child elements, but that would either require an extra "wrapper" element, or some not-so-ideal `.three-column *` type selectors. Both of these options work, but are ugly and not very elegant. Plus, you'd have to do that for everything that is affected by this issue, instead of just making it do something sane to begin with.

## This sounds like a job for....!

With `box-sizing: border-box`, you can now use the percentage widths, with fixed-sized padding, to get this:

<iframe width="100%" height="300" src="//jsfiddle.net/gordondev/yzfH2/5/embedded/css" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

<iframe width="100%" height="300" src="//jsfiddle.net/gordondev/yzfH2/5/embedded/result" allowfullscreen="allowfullscreen" frameborder="0"></iframe>

Yay! And look, this actually makes sense (to most people)! If I tell the element that I want it to be 33% of its parent, that means I want the *everything* within the element's borders to be 33% of its parent.

## I said all that to say this...

As you can see, with the standard `box-sizing: content-box`, making flexibile layouts is a nightmare, especially when trying to keep things lean for our mobile-device-using friends. The shift toward responsive and flexible layouts has necessitated a need for stricter adherence to object-oriented types of rules, for the sake of our sanity.