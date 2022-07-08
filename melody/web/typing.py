from typing import Awaitable, Callable, TypeVar

from aiohttp.web import Request, Response, StreamResponse

__all__ = (
    "Unary",
    "Binary",
    "GenericHandler",
    "GenericMiddleware",
    "StreamHandler",
    "StreamMiddleware",
    "Handler",
    "Middleware",
)

T = TypeVar("T")
U = TypeVar("U")
R = TypeVar("R")

Unary = Callable[[T], R]
Binary = Callable[[T, U], R]

In = TypeVar("In", bound=Request)
Out = TypeVar("Out", bound=StreamResponse)

GenericHandler = Unary[In, Awaitable[Out]]
GenericMiddleware = Binary[In, GenericHandler[In, Out], Awaitable[Out]]

StreamHandler = GenericHandler[Request, StreamResponse]
StreamMiddleware = GenericMiddleware[Request, StreamResponse]

Handler = GenericHandler[Request, Response]
Middleware = GenericMiddleware[Request, Response]
