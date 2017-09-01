title: Pelican, Travis, and Github
subtitle: &mdash; Setting Up Autmated Blog Updates
date: 2016-01-13 16:30
category: tech
tags: site, tips, automation, continuous integration

[TOC]

**Hey-o! There have been some changes made to this process. [Be sure to check out the updates.](http://shaunagordon.com/blog/2017/09/01/pelican-travis-and-github)**

This is actually the second time I've leveraged [Travis CI](https://travis-ci.org/) for managing my static-site blog, but apparently I didn't write about it. I had done it shortly after [setting up the Octopress version of my blog](http://shaunagordon.com/blog/2013/01/13/yet-another-new-home-for-the-blog/). It was nice and convenient, and dramatically lowered the barrier to writing more blog entries, though I didn't realize that until I lost that capability when I switched to Pelican (probably because the Octopress version was a bit finicky, due to breaking changes in the upstream Octopress repo, so the barrier was still pretty high).

But then I switched to [Pelican](http://blog.getpelican.com/), which was infinitely less finicky...once I got it initially set up.

# The Downfall Of Static Site Generators

As the name suggests, at some point, you have to actually *generate* your site when you use a generator. For a while, I was just doing this on my computer, which was okay until my hard drive died and I had to reinstall my operating systems. At that point, I procrastinated horribly about updating my blog.

I do have to hand it to the Ruby guys -- the almost mandatory use of Gemfiles is a godsend (this type of thing is a habit I'm very glad the PHP community has picked up and run with, too). Apparently, [pip actually does have a similar feature](http://stackoverflow.com/questions/19280249/python-equivalent-of-a-ruby-gem-file), but use of such files does not seem to be emphasized nearly as much in the Python world, at least not that I've seen (I had to specifically search for "python gemfile equivalent" to find that link, because I sincerely didn't know if such a thing existed). Not having such a file makes setting up an environment for an existing Python app/site/blog a bit...painful. What dependencies did I have? What were they named? What are the gotchas I have to worry about (I know there were some, but what were they?!)? I've since added a requirements.txt file to my blog source, but not knowing that such a thing existed proved a hindrance to my blogging. If nothing else, it's a nice reference to what needs to be installed for my blog.

I'd also still have to remember the commands needed to build it, and I'd have to set up my repositories again in the way that I had it. I was lazy about it at one point, and had them separate repos, but that's awkward as hell. So, a couple of weeks ago, I decided to clean house and set it up so that I only need to push new posts to a particular branch of my repo, and automation would do the rest.

# Github &mdash; The Static-Site Dream Host

So, first things first, we need a place from which to host our blog. Since the output is entirely html, it can really be hosted anywhere, but for this setup, we use Github's *Pages* feature. If you're not familiar with Github Pages (you must have been living under a rock), it's an easy way to host small websites, simply by designating them as such from a Github repo. Awesome, right? Right.

There are two ways to do this:

* Have a *gh-pages* branch in your project repo. This is known as a "project site" and is most commonly used for little landing pages for open source projects. My [health-oriented blog](http://health.shaunagordon.com) uses this method.
* Have a dedicated *[username].github.io* repository (or the legacy *[username].github.com*). This is known as a "user" or "organization" page and is common for user blogs and aggregate showcases of a user's or organization's repo. This blog uses this method.

The cool thing about Github Pages is that you can also use custom domains, and like the rest of the hosting, it's completely free. That's how my blogs use my domain, instead of the Github one. It's easy to set up, too.

# Step 1: Set Up The Repo

If you're doing a user/org site, then you'll need a repo named *[username].github.io*. In these sites, the master branch will be the branch that holds the generated HTML. If you're doing a project site, then you can use any repo you want, but you'll need to add a *gh-pages* branch. The *gh-pages* branch will be the one with the generated HTML. From here on out, we'll call it the *display* branch.

You'll also need branch to hold the ungenerated source (themes, plugins, markdown files, etc). I use the master branch on my health blog, and a "source" branch on my main blog. It ultimately doesn't matter what the branch name is, but we'll call it the *source* branch, here.

If you want to use a custom domain, you'll also want to be sure to include a CNAME file with the name (in my case, it contains just "shaunagordon.com" and "health.shaunagordon.com" in the relevant repos), and of course, you'll need to point your nameservers to Github.

# Step 2: Set Up Travis

**Some of the settings in this section have changed, be sure to read the update!**

For the purpose of this post, we'll assume you've set up your Pelican blog at least once, to ensure it works and displays as expected. I just fired up a Vagrant box to handle this, that way I didn't have to clutter up my host system with a bunch of Python dependencies that I only use for generating my blogs (which I'll no longer be doing locally). We'll tweak it later, but if you don't have a basic set up done yet, go do that now.

Once your repo is set up, the most basic level of setting up Travis is as simple as adding a *.travis.yml* file and logging in to Travis with your Github account and telling it to watch your repo. We need to tell it what to actually do, though. Pelican makes this pretty easy, since its Makefile handles the actual compilation and deployment. This boils the .travis.yml file down to this:

<script src="https://gist.github.com/ShaunaGordon/0cbf0b8f2d667c5ec794.js?file=travis.yml"></script>

Nifty, right?

## But Wait, What's That "Encrypted Travis Key" And How Do I Get It?

**This is something that's been updated. This technique is now outdated.**

In order to be able to push to your repo once it's built, Travis needs an access token. You get the access token by going to Settings -> Personal Access Tokens and creating a new one with the [permissions required by Travis](https://docs.travis-ci.com/user/github-oauth-scopes/). Storing that access token value in the config file in plain text is insecure, though, because it allows anyone to obtain those rights to your repositories. Not good.

The guys at Travis CI were kind enough to provide a command line tool to address this, though. It can easily be installed and the "encrypt" command run with the following:

<script src="https://gist.github.com/ShaunaGordon/0cbf0b8f2d667c5ec794.js?file=travis_install"></script>

You'll see there are two options on the encrypt command. `--add` automatically puts it into your .travis.yml file. The `--override` command is optional, but useful if you already have a secure key in your .travis.yml file that you want to replace (such as if you didn't generate the key right the first time).

## And What About That Requirements File?

This could probably be refined, but this should get you started. I simply ran `pip freeze > requirements.txt`, which gave me a list like this:

<script src="https://gist.github.com/ShaunaGordon/0cbf0b8f2d667c5ec794.js?file=requirements.txt"></script>

My Vagrant box did have a few things in it that failed in Travis, so I had to remove them. Just remove any lines that appear distribution-specific, and tweak from there based on Travis errors. Alternatively, if you know exactly what packages you installed, then you can include just those. I kind of like it a little more verbose, though.

# Step 3: Tweak Pelican

**This is something that's been updated. This technique is now outdated. Travis was kind enough to build this in!**

Pelican includes a nice little Github command within the Makefile, but it's designed more for running it locally, with credentials for the Github account. That's not really a good idea for a Travis deploy. So, we adjust the Makefile command so that Travis can push to the repo:

<script src="https://gist.github.com/ShaunaGordon/0cbf0b8f2d667c5ec794.js?file=Makefile"></script>

What this does is use the ghp-import tool to deploy the compiled site to Github, to the branch specified by `GITHUB_PAGES_BRANCH`. This allows us to use any branch we choose to be our deploy branch.

Then, we want to tweak Pelican's config files. The publishconf.yml file is most important here, but it's useful to keep pelicanconf.yml synchronized, too. We need to make sure we have a .travis.yml file and our CNAME file in the finished output. The .travis.yml file needs only one directive -- ignore the output branch. Otherwise, Travis will try to build it, too, when it updates. We don't want that.

So, what we do is add an "extras" folder if the project doesn't yet have one, and drop in a travis.yml file and a CNAME file, then let Pelican know to copy them into the compiled site, like so:

<script src="https://gist.github.com/ShaunaGordon/0cbf0b8f2d667c5ec794.js?file=publishconf.py"></script>

Now, you should be ready to go!

(The Travis setup was done with the help of [Mathieu Leplatre's post](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html), though I've made some modifications, such as the extra commands.)

# Step 4: Deploy And Blog!

Not that you're all set up, you should be able to start writing blog entries in your favorite Pelican-supported text format. Just save your blog entry in the "content" folder, commit it in git and push to your source folder in GitHub. Travis will pick up that the source branch changed, build the updated site, and deploy to your deploy branch. Woot!