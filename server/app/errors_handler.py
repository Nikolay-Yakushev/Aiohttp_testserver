from aiohttp import web


class ErrorsHandler(web.HTTPException):

    @staticmethod
    async def not_found():  # 404
        return web.HTTPNotFound()

    @staticmethod
    async def bad_request():  # 400
        return web.HTTPBadRequest()

    @staticmethod
    async def not_implemented():  # 501
        return web.HTTPNotImplemented()

    @staticmethod
    async def internal_error():  # 500
        return web.HTTPInternalServerError()
