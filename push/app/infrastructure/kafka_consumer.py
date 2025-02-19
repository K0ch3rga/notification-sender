import json
import kafka
from app.domain.notification import Notification
from app.infrastructure.database import PostgresNotificationRepository, db
from .logger import logger
import logging


class KafkaConsumer:
    def __init__(self, app):
        self.app = app
        self.consumer = kafka.KafkaConsumer(
            app.config["KAFKA_TOPIC"],
            bootstrap_servers=app.config["KAFKA_BOOTSTRAP_SERVERS"],
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="push_notification_group",
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        )
        with app.app_context():
            self.notification_repository = PostgresNotificationRepository(db.session)

    def start_consuming(self):
        with self.app.app_context():
            try:
                for message in self.consumer:
                    data = message.value
                    logger.log(level=logging.INFO, msg=message)
                    self.notification_repository.add_notification(
                        notification=Notification(
                            message=data.get("message"),
                            address=data.get("address"),
                            notification_type=data.get("type"),
                            title=data.get("title"),
                        ),
                    )
            except Exception as e:
                logger.error(f"Error processing Kafka message: {str(e)}")
            finally:
                self.consumer.close()
