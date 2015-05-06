title: "Anatomy of an Octopress Theme"
date: 2013-01-16 01:14
category: site
tags: themes, html/css
slug: anatomy-of-an-octopress-theme

As you can probably see, I've updated my theme to something a little less Octopress. I still have a few changes to make, such as getting a background image that fits a larger viewport. It probably also needs some polishing for things that I haven't run across yet, and deal with IE8 and below's lack of support for RGBA and media queries, and I might toy around with how it responds to different sizes (oh yeah, and tweak how lists in the content are laid out), but other than that, it's pretty much done.

I'm by no means a designer, so I doubt anyone but me will really like it, and if my history has anything to say, I probably won't like it myself in six months, but for the time being, at least, it's not the very generic, default theme. It also adds a base theme to the (currently insanely small) pool of Octopress themes.
<!-- more -->
## So, What's the Verdict?

Overall, it wasn't too bad. If you're already familiar with CSS preprocessers, such as LESS or Sass, then you're already well on your way to modifying the theme, Octopress uses a series of Sass files to generate the final stylesheet. Unfortunately, I take issue with a number of things with how the default theme handles things. It's no wonder there haven't been very many themes made. For such a simplistic and hacker-friendly framework, it's kind of a pain in the ass to theme.

### The Sheer Number of Files

For a theme that's supposed to be mobile friendly and responsive, there are a *ton* of files. Granted, they all get generated and compressed down into a single, minified file, but it seems Sass and Compass don't merge common declarations that are split between files. This results in a lot of declaration overwriting. Fire up your favorite browser's developer tools, and let it display overwritten declarations, and you'll see what I mean.

All those files also means a lot of digging to find things. A lot of files had variables, mixins, and/or extension templates within them, making it difficult to track down exactly what went where (and also made it possible to break the entire thing just by changing one element). It's no wonder they have the "custom" folder. At the folder level, all these files are organized pretty well; dig deeper, and you start getting into some trouble.

### Context-Specific Variables (And a Ton of Them)

The default theme has 11 color variables, 6 font-family variables, and 13 measurement variables, just in the "custom" folder (there are a dozen or so more scattered throughout the theme SCSS files), and they're all context-specific names, like $sidebar-link-color, $footer-bg, and $sans. This is a bit of a nightmare for maintainability and customizability, because once you change the value of, say, $serif, to a sans-serif font, you've destroyed the perceived meaning of the variable.

### Nuke The World Resets

Yes, plural. There are two resets - one named "reset-html5" and one named "global-reset". Global-reset, in particular, is a "nuke the world" reset. *Everything* is reset. Headings look the same as paragraphs, it's chaos. For a mobile-friendly site, that's a lot of things to get undone, only to be redone a short time later.

Especially when dealing with mobile-friendly and responsive sites, I'm a big fan of normalizing versus "reseting". The reset-html5 seems to leave enough things alone, though, that I left that one. I might ultimately just use normalize.css, though.

### Zero Documentation for Contributors

Octopress has a lot going for it, including great documentation for *using* the system (there's documentation *everywhere*, even in the source!), and even some for doing basic modifications to the default theme (overriding styles, changing the custom HTML in the templates, etc). However, for hackers...there's not much. Kind of ironic for what touts itself as "a blogging framework for hackers" (or, as I've been inclined to call it, "Nerdpress").

"But real hackers don't use documentation!"

Yeah...about that. Hackers are, at the core, problem solvers. If there's something we want done, we'll get it done. However, having documentation designed for contributors is part of being a good open source project, especially once you get large enough to *have* contributors. It saves time and headache.

"But Ruby's a readable language!"

That may be, but SCSS isn't so readable (granted, it's better than plain CSS in most cases), and the issue is compounded when things are spread across a dozen files. Additionally, in code documentation is less about *what* and more about *why* something is done a certain way.

That said, the "core team" of this project I'm pretty sure is still one person, so given that, it's not surprising that there's a lack of documentation for developers (especially since he's still active on it). Hopefully, that will be only a temporary complaint as the project continues to grow and mature.

### The Silver Lining

Now, it really isn't all bad. There's actually a nifty little system in place that it seems most people don't know about. In the root folder, there's a hidden folder called `.themes` (for you Windows folks, the dot in front of the file or folder name makes it hidden). That's where your themes are stored. If you've installed one of the custom themes, you may have noticed that that's where the instructions tell you to clone their git repository to, but if you've never tried installing a theme, you probably don't know it's there.

Additionally, the `rake install` command actually takes a parameter, of which "classic" is the default. This parameter allows you to tell Octopress what theme to install. Once you find out these two little tidbits, you no longer have to worry so much about your customizations getting nuked by an Octopress update.

As I mentioned before, it's also pretty logical about how the files are organized within the folders, which can make it easier to find groups of styles, even if finding specific ones are more difficult. Also, the modular approach, while not without its drawbacks, does have the advantage of allowing you to leave alone whole files (or make only slight modifications) if you want to keep certain things (such as the styles for code blocks).

## Final Thoughts (or TL;DR)

There's a pretty good base in the framework itself for allowing others to contribute themes, but it can certainly use some polish and refinement. I look forward to watching Octopress and its community evolve.