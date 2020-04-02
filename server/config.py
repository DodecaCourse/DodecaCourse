"""App configuration."""
from dotenv import load_dotenv
import os
import redis
load_dotenv()


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = os.getenv('SECRET_KEY')
    # FLASK_APP = environ.get('FLASK_APP')
    # FLASK_ENV = environ.get('FLASK_ENV')

    # Debug flags
    TESTING = True
    DEBUG = True

    # Flask-Session
    SESSION_TYPE = os.getenv('SESSION_TYPE')
    SESSION_REDIS = redis.from_url(os.getenv('SESSION_REDIS'))
