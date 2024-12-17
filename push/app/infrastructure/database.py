from flask_sqlalchemy import SQLAlchemy
from push.app.domain.models import Notification

db = SQLAlchemy(model_class=Notification)