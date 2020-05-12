from aiohttp import web
from .errors_handler import ClientErrorHandler, ServerErrorsHandler, CustomErrorsHandler

routes = web.RouteTableDef()

