from flask import Flask
from app.config import Config
from app.infrastructure.database import db
from app.infrastructure.kafka_consumer import KafkaConsumer
from app.infrastructure.push_service import PushService
from app.interfaces.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    kafka_consumer = KafkaConsumer(app)
    push_service = PushService(app)

    with app.app_context():
        from app.domain.models import Notification

        register_routes(app)
        db.create_all()

    return app
