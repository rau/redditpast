import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    FLASK_APP = environ.get("FLASK_APP")

    TEMPLATES_AUTO_RELOAD = True
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
