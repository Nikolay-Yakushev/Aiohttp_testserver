import os
import sys

import aiofiles
from aiohttp import web
from werkzeug.utils import secure_filename

from . import upload_folder


async def _size(request):
    file_searched = request.rel_url.query['file']
    try:
        path_to_file = os.path.join(upload_folder, file_searched)
        os.path.getsize(path_to_file)
        web.Response(text=f'{os.path.getsize(path_to_file)}')
    except Exception as e:
        print(e)


async def _upload(request):
    reader = await request.multipart()
    field = await reader.next()
    file_searched = field.name
    if file_searched == 'file':
        filename = secure_filename(field.filename)
        response = await write_file(filename, field)
        return response


async def write_file(filename, field):
    file_size = 0
    async with aiofiles.open(os.path.join(upload_folder, filename), 'wb') as infile:
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            # file_size += len(chunk)
            await infile.write(chunk)

    return web.Response(text=f'{filename}has been successfully stored\n')


async def _download(request):
    file_searched = request.rel_url.query['file']
    try:
        for root, dirs, files in os.walk(upload_folder):
            if file_searched in files:
                async with aiofiles.open(os.path.join(upload_folder, file_searched), mode='r') as outfile:
                    content = await outfile.read()
                return web.Response(text=f'{content}')


    except FileNotFoundError:
        web.Response(text='file not found')
