#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Claudio Walser'
SITENAME = 'GITCD'
SITEDESCRIPTION = 'GITCD - continuous delivery with git'
SITEURL = ''
# THEME = 'pelican-striped-html5up'
# THEME = 'twenty-html5up'
# THEME = 'html5-dopetrope'
# sTHEME = 'clean-blog'
# THEME = 'attila'
# THEME = 'pelican-blue'
THEME = 'pelican-marble'

PATH = 'content'
# logo path, needs to be stored in PATH Setting
LOGO = 'images/logo.svg'

TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = 'en'

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

# MENUITEMS = [('Archives', 'archives.html')]


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
  ('Github', 'https://www.github.com/claudio-walser/gitcd'),
  ('Read the Docs', 'https://gitcd.readthedocs.io/en/latest/?badge=latest'),
  ('Travis', 'https://travis-ci.org/claudio-walser/gitcd'),

  # ('Google Plus', 'https://plus.google.com/+ClaudioWalser'),
  # ('Twitter', 'https://www.twitter.com/claudio-walser'),
)

ABOUT = {
  'image': 'images/about.jpeg',
  'mail': 'info@gitcd.io',
  'text': 'Learn more about the creator of gitcd or just drop a message.',
  'link': 'pages/contact.html'
}

HERO = [
  {
    'image': '/images/hero1-backround.jpg',
    'title': 'my first hero title',
    'text': 'check this out',
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

DEFAULT_PAGINATION = False


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