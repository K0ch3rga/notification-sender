from kafka import KafkaConsumer
from app import db
from app.models import Notification
from app.services.push_service import PushService

class KafkaConsumer:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.consumer = KafkaConsumer(
            app.config['KAFKA_TOPIC'],
            bootstrap_servers=app.config['KAFKA_BOOTSTRAP_SERVERS'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='push_notification_group',
            value_deserializer=lambda x: x.decode('utf-8')
        )
        self.push_service = PushService(app)

    def start_consuming(self):
        for message in self.consumer:
            data = message.value
            recipient, message = data.split('|')
            notification = Notification(recipient=recipient, message=message, status='pending')
            db.session.add(notification)
            db.session.commit()
            self.push_service.send_push_notification(notification)