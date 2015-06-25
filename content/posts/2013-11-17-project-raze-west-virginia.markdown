title: Project - Raze West Virginia
date: 2013-11-17 14:37
category: projects
tags: laravel
slug: project-raze-west-virginia

[TOC]

## The Client, and a Little History

While working at Fahlgren Mortine, I had the opportunity to work with the West Virginia Department of Health and Human Resources (DHHR) on the new website for their teen anti-tobacco campaign, Raze West Virgina.

I'm already familiar with teen anti-tobacco campaigns, having been involved in Pennsylvania's for a time when I was a teen, myself, but I found out that what makes West Virginia's somewhat unique - and very important - is that West Virginia ranks as the highest, or second highest (in some subcategories), of tobacco users nearly across the board, from adults, to pregnant women, to teens. When nearly a third of everyone around you, no matter the demographic, uses tobacco, that's a lot of peer pressure.

### Enter Raze

Raze is one of several youth anti-tobacco campaigns in West Virginia. It's a little different from many others, because it's not just conferences. Rather, it's groups of teens at the school and community levels ("crews"), sponsored by an adult, that help create a grassroots anti-tobacco movement. They do this by organizing what they call "commotions," or micro-events to help raise awareness and "tear down tobacco lies." These commotions can be as simple as handing out fliers, or as large as holding an assembly.

As an added incentive, organizing commotions earns the crew a certain number of points. At various thresholds, the crew then earns gear, ranging from pens to backpacks, emblazoned with the Raze logo.
<!-- more -->

### Our Role

As West Virginia DHHR's advertising campaign provider, Fahlgren Mortine was provided a number of tasks in an effort to rebrand the Raze campaign. Among them, was redoing the website and crew management system.

## The Challenge

Raze had an existing crew management system and public-facing website, but it was getting old, and had become unweildly to maintain and use. They needed something more modern, more robust, and easier to use and manage. They needed something tailored to their needs, instead of an off-the-shelf solution that needed to be hacked around and have dozens of add-ons tacked on.

## The Solution

Instead of going with another off-the-shelf solution, we decided to build a custom system from the ground up. This would allow us to provide them with only what they need, and provide it when they need it.

### The Tech

In order to keep the codebase maintainable, we used the MVC framework, [Laravel](http://laravel.com/), as the backbone of the application. Combined with the PHP package management system, [Composer](http://getcomposer.org/), this allows us to swap out certain parts (particularly third-party libraries) nearly at will, without much consequence to the application as a whole.

[![Stylized tooltips to add that application feel.](/images/portfolio/thumbs/raze_announcement_tooltip.jpg)](/images/portfolio/raze_announcement_tooltip.jpg)

To make development of the interface faster and easier, the dashboard interface was built with the help of [Bootstrap](http://getbootstrap.com/). This allowed us to spend less time on building interface components and making them look good, and more time putting them together into a user-friendly interface. It also allowed us to add small garnishes, such as stylized tooltips, for browsers that support the extra features.

Even with the help of Bootstrap and Laravel, we still found ourselves using quite a bit of JavaScript, as well as a fair amount of CSS customization. To help keep these maintainable, and to allow us to generate minimized JavaScript and CSS files, we used the CSS preprocessor, [Sass](http://sass-lang.com/), and the [Node.js](http://nodejs.org/)-based task runner, [Grunt](http://gruntjs.com/).

### The Logic

While we also redid the public facing site ([razewv.com](https://razewv.com)), the dashboard interface at [razewv.com/manage](https://razewv.com/manage) is where the bulk of the work, and the heavy lifting, are done.

[![The Raze Dashboard](/images/portfolio/thumbs/raze_dashboard.jpg)](/images/portfolio/raze_dashboard.jpg)

At its core, it's a user and event management system. Adults and students sign up and join their crews. Adult advisors and crew leaders can schedule commotions based on pretermined choices, and can register for region and organization-wide events (such as Regional Raze Kickoff Events). When the commotions are completed and logged, the system tallies up the crew's total points, and standing compared to other crews, based on the point values of the commotions they performed.

Site Administrators can also generate reports for various statistics, in addition to taking suggestions for, and adding, new commotions, scheduling events, and sending announcements.

## Final Thoughts

This was one of our first built-from-scratch content management systems, so one of the biggest lessons was that such systems are quite a bit larger than they appear.

It was a fun project, though, and really allowed us to stretch our legs when it came to Laravel. It also allowed us to start incorporating some of the automation capabilities of Grunt, which will prove to be invaluable in future projects.