from decouple import config

DEBUG = config("DEBUG")
POSTGRES_URL = f"postgresql://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}@0.0.0.0:5432/{config('POSTGRES_DB')}"

