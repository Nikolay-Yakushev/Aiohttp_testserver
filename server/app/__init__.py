from aiohttp import web
from .errors_handler import ClientErrorHandler, ServerErrorsHandler

routes = web.RouteTableDef()
client_err_handler = ClientErrorHandler
server_err_handler = ServerErrorsHandler

