import logging

from aiohttp import web
from aiologger import Logger
from aiologger.handlers.files import AsyncFileHandler

formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
logger = Logger.with_default_handlers(name='async-logger',
                                      level=logging.WARNING,
                                      formatter=formatter)

file_handler = AsyncFileHandler(filename='log_data.log')
logger.add_handler(file_handler)


class ClientErrorHandler(web.HTTPException):

    @staticmethod
    async def not_found(req_text):  # 404

        return web.HTTPNotFound()

    @staticmethod
    async def bad_request(req_text):
        await logger.warning(f'Failed due to {req_text}')
        return web.HTTPBadRequest(reason=req_text)  # 400


class ServerErrorsHandler(web.HTTPException):

    @staticmethod
    async def not_implemented():  # 501
        return web.HTTPNotImplemented()

    @staticmethod
    async def internal_error():  # 500
        return web.HTTPInternalServerError()
