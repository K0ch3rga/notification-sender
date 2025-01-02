from push.app.domain.models import Notification

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

    def get_all(self):
        return Notification.query.all()