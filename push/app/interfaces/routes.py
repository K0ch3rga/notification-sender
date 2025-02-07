from app.interfaces.api import api
from app.interfaces.pages import pages


def register_routes(app):
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(pages, url_prefix="/")
