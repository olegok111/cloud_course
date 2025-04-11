import os

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile('config.py', silent=True)

    from . import db
    db.init_app(app)

    from . import todolist
    app.register_blueprint(todolist.bp)
    app.add_url_rule("/", endpoint="index")

    return app
