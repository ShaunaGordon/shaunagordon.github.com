---
title: "On Problem Solving"
subtitle: "(And Effectively Asking For Help)"
description: "With ducks!"
date: 2020-10-21
categories: [teaching, tech]
tags: ["personal growth", tips]
---

The most important skill in tech isn't the technology. It's problem-solving. Whether you get into cyber security, system administration, or programming, the heart of all of it is really the ability to take a problem, break it apart, and work out a solution -- very often coming up with solutions that didn't previously exist at all. Even on the more everyday scale, you'll be constantly faced with error messages, odd software behavior, broken tests, and more that you'll be expected to triage and if not fix yourself, hand off detailed information about the problem to those who can fix it.

Likewise, the second most important skill is knowing when -- and how -- to ask for help when you've reached the limits of your current knowledge. Knowing how to ask good questions when asking for help goes a long way toward not just getting _an_ answer or lead, but also for getting a _relevant_ answer or lead that takes you closer to your final solution.

But for both of these, we need to build the foundations. We don't just enter the world knowing how to solve problems and find answers and ask questions. These are skills we must develop like any other, and unfortunately, they aren't really explicitly taught like other skills are. Let's change that.

## Problem Solving

You're working on a project (or assignment) and suddenly you get stuck. Maybe you encounter an error (or maybe you don't), or the documentation you're working with is incomplete or even incorrect. What do you do now?

Believe it or not, problem-solving is highly procedural. There are some places where you might make different decisions or have different options, but the process is largely the same.

### Step 1 - Assess The Situation

How do you know there's something wrong? Are there error messages anywhere? Is the UI not what is expected?

If you don't know the answer to these questions, then take a minute to first list what *should be*. Should the test pass? Should the application run? Should the background be a particular shade of blue? Or, for physical-world application examples, should the car start? Should the paint roller roll smoothly? Should the vacuum pick up the mess? This is your *desired* or *expected* state; your "Point B." Knowing this will help you determine how the *current* state differs, and thus, what is broken.

The *current* state is your "Point A." Problem solving is the process of getting from A to B, not unlike plotting a route between two geographical locations. Just like with navigation, if your Point A and Point B match, then you're already there and there's no problem. But, of course, you wouldn't be here if that was the case.

So, now that you have your list of what *should be*, compile your list of *what is*.

Are there error messages? Be sure to check all potential output locations. Sometimes there are multiple terminals it could output to, or there might also be a log file. Depending on what you're working with, they might not be text-based messages. They might be lights -- such as the dead battery indicator on your car dashboard. They might be sounds -- such as the beep sounds from a computer.

If there aren't any error messages, then compare the current state with the intended state. This is the part where most people stop, because they don't look deep enough. Most people get to this point, declare "it's not working" and immediately expect someone else to step in. The key to good problem solving, though, is *not* stopping here, but digging deeper and seeing *exactly* what's wrong.

What's different? What's missing from the current state that should be there? What's there that shouldn't be?

Take, for example, your (gas-powered) car not starting. It doesn't start. What's wrong with it? Even with a fairly rudimentary knowledge of cars, you could probably name off half a dozen possibilities. If you know a bit more about cars, though, you probably also know that each of those possibilities display different symptoms -- and it's those symptoms you need to seek out.

So your car won't start. Did the lights come on when you opened the door? What happens when you try to start it? Does the dashboard light up when you turn the key into the "on" position? When you turn the key to the "start" position, does the engine even *try* to "turn over" or does nothing happen at all? If the engine tries to start, what does it sound like? Is it a steady whir, or does it sound like it's gaining and losing energy? Does it run when the key is in the "start" position, but die once you let go? Do you even get the "click" sound that immediately precedes the engine starting?

The same line of questioning is necessary in tech, too. Did you get the prompt you were supposed to get? Did it even *attempt* to install its dependencies? If it attempted, was it successful? Are the expected UI elements present and where they should be?

#### **What If I Don't Know Anything About The Thing?**

It's really easy to fall into the trap of "I don't know enough to do this part!"

But here's the thing: you know more about your current situation than you're giving yourself credit for, *and* you have more information at your disposal than you think. 

If you're doing something totally new, you probably already have documentation and other instructional information open. These provide you information about the intended state, even if they don't explicitly state it, through images and statements that indicate expectation of something being in a certain place.

If a tutorial tells us to click on an icon, but that icon isn't there, then that's our indication that something is missing or off. Our next step is then to make note of that missing bit. We don't have that icon. Okay, why not? Are we working with the same version that the instructions are working with? Did we miss something that needed set up? Did the instructions miss a setup step? (This happens, too. It's actually quite difficult for subject matter experts to create thorough beginner instructions on the first pass. The best documentation generally involves several reviewers and many edits.)

### Step 2 - Interpret The Data

Take some time to think about what the data you've gathered *means*. Come up with hypotheses about the likely issues.

Going back to the car -- perhaps it does *try* to "turn over.* The lights also came on when you opened the door, and the dash lights up as expected. That means the battery probably isn't dead (or at least not *totally* dead), right? So what does that leave us with? That leaves us with things like not enough gas or oil, a problem with the spark plug, and a more severe problem with the ingition, among some other things. Well, gas is fairly easy to check -- where's the gauge sitting at when the car is on? If it's not empty, it's *probably* not out of gas. We also see that the "check engine" light isn't on, so it's likely not a more severe engine problem. So now, most of the rest of the stuff requires us to move to a different part of the car.

### Step 3 - Repeat Steps 1 And 2 (If Necessary)

Our goal right now is to reach a testable hypothesis -- a change that we can make to see if we get a different result. Until now, we've been able to rule out problems just from gathering and interpreting data, and our process has led us to another part of the vehicle. So now, we have to re-assess.

So we pop the hood and take a look inside to see if anything sticks out. Checking the oil shows that we have enough, so we can rule that out. But when we get to the spark plug, we notice that it's quite black and there doesn't appear to be much space between the nodes.

That's not what a spark plug is supposed to look like. There's supposed to be a decent gap between the nodes and they're supposed to be bare metal. Instead, it's gunked up with carbon.

### Step 4 - Test The Hypothesis

Now we have a testable hypothesis -- the car won't start because the spark plug is gunked up. So we grab a rag and clean it up, making sure the nodes are nice and clear, and put it back in its place. Finally, we start the car.

### Step 5 - Reassess

Does the car start? If so, great! We found the problem and fixed it!

But sometimes, it's not as simple as that. Perhaps now, when we try to start it, it *starts* fine...but as soon as we let go of the key, it stalls out.

Now what?

#### **Progress!**

Believe it or not, we've actually made progress toward fixing the problem, even though it still doesn't start yet. How do we know?

Because the car now *behaves differently.* Remember: our original main symptom was that the engine would not turn over and get to that fully started state that we're looking for when we turn the key to start it. Now that we've cleaned the spark plug, it does that! ...It now just doesn't *stay* that way.

That's our cue that what we've done has made a difference, but there's still something else wrong.

Now, in tech, sometimes that change in behavior doesn't actually move us *toward* our goal. It might even move us *away* from it. But *that's okay*. What matters here is *the change itself*. The action we've taken has resulted in a *state change* and that change gives us valuable information.

And what if nothing changes? Well, that *also* gives us information, though admittedly not as useful or satisfying as a state change. We can, however, conclude that our hypothesis didn't affect what we thought it would. In the car situation, perhaps the engine still won't "turn over." Well, that means the starter being dirty wasn't the problem. (Now, this *is* where the analogy fails us a little, because we can't really "unclean" a spark plug -- nor would we want to -- but in tech, we would revert the change we just made, so that we ensure our working state is as it was initially, or we risk compounding our issues and not knowing what the actual cause or solution turned out to be.)

### Step 6 - Rinse And Repeat

Not only is problem-solving highly procedural, it's also cyclical. This assess-interpret-test cycle is repeated over and over until you've either fixed the problem, or exhausted your hypotheses. Hopefully, during the process, you generate more hypotheses as you gather more data, so that you reach your solution before you run out of ideas.

## Asking For Help

Sometimes, though, we do run out of ideas. Or maybe we just get "caught in the weeds" and find ourselves going in circles. We're too close to the problem now that we're looking at every proverbial blade of grass with a magnifying glass, when what we need is to take a step back and look at the whole picture.

...and sometimes we just need someone to force us back to basics.

![Have you tried turning it off and on again?](https://media4.giphy.com/media/F7yLXA5fJ5sLC/giphy.gif)

### Knowing *When* To Ask For Help

Putting a hard-and-fast clock time to when we should ask for help...doesn't really work too well. A time that one person finds too long could just as easily be "too short" for someone else. However, if we use the above problem-solving process, we can better gauge when a good time to ask is.

That's because it's less about the amount of time we've spent (at least beyond the extremes of 30 seconds and 12 hours or days), and more about being able to demonstrate what we've tried and articulating that our hypotheses have failed. So, the "right" amount of time is the amount of time it takes to go through the problem-solving cycle at least a couple of times.

### Knowing *How* To Ask For Help

After we've decided that we need to ask for help, we need to determine *how* to ask. Believe it or not, there are better and worse ways to ask for help!

Just saying "it doesn't work, help me fix it!" is a bad way to ask for help, because it doesn't give the person helping any information about what's wrong, what information we've gathered, what we've already tried (or even *that* we've tried anything), or who else we've asked (and what they've come up with). Coming to a person with this forces them to do a bunch of investigative work *just to be able to get the context needed to help.*

Getting help faster means we need to preempt that investigative step by providing the contextual information needed to get them up to speed. So, instead of "it doesn't work!" or "I'm totally lost!" we can use what we gathered in the problem-solving cycle to build out a better request.

Let's say we weren't able to fix the car, so we call our mechanic friend. Instead of saying, "Joe! My car won't start! Help!" we do the following:

> Hey Joe, my car won't start and I've exhausted my knowledge. I was hoping you could help me out.
> 
> When I first tried to start it, the engine would try to start, but not actually be successful. The lights all worked and the gas meter says I still have half a tank. I checked the oil and it seems fine, and I checked the spark plug. It was dirty, so I cleaned it and tried to start the car again. After I did that, the car would start, but now doesn't stay running once I let go of the key.
> 
> That's about my limit of knowledge, so I tried an Internet search to see what it might be and where to go from here, but all the suggestions seem to need tools I don't have or require taking it to a mechanic shop, which would require me to get it towed. Do you have any ideas I could try -- or do you think you could look at it with the tools you have -- before I resort to getting it taken in?

Notice the elements we have here:

1. The specific, overarching issue (the car won't start)
2. Symptoms of the issue (won't "turn over")
3. What we've already tried (assessed the battery and fuel level, checked the oil, cleaned the spark plug)
4. What changed after we tried something (engine now starts, but won't stay running)
5. Indication of research attempt and findings
6. The help request, which includes a "self-help" (what else can I do to troubleshoot this problem and maybe fix it myself?) as well as a "full-service" (is this something you might be able to fix for me?) option

This gives Joe enough information to pick up where we've left off, without having to ask his own probing questions just to find out what we've tried and what symptoms we're observing or repeating work we've already done. It also demonstrates that we've tried to solve the problem ourselves, including stretching our current level of knowledge.

### Rubber-Ducking

Sometimes (most times, really), we don't actually *need* the other person's help. We need the perspective that we gain through *the act of making a good request for help.* This is because the act of explaining the full context forces us to slow down and look at what we're *actually* looking at, instead of what we *think* we're looking at (our brain's are *fantastic* at filling in details that aren't actually there).

This is where "rubber duck debugging" or "rubber ducking" comes in. Rubber ducking is the process of explaining in great detail to something (traditionally a rubber duck, but it can be anything) the problem that you're having. The idea is that the duck has zero context for your problem, so you *must* provide it that context. The act of providing that context forces you go over everything you've done, what worked, what didn't, what problems there are, what confounding factors there are, and more, with a fine-toothed comb. The key, though, [is **actually talking it out**,](http://rubber-duck-debugging.org/) hence the external, inanimate object.

Try it!

<iframe width="500" height="300" src="https://www.youtube.com/embed/huOPVqztPdc" frameborder="0"  allowfullscreen></iframe>
