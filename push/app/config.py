import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_USER = os.getenv("PUSH_POSTGRES_USER")
    DB_PASS = os.getenv("PUSH_POSTGRES_PASSWORD")
    DB_HOST = os.getenv("PUSH_POSTGRES_HOST")
    DB_NAME = os.getenv("PUSH_POSTGRES_DB")
    sqlite_database = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "push_notifications")
    PUSH_NOTIFICATION_API_KEY = os.getenv(
        "PUSH_NOTIFICATION_API_KEY", "your_api_key_here"
    )
