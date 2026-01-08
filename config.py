import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")

    # ============================
    # EMAIL (SMTP)
    # ============================
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    # ============================
    # DATABASE
    # ============================
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ============================
    # SLACK
    # ============================
    SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

    # ============================
    # FILE UPLOADS
    # ============================
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB per file
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

    # Relative to Flask static folder → app/static/uploads
    UPLOAD_FOLDER = "uploads"
