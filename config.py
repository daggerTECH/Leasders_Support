import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")

    # Gmail SMTP
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    EMAIL_USERNAME = "primeadsdigital@gmail.com"
    EMAIL_PASSWORD = "mwwe grms mazj yqeg"

    # SQLAlchemy Database
    SQLALCHEMY_DATABASE_URI = os.getenv("mysql://root:yxpVkOzJCBXpybNYXFdmQXPvULefozpd@nozomi.proxy.rlwy.net:52431/railway")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SLACK NOTIFIER
    SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"




