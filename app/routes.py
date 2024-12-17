from flask import Blueprint, request, jsonify
from app import db
from app.models import Notification
from app.services.push_service import PushService

bp = Blueprint('api', __name__)
push_service = PushService()

@bp.route('/send', methods=['POST'])
def send_notification():
    data = request.json
    recipient = data.get('recipient')
    message = data.get('message')
    notification = Notification(recipient=recipient, message=message, status='pending')
    db.session.add(notification)
    db.session.commit()
    push_service.send_push_notification(notification)
    return jsonify({'message': 'Notification sent', 'notification_id': notification.id}), 202