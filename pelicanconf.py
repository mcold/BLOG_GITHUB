#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael Cold'
SITENAME = u'A little bit about anything'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'Russian'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#          ('python', 'http://python.org/')
# Blogroll
LINKS = (#('pelican', 'http://getpelican.com/'),
	 ('python', '/category/python.html'),
	 ('django', '/category/django.html'),
	 #('git', 'https://github.com/mcold'),
	 ('perl', '/category/perl.html'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = 'min-pelican-theme'