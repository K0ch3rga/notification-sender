import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///notifications.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
    KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'push_notifications')
    PUSH_NOTIFICATION_API_KEY = os.getenv('PUSH_NOTIFICATION_API_KEY', 'your_api_key_here')