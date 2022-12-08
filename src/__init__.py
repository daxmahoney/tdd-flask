import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy()


def create_app(script_info=None):
    # instantiate the db
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blue prints
    from src.api.ping import ping_blueprint
    app.regester_blueprint(ping_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app