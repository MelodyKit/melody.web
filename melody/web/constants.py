from pathlib import Path

ROOT = Path(__file__).parent

ROOT_ROUTE = "/"

TEXT_HTML = "text/html"
TEXT_PLAIN = "text/plain"

BASE_NAME = "base.html"
HOME_NAME = "home.html"

CSS_NAME = "css"
KEYS_NAME = "keys"
STATIC_NAME = "static"
TEMPLATES_NAME = "templates"

KEY_SUFFIX = ".key"

KEYS = ROOT / KEYS_NAME
STATIC = ROOT / STATIC_NAME
CSS = STATIC / CSS_NAME
TEMPLATES = ROOT / TEMPLATES_NAME

DEFAULT_INPUT_NAME = "input.css"
DEFAULT_OUTPUT_NAME = "output.css"

DEFAULT_INPUT = CSS / DEFAULT_INPUT_NAME
DEFAULT_OUTPUT = CSS / DEFAULT_OUTPUT_NAME

EMAIL_TO = "mailto:"
DOMAIN = "melodykit.app"

EMAIL = "{}@{}"

DOCS_LINK = "https://melodykit.github.io/"

DISCORD_NAME = "discord"

DISCORD_LINK = "https://discord.com/invite/NeKqH6ng2G"

GITHUB_NAME = "github"
REDDIT_NAME = "reddit"
TWITTER_NAME = "twitter"
YOUTUBE_NAME = "youtube"

INTRO_NAME = "intro"

GITHUB_LINK = "https://github.com/MelodyKit"
REDDIT_LINK = "https://reddit.com/r/MelodyKit"
TWITTER_LINK = "https://twitter.com/MelodyKit"
YOUTUBE_LINK = "https://youtube.com/MelodyKit"

INTRO_LINK = "https://youtu.be/dQw4w9WgXcQ"

NAME_TO_LINK = {
    DISCORD_NAME: DISCORD_LINK,
    GITHUB_NAME: GITHUB_LINK,
    REDDIT_NAME: REDDIT_LINK,
    TWITTER_NAME: TWITTER_LINK,
    YOUTUBE_NAME: YOUTUBE_LINK,
    INTRO_NAME: INTRO_LINK,
}

DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 1369

DEFAULT_NAME = "web"
