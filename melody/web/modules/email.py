from aiohttp.web import HTTPFound, Request, Response

from melody.web.constants import DOMAIN, EMAIL, EMAIL_TO
from melody.web.core import routes
from melody.web.utils import identifier

NAME = "name"
EMAIL_ROUTE = f"/email/{identifier(NAME)}"


@routes.get(EMAIL_ROUTE)
def handle_docs(request: Request) -> Response:
    name = request.match_info[NAME]

    raise HTTPFound(EMAIL_TO + EMAIL.format(name, DOMAIN))
