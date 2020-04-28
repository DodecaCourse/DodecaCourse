"""
Copyright 2020 Maximilian Herzog, Hans Olischläger, Valentin Pratz,
Philipp Tepel
This file is part of Dodeca Course.

Dodeca Course is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Dodeca Course is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Dodeca Course.  If not, see <https://www.gnu.org/licenses/>.
"""

# App configuration.
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
    TESTING = (int(os.getenv('TESTING', 0)) == 1)
    DEBUG = (int(os.getenv('DEBUG', 0)) == 1)

    # Flask-Session
    SESSION_TYPE = os.getenv('SESSION_TYPE')
    SESSION_REDIS = redis.from_url(os.getenv('SESSION_REDIS'))
    SESSION_COOKIE_SECURE = (int(os.getenv('SESSION_COOKIE_SECURE', 1)) == 1)
    # User
    USER_KEYWORD_LENGTH = int(os.getenv('USER_KEYWORD_LENGTH', 4))
    FRONTEND_SERVER = os.getenv('FRONTEND_SERVER', 'http://localhost:8080')

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
    DEFAULT_SETTINGS = {
        'input_type': INPUT_SOLFEGE,
        'language': LANG_ENGLISH,
        'theme': THEME_LIGHT
    }
