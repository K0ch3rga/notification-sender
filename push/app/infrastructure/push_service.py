import requests
from app.infrastructure.database import db
from app.domain.notification import Notification


class PushService:

    def __init__(self, gateway_url: str):
        self.gateway_url = gateway_url

    def send_push_notification(self, notification: Notification):
        headers = {
            "Content-Type": "application/json",
        }
        payload = {
            "address": notification.address,
            "title": notification.title,
            "message": notification.message,
        }
        try:
            response = requests.post(self.gateway_url, json=payload, headers=headers)
            response.raise_for_status()
            notification.status = "sent"  # FIXME
            notification.log = response.text
        except requests.RequestException as e:
            notification.status = "failed"
            notification.log = str(e)
            notification.attempts += 1
        finally:
            db.session.commit()
