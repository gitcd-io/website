#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Claudio Walser'
SITENAME = 'GITCD Website'
SITEDESCRIPTION = 'This is an info page about gitcd. Mainly about its installation and usage.'
SITEURL = 'https://www.gitcd.io'

# plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites', 'tipue_search']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = './pelican-fh5co-marble'
I18N_GETTEXT_LOCALEDIR = './pelican-fh5co-marble/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Europe/Zurich'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# content paths
PATH = 'content'
PAGE_PATHS = ['pages/en']
ARTICLE_PATHS = ['blog/en']

# logo path, needs to be stored in PATH Setting
LOGO = '/images/logo.svg'

# special content
HERO = [
  {
    'image': '/images/hero/background-1.jpg',
    # for multilanguage support, create a simple dict
    'title': 'How to install',
    'text': 'Read detailed instruction about the installation of gitcd.',
    'links': [
      {
        'icon': 'icon-download',
        'url': '/pages/installation.html',
        'text': 'Installation'
      }
    ]
  }, {
    'image': '/images/hero/background-4.jpg',
    # keep it a string if you dont need multiple languages
    'title': 'How to use',
    # keep it a string if you dont need multiple languages
    'text': 'How about the usage of gitcd? Read about all it\'s features.',
    'links': [
      {
        'icon': 'icon-code-outline',
        'url': '/pages/cli.html',
        'text': 'Cli Usage'
      }
    ]
  }, {
    'image': '/images/hero/background-3.jpg',
    'title': 'It\'s about workflows',
    'text': 'For continuous integration, you need a proper workflow. Read here what works best for us.',
    'links': [
      {
        'icon': 'icon-code-outline',
        'url': '/pages/workflow.html',
        'text': 'Workflows'
      }
    ]
  }
]

# Social widget
SOCIAL = (
  ('Github', 'https://www.github.com/claudio-walser/gitcd'),
  ('Read the Docs', 'https://gitcd.readthedocs.io/en/latest/?badge=latest'),
  ('Travis CI', 'https://travis-ci.org/claudio-walser/gitcd')
)

ABOUT = {
  'image': '/images/about/about.jpeg',
  'mail': 'info@gitcd.io',
  # keep it a string if you dont need multiple languages
  'text': 'Drop me a message if you like.',
  'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'Zürich, Switzerland'
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  ('Contact', 'contact.html')
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
  'contact' # needed for the contact form
]

# setup disqus
DISQUS_SHORTNAME = 'gitcd'
DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page

# setup google maps
GOOGLE_MAPS_KEY = 'AIzaSyCYepGkax6lv4UTfTCF6980IUNvVjbhMdA'


# def createIconsFile():
#   filename = 'output/theme/css/icomoon.css'
#   with open(filename) as file:
#     content = file.read()
#     lines = content.split("\n")
#     icons = []
#     for line in lines:
#       if line.startswith('.icon-'):
#         lineParts = line.split(':')
#         iconClass = lineParts[0].replace('.icon-', 'icon-')

#         icons.append(iconClass)
#     return icons

# ICONS = createIconsFile()
