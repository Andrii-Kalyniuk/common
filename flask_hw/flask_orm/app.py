from flask import Flask

from api.health import health_bp
from api.room import rooms_bp
from api.staff import staff_bp
from api.tenant import tenants_bp

from db import db, migrate, fill_up_db
from config import get_config


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config("TEST"))
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(rooms_bp)
    app.register_blueprint(tenants_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(health_bp)
    with app.app_context():
        db.create_all()
        fill_up_db()
    return app


if __name__ == "__main__":
    create_app().run()
