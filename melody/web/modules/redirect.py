from aiohttp.web import HTTPFound, Request, Response

from melody.web.constants import NAME_TO_LINK, ROOT_ROUTE
from melody.web.core import routes
from melody.web.typing import Handler


def create_redirect(name: str, link: str) -> Handler:
    @routes.get(ROOT_ROUTE + name)
    async def handle_redirect(request: Request) -> Response:
        raise HTTPFound(link)

    return handle_redirect  # type: ignore


for name, link in NAME_TO_LINK.items():
    create_redirect(name, link)
