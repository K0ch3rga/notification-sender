from flask import Flask
from push.app.config import Config
from push.app.infrastructure.database import db
from push.app.infrastructure.kafka_consumer import KafkaConsumer
from push.app.infrastructure.push_service import PushService
from push.app.interfaces.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    kafka_consumer = KafkaConsumer(app)
    push_service = PushService(app)

    with app.app_context():
        register_routes(app)
        db.create_all()

    return app