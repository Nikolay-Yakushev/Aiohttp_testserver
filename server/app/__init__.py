from aiohttp import web
from .errors_handler import ErrorsHandler

routes = web.RouteTableDef()
e_handler = ErrorsHandler

