import requests
from app.infrastructure.database import db


class PushService:
    def __init__(self, app):
        self.api_key = app.config["PUSH_NOTIFICATION_API_KEY"]

    def send_push_notification(self, notification):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "recipient": notification.address,
            "title": notification.title,
            "message": notification.message,
        }
        try:
            response = requests.post(
                "https://api.pushnotification.com/send", json=payload, headers=headers
            )
            response.raise_for_status()
            notification.status = "sent"
            notification.log = response.text
        except requests.RequestException as e:
            notification.status = "failed"
            notification.log = str(e)
            notification.attempts += 1
        finally:
            db.session.commit()
