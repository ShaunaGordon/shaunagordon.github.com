#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shauna Gordon'
SITENAME = 'I Make Things'
SITEURL = 'http://shaunagordon.com'

PATH = 'content'

ARTICLE_PATHS = ['posts']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Delete the contents of the output directory...
DELETE_OUTPUT_DIRECTORY = False

# ...but save the git stuff
OUTPUT_RETENTION = ('.git', '.gitignore')

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['clean_summary', 'collate_content', 'feed_summary', 'footer_insert', 'extract_toc', 'related_posts', 'simple_footnotes', 'share_post', 'summary', 'disqus_static', 'liquid_tags.img','liquid_tags.include_code']
MARKDOWN = {
    'extensions': ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc'],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'}
    },
    'output_format': 'html5'
}

# Theme
THEME = 'elegant'

# Theme Settings
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images', 'images/portfolio', 'images/portfolio/thumbs']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Blogroll
LINKS = (('Resume', 'http://goo.gl/JAjeZ'), ('Soap Shop', 'http://herbncountrysoaps.com'),
        )

# Social widgets
SOCIAL = (('Github', 'https://github.com/ShaunaGordon'),
          ('Twitter', 'https://twitter.com/gordondev')
          )

TWITTER_USERNAME = 'gordondev'

# Comments
DISQUS_SITENAME = 'gordondev'
DISQUS_SECRET_KEY = '0PW94yUQI1gqM7sGUSBNrKXIjtxnbyPeHLvuYjPmIgWJJcCqs72AHhyT4pvDndW1'
DISQUS_PUBLIC_KEY = 'Mcno1Ros11yHwHrV5YpexWEaBOA1Tfb2CfRRuiABYMiyHphh83o4BxXudq0ysNw6'

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = False

# Special theme content

# Landing page content
LANDING_PAGE_ABOUT = {'title': 'I Make Things.','details': "<p>What kinds of things? All kinds of things.</p><p>I'm a software developer by trade and a crafter by passion. In the digital world, I generally build web applications, while in the real world, I've been known to bake, make soap, crochet, and more.</p><p>While I used to confine this blog to tech and tech business, I've decided to open it up to include my crafting and the business(es) I'm creating with that. So, now this blog will have all manner of topics, from mental health and disability to entrepreneurship and business management to tech, gaming, and other nerdy endeavors.</p>"}

# Site License
SITE_LICENSE = '<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br />This work by <a xmlns:cc="http://creativecommons.org/ns#" href="http://shaunagordon.com" property="cc:attributionName" rel="cc:attributionURL">Shauna Gordon</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.'