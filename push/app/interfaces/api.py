from flask import Blueprint, request, jsonify
from app.infrastructure.database import PostgresNotificationRepository
from app.application.usecases.notification_usecase import NotificationUseCase
from app.infrastructure.database import db

api = Blueprint("api", __name__)

notification_repo = PostgresNotificationRepository(db.session)
notification_use_case = NotificationUseCase(notification_repo)


@api.route("/send", methods=["POST"])
def send_notification():
    data = request.json
    notification_type = data.get("Type")
    address = data.get("Address")
    title = data.get("Title")
    message = data.get("Message")
    notification = notification_use_case.create_notification()
    return (
        jsonify({"message": "Notification sent", "notification_id": notification.id}),
        202,
    )


@api.route("/health", methods=["GET"])
def health():
    return jsonify(status="healthy"), 200
