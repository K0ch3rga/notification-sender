from app.domain.models import Notification


class NotificationService:
    def __init__(self, notification_repository, push_service):
        self.notification_repository = notification_repository
        self.push_service = push_service

    def send_notification(self, notification_type, address, title, message):
        notification = Notification(
            notification_type=notification_type,
            address=address,
            title=title,
            message=message,
        )
        self.notification_repository.add(notification)
        self.push_service.send_push_notification(notification)
        return notification
