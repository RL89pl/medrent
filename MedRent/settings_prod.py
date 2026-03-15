import os
from .settings import *

# ── SECURITY ──────────────────────────────────────────────────────────────────
SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

# ── DATABASE (persistent volume) ───────────────────────────────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "data" / "db" / "db.sqlite3",
    }
}

# ── STATIC & MEDIA ─────────────────────────────────────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ── HTTPS / PROXY ──────────────────────────────────────────────────────────────
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    f"https://{h}" for h in os.environ.get("ALLOWED_HOSTS", "").split(",") if h
]

# ── EMAILLABS ──────────────────────────────────────────────────────────────────
EMAILLABS_SMTP = os.environ.get("EMAILLABS_SMTP", "")
EMAILLABS_APP_KEY = os.environ.get("EMAILLABS_APP_KEY", "")
EMAILLABS_SECRET_KEY = os.environ.get("EMAILLABS_SECRET_KEY", "")
