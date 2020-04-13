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

    # User
    USER_KEYWORD_LENGTH = 4

    # ø User Settings
    # TODO: Expand
    # → Input
    INPUT_NONE = 0
    INPUT_PIANO = 1
    INPUT_SOLFEGE = 2

    #  → Language
    LANG_ENGLISH = 0
    LANG_GERMAN = 1
    # ...

    # → Darkmode
    THEME_LIGHT = 0
    THEME_DARK = 1

    # ø Default User Settings
    # TODO: Auslagern
    DEFAULT_SETTINGS = {
        'input_type': INPUT_SOLFEGE,
        'language': LANG_ENGLISH,
        'theme': THEME_LIGHT
    }
