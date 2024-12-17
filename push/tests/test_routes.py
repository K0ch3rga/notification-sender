import unittest
from push.app import create_app
from push.app.domain.models import Notification
from push.app.domain.services import NotificationService
from push.app.infrastructure.database import db
from push.app.infrastructure.push_service import PushService
from push.app.domain.repositories import NotificationRepository

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:5432/test_notifications'
        self.client = self.app.test_client()
        db.create_all()
        self.notification_repository = NotificationRepository(db)
        self.push_service = PushService(self.app)
        self.notification_service = NotificationService(self.notification_repository, self.push_service)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_send_notification(self):
        data = {
            'Type': 'push',
            'Address': 'test@example.com',
            'Title': 'Test Title',
            'Message': 'Hello, World!'
        }
        response = self.client.post('/api/send', json=data)
        self.assertEqual(response.status_code, 202)
        notification = Notification.query.first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.notification_type, 'push')
        self.assertEqual(notification.address, 'test@example.com')
        self.assertEqual(notification.title, 'Test Title')
        self.assertEqual(notification.message, 'Hello, World!')
        self.assertEqual(notification.status, 'pending')