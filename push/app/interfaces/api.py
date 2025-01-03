from flask import Blueprint, request, jsonify, current_app
from app.domain.services import NotificationService
from app.infrastructure.database import db
from app.domain.repositories import NotificationRepository

bp = Blueprint("api", __name__)


@bp.route("/send", methods=["POST"])
def send_notification():
    notification_service = current_app.notification_service
    data = request.json
    notification_type = data.get("Type")
    address = data.get("Address")
    title = data.get("Title")
    message = data.get("Message")
    notification = notification_service.send_notification(
        notification_type, address, title, message
    )
    return (
        jsonify({"message": "Notification sent", "notification_id": notification.id}),
        202,
    )
