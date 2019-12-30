from db import db


class Street(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    houses = db.relationship('House', backref='street')


class House(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    address = db.Column(db.String)
    street_id = db.Column(db.Integer, db.ForeignKey('street.id'))
