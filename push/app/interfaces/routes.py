from app.interfaces.api import bp
from app.interfaces.pages import pages


def register_routes(app):
    app.register_blueprint(bp, url_prefix="/api")
    app.register_blueprint(pages, url_prefix="/")
