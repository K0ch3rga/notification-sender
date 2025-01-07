from app.domain.models import Notification


class NotificationRepository:
    def __init__(self, db):
        self.db = db

    def add(self, notification):
        self.db.session.add(notification)
        self.db.session.commit()

    def update(self, notification):
        self.db.session.commit()

    def get_by_id(self, notification_id):
        return Notification.query.get(notification_id)

    @staticmethod
    def get_all():
        return Notification.query.all()

    @staticmethod
    def get_by_email(email):
        return Notification.query.get(email)
