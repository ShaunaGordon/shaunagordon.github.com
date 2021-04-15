---
title: "What We Owe To Each Other"
subtitle: "Contractualism and Social Justice in the Tech Industry, Explained With Plastic Spiders"
description: "Little changes really can have a big impact, and we really don't have an excuse not to make them if it means creating a better environment for everyone."
date: 2020-07-02
categories: [community, tech]
tags: [diversity, culture, civil rights]
series: ["Black Lives Matter"]
---


The topic of changing verbiage within the tech industry, particularly as it relates to references to "master," particularly in the "master/slave" contexts, but also in places like "master" branch in git (which does, in fact, [have its roots in the "master/slave" paradigm](https://mail.gnome.org/archives/desktop-devel-list/2019-May/msg00066.html)), came up in a couple of Slack groups in which I participate.

It's certainly not new (some discussions on the matter date back a decade or more), but it's always kind of a contentious topic when it comes up, despite the terminology getting phased out over time.

In this latest iteration, a young man voiced his concerns regarding the issue -- while he was okay with making the verbiage change, particularly when it came to git branches (which is a _super_ easy change to make), he didn't really understand the offense in the context (most people do assume git's "master" branch is in the "master copy" sense, which is a reasonable assumption) and felt that the context didn't leave much -- if any -- room for offense. "It feels to me very much like manufacturing outrage," he ended his response with.

He's a good guy, but... :grimacing: it was very much a "your privilege is showing" moment. (For the record, he took my feedback, where the analogy below comes from, with grace and appreciation. It was very much a case of a privilege blind spot.) I needed a way to describe the situation in a way that he could relate to, and I came up with the following scenario:

## The Analogy

Consider this - let's say you have a deep phobia of spiders.

Now let's say your desk neighbor has a realistic fake spider on his desk and it's in such a place that you always see it out of the corner of your eye as you try to work and it frequently triggers your phobia response. Because of the workplace setup, you can't move or arrange yourself so that you don't see the spider throughout the day.

Your only option is to ask your deskmate to move it or put it away.

However, your deskmate says "no." He likes where it is and it's just sitting there. It's just a fake spider. Since he has no such phobia, this strikes him as a stupid and trivial issue that's not even worth discussing. Even your attempts at explaining your phobia to him are ignored. He's written you off as "overly sensitive" and maybe even tells you to "grow a thicker skin."

And maybe you've tried to just ignore it, but despite your best efforts, there's that constant, low-level anxiety and stress triggered by that spider and no matter what you do, you can't shake it.

Maybe you ask him again, this time a bit more firmly, and now he responds that you're just "manufacturing outrage" and over a stupid figurine! Seriously! Don't you have _bigger problems to solve?_

This is the issue.

## Enter Contractualism?

Interestingly enough, I had inadvertently stumbled upon an elementary description of what's known in philosophy as ["Contractualism."](https://plato.stanford.edu/entries/contractualism) If you're like me and have watched _The Good Place_, you're more aware of the idea than you may realize, since it's...well...pretty much Eleanor's entire philosophical North Star. There's even an episode named after one of the most well-known books on the topic (_What We Owe To Each Other_).

The above is contractualism in action. We interact with each other via _social contracts_, whether we're aware of them or not. This is essentially the heart of "offense" -- someone is offended (or harmed), because they do not agree to the social contract in effect in the given situation. This makes it a **consent-based system** -- all parties involved must agree (consent) to the contract, and agreement can be revoked at any time.

In the above example, the hypothetical self never consented to the spider being in eyeshot all the time and had a reasonable rejection of it (a phobia). And no, the deskmate does not have a reasonable rejection, per contractualism, although he is offended by the request:

> In order to reasonably reject a principle, I must have some objection to it. This objection may begin with some direct harm I suffer as a result of the principle. So far, if the harm involved is pain or suffering, contractualism mirrors utilitarianism. However, the fact that a principle impacts negatively on me is not _sufficient_. To know whether I can _reasonably_ reject the principle, I must also ask how it impacts on others. If a principle imposes a certain burden (b1) on me, but every alternative imposes a greater burden (b2) on someone else, then b1 does not give me a reason to reject the principle. If I am reasonable, then I withdraw my objection when I see that your reason is more pressing.

In this case, the greater burden is on the person with the phobia, because it causes actual, physical stress and harm. The inconvenience of moving the figurine pales in comparison to the phobia-induced stress under contractalism.

## So What Does This Have To Do With Branch Names?

In the analogy, the harm is pretty easily understood -- most people, even if they don't really have phobias themselves, generally understand common phobias like arachnophobia on some sort of intellectual level at least enough to understand _that_ it's troublesome for the person, even if they don't fully understand how or why.

The harm of various trigger words or phrases, such as the "master/slave" concept in computers, seems to generally be a lot more nebulous to people (and even moreso when the "slave" half is removed and only "master" remains, such as the case with git). They can't grasp the harm being done, even though it's a drop-in substitution for the spider and the phobia in the analogy.

The simple truth of the matter is that the enslavement of Africans, while not a unique phenomenon (enslavement wasn't exactly unknown to humans, like...ever), was arguably the most exploitative, subversive, and downright inhumane in history, and unlike the other forms, we're still collectively dealing with the fallout. While slavery may have officially ended in the US at the end of the Civil War, that was immediately followed by numerous laws intended to keep the newly-freed slaves down, and it wasn't even a century later when the Civil Rights Era was in full swing, which itself was only about 60 years ago. The older people who marched probably had grandparents (and maybe even _parents_) who were originally slaves, while the younger ones are marching again in the current protests.

Think about that -- some of the people that marched in the Civil Rights Era marches have been marching again the past couple of weeks.

That's how recent this all was. It's not the distant past, not for Black Americans. Those wounds are still raw, especially since they haven't really been able to heal.

So having to constantly see flippant references to slavery, even in cases where _it's not even a very descriptive term for the context_ ([which is most of them](https://tools.ietf.org/id/draft-knodel-terminology-00.html#rfc.section.1.1)), is [like little pieces of sand or salt getting into those wounds](https://dev.to/afrodevgirl/replacing-master-with-main-in-github-2fjf) -- or the ever-present spider to the arachnophobic person. It keeps doing harm to a portion of the people involved, even if it seems inconsequential to another portion.

## But It's A Lot of Work For Something So Trivial!

It's actually not a lot of work to get started, which brings us back to the rules of contractualism -- our inconvenience is not sufficient to claim _reasonable rejection_. The harm caused by the continued presence of such phrasing, especially in the context of git repositories, is still greater than the small and short-lived burden of making the change within one's sphere of influence. It behooves us to make the change _because_ it's so trivial on our end.

At the most basic level, it boils down to an alias, a git command, and a find-and-replace on scripts. [You can change your existing "master" to "main" (or whatever else works for you)](https://www.hanselman.com/blog/EasilyRenameYourGitDefaultBranchFromMasterToMain.aspx), and [Github is even already working on changing its defaults , and several other large projects are getting on board](https://www.zdnet.com/article/github-to-replace-master-with-alternative-term-to-avoid-slavery-references/) (so the whole "it's too complicated!" excuse _really_ doesn't fly).

So, let's hold up our end of the social contract and help make software -- and the rest of the world -- more inclusive, even if it's just a tiny bit.
