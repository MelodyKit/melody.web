from fastapi import status
from fastapi.responses import RedirectResponse

from melody.kit.core import app

ROOT = "/"

DISCORD_NAME = "discord"

DISCORD_LINK = "https://discord.com/invite/NeKqH6ng2G"

GITHUB_NAME = "github"
REDDIT_NAME = "reddit"
X_NAME = "x"
YOUTUBE_NAME = "youtube"
TELEGRAM_NAME = "telegram"
DOCS_NAME = "docs"
DEV_NAME = "dev"

INTRO_NAME = "intro"

GITHUB_LINK = "https://github.com/MelodyKit"
REDDIT_LINK = "https://reddit.com/r/MelodyKit"
X_LINK = "https://x.com/MelodyKitApp"
YOUTUBE_LINK = "https://youtube.com/MelodyKit"
TELEGRAM_LINK = "https://t.me/MelodyKitApp"
DOCS_LINK = "https://docs.melodykit.app/"
DEV_LINK = "https://dev.melodykit.app/"

INTRO_LINK = "https://youtu.be/dQw4w9WgXcQ"

NAME_TO_LINK = {
    DISCORD_NAME: DISCORD_LINK,
    GITHUB_NAME: GITHUB_LINK,
    REDDIT_NAME: REDDIT_LINK,
    X_NAME: X_LINK,
    YOUTUBE_NAME: YOUTUBE_LINK,
    TELEGRAM_NAME: TELEGRAM_LINK,
    DOCS_NAME: DOCS_LINK,
    DEV_NAME: DEV_LINK,
    INTRO_NAME: INTRO_LINK,
}


def create_redirect(name: str, link: str) -> None:
    @app.get(ROOT + name)
    async def _redirect() -> RedirectResponse:
        return RedirectResponse(link, status_code=status.HTTP_302_FOUND)


for name, link in NAME_TO_LINK.items():
    create_redirect(name, link)
