import yaml
from aiohttp import web


def create_app(path: str):
    """Create an application."""
    app = web.Application()

    from .app_routes import routes
    # from . import upload_folder
    with open(path, 'r') as conf_file:
        config = yaml.safe_load(conf_file)
        app['config'] = config

    app.add_routes(routes)
    return app
