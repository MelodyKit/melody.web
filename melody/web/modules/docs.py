from aiohttp.web import HTTPFound, HTTPNotFound, Request, Response
from yarl import URL

from melody.web.constants import DOCS_LINK
from melody.web.core import routes
from melody.web.utils import check_back, identifier

NAME = "name"

DOCS_ROUTE = f"/docs/{identifier(NAME)}"

DOCS = URL(DOCS_LINK)


@routes.get(DOCS_ROUTE)
def handle_docs(request: Request) -> Response:
    name = request.match_info[NAME]

    if check_back(name):
        raise HTTPNotFound()

    raise HTTPFound(DOCS / name)
