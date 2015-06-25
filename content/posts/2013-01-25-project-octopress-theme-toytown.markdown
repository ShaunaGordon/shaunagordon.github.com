title: Project: Octopress Theme Toytown
date: 2013-01-25 09:51
category: project
tags: community contribution, projects
slug: project-octopress-theme-toytown

[TOC]

As part of yet another redesign and blog migration, I needed to create a theme that wasn't so stock. I migrated my site to [Octopress](http://octopress.org/), a blogging platform that runs on GitHub's [Jekyll](http://jekyllrb.com/) static site generator. It's a great platform, as anyone who follows my Twitter or Google+ accounts is aware, but the vast majority of sites that run on Octopress use the default theme, or some slight variation thereof. As good and nice as the default theme is, it's become very generic. I needed something different.
<!-- more -->

## Why "Toytown"?

The entire theme is based around the image in the background. That image is actually one of the views I get to see in the mornings and evenings when I go to and leave from work.

You see, my office is located in one of the biggest shopping districts in the city, and it's pretty unique in that it's built as a blend between an indoor shopping mall and street-facing shops. Every year for the holidays (and evidently, well into the new year, for whatever reason), they string up lights on every building. It always reminds me of a gingerbread town, because of the way the lights are done - it's "warm" white rope lights lined along the corners and some other accent lines, much the same way you'd have the frosting on a gingerbread building. They also have a couple of giant Christmas trees in the main open areas to the north and south of the main "mall" area. I have no doubt that, if viewed from above, in, say, a helicopter, it would look more like something you'd find in a toy or model train store than an actual shopping center.

## The Keystone of the Theme

Combine the natural "toy-like" aspect of the area this time of year, with the view from a few dozen feet above ground level, and a little manipulation in Gimp to create a [tilt-shift miniature effect](http://www.inspiration.scottphotographics.com/amazing-miniature-tilt-shift-photography/), and you end up with a fun background that looks more like a model than a real place.

The first image I had of it wasn't as high quality as I'd like, due to having taken it with my smartphone, especially at the scale needed to adequately make it a background for a website. So, as much as I loved the image itself (because it was late enough in the morning to be "daytime", but you could still see the lights on the buildings), I decided to go out and take more pictures, this time with an actual camera. (Note: as of 1/25/13, the "first image" is still the one used. I don't have access to an SD card reader at the moment, so I can't get the pictures off of my camera.)

It's also this image that I derived the color theme from, with the aid of the wonderfully useful [Color Scheme Designer](http://colorschemedesigner.com). The entire theme actually consists of just three base colors, with which I played with shades, hues, and opacity to achieve the desired effects.

Ah, the joys of working in the digital realm.

## Layout

Since it's largely a blog these days (I still have my "About" page, which has the online version of my resume and will eventually sport the download options, as well, but the main focal point is the blog), I decided to stick with the two-column theme, allowing for various supplementary things, such as recent or related posts, tag clouds, and so forth.

Additionally, I've made the site responsive. Anything above a 920px wide screen (or its rought equivalent, as it also responds to text size; more on that later), will have a single-column experience, with the extra goodies at the bottom. As the viewport gets smaller, some items will even shift their layout entirely, to accommodate the typical touch input of what are typically smaller screens. I also drop out the background image entirely (or rather, I don't add it in until larger sizes), to help keep bandwidth lower on devices that are more likely to be on a connection where download size is important.

## 320 and Up? Kind of.

One of the big new paradigms in web development is what's known as "mobile first" development. Among the large frameworks and bootstrapping tools is [320 and Up](http://www.stuffandnonsense.co.uk/blog/about/this_is_the_new_320_and_up), which starts its <abbr title="Cascading Style Sheets">CSS</abbr> media query "breakpoints" with 320px wide (the most narrow viewport size that most modern smartphones use) and work up from there.
{% pullquote %}
But there's a major problem with it, and every other mobile-first framework out there currently - {" mobile devices lie about their pixel width "}. This is in part because a pixel isn't always a pixel. You see, in <abbr title="Cascading Style Sheets">CSS</abbr>, the unit "pixel" is actually a [standardized measurement](http://www.w3.org/TR/css3-values/#reference-pixel) based on the average viewing distance of the object (and actually, [all CSS units of measurement are based on this "reference pixel"](http://www.quirksmode.org/blog/archives/2012/11/the_css_physica.html)), whereas, in most other computer contexts (including images), a pixel is the smallest unit of measurement for a digital display. Until fairly recently, computers displayed at a pixel density of around 96<abbr title="Dots Per Inch">DPI</abbr>, making 1 CSS pixel roughly equivalent to 1 device pixel.
{% endpullquote %}
Until 1px no longer equals 1px.

This is exactly what we're seeing with the new high-density ("retina") displays, which have upwards of two or more times the number of Dots Per Inch as a 96<abbr title="Dots Per Inch">DPI</abbr> screen. To compound matters, these new devices don't have the same pixel densities. In fact, their densities are [all over the map](http://en.wikipedia.org/wiki/List_of_displays_by_pixel_density#Devices_by_manufacturers). 151, 132, 202, etc. Even if you go off of the "CSS pixel ratio", you still have 1, 1.325, 1.5, 2, and who-knows-what else in the future (and you *know* not all of the real pixel densities match well to the "CSS pixel ratio").

Oh yeah, and, in part because of the above, these devices basically lie about their resolutions. The "Retina" iPhones report their resolutions as half of what they actually are. Additionally, some devices will increase their font size, but report a resolution that looks like a desktop.

So what to do? [How about not use pixel-based media queries to begin with?](http://blog.cloudfour.com/the-ems-have-it-proportional-media-queries-ftw/) This has two added bonuses - you no longer have to worry about CSS pixel to device pixel differences, and you can adjust based on zoom level.

Go ahead, zoom in on the site. Isn't that cool?

It's one of the first projects I've actually done using the "mobile-first" paradigm, as well as using EMs, so it could probably use some polish, but it was fun to learn, and it even looks good on my Android devices.

## Other Technologies

### HTML5 and CSS

Since it's an Octopress theme, it makes heavy use of HTML5, [Sass](http://sass-lang.com), and [Compass](http://compass-style.org/). I didn't do much with the HTML (I didn't need to), but I rewrote the CSS to better fit my programming style and make it simpler to do a simple color scheme change, without having to guess at the variable names.

There is also a fair amount of CSS3 thrown into the mix, with a couple of transitions (namely, mouseover effects for the links), some rounded corners, and alpha-transparent backgrounds.

### Ruby and YAML

Most of this section doesn't really relate to the theme itself, but since building the theme was part of the project of redoing my site, I'm just going to include this, as well. The theme itself really only needs the HTML and CSS related stuff.

Since GitHub is a Ruby shop, it's only natural that Jekyll and, by extension, Octopress are Ruby based. I didn't delve a whole lot into the Ruby code, but I did use it a little to customize a couple of plugins I found (incidentally, before I found better ones), and to add a little template logic into the header section, to display things like a link to GitHub, or a "Highlights" page (in my case, I used the "Highlights" page to list all entries under the "projects" category). I also added a couple entries to the Gemfile to add the GSL and Classifier gems to the Bundler install script, so that I could make use of the "related posts" capabilities of Jekyll.

The configuration is all done through YAML files, which, of course, requires editing them so that things work as I want them to. This includes defining a separate set of sidebar widgets for the individual post view page vs the list view page, adding my own configuration options for the theme, and activating the "related posts" plugin. I also added an abbreviations plugin, which contains a list of known abbreviations and wraps any it finds in posts or pages in `<abbr>` tags. I've added significantly to this list, so that it covers more abbreviations.

## Conclusion

[The theme is up on GitHub](https://github.com/ShaunaGordon/octopress-theme-toytown), so feel free to fork it and play around with it. I made it largely for personal use, so I have next to no documentation for it, but I've tried to make it simple enough that it should be easy to modify. It's also probably going to be an evolving project, as I find things I don't like or are broken entirely. All in all, it's been a fun project so far, though.