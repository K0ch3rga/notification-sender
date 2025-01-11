from push.app import create_app
from flask import Flask, request, redirect, url_for, session, render_template_string, render_template
from flask_session import Session
from push.app.infrastructure.database import db
from push.app.infrastructure.push_service import PushService
from push.app.domain.repositories import NotificationRepository
from push.app.domain.services import NotificationService
from push.app.interfaces.api import bp

app = create_app()

push_service = PushService(app)
notification_repository = NotificationRepository(db)
notification_service = NotificationService(notification_repository, push_service)

Session(app)

@app.context_processor
def inject_notification_service():
    return dict(notification_service=notification_service)

app.register_blueprint(bp)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = notification_repository.get_by_address(email)
        if user:
            session['email'] = user.address
            return redirect(url_for('push'))
        else:
            return "Email not found", 401
    return render_template('login.html')


@app.route('/push')
def push():
    if 'email' in session:
        notifications = notification_repository.get_all()
        return render_template('push_service.html', notifications=notifications)
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)