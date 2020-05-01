import argparse

import aiohttp
from aiohttp import web
from app import app_init

parser = argparse.ArgumentParser('description= aiohttp sever')

parser.add_argument('--host', help="for example 127.0.0.1", type=str, default="0.0.0.0")
parser.add_argument('--port', help="for example 8080", type=int, default=8080)
parser.add_argument("--config", type=str, help="Path to configuration file",
                    default='/home/server/app/config.yaml')

args = parser.parse_args()
app = app_init.create_app(args.config)

if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)
