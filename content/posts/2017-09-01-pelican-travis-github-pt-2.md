---
title: "Pelican, Travis, and Github, Part 2"
description: "Updating Pelican and the Travis config to account for changes in both. Yay for simpler configs!"
date: 2017-09-01T23:00:00-05:00
categories: [tech]
tags: [blog, tips, automation, continuous integration]
aliases:
- "/blog/2016/01/13/pelican-travis-and-github-pt-2"
---

Last year, I wrote a post on [automating the generation of my static-site blog](http://shaunagordon.com/2016/01/13/pelican-travis-and-github/). As they do, things have since changed, and I figured I'd update accordingly.

# Changes To Travis And .travis.yml

Travis recently made several updates, many of which make our job easier.

## Build Settings

Travis now has the option to build only if a .travis.yml file is present. Before, you needed a .travis.yml file in both your source and your display branch. Now, that's no longer the case.

There's also the ability to auto-cancel queued builds that haven't yet started and only build the latest push or pull request. While this ought to have limited use on a blog (unless you're like me and find or think of things immediately after pushing a commit), it's still a neat feature.

## No More Encrypted Travis Keys!

Okay, that sounds bad out of context, but it's actually a good thing. Before, the key needed for Travis to push the built content to production had to be in the .travis.yml file. While it was encrypted, it still wasn't really good practice. That's no longer an issue, because Travis now has an "Environment Variables" section.

So, [where you would have set up that key,](http://shaunagordon.com/2016/01/13/pelican-travis-and-github/#but-wait-whats-that-encrypted-travis-key-and-how-do-i-get-it) you now just take the key and set it in the Travis dashboard, using the same variable name. Yay! No more keys in the repo!

## Built In Deploy To Github

Another update precludes the need for the `ghp-import` script in the Makefile, and renders [this entire section](http://shaunagordon.com/2016/01/13/pelican-travis-and-github/#step-3-tweak-pelican) moot.

Instead, our `script` section simplifies slightly and we add a `deploy` section:

<script src="https://gist.github.com/ShaunaGordon/8efbf5408ebc6e8f8fef92ecdb5e4c7c.js"></script>

This new section is particularly cool, because it supports a ton of different platforms, so you're no longer bound to Github. You can declaratively deploy to almost anywhere, simply by changing the `provider` and updating the options accordingly.

For more information, be sure to [check out the documentation.](https://docs.travis-ci.com/user/deployment/pages/)

## Changes To Pelican Config

The main change to the config is with the Markdown plugin.

We went from this:

<script src="https://gist.github.com/ShaunaGordon/58a1e78020bfd6c025f598871a053b44.js?file=old-n-busted.py"></script>

To this:

<script src="https://gist.github.com/ShaunaGordon/58a1e78020bfd6c025f598871a053b44.js?file=new-hotness.py"></script>

While it looks more complicated, it's a lot more expressive.

Happy blogging!