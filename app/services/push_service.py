import requests
from app import db
from app.models import Notification
from app.utils.logger import logger

class PushService:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.api_key = app.config['PUSH_NOTIFICATION_API_KEY']

    def send_push_notification(self, notification):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'recipient': notification.recipient,
            'message': notification.message
        }
        try:
            response = requests.post('https://api.pushnotification.com/send', json=payload, headers=headers)
            response.raise_for_status()
            notification.status = 'sent'
            notification.log = response.text
        except requests.RequestException as e:
            notification.status = 'failed'
            notification.log = str(e)
            notification.attempts += 1
        finally:
            db.session.commit()