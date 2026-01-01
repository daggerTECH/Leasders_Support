import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Gmail SMTP
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME = "MAIL_USERNAME"
    MAIL_PASSWORD = "MAIL_PASSWORD"

    # SQLAlchemy Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SLACK NOTIFIER
    SLACK_WEBHOOK_URL = "SLACK_WEBHOOK_URL"
