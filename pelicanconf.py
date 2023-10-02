

AUTHOR = "Christopher O'Brien"
SITENAME = 'obriencj'
SITESUBTITLE = "selfish as a shellfish"
SITEURL = 'https://obriencj.preoccupied.net/'

LICENSE_NAME = "CC BY-SA 4.0"
LICENSE_URL = "https://creativecommons.org/licenses/by-sa/4.0/"

from datetime import datetime

COPYRIGHT = f"2014-{datetime.now().year}, {AUTHOR}"

SITE_LICENSE = f"""
&copy; {COPYRIGHT},
<a property="http://creativecommons.org/ns#license"
   rel="license" href="{LICENSE_URL}">{LICENSE_NAME}</a>
"""


THEME = 'inelegant'

PATH = 'content'
OUTPUT_PATH = 'output'

RELATIVE_URLS = True

GOOGLE_ANALYTICS = "UA-47351906-2"

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en-US'
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ['index', 'archives', 'tags', 'categories', 'pages']

DEFAULT_PAGINATION = 0

RECENT_ARTICLE_SUMMARY = True


FEATURED_IMAGE = None  # TODO

LANDING_PAGE_TITLE = "Christopher O'Brien"


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
SOCIAL = (
    ( 'GitHub', 'https://github.com/obriencj', ),
    ( 'Mastodon', 'https://fosstodon.org/@obriencj', ),
    ( 'Instagram', 'https://instagram.com/obriencj.preoccupied/', ),
)


GITHUB_URL = "https://github.com/obriencj/obriencj.github.io/"
GITHUB_USER = "obriencj"
GITHUB_REPO_COUNT = 0
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

DISPLAY_FEEDS_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

APPLAUSE_BUTTON = False


PATH_METADATA = '(?P<dirname>.*/)(?P<basename>.*)\.md'
EXTRA_PATH_METADATA = {
    'about.md': {
        'dirname': '',
        'basename': 'about'
    },
    'landing.md': {
        'dirname': '',
        'basename': 'landing'
    },
    'projects.md': {
        'dirname': '',
        'basename': 'projects'
    },
}


ARTICLE_PATHS = [ 'blog', ]
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_PATHS = [
    'about', 'about.md', 'landing.md', 'projects', 'projects.md',
]
PAGE_URL = '{dirname}{basename}/'
PAGE_SAVE_AS = '{dirname}{basename}/index.html'

STATIC_PATHS = [
    'CNAME', 'gpg', 'images', 'keybase.txt', 'photos',
    'robots.txt', 'theme',
]


PLUGIN_PATHS = [ "/pelican/plugins", ]
PLUGINS = [
    "extract_toc", "image_process", "liquid_tags",
    "summary", "yaml_metadata",
]


IMAGE_PROCESS = {
    "inline": {
        "type": "image",
        "ops": ["scale_out 300 225 True"],
    },
    "upline": {
        "type": "image",
        "ops": ["scale_out 225 300 True"],
    },
}

IMAGE_PROCESS_DIR = "processed"
IMAGE_PROCESS_COPY_EXIF_TAGS = True


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


# liquid tags plugin settings
LIQUID_TAGS = ["img", "literal", "video", "youtube",
               "vimeo", "include_code", ]

# summary plugin settings
SUMMARY_BEGIN_MARKER = "<!-- summary -->"
SUMMARY_END_MARKER = "<!-- more -->"


# The end.
