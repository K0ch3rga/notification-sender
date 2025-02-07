from app.domain.notification import Notification
from app.domain.notification_repository import NotificationRepository


class NotificationUseCase:

    def __init__(self, notification_repository: NotificationRepository):
        self.notification_repository = notification_repository

    def create_notification(self, name: str):
        new_notification = Notification(name=name)  # FIXME
        print(new_notification)
        self.notification_repository.add_notification(new_notification)
