from typing import List
from abc import ABC, abstractmethod
from .notification import Notification


class NotificationRepository(ABC):
    @abstractmethod
    def get_notification(self, id: int) -> Notification:
        pass

    @abstractmethod
    def get_user_notifications(self, user_id: int) -> List[Notification]:
        pass

    @abstractmethod
    def add_notification(self, notification: Notification) -> None:
        pass
