import unittest
from unittest.mock import patch
from app import create_app, db
from app.models import Notification
from app.services.push_service import PushService

class PushServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        db.create_all()
        self.push_service = PushService(self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @patch('requests.post')
    def test_send_push_notification_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = 'Notification sent successfully'
        notification = Notification(recipient='test@example.com', message='Hello, World!')
        db.session.add(notification)
        db.session.commit()
        self.push_service.send_push_notification(notification)
        self.assertEqual(notification.status, 'sent')
        self.assertEqual(notification.log, 'Notification sent successfully')

    @patch('requests.post')
    def test_send_push_notification_failure(self, mock_post):
        mock_post.side_effect = Exception('Failed to send notification')
        notification = Notification(recipient='test@example.com', message='Hello, World!')
        db.session.add(notification)
        db.session.commit()
        self.push_service.send_push_notification(notification)
        self.assertEqual(notification.status, 'failed')
        self.assertEqual(notification.log, 'Failed to send notification')
        self.assertEqual(notification.attempts, 1)