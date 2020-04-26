import yaml
from aiohttp import web

from .app import create_app

routes = web.RouteTableDef()

path = './app/config.yaml'
with open(path, 'r') as config:
    data = yaml.load(config, Loader=yaml.FullLoader)
    upload_folder = data['upload_folder']

from . import app_routes, app_logic
