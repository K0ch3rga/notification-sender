from flask import Flask
from .config import Config
from .interfaces.routes import register_routes
from .infrastructure.database import db, migrate
from .infrastructure.kafka_consumer import KafkaConsumer


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(
        app=app,
        db=db,
    )

    with app.app_context():
        db.create_all()

    register_routes(app)

    with app.app_context():
        KafkaConsumer(app).start_consuming()

    return app
