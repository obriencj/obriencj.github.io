# Primary site build configuration using Pelican

import logging
import datetime


AUTHOR = "Christopher O'Brien"
SITENAME = 'obriencj'
SITESUBTITLE = "selfish as a shellfish"
SITEURL = 'https://obriencj.preoccupied.net'


LICENSE_NAME = "CC BY-SA 4.0"
LICENSE_URL = "https://creativecommons.org/licenses/by-sa/4.0"

COPYRIGHT = f"2014-{datetime.datetime.now().year}, {AUTHOR}"

SITE_LICENSE = f"""
&copy; {COPYRIGHT},
<a property="http://creativecommons.org/ns#license"
   rel="license" href="{LICENSE_URL}">{LICENSE_NAME}</a>
"""


LANDING_PAGE_TITLE = "Christopher O'Brien"

FEATURED_IMAGE = None  # TODO


GOOGLE_ANALYTICS = None  # "UA-47351906-2"
MODERN_GOOGLE_ANALYTICS = "G-82F89XX3FD"


THEME = 'inelegant'

PATH = 'content'
OUTPUT_PATH = 'output'

RELATIVE_URLS = True


TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en-US'
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = [
    '404', 'index', 'archives', 'tags', 'categories', 'pages',
]

DEFAULT_PAGINATION = 0

RECENT_ARTICLE_SUMMARY = True


PROJECTS_TITLE = "Projects"
PROJECTS = [
    {
        "name": "koji-smoky-dingo",
        "url": "https://github.com/obriencj/koji-smoky-dingo",
        "description": "Client utilities for the koji build system",
    },
    {
        "name": "pelican-inelegant",
        "url": "https://github.com/obriencj/pelican-inelegant",
        "description": "Containerized pelican theme used by this site",
    },
]


# Social widget
SOCIAL_PROFILE_LABEL = "Social"

SOCIAL = (
    # ( 'GMail', 'mailto://obriencj@gmail.com', ),
    ( 'GitHub', 'https://github.com/obriencj', ),
    ( 'Keybase', 'https://keybase.io/obriencj', ),
    ( 'Mastodon', 'https://fosstodon.org/@obriencj', ),
    # ( 'Twitter', 'https://twitter.com/obriencj', ),
    ( 'Instagram', 'https://instagram.com/obriencj.preoccupied', ),
    ( 'Strava', 'https://strava.com/athletes/obriencj', ),
)


# site-wide features
APPLAUSE_BUTTON = False
DISPLAY_FEEDS_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False


PATH_METADATA = '(?P<dirname>.*/?)(?P<basename>.*)\.md'


ARTICLE_PATHS = [ 'blog', ]
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


PAGE_PATHS = [
    'about', 'about.md', 'landing.md', 'projects', 'projects.md',
]
PAGE_URL = '{dirname}{basename}/'
PAGE_SAVE_AS = '{dirname}{basename}/index.html'


STATIC_PATHS = [
    'CNAME', 'favicon.ico', 'gpg', 'images', 'keybase.txt',
    'photos', 'robots.txt', 'theme',
]


PLUGIN_PATHS = [ "/pelican/plugins", ]
PLUGINS = [
    "extract_toc", "image_process", "liquid_tags",
    "summary", "yaml_metadata",
]


# the image-process plugin
IMAGE_PROCESS = {
    "inline": {
        # inline images in horizontal mode
        "type": "image",
        "ops": ["scale_out 300 225 True"],
    },
    "upline": {
        # inline images in portrait mode
        "type": "image",
        "ops": ["scale_out 225 300 True"],
    },
}

IMAGE_PROCESS_DIR = "processed"
IMAGE_PROCESS_COPY_EXIF_TAGS = True


# liquid tags plugin settings
LIQUID_TAGS = [
    "img", "literal", "video", "youtube",
    "vimeo", "include_code",
]


# summary plugin settings
SUMMARY_BEGIN_MARKER = "<!-- summary -->"
SUMMARY_END_MARKER = "<!-- more -->"


# markdown extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.abbr": {},
        "markdown.extensions.attr_list": {},
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
            "guess_lang": False,
            "pygments_style": "default",
            "use_pygments": True,
        },
        "markdown.extensions.def_list": {},
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.footnotes": {},
        "markdown.extensions.toc": {
            "marker": "[TOC]",
            "permalink": "",
        },
    },
    "output_format": "xhtml",
}


# this is very annoying
LOG_FILTER = [(logging.WARN, 'Empty alt attribute for image %s in %s')]


CACHE_CONTENT = True
CACHE_PATH = ".cache"
LOAD_CONTENT_CACHE = True


# The end.
