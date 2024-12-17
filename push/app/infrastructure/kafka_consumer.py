from kafka import KafkaConsumer
from push.app.domain.repositories import NotificationRepository
from push.app.infrastructure.push_service import PushService
from push.app.domain.services import NotificationService
from push.app.infrastructure.database import db
import json

class KafkaConsumer:
    def __init__(self, app):
        self.consumer = KafkaConsumer(
            app.config['KAFKA_TOPIC'],
            bootstrap_servers=app.config['KAFKA_BOOTSTRAP_SERVERS'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='push_notification_group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        self.notification_repository = NotificationRepository(db)
        self.push_service = PushService(app)
        self.notification_service = NotificationService(self.notification_repository, self.push_service)

    def start_consuming(self):
        for message in self.consumer:
            data = message.value
            notification_type = data.get('Type')
            address = data.get('Address')
            title = data.get('Title')
            message = data.get('Message')
            self.notification_service.send_notification(notification_type, address, title, message)