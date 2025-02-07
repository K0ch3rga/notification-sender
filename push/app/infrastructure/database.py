from typing import List, Optional
from app.domain.notification import Notification
from app.domain.notification_repository import NotificationRepository
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class NotificationModel(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    notification_type = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(100), nullable=False)

    def __init__(self, notification_type: str, address: str, title: str, message: str):
        self.notification_type = notification_type
        self.address = address
        self.title = title
        self.message = message

    def __repr__(self) -> str:
        return f"<Notification {self.id}>"


class PostgresNotificationRepository(NotificationRepository):
    def __init__(self, session):
        self.session = session

    def get_notification(self, id: int) -> Optional[Notification]:
        notification_db = self.session.query.get(id)
        return notificationModelToEntity(notification_db)  # FIXME

    def get_user_notifications(self, user_id: int) -> List[Notification]:
        notifications_db = self.session.query().filter_by(address=user_id)
        return [notificationModelToEntity(n) for n in notifications_db]

    def add_notification(self, notification: Notification) -> None:
        db_notification = notificationToModel(notification)
        self.session.add(db_notification)
        self.session.commit()


def notificationToModel(notification: Notification) -> NotificationModel:
    return NotificationModel(
        notification_type=notification.notification_type,
        address=notification.address,
        title=notification.notification_type,
        message=notification.message,
    )


def notificationModelToEntity(notificationModel: NotificationModel) -> Notification:
    return Notification(
        notification_type=notificationModel.notification_type,
        address=notificationModel.address,
        title=notificationModel.notification_type,
        message=notificationModel.message,
    )
