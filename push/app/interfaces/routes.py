from push.app.interfaces.api import bp

def register_routes(app):
    app.register_blueprint(bp, url_prefix='/api')