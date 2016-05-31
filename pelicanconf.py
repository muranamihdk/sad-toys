#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Takuboku'
SITENAME = 'Sad Toys'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# The Above is created by pelican-quickstart command.
# ---------------------------------------------
# The following is manually set for the site "Sad Toys".


# Settings only enabled during Developing
# ---------------------------------
#LOAD_CONTENT_CACHE = False
#DELETE_OUTPUT_DIRECTORY = True

# Common Settings
# ------------
#SLUGIFY_SOURCE = 'basename'
DEFAULT_DATE = 'fs'
LOCALE = 'en_US'

# Page Settings
# -----------
PAGE_PATHS = ['']
PAGE_EXCLUDES = ['resources']
PATH_METADATA= '(?P<path_no_ext>.*)\..*'
PAGE_SAVE_AS= '{path_no_ext}.html'
PAGE_URL= '{path_no_ext}.html'

# Article Settings
# --------------
ARTICLE_PATHS = ['diary']
ARTICLE_URL = 'diary/entries/{date:%Y}/{date:%b}/{slug}.html'
ARTICLE_SAVE_AS = 'diary/entries/{date:%Y}/{date:%b}/{slug}.html'

TAG_URL = 'diary/tag/{slug}.html'
TAG_SAVE_AS = 'diary/tag/{slug}.html'
CATEGORY_URL = 'diary/category/{slug}.html'
CATEGORY_SAVE_AS = 'diary/category/{slug}.html'
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']
INDEX_SAVE_AS = 'diary/index.html'
TAGS_SAVE_AS = 'diary/tags.html'
CATEGORIES_SAVE_AS = 'diary/categories.html'
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = 'diary/archives.html'
YEAR_ARCHIVE_SAVE_AS = 'diary/entries/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'diary/entries/{date:%Y}/{date:%b}/index.html'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'

ARTICLE_ORDER_BY = 'date'  #<-> reversed-date

# Themes
# -------
THEME = 'themes/gum'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Works', 'works/index.html'), ('Diary', 'diary/index.html'), ('Biography', 'bio.html'), ('About', 'about.html')]
#SITESUBTITLE = 'A subtitle to appear in the header.'
GITHUB_URL = 'https://github.com/muranamihdk/pelican-page-centered'

# Markdown Extensions
# ------------------
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'nl2br', 'sane_lists', 'denden_extension(footnote_sub=False)']

# Plugins
# ------
PLUGIN_PATHS = ['plugins']
PLUGINS = ['tag_cloud']

#https://github.com/getpelican/pelican-plugins/tree/master/tag_cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'size'  #random, alphabetically, alphabetically-rev, size, size-rev
TAG_CLOUD_BADGE = False
