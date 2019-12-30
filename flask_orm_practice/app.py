from flask import Flask

from config import get_config
from db import db, migrate

from api.school import school_blueprint
from api.students import student_blueprint
from api.teacher import teacher_blueprint
from api.diary import diary_blueprint


def create_app(env="DEFAULT"):
    app = Flask(__name__)
    app.config.from_object(get_config(env))

    db.init(app=app)
    db.create_all()
    migrate.init(app, db)

    app.register_blueprint(school_blueprint)
    app.register_blueprint(student_blueprint)
    app.register_blueprint(teacher_blueprint)
    app.register_blueprint(diary_blueprint)

    return app
