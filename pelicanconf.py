AUTHOR = "Iain Dillingham"
SITENAME = "Iain Dillingham"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = PAGE_URL

ARTICLE_TRANSLATION_ID = None
PAGE_TRANSLATION_ID = None

THEME = "theme"
THEME_STATIC_DIR = "theme"
CSS_FILE = "theme.css"

TYPOGRIFY = True
