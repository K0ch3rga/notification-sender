from flask import Blueprint, request, jsonify
from push.app.domain.services import NotificationService
from push.app.infrastructure.database import db
from push.app.infrastructure.push_service import PushService
from push.app.domain.repositories import NotificationRepository

bp = Blueprint('api', __name__)

notification_repository = NotificationRepository(db)
push_service = PushService(None)
notification_service = NotificationService(notification_repository, push_service)

@bp.route('/send', methods=['POST'])
def send_notification():
    data = request.json
    notification_type = data.get('Type')
    address = data.get('Address')
    title = data.get('Title')
    message = data.get('Message')
    notification = notification_service.send_notification(notification_type, address, title, message)
    return jsonify({'message': 'Notification sent', 'notification_id': notification.id}), 202