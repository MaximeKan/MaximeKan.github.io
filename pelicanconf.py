#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'MaximeKan'
SITENAME = 'Data Science for Movies'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('tags', '/tags.html'))

# Social widget
SOCIAL = (('GitHub', 'https://github.com/MaximeKan'),
          ('StackOverflow', 'https://stackoverflow.com/users/10956606/maximekan?tab=profile'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
#PLUGINS = ['ipynb.markup', 'i18n_subsites']

#CUSTOM_ARTICLE_FOOTERS = ("taglist.html")

THEME = '/Users/maxime/Movies_DS/pelican-themes/voidy-bootstrap' #fresh is also good
#JINJA_ENVIRONMENT = {
#    'extensions': ['jinja2.ext.i18n'],
#}
#THEME = 'notmyidea'
#THEME = '/Users/maxime/Movies_DS/pelican-themes/notmyidea-cms'
