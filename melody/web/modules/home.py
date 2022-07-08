from aiohttp.web import Request, Response

from melody.web.constants import HOME_NAME, ROOT_ROUTE, TEXT_HTML
from melody.web.core import environment, routes

template = environment.get_template(HOME_NAME)


@routes.get(ROOT_ROUTE)
async def home(request: Request) -> Response:
    return Response(content_type=TEXT_HTML, text=await template.render_async())
