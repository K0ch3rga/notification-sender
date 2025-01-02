from push.app import create_app
from flask import render_template
from push.app.infrastructure.database import db
from push.app.infrastructure.push_service import PushService
from push.app.domain.repositories import NotificationRepository
from push.app.domain.services import NotificationService
from push.app.interfaces.api import bp

app = create_app()

push_service = PushService(app)
notification_repository = NotificationRepository(db)
notification_service = NotificationService(notification_repository, push_service)

@app.context_processor
def inject_notification_service():
    return dict(notification_service=notification_service)

app.register_blueprint(bp)

@app.route('/push')
def push():
    return render_template('push_service.html')

if __name__ == '__main__':
    app.run(debug=True)