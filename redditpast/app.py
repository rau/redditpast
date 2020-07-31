import os, sys
from flask import Flask
from flask_talisman import Talisman
from flask_seasurf import SeaSurf
from dotenv import load_dotenv

load_dotenv()


csrf = SeaSurf()
talisman = Talisman()

def create_app():
    app = Flask(__name__)
    set_config(app)
    init_apps(app)
    with app.app_context():
        register_blueprints(app)
        return app

def set_config(app):
    from redditpast.config import Config
    app.config.from_object(Config)

def init_apps(app):
    csrf.init_app(app)
    talisman.init_app(app, content_security_policy=get_csp())

def get_csp():
    return {
        'default-src': [
            '\'self\''
        ],
        'script-src': [
            '\'self\''
        ]
    }


def register_blueprints(app):
    from redditpast.home import home

    app.register_blueprint(home.home_bp)
