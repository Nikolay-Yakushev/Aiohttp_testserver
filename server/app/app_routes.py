from . import routes
from aiohttp import web
from .app_logic import _upload, _download, _size


@routes.post('/upload')
async def upload(request):
    if request.method == 'POST':
        response = await _upload(request)
        return response


@routes.get('/hello')
async def upload(request):
    return web.Response(text='hello world')


@routes.get('/download')
async def download(request):
    if request.method == 'GET':
        data = await _download(request)
        return data


@routes.get('/size')
async def size(request):
    if request.method == 'GET':
        data = await _size(request)
        return data
