from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class School(db.Model):
    pass


class Student(db.Model):
    pass


class Teacher(db.Model):
    pass


class Diary(db.Model):
    pass
