title: Vagrant - Initial Thoughts
date: 2013-11-17 01:14
category: tech
tags: vagrant
slug: vagrant-initial-thoughts

So, I finally did it. I finally started playing with [Vagrant](http://www.vagrantup.com/). I have to say, I quite like it.

At the moment, I just have a generic Ubuntu box that I downloaded from [Vagrentboxes](http://www.vagrantbox.es/) and then used a script to download the dependencies needed to run Octopress and my blog. Add a little port-forwarding magic, and I no longer have to deal with RVM, Ruby versions, and what-have-you on my MacBook Pro (this is a very good thing, as I've found OSX to be surprisingly hostile to developers in its attempt to be "helpful"). This is great, but quite cumbersome, because it involves updating apt-get, installing a bunch of things that have a laundry list of dependencies out of apt-get, then installing the Ruby gems needed, *then*, finally, running `rake preview`. Once it's up and running, it's great, but that process takes somewhere between 5 and 10 minutes.

Come on now, we can do better than that.

So, now, my next project with Vagrant will be to create a box that already has the necessary prerequisites for Octopress. Then, at some point, I think I'll make one for other development projects, too. I suspect it will save me - and some of my coworkers - quite a bit of headache when it comes to dealing with different development environments (I know at least one coworker who has to support legacy 5.3 applications, and help with our new Laravel apps that require 5.4+ due to our heavy usage of array literal notation).