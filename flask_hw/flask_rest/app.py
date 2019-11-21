from flask import Flask

from api.room import rooms_bp
from db import db, migrate, fill_up_db
from config import get_config


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config("TEST"))
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(rooms_bp)
    with app.app_context():
        db.create_all()
        fill_up_db()
    return app


if __name__ == "__main__":
    create_app().run()
