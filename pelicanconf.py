#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Claudio Walser'
SITENAME = 'GITCD'
SITEDESCRIPTION = 'GITCD - continuous delivery with git'
SITEURL = 'http://10.20.1.71'
# THEME = 'pelican-striped-html5up'
# THEME = 'twenty-html5up'
# THEME = 'html5-dopetrope'
# sTHEME = 'clean-blog'
# THEME = 'attila'
# THEME = 'pelican-blue'
THEME = 'pelican-marble'
# THEME = 'flex'
# THEME = 'graymill'

PATH = 'content'
# logo path, needs to be stored in PATH Setting
LOGO = '/images/logo.svg'

TIMEZONE = 'Europe/Zurich'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'
DISQUS_SHORTNAME = 'gitcd-dev'
DISQUS_ON_PAGES = False

PYGMENTS_RST_OPTIONS = {}

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites', 'tipue_search']
# PLUGINS = ['tipue_search']

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search',
  'contact'
]

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_GETTEXT_LOCALEDIR = '../pelican-marble/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True

I18N_TEMPLATES_LANG = 'de_DE'
DEFAULT_LANG = 'de'
LOCALE = 'de_DE'
I18N_SUBSITES = {
  'en': {
    'PAGE_PATHS': ['pages/en'],
    'ARTICLE_PATHS': ['blog/en']
  }, 'fr': {
    'PAGE_PATHS': ['pages/fr'],
    'ARTICLE_PATHS': ['blog/fr']
  }, 'es': {
    'PAGE_PATHS': ['pages/es'],
    'ARTICLE_PATHS': ['blog/es']
  }
}

PAGE_PATHS = ['pages/de']
ARTICLE_PATHS = ['blog/de']

MENUITEMS = [
  ('Archive', 'archives.html'),
  ('Contact', 'contact.html')
]

# Blogroll
LINKS = (
  ('Pelican', 'http://getpelican.com/'),
  ('Python.org', 'http://python.org/'),
  ('Jinja2', 'http://jinja.pocoo.org/'),
  ('You can modify those links in your config file', '#')
)

# Social widget
SOCIAL = (
  ('Github', 'https://www.github.com/claudio-walser/gitcd'),
  ('Read the Docs', 'https://gitcd.readthedocs.io/en/latest/?badge=latest'),
  ('Travis', 'https://travis-ci.org/claudio-walser/gitcd')
)

ABOUT = {
  'image': '/images/about.jpeg',
  'mail': 'info@gitcd.io',
  'text': {
    'en': 'Learn more about the creator of gitcd or just drop a message.',
    'de': 'Lesen Sie mehr über den Entwickler von gitcd oder lassen Sie mir eine Nachricht da.',
    'fr': 'je suis derrier'
  },
  'link': 'contact.html',
  'address': 'Zürich, Schweiz',
  'phone': '15552236'
}

HERO = [
  {
    'image': '/images/hero1-backround.jpg',
    'title': {
      'en' :'my first hero title',
      'de' :'Das ist ein Top Titel'
    },
    'text': {
      'en': 'Learn more about the creator of gitcd or just drop a message.',
      'de': 'Lesen Sie mehr über den Entwickler von gitcd oder lassen Sie mir eine Nachricht da.',
    },
    'links': [
      {
        'icon': 'icon-code',
        'url': 'https://github.com',
        'text': 'Github'
      }
    ]
  }, {
    'image': '/images/hero2-backround.jpg',
    'title': 'something else',
    'text': 'well well well',
    'links': []
  }, {
    'image': '/images/hero3-backround.jpg',
    'title': 'hui',
    'text': 'buh',
    'links': []
  }, {
    'image': '/images/hero4-backround.jpg',
    'title': 'grappelensee',
    'text': 'in hd colors',
    'links': []
  }
]

DEFAULT_PAGINATION = 2

GOOGLE_MAPS_KEY = 'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'

def createIconsFile():
  filename = 'output/theme/css/icomoon.css'
  icons = []
  if not os.path.isfile(filename):
    return icons
  with open(filename) as file:
    content = file.read()
    lines = content.split("\n")
    for line in lines:
      if line.startswith('.icon-'):
        lineParts = line.split(':')
        iconClass = lineParts[0].replace('.icon-', 'icon-')

        icons.append(iconClass)
    return icons

ICONS = createIconsFile()

def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'

  JINJA_FILTERS = {'sidebar': sidebar}