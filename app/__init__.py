from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.utils.kafka_consumer import KafkaConsumer
from app.services.push_service import PushService

db = SQLAlchemy()
kafka_consumer = KafkaConsumer()
push_service = PushService()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    kafka_consumer.init_app(app)
    push_service.init_app(app)

    with app.app_context():
        from app import routes
        db.create_all()

    return app