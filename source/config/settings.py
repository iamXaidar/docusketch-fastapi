from decouple import config
from pathlib import Path

# WEB
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = config("DEBUG")

# DB
POSTGRES_URL = f"postgresql://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}@0.0.0.0:5432/{config('POSTGRES_DB')}"

# LOGGING
logconfig = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "[%(levelname)s] [%(asctime)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"

        },
    },
    "handlers": {
        "file": {
            "formatter": "default",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{BASE_DIR}/logs/app.log",
            "maxBytes": 100000,
            "backupCount": 3
        },
        "console": {
            "formatter": "default",
            "class": "logging.StreamHandler",
        },

    },
    "loggers": {
        "file-logger": {"handlers": ["file"], "level": "DEBUG"},
    },  "console-logger": {"handlers": ["console"], "level": "DEBUG"}
}
