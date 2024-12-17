from app import db

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(128), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(32), nullable=False)
    attempts = db.Column(db.Integer, default=0)
    log = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Notification {self.id}>'