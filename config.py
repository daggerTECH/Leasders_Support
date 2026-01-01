import os

class Config:
    SECRET_KEY = os.environ.get("0b1bba2bef32b8faf0a404daf5378bd448ed04bf552642f91ef1231ff42b4687")

    # Gmail SMTP
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME = "danny.villanueva@leaders.st"
    MAIL_PASSWORD = "wsut sfvc ctja yofz"

    # SQLAlchemy Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("mysql://root:yxpVkOzJCBXpybNYXFdmQXPvULefozpd@nozomi.proxy.rlwy.net:52431/railway")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SLACK NOTIFIER
    SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"
