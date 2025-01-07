from flask import Blueprint, render_template, request, jsonify, current_app
from app.domain.services import NotificationService
from app.infrastructure.database import db
from app.domain.repositories import NotificationRepository

pages = Blueprint("/", __name__)


@pages.route("/", methods=["GET"])
def main_page():
    # notifications = NotificationRepository.get_by_email("email")
    notifications = NotificationRepository.get_all()
    return render_template("push_service.html", notifications=notifications)


@pages.route("/login", methods=["GET"])
def login():
    return jsonify(status="healthy"), 200
