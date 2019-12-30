from flask import Flask
from config import get_config
from api.films import films_blueprint
from api.studios import studios_blueprint

from db import db, migrate


def create_app(env="DEV"):
    app = Flask(__name__)
    app.config.from_object(get_config(env))
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(films_blueprint)
    app.register_blueprint(studios_blueprint)
    db.create_all(app=app)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
