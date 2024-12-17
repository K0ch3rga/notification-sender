import unittest
from app import create_app, db
from app.models import Notification

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_send_notification(self):
        response = self.client.post('/send', json={'recipient': 'test@example.com', 'message': 'Hello, World!'})
        self.assertEqual(response.status_code, 202)
        notification = Notification.query.first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.recipient, 'test@example.com')
        self.assertEqual(notification.message, 'Hello, World!')
        self.assertEqual(notification.status, 'pending')