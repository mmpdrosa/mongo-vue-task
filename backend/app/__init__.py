from flask import Flask

from .models import init_app
from .routes import api


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    init_app(app)

    app.register_blueprint(api, url_prefix="/api")

    return app