import os
import aiofiles
from aiohttp import web
from werkzeug.utils import secure_filename


async def _size(request):
    upload_folder = request.app['config'].get('upload_folder')
    file_searched = request.rel_url.query['file']
    try:
        path_to_file = os.path.join(upload_folder, file_searched)
        file_size = os.path.getsize(path_to_file)
        return web.Response(text=f' {file_searched} size is {file_size} bytes\n\n ')

    except Exception as e:
        print(e)


async def _upload(request):
    upload_folder = request.app['config'].get('upload_folder')
    reader = await request.multipart()
    field = await reader.next()
    file_searched = field.name
    if file_searched == 'file':
        filename = secure_filename(field.filename)
        response = await write_file(upload_folder, filename, field)
        return response


async def write_file(upload_folder, filename, field):
    async with aiofiles.open(os.path.join(upload_folder, filename), 'wb') as infile:
        while True:
            chunk = await field.read_chunk(8192)
            if not chunk:
                break
            await infile.write(chunk)

    return web.Response(text=f'{filename} has been successfully stored\n')


async def _download(request):
    upload_folder = request.app['config'].get('upload_folder')
    file_searched = request.rel_url.query['file']
    try:
        async with aiofiles.open(os.path.join(upload_folder, file_searched), mode='r') as outfile:
            content = await outfile.read()
        return web.Response(text=f'{content}\n\n')


    except Exception as e:
        return web.Response(text='file not found')
