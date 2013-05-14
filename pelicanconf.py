#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'atzorvas'
SITENAME = u"atzorvas' space"
SITEURL = 'http://tzorvas.com'
DISQUS_SITENAME = "tzorvas"
TWITTER_USERNAME = "atzorvas"
GITHUB_URL = "https://github.com/atzorvas/tzorvas.com"
#GOOGLE_ANALYTICS = "UA-40901002-1"
DEFAULT_PAGINATION = 5

TIMEZONE = 'Europe/Athens'
DEFAULT_LANG = u'en'
THEME = "theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
#FEED_ALL_RSS = 'rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('ICSD', 'http://www.icsd.aegean.gr/'),
		  ("OSArena.net", 'http://osarena.net'),)

# Social widget
SOCIAL = (('facebook', 'http://facebook.com/atzorvas'),
          ('twitter', 'http://twitter.com/atzorvas'),
          ('linkedin', 'http://gr.linkedin.com/in/atzorvas'),
          ('github', 'http://github.com/atzorvas'),)


MENUITEMS = (('archives', 'http://tzorvas.com/archives.html'),)
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}/index.html"
DEFAULT_CATEGORY = "posts"
CATEGORY_URL = "{slug}"
CATEGORY_SAVE_AS = "{slug}/index.html"

#PDF_GENERATOR = True
#PDF_STYLE = "twelvepoint"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True