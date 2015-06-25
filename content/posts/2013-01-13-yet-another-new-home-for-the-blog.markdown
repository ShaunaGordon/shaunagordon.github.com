title: Yet Another New Home for the Blog!
date: 2013-01-13 21:22
category: tech
tags: site
slug: yet-another-new-home-for-the-blog

Yes, I know. It seems like I've changed blog platforms on an annual basis. With a little luck, this will be the last time. 

## What Happened?

In short, I became disillusioned with Blogger. It seemed like a nice platform, at first, but I soon came to find the cracks in the foundation. So, after some thought about what I *really* want/need in a blog platform, I decided to go a different direction.
<!-- more -->
## The Problems With Blogger (and the Other Big Platforms)

Blog platforms are great for the people who don't know any better, but I'm a web developer. Not only do I get the...ahem...*joy* of seeing how the sausage is made on platforms like Wordpress, where I can look at the source code itself and even have to modify it through extensions, but I also get glimpses of that process in platforms where I'm not privy to the source code, such as Blogger.

One of the first problems I ran into was the HTML that Blogger outputs in posts. It seems that Blogger was written back when Geocities was still popular, and people didn't care about semantic HTML, and Google doesn't seem to care about updating it.

It's very difficult to control the style of text that isn't inside any kind of predictable tag block. It's also difficult to deal with code that's filled with &lt;div&gt;s that are nested twelve deep.

The other big problem I found was the editor. I hate the standard WYSIWYG editors, in part because I spend most of my time typing in some form of code or markup. That said, wrapping everything in &lt;p&gt; tags gets tedious, so my favorite editor for blogging is one that will deal with that tedium, while allowing me to add HTML as needed.

"Why not just use Wordpress? It wraps everything in &lt;p&gt; tags!" Yeah...it does a "wrap the world" thing. Instead of wrapping the text as it's being written, or even wrapping it on save, it does it only on *output*. Dynamically, which means it's an extra output step, which seems unnecessary to me. Additionally (and here's where the "wrap the world!" part comes in), it doesn't care what it wraps. Therefore, it wraps, say, images in their own paragraphs, or even in with a neighboring paragraph. Wordpress's editor also drives me insane with what it does and does not allow. Even the little bit I've worked with it for client projects, I've wanted to throw it out a window, due to the way the content editor tries to dictate what I can and can't post.

To Blogger's credit, its editor doesn't do what Wordpress does. On the other hand, it takes the completely opposite approach - the HTML editor doesn't assume anything. This means that every single paragraph has to be wrapped in &lt;p&gt; tags, by hand.

This wouldn't be too big a deal, if it weren't for the fact that I've started posting from my mobile devices, which, of course, don't have great keyboards for typing HTML tags. That raises writing out the tags from mildly tedius to unacceptable. It also brings me to my next problem with Blogger.

The mobile app isn't all it's cracked up to be. In fact, it kind of sucks. It's impossible to tell if it uses rich text or HTML mode. When you save a draft, it inserts HTML, but then encodes existing HTML. On a phone, there's also all of about three lines visible when the keyboard is active, thanks to all the chrome. In short, it's a mess.

I'm done with this crap. Time to move on to greener pastures.

## Enter Octopress (and Disqus)

Followers of my G+ probably noticed that I voiced my issues and mind-leaks this past weekend. I enumerated the reasons for wanting a new blogging platform, which largely hasn't changed, except for wanting sane HTML output, and, ideally, to be able to write it in Markdown.

While searching, I also stumbled on an entirely different approach to writing blogs - static site generators. You see, with your typical blogs, the content is stored in a database, and is dynamically generated each time someone visits that URL. This is a terrific mechanism...for Amazon. For a blog? Not so much, if you really think about it. The content doesn't change *that* much, and, with the help of a tool, even the lists can be updated accordingly. Granted, for Joe Schmoe, who has a blog because his "brother's kid is good with computers," something like Wordpress or Blogger or even Dreamwidth is good enough. For someone who lives in the world of code? I can find something better.

And it seems I may have.

I found Octopress, but didn't give it much stock at first. When I first found it, I was under the mistaken impression that you put the system on a server in much the same way you would with Wordpress. It also seemed like one of those blogs where you couldn't have comments. I wanted commenting, so I looked elsewhere.

Then I stumbled onto a blog that talked about migrating to Disqus and whatever their blog platform of choice ended up being. Now, I'd seen Disqus around, and even commented using it, but never thought much of it. It's one of those things that you get so used to seeing that you no longer see it at all. What I found out while reading that blog was that not only could you add it to damn near anything, but you could migrate the comments, making it completely platform-agnostic. The fact that you can use the same Disqus login for any site that uses it is just icing on the cake. I was sold so quick that my Blogger blog already has it, so that I can migrate the comments over.

Once I did that, options opened up for blogging platforms, because then, the built in capabilities (or lack of capabilities) no longer mattered. I now have my threaded comments wherever I go. So, I ended up circling back to Octopress, thanks to finding it pretty much everywhere when searching for "markdown blog". So, I dug some more into it, and the more I read about how it works, the more I liked it.

I found out that you don't actually set it up anywhere but on your working computer. It takes some command line, and the instructions are for Debian-based Linux distributions (including Ubuntu), but again, that's the world I live in, so no problem there. You then hook it up to a repository that's hosted somewhere, tell Octopress to generate everything, and upload the generated content.

Upload it where? Well, there are a number of places you could, but the most convenient I found was actually GitHub (factoid: it's named "Octopress", because it runs off of GitHub's Jekyll static site generator, and GitHub's mascot is the "Octo-cat"). GitHub has a "GitHub Pages" feature that automatically renders HTML from a repository. So, what's uploaded to GitHub in my [personal repository](https://github.com/ShaunaGordon/shaunagordon.github.com), is actually *the* source for the rendered blog. How cool is that? Oh, and GitHub is nice and allows you to use your own domain, free of charge (because, really, it's stupid to charge to allow that kind of use; it's a setting in a text file).

## What Now?

Over the next...well, I don't know how long, I'll be working on migrating my Blogger over. Hopefully, the export feature is sane, and I'll be able to easily convert the HTML to Markdown, even if it means the third party tool. Then, I'll move my domain information over to it. I may even just move the rest of my site over, while I'm at it, since I'm already planning on reworking my site's design to be more mobile-friendly, and it's static and only a couple of pages, anyway. So, until then, I'll use the default Octopress theme for this blog. I'll have to see just how GitHub deals with more complex nameserver stuff.

Ah, the world of web development, ain't it grand?