from aiohttp.web import HTTPFound, HTTPNotFound, Request, Response
from yarl import URL

from melody.web.core import routes
from melody.web.constants import GITHUB_LINK
from melody.web.utils import check_back, identifier

GITHUB = URL(GITHUB_LINK)

NAME = "name"

GITHUB_ROUTE = f"/github/{identifier(NAME)}"


@routes.get(GITHUB_ROUTE)
async def handle_github(request: Request) -> Response:
    name = request.match_info[NAME]

    if check_back(name):
        raise HTTPNotFound()

    raise HTTPFound(GITHUB / name)
