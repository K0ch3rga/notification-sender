import unittest
from unittest.mock import patch
from push.app import create_app
from push.app.domain.models import Notification
from push.app.domain.services import NotificationService
from push.app.infrastructure.database import db
from push.app.infrastructure.push_service import PushService
from push.app.domain.repositories import NotificationRepository

class PushServiceTestCase(unittest.TestCase):
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

    @patch('requests.post')
    def test_send_push_notification_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = 'Notification sent successfully'
        notification = Notification(notification_type='push', address='test@example.com', title='Test Title', message='Hello, World!')
        db.session.add(notification)
        db.session.commit()
        self.push_service.send_push_notification(notification)
        self.assertEqual(notification.status, 'sent')
        self.assertEqual(notification.log, 'Notification sent successfully')

    @patch('requests.post')
    def test_send_push_notification_failure(self, mock_post):
        mock_post.side_effect = Exception('Failed to send notification')
        notification = Notification(notification_type='push', address='test@example.com', title='Test Title', message='Hello, World!')
        db.session.add(notification)
        db.session.commit()
        self.push_service.send_push_notification(notification)
        self.assertEqual(notification.status, 'failed')
        self.assertEqual(notification.log, 'Failed to send notification')
        self.assertEqual(notification.attempts, 1)