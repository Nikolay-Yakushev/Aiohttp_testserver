import os

import aiofiles
from aiohttp import web
from werkzeug.utils import secure_filename

from errors_handler import ServerErrorsHandler, \
    ClientErrorHandler, CustomErrorsHandler


async def _size(request):
    upload_folder = request.app['config'].get('upload_folder')
    query = request.rel_url.query

    if query and 'file' in query:

        file_searched = query['file']
        path_to_file = os.path.join(upload_folder, file_searched)

        if not path_to_file:
            return await ServerErrorsHandler.internal_error()

        try:
            file_size = os.path.getsize(path_to_file)
        except CustomErrorsHandler.file_not_found(path_to_file):

            response = await CustomErrorsHandler.file_not_found(path_to_file)
            return response

        return web.json_response({'info': {'filename': f' {file_searched}', 'size': f'{file_size} bytes'}})
    else:
        return await ClientErrorHandler.bad_request(request.rel_url.query)


async def _upload(request):
    upload_folder = request.app['config'].get('upload_folder')
    reader = await request.multipart()

    if not reader:
        return await ClientErrorHandler.bad_request(request.multipart)

    while True:
        field = await reader.next()
        if field is None:
            return await ClientErrorHandler.bad_request(reader)
        if field.name == 'file':
            break

    filename = secure_filename(field.filename)
    response = await save(upload_folder, filename, field)

    return response


async def save(upload_folder, filename, field):
    async with aiofiles.open(os.path.join(upload_folder, filename), 'wb') as infile:
        while True:
            chunk = await field.read_chunk(8192)

            if not chunk:
                break
            await infile.write(chunk)

    return web.json_response({'info': {'filename': f'{filename}', 'status': 'uploaded'}})


async def _download(request):
    upload_folder = request.app['config'].get('upload_folder')
    query = request.rel_url.query

    if query and 'file' in query:
        file_searched = query['file']

        async with aiofiles.open(os.path.join(upload_folder, file_searched), mode='r') as outfile:
            content = await outfile.read()
        return web.Response(text=f'{content}\n\n')

    else:
        return await ClientErrorHandler.bad_request(request.rel_url.query)
