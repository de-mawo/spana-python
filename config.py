"""Config Class"""

from os import environ, path
from dotenv import load_dotenv
import redis

from app.constants import BASE_DIR

# load_dotenv()

load_dotenv(path.join(BASE_DIR, ".env"))  # Load environment variables from .env file


class Config:
    """Class that defines Environmental Variables for the App"""

    # Flask-SQLAlchemy

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URI")

    # Flask-Session
    REDIS_URI = environ.get("REDIS_URI")
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.from_url(environ.get("REDIS_URI"))
