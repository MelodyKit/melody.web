from aiohttp.web import HTTPNotFound, Request, Response

from melody.web.constants import KEY_SUFFIX, KEYS, TEXT_PLAIN
from melody.web.core import routes
from melody.web.utils import check_back, identifier

NAME = "name"

KEYS_ROUTE = f"/keys/{identifier(NAME)}"


@routes.get(KEYS_ROUTE)
async def handle_keys(request: Request) -> Response:
    name = request.match_info[NAME]

    if check_back(name):
        raise HTTPNotFound()

    path = (KEYS / name).with_suffix(KEY_SUFFIX)

    if path.exists():
        return Response(content_type=TEXT_PLAIN, text=path.read_text())

    raise HTTPNotFound()
