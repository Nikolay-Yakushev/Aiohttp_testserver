import os

import aiofiles
from aiohttp import web
from werkzeug.utils import secure_filename
from . import e_handler


async def _size(request):
    upload_folder = request.app['config'].get('upload_folder')
    file_searched = request.rel_url.query['file']

    if file_searched:
        path_to_file = os.path.join(upload_folder, file_searched)

        if not path_to_file:
            return await e_handler.internal_error()

        file_size = os.path.getsize(path_to_file)
        return web.json_response({'info': {'filename': f' {file_searched}', 'size(bytes)': f'{file_size}'}})
    else:
        await e_handler.bad_request()


async def _upload(request):
    upload_folder = request.app['config'].get('upload_folder')
    reader = await request.multipart()

    if not reader:
        return await e_handler.bad_request()

    field = await reader.next()
    file_searched = field.name

    if file_searched == 'file':
        filename = secure_filename(field.filename)
        response = await write_file(upload_folder, filename, field)

        if response is None:
            return await e_handler.internal_error()

        return response


async def write_file(upload_folder, filename, field):
    try:
        async with aiofiles.open(os.path.join(upload_folder, filename), 'wb') as infile:
            while True:
                chunk = await field.read_chunk(8192)
                if not chunk:
                    break
                await infile.write(chunk)
        return web.json_response({'info': {'filename': f'{filename}', 'status': 'uploaded'}})
    except:
        return None


async def _download(request):
    upload_folder = request.app['config'].get('upload_folder')
    file_searched = request.rel_url.query['file']

    if file_searched:
        async with aiofiles.open(os.path.join(upload_folder, file_searched), mode='r') as outfile:
            content = await outfile.read()
        return web.Response(text=f'{content}\n\n')

    else:
        return await e_handler.bad_request()
