import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Stripe FastAPI Demo"
    PROJECT_VERSION: str = "1.0.0"
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER")
    MYSQL_USERNAME: str = os.getenv("MYSQL_USERNAME")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB: str = os.getenv("MYSQL_DB")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT")
    BASE_URL: str = os.getenv("BASE_URL")
    STRIPE_API_KEY: str = os.getenv("STRIPE_SECRET_KEY")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    MYSQL_CONNECTION: str = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"


settings = Settings()
