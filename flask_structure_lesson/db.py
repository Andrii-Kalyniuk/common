from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

film_studio = db.Table(
    "film_studio",
    db.Column('film_id', db.Integer, db.ForeignKey('films.id')),
    db.Column('studio_id', db.Integer, db.ForeignKey('studios.id'))
)


class Films(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    year = db.Column(db.String)


class Studios(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    films = db.relationship('Films', secondary=film_studio, backref='studios')
