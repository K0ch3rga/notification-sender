from flask import Blueprint, render_template, jsonify
from app.infrastructure.database import PostgresNotificationRepository, db
from app.application.usecases.notification_usecase import NotificationUseCase
from app import Config


pages = Blueprint("/", __name__)
notification_repo = PostgresNotificationRepository(db.session)
notification_use_case = NotificationUseCase(notification_repo)


@pages.route("/", methods=["GET"])
def main_page():
    # notifications = notification_repo.get_user_notifications(1)
    return render_template(
        "index.html",
        # notifications=notifications,
        # notification_use_case=notification_use_case,
    )


@pages.route("/login", methods=["GET"])
def login():
    return jsonify(status="healthy"), 200
