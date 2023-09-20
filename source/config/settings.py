from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = config("DEBUG")
POSTGRES_URL = f"postgresql://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}@0.0.0.0:5432/{config('POSTGRES_DB')}"
